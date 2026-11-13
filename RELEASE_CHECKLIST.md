# Checklist before publishing v1.0.0

- [ ] Keep existing four **Draft Release assets**; do not upload them again, overwrite or repackage them.
- [ ] Upload the **updated small documentation** to Code: README, docs/, scripts/, START_HERE, checksums, archive manifest, release checklist.
- [ ] Open README links in the repository to confirm file structure and scientific attribution to Markaj et al. (2024), DOI 10.1016/j.compchemeng.2024.108798.
- [ ] Download all four numbered ZIP Assets as the owner; `python scripts/prepare_archives.py --verify` passes; compare SHA-256 with GitHub displayed SHA-256.
- [ ] Confirm archived `results/run_manifest.json` source is **external** and hashes match the standalone AI/Human predictions. Separate the different bundled reference input mode.
- [ ] Execute `python HA_Conflict_Paper_Complete/test_bayesian_audit.py` and `python HA_Conflict_Paper_Complete/run_package.py` in a fresh working copy; compare regenerated figures, tables and reports to the historical evidence.
- [ ] Record Python, NumPy, pandas, scikit-learn, matplotlib and joblib versions. Verify whether MATLAB/Simulink rerun is actually possible; do not claim it without a documented run.
- [ ] Cross-check every value/claim in the manuscript against same provenance output and source CSV. Use correct C3 common-cohort counts, scenario assumptions and risk index interpretation.
- [ ] Confirm permission to redistribute upstream ASTE source and compiled `.mexw64`; review any proprietary/confidential content, local paths and metadata, and get coauthor/institution approval. **Blocking step for public release.**
- [ ] Decide separate licenses for own code/data and third-party assets. No unverified blanket open-source license.
- [ ] Change temporary draft `untagged-*` to **v1.0.0**, write release notes and publish only after clearance. Check asset links are accessible without authentication after publishing.
- [ ] Archive all full ZIP file bytes in a DOI-bearing record (e.g., manual Zenodo deposit if auto source snapshot does not include release assets), then verify the DOI files.
- [ ] Add accurate CITATION.cff with real authors, journal citation and DOI after available. Update the manuscript Data and Code Availability text.
