# Provenance, licensing and release restrictions

## Uploaded source materials

All four ZIP archives are preserved without modification in this GitHub template; their hashes are in `archive_manifest.json` and `ARCHIVE_CHECKSUMS.sha256`. The documentation and scripts are original packaging created for reproducible access, not replacements for the original scientific model.

## Licensing gate

The `ASTE_Long_Context_Feasible(1).zip` contains simulation source and a compiled Windows `.mexw64`, including material associated with the ASTE framework. The ASTE publication is attributed in the supplied model notes to Markaj, Mercangöz and Fay, *Computers & Chemical Engineering* (2024), article 108798, DOI: https://doi.org/10.1016/j.compchemeng.2024.108798 . **The paper citation does not grant permission to redistribute its source files or binary.** Read the source file headers and upstream license terms and obtain permission as needed. The exact copyright owner and redistribution license are not determined by this packaging exercise.

The published ZIPs might also contain local machine paths or metadata. Verify no confidential files, proprietary datasets, credentials, personal information or paths that you do not want to disclose. The original study is synthetic, but still inspect each asset before publication.

Do not assert an MIT/Apache/CC license for all uploaded files without separate authorization. If approved, label your **own code**, model outputs and third-party material with distinct license scopes. If permission is unavailable, publish the three Python packages and a descriptive ASTE acquisition/execution guide **instead of** publishing the restricted fourth ZIP, and explain the unavoidable reproduction restriction.

## Distinct result provenance

The conflict ZIP's `input/reference_ai_provenance.json` documents internally regenerated reference AI outputs. The separate standalone AI ZIP may have slightly different predictions and metrics. The `run_bundled_reference.py` route uses archived reference inputs, whereas `run_package.py` tests matching external local human/AI results when the sibling archives have been extracted. No paper claim should combine unlike provenance records.

## Versioned scientific record

Preserve the original uploads as read-only input artifacts. If correcting paths, repairing dependency versions or changing algorithms, make separate versioned releases. Disclose all deviations from the archived evidence; do not rewrite the original ZIP and retain its previous hash/version label. CI can test the Python verification on extracted sources, but it cannot claim a newly validated physical CSTR model or independent human-subject evaluation.
