#!/usr/bin/env python3
"""Build localized READMEs from the curated source and language-specific translations."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
R2 = "https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases"
CATEGORY_EMOJI = {"games-3d": "🎮", "frontend-motion": "🎨", "coding-integrations": "💻", "evaluation-limits": "🧪"}
CATEGORY_ENGLISH = {
    "games-3d": "Interactive Games & 3D",
    "frontend-motion": "Frontend & Motion Design",
    "coding-integrations": "Coding & Integrations",
    "evaluation-limits": "Evaluation & Limits",
}
BANNER_ALT = {
    "de": "Lokalisierter Kimi K3 Banner mit Mondlandschaft und EvoLink Handlungsaufforderung",
    "es": "Banner localizado de Kimi K3 con paisaje lunar y llamada a la acción de EvoLink",
    "fr": "Bannière Kimi K3 localisée avec paysage lunaire et appel à l’action EvoLink",
    "ja": "月面風景とEvoLinkの案内を含む日本語版Kimi K3バナー",
    "ko": "달 표면과 EvoLink 사용 안내가 포함된 한국어 Kimi K3 배너",
    "pt": "Banner em inglês de casos de uso do Kimi K3 com chamada da EvoLink",
    "ru": "Локализованный баннер Kimi K3 с лунным пейзажем и призывом EvoLink",
    "tr": "Ay manzarası ve EvoLink çağrısı içeren Türkçe Kimi K3 bannerı",
    "zh-CN": "带月面场景与 EvoLink 使用入口的简体中文 Kimi K3 banner",
    "zh-TW": "帶月面場景與 EvoLink 使用入口的繁體中文 Kimi K3 banner",
}
MODEL_PAGE = "https://evolink.ai/kimi-k3"
API_DOCS = "https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat"
ARTICLE_URL = "https://evolink.ai/blog/is-kimi-k3-available-on-evolink"
KIMIK3_IO_DEFAULT = "https://kimik3.io/"
KIMIK3_IO_BY_LOCALE = {
    "zh-CN": "https://kimik3.io/zh",
    "zh-TW": "https://kimik3.io/zh",
    "ru": "https://kimik3.io/ru/",
}
EVOLINK_URL = f"{MODEL_PAGE}?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=introduction_cta"
API_EXAMPLE = [
    "```bash",
    "curl --request POST \\",
    '  --url "https://direct.evolink.ai/v1/chat/completions" \\',
    '  --header "Authorization: Bearer $EVOLINK_API_KEY" \\',
    '  --header "Content-Type: application/json" \\',
    "  --data '{",
    '    "model": "kimi-k3",',
    '    "messages": [',
    '      {"role": "user", "content": "Introduce Kimi K3 in three sentences."}',
    "    ]",
    "  }'",
    "```",
]
BADGES = """[![🇺🇸 English](https://img.shields.io/badge/🇺🇸_English-English-111111)](README.md)
[![🇪🇸 Español](https://img.shields.io/badge/🇪🇸_Español-Español-ffb703)](README_es.md)
[![🇵🇹 Português](https://img.shields.io/badge/🇵🇹_Português-Português-2a9d8f)](README_pt.md)
[![🇯🇵 日本語](https://img.shields.io/badge/🇯🇵_日本語-日本語-52b788)](README_ja.md)
[![🇰🇷 한국어](https://img.shields.io/badge/🇰🇷_한국어-한국어-4ea8de)](README_ko.md)
[![🇩🇪 Deutsch](https://img.shields.io/badge/🇩🇪_Deutsch-Deutsch-f4a261)](README_de.md)
[![🇫🇷 Français](https://img.shields.io/badge/🇫🇷_Français-Français-e76f51)](README_fr.md)
[![🇹🇷 Türkçe](https://img.shields.io/badge/🇹🇷_Türkçe-Türkçe-d62828)](README_tr.md)
[![🇹🇼 繁體中文](https://img.shields.io/badge/🇹🇼_繁體中文-繁體中文-8338ec)](README_zh-TW.md)
[![🇨🇳 简体中文](https://img.shields.io/badge/🇨🇳_简体中文-简体中文-ef476f)](README_zh-CN.md)
[![🇷🇺 Русский](https://img.shields.io/badge/🇷🇺_Русский-Русский-577590)](README_ru.md)"""


def media_block(item: dict) -> str:
    number = item["public_number"]
    blocks: list[str] = []
    image_number = 0
    for asset in item.get("media_assets", []):
        if asset["kind"] == "video":
            blocks.extend([
                f'<a href="{asset["url"]}"><img src="{asset["poster_url"]}" '
                f'alt="Case {number} source video poster" height="360"></a>',
                f'[{asset["play_label"]}]({asset["url"]})',
            ])
        elif asset["kind"] == "image":
            image_number += 1
            blocks.append(
                f'<a href="{asset["url"]}"><img src="{asset["url"]}" '
                f'alt="Case {number} source image {image_number}" height="360"></a>'
            )
    return "\n\n".join(blocks)


def append_case_menu(lines: list[str], items: list[dict], category_names: dict[str, str], translations: dict | None = None) -> None:
    lines.extend([
        "",
        "| Case | Category | What it shows | Type |",
        "|---|---|---|---|",
    ])
    for item in items:
        content = translations[str(item["public_number"])] if translations else item
        lines.append(
            f'| [{content["title"]}](#case-{item["public_number"]}) | '
            f'{category_names[item["category_key"]]} | {content["takeaway"]} | {item["type"]} |'
        )


def english_quickstart_block() -> list[str]:
    return [
        '<a id="quick-api-access"></a>',
        "## ⚡ Quick API Access",
        "",
        "EvoLink publishes Kimi K3 with the model ID `kimi-k3` and an OpenAI-compatible Chat Completions API",
        "",
        f"1. [View Kimi K3 details and pricing on EvoLink]({MODEL_PAGE}?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=landing_overview)",
        "2. [Create or manage an EvoLink API key](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-kimi-k3-usecases&utm_content=api_key)",
        "",
        *API_EXAMPLE,
        "",
        "Endpoint: `POST https://direct.evolink.ai/v1/chat/completions`",
        "",
        f"[Read the Kimi K3 API documentation]({API_DOCS}?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=first_run)",
        "",
        "> [!IMPORTANT]",
        "> The EvoLink model page and API documentation verify the public route and model ID. This usecase repository links to those surfaces but does not claim an independent credit-consuming API smoke test",
        "",
    ]


def localized_quickstart_block(config: dict) -> list[str]:
    return [
        '<a id="quick-api-access"></a>',
        f'## ⚡ {config["quickstart_heading"]}',
        "",
        config["quickstart_intro"],
        "",
        f'1. [{config["explore_evolink"]}]({MODEL_PAGE}?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=landing_overview)',
        f'2. [{config["manage_key"]}](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-kimi-k3-usecases&utm_content=api_key)',
        "",
        *API_EXAMPLE,
        "",
        "Endpoint: `POST https://direct.evolink.ai/v1/chat/completions`",
        "",
        f'[{config["official_quickstart"]}]({API_DOCS}?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=first_run)',
        "",
        "> [!IMPORTANT]",
        f'> {config["important"]}',
        "",
    ]


def render_english(items: list[dict]) -> str:
    categories = ["games-3d", "frontend-motion", "coding-integrations", "evaluation-limits"]
    case_count = len(items)
    handles = list(dict.fromkeys(item["author_handle"] for item in items))
    lines = [
        '<div align="center">',
        "",
        f'<a href="{MODEL_PAGE}?utm_source=github&utm_medium=banner&utm_campaign=awesome-kimi-k3-usecases&utm_content=readme_banner"><img src="{R2}/images/en-v2.png" alt="Awesome Kimi K3 usecases banner with moon landscape and EvoLink call to action" width="760"></a>',
        "",
        "[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)",
        f"[![API Quick Start](https://img.shields.io/badge/Kimi_K3-API_Quick_Start-22c55e)]({API_DOCS}?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=docs_link)",
        "",
        BADGES,
        "",
        "</div>",
        "",
        "# Awesome Kimi K3 Use Cases",
        "",
        "## 🍌 Introduction",
        "",
        "Welcome to the Kimi K3 high-signal usecase repository",
        "",
        "**We collect source-backed Kimi K3 games, 3D builds, motion designs, integrations, evaluations, and practical limits from public creator evidence**",
        "",
        f"All {case_count} cases come from high-confidence public sources. Case titles link to the original posts and author handles link to creator profiles",
        "",
        "## 📊 Overview",
        "",
        f"- **{case_count} high-confidence Kimi K3 cases from public creators and practitioners**",
        "- Covers interactive games, 3D and scientific visualization, frontend and motion design, coding workflows, research, benchmarks, and practical limits",
        "- Each case preserves its original source, creator attribution, evidence type, date, and prompt boundary",
        "- Medium-confidence candidates and unsupported extrapolations are excluded",
        "",
        "> [!NOTE]",
        "> This collection favors concrete evidence over hype. It does not reconstruct missing prompts, infer unpublished setup steps, or turn one person's observation into a general benchmark",
        "",
        *english_quickstart_block(),
        "## 📑 Menu",
        "",
        "| Section | Cases |",
        "|---|---|",
    ]
    for key in categories:
        count = sum(1 for item in items if item["category_key"] == key)
        lines.append(f'| [{CATEGORY_EMOJI[key]} {CATEGORY_ENGLISH[key]}](#{key}) | {count} Cases |')
    lines.append("| [Related Resources](#related-resources) | Model and ecosystem links |")
    lines.append("| [Quick API Access](#quick-api-access) | Model, API key, docs, and first call |")
    lines.append("| [Acknowledge](#acknowledge) | Credits and correction policy |")
    append_case_menu(lines, items, CATEGORY_ENGLISH)

    for key in categories:
        category_items = [item for item in items if item["category_key"] == key]
        lines.extend([
            "",
            f'<a id="{key}"></a>',
            f'## {CATEGORY_EMOJI[key]} {CATEGORY_ENGLISH[key]}',
            "",
        ])
        for item in category_items:
            lines.extend([
                f'<a id="case-{item["public_number"]}"></a>',
                f'### Case {item["public_number"]}: [{item["title"]}]({item["source_url"]}) (by [{item["author_handle"]}]({item["author_url"]}))',
                "",
                f'**{item["takeaway"]}**',
                "",
                item["body_notes"],
                "",
            ])
            if item.get("source_status_note"):
                lines.extend(["> [!WARNING]", f'> {item["source_status_note"]}', ""])
            if item["prompt_public"]:
                lines.extend(["**Prompt:**", "", "```text", item["prompt_text"], "```", ""])
            block = media_block(item)
            if block:
                lines.extend([block, ""])
            lines.extend([f'Type: {item["type"]} | Date: {item["date"]}', "", "---", ""])

    lines.extend([
        '<a id="related-resources"></a>',
        "## Related Resources",
        "",
        f"- [Kimi K3 model overview on EvoLink]({MODEL_PAGE}?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=landing_overview) — availability, model ID, context, and pricing",
        f"- [Kimi K3 OpenAI-compatible API documentation]({API_DOCS}?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=docs_link) — Chat Completions endpoint and request format",
        f"- [Learn more about Kimi K3 on EvoLink]({ARTICLE_URL}?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_article)",
        f"- [KimiK3.io]({KIMIK3_IO_DEFAULT})",
        "- No installable EvoLink Kimi K3 skill was independently verified for this update",
        "",
        '<a id="acknowledge"></a>',
        "## 🙏 Acknowledge",
        "",
        "This repository is possible because creators and practitioners shared Kimi K3 work publicly",
        "",
        "Thanks to the source creators represented here:",
        "",
        ", ".join(f'[{handle}](https://x.com/{handle[1:]})' for handle in handles),
        "",
        "*We cannot guarantee that every case is attributed to the earliest original creator. If attribution or wording needs correction, please open a correction issue with a public source*",
        "",
        "To propose another source-backed Kimi K3 case, open an issue or pull request and follow the contribution checklist",
        "",
    ])
    return "\n".join(lines)


def render(locale: str, config: dict, items: list[dict]) -> str:
    categories = ["games-3d", "frontend-motion", "coding-integrations", "evaluation-limits"]
    handles = list(dict.fromkeys(item["author_handle"] for item in items))
    lines = [
        '<div align="center">',
        "",
        f'<a href="{MODEL_PAGE}?utm_source=github&utm_medium=banner&utm_campaign=awesome-kimi-k3-usecases&utm_content=readme_banner"><img src="{R2}/images/{config["banner"]}" alt="{BANNER_ALT[locale]}" width="760"></a>',
        "",
        "[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)",
        f"[![API Quick Start](https://img.shields.io/badge/Kimi_K3-API_Quick_Start-22c55e)]({API_DOCS}?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=docs_link)",
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
        f'## 📊 {config["overview_heading"]}',
        "",
        *[f'- {entry}' for entry in config["overview"]],
        "",
        "> [!NOTE]",
        f'> {config["note"]}',
        "",
        *localized_quickstart_block(config),
        f'## 📑 {config["menu_heading"]}',
        "",
        "| Section | Cases |",
        "|---|---|",
    ]
    for key in categories:
        count = sum(1 for item in items if item["category_key"] == key)
        lines.append(f'| [{config["categories"][key]}](#{key}) | {count} |')
    lines.append(f'| [{config["resources_heading"]}](#related-resources) | {config["resources_heading"]} |')
    lines.append(f'| [{config["quickstart_heading"]}](#quick-api-access) | {config["quickstart_heading"]} |')
    lines.append(f'| [{config["ack_heading"]}](#acknowledge) | {config["credits"]} |')
    append_case_menu(lines, items, config["categories"], config["cases"])

    for key in categories:
        category_items = [item for item in items if item["category_key"] == key]
        lines.extend([
            "",
            f'<a id="{key}"></a>',
            f'## {CATEGORY_EMOJI[key]} {config["categories"][key]}',
            "",
        ])
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
            if item.get("source_status_note"):
                lines.extend(["> [!WARNING]", f'> {item["source_status_note"]}', ""])
            if item["prompt_public"]:
                lines.extend(["**Prompt:**", "", "```text", item["prompt_text"], "```", ""])
            block = media_block(item)
            if block:
                lines.extend([block, ""])
            lines.extend([f'Type: {item["type"]} | Date: {item["date"]}', "", "---", ""])

    lines.extend([
        '<a id="related-resources"></a>',
        f'## {config["resources_heading"]}',
        "",
        f'- [{config["explore_evolink"]}]({MODEL_PAGE}?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=landing_overview)',
        f'- [{config["official_quickstart"]}]({API_DOCS}?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=docs_link)',
        f'- [{config["learn_more_article"]}]({ARTICLE_URL}?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_article)',
        f'- [KimiK3.io]({KIMIK3_IO_BY_LOCALE.get(locale, KIMIK3_IO_DEFAULT)})',
        f'- {config["no_evolink_surface"]}',
        "",
        '<a id="acknowledge"></a>',
        f'## 🙏 {config["ack_heading"]}',
        "",
        config["ack_text"],
        "",
        ", ".join(f'[{handle}](https://x.com/{handle[1:]})' for handle in handles),
        "",
        f'*{config["correction_text"]}*',
        "",
    ])
    return "\n".join(lines)


def main() -> None:
    curated = json.loads((ROOT / "data/use-cases.json").read_text())
    translations = {
        path.stem: json.loads(path.read_text())
        for path in sorted((ROOT / "data/localizations").glob("*.json"))
    }
    (ROOT / "data/localization-cache.json").write_text(
        json.dumps(translations, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (ROOT / "README.md").write_text(render_english(curated["items"]), encoding="utf-8")
    print("README.md")
    for locale, config in translations.items():
        destination = ROOT / config["filename"]
        destination.write_text(render(locale, config, curated["items"]), encoding="utf-8")
        print(destination.name)


if __name__ == "__main__":
    main()
