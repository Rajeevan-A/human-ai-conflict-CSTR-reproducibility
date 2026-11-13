# Human–AI Conflict in Intelligent Processing Systems — ASTE–CSTR Reproducibility

**Companion research software and archived data for _Human–Artificial Intelligence Conflict in Intelligent Processing Systems: A Modeling Perspective_.**  
**Original process-simulation reference:** Markaj, Mercangöz & Fay (2024), *Computers & Chemical Engineering*, 189, 108798. [https://doi.org/10.1016/j.compchemeng.2024.108798](https://doi.org/10.1016/j.compchemeng.2024.108798).

> **Research release status: **Version v1.0.0** is publicly available. The four research model archives can be downloaded from GitHub Release v1.0.0. Release attachments are separate from the repository's Code tab..

## START HERE — download all four research models

**[OPEN THE FOUR MODEL ARCHIVES IN RELEASES](https://github.com/Rajeevan-A/human-ai-conflict-CSTR-reproducibility/releases)**  
Repository owner: open the [Published Release v1.0.0](https://github.com/Rajeevan-A/human-ai-conflict-CSTR-reproducibility/releases/tag/untagged-e67c10659ea266dcf9e9), then open **Assets**. When this release is eventually published, its tag/URL may change; the stable **Releases** link above remains the reader entry point.

| Release asset — download each ZIP | Contents | Needed for |
|---|---|---|
| `1.ASTE_Long_Context_Feasible.zip` (736 KB) | Adapted ASTE CSTR MATLAB/Simulink `.slx`, MATLAB `.m`, fault schedules, MATLAB-driving Python scripts | **Fresh physical reactor simulation** |
| `2.Human_Operator_ABC.zip` (16.7 MB) | Simulated human diagnostic surrogate, A/B/C data and saved outputs | Human diagnostic analysis |
| `3.AI_Operator_ABC.zip` (54.2 MB) | Random Forest fault classifier, saved predictions/model, A/B/C data | AI diagnostic analysis |
| `4.HA_Conflict_Paper_Complete.zip` (129 MB) | Context-specific Bayesian conflict model, diagnostic review, risk, verification, figures and tables | **Reproduce paper results** |

**Do not use `Code → Download ZIP` to obtain these four archives.** That command only downloads files committed in the Code tab, not uploaded Release assets. To inspect their contents, download each asset and extract it locally. Full instructions: [download and extraction](docs/DOWNLOAD_ALL_FOUR_MODELS.md).

## Which software do you need?

| Goal | MATLAB required? | Required tools |
|---|---|---|
| Inspect saved figures, tables, and numerical audit | **No** | Python 3 (archive inspection uses Python standard library) |
| Recompute conflict, review and risk from saved human/AI outputs | **No** | Python 3 and package dependencies |
| Recompute human surrogate and Random Forest predictions | **No** | Python 3, NumPy, pandas, scikit-learn and package dependencies |
| **Regenerate the ASTE–CSTR reactor trajectory** | **Yes** | **MATLAB, Simulink, MATLAB Engine API for Python**, model-required toolboxes and Windows-compatible compiled component where used |

The ASTE launcher identifies **MATLAB R2023b + Simulink** as its intended environment. For R2023b, use compatible **64-bit Python 3.9–3.11** and a matching MATLAB Engine API, e.g. `python -m pip install matlabengine==23.2.3` (not an unversioned latest Engine package). Verify all MATLAB licenses and toolbox/model dependencies locally. **A successful full ASTE simulation is not established merely by downloading the archives.** See **[complete MATLAB setup and ASTE execution guide](docs/MATLAB_ASTE_SETUP.md)**.

## Run the archived results without MATLAB (quick start)

Place the four downloaded ZIPs alongside the repository's `scripts/` and `archive_manifest.json`. In that directory:

```bash
python scripts/prepare_archives.py --verify
python scripts/inspect_archive_reports.py
python scripts/summarize_archived_results.py
python scripts/prepare_archives.py --extract
```

The first three commands **inspect the existing saved outputs**; they do not recompute reactor or conflict results. To recompute the archived conflict model after extraction and dependency installation:

```bash
python -m pip install -r HA_Conflict_Paper_Complete/requirements.txt
python -m pip install -r Human_Operator_ABC/requirements.txt
python -m pip install -r AI_Operator_ABC/requirements.txt
python HA_Conflict_Paper_Complete/test_bayesian_audit.py
python HA_Conflict_Paper_Complete/run_package.py
```

**Important provenance:** the archived publication outputs use `external` human and AI prediction files from the separate ZIPs; the bundled reference AI stream in ZIP 4 is different. `run_package.py` rewrites outputs; preserve an untouched copy. See [full reproduction instructions](docs/REPRODUCE.md).

## Regenerate physical ASTE–CSTR data with MATLAB/Simulink

Once the ASTE archive is extracted and MATLAB Engine works from Python, the intended fresh-run order on a compatible Windows setup is:

```bash
python ASTE_Long_Context_Feasible/run_input_check.py
python ASTE_Long_Context_Feasible/run_duration_screen.py
python ASTE_Long_Context_Feasible/run_long_sequences.py
python ASTE_Long_Context_Feasible/plot_reactor_results.py
```

The launcher uses a Windows runtime path `D:/ASTE_LONG/` by default, which may need reconfiguration if that drive is absent. Each 70,000-second A/B/C trajectory is **simulated afresh in MATLAB**, not read back from a saved CSV. The full guide documents the prerequisites, runtime paths, screens and generated CSVs: **[MATLAB ASTE setup](docs/MATLAB_ASTE_SETUP.md)**.

---

## Research objective

To examine how **issue-qualified repeated human–AI diagnostic interactions** affect context-specific estimated conflict states and downstream **conditional, scenario-based risk indices**. The study builds on the ASTE–CSTR process simulation but does **not** claim empirical human-operator validation, intervention on the physical process, or measured accident-risk reduction.

## What is new relative to the ASTE reference framework?

The original ASTE provides a modular MATLAB/Simulink process and supervisory/safety simulation environment. The supplied research adaptation retains its CSTR plant/regulatory-control basis while configuring a **70,000-second, deterministic scheduled-fault, offline diagnostic study** in three distinct runs A/B/C. The project then adds **a separate stochastic finite-state human diagnostic surrogate**, **a Random Forest fault classifier**, **an issue-specific A/U/R interaction ledger**, **a context-specific Bayesian low/high conflict estimator with persistence/recurrence**, **two evidence-review policies**, and **a conditional consequence-risk index**. These diagnostic components are additional research modules, **not new ASTE plant physics**. No human/AI review action is sent back to actuate the reactor. Read [exact differences and qualifications](docs/ASTE_ADAPTATIONS.md).

## Where readers find the results

Once `4.HA_Conflict_Paper_Complete.zip` is extracted:

- `HA_Conflict_Paper_Complete/paper/figures/` — main figures 01–07 (PNG and PDF) and figure data.
- `HA_Conflict_Paper_Complete/paper/supplementary_figures/` — sensitivity and supporting plots.
- `HA_Conflict_Paper_Complete/paper/tables/` — comparison data, C3 common-cohort recovery, risk summary.
- `HA_Conflict_Paper_Complete/paper/verification_results/` — Bayesian numerical audit evidence.
- `HA_Conflict_Paper_Complete/results/run_manifest.json` — **source mode and SHA-256 provenance**.

See [results interpretation and lemma-evidence map](docs/RESULTS_AND_LEMMAS.md). Figure filenames are **development identifiers**; renumber to match the manuscript, not blindly as Fig01–07.

## Documentation index

| Guide | Reader question |
|---|---|
| [Download four research models](docs/DOWNLOAD_ALL_FOUR_MODELS.md) | Which ZIP to download, why Code does not display it, and how to extract it |
| [MATLAB/Simulink ASTE execution](docs/MATLAB_ASTE_SETUP.md) | Full MATLAB requirements, input checks, screens and fresh A/B/C reactor simulations |
| [Complete reader manual](docs/COMPLETE_READER_MANUAL.md) | What is the research, how does the pipeline work, what do the tests mean? |
| [Changes from the original ASTE](docs/ASTE_ADAPTATIONS.md) | What was inherited, reconfigured, disabled, and added? |
| [Reproduction and execution](docs/REPRODUCE.md) | How do I download, verify, extract, run and identify outputs? |
| [Testing protocol](docs/TESTING_PROTOCOL.md) | How are the six lemmas and numerical implementation checked? |
| [Results and lemmas](docs/RESULTS_AND_LEMMAS.md) | What can and cannot be concluded from figures and numerical values? |
| [Third-party source and provenance](docs/THIRD_PARTY_AND_PROVENANCE.md) | What can be redistributed? Which results come from which AI input? |
| [Publication next steps](docs/NEXT_STEPS_TO_PUBLICATION.md) | How to inspect the private draft, publish and cite a release? |
| [GitHub and publication guide](docs/GITHUB_AND_PUBLICATION.md) | Where does GitHub store source versus release attachments? |

## Scientific boundaries and reproducibility limitations

- Three **separately initialized** 70,000-second simulated sequences: **A** development/AI training, **B** validation, **C** designated retrospective test. They share a simulator and do not constitute independent plant trials.
- Each policy uses the **same reactor trajectory and fixed AI predictions** within a run. Review changes subsequent **simulated human interpretation**, **not reactor control**.
- The latent probability of higher conflict is a **model posterior under assigned transitions and likelihoods**, not an empirically calibrated frequency of conflict.
- Conditional risk assumes **400 hypothetical consequence scenarios**, seed 10601 and an equal-exposure mixture of C1/C2/C3. Risk bands describe *assumption scenarios*, not confidence intervals and not measured accident risk.
- No recorded human participants, industrial incident outcomes or prospective plant deployment are included. See the documentation before reporting effect size or statistical significance.

## Citation and attribution

**Original reference:** Markaj, A., Mercangöz, M., & Fay, A. (2024). Design and implementation of an Autonomous Systems Training Environment framework for control algorithm evaluation in autonomous plant operation. *Computers & Chemical Engineering, 189*, 108798. https://doi.org/10.1016/j.compchemeng.2024.108798

**This repository:** cite the actual versioned GitHub release and Zenodo DOI *after those exist*. The current release is a draft and has no confirmed final DOI; see [citation template](CITATION_TEMPLATE.md). A published article's open-access license does **not automatically license all associated MATLAB files/binaries**. Check upstream and author permissions before publishing those assets.
