#!/usr/bin/env python3
"""Verify original archive payloads despite GitHub Release's 1.-4. asset names.

Standard library only. Usage:
  python scripts/prepare_archives.py --verify
  python scripts/prepare_archives.py --extract

The archive_manifest.json records exact original SHA-256, member counts, and expected
root folder. Release asset filenames and original uploaded filenames are aliases
of identical bytes. Extraction does not overwrite an existing extracted folder.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import sys
import zipfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'archive_manifest.json'


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for buf in iter(lambda: f.read(1024 * 1024), b''):
            h.update(buf)
    return h.hexdigest()


def locate_archive(record: dict) -> Path:
    names = [record['release_filename'], record['original_upload_name']]
    found = [ROOT / n for n in names if (ROOT / n).is_file()]
    if not found:
        raise FileNotFoundError('Missing ZIP; download release Asset ' + names[0] + ' beside README.md (also accepts ' + names[1] + ')')
    return found[0]


def inspect_archive(path: Path, record: dict) -> int:
    if path.stat().st_size < 256:
        raise ValueError(f'{path.name}: unexpectedly tiny; Git LFS pointer? Download full release asset.')
    if path.stat().st_size != record['size_bytes']:
        raise ValueError(f'{path.name}: size mismatch; expected {record["size_bytes"]}, got {path.stat().st_size}')
    observed = sha256(path)
    if observed != record['sha256']:
        raise ValueError(f'{path.name}: SHA-256 mismatch; expected {record["sha256"]}, got {observed}')
    with zipfile.ZipFile(path) as z:
        members = [m for m in z.infolist() if not m.is_dir()]
        if len(members) != record['files']:
            raise ValueError(f'{path.name}: file member count mismatch {len(members)} vs {record["files"]}')
        base = record['root']
        for m in z.infolist():
            n = m.filename
            parts = PurePosixPath(n).parts
            if not n or '\\' in n or n.startswith('/') or not parts or parts[0] != base or any(p in ('.', '..', '') for p in parts):
                raise ValueError('Invalid ZIP path: ' + n)
            if (m.external_attr >> 16) & 0o170000 == 0o120000:
                raise ValueError('Refusing ZIP symlink: ' + n)
        corrupt = z.testzip()
        if corrupt:
            raise ValueError(f'{path.name}: CRC failed in {corrupt}')
    return len(members)


def extract_archive(path: Path, record: dict) -> None:
    target = ROOT / record['root']
    if target.exists():
        print(f'  SKIP extracted folder already exists: {target} (make a fresh working directory if needed)')
        return
    with zipfile.ZipFile(path) as z:
        for item in z.infolist():
            dest = (ROOT / item.filename).resolve()
            if not dest.is_relative_to(ROOT.resolve()):
                raise ValueError('Unsafe path: ' + item.filename)
        print('  Extracting to:', target)
        z.extractall(ROOT)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    flag = parser.add_mutually_exclusive_group(required=True)
    flag.add_argument('--verify', action='store_true')
    flag.add_argument('--extract', action='store_true')
    args = parser.parse_args()
    data = json.loads(MANIFEST.read_text(encoding='utf-8'))
    for key, record in data['archives'].items():
        path = locate_archive(record)
        print('VERIFY:', key, '<-', path.name, flush=True)
        n = inspect_archive(path, record)
        print('  PASS SHA-256, length,', n, 'member CRC/path checks', flush=True)
        if args.extract:
            extract_archive(path, record)
    print('PASS: all four original archive payloads match expected manifest.')
    if args.extract:
        print('Extracted directories are peers of docs/ and scripts/.')


if __name__ == '__main__':
    try:
        main()
    except (FileNotFoundError, KeyError, ValueError, zipfile.BadZipFile) as exc:
        print('FAIL:', exc, file=sys.stderr)
        sys.exit(1)
