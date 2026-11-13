# How the present research uses and extends ASTE–CSTR

## 1. Citation and scope of comparison

**Reference work:** Markaj, A., Mercangöz, M., & Fay, A. (2024), "Design and implementation of an Autonomous Systems Training Environment framework for control algorithm evaluation in autonomous plant operation," *Computers & Chemical Engineering*, 189, 108798. DOI: https://doi.org/10.1016/j.compchemeng.2024.108798.

The original ASTE is a framework for evaluating autonomous control algorithms. Its exemplary CSTR integrates process and regulatory control, fault generation, a supervisory/state-based model, an operator model, safety instrumented functions and agent interfaces. Our research is **not a replication of every mode of the original ASTE**: it uses its reactor simulation as a source of offline process observations and separately evaluates human–AI diagnostic interaction and conditional risk.

**Evidence basis:** the code, schedules, explanatory notes and results in the four distributed ZIPs and the 2024 reference article. The four ZIPs do **not** include a separately identified, immutable upstream ASTE commit paired with a machine-generated source-code diff. Thus the classification below reflects the described research configuration, not an assertion of an exhaustive line-by-line diff against the upstream ASTE repository.

## 2. Component-by-component change log

| Component | Original ASTE reference | This study's adaptation | Evidence in distributed code | Scientific implication |
|---|---|---|---|---|
| CSTR process/plant | MATLAB/Simulink CSTR with physical dynamics | Retained CSTR plant simulation and original regulatory PID according to package notes; varied scheduled fault factors and duration | `1.ASTE...zip` → `source/cstr_simulationEnv.slx`, `source/cstrm.m`, `source/aste_run_v122.m`, `README.md` | Reactor process remains the test system; **new Human–AI conflict equations are not new CSTR physics** |
| Fault generation | ASTE fault-engine capabilities | **Predefined deterministic fault schedules** for three differently ordered long runs; fault values C1=0.8, C2=0.6, C3=1.2 | `experiment_design.json`, `schedules/run_A.mat`–`run_C.mat` and `tables/run_*_sequence.csv` | Controlled/repeatable fault opportunities, not naturally occurring or estimated fault frequencies |
| Execution duration | Original article demonstrates the framework using example runs | **A/B/C, 70,000 s each**, physical recording at 1 Hz | `experiment_design.json`, `run_long_sequences.py` and the input CSVs in human/AI ZIPs | Supports repeated diagnostic opportunities on extended operating sequences |
| Operator and safety actuation | Original ASTE includes operator intervention and safety functionality | For this **offline comparison**, operator/SIF actuation is disabled in the research configuration, while nominal regulatory PID operates | ASTE `README.md`, driver settings | Human/AI review **cannot alter the physical trajectory** and no causal plant-safety reduction is measured |
| Simulation input representation | Fault inputs fed to MATLAB workspace/Simulink | Corrected scheduled MAT variables from integer arrays to finite MATLAB `double`, with explicit base-workspace assignment | `INPUT_FORMAT_FIX.md`, `source/aste_run_v122.m`, schedule MATs | Interface compatibility correction; documentation says numeric schedule values and reactor equations are unchanged |
| Rejected long fault | C2 outlet restriction was screened at multiple durations | C2 1,000 s stress test exceeded the selected level screen; **removed from active mixed sequences**, retained as a documented rejected stress case | `C2_REJECTION_REVIEW.md`, `experiment_design.json` | C2 active episodes are 200 s (5) and 500 s (10); do not misreport an accepted 1,000 s C2 experiment |
| Human diagnostic interpretation | Original ASTE has an operator-control component | **Separate computational stochastic finite-state diagnostic surrogate**, driven by exported CSTR observations, reset for each run; no human participants | `2.Human...zip` → `human_operator_model.py`, `run_config.json`, `MODEL_NOTES.md` | Simulated human labels/uncertainty; not observed cognition or real operators |
| AI diagnosis | Original ASTE supports autonomous agents | **Separate Random Forest** with engineered causal/past-only features. Fit only on run A; assess B and C without refitting | `3.AI...zip` → `ai_fault_model.py`, `run_config.json`, saved `ai_classifier.joblib` | Fixed AI prediction stream within each diagnostic-review comparison |
| Conflict state and memory | The original ASTE article does not implement this manuscript's Bayesian conflict-history construction | Added A/U/R observable interaction state, L/H latent states, context-specific posterior/history, duration D and recurrence M, qualified evidence/update gating | `4.HA...zip` → `issue_model.py`, `run_conflict_model.py`, `config.json`, `BAYESIAN_DERIVATION.md` | Tests **dynamic, context-specific Human–AI conflict**, not baseline fault-detection accuracy alone |
| Diagnostic review | Original ASTE's operator/agent framework is a control-evaluation platform | Added **baseline**, observation-review and PI-response-evidence-review arms, compared on same process/AI signals | `human_review.py`, `issue_model.py`, `run_conflict_model.py` | Review affects **subsequent simulated diagnostic evidence**, not immediate posterior override or actuation |
| Conflict-related risk | Original ASTE can evaluate control/reward/safety behavior | Added process-severity proxy, context-specific conditional consequence model and standardized equal-exposure risk mixture | `risk_model.py`, `config.json`, `paper/tables/risk_summary.csv` | **Scenario-based conditional risk index**, not the original ASTE reward function or observed accident probability |
| Verification and presentation | Original ASTE provides simulation/test demonstrations | Added numerical Bayesian audit, controlled synthetic traces, cohort analysis, figures, assumption sensitivities | `test_bayesian_audit.py`, `run_bayesian_audit.py`, `paper/verification_results/`, `paper/figures/` | Tests fidelity of implementation and behavior under declared rules, **not empirical calibration** |

## 3. Operating contexts, trajectories and intended comparisons

| Context | Simulation setting | Fault duration in each 70,000-s run | Use |
|---|---|---:|---|
| C0 | Nominal/no injected fault | 47,000 s | Process reference; **excluded from standardized abnormal-context risk mixture** |
| C1 | Inlet flow factor **0.8** | 8,500 s | Reduced inlet fault |
| C2 | Outlet flow factor **0.6** | 6,000 s | Restricted outlet fault; 1,000-s stress case excluded |
| C3 | Cooling-response factor **1.2** | 8,500 s | Cooling alteration; notable diagnostic mismatch |

C1/C3 each have five episodes at 200, 500 and 1,000 s. C2 has five at 200 s and ten at 500 s. Run A/B/C differ in order, share nominal model/settings and are **separately initialized scenarios**, not unrelated real-plant trials. The common CSTR trajectories are held unchanged across review arms.

### Why the C2 1,000-second case was excluded

The supplied C2 stress-case note reports 269 observations with reactor level above the model's configured 500-unit screen, with a simulated peak approximately 600.60. It returned toward nominal afterward, but recovery does not make those out-of-screen samples acceptable within the chosen main experiment. The magnitude, reactor physics and acceptance limit were not altered to make the test pass; the active fault duration was revised and the rejected case retained for provenance.

### Input-format correction

The supplied `INPUT_FORMAT_FIX.md` records that all schedule `.mat` arrays use finite float64/MATLAB `double`, and the MATLAB launcher reassigns the base-workspace fault-enable variables before compiling the Fault Engine. This is a numerical interface correction and should not be presented as a new chemical kinetic, mass-balance or PID-control contribution.

## 4. Research pipeline and observable outputs

```text
Adapted ASTE MATLAB/Simulink CSTR → 1 Hz reactor CSVs (A, B, C)
                    ├────→ simulated human diagnostic predictions
                    └────→ Random Forest AI predictions (A train; B validate; C test)
                                     ↓ matched (run_id, time_s)
                         10 s diagnostic comparison/issue ledger
                                     ↓
                       context-specific A/U/R and D/M history
                                     ↓
                          Bayesian P(X=H | qualified evidence)
                                     ↓
                          baseline / observation / PI-evidence review
                                     ↓
                     context and standardized system risk indices
                                     ↓
                    figures, tables, software checks, numerical audit
```

The experiment **does not** send PI review signals, human diagnoses or AI labels to the MATLAB reactor as control actions; thus physical process trajectories remain common within each run. C0–C3 injection labels are used for supervised learning/evaluation and scenario reporting, **not as direct runtime ground truth** that automatically validates agreement and resolution.

## 5. Scope of originality and limitations

The project is an **application and extension around an ASTE reference CSTR**, not a claim to have invented ASTE, the CSTR equations, PID control or the original Stateflow/safety design. The distinctive contribution is the **context-specific, history-dependent, evidence-gated Human–AI conflict estimator and its risk linkage**, evaluated on controlled fault scenarios.

The code's mathematical checks support correct numerical implementation; simulation comparisons support behavior under configured conditions. Neither independently proves that the latent probabilities, recovery likelihoods, human surrogate, or conditional losses describe actual industrial behavior. Mention this distinction in any code availability or validation statement.

## 6. Before public redistribution

The reference article may be open access; **source and compiled executable redistribution is still a separate legal question**. Check the original GitHub repository's actual license and the permission for the `.slx`, `.m` and `.mexw64` files, plus all contributor/institutional rights. If rights cannot be confirmed, do not publicly distribute the ASTE source/binary asset. Provide upstream acquisition instructions and publish only materials you are authorized to release. See [third-party and provenance documentation](THIRD_PARTY_AND_PROVENANCE.md).
