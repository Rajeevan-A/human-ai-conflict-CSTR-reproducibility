# Human–AI Conflict in Intelligent Processing Systems — ASTE–CSTR Reproducibility

**Research materials for _Human–Artificial Intelligence Conflict in Intelligent Processing Systems: A Modeling Perspective_.**  
**Reference platform:** the Autonomous Systems Training Environment (ASTE) CSTR described by Markaj, Mercangöz & Fay (2024), *Computers & Chemical Engineering* **189**, 108798, https://doi.org/10.1016/j.compchemeng.2024.108798.

> **Status: draft research release, not yet a public, independently validated software release.** The four complete source archives are attached to a **GitHub Release**, **not** the Code tab. A draft release is only available to the owner/collaborators with access. Consult the [publication checklist](RELEASE_CHECKLIST.md) before publishing; ASTE source/binary redistribution rights must be resolved.

## Research objective

To examine how **issue-qualified repeated human–AI diagnostic interactions** affect context-specific estimated conflict states and downstream **conditional, scenario-based risk indices**. The study builds on the ASTE–CSTR process simulation but does **not** claim empirical human-operator validation, intervention on the physical process, or measured accident-risk reduction.

## What is new relative to the ASTE reference framework?

The original ASTE provides a modular MATLAB/Simulink process and supervisory/safety simulation environment. The supplied research adaptation retains its CSTR plant/regulatory-control basis while configuring a **70,000-second, deterministic scheduled-fault, offline diagnostic study** in three distinct runs A/B/C. The project then adds **a separate stochastic finite-state human diagnostic surrogate**, **a Random Forest fault classifier**, **an issue-specific A/U/R interaction ledger**, **a context-specific Bayesian low/high conflict estimator with persistence/recurrence**, **two evidence-review policies**, and **a conditional consequence-risk index**. These diagnostic components are additional research modules, **not new ASTE plant physics**. No human/AI review action is sent back to actuate the reactor. Read [exact differences and qualifications](docs/ASTE_ADAPTATIONS.md).

## Access the four original study archives

Navigate to **[Releases](https://github.com/Rajeevan-A/human-ai-conflict-CSTR-reproducibility/releases)** and open **Human–AI Conflict ASTE–CSTR Research Model**. Under **Assets**, download *all four* archives. They are not visible as individual source files under **Code**.

| Release asset filename | Approx. size | Contents |
|---|---:|---|
| `1.ASTE_Long_Context_Feasible.zip` | 736 KB | ASTE MATLAB/Simulink source, CSTR fault schedules and experiment scripts |
| `2.Human_Operator_ABC.zip` | 16.7 MB | Human diagnostic surrogate, A/B/C reactor input CSVs, saved predictions and evaluations |
| `3.AI_Operator_ABC.zip` | 54.2 MB | Random Forest training/evaluation scripts, saved classifier, A/B/C predictions |
| `4.HA_Conflict_Paper_Complete.zip` | 129 MB | Conflict-model source, inputs/outputs, review policies, risk, audit, tables and figures |

**The four release assets are renamed copies of the original uploads. Their SHA-256 identities are unchanged** and are listed in [`archive_manifest.json`](archive_manifest.json). **Do not rename any content inside the ZIPs.** The archive-check script accepts both numbered release filenames and original upload names.

### Quick start — read saved results (no MATLAB, no Git required)

1. Download all four assets under **Releases → Assets** and put them in the **same folder** as this README, `scripts/`, `docs/`, and `archive_manifest.json`. Do not place the documentation ZIP itself in the folder; **extract the documentation first**.
2. Install Python 3.9 or another Python 3 version compatible with the dependencies used in the source code. For the following **archive inspection** you only need Python's standard library.
3. From that folder run:

```bash
python scripts/prepare_archives.py --verify
python scripts/inspect_archive_reports.py
python scripts/summarize_archived_results.py
```

4. To extract all four archives as sibling source-code directories:

```bash
python scripts/prepare_archives.py --extract
```

**No Git CLI is required for readers downloading release assets.** Draft releases are inaccessible to ordinary public readers; these steps apply to the owner now and to readers **after a release is published and accessible**.

### Reproduce the archived external-input model and figures

The *saved* conflict model's `results/run_manifest.json` says `source_mode: external` for A/B/C. Their AI/human SHA-256 hashes **match the separate standalone AI and human ZIPs**. This is the provenance of the saved figures, tables and audit, and is the recommended way to attempt reproduction from the original supplied files:

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1 ; Windows cmd: .venv\Scripts\activate.bat
# macOS/Linux: source .venv/bin/activate
python -m pip install -r HA_Conflict_Paper_Complete/requirements.txt
python -m pip install -r Human_Operator_ABC/requirements.txt
python -m pip install -r AI_Operator_ABC/requirements.txt
python HA_Conflict_Paper_Complete/test_bayesian_audit.py
python HA_Conflict_Paper_Complete/run_package.py
```

`run_package.py` uses the **standalone human/AI outputs** in their sibling directories and runs structural checks, figures/tables, sensitivity tests and the independent Bayesian numerical audit. **It overwrites generated outputs**, so make a fresh working copy first. Confirm `results/run_manifest.json` identifies every run as `external` and matches source hashes.

**Alternative, separate experiment:** `python HA_Conflict_Paper_Complete/run_bundled_reference.py` uses the included *different* reference AI predictions and produces potentially different outputs. **Do not mix those results with the saved external-input results or cite the two modes as identical.** Full MATLAB/Simulink recreation is an additional, system-specific workflow; see [reproduction instructions](docs/REPRODUCE.md).

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
