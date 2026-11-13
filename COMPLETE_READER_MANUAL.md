# Complete reader manual: purpose, pipeline, execution, evidence, limitations

This guide accompanies the four original release assets of **Human–AI Conflict in Intelligent Processing Systems: ASTE–CSTR Reproducibility**. It is written for a reviewer who has not previously used the simulation. Before attempting a run, read the [reference-system adaptation log](ASTE_ADAPTATIONS.md) and [exact execution protocol](REPRODUCE.md).

## 1. Aim and scientific questions

The research evaluates a **model of Human–AI diagnostic conflict**, not a new control algorithm for the plant. It asks:

1. Can unresolved diagnostic disagreements be retained as dynamic evidence rather than modeled as independent instantaneous events?
2. Can previous interactions be tracked **separately for different CSTR fault contexts**, so a past cooling issue does not automatically determine an inlet-fault conflict estimate?
3. Can persistence (length of an unresolved sequence) and recurrence (new unresolved episodes) be treated distinctly?
4. Can agreement be recorded as resolved only after an **eligible, same-issue, sensor-supported diagnostic verification**?
5. Can observation-based or PI-response evidence review change **subsequent simulated human diagnoses** under the same process/AI inputs?
6. How do these conflict estimates feed a **conditional risk index** under declared loss assumptions, without implying measured accidents?

The paper's six lemmas formalize consequences of its modeling assumptions and update rules. The software tests verify those consequences are respected in code; the CSTR data illustrate behavior under selected faults. That is **not empirical proof** of real operators or accident rates.

## 2. Reference platform and alterations

The CSTR is based on Markaj, Mercangöz and Fay's (2024) ASTE framework. ASTE supplies a MATLAB/Simulink environment with the CSTR process, PID regulatory control, fault engine, supervisory/operator model and safety functions. In this research the reactor/fault platform is **configured for repeatable offline diagnostic data generation**; operator/SIF intervention is disabled, and diagnostic policy actions do not modify the generated physical trajectories.

Three long, separately initialized reactor sequences (A/B/C) span **70,000 simulated seconds each**, with one-second physical observations. Operating fault factors are C1 inlet 0.8, C2 outlet 0.6 and C3 cooling 1.2; each sequence includes 47,000 C0 nominal, 8,500 C1, 6,000 C2 and 8,500 C3 seconds. C2 episodes longer than 500 s were removed after a 1,000-s test exceeded the selected level screen. The original source, revised fault schedules and tests are retained in Archive 1. See [full change table](ASTE_ADAPTATIONS.md).

## 3. The four source packages and major entry points

| Package | Input | Executable file | Main output |
|---|---|---|---|
| ASTE simulation | `.slx`, `.m`, `.mat` schedules, MATLAB environment | `ASTE_Long_Context_Feasible/run_input_check.py`, `run_duration_screen.py`, `run_long_sequences.py` | Fresh `run_A/B/C` physical CSVs under configured MATLAB runtime path |
| Human surrogate | Included reactor `input/run_*.csv` | `Human_Operator_ABC/human_operator_model.py` | `my_results/run_*/human_stage1_predictions.csv` and accuracy summaries |
| AI diagnosis | Included reactor `input/run_*.csv` | `AI_Operator_ABC/ai_fault_model.py` | `ai_results/run_*/ai_predictions_70000.csv`, model and metrics |
| Conflict/review/risk | Reactor, human and AI time-aligned inputs | `HA_Conflict_Paper_Complete/run_package.py` | `results/`, `paper/tables/`, `paper/figures/`, `paper/verification_results/` |

**Important:** Run the human/AI/conflict Python analysis without MATLAB by using the included reactor CSVs. To regenerate the *physical* CSVs, MATLAB/Simulink and additional ASTE environment files/screens are required; see §7.

## 4. Diagnostic pipeline and model

The human component is a stochastic finite-state surrogate with predefined physical evidence and uncertainty rules; it is **not learned from human participants**. Each A/B/C run resets state. The AI component is a Random Forest with 300 trees, minimum leaf size 2, balanced subsampling, random seed 42. It fits on all of run A; run B is validation and run C is designated retrospective held-out evaluation. Fault injection label `S_fault` is used for training/evaluation, not as an AI inference feature. The three model stages should use consistent `run_id` and `time_s`.

The conflict algorithm checks eligible pairwise diagnostic interpretations at **10-second** opportunities. It builds an issue-specific A/U/R record: **A** agreement without unresolved issue, **U** unresolved disagreement, **R** evidence-qualified resolution of that specific diagnostic issue. A latent high-conflict posterior **p(X=H)** is updated by Bayes' rule using configured likelihood pairs and a prediction dependent on retained context history. The duration variable **D** counts evaluated unresolved opportunities, and **M** counts new unresolved episodes. Ineligible evidence, inactive contexts and ordinary unverified label equality do not independently earn a posterior reduction.

Review conditions are **baseline** (fixed human model), **observation_review** and **pi_review**. Review can change later simulated human diagnostic interpretations through accepted modeled process evidence. It does not write a new posterior directly or send actuation commands to the CSTR. All arms in a run reuse the same reactor and fixed AI predictions. This is an **offline matched-model comparison**, not a physical randomized intervention.

## 5. Results the reader should inspect first

1. **Numerical audit:** `HA_Conflict_Paper_Complete/paper/verification_results/Audit_Report.json`. Saved report: PASS across 189,000 context records and 14,942 eligible Bayesian updates; maximum prediction residual 2.22045e−16, posterior residual 3.88578e−16; frozen-step posterior change 0. This checks software implementation under specified equations.
2. **Synthetic mechanism tests:** `paper/figures/Fig02_Controlled_Mechanisms.png` and `paper/tables/controlled_qualified_sequences.csv`. These exercise persistence, recurrence, unverified agreements and qualified recovery; they are designed traces, not plant trials.
3. **Context-specific trajectories:** `paper/figures/Fig04_Context_and_System_Conflict.png`. Run C context estimates are separate and system estimate is a **standardized weighted mixture**, not probability of any conflict anywhere.
4. **One matched C3 issue:** `paper/figures/Fig05_Matched_Fault_Period_Issue.png`. Demonstrates initial diagnostic agreement after PI evidence and possible renewed disagreement; a single illustrative issue does not measure sustained efficacy.
5. **Shared-case follow-up:** `paper/figures/Fig06_Common_Cohort_Recovery.png` and `paper/tables/common_cohort_landmarks.csv`. Run C C3, at 120 s: baseline 0/13, observation review 0/13, PI review 6/13. At 180 s, PI is 1/13; at 300 s, all arms are 5/13. This demonstrates **non-durable, time-dependent** behavior in a small dependent cohort.
6. **Risk:** `paper/figures/Fig07_Conditional_Risk.png`, `paper/tables/risk_summary.csv` and supplementary S08. Saved Run C equal-exposure system mean indices: baseline 0.00511622, observation 0.00467112, PI 0.00455979. These are **conditional assumption-based indices**, not risk of an observed accident or measured plant safety improvement.

The 400 consequence scenarios (seed 10601) are hypothetical and configurable. Their plotted 5th–95th percentile bands are **scenario envelopes**, not sampling confidence intervals. C0 is excluded from the system-risk exposure mixture; C1/C2/C3 each carry weight 1/3 independent of actual fault duration. Equalizing assumed conditional losses removes policy differences from conflict, and reversing loss ordering reverses the direction of ranking.

### Human/AI baseline diagnostic accuracy (source CSV summaries)

| Component | Run A | Run B | Run C | C3 recall in Run C |
|---|---:|---:|---:|---:|
| Simulated human surrogate | 84.64% | 84.51% | 84.77% | 0.79% |
| Random Forest AI | 99.97% (in sample) | 92.40% | 91.86% | 47.67% |

These figures compare classification outputs with **injected simulation labels**, which can cover onset/recovery periods and are not direct external ground truth. In-sample AI training accuracy is **not** evidence of independent generalization. Existing results are from saved outputs; rerunning with different Python/scikit-learn versions may change them.

## 6. Check provenance before comparing numbers

**This is critical for the journal.** The archived `HA_Conflict_Paper_Complete/results/run_manifest.json` records the **external** input mode for A/B/C, and its AI/human source hashes match the files in the standalone AI/Human ZIPs. Therefore, the saved figures/tables/audit must be interpreted as **external-standalone-input results**.

The conflict archive *also* includes `input/run_A|B|C/ai.csv` and `input/reference_ai_provenance.json`: these contain a **separate regenerated reference AI stream** with different file hashes. Running `run_bundled_reference.py` will use these and may produce somewhat different performance metrics, tables and figures. The separate modes must be named in reports and **not combined as if interchangeable**.

Two reproducibility levels should be reported:

- **Level 1: inspect the archived evidence** (zip integrity, files, original manifests and saved audit), no calculation rerun.
- **Level 2: rerun the conflict algorithm using unchanged standalone human/AI outputs** (`run_package.py`, external mode), which matches the provenance of the archived execution.

A **Level 3** extension retrains the AI, regenerates all human outputs and/or physically reruns ASTE; this is a new executed pipeline with new recorded software versions and potentially new hashes, requiring separate assessment. No result in this guide claims Level 3 was independently completed on a fresh computer.

## 7. Installation and running the simulations

### 7.1 Download and unpack

Open the GitHub **Releases** page, download the four named ZIP Assets to the directory containing this repository documentation, and run:

```bash
python scripts/prepare_archives.py --verify
python scripts/inspect_archive_reports.py
python scripts/summarize_archived_results.py
python scripts/prepare_archives.py --extract
```

The archive verification uses Python's standard library. It checks the exact original SHA-256 values despite the `1.`–`4.` renamed GitHub release asset filenames, member counts, ZIP CRC and path safety. It does not run the scientific pipeline. Ensure disk space for approximately 700 MB of extracted data plus generated outputs.

### 7.2 Python verification without running MATLAB

```bash
python -m venv .venv
# Activate as appropriate on Windows, macOS, or Linux
python -m pip install -r HA_Conflict_Paper_Complete/requirements.txt
python -m pip install -r Human_Operator_ABC/requirements.txt
python -m pip install -r AI_Operator_ABC/requirements.txt
python HA_Conflict_Paper_Complete/test_bayesian_audit.py
```

Check `HA_Conflict_Paper_Complete/SOFTWARE_TEST_REPORT.json` for status. These fixture tests check numerical rules and deliberately corrupted examples, not real-world validation.

### 7.3 Re-run the model used in the archive

Because all four unpacked packages are siblings and contain the saved external human and AI prediction files, use:

```bash
python HA_Conflict_Paper_Complete/run_package.py
```

Before running, **copy the extracted folder** because the runner regenerates `results/`, figures, summaries and audit files. Inspect the freshly written `HA_Conflict_Paper_Complete/results/run_manifest.json`; it should say `source_mode = external` for all runs. Review `paper/completion.json` and independent audit reports. Compare numerically rather than insisting on bitwise equality across unpinned software stacks.

### 7.4 Alternative separate bundled-reference experiment

```bash
python HA_Conflict_Paper_Complete/run_bundled_reference.py
```

This uses `input/` inside the conflict package, **not** the separate AI ZIP predictions. Archive resulting outputs under a **different folder or version**, and describe the different provenance when comparing to the article.

### 7.5 Full simulated human/AI re-execution

```bash
python Human_Operator_ABC/human_operator_model.py
python Human_Operator_ABC/plot_human_operator.py
python AI_Operator_ABC/ai_fault_model.py
python AI_Operator_ABC/plot_ai_results.py
python HA_Conflict_Paper_Complete/run_package.py
```

Run A alone trains the AI; B and C remain evaluation data. A different package/environment may produce new model/prediction file hashes. The conflict runner checks external hashes; if they mismatch, **do not bypass verification or replace inputs silently**. Record changed versions and results in a distinct scientific release.

### 7.6 Recreate the physical ASTE reactor data (advanced; environment-specific)

The ASTE package describes a Windows MATLAB/Simulink workflow: `D:/ASTE_LONG/` runtime, compiled `.mexw64`, existing duration-screen summary, and revised source/fault schedules. Follow its own `README.md` and `INPUT_FORMAT_FIX.md`. The intended order on a compatible system is:

```bash
python ASTE_Long_Context_Feasible/run_input_check.py
python ASTE_Long_Context_Feasible/run_duration_screen.py
python ASTE_Long_Context_Feasible/run_long_sequences.py
python ASTE_Long_Context_Feasible/plot_reactor_results.py
```

**Do not assume these four scripts are a clean plug-and-play cross-platform MATLAB rerun:** the long-run driver checks a pre-existing matching `D:/ASTE_LONG/duration_screen_summary.csv` and a local MATLAB/Simulink environment with necessary toolboxes/compiler support. A new researcher may need to generate the duration-screen summary, adapt platform paths, validate MATLAB version, and preserve runtime provenance. Failed stress cases are explicitly retained and not part of accepted active long runs. In the supplied ASTE README, a fresh 70,000-s triple MATLAB rerun was **not** performed as part of that particular packaging step.

## 8. What the data do—and do not—justify

- **Supported:** numerical integrity of the implemented update equations; distinct retained context trajectories; evidence-gated issue-level updates; simulation-based difference in diagnostic review outcomes; conditional assumed-risk mapping.
- **Not supported without new validation:** latent conflict posterior calibration against real operators; independent-trial significance; actual physical plant improvements from review; measured accident probabilities; reliable generalization to different plants/faults.
- **Potential next tests:** matched history-independent model ablation, new fault orders and parameters, other plant models, real human diagnostics, independent software rerun with frozen environment, conditional-loss elicitation. These are **future work**, not completed evidence.

## 9. Contributor and reviewer checklist

| Item | Evidence to inspect | Acceptance condition |
|---|---|---|
| Four archives present | GitHub Release → Assets | Exact four full ZIP files and expected SHA-256 values |
| File identity/contents | `scripts/prepare_archives.py --verify` | All pass, no LFS pointers/corruption |
| Source provenance | `results/run_manifest.json` | Archived source mode and hashes match standalone AI/human inputs |
| Tests | `test_bayesian_audit.py`, `Audit_Report.json` | Recorded vs newly executed status kept distinct |
| Correct statistical interpretation | `common_cohort_landmarks.csv` | Matched cohorts; small dependent samples noted |
| Conditional risk | `config.json`, risk CSV and S08 | Assumptions, exposure weights and bands correctly labeled |
| ASTE authorization | Upstream source/binary permissions | Permission verified before making release public |
| Scientific citation | Published GitHub tag, Zenodo DOI, article | Actual stable links, not draft `untagged-*` |

## 10. What to cite

Cite **both** the original ASTE reference (Markaj, Mercangöz & Fay, 2024; https://doi.org/10.1016/j.compchemeng.2024.108798) **and** the versioned archive of this research when released. Cite the journal article when it exists. A source reference is not equivalent to permission to redistribute third-party executable components.
