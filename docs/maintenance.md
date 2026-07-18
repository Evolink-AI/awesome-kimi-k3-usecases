# Maintenance

## Source of truth

- Public cases: `data/use-cases.json`
- Selection lineage: `data/ingested_tweets.json`
- Reviewed link exceptions: `data/link-audit-exceptions.json`
- English source: `README.md`
- Language-specific translation sources: `data/localizations/*.json`
- Aggregate localization cache: `data/localization-cache.json`
- Localization build: `python3 scripts/build_localizations.py`
- Recurring-update config: `data/usecase-update-config.json`
- Recurring-update agent: `model-repo-pipeline/bundled-skills/usecase-update-loop`
- Legacy source-media sync: `python3 scripts/sync_source_media.py --source /path/to/use-case-posts.json --apply-data`

The latest recurring source artifact is `.codex/usecase-update-loop/source/20260718T031851Z-twitterapi.json`. It contains 624 deduplicated candidates; 79 fell inside the review window and were classified as 9 high-confidence updates, 8 deferred, 5 unsure, and 57 dropped. The artifact and review package remain ignored local evidence, while `data/ingested_tweets.json` records the public lineage. Future updates must use a new fixed collection timestamp

## Case contract

Every public case requires a contiguous number, stable `case-N` anchor, source URL, author URL, translated title, reader-action takeaway, source-grounded notes, allowed type, ISO date, category, decision reason, dedup key, explicit prompt boundary, source-media lineage, and at least one rendered media asset

Do not invent prompts, workflow steps, results, pricing, benchmark numbers, dates, or attribution. A creator report must remain labeled as a report. A single observation must not be presented as a benchmark

## Update workflow

1. Collect candidates with a fixed timestamp and deduplicate by canonical source URL
2. Classify every candidate, retain only high-confidence cases for publication, and record a decision reason
3. Update `data/use-cases.json` and English README first
4. Resolve and verify the complete handoff package before mutating public files, then upload selected media to the approved R2 namespace and verify every public object before rebuilding READMEs
5. Update each language-specific file under `data/localizations/` with a language-specific agent while preserving anchors, source URLs, author URLs, types, dates, model IDs, code, prompt text, and media order
6. Run the framework verifier, repository verifier, media audit, link audit, and `git diff --check`
7. Fix every P0/P1 issue, then re-run the complete audit before commit or push

If an owner-required source permalink becomes unavailable after collection, preserve the exact permalink, add a visible case-level disclosure, and record the reviewed HTTP status plus source-package evidence in `data/link-audit-exceptions.json`

## Validation

```bash
python3 scripts/build_localizations.py
python3 scripts/verify_repository.py
python3 /path/to/model-repo-pipeline/bundled-skills/usecase-update-loop/scripts/verify_usecase_update.py --repo .
git diff --check
```

## Media

README media uses Cloudflare R2 under `github-repo-media/awesome-kimi-k3-usecases`. Every public case must render at least one source-backed visual. Videos use R2-hosted poster frames with playable links rather than direct video embeds, while image cases preserve every usable source image. Local staging media under `media/cases/` and `media/source-cases/` is ignored after upload, while language banners remain versioned as repository assets

The complete case index belongs inside the top `## 📑 Menu`. Do not repeat case tables inside category sections. Creator links in Acknowledge remain one comma-separated inline list rather than one creator per bullet

## Related surfaces

This repository links the verified EvoLink Kimi K3 landing page and OpenAI-compatible Chat Completions documentation. No distinct browser/no-code Kimi K3 surface has been verified. Any installable skill, browser-trial claim, or independent paid API smoke-test claim must be verified in the appropriate release pipeline before the README can claim it
