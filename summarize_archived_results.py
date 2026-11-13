#!/usr/bin/env python3
"""Read-only concise result summary from original four ZIPs; no model rerun needed."""
import csv
import io
import json
import zipfile

from prepare_archives import MANIFEST, locate_archive

archives = json.loads(MANIFEST.read_text())['archives']


def csv_in_zip(z, path):
    return list(csv.DictReader(io.StringIO(z.read(path).decode('utf-8'))))


with (zipfile.ZipFile(locate_archive(archives['human'])) as zh,
      zipfile.ZipFile(locate_archive(archives['ai'])) as za,
      zipfile.ZipFile(locate_archive(archives['conflict'])) as zc):
    human = csv_in_zip(zh,'Human_Operator_ABC/my_results/run_comparison.csv')
    ai = csv_in_zip(za,'AI_Operator_ABC/ai_results/run_comparison.csv')
    risks = csv_in_zip(zc,'HA_Conflict_Paper_Complete/paper/tables/risk_summary.csv')
    cohort = csv_in_zip(zc,'HA_Conflict_Paper_Complete/paper/tables/common_cohort_landmarks.csv')
    audit = json.loads(zc.read('HA_Conflict_Paper_Complete/paper/verification_results/Audit_Report.json'))
    print('ARCHIVED RESULTS; EXTERNAL-INPUT MODE; NOT A RE-EXECUTION')
    print('Bayesian audit:',audit['status'],'rows:',audit['rows'], 'eligible updates:', audit['eligible_updates'],
          'max posterior error:',audit['max_posterior_error'])
    h = next(x for x in human if x['run_id']=='run_C')
    a = next(x for x in ai if x['run_id']=='run_C')
    print('\nRun C classifier accuracy vs injected simulation labels:')
    print(' Human:',h['accuracy_against_injection'], 'C3 recall:',h['C3_recall'])
    print(' AI:   ',a['accuracy'], 'C3 recall:',a['C3_recall'])
    print('\nRun C mean standardized system conditional risk index:')
    d = {}
    for row in risks:
        if row['run_id']=='run_C' and row['context']=='system':
            d[row['arm']] = float(row['mean_risk_index'])
            print(' ',row['arm'],':',row['mean_risk_index'])
    print(' PI minus baseline (relative %):', 100*(d['pi_review']/d['baseline'] - 1))
    print('\nRun C C3 common eligible issue outcomes (maintained verified agreement):')
    for landmark in ('120','180','300'):
        entries=[]
        for arm in ('baseline','observation_review','pi_review'):
            group=[r for r in cohort if r['run_id']=='run_C' and r['context']=='C3' and
                   r['arm']==arm and r['horizon_s']==landmark and str(r['eligible'])=='1' and str(r['scheduled_fault_case'])=='1']
            total=len(group); succ=sum(str(r['success'])=='1' for r in group)
            entries.append(f'{arm} {succ}/{total}')
        print(' ',landmark,'s:',', '.join(entries))
    print('\nInterpretation: model checks and simulated observations; risk values are scenario-based indices, not observed accident probabilities.')
