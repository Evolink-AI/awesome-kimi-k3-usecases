# Awesome Kimi K3 Use Cases Audit Report

Audit date: 2026-07-17
Scope: first-publication repository contract plus the recurring EvoLink conversion-route correction, source grounding, localization, media, GitHub front door, maintainability, and publication readiness

## Audit method

The audit used the active EvoLink usecase repository template, the model-repo pipeline completion contract, the usecase handoff verifier, the GitHub repository review checklist, direct file inspection, structured-data comparison, R2 origin checks, and local Git checks

## Initial findings

| Priority | Finding | Evidence | Required action |
|---|---|---|---|
| P1 | English category anchors used long display-name slugs while localized READMEs and the verifier used stable category keys | Framework verifier reported eight missing anchor/menu errors for four English categories | Standardize English menu links and section anchors to `games-3d`, `frontend-motion`, `coding-integrations`, and `evaluation-limits` |
| P2 | Scaffold SVG banner and logo files remained beside the final PNG banner set | Unused `assets/banner.svg`, `images/en.svg`, and `images/logo.svg` had no public README references | Remove unused scaffold assets so the 11 PNG files are the only banner source of truth |
| P2 | First concurrent public-link audit returned three transient R2 disconnects | `pt.png`, `ru.png`, and `case-08.jpg` returned `RemoteDisconnected` while the other R2 objects returned `206` | Retry the three objects and require a clean complete link audit before publication |

## Source and claim review

- All 10 public cases originate from the supplied `/Users/cheercheung/X-info/热词搜索/kimi-k3` source package
- Each case preserves source URL, author URL, date, evidence type, decision reason, and prompt boundary
- Only Case 1 includes an exact prompt because it is the only selected source that publishes complete reusable prompt text
- The 28 tokens-per-second value is labeled as a single observation rather than a benchmark or guarantee
- Vision quality remains scoped to one practitioner's workload
- Maximum-effort looping remains attributed to an unresolved model-and-harness interaction rather than the model alone
- EvoLink Kimi K3 availability, model ID, model details, and API route now link to the owner-specified EvoLink model page and API documentation; the repository still does not claim an independent paid API smoke test

## 2026-07-17 conversion-route correction audit

- Canonical model destination: `https://evolink.ai/kimi-k3`
- Canonical first-run API destination: `https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat`
- Documented model ID: `kimi-k3`
- Documented API route: `POST /v1/chat/completions`
- Updated surfaces: banner link, top badges, introduction CTA, quick start, related resources, 10 localized README files, structured data, localization source, maintenance notes, update log, and automated verifier
- Removed routes: generic `https://evolink.ai/` CTA and the former official-provider quick-start link from every public README
- Runtime boundary: the model page and API documentation were verified, but no independent credit-consuming API call is claimed
- Initial link-audit result: five transient R2 `RemoteDisconnected` responses while the new EvoLink routes returned HTTP 200
- Remediation: every transient object passed a direct HTTP range retry with 206; the auditor now uses resilient curl checks for R2 and two-worker concurrency
- Final link-audit result: 51 checked, 0 failures

## Repository and localization review

- 11 README files exist in the required order and use the required language badge matrix
- English has 10 cases and localized READMEs contain 100 translated case instances
- Source URL, author URL, type, date, case number, anchor, model ID, and exact public prompt remain stable across languages
- Community files, issue forms, pull request template, maintenance guide, update log, and validation workflow are present
- New repositories do not show a Star History chart before a meaningful live star history exists

## Media review

- All 11 banners are 1774 × 887 PNG files with a 2:1 ratio
- Six source videos use poster-frame plus playable-link presentation and are not directly embedded
- Six videos, six poster frames, two source screenshots, and the banner set were uploaded to the approved R2 namespace
- Public Markdown uses R2 URLs under `github-repo-media/awesome-kimi-k3-usecases`

## Remediation log

1. Replaced English category anchors and menu links with stable contract keys
2. Removed unused scaffold SVG banner and logo assets
3. Re-ran the repository verifier and framework usecase verifier
4. Re-ran R2 and public-link checks after transient failures
5. Re-ran template and GitHub review after all P0/P1 fixes

## Final result

**Local audit status: PASS**

- P0: 0
- P1: 0
- P2: 0 after remediation
- Repository verifier: PASS
- Framework usecase verifier: PASS
- Public-link audit: 51 checked, 0 failures
- Active R2 media: 25 checked, 0 failures
- Localization: 11 README files, 100 translated case instances
- Git diff check: PASS

## Public verification

**Public audit status: PASS**

- Repository: https://github.com/Evolink-AI/awesome-kimi-k3-usecases
- Visibility: public
- Default branch: `main`
- Initial publication commit: `15fceecfd5318c9e5f80f29dba28753368a3410d`
- Pre-push completion gate: PASS with no blockers
- Initial remote branch SHA: matched the local commit
- Raw README SHA-256: matched local content
- Rendered README: banner, cases, R2 poster images, playable video links, and `case-10` verified through GitHub's rendered README API
- About description, homepage, and eight repository topics: verified
- GitHub Actions `Validate repository`: success on the initial publication commit

The final audit-record commit must also pass the same branch readback and validation workflow before this publication is considered complete
