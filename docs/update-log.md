# Update Log

## 2026-07-18 — Daily recurring update to 79 cases

- Collected 624 deduplicated X/Twitter candidates across 10 Kimi K3 queries with a fixed `20260718T031851Z` timestamp, a 24-hour window, minimum 11 likes, and at most three pages per query
- Semantically reviewed all 79 in-window candidates: 9 high-confidence updates, 8 deferred, 5 unsure, and 57 dropped
- Added Cases 71–79 to the English source and all ten localized editions, including games, self-testing workflows, frontend comparisons, coding-agent evaluations, a Codex/OpenCode integration, a website tutorial, and a ChatLLM router
- Uploaded 14 source-backed images, video posters, and playable videos to the approved R2 namespace; local staging media remains ignored
- Reduced Quick Start to two pre-code actions, added the explicit `POST https://direct.evolink.ai/v1/chat/completions` endpoint, removed misleading browser-trial copy, and recorded that neither an independent browser surface nor a paid API smoke was verified
- Generalized repository verification from a hard-coded 70-case baseline to the structured public case count

## 2026-07-17 — Complete source media and centralized navigation

- Restored source-backed media for all 70 high-confidence cases, including 53 video cases and 17 image cases
- Uploaded 73 new source images or video posters to R2 and rendered 79 total media assets in each of the 11 README editions
- Centralized all 70 case links in one Menu table near the top and removed repeated navigation tables from the four category sections
- Replaced one-creator-per-line Acknowledge bullets with one comma-separated inline creator list
- Added a reproducible source-media sync script, stricter media and layout verification, and a dedicated audit report
- Passed repository verification and a 277-URL public audit with zero unhandled failures

## 2026-07-17 — Full high-confidence expansion and localized banners

- Filtered the supplied `use-case-posts.json` from 101 candidates to all 70 high-confidence cases and excluded all 31 medium-confidence cases
- Expanded the English README and ten localized editions to 70 source-backed cases each, for 770 localized case instances
- Preserved stable case 1–6 anchors and grouped the complete numbered set under the repository's four category anchors
- Generated nine localized 1774 × 887 banners with ChatGPT Image 2, uploaded each through a new R2 `*-v2.png` key, and reused the English `en-v2.png` banner for Portuguese as requested
- Split translation sources by locale under `data/localizations/` and retained the aggregate localization cache for compatibility
- Preserved source attribution, dates, numeric facts, prompt boundaries, self-reported benchmark caveats, and limitation cases across all languages
- Preserved one post-collection unavailable source permalink as Case 67 with a visible disclosure and a reviewed link-audit exception backed by the supplied source package
- Preserved the supplied `@filicroval` attribution through a reviewed author-profile exception because both attributed source posts remain reachable while the profile URL returns 404

## 2026-07-17 — Owner-provided English banner replacement

- Replaced the English README banner with the owner-provided 1774 × 887 PNG
- Kept the existing model-page click target and banner UTM attribution
- Used a new R2 object key to avoid stale GitHub camo cache reuse
- Preserved the existing localized banners because no translated replacements were requested

## 2026-07-17 — Kimi K3 related reading link

- Added the owner-specified EvoLink Kimi K3 article as a Related Resources jump link across all 11 README files
- Kept the article as a link only, without adding a dedicated introduction or new availability claim

## 2026-07-17 — EvoLink conversion route correction

- Replaced generic and official-provider first-run CTAs with the owner-specified EvoLink Kimi K3 model page
- Routed Quick Start to the EvoLink Kimi K3 Chat Completions documentation
- Updated all 11 language editions, badges, banner clicks, related resources, audit wording, and GitHub About homepage
- Preserved the boundary that this usecase repository has not run an independent paid API smoke test

## 2026-07-17 — First publication candidate

- Curated 10 high-confidence cases from the supplied Kimi K3 source package
- Added 11 complete language editions with localized titles, takeaways, notes, navigation, and banners
- Uploaded six videos, six poster frames, two screenshots, and language banners to the approved R2 namespace
- Added source lineage, maintenance documentation, contribution templates, local verification, and audit evidence
- Preserved unverified boundaries for EvoLink availability, missing prompts, single-user throughput, personal vision quality, and model-versus-harness looping
