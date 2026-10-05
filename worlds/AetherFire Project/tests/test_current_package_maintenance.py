"""Disposable-copy tests: python -B -m unittest discover -s tests -v."""

import hashlib
import importlib.util
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


PROJECT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('maintenance', PROJECT / 'build_consolidation.py')
tool = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tool)


class MaintenanceTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='af-package-')
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / 'checkout with spaces' / 'AetherFire Project'
        self.root.mkdir(parents=True)
        for name in tool.CURRENT_FILES + (tool.MANIFEST, 'build_consolidation.py'):
            (self.root / name).write_bytes((PROJECT / name).read_bytes())

    def snapshot(self):
        return {p.relative_to(self.root).as_posix(): p.read_bytes()
                for p in self.root.rglob('*') if p.is_file()}

    def run_cli(self, *args):
        return subprocess.run([sys.executable, '-B', str(self.root / 'build_consolidation.py'), *args],
                              cwd=self.root.parent.parent, capture_output=True, text=True)

    def sync(self):
        result = self.run_cli('--write')
        self.assertEqual(result.returncode, 0, result.stderr)

    def rejected_without_writes(self):
        before = self.snapshot()
        for args in ((), ('--check',), ('--write',)):
            result = self.run_cli(*args)
            self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
            self.assertEqual(before, self.snapshot())

    def test_no_lore_writes_header_survival_and_idempotence(self):
        before = {name: (self.root / name).read_bytes() for name in tool.CURRENT_FILES[1:]}
        hashes = {name: hashlib.sha256(data).hexdigest() for name, data in before.items()}
        self.sync()
        for number, name in enumerate(tool.MODULE_FILES, 1):
            self.assertEqual(tool.header((self.root / name).read_bytes(), name)['Module ID'],
                             f'AFM-{number:03d}')
        for name, data in before.items():
            self.assertEqual(data, (self.root / name).read_bytes())
            self.assertEqual(hashes[name], hashlib.sha256((self.root / name).read_bytes()).hexdigest())
        snapshot = self.snapshot()
        self.sync()
        self.assertEqual(snapshot, self.snapshot())

    def test_catalog_manifest_and_read_only_default(self):
        self.sync()
        before = self.snapshot()
        self.assertEqual(self.run_cli().returncode, 0)
        self.assertEqual(self.run_cli('--check').returncode, 0)
        self.assertEqual(before, self.snapshot())
        _, _, _, catalog = tool.region(before[tool.INDEX], tool.CATALOG)
        entries = tool.rows(catalog,
                            '| Module ID | Current source path (relative to AetherFire Project/) |',
                            tool.ACCEPTED)
        self.assertEqual(entries, tool.ACCEPTED)
        _, _, _, block = tool.region(before[tool.MANIFEST], tool.HASHES)
        hashes = tool.rows(block, '| File | SHA-256 |', tool.CURRENT_FILES)
        for name in tool.CURRENT_FILES:
            self.assertEqual(hashes[name], hashlib.sha256(before[name]).hexdigest().upper())
        self.assertNotIn(tool.MANIFEST, hashes)

    def test_politics_admission_and_previous_schema_bootstrap(self):
        name = tool.ACCEPTED['AFM-011']
        self.assertEqual(name, '25_POLITICS_DYNASTIC_SECURITY_CURRENT.md')
        values = tool.header((self.root / name).read_bytes(), name)
        for owner in ('AFM-001', 'AFM-002', 'AFM-003', 'AFM-004', 'AFM-008'):
            self.assertIn(owner, values['Cross-domain owner boundary'])
        self.sync()
        for filename, prefix in (
                (tool.INDEX, b'| `AFM-011` |'),
                (tool.MANIFEST, f'| `{name}` |'.encode())):
            path = self.root / filename
            path.write_bytes(b'\n'.join(line for line in path.read_bytes().split(b'\n')
                                       if not line.startswith(prefix)))
        before = self.snapshot()
        self.assertEqual(self.run_cli('--check').returncode, 2)
        self.assertEqual(before, self.snapshot())
        self.sync()
        self.assertEqual(self.run_cli('--check').returncode, 0)

    def test_missing_older_catalog_row_is_not_admission(self):
        self.sync()
        path = self.root / tool.INDEX
        path.write_bytes(b'\n'.join(line for line in path.read_bytes().split(b'\n')
                                   if not line.startswith(b'| `AFM-002` |')))
        self.rejected_without_writes()

    def test_technology_module_admission_and_owner_boundary(self):
        name = '15_TECHNOLOGY_AND_PUBLIC_SERVICE_INFRASTRUCTURE_CURRENT.md'
        self.assertEqual(tool.ACCEPTED['AFM-010'], name)
        values = tool.header((self.root / name).read_bytes(), name)
        self.assertEqual(values['Module ID'], 'AFM-010')
        for owner in ('AFM-001', 'AFM-002', 'AFM-003', 'AFM-008'):
            self.assertIn(owner, values['Cross-domain owner boundary'])
        self.sync()
        self.assertEqual(self.run_cli('--check').returncode, 0)

    def test_guest_admission_preserves_explicit_open_boundaries(self):
        text = (self.root / tool.ACCEPTED['AFM-010']).read_text(encoding='utf-8')
        for marker in ('AF-TECH-001', 'AF-TECH-002', 'AF-OPEN-006',
                       'Guest Wallet denomination', 'Offline behavior',
                       'candidate accounting', '500', 'UNKNOWN'):
            with self.subTest(marker=marker):
                self.assertIn(marker, text)
        ledger = (self.root / '92_OPEN_ISSUES_CURRENT.md').read_text(encoding='utf-8')
        for marker in ('AF-TECH-001', 'AF-TECH-002', 'AF-STATE-001',
                       'AF-OPEN-006', 'AF-OPEN-008', 'AF-OPEN-014', 'AF-ML-007'):
            with self.subTest(marker=marker):
                self.assertIn(marker, ledger)

    def test_generated_regions_only_and_archive_inventory_preserved(self):
        before = self.snapshot()
        self.sync()
        after = self.snapshot()
        for name, labels in ((tool.INDEX, (tool.CATALOG,)),
                             (tool.MANIFEST, (tool.METADATA, tool.HASHES))):
            old, new = before[name], after[name]
            for label in labels:
                old = tool.replace_region(old, label, '')
                new = tool.replace_region(new, label, '')
            self.assertEqual(old, new)
        self.assertEqual(set(before), set(after))

    def test_archive_hidden_check_and_write_without_archive_access(self):
        archive = self.root / 'Source_Archive'
        archive.mkdir()
        (archive / 'sentinel.md').write_bytes(b'historical sentinel')
        self.sync()
        archive.rename(self.root / 'hidden historical archive')
        self.assertEqual(self.run_cli('--check').returncode, 0)
        self.sync()
        original_read = Path.read_bytes

        def guarded_read(path):
            self.assertEqual(path.parent, self.root)
            return original_read(path)

        with patch.object(Path, 'read_bytes', guarded_read):
            inputs, changes = tool.plan(self.root, write=True)
            tool.atomic_write(self.root, inputs, changes)
        self.assertEqual((self.root / 'hidden historical archive' / 'sentinel.md').read_bytes(),
                         b'historical sentinel')

    def test_duplicate_module_id_fails_before_writes(self):
        name = tool.MODULE_FILES[1]
        path = self.root / name
        path.write_bytes(path.read_bytes().replace(b'> Module ID: `AFM-002`',
                                                 b'> Module ID: `AFM-001`', 1))
        self.rejected_without_writes()

    def test_missing_field_fails_before_writes(self):
        path = self.root / tool.MODULE_FILES[0]
        path.write_bytes(b'\n'.join(line for line in path.read_bytes().split(b'\n')
                                    if not line.startswith(b'> Load mode:')))
        self.rejected_without_writes()

    def test_unapproved_structural_header_field_fails(self):
        path = self.root / tool.MODULE_FILES[0]
        original = path.read_bytes()
        for field in ('MODULE_REQUIRES', 'NODE_REQUIRES'):
            for prose in (b'', b'> Note: ordinary prose is allowed.\n'):
                with self.subTest(field=field, prose=prose):
                    path.write_bytes(original.replace(
                        b'> Load mode: `FULL_FILE`',
                        b'> Load mode: `FULL_FILE`\n' + prose
                        + f'> {field}: `AFM-002`'.encode(), 1))
                    self.rejected_without_writes()

    def test_ordinary_header_prose_and_body_blockquote_are_allowed(self):
        path = self.root / tool.MODULE_FILES[0]
        original = path.read_bytes()
        path.write_bytes(original.replace(
            b'> Load mode: `FULL_FILE`',
            b'> Load mode: `FULL_FILE`\n> Note: ordinary prose is allowed.', 1)
            + b'\n> MODULE_REQUIRES: quoted body example, not header metadata.\n')
        self.sync()
        self.assertEqual(self.run_cli('--check').returncode, 0)

    def test_root_powershell_wrapper_forwards_python_only(self):
        wrapper = (PROJECT / 'build_consolidation.ps1').read_text(encoding='utf-8-sig')
        self.assertIn('build_consolidation.py', wrapper)
        for forbidden in ('Source_Archive', 'Read-MarkdownSource', 'Get-Range',
                          'Join-H1Sections', 'Replace-Required', 'Remove-RequiredRange',
                          'Write-MarkdownOutput'):
            with self.subTest(forbidden=forbidden):
                self.assertNotIn(forbidden, wrapper)

    def test_wrong_catalog_path_fails_before_writes(self):
        path = self.root / tool.INDEX
        data = path.read_bytes()
        data = data.replace(b'| `AFM-001` | `' + tool.MODULE_FILES[0].encode() + b'` |',
                            b'| `AFM-001` | `' + tool.MODULE_FILES[1].encode() + b'` |', 1)
        path.write_bytes(data)
        self.rejected_without_writes()

    def test_unknown_current_source_not_admitted(self):
        data = (self.root / tool.MODULE_FILES[0]).read_bytes().replace(b'AFM-001', b'AFM-999')
        (self.root / 'unexpected.md').write_bytes(data)
        self.rejected_without_writes()

    def test_bad_cross_domain_reference_fails_before_writes(self):
        path = self.root / tool.MODULE_FILES[0]
        path.write_bytes(path.read_bytes().replace(b'`AFM-007`', b'`AFM-999`', 1))
        self.rejected_without_writes()

    def test_wrong_role_and_load_mode_fails_before_writes(self):
        path = self.root / tool.MODULE_FILES[0]
        original = path.read_bytes()
        for old, new in ((b'`CURRENT_SOURCE`', b'`PROPOSAL`'),
                         (b'`FULL_FILE`', b'`NODE_OR_FULL`')):
            with self.subTest(field=old):
                path.write_bytes(original.replace(old, new, 1))
                self.rejected_without_writes()

    def test_duplicate_header_field_and_missing_markers(self):
        path = self.root / tool.MODULE_FILES[0]
        data = path.read_bytes()
        path.write_bytes(data.replace(b'> Module ID: `AFM-001`',
                                     b'> Module ID: `AFM-001`\n> Module ID: `AFM-001`', 1))
        self.rejected_without_writes()
        path.write_bytes(data)
        index = self.root / tool.INDEX
        index.write_bytes(index.read_bytes().replace(b'<!-- END GENERATED MODULE CATALOG -->', b''))
        self.rejected_without_writes()

    def test_missing_current_file(self):
        (self.root / tool.CURRENT_FILES[-1]).unlink()
        self.rejected_without_writes()

    def test_hash_refresh_after_human_current_edit(self):
        self.sync()
        path = self.root / tool.CURRENT_FILES[-1]
        path.write_bytes(path.read_bytes() + b'\nDisposable human edit\n')
        current = path.read_bytes()
        self.assertEqual(self.run_cli('--check').returncode, 2)
        self.sync()
        self.assertEqual(current, path.read_bytes())
        self.assertEqual(self.run_cli('--check').returncode, 0)

    def test_crlf_and_lf_generated_regions(self):
        for name in (tool.INDEX, tool.MANIFEST):
            path = self.root / name
            path.write_bytes(path.read_bytes().replace(b'\r\n', b'\n').replace(b'\n', b'\r\n'))
        self.sync()
        self.assertEqual(self.run_cli('--check').returncode, 0)
        for name, label in ((tool.INDEX, tool.CATALOG), (tool.MANIFEST, tool.HASHES)):
            _, _, newline, block = tool.region((self.root / name).read_bytes(), label)
            self.assertEqual(newline, b'\r\n')
            self.assertNotIn(b'\n', block.replace(b'\r\n', b''))

    def test_write_allowlist_and_outside_region_guard(self):
        inputs, _ = tool.plan(self.root, write=True)
        before = self.snapshot()
        with self.assertRaises(tool.ValidationError):
            tool.atomic_write(self.root, inputs, {tool.MODULE_FILES[0]: b'forbidden'})
        with self.assertRaises(tool.ValidationError):
            tool.atomic_write(self.root, inputs, {tool.INDEX: inputs[tool.INDEX] + b'forbidden'})
        self.assertEqual(before, self.snapshot())

    def test_replace_failure_rolls_back_and_cleans_temporary_files(self):
        self.sync()
        index = self.root / tool.INDEX
        index.write_bytes(index.read_bytes().replace(b'> Derived routing index only.',
                                                    b'> Stale derived routing text.', 1))
        manifest = self.root / tool.MANIFEST
        manifest.write_bytes(manifest.read_bytes().replace(b'## Current package maintenance',
                                                          b'## Stale maintenance metadata', 1))
        inputs, changes = tool.plan(self.root, write=True)
        self.assertEqual(set(changes), {tool.INDEX, tool.MANIFEST})
        before = self.snapshot()
        replace = os.replace
        calls = 0

        def fail_second(source, target):
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError('injected replacement failure')
            replace(source, target)

        with patch.object(tool.os, 'replace', fail_second):
            with self.assertRaises(OSError):
                tool.atomic_write(self.root, inputs, changes)
        self.assertEqual(before, self.snapshot())

    def test_concurrent_edit_is_preserved(self):
        inputs, changes = tool.plan(self.root, write=True)
        # Force a valid derived change even when the fixture is already synced.
        index = self.root / tool.INDEX
        index.write_bytes(index.read_bytes().replace(b'## Runtime Module Catalog',
                                                    b'## Runtime Module Catalog ', 1))
        inputs, changes = tool.plan(self.root, write=True)
        path = self.root / tool.CURRENT_FILES[-1]
        path.write_bytes(path.read_bytes() + b'\nConcurrent human edit\n')
        before = self.snapshot()
        with self.assertRaises(tool.ValidationError):
            tool.atomic_write(self.root, inputs, changes)
        self.assertEqual(before, self.snapshot())


if __name__ == '__main__':
    unittest.main()
