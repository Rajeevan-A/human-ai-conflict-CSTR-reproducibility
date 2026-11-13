# Regenerating ASTE–CSTR data in MATLAB/Simulink

This document describes the physical simulation in Release Asset 1, `1.ASTE_Long_Context_Feasible.zip`. **MATLAB is necessary for fresh reactor simulation.** The saved CSVs in Release Assets 2–4 allow the separate Human–AI analyses to be examined and rerun **without MATLAB**.

## 1. Software and platform requirements

- **MATLAB with Simulink.** The supplied `v122_core.py` header identifies **MATLAB R2023b + Simulink** as its intended configuration. This is a code-declared environment, not a certified cross-version compatibility matrix.
- **Additional MathWorks products required by the original `cstr_simulationEnv.slx` model:** verify with MathWorks licensing and the local model. The model contains control, fault and supervisory components. This package has not independently certified every required toolbox on a clean machine.
- **Windows 64-bit is the safest initial reproduction target.** The bundle includes `source/cstr_simulationEnv_sfun.mexw64`, a Windows 64-bit compiled component. It may be incompatible with other operating systems, architectures, or MATLAB releases.
- **Python 3.9, 3.10 or 3.11 (64-bit)** for the R2023b MATLAB Engine interface. Check the [MathWorks Python compatibility table](https://www.mathworks.com/support/requirements/python-compatibility.html) if using another MATLAB version.
- **MATLAB Engine API for Python**, installed to the **same Python interpreter** used to start the scripts. For R2023b, MathWorks publishes version `23.2.3`; see [the version-specific package](https://pypi.org/project/matlabengine/23.2.3/) and the [official installation guide](https://www.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html). `pip install matlabengine` without a version can install an engine targeting a different MATLAB release.
- Python packages listed in `ASTE_Long_Context_Feasible/requirements.txt`: `numpy`, `scipy`, `matplotlib`.
- A working MATLAB installation and license. GitHub does not execute `.slx` MATLAB simulations on its web page.

## 2. Download and extract

1. Visit [the repository's Releases page](https://github.com/Rajeevan-A/human-ai-conflict-CSTR-reproducibility/releases) and download `1.ASTE_Long_Context_Feasible.zip` under **Assets** (the existing draft is only accessible to its owner/collaborators).
2. Extract it locally. The archive contains a top-level `ASTE_Long_Context_Feasible` folder. Do not run from inside the ZIP viewer.
3. Confirm that the extracted folder contains `experiment_design.json`, `experiment_driver.py`, `v122_core.py`, `run_input_check.py`, `run_duration_screen.py`, `run_long_sequences.py`, `plot_reactor_results.py`, `requirements.txt`, `schedules/`, `tables/` and `source/`.
4. `source/` should contain `cstr_simulationEnv.slx`, `cstrm.m`, `init_data.mat`, `aste_run_v122.m` and the `.mexw64` component. The run launcher copies the appropriate saved schedule to the required runtime filename `fault_schedule_50000.mat` automatically. **Do not manually insert or replace physical measurements**.

## 3. Install the Python side of the MATLAB interface

Open Windows Command Prompt or PowerShell. Select a 64-bit Python version compatible with the installed MATLAB release, then run:

```bash
python --version
python -m pip install -r ASTE_Long_Context_Feasible/requirements.txt
python -m pip install matlabengine==23.2.3
python -c "import matlab.engine; print('MATLAB Engine import OK')"
```

The `matlabengine==23.2.3` command above is **for MATLAB R2023b**; do not use it blindly with another release. See the official MathWorks compatibility table and installation documentation. If you prefer, install the Engine API from your installed MATLAB `extern/engines/python` directory following the MathWorks guide.

**Optional functional startup check** (it starts MATLAB and requires a valid license):

```bash
python -c "import matlab.engine; eng=matlab.engine.start_matlab(); print(eng.version()); eng.quit()"
```

If this fails, fix Python–MATLAB Engine compatibility or licensing **before** running the reactor scripts.

## 4. Set the runtime directory before running

**The supplied launcher uses `D:/ASTE_LONG/`** as the default output location in `ASTE_Long_Context_Feasible/experiment_driver.py`:

```python
RUNTIME = Path('D:/ASTE_LONG')
```

On a Windows computer with no `D:` drive, change this to an existing **short absolute path**, e.g. `Path('C:/ASTE_LONG')`, before starting new runs. If changed, make the same adjustment in `ASTE_Long_Context_Feasible/plot_reactor_results.py`. The underlying simulator checks that trial output paths are short (at most 55 characters), and stores results in the runtime folder, **not** inside the GitHub ZIP. This is a local output-path configuration change, not a proposed modification to the reactor equations.

## 5. Read the experiment design and model adaptations

Read `ASTE_Long_Context_Feasible/README.md`, `INPUT_FORMAT_FIX.md`, `C2_REJECTION_REVIEW.md` and `experiment_design.json`. In this study the original CSTR physics and regulatory PID are retained, but the fault inputs and operating configuration are adapted for offline comparisons:

| Context | Operating modification | Seconds in each A/B/C run |
|---|---|---:|
| C0 | Nominal condition, no scheduled fault | 47,000 |
| C1 | Inlet flow multiplier 0.8 | 8,500 |
| C2 | Outlet flow multiplier 0.6 | 6,000 |
| C3 | Cooling-response multiplier 1.2 | 8,500 |

Each run lasts **70,000 s** with 1 s physical logging; A/B/C have different scheduled fault order. The scheduled 1,000 s C2 case was excluded from the accepted long runs after exceeding a configured research screening level; its report remains a separate rejected stress case. The nominal inlet flow command is 3.5; operator and safety-instrumented-function actuation is disabled **for these offline research trajectories**. This is not safety certification of the CSTR.

## 6. Execute the physical reactor tests, in order

Run from a **fresh extracted working folder** containing the `ASTE_Long_Context_Feasible` directory. The user can run these commands in a terminal or open each corresponding `.py` in Spyder and press F5 (as the original package README describes).

**A. Input-format check:** One 2,200 s C1 model simulation checks the MATLAB workspace schedule and model interface:

```bash
python ASTE_Long_Context_Feasible/run_input_check.py
```

The runner reports `PROVISIONAL_SCREEN_PASS` or `FAILED_OR_REJECTED`; review `driver_error.txt` and physical validation reports after any failure. The software verifies the fault-enable arrays are finite MATLAB `double` and the original model source file is not altered on disk.

**B. Eight active duration-screen simulations:**

```bash
python ASTE_Long_Context_Feasible/run_duration_screen.py
```

The eight passing active tests are C1 200/500/1000 s, C2 200/500 s, and C3 200/500/1000 s. The excluded C2 1000 s stress case is *not* a required passing test. The runtime stores a `duration_screen_summary.csv` with status and source/schedule hashes.

**C. Full CSTR scenario runs A, B and C:**

```bash
python ASTE_Long_Context_Feasible/run_long_sequences.py
```

This script checks that the required screens passed, verifies matching model/schedule hashes, and then runs **three new 70,000-second MATLAB/Simulink simulations**. The driver reports pass/fail statuses in `long_sequence_summary.csv`; ending the script does not by itself certify success.

**D. Plot the new reactor output:**

```bash
python ASTE_Long_Context_Feasible/plot_reactor_results.py
```

The script saves physical plots beside each generated reactor CSV.

**Note:** These commands require a locally working MATLAB installation. This guide has not newly re-executed the three MATLAB reactor simulations; the archived results and verification come from the supplied project materials.

## 7. Where to find the newly produced results

By default, physical simulation outputs are written under:

```text
D:/ASTE_LONG/
  duration_screen_summary.csv
  long_sequence_summary.csv
  sources/
    run_A/ ...
    run_B/ ...
    run_C/ ...
  outputs/
    run_A/
      ASTE_v122_physical_70000.csv
      ASTE_v122_validation_70000.txt
      run_provenance.json
    run_B/
      ASTE_v122_physical_70000.csv
      ASTE_v122_validation_70000.txt
      run_provenance.json
    run_C/
      ASTE_v122_physical_70000.csv
      ASTE_v122_validation_70000.txt
      run_provenance.json
```

A failed or rejected trajectory may be saved with an `_REJECTED.csv` suffix instead of a passing physical CSV. Review validation text, driver errors and model source hashes before accepting any output. Some additional diagnostics are written per run and the exact contents can vary with execution outcomes.

## 8. Feed new reactor outputs into the human and AI models

The downstream **human** and **AI** packages include their own pre-existing reactor-input CSVs. They can be used to reproduce the original *archived* conflict results without running MATLAB. If you regenerate ASTE trajectories, you must explicitly build and validate the matching input schema and recompute human and AI diagnostic outputs for the **new** physical data, preserving the A/B/C training/evaluation split. Running the old saved classifiers against different inputs without new hashes/provenance **does not constitute exact reproduction** of the archived publication results. Read [the full data and model reproduction guide](REPRODUCE.md) and [source/provenance notes](THIRD_PARTY_AND_PROVENANCE.md).

## 9. Common problems

| Message or symptom | Likely cause or action |
|---|---|
| `ModuleNotFoundError: No module named 'matlab.engine'` | Install the version-matched MATLAB Engine for the same Python interpreter |
| MATLAB Engine import succeeds but MATLAB does not start | Check installed MATLAB, license, Python version, and architecture |
| Missing `fault_schedule_50000.mat` in original `source/` | Normal: the Python launcher stages the appropriate `run_A.mat` or screen schedule under that name before simulation |
| `D:/ASTE_LONG` output not found | Configure a valid runtime path in `experiment_driver.py` and `plot_reactor_results.py` |
| Duration-screen hash mismatch | Confirm active MAT schedules and `.slx` correspond to the same extracted package; do not bypass the check |
| `FAILED_OR_REJECTED` | Read the per-case validation text and `driver_error.txt`; do not label the run as accepted |
| Missing `.mexw64` or incompatible compiled component | Check Windows/MATLAB binary compatibility and upstream source/license prerequisites |

## Reference

Markaj, A., Mercangöz, M., & Fay, A. (2024). *Design and implementation of an Autonomous Systems Training Environment framework for control algorithm evaluation in autonomous plant operation.* Computers & Chemical Engineering, 189, 108798. https://doi.org/10.1016/j.compchemeng.2024.108798

**Third-party rights:** This study adapts an ASTE reference model. Redistribution of `.slx`, `.m`, and `.mexw64` components requires a separate license/permission check before publishing the Release asset.
