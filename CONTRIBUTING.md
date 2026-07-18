# Contributing

Thank you for helping improve this Kimi K3 usecase collection

## Propose a case

Open the use-case issue form or a pull request with the original public source, creator profile, reader-action takeaway, evidence type, date, and any known limitations

Only submit concrete workflows, demos, integrations, evaluations, benchmarks, or limitations. Do not reconstruct a prompt that the source did not publish

## Required checks

```bash
python3 scripts/build_localizations.py
python3 scripts/verify_repository.py
python3 scripts/audit_r2_source_media.py --report .codex/audits/r2-source-media-audit.md
python3 scripts/audit_public_links.py --report .codex/audits/public-link-audit.md
git diff --check
```

All 11 README files must preserve source URLs, author URLs, type, date, anchors, model IDs, exact public prompt text, and the 79-item visual expected set. Any media change must update `data/source-fidelity-manifest.json`, preserve source lineage, and keep every video poster and playable MP4 on the approved R2 namespace

## Corrections

For attribution or factual corrections, use the correction issue form and include a public source
