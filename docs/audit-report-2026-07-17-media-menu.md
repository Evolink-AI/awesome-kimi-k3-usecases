# Media, Menu, and Acknowledge Audit

Date: 2026-07-17

## Verdict

PASS after remediation

- Public cases: 70 high-confidence cases
- Localized README files: 11
- Localized case instances: 770
- Source-backed media coverage: 70/70 cases
- Media inventory: 53 video cases, 17 image cases, 79 rendered media assets
- Public URLs checked: 277
- Unhandled public-link failures: 0
- Reviewed exceptions: 1 unavailable source permalink with a visible case-level warning

## Initial findings

| Priority | Finding | Evidence | Resolution |
|---|---|---|---|
| P1 | Cases 7–70 rendered without media even though every selected source record contained media | `data/use-cases.json` classified 64 cases as `none`; the supplied source artifact contained media for all 70 cases | Restored source-backed media lineage, uploaded 73 new images or video posters to R2, and rendered 79 media assets across every README |
| P1 | Case navigation was repeated inside four category sections instead of being centralized near the top | Every category section contained its own summary table | Replaced the repeated tables with one 70-row case index inside `## 📑 Menu`; category sections now contain case bodies only |
| P2 | Acknowledge listed one creator per bullet | Creator attribution occupied one Markdown list row per handle | Rebuilt attribution as one comma-separated inline list in every README |
| P1 | The first public-link re-audit found a second 404 URL derived from the already unavailable Case 67 source | The original source permalink was reviewed, but its `/video/1` derivative was not part of the declared exception | Pointed the Case 67 media action at the disclosed source permalink and repeated the full audit without adding a broader exception |

## Remediation details

- Added `scripts/sync_source_media.py` to map the canonical 70-case set back to the supplied source artifact by canonical X URL
- Preserved all usable source visuals rather than generating substitute case media
- Used R2-hosted posters for video cases and R2-hosted originals for image cases
- Kept the six existing R2 video files for Cases 1–6 and linked later video posters to their public X video surfaces
- Added source-media lineage and structured media assets to `data/use-cases.json`
- Updated the localization builder so media, centralized Menu structure, and attribution formatting remain identical across all 11 editions
- Extended the repository verifier to fail if any case lacks media, any per-category menu table returns, or Acknowledge reverts to one creator per line

## Re-audit evidence

```text
python3 scripts/verify_repository.py
PASS
readmes=11
cases=70
localized_case_instances=770
public_prompt_cases=1
r2_policy=pass
```

```text
python3 scripts/audit_public_links.py
checked=277 accepted_exceptions=1 failures=0
```

The accepted exception is the already disclosed unavailable Case 67 source permalink. Its poster remains publicly readable from R2, and the README preserves a visible warning instead of silently replacing the source

## Publication gate

The media, Menu, Acknowledge, localization, source-lineage, public-link, framework, syntax, and diff checks all pass. P0: 0, P1: 0, P2: 0. This update is eligible for public push
