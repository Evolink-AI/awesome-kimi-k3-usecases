# Maintenance

## Source of truth

- Public cases: `data/use-cases.json`
- Selection lineage: `data/ingested_tweets.json`
- Reviewed link exceptions: `data/link-audit-exceptions.json`
- English source: `README.md`
- Language-specific translation sources: `data/localizations/*.json`
- Aggregate localization cache: `data/localization-cache.json`
- Localization build: `python3 scripts/build_localizations.py`

The current source artifact is `/Users/cheercheung/X-info/热词搜索/kimi-k3/use-case-posts.json`, filtered at `2026-07-17T15:57:58+0800` to retain all 70 high-confidence items and exclude all 31 medium-confidence items. Future public updates must record a new source artifact and fixed collection timestamp

## Case contract

Every public case requires a contiguous number, stable `case-N` anchor, source URL, author URL, translated title, reader-action takeaway, source-grounded notes, allowed type, ISO date, category, decision reason, dedup key, and explicit prompt boundary

Do not invent prompts, workflow steps, results, pricing, benchmark numbers, dates, or attribution. A creator report must remain labeled as a report. A single observation must not be presented as a benchmark

## Update workflow

1. Collect candidates with a fixed timestamp and deduplicate by canonical source URL
2. Classify every candidate, retain only high-confidence cases for publication, and record a decision reason
3. Update `data/use-cases.json` and English README first
4. Update each language-specific file under `data/localizations/` with a language-specific agent while preserving anchors, source URLs, author URLs, types, dates, model IDs, code, and prompt text
5. Run the framework verifier, repository verifier, media audit, link audit, and `git diff --check`
6. Fix every P0/P1 issue, then re-run the complete audit before commit or push

If an owner-required source permalink becomes unavailable after collection, preserve the exact permalink, add a visible case-level disclosure, and record the reviewed HTTP status plus source-package evidence in `data/link-audit-exceptions.json`

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

This repository links the verified EvoLink Kimi K3 model page and OpenAI-compatible Chat Completions documentation. Any installable skill or independent paid API smoke-test claim must still be verified in the appropriate release pipeline before the README can claim it
