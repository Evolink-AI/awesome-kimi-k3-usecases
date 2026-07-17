#!/usr/bin/env python3
"""Build the ten localized READMEs from the curated source and translation cache."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
R2 = "https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases"
HANDLES = ["@ivanfioravanti", "@TheAhmadOsman", "@HarshithLucky3", "@chetaslua", "@abhinavflac", "@scaling01", "@mitsuhiko", "@emollick"]
CATEGORY_EMOJI = {"games-3d": "🎮", "frontend-motion": "🎨", "coding-integrations": "💻", "evaluation-limits": "🧪"}
MODEL_PAGE = "https://evolink.ai/kimi-k3"
API_DOCS = "https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat"
ARTICLE_URL = "https://evolink.ai/blog/is-kimi-k3-available-on-evolink"
EVOLINK_URL = f"{MODEL_PAGE}?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=introduction_cta"
BADGES = """[![🇺🇸 English](https://img.shields.io/badge/🇺🇸_English-Default_Source-111111)](README.md)
[![🇪🇸 Español](https://img.shields.io/badge/🇪🇸_Español-Ver-ffb703)](README_es.md)
[![🇵🇹 Português](https://img.shields.io/badge/🇵🇹_Português-Ver-2a9d8f)](README_pt.md)
[![🇯🇵 日本語](https://img.shields.io/badge/🇯🇵_日本語-表示-52b788)](README_ja.md)
[![🇰🇷 한국어](https://img.shields.io/badge/🇰🇷_한국어-보기-4ea8de)](README_ko.md)
[![🇩🇪 Deutsch](https://img.shields.io/badge/🇩🇪_Deutsch-Ansehen-f4a261)](README_de.md)
[![🇫🇷 Français](https://img.shields.io/badge/🇫🇷_Français-Voir-e76f51)](README_fr.md)
[![🇹🇷 Türkçe](https://img.shields.io/badge/🇹🇷_Türkçe-Görüntüle-d62828)](README_tr.md)
[![🇹🇼 繁體中文](https://img.shields.io/badge/🇹🇼_繁體中文-查看-8338ec)](README_zh-TW.md)
[![🇨🇳 简体中文](https://img.shields.io/badge/🇨🇳_简体中文-查看-ef476f)](README_zh-CN.md)
[![🇷🇺 Русский](https://img.shields.io/badge/🇷🇺_Русский-Смотреть-577590)](README_ru.md)"""


def media_block(item: dict) -> str:
    number = item["public_number"]
    nn = f"{number:02d}"
    media_type = item["media_type"]
    if media_type == "video":
        return (
            f'<a href="{R2}/media/cases/case-{nn}.mp4"><img src="{R2}/media/cases/case-{nn}-poster.jpg" '
            f'alt="Case {number} video poster" height="360"></a>\n\n'
            f'[Play case {number} demo video]({R2}/media/cases/case-{nn}.mp4)'
        )
    if media_type == "image":
        return f'<img src="{R2}/media/cases/case-{nn}.jpg" alt="Case {number} source media" height="360">'
    return ""


def render(locale: str, config: dict, items: list[dict]) -> str:
    categories = ["games-3d", "frontend-motion", "coding-integrations", "evaluation-limits"]
    lines = [
        '<div align="center">',
        "",
        f'<a href="{MODEL_PAGE}?utm_source=github&utm_medium=banner&utm_campaign=awesome-kimi-k3-usecases&utm_content=readme_banner"><img src="{R2}/images/{config["banner"]}" alt="Kimi K3 usecase repository banner" width="760"></a>',
        "",
        "[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)",
        f"[![Kimi K3 on EvoLink](https://img.shields.io/badge/Kimi_K3-Available_on_EvoLink-111111)]({MODEL_PAGE}?utm_source=github&utm_medium=badge&utm_campaign=awesome-kimi-k3-usecases&utm_content=top_badge)",
        f"[![API Quick Start](https://img.shields.io/badge/Kimi_K3-API_Quick_Start-22c55e)]({API_DOCS}?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=first_run)",
        "",
        BADGES,
        "",
        "</div>",
        "",
        f'# {config["repo_title"]}',
        "",
        f'## 🍌 {config["introduction_heading"]}',
        "",
        config["intro"],
        "",
        f'**{config["mission"]}**',
        "",
        config["source_boundary"],
        "",
        f'[EvoLink]({EVOLINK_URL})',
        "",
        f'## 📊 {config["overview_heading"]}',
        "",
        *[f'- {entry}' for entry in config["overview"]],
        "",
        "> [!NOTE]",
        f'> {config["note"]}',
        "",
        f'## ⚡ {config["quickstart_heading"]}',
        "",
        config["quickstart_intro"],
        "",
        f'1. [{config["explore_evolink"]}]({MODEL_PAGE}?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-kimi-k3-usecases&utm_content=model_link)',
        f'2. [{config["manage_key"]}](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-kimi-k3-usecases&utm_content=api_key)',
        f'3. [{config["official_quickstart"]}]({API_DOCS}?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=first_run)',
        "",
        "> [!IMPORTANT]",
        f'> {config["important"]}',
        "",
        f'## 📑 {config["menu_heading"]}',
        "",
        "| Section | Cases |",
        "|---|---|",
    ]
    for key in categories:
        count = sum(1 for item in items if item["category_key"] == key)
        lines.append(f'| [{config["categories"][key]}](#{key}) | {count} |')
    lines.append(f'| [{config["ack_heading"]}](#acknowledge) | {config["credits"]} |')

    for key in categories:
        category_items = [item for item in items if item["category_key"] == key]
        lines.extend(["", f'<a id="{key}"></a>', f'## {CATEGORY_EMOJI[key]} {config["categories"][key]}', ""])
        for item in category_items:
            translated = config["cases"][str(item["public_number"])]
            lines.extend([
                f'<a id="case-{item["public_number"]}"></a>',
                f'### Case {item["public_number"]}: [{translated["title"]}]({item["source_url"]}) (by [{item["author_handle"]}]({item["author_url"]}))',
                "",
                f'**{translated["takeaway"]}**',
                "",
                translated["notes"],
                "",
            ])
            if item["prompt_public"]:
                lines.extend(["**Prompt:**", "", "```text", item["prompt_text"], "```", ""])
            block = media_block(item)
            if block:
                lines.extend([block, ""])
            lines.extend([f'Type: {item["type"]} | Date: {item["date"]}', "", "---", ""])

    lines.extend([
        f'## {config["resources_heading"]}',
        "",
        f'- [{config["explore_evolink"]}]({MODEL_PAGE}?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_model)',
        f'- [{config["official_quickstart"]}]({API_DOCS}?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_api_docs)',
        f'- [{config["learn_more_article"]}]({ARTICLE_URL}?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_article)',
        f'- {config["no_evolink_surface"]}',
        "",
        '<a id="acknowledge"></a>',
        f'## 🙏 {config["ack_heading"]}',
        "",
        config["ack_text"],
        "",
        *[f'- [{handle}](https://x.com/{handle[1:]})' for handle in HANDLES],
        "",
        config["correction_text"],
        "",
    ])
    return "\n".join(lines)


def main() -> None:
    curated = json.loads((ROOT / "data/use-cases.json").read_text())
    translations = json.loads((ROOT / "data/localization-cache.json").read_text())
    for locale, config in translations.items():
        destination = ROOT / config["filename"]
        destination.write_text(render(locale, config, curated["items"]), encoding="utf-8")
        print(destination.name)


if __name__ == "__main__":
    main()
