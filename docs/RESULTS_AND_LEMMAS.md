# Results, figure/lemma mapping and scientific interpretation

All file identifiers are the names within the original `HA_Conflict_Paper_Complete(6).zip`. **Figure numbers are development-package identifiers, not final manuscript numbering.**

| Figure or table | Model question | Lemmas | Publication use |
|---|---|---|---|
| `Fig02_Controlled_Mechanisms.png` | Does the implementation preserve history, differentiate U duration from recurrence, and require evidence for R? | 1, 2, 3 | Main: controlled mechanism verification |
| `Fig04_Context_and_System_Conflict.png` | Do distinct context traces contribute to the standardized mixture? | 1, 4 | Main: context-specific conflict development |
| `Fig05_Matched_Fault_Period_Issue.png` | What happens within one matched C3 issue under different review policies? | 3, 5 | Supplement or main explanatory panel, **not population-level proof** |
| `Fig06_Common_Cohort_Recovery.png` | How often is verified diagnostic agreement maintained at fixed follow-up times for shared eligible cases? | 3, 5 | Main: common-denominator comparison |
| `Fig07_Conditional_Risk.png` | How do conflict posteriors and severity contribute to modeled risk? | 4, 6 | Main: risk comparison, consequence assumptions required |
| `S08_Consequence_Assumption_Sensitivity.png` | Is policy risk ranking dependent on relative loss assumptions? | 6 | Supplemental sensitivity; discuss in main text |
| `S07_Trigger_Sensitivity.png`, `S09_Bayesian_Update_Audit.png` | Trigger configuration and formula implementation | 3, 5 | Supplemental |

The package contains `Fig01_Model_and_Qualification.png` and `Fig03_Reactor_Contexts_and_Severity.png`; their scientific value is mostly explanatory/physical-context validation, and they may be supplementary if space is limited.

## Principal results and limits

**Numerical verification:** Recorded maximum Bayes posterior residual approximately 3.89e-16 over 14,942 eligible updates; the audit supports implementation fidelity under the defined equations, not external validity or calibration.

**Review:** C3 matched issues can show earlier verified diagnostic agreement with PI-response evidence. The improvement is not persistent across every follow-up landmark. A verified resolution transition can be followed by renewed disagreement; do not equate R event count with durable issue resolution.

**Risk:** Saved Run C standardized system risk means: baseline `0.005116`, observation review `0.004671`, PI review `0.004560` (rounding from exported source table). Their interpretation is conditional on severity, comparison policies and consequence assumptions. The PI-baseline difference is **not** measured physical safety improvement; the process trajectory remains unchanged.

**Comparability:** The source ZIP includes regenerated reference AI predictions with its own provenance, separate from the standalone AI package. Published figures must identify their true input mode; never merge labels from one classifier artifact with hashes, claims or figures from the other mode.
