# Downloading the four model archives

## Why the four ZIPs do not appear in the Code tab

The GitHub repository has **two storage locations**:

1. **Code** holds `README.md`, `docs/`, `scripts/`, manifests and citation material. Those items can be browsed as ordinary files.
2. **Releases** holds four separate large ZIP *attachments* that were uploaded by the repository owner. They are not present in **Code → Download ZIP** and are not browsable individually in GitHub until extracted and committed separately.

**[Go to the repository Releases page](https://github.com/Rajeevan-A/human-ai-conflict-CSTR-reproducibility/releases)**. Select the latest approved versioned research release. While a release is still a **Draft**, it is not accessible to general public readers; owners/collaborators can inspect it. The existing owner draft is [here](https://github.com/Rajeevan-A/human-ai-conflict-CSTR-reproducibility/releases/tag/untagged-e67c10659ea266dcf9e9).

## Four required release attachments

| Original uploaded asset | Description |
|---|---|
| `1.ASTE_Long_Context_Feasible.zip` | MATLAB/Simulink CSTR model, physical fault injection schedules, simulation launcher |
| `2.Human_Operator_ABC.zip` | Human diagnostic surrogate, inputs and saved diagnostic outputs |
| `3.AI_Operator_ABC.zip` | Random Forest classifier and saved AI diagnostic predictions |
| `4.HA_Conflict_Paper_Complete.zip` | Conflict dynamics, diagnostic review, consequences/risk, numerical verification, figures and tables |

### Steps for readers

1. Go to **Releases** (not Code). Open the published release and expand **Assets**.
2. Download **each** of the four ZIPs. Do not assume the GitHub-generated Source code (zip) contains these separate attachments.
3. Put them in the folder containing the repository's `archive_manifest.json` and `scripts/` directory.
4. Verify each downloaded archive using `python scripts/prepare_archives.py --verify`. Checksums identify bytes, not whether a model executes successfully.
5. Extract with `python scripts/prepare_archives.py --extract`. This produces four sibling directories: `ASTE_Long_Context_Feasible`, `Human_Operator_ABC`, `AI_Operator_ABC` and `HA_Conflict_Paper_Complete`.
6. Choose one of the two workflows: [MATLAB/Simulink physical regeneration](MATLAB_ASTE_SETUP.md), or [Python archived analysis](REPRODUCE.md).

The asset prefixes `1.`–`4.` are just GitHub attachment filenames; the checker accepts them. **Do not rename files inside the archives**.

## Owner checklist before publishing

The four original assets have already been attached to the Draft Release; **do not upload them again**. Make the `README.md` visible on Code and link to Releases. Confirm third-party ASTE `.slx`, `.m`, and `.mexw64` redistribution rights, coauthor/institutional approvals, scientific reproducibility and release content. Only then publish the release, preferably with a normal version tag such as `v1.0.0`, and consider archiving the true release assets in Zenodo.
