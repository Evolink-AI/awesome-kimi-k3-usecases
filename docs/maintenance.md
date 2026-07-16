# Maintenance

## Source of truth

- Public cases: `data/use-cases.json`
- Selection lineage: `data/ingested_tweets.json`
- English source: `README.md`
- Localization cache: `data/localization-cache.json`
- Localization build: `python3 scripts/build_localizations.py`

The first-publication source artifact was `/Users/cheercheung/X-info/热词搜索/kimi-k3/posts.json`, generated at `2026-07-16T15:40:09.165295+00:00`. Future public updates must record a new source artifact and fixed collection timestamp

## Case contract

Every public case requires a contiguous number, stable `case-N` anchor, source URL, author URL, translated title, reader-action takeaway, source-grounded notes, allowed type, ISO date, category, decision reason, dedup key, and explicit prompt boundary

Do not invent prompts, workflow steps, results, pricing, benchmark numbers, dates, or attribution. A creator report must remain labeled as a report. A single observation must not be presented as a benchmark

## Update workflow

1. Collect candidates with a fixed timestamp and deduplicate by canonical source URL
2. Classify every candidate and record a decision reason
3. Update `data/use-cases.json` and English README first
4. Translate visible prose while preserving anchors, source URLs, author URLs, types, dates, model IDs, code, and prompt text
5. Run the framework verifier, repository verifier, media audit, link audit, and `git diff --check`
6. Fix every P0/P1 issue, then re-run the complete audit before commit or push

## Validation

```bash
python3 scripts/build_localizations.py
python3 scripts/verify_repository.py
python3 /path/to/model-repo-pipeline/bundled-skills/usecase-update-loop/scripts/verify_usecase_update.py --repo .
git diff --check
```

## Media

README media uses Cloudflare R2 under `github-repo-media/awesome-kimi-k3-usecases`. Videos are linked through R2-hosted poster frames and playable video URLs rather than embedded directly. Local source media under `media/cases/` is ignored after upload, while language banners remain versioned as repository assets

## Related surfaces

This repository links only verified model resources. Kimi K3 availability on EvoLink, any installable skill, and any provider-specific API smoke test must be verified in the appropriate release pipeline before the README can claim them
