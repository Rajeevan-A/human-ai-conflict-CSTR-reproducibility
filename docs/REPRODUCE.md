# Reproduction guide: four original archives

**Choose the workflow before running.** This archive supports inspection of the saved results, a clean conflict-model rerun using the enclosed bundled reference stream, and an optional separately provenance-checked complete Python pipeline. MATLAB CSTR regeneration has additional external prerequisites.

## A. Get the ZIP files and check integrity

Install Git and Git LFS; after cloning:

```bash
git lfs pull
python scripts/prepare_archives.py --verify
python scripts/prepare_archives.py --extract
```

Check that all four extracted directories are direct siblings of `docs` and `scripts`. The script refuses wrong SHA-256 contents, Git LFS pointer stubs, corrupted ZIP members or unsafe extraction paths. If original ZIP names or contents change, publish an updated `archive_manifest.json` with a new version instead of disabling checks.

## B. Inspect existing archived results without modifying them

```bash
python scripts/inspect_archive_reports.py
```

This examines saved report status within the uploaded conflict ZIP. It does not execute scientific simulations, cannot replace independent reruns and does not show that empirical validation occurred. After extraction, read `HA_Conflict_Paper_Complete/paper/README.md`, `paper/appendix/Model_Verification_Results.md`, `paper/tables/`, and `paper/verification_results/`.

## C. Python environment

For portability use a fresh environment and record `python --version`, `python -m pip freeze`, OS and hardware. The supplied packages provide **unpinned** dependency requirements; this archive is not a locked environment and exact bit-for-bit rerun outcomes are not guaranteed across versions. Typical dependencies are numpy, pandas, matplotlib, scikit-learn, and joblib. A fresh run may require more memory/time than audit inspection. On Windows use `.venv\Scripts\activate` rather than the Unix activation line.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r HA_Conflict_Paper_Complete/requirements.txt
python -m pip install -r Human_Operator_ABC/requirements.txt
python -m pip install -r AI_Operator_ABC/requirements.txt
```

## D. Run the supplied synthetic software checks

```bash
python HA_Conflict_Paper_Complete/test_bayesian_audit.py
```

The executable creates/overwrites `HA_Conflict_Paper_Complete/SOFTWARE_TEST_REPORT.json` and verifies numerical consistency and tamper detection on constructed traces; it does not use the external reactor runs. Check the `status` and failed assertions. Only refer to the printed pass after running it in your environment.

## E. Recompute archived bundled-reference figures and tables

**This is the recommended first executable reproduction path**, because it does not depend on recomputing human or AI predictions or on MATLAB installation. Save an unmodified copy of the archive first because outputs in the extracted tree are overwritten.

```bash
python HA_Conflict_Paper_Complete/run_bundled_reference.py
```

This explicitly chooses `bundled_reference` input mode. `run_package.py` automatically invokes conflict simulation, structural verification, result figure/table export, numerical Bayesian audit and manuscript-output packaging. After completion inspect:

- `HA_Conflict_Paper_Complete/results/completion.json` and `paper/completion.json` (must say PASS for this execution).
- `HA_Conflict_Paper_Complete/paper/tables/` and `paper/figures/` for model and result outputs.
- `HA_Conflict_Paper_Complete/paper/verification_results/` for numerical audit evidence.
- `HA_Conflict_Paper_Complete/results/run_manifest.json` for exact input-mode and file SHA-256 provenance.

The supplied article results are generated with the **bundled reference AI predictions**, not silently with the separate uploaded `AI_Operator_ABC` predictions. Model settings are in `config.json`, and software warnings are in `START_HERE.md` and `paper/README.md`.

## F. Full source-derived Python pipeline (separate provenance mode)

This path makes fresh human and AI outputs from their included reactor CSVs. It is **not guaranteed to reproduce the archived reference AI bytes**. The conflict runner checks matching files, hashes, model artifact and manifests before proceeding.

```bash
python Human_Operator_ABC/human_operator_model.py
python Human_Operator_ABC/plot_human_operator.py
python AI_Operator_ABC/ai_fault_model.py
python AI_Operator_ABC/plot_ai_results.py
python HA_Conflict_Paper_Complete/run_package.py
```

Run each command with the extracted folders as siblings; the scripts use their own file locations. **Rerunning overwrites local stage outputs.** AI fitting occurs on A only, with B and C reserved for evaluation; all classifier/model versions and output hashes must be kept with subsequent conflict execution. `run_package.py` enters external/auto mode when complete sibling packages are present. Confirm `results/run_manifest.json` reports `external` after executing this workflow. If the run fails validation, do not copy bundled reference predictions into external files to force success; diagnose the manifest mismatch.

## G. Physical CSTR regeneration with MATLAB/Simulink

The physical package is `ASTE_Long_Context_Feasible/`. It includes `run_input_check.py`, `run_duration_screen.py`, `run_long_sequences.py`, source/SLX and MAT schedules. Its README requires a matching, previously generated duration-screen summary from a historical `D:/ASTE_LONG` directory; it also uses environment-specific output paths and a Windows compiled `.mexw64`. Adaptation and an actually available MATLAB license, toolbox/source components and platform are required. The four archives alone **do not establish that a fresh ASTE run is executable on any new computer**. Do not present this as a one-command portable CSTR rerun; follow its README and record any path/configuration changes as a new execution manifest.

A validated new reactor trajectory would require rerunning the human, AI and conflict stages using the **same** new physical data and maintaining the A/B/C partition and input hashes. Do not mix current input files with outputs from a different CSTR version.

## H. Scientific output checks

See [`TESTING_PROTOCOL.md`](TESTING_PROTOCOL.md) and [`RESULTS_AND_LEMMAS.md`](RESULTS_AND_LEMMAS.md). Do not claim that synthetic pass status verifies real human cognition, probability calibration or actual accident reduction. Preserve the original ZIPs and create a new tagged release whenever science-relevant assumptions or source outputs change.
