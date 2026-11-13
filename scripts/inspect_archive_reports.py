#!/usr/bin/env python3
"""Read and identify existing saved reports; this does NOT run or validate a new experiment."""
import csv
import io
import json
import zipfile
from pathlib import Path

root = Path(__file__).resolve().parents[1]
path = root / 'HA_Conflict_Paper_Complete(6).zip'
with zipfile.ZipFile(path) as z:
    reports = [
        'HA_Conflict_Paper_Complete/paper/completion.json',
        'HA_Conflict_Paper_Complete/results/completion.json',
        'HA_Conflict_Paper_Complete/SOFTWARE_TEST_REPORT.json',
    ]
    print('ARCHIVED RESULTS ONLY — these are saved historical reports, not an execution.')
    for name in reports:
        if name not in z.namelist():
            print(name, 'NOT PRESENT')
        else:
            obj = json.loads(z.read(name).decode('utf-8'))
            print(name, 'status=', obj.get('status', 'unspecified'))
    name = 'HA_Conflict_Paper_Complete/paper/verification_results/Audit_Summary.csv'
    if name in z.namelist():
        rows = list(csv.DictReader(io.StringIO(z.read(name).decode('utf-8'))))
        print('Archived audit summary:', len(rows), 'rows; fields:', ', '.join(rows[0]) if rows else 'none')
print('Read the executed audit and provenance reports in the ZIP before making any claim.')
