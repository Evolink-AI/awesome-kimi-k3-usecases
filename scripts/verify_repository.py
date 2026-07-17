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
        if text.count(API_ENDPOINT) != 1:
            errors.append(f"{filename}: copyable Quick API endpoint must appear exactly once")
        if text.count('"model": "kimi-k3"') != 1:
            errors.append(f"{filename}: copyable Quick API model must appear exactly once")
        if 'Authorization: Bearer $EVOLINK_API_KEY' not in text:
            errors.append(f"{filename}: Quick API example lacks environment-key Bearer authentication")
        if text.count("](#case-") != EXPECTED_CASES:
            errors.append(f"{filename}: category summary tables do not link all {EXPECTED_CASES} cases")
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
            locale = LOCALES[index]
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
    print("evolink_model_route=pass")
    print("evolink_api_docs_route=pass")
    print("quick_api_access=pass")
    print("evolink_article_route=pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
