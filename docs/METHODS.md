# Detailed research objectives and computational methodology

This document describes the **supplied implementation**. It is not a claim that every result has been independently replicated on an unrelated process or with measured human operators. The exact numerical assumptions and data provenance belong to the extracted source files, especially `config.json`, `run_config.json`, `experiment_design.json`, and the archived results.

## 1. Scientific problem and objective

Human–AI diagnostic systems can produce agreement or unresolved disagreement over the same process condition, and repeated interactions may affect how conflict is estimated. The computational research investigates whether a context-specific state model can retain earlier unresolved interactions and verified diagnostic outcomes rather than treating each new comparison in isolation. It also examines whether subsequent qualified review evidence changes the inferred conflict state and a downstream conditional process-risk index.

## 2. CSTR operating scenarios and experimental units

The provided ASTE long-run design uses a CSTR represented by a MATLAB/Simulink model, with three separately initialized 70,000-second runs A/B/C and one-second recorded observations. Fault schedules contain C0 nominal operation and three injected diagnostic contexts: C1 inlet flow factor 0.8; C2 outlet factor 0.6; C3 cooling response factor 1.2. Each run includes 47,000 nominal, 8,500 C1, 6,000 C2, and 8,500 C3 seconds. Planned episode lengths include 200, 500, 1000 seconds for C1/C3, and 200/500 seconds for C2. The attempted 1000-second C2 case exceeded the study screen and was excluded from active schedules. Each fault context has 15 episodes per mixed run. A planned schedule does not itself establish an observed fault response.

The ASTE package includes source files, `.mat` schedules, an `.slx` model, a Windows `.mexw64` binary and screening procedures. The original README points to an existing `D:/ASTE_LONG/duration_screen_summary.csv`, plus new run output directories; those paths are **not portable automatically**. Original regulatory simulation and the adapted offline study must be distinguished: the reviewed dataset disables operator/SIF actuation, so diagnostic decisions have no effect on the physical trajectory.

## 3. Simulated human operator

`Human_Operator_ABC/human_operator_model.py` implements a deterministic-structure finite-state diagnostic surrogate with evidence accumulation and fixed parameterization. Inputs are each run's recorded reactor signals; classifying a new run resets counters, inference history and random state. `run_config.json` declares settings. Generated predictions are in `my_results/run_A`, `run_B`, and `run_C`; evaluation against simulator-injected labels is a simulation metric, not a measurement of human judgment.

## 4. AI operator

`AI_Operator_ABC/ai_fault_model.py` trains a Random Forest using the complete Run A (70,000 observations), then evaluates the fitted model without refitting on B and C. Its stored settings include 300 trees, `min_samples_leaf=2`, balanced subsampling and seed 42. Only process-observation-derived features are used for inference, including process deviations, trailing changes/means and lags; injected `S_fault` labels are for training and evaluation, not inference. Stored `ai_score_*` values are uncalibrated classifier scores. Model artifacts and evaluation manifests are in `ai_results/`. A's performance is in-sample; B and C share simulation assumptions and are not independent field validations.

## 5. Shared diagnostic comparisons and evidence qualification

The conflict package aligns reactor, human and AI records by run and `time_s`. At scheduled 10-second comparison opportunities, it constructs common issue histories, qualifies sensor/evidence references, and assigns observable A/U/R outcomes: A = no unresolved issue/agreement; U = unresolved diagnostic disagreement; R = an issue-specific, corroborated diagnostic resolution. A matched label alone is not sufficient for R. Sensor epoch, issue identity and consecutive qualified agreements control the resolution gate. Ineligible or inactive context observations do not update the state or history.

For each diagnostic context c, the latent state is low or high conflict, represented by a posterior probability p_c(H). Its prior is 0.05, and the transition probabilities depend on previous eligible unresolved duration D and recurrence count M. Qualifying observation likelihoods update the transition-predicted state via Bayes' rule:

```
p_pred = (1 - p_previous) * p_L_to_H + p_previous * (1 - p_H_to_L)
p_post = likelihood_H * p_pred / (likelihood_H * p_pred + likelihood_L * (1-p_pred))
```

Current D/M counters are committed **after** the current Bayesian update. Configured transition rates, likelihood categories and evidence requirements are fully specified in `HA_Conflict_Paper_Complete/config.json`, and the derivation is in `BAYESIAN_DERIVATION.md`. Context histories remain separate.

## 6. Comparison arms and review timing

Three policy arms are compared within every run: `baseline` fixed simulated human, `observation_review`, and `pi_review` (PI controller-response evidence). The reviewer has access to the same physical trajectory and fixed AI interpretation under all arms; the review logic can alter the simulated human diagnosis at a later eligible opportunity. The trigger uses three unresolved eligible comparison opportunities; the review action does not directly force a lower conflict posterior or actuate a cooling repair. This makes policy differences a *modeled diagnostic interpretation effect*, not plant-control effectiveness.

## 7. Context and system aggregation

For c in C1, C2 and C3, context-specific high-conflict estimates are aggregated by a nonnegative convex weight set summing to one:

```
p_system(H) = sum_c w_c * p_c(H)
```

This is an **exposure-weighted mixture**, not the probability of at least one simultaneous conflict. The saved equal-weight 1/3 choice is a hypothetical standardized comparison over abnormal contexts; it is not the observed duration distribution of injected faults.

## 8. Severity and conditional risk

The package transforms recorded level and temperature deviations into nonnegative clipped severity proxies, with intervention references defined in `config.json` (e.g., low level 45, high level 200 in supplied level units; high temperature 400 degC). For context c, the low/high latent-state conditional risks r_c(L), r_c(H) depend on physical severity and scenario-assumed consequences. The reported conditional index is:

```
Gamma_c = (1 - p_c(H))*r_c(L) + p_c(H)*r_c(H)
Gamma_system = sum_c w_c*Gamma_c
```

A fixed seed (10601) produces 400 hypothetical consequence scenarios spanning no adverse outcome, delay only, inappropriate response only, or both. Scenario percentile ranges express **assumed consequence variation**, not observational confidence intervals. Measured accident rates, full plant safety risk and monetary losses are outside this model's validation.

## 9. Study design and interpretation

Comparison within each run controls for the same process trajectory and fixed AI interpretation; however, review arms share dependent events, and selected matched issue cohorts are small. A and B/C differ in AI training roles, not physical-system independence. Run C has already been inspected during development, so characterize its comparisons as retrospective held-out run evaluations, not untouched prospective test performance. Numerical audit and controlled synthetic tests verify the implementation; they do not empirically prove correct latent conflict likelihoods, human behavior or causal plant-safety improvements.
