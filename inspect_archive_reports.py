#!/usr/bin/env python3
"""Inspect saved reports and verify their external-input provenance against separate ZIPs.
This is read-only verification of historical files, NOT a new model execution.
"""
import hashlib
import json
import zipfile
from pathlib import Path

from prepare_archives import MANIFEST, locate_archive

manifest = json.loads(MANIFEST.read_text())['archives']
paths = {k: locate_archive(v) for k,v in manifest.items()}


def digest_zip_member(z: zipfile.ZipFile, member: str) -> str:
    h = hashlib.sha256()
    with z.open(member) as f:
        for part in iter(lambda: f.read(1024*1024), b''):
            h.update(part)
    return h.hexdigest()


with zipfile.ZipFile(paths['conflict']) as zc, zipfile.ZipFile(paths['human']) as zh, zipfile.ZipFile(paths['ai']) as za:
    def read_conflict(p):
        return json.loads(zc.read('HA_Conflict_Paper_Complete/' + p).decode('utf-8'))

    print('READ-ONLY INSPECTION OF ORIGINAL ARCHIVE REPORTS')
    for report in ('paper/completion.json', 'results/completion.json', 'SOFTWARE_TEST_REPORT.json'):
        try:
            print('  saved', report, ':', read_conflict(report).get('status'))
        except KeyError:
            print('  saved', report, ': missing')

    audit = read_conflict('paper/verification_results/Audit_Report.json')
    print('  saved audit:', audit.get('status'), 'rows', audit.get('rows'), 'eligible', audit.get('eligible_updates'),
          'max posterior error', audit.get('max_posterior_error'))

    records = read_conflict('results/run_manifest.json')['inputs']
    print('\nExternal source provenance (comparison with separate human/AI ZIP members):')
    for r in ('run_A','run_B','run_C'):
        rec = records[r]
        if rec['source_mode'] != 'external':
            raise RuntimeError(f'{r} is {rec["source_mode"]}, not the documented archived external mode')
        files = {
            'human': (zh, f'Human_Operator_ABC/my_results/{r}/human_stage1_predictions.csv'),
            'ai': (za, f'AI_Operator_ABC/ai_results/{r}/ai_predictions_70000.csv'),
            'reactor': (za, f'AI_Operator_ABC/input/{r}.csv'),
        }
        for component,(z,path) in files.items():
            actual = digest_zip_member(z,path)
            expected = rec['files'][component]['sha256']
            if actual != expected:
                raise RuntimeError(f'MISMATCH: {r}, {component} -- saved manifest does not match standalone archive')
        print('  PASS',r, 'external reactor + human + AI member hashes')

    print('\nDifferent bundled reference AI hashes (NOT the saved external outputs):')
    for r in ('run_A','run_B','run_C'):
        bundled_hash = digest_zip_member(zc, f'HA_Conflict_Paper_Complete/input/{r}/ai.csv')
        saved_external_hash = records[r]['files']['ai']['sha256']
        print(' ',r, 'bundled AI distinct from standalone:',bundled_hash != saved_external_hash)

    print('\nPASS: saved source provenance matches the uploaded standalone inputs. No simulation was executed.')
