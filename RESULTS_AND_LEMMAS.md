# Guide to the model results, six lemmas and publication figures

**Source:** the saved result files in original `4.HA_Conflict_Paper_Complete.zip` / extracted `HA_Conflict_Paper_Complete/paper/`. Its archived `results/run_manifest.json` records `source_mode = external` for all three reactor runs. Values here are **from the saved external-input outputs**, not a new execution.

## Numerical verification of the Bayesian implementation

`paper/verification_results/Audit_Report.json` records `status: PASS`, 189,000 context records, 14,942 eligible updates and a maximum posterior reconstruction error of approximately 3.89×10^-16 (tolerance 10^-12), with zero ineligible/frozen-step probability drift. Nine run×review traces are checked. This demonstrates consistency of *implemented arithmetic and gates* with the specified model, **not calibrated latent conflict probabilities**. Closed-form synthetic/tampering tests appear in `SOFTWARE_TEST_REPORT.json`.

## Lemma to evidence matrix

| Lemma | Theoretical/computational property | Main evidence in ZIP | Suitable journal interpretation |
|---|---|---|---|
| **1 — Context preservation** | Ineligible/inactive context retains posterior and D/M history | `Fig02_Controlled_Mechanisms`, frozen-step audit, `Fig04_Context_and_System_Conflict` | Model preserves distinct context estimates; controlled tests verify implementation |
| **2 — Persistence and recurrence** | Continued U increases evaluated duration D; new A/R→U episode increases M | `Fig02_Controlled_Mechanisms`, `controlled_qualified_sequences.csv` | Persistence and recurrence are distinguished computationally, not behaviorally calibrated |
| **3 — Bayesian evidence update** | Eligible evidence modifies posterior relative to prediction according to configured likelihood; unqualified agreement is not R | `Fig02`, audit reconstruction, selected case `Fig05` | Correct conditional updating under specified likelihoods, not empirical Bayesian calibration |
| **4 — Context-to-system mixture** | System quantity is a normalized weighted sum of context-specific probabilities | `Fig04_Context_and_System_Conflict` and underlying plot-data CSVs | Standardized mixture; **not** event-union probability for conflict somewhere in a plant |
| **5 — Review only through later evidence** | Review does not directly overwrite current posterior; response appears in subsequent qualified interactions | `Fig05_Matched_Fault_Period_Issue` and `Fig06_Common_Cohort_Recovery` | Early verified agreement occurs in some cases; later relapse is possible |
| **6 — Conditional conflict-related risk** | Scenario loss under low/high latent conflict and context exposure generate conditional risk index | `Fig07_Conditional_Risk`, `risk_summary.csv`, supplementary S08 | Assumption-based index, **not** observed accidents or intervention-caused safety improvement |

## Baseline performance of the human and AI components

Data: `2.Human_Operator_ABC.zip` → `my_results/run_comparison.csv` and `3.AI_Operator_ABC.zip` → `ai_results/run_comparison.csv`.

| Metric | Human Run C | AI Run C |
|---|---:|---:|
| Accuracy against injected context label | 0.847743 | 0.918614 |
| C3 recall | 0.007882 | 0.476706 |

The human model is a simulated stochastic surrogate; AI fit uses Run A, with Run C as designated retrospective test. Neither metric is human clinical/industrial validation. The C3 mismatch helps explain why cooling-diagnostic interactions are informative, but classification performance is **not** equivalent to calibrated conflict probability.

## Common-cohort verified diagnostic agreement

Source: `paper/tables/common_cohort_landmarks.csv`; counts represent issues with a 30-s maintained verified diagnostic agreement at the given elapsed landmark. All policies use the same eligible issue denominator at each landmark; later relapse can reduce success counts.

| Run / C3 landmark | Baseline | Observation review | PI-evidence review |
|---|---:|---:|---:|
| Run B, 120 s | 0/4 | 0/4 | 1/4 |
| Run B, 180 s | 0/4 | 0/4 | 1/4 |
| Run B, 300 s | 1/4 | 1/4 | 1/4 |
| Run C, 120 s | 0/13 | 0/13 | 6/13 |
| Run C, 180 s | 0/13 | 0/13 | 1/13 |
| Run C, 300 s | 5/13 | 5/13 | 5/13 |

These are small **dependent** simulation cohorts, not independent-randomized trial effect estimates. The temporary PI-review advantage cannot be described as permanent recovery. `Fig05` is one illustration of resolution followed by renewed disagreement; `Fig06` provides shared-denominator descriptive comparison.

## Run C conditional-risk results

Source: `paper/tables/risk_summary.csv`, `context = system`, `mean_risk_index`.

| Arm | Mean standardized system risk index |
|---|---:|
| Baseline | 0.00511622 |
| Observation review | 0.00467112 |
| PI review | 0.00455979 |

Under the configured assumptions, PI review is about **10.9% below baseline** in this *modeled index*. The **physical trajectories are unchanged across arms**, so this must **not** be called a measured 10.9% reduction in plant accident risk. The 400 consequence scenarios (seed 10601) and equal C1/C2/C3 exposure weights are hypothetical assumptions. Figure bands are 5th–95th *scenario-assumption quantiles*, not confidence intervals. Supplementary S08 checks equal/reversed low/high consequence rankings and confirms model dependence on consequence assumptions.

## Figure locations and manuscript use

| Source filename | Role | Recommended placement |
|---|---|---|
| `Fig01_Model_and_Qualification` | Model schematic and evidence qualifications | Methods/optional appendix, not duplicate existing manuscript figure numbering |
| `Fig02_Controlled_Mechanisms` | Numerical/controlled mechanism behavior | Section 5.1 main |
| `Fig03_Reactor_Contexts_and_Severity` | Actual simulator context and severity visualization | Supplement if main text is dense |
| `Fig04_Context_and_System_Conflict` | Distinct context histories and standardized mixture | Section 5.1 main |
| `Fig05_Matched_Fault_Period_Issue` | Single event explaining policy mechanism | Section 5.2 or supplement |
| `Fig06_Common_Cohort_Recovery` | Shared-case, fixed-landmark comparison | Section 5.2 main |
| `Fig07_Conditional_Risk` | Conditional risk and scenario bands | Section 5.3 main |
| `S07_Trigger_Sensitivity` | Review trigger setting stress test | Supplement |
| `S08_Consequence_Assumption_Sensitivity` | Loss assumptions reverse risk mapping | Supplement; discuss in main |
| `S09_Bayesian_Update_Audit` | Independent posterior reconstruction check | Supplement |

The manuscript already contains other figures/tables; internal filenames do not set final journal figure/table numbers. Avoid overstating that the six mathematical lemmas are independently proven by a finite set of CSTR simulations. The code's numerical verification, modeled behavior and real-world validation are different evidence levels.
