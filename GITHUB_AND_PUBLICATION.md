# GitHub owner instructions: your four ZIPs are already in a Draft Release

Repository: https://github.com/Rajeevan-A/human-ai-conflict-CSTR-reproducibility

**Present state:** The four original research packages were already uploaded as numbered **Release Assets** to the Draft Release **Human–AI Conflict ASTE–CSTR Research Model**. **Do not repeat this upload.** You can continue entirely in a web browser; Git/Git LFS are **not required** for the current workflow.

## A. Where files are located

- **Code** tab: `README.md`, `docs/` and `scripts/` (documentation and small verification scripts). No release assets appear here.
- **Releases** page → **Draft** → **Assets**: your four large ZIPs, accessible to your account/collaborators. The current draft's temporary `untagged-*` identifier is not the public citation tag.
- **After publication:** the release asset downloads become accessible to ordinary readers if repository/release visibility permits it. Readers can download through their browser without Git. GitHub `Code → Download ZIP` is **not** a download of the separate research ZIP assets.

## B. Upload this new small documentation update to the Code tab

1. Download and **extract** the small package `GitHub_Reader_Guide_Updated.zip` to your computer.
2. On the GitHub repository, open **Code**. For existing `README.md`, click the file, then **Edit** (pencil) and replace/commit its contents, or upload the file in **Add file → Upload files** and confirm the update if prompted.
3. Upload/update `docs/`, `scripts/`, `START_HERE.md`, `archive_manifest.json`, `ARCHIVE_CHECKSUMS.sha256`, `RELEASE_CHECKLIST.md` and `CITATION_TEMPLATE.md`. Keep `docs/` and `scripts/` directory hierarchy. The small documentation package contains **no large model ZIPs**.
4. Check the README links and repository structure. Nothing in this step changes the four uploaded model archives or their SHA-256 hashes.

## C. Test as the owner

1. Download your four numbered assets from **Releases → Draft → Assets** into the **same local folder** where the updated documentation is extracted.
2. Open your terminal and run:

```bash
python scripts/prepare_archives.py --verify
python scripts/inspect_archive_reports.py
python scripts/summarize_archived_results.py
```

3. The archive verifier accepts `1.ASTE_Long_Context_Feasible.zip`, `2.Human_Operator_ABC.zip`, `3.AI_Operator_ABC.zip` and `4.HA_Conflict_Paper_Complete.zip` *without renaming them*. It also recognizes the original uploaded names with `(1)`, `(2)`, `(6)`.
4. For full source extraction and optional rerun, continue with [`REPRODUCE.md`](REPRODUCE.md). The bundled-reference route produces a distinct AI-source experiment; use `run_package.py` with the standalone inputs to reproduce the archived **external** figures/tables.

## D. Finalization and DOI

Do **not** publish the draft before ASTE third-party source/binary permission, confidentiality and coauthor approvals are confirmed. The original 2024 ASTE research paper should be cited in the README, but an academic citation does not itself establish executable-code redistribution permission.

Once clear: edit the draft to choose actual tag `v1.0.0`, add explanatory release notes, and publish. Verify links in an unauthenticated browser. For a DOI, deposit the **actual full release ZIPs** with Zenodo (manually if necessary); GitHub's automatically generated source snapshot may not include Release assets. Record the verified Zenodo DOI in the paper and `CITATION.cff` only once available.

See [detailed owner checklist](NEXT_STEPS_TO_PUBLICATION.md) and [release checklist](../RELEASE_CHECKLIST.md).
