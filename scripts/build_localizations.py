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


def render_english(items: list[dict]) -> str:
    categories = ["games-3d", "frontend-motion", "coding-integrations", "evaluation-limits"]
    handles = list(dict.fromkeys(item["author_handle"] for item in items))
    lines = [
        '<div align="center">',
        "",
        f'<a href="{MODEL_PAGE}?utm_source=github&utm_medium=banner&utm_campaign=awesome-kimi-k3-usecases&utm_content=readme_banner"><img src="{R2}/images/en-v2.png" alt="Awesome Kimi K3 usecases banner with moon landscape and EvoLink call to action" width="760"></a>',
        "",
        "[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)",
        f"[![Kimi K3 on EvoLink](https://img.shields.io/badge/Kimi_K3-Available_on_EvoLink-111111)]({MODEL_PAGE}?utm_source=github&utm_medium=badge&utm_campaign=awesome-kimi-k3-usecases&utm_content=top_badge)",
        f"[![API Quick Start](https://img.shields.io/badge/Kimi_K3-API_Quick_Start-22c55e)]({API_DOCS}?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=first_run)",
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
        "All 70 cases come from the supplied high-confidence source set. Case titles link to the original posts and author handles link to creator profiles",
        "",
        f"[View Kimi K3 on EvoLink]({EVOLINK_URL})",
        "",
        "## 📊 Overview",
        "",
        "- **70 high-confidence Kimi K3 cases from public creators and practitioners**",
        "- Covers interactive games, 3D and scientific visualization, frontend and motion design, coding workflows, research, benchmarks, and practical limits",
        "- Each case preserves its original source, creator attribution, evidence type, date, and prompt boundary",
        "- Medium-confidence candidates and unsupported extrapolations are excluded",
        "",
        "> [!NOTE]",
        "> This collection favors concrete evidence over hype. It does not reconstruct missing prompts, infer unpublished setup steps, or turn one person's observation into a general benchmark",
        "",
        "## ⚡ Quick API Access",
        "",
        "EvoLink publishes Kimi K3 with the model ID `kimi-k3` and an OpenAI-compatible Chat Completions API",
        "",
        f"1. [View Kimi K3 details and pricing on EvoLink]({MODEL_PAGE}?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-kimi-k3-usecases&utm_content=model_link)",
        "2. [Create or manage an EvoLink API key](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-kimi-k3-usecases&utm_content=api_key)",
        f"3. [Run your first Kimi K3 Chat Completions call]({API_DOCS}?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=first_run)",
        "",
        *API_EXAMPLE,
        "",
        "> [!IMPORTANT]",
        "> The EvoLink model page and API documentation verify the public route and model ID. This usecase repository links to those surfaces but does not claim an independent credit-consuming API smoke test",
        "",
        "## 📑 Menu",
        "",
        "| Section | Cases |",
        "|---|---|",
    ]
    for key in categories:
        count = sum(1 for item in items if item["category_key"] == key)
        lines.append(f'| [{CATEGORY_EMOJI[key]} {CATEGORY_ENGLISH[key]}](#{key}) | {count} Cases |')
    lines.append("| [Acknowledge](#acknowledge) | Credits and correction policy |")

    for key in categories:
        category_items = [item for item in items if item["category_key"] == key]
        lines.extend([
            "",
            f'<a id="{key}"></a>',
            f'## {CATEGORY_EMOJI[key]} {CATEGORY_ENGLISH[key]}',
            "",
            "| Case | What it shows | Type |",
            "|---|---|---|",
        ])
        for item in category_items:
            lines.append(f'| [{item["title"]}](#case-{item["public_number"]}) | {item["takeaway"]} | {item["type"]} |')
        lines.append("")
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
        "## Related Resources",
        "",
        f"- [Kimi K3 model details and pricing on EvoLink]({MODEL_PAGE}?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_model) — availability, model ID, context, and pricing",
        f"- [Kimi K3 OpenAI-compatible API documentation]({API_DOCS}?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_api_docs) — Chat Completions endpoint and request format",
        f"- [Learn more about Kimi K3 on EvoLink]({ARTICLE_URL}?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_article)",
        "- No installable EvoLink Kimi K3 skill was independently verified for this update",
        "",
        '<a id="acknowledge"></a>',
        "## 🙏 Acknowledge",
        "",
        "This repository is possible because creators and practitioners shared Kimi K3 work publicly",
        "",
        "Thanks to the source creators represented here:",
        "",
        *[f'- [{handle}](https://x.com/{handle[1:]})' for handle in handles],
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
        *API_EXAMPLE,
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
        lines.extend([
            "",
            f'<a id="{key}"></a>',
            f'## {CATEGORY_EMOJI[key]} {config["categories"][key]}',
            "",
            "| Case | What it shows | Type |",
            "|---|---|---|",
        ])
        for item in category_items:
            translated = config["cases"][str(item["public_number"])]
            lines.append(
                f'| [{translated["title"]}](#case-{item["public_number"]}) | '
                f'{translated["takeaway"]} | {item["type"]} |'
            )
        lines.append("")
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
        *[f'- [{handle}](https://x.com/{handle[1:]})' for handle in handles],
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
