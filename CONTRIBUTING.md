# Contributing

Thank you for helping improve this Kimi K3 usecase collection

## Propose a case

Open the use-case issue form or a pull request with the original public source, creator profile, reader-action takeaway, evidence type, date, and any known limitations

Only submit concrete workflows, demos, integrations, evaluations, benchmarks, or limitations. Do not reconstruct a prompt that the source did not publish

## Required checks

```bash
python3 scripts/build_localizations.py
python3 scripts/verify_repository.py
git diff --check
```

All 11 README files must preserve source URLs, author URLs, type, date, anchors, model IDs, and exact public prompt text. Visible prose in localized README files must be translated

## Corrections

For attribution or factual corrections, use the correction issue form and include a public source
