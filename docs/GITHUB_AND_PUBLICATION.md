# Create your GitHub repository from the four original ZIP archives

This is a **step-by-step owner guide**, not a claim that a GitHub repository has already been created. Your original ZIP names are exactly:

- `HA_Conflict_Paper_Complete(6).zip` (~129 MiB)
- `Human_Operator_ABC(2).zip` (~16.7 MiB)
- `AI_Operator_ABC(2).zip` (~54.2 MiB)
- `ASTE_Long_Context_Feasible(1).zip` (~0.7 MiB)

## 1. Download Git and Git LFS

1. Create a free account at https://github.com/signup if you don't have one.
2. Download **Git** from https://git-scm.com/downloads . On Windows install it and open **Git Bash**. On Mac/Linux use the platform-specific installer.
3. Check Git: `git --version`.
4. Download or enable **Git LFS** from https://git-lfs.com/ (Git for Windows typically includes it; on other systems install separately). Check `git lfs version`, then run `git lfs install`.
5. If you prefer a GUI, GitHub Desktop is https://desktop.github.com/ ; **Git LFS must still be configured before committing the archives**. For a first upload, the explicit Git Bash commands below are less ambiguous.

**Why LFS?** GitHub browser uploads support only 25 MiB per file and ordinary Git blocks files over 100 MiB. Your 129 MiB ZIP cannot be uploaded directly through the website or normal Git. Git LFS stores large data separately and commits pointers. Free allowances exist, but storage/bandwidth usage and possible charges depend on your account and downloads; verify current GitHub billing rules.

## 2. Prepare one folder on your computer

Create a folder `human-ai-conflict-CSTR-reproducibility`. Extract **this documentation-only template ZIP** into it, then copy the original **four ZIP files without extracting or renaming them** into this same folder. The repository should look like:

```text
human-ai-conflict-CSTR-reproducibility/
├── README.md
├── .gitattributes             # already maps *.zip to Git LFS
├── .gitignore
├── ARCHIVE_CHECKSUMS.sha256
├── archive_manifest.json
├── RELEASE_CHECKLIST.md
├── CITATION_TEMPLATE.md
├── docs/
├── scripts/
├── HA_Conflict_Paper_Complete(6).zip
├── Human_Operator_ABC(2).zip
├── AI_Operator_ABC(2).zip
└── ASTE_Long_Context_Feasible(1).zip
```

On Windows, show hidden files if necessary to confirm that `.gitattributes` and `.gitignore` are present. Do **not** also commit expanded copies of all four directories: that doubles the repository and may hit GitHub size limits; readers can extract locally.

Verify the original ZIPs before uploading:

```bash
python scripts/prepare_archives.py --verify
```

If the script says **Git LFS pointer**, the large file has not yet downloaded; run `git lfs pull` in an existing clone.

## 3. Create an empty repository online

1. Visit https://github.com/new after signing in.
2. Repository name: `human-ai-conflict-CSTR-reproducibility` (suggestion; you can select a different name).
3. Description: `Research code and simulation evidence for context-specific Human–AI diagnostic conflict and conditional risk in ASTE–CSTR systems`.
4. Choose **Private**, pending authorship/third-party ASTE redistribution approval. It can be made public later.
5. **Do not** check `Add a README`, `Add .gitignore`, or `Choose a license`, because this template already supplies documentation and the final license is unresolved.
6. Click **Create repository**. Copy the HTTPS remote URL displayed by GitHub.

## 4. Use Git Bash or Terminal in your prepared folder

Replace identity text with your own actual values. Use `cd` to enter the folder first, or right-click the folder on Windows → **Open Git Bash here**.

```bash
# One-time configuration on this computer:
git config --global user.name "YOUR NAME"
git config --global user.email "YOUR VERIFIED GITHUB EMAIL"

# Start the repository and configure LFS before adding the ZIPs:
git init
git branch -M main
git lfs install
git lfs track "*.zip"

# Add the documentation and the exact original ZIPs:
git add .
git lfs ls-files
git status
git commit -m "Add publication research archives and reproducibility documentation"

# Link to the empty repository you made on GitHub:
git remote add origin https://github.com/Rajeevan-A/human-ai-conflict-CSTR-reproducibility.git
git push -u origin main
```

At `git lfs ls-files`, you should see **four ZIP archives**. If the `.gitattributes` was absent or you added ZIP files before setting up LFS, stop **before your first commit** and correct the tracking. The first push sends approximately 200 MiB of large ZIP files; allow for normal upload time and verify your account's remaining LFS allowance.

Authentication: GitHub does not accept your normal account password for Git command-line pushes. Use Git Credential Manager's browser sign-in, GitHub CLI (`gh auth login`), SSH, or GitHub Desktop. Never paste your access token into a file or a chat.

## 5. Check your GitHub page

Open `https://github.com/Rajeevan-A/human-ai-conflict-CSTR-reproducibility`. Confirm:

- README displays the objective, methodology and reader quick start.
- `docs/` and `scripts/` are visible.
- All four ZIP filenames appear and have **Git LFS pointers**, not 129-MiB regular Git blobs.
- `.gitattributes` is tracked; `git lfs ls-files` lists the four archives.
- `python scripts/prepare_archives.py --verify` works after a fresh `git clone` and `git lfs pull` on another machine.

**This is how you get your GitHub link:** once the push succeeds, the URL is automatically the permanent **repository address**. It is not a DOI and does not require a journal publication first.

## 6. Make the repository public only when approved

Review `RELEASE_CHECKLIST.md` and `docs/THIRD_PARTY_AND_PROVENANCE.md`, secure coauthor approval and ASTE redistribution rights, ensure no credentials/private metadata, and confirm all final figures and the publication manuscript use the same source/version. Set the repository visibility to **Public** only after approval.

## 7. Create an official cited version and DOI

1. Finalize the author names, manuscript title and license scope. Fill out `CITATION_TEMPLATE.md` and create a correct `CITATION.cff` before release (do not copy placeholder identities as real authors).
2. Commit final documentation changes, then tag a release:

```bash
git add .
git commit -m "Finalize publication metadata"  # Only if files have changed
git push
git tag -a v1.0.0 -m "First publication research software release"
git push origin v1.0.0
```

3. GitHub → repository **Releases** → **Draft a new release**, select `v1.0.0`, add software and data provenance notes, and publish.
4. Create an account at https://zenodo.org, connect GitHub, sync repositories, and **enable this repository before creating a new GitHub release** if you want automatic archive/DOI creation. Do not pretend that a prior release automatically gets a DOI.
5. **IMPORTANT FOR THIS FOUR-ZIP DESIGN:** GitHub source archives by default may contain only **LFS pointer files**, not the actual data. Check GitHub Settings → Archives → Include Git LFS objects in archives, or use a **separate manual Zenodo deposit of the four real ZIPs**. Verify the archival DOI record actually contains recoverable model bytes, not mere LFS pointers. If you manually deposit, avoid unintentionally giving distinct DOIs to the same version without explaining the relationship.
6. Copy the **actual** Zenodo DOI into README, paper availability statement and CITATION metadata. No DOI exists until you perform the archive deposit or release integration.

## 8. Suggested article data/code availability statement

**Before publication:** "The computational model, simulation inputs, numerical verification tests, and results have been organized into a versioned research repository and will be made available at the final archive URL following the code-licensing review."

**After publication:** "The code, recorded data, diagnostic comparison outputs, numerical verification records, and figure-generation materials underlying this study are archived at [actual versioned repository or Zenodo DOI]. Materials derived from the ASTE framework are distributed only according to the applicable third-party license terms."

## 9. GitHub-specific troubleshooting

- **Push rejected: file >100 MB:** `.gitattributes` wasn't applied before the original commit. If not pushed yet, make a clean repo and commit the files as LFS *from the beginning*; do not keep a regular-Git 129 MB blob in commit history.
- **404 or missing repo:** wrong USERNAME, not signed in or private-repo permissions.
- **Authentication failed:** use browser sign-in via Git Credential Manager/GitHub CLI, not the account password.
- **LFS quota exceeded:** consult GitHub storage/bandwidth allowances; keep source docs on GitHub and deposit ZIPs as a separately citable data archive if permitted.
- **GitHub download archive only contains tiny pointer text:** use `git clone` followed by `git lfs pull`, turn on LFS inclusion in GitHub-generated archives, or provide a verified data repository deposit.
- **`git commit` reports no changes:** nothing new to commit; skip that command before tagging.
- **Missing MATLAB stage:** this archive contains a platform-specific binary and hard-coded legacy paths; read the ASTE README and do not claim portable full-plant regeneration.

**Official references:**

- Git: https://git-scm.com/downloads
- GitHub setup: https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github
- GitHub file sizes: https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository
- Git LFS installation: https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage
- LFS archives: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-git-lfs-objects-in-archives-of-your-repository
- Zenodo connection: https://help.zenodo.org/docs/github/enable-repository/
