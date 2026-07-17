# Awesome Kimi K3 Use Cases Audit Report

Audit date: 2026-07-17

Scope: all 70 high-confidence use cases, English plus ten localized README files, owner-provided and localized banners, source lineage, template compliance, EvoLink conversion routes, public links, R2 media, repository front door, maintainability, and release readiness

## Final decision

**Pre-push audit status: PASS**

- P0: 0
- P1: 0
- P2 requiring remediation: 0
- Reviewed source exceptions: 1 active and visibly disclosed
- Commit and push are permitted only after the clean-worktree pre-push completion gate also passes

## Requirements and authoritative evidence

| Requirement | Evidence | Result |
|---|---|---|
| Include every high-confidence case | Supplied `use-case-posts.json` has 70 items and `confidence_counts.high=70`; canonical URL-set comparison is 70/70 with 0 missing, 0 unexpected, and 0 field errors | PASS |
| Exclude lower-confidence cases | Source metadata records 31 removed medium-confidence candidates; all canonical `decision` values are `high_confidence_update` and all `quality_tier` values are `high` | PASS |
| Build all repository languages | 11 README files × 70 cases = 770 localized case instances; each localized JSON has 70 complete records, 0 blank records, and 0 unchanged English titles | PASS |
| Preserve stable case identity | Case numbers remain 1–70; every README has 70 `case-<n>` anchors and 70 category-table links; immutable source, author, type, and date fields match English | PASS |
| Use the requested English banner | `images/en-v2.png` is the owner-supplied 1774 × 887 RGB PNG and is the English README banner | PASS |
| Localize remaining banners | Nine ChatGPT Image 2 localized 1774 × 887 RGB PNG files are active; Portuguese intentionally reuses `en-v2.png` under the owner's English fallback instruction | PASS |
| Upload and replace through R2 | All ten active banner objects have local/remote SHA-256 equality and return HTTP 206 from the required `github-repo-media/awesome-kimi-k3-usecases` namespace | PASS |
| Route model CTA to EvoLink | Banner, badges, introduction, Quick API Access, and related resources link to `https://evolink.ai/kimi-k3` with surface-specific UTM parameters | PASS |
| Provide quick API access | README includes a copyable Bearer-authenticated `POST https://direct.evolink.ai/v1/chat/completions` request with model `kimi-k3`, verified from the owner-specified OpenAPI document | PASS |
| Add the article as a jump link | `https://evolink.ai/blog/is-kimi-k3-available-on-evolink` appears exactly once in every README and is not expanded into a separate article introduction | PASS |
| Pass repository and public audit | Repository verifier, shape-specific usecase verifier, framework integrity check, Star History policy, Git diff check, media hash audit, and 159-URL public audit all pass | PASS |

## Source and content audit

- Supplied source artifact: `/Users/cheercheung/X-info/热词搜索/kimi-k3/use-case-posts.json`
- Source total after owner-required filtering: 70
- Source high-confidence total: 70
- Canonical structured total: 70
- Unique source URLs: 70
- Source/canonical URL-set difference: 0 missing, 0 unexpected
- Author handle, author URL, date, likes, views, bookmarks, and repost field differences: 0
- Category counts: 22 games/3D, 15 frontend/motion, 8 coding/integrations, 25 evaluation/limits
- Evidence-type counts: 33 Demo, 16 Evaluation, 11 Benchmark, 5 Tutorial, 3 Limit, 2 Integration
- Exact public prompt boundary: one case only; no missing prompt was reconstructed
- Claims about cost, speed, rankings, quality, and failure modes remain attributed and bounded to the supplied evidence

## Localization audit

- README language set: English, Spanish, Portuguese, Japanese, Korean, German, French, Turkish, Traditional Chinese, Simplified Chinese, and Russian
- Every README contains 70 case headings, 70 stable anchors, 70 category-summary links, the required menu, source attribution, metadata, related resources, and acknowledgement/correction policy
- Every language-specific source contains keys 1–70 with non-empty title, takeaway, and notes fields
- Translated title residuals matching English: 0 in every locale
- Language badge blocks: 11 checked, 1 unique canonical block
- Simplified and Traditional Chinese README full-width sentence-ending `。` count: 0
- Code, model ID, API endpoint, exact public prompt, URLs, dates, and evidence types remain unchanged across languages
- The generic `verify_localized_readmes.py` parser is not authoritative for this active template because it only accepts section-prefixed case anchors and a different per-case output/prompt schema; the active shape-specific verifier and repository verifier both pass all 770 instances

## Template and GitHub repository review

- Required front door is present: banner, badges, language matrix, title, Introduction, Overview, Quick API Access, Menu, four category sections, Related Resources, Acknowledge, license, and community files
- Every category includes a summary table and stable case anchors
- The correction statement is italicized in all 11 README files
- `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, issue forms, pull request template, maintenance guide, update log, validation workflow, structured data, and deterministic localization builder are present
- GitHub About is public and points to `https://evolink.ai/kimi-k3`; description and eight topics are populated
- Live Star History policy check: 0 stars, threshold 10, chart correctly absent from all 11 README files
- `github-repo-review-action-list.md` records no remaining P0/P1/P2 remediation

## Media and R2 audit

- Active banner files: 10 local PNG files, all 1774 × 887, 2:1, RGB
- English: owner-provided `en-v2.png`
- Localized: `de-v2.png`, `es-v2.png`, `fr-v2.png`, `ja-v2.png`, `ko-v2.png`, `ru-v2.png`, `tr-v2.png`, `zh-TW-v2.png`, and `zh-v2.png`
- Portuguese: intentional English fallback; no `pt-v2.png`
- Existing case media: six MP4 files plus six poster JPG files
- Public Markdown embeds poster images and links playable MP4 files; it does not directly embed video elements
- All active banner and case-media R2 URLs returned HTTP 206 in the final link audit

## Initial findings and remediation

| Priority | Initial finding | Remediation | Re-audit |
|---|---|---|---|
| P1 | README exposed links but lacked the template-required copyable Quick API Access call | Added verified EvoLink base URL, endpoint, Bearer environment variable, model ID, and minimal request to all 11 README files | PASS |
| P1 | Localized category sections lacked the English category-summary table structure | Added translated 70-case summary links across all ten localized README files | PASS |
| P1 | The initial full-cycle intake used labels that did not match the orchestrator contract | Added exact conversion-path fields and re-ran full-cycle; intake P1 count is now 0 | PASS |
| P1 | The link auditor treated a POST-only API endpoint in a fenced curl block as a GET link | Excluded fenced code blocks from public-link extraction | PASS |
| P1 | Concurrent `urllib` checks produced random URL and SSL transport failures | Standardized the auditor on retrying curl checks and re-ran the complete URL set | PASS |
| P2 | Case 67's exact collected source permalink now returns HTTP 404 | Preserved the owner-required case, added a visible warning in all README files, and recorded source-package evidence in `data/link-audit-exceptions.json` | ACCEPTED |
| P2 | The collected `@filicroval` profile intermittently returned HTTP 404 while both attributed posts stayed reachable | Preserved attribution and recorded the reviewed profile contingency; the final audit returned HTTP 200 for the profile and both posts | PASS |

## Final verification commands

```bash
python3 scripts/build_localizations.py
python3 scripts/verify_repository.py
python3 /Users/cheercheung/agent-repo/agents/model-repo-pipeline/bundled-skills/usecase-update-loop/scripts/verify_usecase_update.py --repo .
python3 scripts/audit_public_links.py
python3 /Users/cheercheung/agent-repo/agents/model-repo-pipeline/scripts/verify_star_history_policy.py --repo . --repository Evolink-AI/awesome-kimi-k3-usecases --json
python3 /Users/cheercheung/agent-repo/agents/model-repo-pipeline/scripts/validate_framework.py
git diff --check
```

Final results:

- Repository verifier: PASS, 11 README files, 70 cases, 770 localized case instances
- Shape-specific usecase verifier: PASS, English 70, localized README files 10
- Public links: PASS, 159 checked, 1 accepted disclosed exception, 0 failures
- Star History policy: PASS, 0 stars, chart absent
- Active banner local/R2 hash identity: PASS, 10/10
- Framework integrity: PASS, 43 required files and 8 active-template files
- Git diff check: PASS

## Public verification

**Post-push public status: PASS**

- Repository: https://github.com/Evolink-AI/awesome-kimi-k3-usecases
- Visibility: public
- Default branch: `main`
- Published content commit: `16c93cd417f6705199ea34ab4774de265b0acf58`
- Remote branch SHA after content push: exact match
- Local and raw GitHub README SHA-256: `a8a700b7618b01d0acbfb94d9d30c115bb6e3670a6207f3f3867808d55056904`, exact match
- GitHub rendered README HTML: 173,331 bytes and contains `case-70`, Quick API Access, the EvoLink article link, `en-v2.png`, and the Case 67 source-status warning
- GitHub rendered media audit: 21 images checked, 0 failures; English banner, six case posters, license/API badges, and all language badges passed through GitHub camo and canonical-origin checks
- GitHub Actions `Validate repository`: success for the published content commit
- Actions run: https://github.com/Evolink-AI/awesome-kimi-k3-usecases/actions/runs/29588772566
- GitHub About: public, homepage `https://evolink.ai/kimi-k3`, description populated, eight topics populated

The follow-up audit-record commit must pass the same branch readback and validation workflow before final completion is claimed
