#!/usr/bin/env python3
"""Check SHA256, structure and CRC of the four original uploaded ZIP files; optionally extract safely.

Python 3 standard library only. Run from anywhere:
  python scripts/prepare_archives.py --verify
  python scripts/prepare_archives.py --extract
"""
import argparse
import hashlib
import json
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'archive_manifest.json'


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def inspect(path, expected):
    if not path.is_file():
        raise FileNotFoundError('Missing original ZIP: ' + path.name)
    if path.stat().st_size < 256:
        raise ValueError(path.name + ' appears to be a Git LFS pointer. Run: git lfs pull')
    actual = digest(path)
    if actual != expected['sha256']:
        raise ValueError(path.name + ' SHA-256 mismatch. Expected ' + expected['sha256'] + '; got ' + actual)
    with zipfile.ZipFile(path, 'r') as z:
        members = [n for n in z.namelist() if not n.endswith('/')]
        if len(members) != expected['files']:
            raise ValueError(path.name + ' file inventory changed')
        expected_root = expected['root'] + '/'
        for info in z.infolist():
            n = info.filename
            if n.startswith('/') or '\\' in n or not n.startswith(expected_root):
                raise ValueError(path.name + ' unsafe/unexpected member: ' + n)
            if any(p in ('', '.', '..') for p in Path(n).parts):
                raise ValueError(path.name + ' unsafe member: ' + n)
            # Reject symlinks to ensure archives don't redirect writes.
            if (info.external_attr >> 16) & 0o170000 == 0o120000:
                raise ValueError(path.name + ' contains symlink: ' + n)
        corrupt = z.testzip()
        if corrupt:
            raise ValueError(path.name + ' CRC check failed at: ' + corrupt)
        return len(members)


def extract(path, expected):
    with zipfile.ZipFile(path, 'r') as z:
        members = z.infolist()
        for item in members:
            dest = (ROOT / item.filename).resolve()
            if not dest.is_relative_to(ROOT.resolve()):
                raise ValueError('unsafe extraction path: ' + item.filename)
        target = ROOT / expected['root']
        if target.exists():
            print('  SKIP existing extracted folder:', target.name, '(delete or rename only after backing up)')
            return
        print('  Extracting', path.name, '...')
        z.extractall(ROOT)


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--verify', action='store_true', help='Verify file identity/CRC without extracting')
    g.add_argument('--extract', action='store_true', help='Verify and extract as four sibling directories')
    args = ap.parse_args()
    d = json.loads(MANIFEST.read_text(encoding='utf-8'))
    checks = d['archives']
    for name, expected in checks.items():
        path = ROOT / name
        print('CHECK', name, flush=True)
        count = inspect(path, expected)
        print('  PASS SHA-256, ZIP inventory and CRC:', count, 'files', flush=True)
        if args.extract:
            extract(path, expected)
    print('PASS: all four original source archives verified.', flush=True)
    if args.extract:
        print('The four extracted folders now sit beside docs/ and scripts/.')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, FileNotFoundError, zipfile.BadZipFile) as e:
        print('FAIL:', e, file=sys.stderr)
        sys.exit(1)
