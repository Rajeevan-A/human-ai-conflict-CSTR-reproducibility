# From your current Draft Release to a citable journal software record

## Your present GitHub status

- Repository: https://github.com/Rajeevan-A/human-ai-conflict-CSTR-reproducibility
- Release title: **Human–AI Conflict ASTE–CSTR Research Model**
- Release state: **Draft** (not available to ordinary public readers)
- Existing Assets: `1.ASTE_Long_Context_Feasible.zip`, `2.Human_Operator_ABC.zip`, `3.AI_Operator_ABC.zip`, `4.HA_Conflict_Paper_Complete.zip`.
- **Do not upload the four ZIPs again.** Your immediate task is to update the repository's **Code tab documentation** to match the already attached asset filenames.

## Step-by-step actions on github.com — no Git command-line installation required

### 1. Update the repository README and reader documents

1. On the repository page, click **Code**. If `README.md` exists, open it, click the pencil/ **Edit this file** and replace it with the updated `README.md` from this documentation package. Commit the change.
2. Upload/update the `docs/` and `scripts/` directories, `START_HERE.md`, `archive_manifest.json` and `.sha256` file through **Add file → Upload files**. On an empty repository, GitHub offers **uploading an existing file**. Keep the original folder structure.
3. Click each README relative link. It should open a documentation file, not a 404.
4. The source remains in the **Release assets**. Readers cannot browse its individual `.py`/`.m` files on GitHub until extracted source is additionally committed to the **Code** branch.

### 2. Verify the four original assets without modifying them

1. Open **Releases**, select the existing **Draft** and confirm all four named Assets and sizes.
2. Compare their published GitHub SHA-256 values against `archive_manifest.json` / `ARCHIVE_CHECKSUMS.sha256`.
3. Download the four assets to an empty computer folder, alongside the extracted documentation files. Run `python scripts/prepare_archives.py --verify` then `python scripts/inspect_archive_reports.py`.
4. Extract in a working directory and test the saved *external-input* workflow. Do not overwrite the only copy of historical outputs.

### 3. Check the science and provenance

- Confirm the saved conflict result `results/run_manifest.json` identifies `source_mode=external` for A/B/C and matches the standalone human and AI ZIP output checksums. The bundled reference AI input in the conflict archive is **different** and needs its own separate label.
- Check manuscript figures, case denominators, context weights, scenario assumptions and versioned configuration against the saved output CSVs.
- Record Python / scikit-learn versions and whether the scripts were actually rerun by a second researcher; do not claim new physical MATLAB execution without it.
- Read `docs/TESTING_PROTOCOL.md` and `docs/RESULTS_AND_LEMMAS.md` to avoid claiming empirical probability calibration or causal process safety improvements.

### 4. Clear rights and privacy (blocking step before publishing)

- Confirm permission/license for upstream ASTE CSTR source, Simulink `.slx`, MATLAB `.m`, and compiled `.mexw64` component. The ASTE article's citation by itself is **not** a redistribution license.
- Review local Windows paths, metadata, scripts, output CSVs, pretrained model and any confidential/proprietary material. Check coauthor and institution approvals.
- Create `LICENSE` only after rights are verified, with scopes for your code, datasets, figures and third-party assets.
- If ASTE files cannot legally be redistributed, remove the restricted archive **before making the release public**, keep upstream acquisition instructions, and update the README's completeness/reproducibility statement honestly.

### 5. Prepare the versioned public release

1. In **Releases → Draft → Edit**, choose a real semantic tag, for example `v1.0.0`, rather than leaving the current temporary `untagged-...` draft identifier.
2. Add release notes: archived source/model, paper title (if final), provenance (`external` saved runs), environment requirements, known limitations, third-party attribution, and changes since previous release.
3. Confirm the asset names and integrity again. Decide public repository/release visibility only after the licensing review.
4. If authorized and approved, make the repository public and click **Publish release**. Verify the resulting tag URL in an incognito window: draft links are **not permanent public research citations**.

### 6. DOI and manuscript citation

- Enable GitHub → Zenodo integration for the repository. Archive a published, immutable `v1.0.0` release and obtain the **actual DOI**. Check that Zenodo has all full ZIP payloads; its GitHub source snapshot need not automatically contain large Release asset payloads.
- Update `CITATION.cff` or `CITATION_TEMPLATE.md` with real author list, version, date, source URL and DOI; add a paper DOI if available.
- Use the **versioned release/Zenodo DOI** in the manuscript's Data and Code Availability section, not the temporary `untagged-*` draft URL.
- Keep a list of known limitations (MATLAB system dependencies, unpinned Python requirements, external vs bundled AI provenance).

## Publication-ready model availability statement (complete with real URLs/DOI)

> The simulation code, model configurations, archived Human–AI diagnostic outputs, numerical verification records, and figure source data are available in a versioned research-software release at [GitHub release URL] and [software DOI]. The study uses an adapted ASTE–CSTR reference model derived from the framework of Markaj et al. (2024). Reproduction instructions and third-party software requirements are documented in the repository. The reported conflict probabilities and conditional risk estimates are simulation-based and depend on stated model and consequence assumptions.

Only publish that statement once the release is genuinely public, all cited files are included/authorized, and the links work for an unauthenticated reader.

## Recommended follow-on research

1. Run the same full external-input Python pipeline on a **fresh environment**, keep complete versions/hashes, and compare results with archived tables.
2. If possible, independently execute the adapted ASTE MATLAB sequences, including input-format checks and physical sanity checks, then rerun the human/AI/conflict pipeline on *those* new trajectories.
3. Add a **matched history-independent comparator** (same reactor data, AI labels, human labels and consequence model) to isolate the value of duration/recurrence memory; this is **not an existing verified result** and would need a separately versioned analysis.
4. Evaluate diagnostic resolution on additional faults, parameter shifts and actual operator observations before making claims about transferability or calibrated human conflict behavior.
