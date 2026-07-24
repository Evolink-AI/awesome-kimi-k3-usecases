# Maintenance

## Source of truth

- Public cases: `data/use-cases.json`
- Source-fidelity expected set: `data/source-fidelity-manifest.json`
- Selection lineage: `data/ingested_tweets.json`
- Reviewed link exceptions: `data/link-audit-exceptions.json`
- English source: `README.md`
- Language-specific translation sources: `data/localizations/*.json`
- Aggregate localization cache: `data/localization-cache.json`
- Localization build: `python3 scripts/build_localizations.py`
- Source-media sync: `python3 scripts/sync_source_media.py --source /path/to/use-case-posts.json --apply-data`
- Source-fidelity build: `python3 scripts/build_source_fidelity_package.py --source /path/to/use-case-posts.json --package .codex/audits/source-fidelity-package.json`
- Multi-source fidelity build for this release: `python3 scripts/build_source_fidelity_package.py --source /path/to/use-case-posts.json --supplemental-git-ref 6228470f7726a4385b3a098f9acdb151a9608ec2 --combined-source .codex/audits/combined-use-case-source.json --package .codex/audits/source-fidelity-package.json`

The latest recurring source artifacts are under `.codex/usecase-update-loop/runs/20260724T034504Z/` with fixed collector window end `2026-07-24T03:49:12.113468+00:00`. The collector returned 667 deduplicated candidates; 66 fell inside the review window and were classified as 10 high-confidence updates, 15 deferred, 14 unsure, and 27 dropped. The artifact and review package remain ignored local evidence, while `data/ingested_tweets.json` records the public lineage. Future updates must use a new fixed collection timestamp

## Case format and contract

Every public case requires a contiguous number, stable `case-N` anchor, source URL, author URL, translated title, reader-action takeaway, source-grounded notes, allowed type, ISO date, category, decision reason, dedup key, explicit prompt boundary, source-media lineage, and at least one rendered media asset

Do not invent prompts, workflow steps, results, pricing, benchmark numbers, dates, or attribution. A creator report must remain labeled as a report. A single observation must not be presented as a benchmark

## Update workflow

1. Collect candidates with a fixed timestamp and deduplicate by canonical source URL
2. Classify every candidate, retain only high-confidence cases for publication, and record a decision reason
3. Update `data/use-cases.json` and English README first
4. Run `scripts/sync_source_media.py --source /path/to/use-case-posts.json --apply-data`, upload the prepared files to the approved R2 namespace, and verify every public object before rebuilding READMEs
5. Build `data/source-fidelity-manifest.json` and the run-local handoff package with `scripts/build_source_fidelity_package.py`, then pass the framework handoff verifier before README mutation
6. Update each language-specific file under `data/localizations/` with a language-specific agent while preserving anchors, source URLs, author URLs, types, dates, model IDs, code, prompt text, and media order
7. Run the framework verifier, repository verifier, R2 source-media audit, public-link audit, and `git diff --check`
8. Fix every P0/P1 issue, then re-run the complete audit before commit or push
9. Immediately before the pre-push completion gate, fetch the target branch and prove that `HEAD` contains the current remote SHA; any remote advance invalidates the previous gate and requires integration plus a full re-audit

If an owner-required source permalink becomes unavailable after collection, preserve the exact permalink, add a visible case-level disclosure, and record the reviewed HTTP status plus source-package evidence in `data/link-audit-exceptions.json`

## Validation

```bash
python3 scripts/build_localizations.py
python3 scripts/verify_repository.py
python3 scripts/audit_r2_source_media.py --report .codex/audits/r2-source-media-audit.md
python3 scripts/audit_public_links.py --report .codex/audits/public-link-audit.md
python3 /path/to/model-repo-pipeline/bundled-skills/usecase-update-loop/scripts/verify_usecase_update.py --repo .
git diff --check
```

## Media

README media uses Cloudflare R2 under `github-repo-media/awesome-kimi-k3-usecases`. Every public case must render the complete expected visual set from `data/source-fidelity-manifest.json`. Videos use R2-hosted poster frames with playable R2 MP4 links rather than direct video embeds, while image cases preserve every usable source image. Local staging media under `media/cases/` and `media/source-cases/` is ignored after upload, while language banners remain versioned as repository assets

The complete case index belongs inside the top `## 📑 Menu`. Do not repeat case tables inside category sections. Creator links in Acknowledge remain one comma-separated inline list rather than one creator per bullet

## Related surfaces

This repository links the verified EvoLink Kimi K3 landing page and OpenAI-compatible Chat Completions documentation. No distinct browser/no-code Kimi K3 surface has been verified. Any installable skill, browser-trial claim, or independent paid API smoke-test claim must be verified in the appropriate release pipeline before the README can claim it
