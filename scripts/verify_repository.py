#!/usr/bin/env python3
"""Verify the public Kimi K3 usecase repository contract."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_CASES = 70
LOCALES = ["", "es", "pt", "ja", "ko", "de", "fr", "tr", "zh-TW", "zh-CN", "ru"]
FILENAMES = ["README.md"] + [f"README_{locale}.md" for locale in LOCALES[1:]]
CASE_RE = re.compile(
    r'^### Case (\d+): \[([^\]]+)\]\((https://x\.com/[^)]+)\) '
    r'\(by \[(@[^\]]+)\]\((https://x\.com/[^)]+)\)\)',
    re.MULTILINE,
)
META_RE = re.compile(r"^Type: (Demo|Tutorial|Evaluation|Integration|Benchmark|Limit) \| Date: (\d{4}-\d{2}-\d{2})$", re.MULTILINE)
R2_PREFIX = "https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/"
MODEL_PAGE_PREFIX = "https://evolink.ai/kimi-k3"
API_DOCS_PREFIX = "https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat"
ARTICLE_PREFIX = "https://evolink.ai/blog/is-kimi-k3-available-on-evolink"
API_ENDPOINT = "https://direct.evolink.ai/v1/chat/completions"
KIMIK3_IO_BY_LOCALE = {
    "zh-TW": "https://kimik3.io/zh",
    "zh-CN": "https://kimik3.io/zh",
    "ru": "https://kimik3.io/ru/",
}


def fail(errors: list[str]) -> int:
    print("FAIL")
    for error in errors:
        print(f"- {error}")
    return 1


def main() -> int:
    errors: list[str] = []
    missing = [name for name in FILENAMES if not (ROOT / name).is_file()]
    if missing:
        errors.append(f"missing README files: {missing}")

    required = [
        "LICENSE", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "SECURITY.md",
        ".github/PULL_REQUEST_TEMPLATE.md", ".github/ISSUE_TEMPLATE/case.yml",
        ".github/ISSUE_TEMPLATE/correction.yml", "docs/maintenance.md",
        "docs/update-log.md", "data/use-cases.json", "data/localization-cache.json",
        "data/ingested_tweets.json", "data/link-audit-exceptions.json",
        "data/source-fidelity-manifest.json",
    ]
    required.extend(f"data/localizations/{locale}.json" for locale in LOCALES[1:])
    errors.extend(f"missing required file: {path}" for path in required if not (ROOT / path).is_file())
    if errors:
        return fail(errors)

    data = json.loads((ROOT / "data/use-cases.json").read_text(encoding="utf-8"))
    items = data.get("items", [])
    if len(items) != EXPECTED_CASES:
        errors.append(f"structured case count is {len(items)}, expected {EXPECTED_CASES}")
    numbers = [item.get("public_number") for item in items]
    expected_numbers = list(range(1, EXPECTED_CASES + 1))
    if numbers != expected_numbers:
        errors.append(f"structured numbers are not contiguous: {numbers}")
    sources = [item.get("source_url") for item in items]
    if len(sources) != len(set(sources)):
        errors.append("structured source URLs are not unique")
    if any(item.get("decision") != "high_confidence_update" for item in items):
        errors.append("structured data contains a non-high-confidence decision")
    if any(item.get("quality_tier") != "high" for item in items):
        errors.append("structured data contains a non-high quality tier")
    if any(item.get("media_type") not in {"video", "image"} for item in items):
        errors.append("structured data contains a case without source media")
    if sum(item.get("media_type") == "video" for item in items) != 53:
        errors.append("structured media classification does not contain 53 video cases")
    if sum(item.get("media_type") == "image" for item in items) != 17:
        errors.append("structured media classification does not contain 17 image cases")
    if any(not item.get("media_assets") for item in items):
        errors.append("structured data contains a case without media assets")
    if any(not item.get("media_source_urls") for item in items):
        errors.append("structured data contains a case without source-media lineage")
    if sum(len(item.get("media_assets", [])) for item in items) != 79:
        errors.append("structured data does not contain the expected 79 media assets")
    for item in items:
        for asset in item.get("media_assets", []):
            if asset.get("kind") == "video" and not asset.get("poster_url", "").startswith(R2_PREFIX):
                errors.append(f'case {item.get("public_number")}: video poster is not on repository R2')
            if asset.get("kind") == "video" and not asset.get("url", "").startswith(R2_PREFIX):
                errors.append(f'case {item.get("public_number")}: playable video is not on repository R2')
            if asset.get("kind") == "image" and not asset.get("url", "").startswith(R2_PREFIX):
                errors.append(f'case {item.get("public_number")}: source image is not on repository R2')
    if sum(bool(item.get("prompt_public")) for item in items) != 1:
        errors.append("exactly one case must expose a public prompt")
    if items and items[0].get("prompt_text") != "Voxel star wars pod-racers run":
        errors.append("case 1 exact public prompt changed")
    category_order = ["games-3d", "frontend-motion", "coding-integrations", "evaluation-limits"]
    expected_readme_order = [
        item["public_number"]
        for category in category_order
        for item in items
        if item.get("category_key") == category
    ]
    if sorted(expected_readme_order) != expected_numbers:
        errors.append("category grouping does not cover the contiguous structured case set")
    if not str(data.get("source_artifact", "")).endswith("/use-case-posts.json"):
        errors.append("structured data does not point to the high-confidence source artifact")
    unavailable = [item for item in items if item.get("source_status_note")]
    if len(unavailable) != 1 or unavailable[0].get("public_number") != 67:
        errors.append("source availability disclosure must identify only case 67")

    fidelity = json.loads((ROOT / "data/source-fidelity-manifest.json").read_text(encoding="utf-8"))
    fidelity_cases = fidelity.get("cases", [])
    if fidelity.get("selected_case_count") != EXPECTED_CASES:
        errors.append("source fidelity selected case denominator is not 70")
    if fidelity.get("cases_with_source_media") != EXPECTED_CASES:
        errors.append("source fidelity media case denominator is not 70")
    if fidelity.get("expected_public_visual_count") != 79:
        errors.append("source fidelity expected media denominator is not 79")
    if not re.fullmatch(r"[0-9a-f]{64}", str(fidelity.get("source_manifest_sha256", ""))):
        errors.append("source fidelity manifest lacks a valid source SHA256")
    expected_presentation = {
        "menu_layout": "centralized-single-table",
        "acknowledge_layout": "inline-comma",
        "quick_start_position": "penultimate-section",
        "media_policy": "all-source-media",
        "video_playback_policy": "r2-playable",
        "localization_fallback": "english",
    }
    if fidelity.get("owner_presentation") != expected_presentation:
        errors.append("source fidelity owner presentation differs from the locked contract")
    if len(fidelity_cases) != EXPECTED_CASES:
        errors.append("source fidelity case set is not complete")
    else:
        for item, manifest_case in zip(items, fidelity_cases):
            expected_visuals = [
                asset["poster_url"] if asset["kind"] == "video" else asset["url"]
                for asset in item.get("media_assets", [])
            ]
            expected_playable = next(
                (asset["url"] for asset in item.get("media_assets", []) if asset["kind"] == "video"),
                None,
            )
            if manifest_case.get("public_number") != item.get("public_number"):
                errors.append(f'case {item.get("public_number")}: source fidelity number differs')
            if manifest_case.get("source_url") != item.get("source_url"):
                errors.append(f'case {item.get("public_number")}: source fidelity URL differs')
            if manifest_case.get("source_media_urls") != item.get("media_source_urls"):
                errors.append(f'case {item.get("public_number")}: source fidelity media lineage differs')
            if manifest_case.get("expected_public_media_urls") != expected_visuals:
                errors.append(f'case {item.get("public_number")}: source fidelity expected visuals differ')
            if manifest_case.get("playable_video_url") != expected_playable:
                errors.append(f'case {item.get("public_number")}: source fidelity playable video differs')

    link_exceptions = json.loads((ROOT / "data/link-audit-exceptions.json").read_text(encoding="utf-8"))
    exception_items = link_exceptions.get("exceptions", [])
    exception_urls = {item.get("url") for item in exception_items}
    if len(exception_items) != 2 or not unavailable or unavailable[0].get("source_url") not in exception_urls:
        errors.append("link audit exception does not match the disclosed unavailable source")
    if "https://x.com/filicroval" not in exception_urls:
        errors.append("link audit exception does not preserve the unavailable author profile")

    ingested = json.loads((ROOT / "data/ingested_tweets.json").read_text(encoding="utf-8"))
    selected_ids = ingested.get("selected_ids", [])
    expected_ids = [str(source).rstrip("/").split("/")[-1] for source in sources]
    if selected_ids != expected_ids:
        errors.append("ingested tweet lineage differs from structured case order")

    locale_configs = {}
    for locale in LOCALES[1:]:
        config = json.loads((ROOT / "data" / "localizations" / f"{locale}.json").read_text(encoding="utf-8"))
        locale_configs[locale] = config
        keys = [int(key) for key in config.get("cases", {}).keys()]
        if keys != expected_numbers:
            errors.append(f"data/localizations/{locale}.json: translation keys are {keys}")

    aggregate = json.loads((ROOT / "data/localization-cache.json").read_text(encoding="utf-8"))
    if aggregate != locale_configs:
        errors.append("aggregate localization cache differs from per-language source files")

    english_cases = None
    english_meta = None
    english_titles = None
    handles = list(dict.fromkeys(item["author_handle"] for item in items))
    expected_creator_line = ", ".join(f'[{handle}](https://x.com/{handle[1:]})' for handle in handles)
    for index, filename in enumerate(FILENAMES):
        text = (ROOT / filename).read_text(encoding="utf-8")
        for marker in ("TBD", "TODO", "lorem ipsum", "<placeholder>"):
            if marker in text:
                errors.append(f"{filename}: unresolved marker {marker}")
        cases = CASE_RE.findall(text)
        meta = META_RE.findall(text)
        case_numbers = [int(row[0]) for row in cases]
        anchors = [int(value) for value in re.findall(r'^<a id="case-(\d+)"></a>$', text, re.MULTILINE)]
        if case_numbers != expected_readme_order:
            errors.append(f"{filename}: case order is {case_numbers}")
        if anchors != expected_readme_order:
            errors.append(f"{filename}: anchor order is {anchors}")
        if len(meta) != EXPECTED_CASES:
            errors.append(f"{filename}: metadata count is {len(meta)}")
        if text.count("**Prompt:**") != 1 or text.count("Voxel star wars pod-racers run") != 1:
            errors.append(f"{filename}: public prompt boundary differs")
        if R2_PREFIX not in text:
            errors.append(f"{filename}: no R2 public media URL")
        if MODEL_PAGE_PREFIX not in text:
            errors.append(f"{filename}: missing exact EvoLink Kimi K3 model page")
        if API_DOCS_PREFIX not in text:
            errors.append(f"{filename}: missing exact EvoLink Kimi K3 API docs")
        if text.count(ARTICLE_PREFIX) != 1:
            errors.append(f"{filename}: related article must appear exactly once as a jump link")
        locale = LOCALES[index]
        expected_kimik3_io = KIMIK3_IO_BY_LOCALE.get(locale, "https://kimik3.io/")
        kimik3_io_urls = re.findall(r"https://kimik3\.io/[^)\s]*", text)
        if kimik3_io_urls != [expected_kimik3_io]:
            errors.append(
                f"{filename}: KimiK3.io route is {kimik3_io_urls}, expected only {expected_kimik3_io}"
            )
        if text.count(API_ENDPOINT) != 1:
            errors.append(f"{filename}: copyable Quick API endpoint must appear exactly once")
        if text.count('"model": "kimi-k3"') != 1:
            errors.append(f"{filename}: copyable Quick API model must appear exactly once")
        if 'Authorization: Bearer $EVOLINK_API_KEY' not in text:
            errors.append(f"{filename}: Quick API example lacks environment-key Bearer authentication")
        if text.count("](#case-") != EXPECTED_CASES:
            errors.append(f"{filename}: centralized Menu does not link all {EXPECTED_CASES} cases")
        first_category = text.find('<a id="games-3d"></a>')
        menu_start = text.find("## 📑")
        if menu_start == -1 or first_category == -1 or menu_start > first_category:
            errors.append(f"{filename}: centralized Menu is not before the case sections")
        else:
            menu_text = text[menu_start:first_category]
            case_text = text[first_category:]
            if menu_text.count("](#case-") != EXPECTED_CASES:
                errors.append(f"{filename}: centralized Menu does not contain all case links")
            if "](#case-" in case_text:
                errors.append(f"{filename}: case menu tables are repeated inside category sections")
            if menu_text.count("| Case | Category | What it shows | Type |") != 1:
                errors.append(f"{filename}: centralized case menu table is missing or duplicated")
        quick_start = text.find('<a id="quick-api-access"></a>')
        related_resources = text.find('<a id="related-resources"></a>')
        acknowledge_start = text.find('<a id="acknowledge"></a>')
        if not (first_category < related_resources < quick_start < acknowledge_start):
            errors.append(f"{filename}: Quick Start is not the penultimate section after Related Resources")
        headings = re.findall(r"^## .+$", text, re.MULTILINE)
        if len(headings) < 2 or "⚡" not in headings[-2] or "🙏" not in headings[-1]:
            errors.append(f"{filename}: Quick Start and Acknowledge are not the final two sections")
        early_conversion = text[:first_category]
        for required_route in (MODEL_PAGE_PREFIX, "https://evolink.ai/dashboard/keys", API_DOCS_PREFIX):
            if required_route not in early_conversion:
                errors.append(f"{filename}: compact pre-case conversion path is missing {required_route}")
        acknowledge = text.split('<a id="acknowledge"></a>', 1)[-1]
        if re.search(r'^- \[@', acknowledge, re.MULTILINE):
            errors.append(f"{filename}: Acknowledge creators are still one-per-line bullets")
        if expected_creator_line not in acknowledge:
            errors.append(f"{filename}: Acknowledge creators are not the canonical comma-separated list")
        for item in items:
            visual_urls = [
                asset["poster_url"] if asset["kind"] == "video" else asset["url"]
                for asset in item.get("media_assets", [])
            ]
            if not visual_urls:
                errors.append(f'{filename}: case {item["public_number"]} has no rendered source media')
            for url in visual_urls:
                if text.count(f'src="{url}"') != 1:
                    errors.append(
                        f'{filename}: case {item["public_number"]} media is missing or duplicated: {url}'
                    )
        if text.count(f'src="{R2_PREFIX}media/') != 79:
            errors.append(f"{filename}: rendered case-media denominator is not exactly 79")
        if text.count("The original source permalink returned HTTP 404 during the 2026-07-17 audit") != 1:
            errors.append(f"{filename}: unavailable source disclosure must appear exactly once")
        if "https://evolink.ai/?utm_" in text:
            errors.append(f"{filename}: stale generic EvoLink CTA")
        if "https://platform.moonshot.ai/docs/guide/start-using-kimi-api" in text:
            errors.append(f"{filename}: stale primary quick-start route")
        if re.search(r'<(?:img|video)[^>]+src="[^"]+\.mp4', text):
            errors.append(f"{filename}: directly embeds video instead of poster-link policy")
        titles = [row[1] for row in cases]
        stable = [(row[0], row[2], row[3], row[4]) for row in cases]
        if index == 0:
            english_cases, english_meta, english_titles = stable, meta, titles
            if "## ⚡ Quick API Access" not in text:
                errors.append("README.md: required Quick API Access heading is missing")
            correction = "We cannot guarantee that every case is attributed to the earliest original creator. If attribution or wording needs correction, please open a correction issue with a public source"
            if f"*{correction}*" not in text:
                errors.append("README.md: correction statement is not italicized")
        else:
            if stable != english_cases:
                errors.append(f"{filename}: source, author, or numbering differs from English")
            if meta != english_meta:
                errors.append(f"{filename}: type or date differs from English")
            if any(a == b for a, b in zip(titles, english_titles or [])):
                errors.append(f"{filename}: at least one title is unchanged from English")
            correction = locale_configs[locale]["correction_text"]
            if f"*{correction}*" not in text:
                errors.append(f"{filename}: correction statement is not italicized")

    image_names = [
        "en-v2.png", "es-v2.png", "ja-v2.png", "ko-v2.png", "de-v2.png",
        "fr-v2.png", "tr-v2.png", "zh-TW-v2.png", "zh-v2.png", "ru-v2.png",
    ]
    for image in image_names:
        path = ROOT / "images" / image
        if not path.is_file() or path.stat().st_size < 50_000:
            errors.append(f"missing or undersized banner: images/{image}")

    if errors:
        return fail(errors)
    print("PASS")
    print("readmes=11")
    print(f"cases={EXPECTED_CASES}")
    print(f"localized_case_instances={EXPECTED_CASES * len(FILENAMES)}")
    print("public_prompt_cases=1")
    print("r2_policy=pass")
    print("r2_playable_video_cases=53")
    print("source_fidelity_expected_media=79")
    print("evolink_model_route=pass")
    print("evolink_api_docs_route=pass")
    print("quick_api_access=pass")
    print("quick_api_access_position=penultimate-section")
    print("evolink_article_route=pass")
    print("kimik3_io_locale_routes=pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
