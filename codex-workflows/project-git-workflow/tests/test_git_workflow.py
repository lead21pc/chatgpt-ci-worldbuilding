import importlib.util
from pathlib import Path
import tempfile
import unittest
from types import SimpleNamespace

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts' / 'git_workflow.py'
SPEC = importlib.util.spec_from_file_location('workflow', SCRIPT)
workflow = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(workflow)


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.project = self.root / 'project'
        self.project.mkdir()
        self.git('init', '-b', 'work')
        self.git('config', 'user.name', 'Workflow Test')
        self.git('config', 'user.email', 'test@example.invalid')
        self.write('project/base.txt', 'base\n')
        self.write('other.txt', 'other\n')
        self.git('add', '.')
        self.git('commit', '-m', 'baseline')

    def git(self, *args):
        return workflow.git(self.root, *args)

    def write(self, name, content):
        target = self.root / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding='utf-8')

    def call(self, command, **kwargs):
        options = dict(command=command, checkout=str(self.root), chat_key='chat-a',
                       project=str(self.project), branch='work', refresh_head=False)
        options.update(kwargs)
        return workflow.run(SimpleNamespace(**options))

    def task_file(self):
        self.write('project/new [file].txt', 'new\n')
        self.git('add', '--', ':(literal)project/new [file].txt')

    def test_reuse_across_commits_creates_no_branch(self):
        self.call('bind')
        branches = self.git('branch', '--list')
        for number in range(2):
            name = f'project/task{number}.txt'
            self.write(name, 'task\n')
            self.git('add', name)
            self.call('commit', file=[name], message='checkpoint')
            self.call('bind')
            self.call('check')
        self.assertEqual(branches, self.git('branch', '--list'))

    def test_rename_tracks_both_endpoints(self):
        self.call('bind')
        self.git('mv', 'project/base.txt', 'project/renamed.txt')
        self.assertEqual({'project/base.txt', 'project/renamed.txt'},
                         set(workflow.staged(self.root)))
        self.call('commit', file=['project/base.txt', 'project/renamed.txt'],
                  message='rename checkpoint')
        self.assertEqual(b'', self.git('status', '--porcelain'))
        self.call('check')

    def test_wrong_branch_blocks_commit(self):
        self.call('bind')
        self.git('switch', '-c', 'another')
        self.task_file()
        before = self.git('rev-parse', 'HEAD')
        with self.assertRaisesRegex(ValueError, 'Branch differs'):
            self.call('commit', file=['project/new [file].txt'], message='blocked')
        self.assertEqual(before, self.git('rev-parse', 'HEAD'))

    def test_preexisting_staging_survives_scoped_commit(self):
        self.write('other.txt', 'staged user edit\n')
        self.git('add', 'other.txt')
        before = self.git('diff', '--cached', '--binary')
        self.call('bind')
        self.task_file()
        self.call('commit', file=['project/new [file].txt'], message='task')
        self.assertEqual(before, self.git('diff', '--cached', '--binary'))
        self.assertEqual(b'project/new [file].txt\n',
                         self.git('diff-tree', '--no-commit-id', '--name-only', '-r', 'HEAD'))

    def test_baseline_path_overlap_blocked(self):
        self.write('project/base.txt', 'user edit\n')
        self.git('add', 'project/base.txt')
        self.call('bind')
        with self.assertRaisesRegex(ValueError, 'pre-existing staged'):
            self.call('commit', file=['project/base.txt'], message='blocked')

    def test_scope_blocks_other_project(self):
        self.call('bind')
        self.write('other.txt', 'other edit\n')
        self.git('add', 'other.txt')
        with self.assertRaisesRegex(ValueError, 'outside project'):
            self.call('commit', file=['other.txt'], message='blocked')

    def test_unverified_worktree_edit_blocked(self):
        self.call('bind')
        self.task_file()
        self.write('project/new [file].txt', 'changed after stage\n')
        with self.assertRaisesRegex(ValueError, 'staged snapshot'):
            self.call('commit', file=['project/new [file].txt'], message='blocked')

    def test_readonly_check_does_not_create_state(self):
        before = self.git('status', '--porcelain')
        with self.assertRaisesRegex(ValueError, 'No chat binding'):
            self.call('check')
        self.assertFalse(workflow.state_path(self.root, 'chat-a').parent.exists())
        self.assertEqual(before, self.git('status', '--porcelain'))

    def test_other_chat_cannot_claim_same_checkout(self):
        self.call('bind')
        with self.assertRaisesRegex(ValueError, 'another chat'):
            self.call('bind', chat_key='chat-b')

    def test_external_head_requires_explicit_refresh(self):
        self.call('bind')
        self.write('project/base.txt', 'external change\n')
        self.git('add', 'project/base.txt')
        self.git('commit', '-m', 'external')
        with self.assertRaisesRegex(ValueError, 'HEAD changed'):
            self.call('check')
        self.call('bind', refresh_head=True)
        self.call('check')

    def test_binding_cannot_change_project(self):
        self.call('bind')
        with self.assertRaisesRegex(ValueError, 'cannot be reassigned'):
            self.call('bind', project=str(self.root))

    def test_unstaged_extra_path_blocked(self):
        self.call('bind')
        self.task_file()
        self.write('project/unstaged.txt', 'not verified\n')
        with self.assertRaisesRegex(ValueError, 'explicitly staged'):
            self.call('commit', file=['project/new [file].txt', 'project/unstaged.txt'],
                      message='blocked')

    @unittest.skipUnless(workflow.os.name == 'nt', 'Windows path comparison')
    def test_case_alias_cannot_bypass_baseline(self):
        self.write('project/base.txt', 'user edit\n')
        self.git('add', 'project/base.txt')
        self.call('bind')
        with self.assertRaisesRegex(ValueError, 'pre-existing staged'):
            self.call('commit', file=['PROJECT/BASE.TXT'], message='blocked')

    def test_different_checkout_blocked(self):
        self.call('bind')
        checkout = self.root.parent / (self.root.name + '-worktree')
        self.git('worktree', 'add', '-b', 'second', str(checkout))
        try:
            with self.assertRaisesRegex(ValueError, 'Checkout differs'):
                self.call('check', checkout=str(checkout))
        finally:
            self.git('worktree', 'remove', str(checkout))


if __name__ == '__main__':
    unittest.main()
