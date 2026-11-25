# Human–AI Conflict in Intelligent Processing Systems — ASTE–CSTR Reproducibility

Research code, fixed simulation inputs, numerical verification, and figures supporting the manuscript *Human–Artificial Intelligence Conflict in Intelligent Processing Systems: A Modeling Perspective*.

The proposed framework uses **seven postulates and six lemmas** to represent human–AI conflict as a **context-specific, history-dependent process** and relate estimated conflict probability to conditional process risk. It is evaluated using an adapted Autonomous Systems Training Environment (ASTE) continuous stirred-tank reactor (CSTR) simulation.

**Upstream process-model reference:** Markaj, A., Mercangöz, M., & Fay, A. (2024). *Design and implementation of an Autonomous Systems Training Environment framework for control algorithm evaluation in autonomous plant operation*. *Computers & Chemical Engineering, 189*, 108798. https://doi.org/10.1016/j.compchemeng.2024.108798

## Download the research packages

**[GitHub Releases](https://github.com/Rajeevan-A/human-ai-conflict-CSTR-reproducibility/releases)** · **[Currently published release: v1.0.0](https://github.com/Rajeevan-A/human-ai-conflict-CSTR-reproducibility/releases/tag/v1.0.0)**

The published release currently contains these four assets. Download the fourth archive for the **revised human–AI conflict model and current manuscript figures**.

| Release asset | Contents | Purpose |
|---|---|---|
| [`1.ASTE_Long_Context_Feasible.zip`](https://github.com/Rajeevan-A/human-ai-conflict-CSTR-reproducibility/releases/download/v1.0.0/1.ASTE_Long_Context_Feasible.zip) | Adapted ASTE–CSTR MATLAB/Simulink model and simulation scripts | Regenerate the process trajectories, subject to MATLAB dependencies |
| [`2.Human_Operator_ABC.zip`](https://github.com/Rajeevan-A/human-ai-conflict-CSTR-reproducibility/releases/download/v1.0.0/2.Human_Operator_ABC.zip) | Simulated human diagnostic model and Runs A–C outputs | Upstream human diagnostic analysis |
| [`3.AI_Operator_ABC.zip`](https://github.com/Rajeevan-A/human-ai-conflict-CSTR-reproducibility/releases/download/v1.0.0/3.AI_Operator_ABC.zip) | AI fault classifier and Runs A–C outputs | Upstream AI diagnostic analysis |
| [`4.HA_Conflict_Model_and_All_Plots.zip`](https://github.com/Rajeevan-A/human-ai-conflict-CSTR-reproducibility/releases/download/v1.0.0/4.HA_Conflict_Model_and_All_Plots.zip) | **Revised** human–AI conflict model, fixed CSTR/human/AI input files, A–C results, numerical checks, final figures and plotting scripts | **Reproduce the current human–AI conflict analysis** |

The updated fourth archive is approximately **183 MiB** (191,688,058 bytes), SHA-256:

```text
76e366088601edfa275bf4724300e062f2e8b6937694ac00a2c4378f0e03a40b
```

**Version note:** The fourth archive currently hosted under the `v1.0.0` tag has been replaced with the updated model package. For a stable journal record, a **new, unchanged, versioned release** should be published and cited before final submission. The original release tag alone does not distinguish the archive versions. The repository's `archive_manifest.json` and `ARCHIVE_CHECKSUMS.sha256` must match the current assets.

Release ZIP assets are **not included** when selecting **Code → Download ZIP** on GitHub. Download them from the release's **Assets** section.

## Research model

The three algorithms implement the proposed framework:

1. **Algorithm 1 — Human–AI interaction outcomes:** maintains agreement (`A`), unresolved disagreement (`U`), and evidence-supported resolution (`R`) for each operating context. It distinguishes continuing disagreement from recurring episodes and requires repeated qualified agreement for resolution.
2. **Algorithm 2 — Conflict estimation:** updates a context-specific Bayesian posterior using retained unresolved duration (`D`), recurrence count (`M`), and interaction evidence, then computes a weighted system-level estimate.
3. **Algorithm 3 — Conflict-related risk:** combines the modeled probability of higher conflict, process severity, and assumed conditional consequences to calculate context-specific and system-level risk indices.

The ASTE–CSTR analysis uses **Run A** for diagnostic-model development/training, **Run B** for validation, and **Run C** for the manuscript's principal numerical tests. Each reactor simulation spans **70,000 seconds**; human–AI diagnostic comparisons are evaluated at **10-second intervals**. The model compares three review policies: **baseline**, **observation review**, and **PI evidence review**.

Contexts comprise normal operation (`C0`) and three abnormal operating conditions (`C1`–`C3`), including cooling-related context `C3`. In this controlled simulation, the injected fault labels select the context for analysis; the labels are not fed into the human or AI classifiers. This context-selection mechanism is **not** a validated method for identifying operating contexts in a real plant.

## Reproduce the updated human–AI analysis (without MATLAB)

Archive 4 includes the fixed reactor observations and human/AI diagnostic data, so **MATLAB is not required** to rerun the human–AI conflict and conditional risk calculations.

1. Download and extract `4.HA_Conflict_Model_and_All_Plots.zip`.
2. Open a terminal in its `HA_Conflict_Updated/Model/` directory.
3. Run:

```bash
python -m pip install -r requirements.txt
python test_bayesian_audit.py
python run_package.py
```

The main pipeline recomputes the **nine Run A/B/C × review-policy analyses**, numerical checks, and model-generated figures. It writes outputs into the model's `results/` and `paper/` folders. **Keep an untouched copy of the downloaded ZIP**, because rerunning may overwrite saved outputs.

For the detailed model configuration, input provenance, figure-generation scripts, and limitations, see the files inside the ZIP:

- `HA_Conflict_Updated/START_HERE.md` — package map and current figure numbering.
- `HA_Conflict_Updated/Model/START_HERE_REVISED.md` — revised implementation and execution instructions.
- `HA_Conflict_Updated/Model/results/run_manifest.json` — source mode, input hashes, configuration, and environment details.
- `HA_Conflict_Updated/Model/results/verification.json` — numerical verification.
- `HA_Conflict_Updated/Model/config.json` — Bayesian, review, and risk assumptions.

The `Model/paper/` figures generated by the code retain some **development-stage figure numbering**. The current journal layouts are stored separately in `Paper_Final/`, as listed below.

## Figures supporting the current manuscript

Inside `HA_Conflict_Updated/Paper_Final/`:

| Manuscript figure | Exact file stem | Content |
|---|---|---|
| **Figure 2** | `Figure_2_Algorithm1_Interaction_Evidence` | Run C human–AI decisions, PI evidence and interaction outcomes |
| **Figure 3** | `Figure_3_Algorithm2_History_and_Conflict` | Unresolved history, recurrence and conflict posterior during a C3 issue |
| **Figure 4** | `Figure_4_Algorithm2_Context_and_System` | Context-specific and weighted system conflict estimates and their cumulative mean |
| **Figure 5** | `Figure_5_Algorithm3_Cumulative_Risk_Context_Regions` | Context severity, cumulative system conflict estimate and conflict-related risk |
| **Appendix Figure A1** | `appendix/Figure_A1_Algorithm1_RunC_Transition_Comparison` | Run C interaction transitions |
| **Appendix Figure B1** | `appendix/Figure_B1_Algorithm1_RunC_Resolution_Timing` | Run C matched-issue resolution timing |

Each listed figure is supplied in **PNG and PDF** formats. The `Paper_Final/data/` directory contains exported plotting data, and `Paper_Final/supplementary/` contains numerical and sensitivity figures. `Additional_Plot_Gallery/` and other historical folders include older figure layouts, **not the current manuscript numbering**.

**Interpretation note:** The instantaneous system-level conflict probability is the weighted context estimate in Eq. (3.12). Curves labeled *cumulative* are **running time averages**, not the probability that at least one conflict will occur.

## Regenerate the physical ASTE–CSTR trajectories (MATLAB required)

The first archive contains the adapted MATLAB/Simulink process model. Fresh process simulation requires a compatible MATLAB/Simulink installation, required toolboxes and model components, and a working MATLAB Engine API for Python. Its launcher was developed for **MATLAB R2023b** on a compatible Windows environment, and its default `D:/ASTE_LONG/` path may need to be changed.

The intended launcher sequence is:

```bash
python ASTE_Long_Context_Feasible/run_input_check.py
python ASTE_Long_Context_Feasible/run_duration_screen.py
python ASTE_Long_Context_Feasible/run_long_sequences.py
python ASTE_Long_Context_Feasible/plot_reactor_results.py
```

These commands require the corresponding extracted ASTE archive and system dependencies; they are **not needed** to analyze the fixed saved inputs from archive 4. See [MATLAB setup](MATLAB_ASTE_SETUP.md) and [ASTE modifications](ASTE_ADAPTATIONS.md).

## Scientific scope and limitations

This release supports **simulation-based evaluation and numerical verification**, not empirical validation of human conflict probabilities or measured accident-risk reduction.

- Human diagnostic decisions are generated by a **simulated operator model**; the AI classifier is fixed. The revised HA analysis does not retrain the upstream models.
- Operating contexts are assigned using **injected simulator labels** rather than an independently deployed context detector.
- The C3 PI review and the diagnostic verification mechanism use **related controller-response evidence**; independent verification remains future work.
- Diagnostic review changes subsequent interpretation and interaction outcomes, **not reactor control actions**. The reported risk index uses **specified conditional-consequence assumptions** and 400 illustrative scenarios, not observed accidents.
- The six lemmas are assessed through mathematical conditions and numerical implementation checks. These checks do **not** establish empirical validity of all postulated relationships. The revised HA model was developed after examination of simulation results; Run C is not an untouched prospective validation of the final HA assumptions.

Reproducibility requires preserving the exact input versions, parameter files, results, release assets, and checksums. Avoid combining earlier archived conflict-model outputs with the revised model's figures or numerical claims.

## Documentation and provenance

The repository contains supporting guides, some of which describe the **earlier** archive layout. For the revised model, the instructions **inside archive 4 take precedence**.

- [Download instructions](DOWNLOAD_ALL_FOUR_MODELS.md)
- [ASTE adaptations](ASTE_ADAPTATIONS.md)
- [MATLAB/Simulink setup](MATLAB_ASTE_SETUP.md)
- [Testing protocol](TESTING_PROTOCOL.md)
- [Reproduction guide](REPRODUCE.md)
- [Results and lemmas](RESULTS_AND_LEMMAS.md)
- [Third-party software and data provenance](THIRD_PARTY_AND_PROVENANCE.md)
- [Citation template](CITATION_TEMPLATE.md)

**Third-party rights:** Attribution to the ASTE authors does not by itself establish permission to redistribute upstream MATLAB/Simulink files or compiled components. Confirm licensing and permission for all distributed third-party assets before journal publication.

## Citation and code availability

For a manuscript code/data availability statement:

> The Python implementation of the proposed human–AI conflict framework, fixed ASTE–CSTR simulation inputs, numerical verification results, and supporting figures are available at https://github.com/Rajeevan-A/human-ai-conflict-CSTR-reproducibility.

When finalizing the journal article, cite the **specific frozen release/version** used to generate its results (and an archival DOI, if one has actually been issued), rather than citing an unspecified version. Cite the Markaj, Mercangöz & Fay (2024) ASTE study separately for the upstream process-simulation framework.
