# Reproduce the archived analysis — exact reader workflow

## 0. Distinguish the three tasks

- **Inspect saved results (no MATLAB / no ML training):** archive verification, saved report inspection and numerical result summary.
- **Recompute saved conflict results:** use the standalone A/B/C human/AI output files in the other two ZIPs and run `HA_Conflict_Paper_Complete/run_package.py`. This matches the archived `external` input-mode provenance.
- **Regenerate everything:** rerun human surrogate, fit AI on A, and optionally run MATLAB/Simulink ASTE. This is a **new scientific execution** that must be versioned and compared, and may not produce identical hashes.

## 1. Download the data

At https://github.com/Rajeevan-A/human-ai-conflict-CSTR-reproducibility/releases open the **published** software release and download **all four Assets** to your repository/documentation folder:

```
1.ASTE_Long_Context_Feasible.zip
2.Human_Operator_ABC.zip
3.AI_Operator_ABC.zip
4.HA_Conflict_Paper_Complete.zip
```

While the release remains a **Draft**, ordinary readers cannot see/download its assets. A browser download from **Releases** does not require the Git command-line or Git LFS. The `Code → Download ZIP` archive does **not** include release assets.

## 2. Verify all four files

Run from the documentation root (where `scripts/` is located):

```bash
python scripts/prepare_archives.py --verify
python scripts/inspect_archive_reports.py
python scripts/summarize_archived_results.py
```

These scripts use Python standard libraries and inspect historical files; **they do not rerun the model**. Expect four SHA-256 passes and reports showing `external` input provenance. The script also accepts the original unnumbered user-upload filenames because their SHA-256 values are identical.

## 3. Extract source and data

```bash
python scripts/prepare_archives.py --extract
```

Your filesystem will then contain `ASTE_Long_Context_Feasible/`, `Human_Operator_ABC/`, `AI_Operator_ABC/`, `HA_Conflict_Paper_Complete/`, `docs/` and `scripts/` as sibling folders. Extraction verifies first and refuses unsafe paths; if an extracted folder already exists, the script skips it to avoid overwriting your work. To rerun from clean input, work on a newly extracted copy.

## 4. Environment

Python 3.9 was used in original operator-development notes, but versions are **not fully pinned** in the source `requirements.txt` files. Record `python --version` and `python -m pip freeze` after installation. On some computers, old scikit-learn `joblib` files cannot be deserialized by a new version; avoid loading unknown `.joblib` files from untrusted repositories.

```bash
python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows cmd:
# .venv\Scripts\activate.bat
# Windows PowerShell:
# .venv\Scripts\Activate.ps1
python -m pip install -r HA_Conflict_Paper_Complete/requirements.txt
python -m pip install -r Human_Operator_ABC/requirements.txt
python -m pip install -r AI_Operator_ABC/requirements.txt
```

## 5. Controlled software tests

```bash
python HA_Conflict_Paper_Complete/test_bayesian_audit.py
```

Review `HA_Conflict_Paper_Complete/SOFTWARE_TEST_REPORT.json`, including tamper detection, posterior continuity, frozen histories and same-issue epoch checks. The tests are synthetic software fixtures, not a validation experiment with humans.

## 6. Recompute the model corresponding to the saved article outputs

**This is the recommended reproduction path.** The historical `results/run_manifest.json` in Archive 4 identifies `external` human and AI streams, whose hashes match the standalone ZIPs. Preserve an untouched copy first because outputs are rewritten.

```bash
python HA_Conflict_Paper_Complete/run_package.py
```

The runner executes `run_conflict_model`, `verify_model`, `plot_article_figures`, `run_bayesian_audit` and `publish_paper`. Check:

- `HA_Conflict_Paper_Complete/results/run_manifest.json`: `inputs.run_A/B/C.source_mode = external`.
- `HA_Conflict_Paper_Complete/paper/completion.json`: `status = PASS` after the *new* execution.
- `HA_Conflict_Paper_Complete/paper/verification_results/Audit_Report.json`: `status = PASS`; compare max residuals and eligible update totals with archived report.
- `HA_Conflict_Paper_Complete/paper/tables/common_cohort_landmarks.csv` and `risk_summary.csv`: compare with published tables.
- `HA_Conflict_Paper_Complete/paper/figures/` and `paper/supplementary_figures/`: generated figures and figure data.

A changed software stack can yield non-bitwise-identical results even if model equations are the same; report any discrepancy rather than silently overwriting the reference version.

## 7. Separate bundled-reference computation (NOT the saved external-input outputs)

```bash
python HA_Conflict_Paper_Complete/run_bundled_reference.py
```

This chooses the different AI data in `HA_Conflict_Paper_Complete/input/run_*/ai.csv` and `input/reference_ai_provenance.json`. The original archived results' **external** mode and this **bundled_reference** mode are different. Do not report the resulting figures as exact replicas without checking. Run them in separate copies/directories.

## 8. Fresh human and AI predictions (another independent executed variant)

```bash
python Human_Operator_ABC/human_operator_model.py
python Human_Operator_ABC/plot_human_operator.py
python AI_Operator_ABC/ai_fault_model.py
python AI_Operator_ABC/plot_ai_results.py
python HA_Conflict_Paper_Complete/run_package.py
```

AI runs A/B/C have **TRAIN / VALIDATION / TEST** roles, 70,000 records each; fit happens on A only. The human surrogate resets for each run. The AI classifier is saved/reloaded; check each stage's manifest before the downstream model. All scripts overwrite their generated outputs; use a clean working copy. Input/output hash changes should be recorded as a new provenance record, not disguised as the archived run.

## 9. MATLAB/Simulink ASTE physical data regeneration

The original ASTE model **is not needed** to rerun the saved Python conflict analyses, because the physical reactor CSVs are included. Full physical regeneration is platform-dependent:

- Environment: Windows-style `D:/ASTE_LONG/` location, MATLAB/Simulink, necessary toolboxes and compiled `.mexw64` component compatible with the MATLAB version/architecture. Original ASTE publication describes MATLAB/Simulink 2022b, but the archive does not prove that any arbitrary newer release works.
- Read `ASTE_Long_Context_Feasible/README.md`, `INPUT_FORMAT_FIX.md`, `C2_REJECTION_REVIEW.md` and `experiment_design.json` before execution.
- The runner checks a pre-existing duration-screen summary and physical/fault hashes; regenerating the screen summary may be required on a new system.
- Once configured, the intended sequence is `run_input_check.py`, `run_duration_screen.py`, `run_long_sequences.py` and `plot_reactor_results.py`. The original package notes its long-run MATLAB runs were not executed *during the revised package preparation*. Verify the actual new result status and physical bounds.
- Never relabel a 1,000-s C2 out-of-envelope stress case as an accepted main run.

## 10. Expected saved-result interpretation

See [complete manual](COMPLETE_READER_MANUAL.md), [six-lemma map](RESULTS_AND_LEMMAS.md), [test protocol](TESTING_PROTOCOL.md), [ASTE differences](ASTE_ADAPTATIONS.md), and [source provenance](THIRD_PARTY_AND_PROVENANCE.md). The study's conflict posterior is a model inference; the risk index depends on hypothetical scenario losses. Avoid language of measured accident frequency or physical intervention efficacy.
