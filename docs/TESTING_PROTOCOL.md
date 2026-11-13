# Testing and verification protocol

## Distinct levels of evidence

**Structural/source validation** checks paths, source and data integrity. **Numerical verification** checks implementation of stated rules. **Simulation evaluation** assesses modeled differences under shared input assumptions. **External validation** would require empirical humans and/or independent plant evidence and is not established by these archives.

| Layer | Required execution/inspection | Expected scientific check | Location |
|---|---|---|---|
| Archive integrity | `python scripts/prepare_archives.py --verify` | All four original SHA-256 hashes, archive CRC and safe paths match | Root manifest and original ZIPs |
| Reactor stage | Inspect source/screening; execute only with licensed MATLAB/Simulink and matching prerequisites | 70,000 rows per run; C0/C1/C2/C3 scheduled durations; feasibility screens; no human/SIF actuation | `ASTE_Long_Context_Feasible/README.md`, `verification.json`, design files |
| Simulated human | Fresh `human_operator_model.py` | Independent reset per run; 70k aligned predictions; agreement with injected schedule used only as simulation evaluation | `Human_Operator_ABC/my_results/`, `run_manifest.json` |
| AI classifier | Fresh `ai_fault_model.py` | Fit on A, evaluate B and C without refitting; no injected labels among inference features | `AI_Operator_ABC/ai_results/`, prediction manifests |
| Controlled interaction fixtures | `test_bayesian_audit.py` | Closed-form Bayes check; negative mutations for likelihood, history, evidence and issue identity rejected | `SOFTWARE_TEST_REPORT.json` |
| Complete conflict/risk rerun | `run_bundled_reference.py` or provenance-validated external `run_package.py` | All nine run×policy traces, PASS gates, qualified A/U/R evidence and consistency with saved data | `results/`, `paper/` |
| Independent numerical audit | Included in `run_package.py` | Prediction/posterior recomputation, frozen ineligible rows, separate contexts | `paper/verification_results/` |
| Policies and risk | Inspect matched cohorts, scenario sensitivity and source CSVs | Same reactor/AI within each run; reported common denominators; risk assumptions explicit | `paper/tables/`, `paper/figures/data/` |

## Six-lemma verification matrix

| Lemma | Testable implementation property | Evidence | What is **not** established |
|---|---|---|---|
| 1 Context preservation | Ineligible or inactive context retains prior posterior and history | Synthetic fixture and frozen-step trace audit; Fig02/Fig04 illustrate | Empirical independence of real operator conflicts |
| 2 Persistence/recurrence | Consecutive unresolved U steps increase D; new A/R→U increases M | Controlled sequences, state/counter audit; Fig02 | Actual behavioral duration/recurrence calibration |
| 3 Bayesian update | Eligible likelihood applied to predicted state with old history, no extra update for unqualified agreement | Closed-form and independent posterior recomputation; Fig02 | Likelihood ratios empirically validated |
| 4 System aggregation | Context estimates combine as convex weighted mixture, weights sum to 1 | Calculated system series and numerical assertions; Fig04 | Probability of any simultaneous system conflict |
| 5 Evidence-mediated review | Review only affects subsequent qualified evidence, not current posterior directly | Policy code, matched case traces; Fig05/Fig06 | Genuine human adaptation or causal physical intervention |
| 6 Conflict-related risk | Conditional expectation and standardized context mixture computed as stated | Risk assertions, Fig07 and supplementary S08 | Actual loss probability or unconditional plant risk |

## Recorded archived audit values (must be rechecked after rerun)

- Nine run×policy traces: A/B/C times baseline/observation_review/pi_review.
- **189,000 context records**, **14,942 eligible Bayesian updates**.
- Largest prediction discrepancy **2.220446049250313e-16**.
- Largest posterior discrepancy **3.885780586188048e-16**.
- Frozen/ineligible row posterior drift **0**; acceptance tolerance `1e-12`.
- These figures are **archived execution claims**, not proof that a different environment reproduces identical outputs.

## Matched C3 review comparison

Use `paper/tables/common_cohort_landmarks.csv` or `paper/figures/data/Fig06_Common_Cohort_Recovery.csv` from the same executed version. At 120/180/300 s after a common issue onset, the endpoint is verified diagnostic agreement maintained in the preceding 30 s. The denominator includes eligible unresolved and later-relapsed issues. For example, the recorded C3 Run C at 120 s is baseline **0/13**, observation **0/13**, PI **6/13**; at 180 s PI is **1/13**, and at 300 s all arms are **5/13**. These are small dependent descriptive cohorts, not proof of statistical significance or permanent recovery.

## Consequence-risk sensitivity

The supplied study uses 400 assumed consequence scenarios, seed 10601, equal C1/C2/C3 exposure weights. Stress test equal and reversed high-/low-conflict conditional loss ordering (supplementary S08). If H and L consequences are equal, the policies' differences attributable solely to posterior p disappear; reversing their ordering reverses the relationship. Bands from scenario assumptions are **not confidence intervals**.

## Pre-publication acceptance criteria

1. All four source ZIP checksums pass; do not conceal a modified archive behind its original name.
2. Required Python versions and dependency versions are documented for the executed release.
3. Stored test reports and new execution outputs are **clearly distinguished**.
4. MATLAB paths, binary/rights prerequisites and missing stage input artifacts are explicit.
5. One provenance mode is used consistently for any table/figure comparison.
6. Risk indices are called conditional scenario-based indices, and A/B/C roles are stated accurately.
7. Published figures/tables exactly match the tagged source and release notes.
