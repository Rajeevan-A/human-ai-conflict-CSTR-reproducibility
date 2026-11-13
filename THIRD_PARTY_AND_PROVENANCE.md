# Upstream ASTE attribution, licensing, source hashes and result provenance

## Original work and rights

Markaj, A., Mercangöz, M., & Fay, A. (2024). *Design and implementation of an Autonomous Systems Training Environment framework for control algorithm evaluation in autonomous plant operation*. Computers & Chemical Engineering, 189, 108798. https://doi.org/10.1016/j.compchemeng.2024.108798.

The ASTE package includes MATLAB/Simulink `.slx`, `.m`, `.mat` files and a compiled Windows `.mexw64`. **A citation and open-access article license do not automatically authorize redistribution of the source or binary.** Confirm permissions/identifiable upstream license, authors/coauthors/institution consent and confidentiality before publishing the four full archives. If unclear, keep the release private and publish only independently licensed components and upstream acquisition instructions. See [ASTE adaptations](ASTE_ADAPTATIONS.md).

## Exact file identity

Each release ZIP was renamed with prefix `1.`–`4.` for its GitHub Release, but the SHA-256 of each payload matches the original archive. Use [`archive_manifest.json`](../archive_manifest.json) and `python scripts/prepare_archives.py --verify` to inspect identity. Do not edit original ZIP internals without a new version/reproducibility report.

## Critical: two AI input provenances

**What the saved figures/tables actually used:** The *archived saved* conflict `results/run_manifest.json` specifies `external` mode for A, B and C. Its recorded human and AI prediction SHA-256 values match the standalone `2.Human_Operator_ABC.zip` and `3.AI_Operator_ABC.zip` corresponding output members exactly. Therefore the saved conflict results and audit in the supplied ZIP should be identified as **EXTERNAL / STANDALONE-INPUT** output.

**Other included, distinct stream:** `HA_Conflict_Paper_Complete/input/run_A/B/C/ai.csv` was regenerated as a bundled reference AI stream; its hashes are **not identical** to the standalone AI ZIP's outputs. `HA_Conflict_Paper_Complete/run_bundled_reference.py` selects this separate mode. It can be rerun for comparison but is **not** the correct source label for the saved external-mode figures.

The same reactor/AI/environment details do not justify silently swapping one AI predictions file for the other. Always inspect the newly generated `results/run_manifest.json`, exact input hashes and paper CSVs. Store reruns separately to preserve the archival scientific record.

## Other release limitations

- Some reports contain local Windows absolute paths inherited from the original execution. They are historical provenance fields, **not** installation paths for readers. Inspect for accidental private/personal data before public release.
- Python dependency lists are not pinned to a verified lockfile, and pretrained scikit-learn/joblib artifacts may be version-dependent. Only load known, trusted artifacts.
- The offline CSTR input CSVs are present; a new physical MATLAB run can require a `D:/ASTE_LONG` duration-screen summary, compatible compiled `.mexw64` and licensed toolboxes.
- Software tests verify the declared mathematical implementation, not calibrated real conflict, measured safety improvements, or deployed plant operation.
- For the publicly citable record, freeze the code, output files, figure numbering, source provenance, release notes, relevant environment versions, and **actual** archive DOI.
