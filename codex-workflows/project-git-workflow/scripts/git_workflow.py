"""Bind one chat to a checkout and guard scoped local commits."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys


def git(root, *args):
    result = subprocess.run(
        ['git', '-c', f'safe.directory={root.as_posix()}', '-C', str(root), *args],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode:
        raise ValueError(result.stderr.decode('utf-8', 'replace').strip())
    return result.stdout


def text(root, *args):
    return git(root, *args).decode('utf-8', 'surrogateescape').strip()


def staged(root):
    return git(root, 'diff', '--cached', '--no-renames', '--name-only', '-z').decode(
        'utf-8', 'surrogateescape').split('\0')[:-1]


def state_path(root, key):
    common = Path(text(root, 'rev-parse', '--path-format=absolute', '--git-common-dir'))
    return common / 'codex-chat-bindings' / (hashlib.sha256(key.encode()).hexdigest() + '.json')


def save(path, state):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(state, ensure_ascii=True, indent=2), encoding='utf-8')
    os.replace(temporary, path)


def validate(root, state, head=True):
    if root != Path(state['checkout']).resolve():
        raise ValueError('Checkout differs from chat binding')
    if Path(text(root, 'rev-parse', '--show-toplevel')).resolve() != root:
        raise ValueError('Expected repository-root checkout')
    if text(root, 'symbolic-ref', '--short', 'HEAD') != state['branch']:
        raise ValueError('Branch differs from chat binding')
    if head and text(root, 'rev-parse', 'HEAD') != state['head']:
        raise ValueError('HEAD changed outside workflow; inspect before refresh')
    project = Path(state['project'])
    if not project.is_dir() or project.resolve() != project or not project.is_relative_to(root):
        raise ValueError('Project scope missing or redirected')


def run(args):
    root = Path(args.checkout).resolve()
    path = state_path(root, args.chat_key)
    state = json.loads(path.read_text(encoding='utf-8')) if path.exists() else None
    if args.command == 'bind':
        project = Path(args.project).absolute()
        candidate = dict(checkout=str(root), project=str(project), branch=args.branch,
                         head=text(root, 'rev-parse', 'HEAD'), staged_baseline=staged(root))
        validate(root, candidate)
        if state:
            if any(state[key] != candidate[key] for key in ('checkout', 'project', 'branch')):
                raise ValueError('Existing chat binding cannot be reassigned')
            validate(root, state, head=not args.refresh_head)
            if not args.refresh_head:
                print('PASS: existing binding reused')
                return
        for other in path.parent.glob('*.json'):
            if other == path:
                continue
            owner = json.loads(other.read_text(encoding='utf-8'))
            if Path(owner['checkout']).resolve() == root or owner['branch'] == args.branch:
                raise ValueError('Checkout or branch already belongs to another chat')
        save(path, candidate)
        print('PASS: binding saved; no branch created')
        return
    if state is None:
        raise ValueError('No chat binding; read-only check did not create one')
    validate(root, state)
    if args.command == 'check':
        print('PASS: checkout, scope, branch and HEAD match')
        return
    if git(root, 'ls-files', '-u'):
        raise ValueError('Unresolved index conflicts')
    files = []
    project = Path(state['project'])
    for name in args.file:
        relative = Path(name)
        target = root / relative
        if relative.is_absolute() or '..' in relative.parts or not relative.parts:
            raise ValueError(f'Expected literal repository-relative file: {name}')
        if not target.resolve().is_relative_to(project):
            raise ValueError(f'File outside project scope: {name}')
        for component in [target, *target.parents]:
            if component == root:
                break
            if component.is_symlink() or component.resolve() != component:
                raise ValueError(f'Redirected file path: {name}')
        if target.is_dir():
            raise ValueError(f'Explicit files required, not directories: {name}')
        files.append(relative.as_posix())
    normalize = (lambda name: name.casefold()) if os.name == 'nt' else (lambda name: name)
    if {normalize(name) for name in files} & {normalize(name) for name in state['staged_baseline']}:
        raise ValueError('Commit overlaps pre-existing staged paths')
    if {normalize(name) for name in files} - {normalize(name) for name in staged(root)}:
        raise ValueError('Every commit path must have an explicitly staged change')
    literal = [f':(literal){name}' for name in files]
    if git(root, 'diff', '--name-only', '-z', '--', *literal):
        raise ValueError('Worktree differs from verified staged snapshot')
    if not git(root, 'diff', '--cached', '--name-only', '-z', '--', *literal):
        raise ValueError('No staged changes in commit scope')
    git(root, '-c', 'core.whitespace=blank-at-eol,blank-at-eof,space-before-tab,cr-at-eol',
        'diff', '--cached', '--check', '--', *literal)
    validate(root, state)
    print(git(root, 'commit', '--only', '-m', args.message, '--', *literal).decode('utf-8', 'replace'))
    state['head'] = text(root, 'rev-parse', 'HEAD')
    state['staged_baseline'] = staged(root)
    save(path, state)
    print(f"COMMITTED_LOCAL: {state['head']}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    for command in ('bind', 'check', 'commit'):
        item = sub.add_parser(command)
        item.add_argument('--checkout', required=True)
        item.add_argument('--chat-key', required=True)
        if command == 'bind':
            item.add_argument('--project', required=True)
            item.add_argument('--branch', required=True)
            item.add_argument('--refresh-head', action='store_true')
        if command == 'commit':
            item.add_argument('--file', action='append', required=True)
            item.add_argument('--message', required=True)
    try:
        run(parser.parse_args())
        return 0
    except (ValueError, OSError, KeyError) as error:
        print(f'BLOCKED: {error}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
