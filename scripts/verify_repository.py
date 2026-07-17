#!/usr/bin/env python3
"""Verify the public Kimi K3 usecase repository contract."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
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
    ]
    errors.extend(f"missing required file: {path}" for path in required if not (ROOT / path).is_file())
    if errors:
        return fail(errors)

    data = json.loads((ROOT / "data/use-cases.json").read_text(encoding="utf-8"))
    items = data.get("items", [])
    if len(items) != 10:
        errors.append(f"structured case count is {len(items)}, expected 10")
    numbers = [item.get("public_number") for item in items]
    if numbers != list(range(1, 11)):
        errors.append(f"structured numbers are not contiguous: {numbers}")
    sources = [item.get("source_url") for item in items]
    if len(sources) != len(set(sources)):
        errors.append("structured source URLs are not unique")
    if sum(bool(item.get("prompt_public")) for item in items) != 1:
        errors.append("exactly one case must expose a public prompt")
    if items and items[0].get("prompt_text") != "Voxel star wars pod-racers run":
        errors.append("case 1 exact public prompt changed")

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
        if case_numbers != list(range(1, 11)):
            errors.append(f"{filename}: case order is {case_numbers}")
        if anchors != list(range(1, 11)):
            errors.append(f"{filename}: anchor order is {anchors}")
        if len(meta) != 10:
            errors.append(f"{filename}: metadata count is {len(meta)}")
        if text.count("**Prompt:**") != 1 or text.count("Voxel star wars pod-racers run") != 1:
            errors.append(f"{filename}: public prompt boundary differs")
        if R2_PREFIX not in text:
            errors.append(f"{filename}: no R2 public media URL")
        if MODEL_PAGE_PREFIX not in text:
            errors.append(f"{filename}: missing exact EvoLink Kimi K3 model page")
        if API_DOCS_PREFIX not in text:
            errors.append(f"{filename}: missing exact EvoLink Kimi K3 API docs")
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
        else:
            if stable != english_cases:
                errors.append(f"{filename}: source, author, or numbering differs from English")
            if meta != english_meta:
                errors.append(f"{filename}: type or date differs from English")
            if any(a == b for a, b in zip(titles, english_titles or [])):
                errors.append(f"{filename}: at least one title is unchanged from English")

    image_names = ["en.png", "es.png", "pt.png", "ja.png", "ko.png", "de.png", "fr.png", "tr.png", "zh-TW.png", "zh.png", "ru.png"]
    for image in image_names:
        path = ROOT / "images" / image
        if not path.is_file() or path.stat().st_size < 50_000:
            errors.append(f"missing or undersized banner: images/{image}")

    if errors:
        return fail(errors)
    print("PASS")
    print("readmes=11")
    print("cases=10")
    print("localized_case_instances=100")
    print("public_prompt_cases=1")
    print("r2_policy=pass")
    print("evolink_model_route=pass")
    print("evolink_api_docs_route=pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
