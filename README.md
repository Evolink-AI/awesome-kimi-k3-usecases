<div align="center">

<a href="https://evolink.ai/kimi-k3?utm_source=github&utm_medium=banner&utm_campaign=awesome-kimi-k3-usecases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/images/en.png" alt="Kimi K3 practical usecase repository banner" width="760"></a>

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)
[![Kimi K3 on EvoLink](https://img.shields.io/badge/Kimi_K3-Available_on_EvoLink-111111)](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=badge&utm_campaign=awesome-kimi-k3-usecases&utm_content=top_badge)
[![API Quick Start](https://img.shields.io/badge/Kimi_K3-API_Quick_Start-22c55e)](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=first_run)

[![🇺🇸 English](https://img.shields.io/badge/🇺🇸_English-Default_Source-111111)](README.md)
[![🇪🇸 Español](https://img.shields.io/badge/🇪🇸_Español-Ver-ffb703)](README_es.md)
[![🇵🇹 Português](https://img.shields.io/badge/🇵🇹_Português-Ver-2a9d8f)](README_pt.md)
[![🇯🇵 日本語](https://img.shields.io/badge/🇯🇵_日本語-表示-52b788)](README_ja.md)
[![🇰🇷 한국어](https://img.shields.io/badge/🇰🇷_한국어-보기-4ea8de)](README_ko.md)
[![🇩🇪 Deutsch](https://img.shields.io/badge/🇩🇪_Deutsch-Ansehen-f4a261)](README_de.md)
[![🇫🇷 Français](https://img.shields.io/badge/🇫🇷_Français-Voir-e76f51)](README_fr.md)
[![🇹🇷 Türkçe](https://img.shields.io/badge/🇹🇷_Türkçe-Görüntüle-d62828)](README_tr.md)
[![🇹🇼 繁體中文](https://img.shields.io/badge/🇹🇼_繁體中文-查看-8338ec)](README_zh-TW.md)
[![🇨🇳 简体中文](https://img.shields.io/badge/🇨🇳_简体中文-查看-ef476f)](README_zh-CN.md)
[![🇷🇺 Русский](https://img.shields.io/badge/🇷🇺_Русский-Смотреть-577590)](README_ru.md)

</div>

# Awesome Kimi K3 Use Cases

## 🍌 Introduction

Welcome to the Kimi K3 high-signal usecase repository

**We collect source-backed Kimi K3 games, 3D builds, motion designs, integrations, evaluations, and practical limits from public creator evidence**

Every case in this first edition comes from the supplied Kimi K3 source package. Case titles link to the original posts and author handles link to creator profiles

[View Kimi K3 on EvoLink](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=introduction_cta)

## 📊 Overview

- **10 selected Kimi K3 cases from public creators and practitioners**
- Covers interactive games, Three.js scenes, motion graphics, CLI access, serving observations, vision quality, and agent-loop limits
- Each case includes an original source, creator attribution, reader-action takeaway, evidence type, date, and prompt boundary
- Claims from individual posts remain labeled as creator reports or single observations

> [!NOTE]
> This collection favors concrete evidence over hype. It does not reconstruct missing prompts, infer unpublished setup steps, or turn one person's observation into a benchmark

## ⚡ Quick Start

EvoLink publishes Kimi K3 with the model ID `kimi-k3` and an OpenAI-compatible Chat Completions API

1. [View Kimi K3 details and pricing on EvoLink](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-kimi-k3-usecases&utm_content=model_link)
2. [Create or manage an EvoLink API key](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-kimi-k3-usecases&utm_content=api_key)
3. [Run your first Kimi K3 Chat Completions call](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=first_run)

> [!IMPORTANT]
> The EvoLink model page and API documentation verify the public route and model ID. This usecase repository links to those surfaces but does not claim an independent credit-consuming API smoke test

## 📑 Menu

| Section | Cases |
|---|---|
| [🎮 Interactive Games & 3D](#games-3d) | 4 Cases |
| [🎨 Frontend & Motion Design](#frontend-motion) | 2 Cases |
| [💻 Coding & Integrations](#coding-integrations) | 2 Cases |
| [🧪 Evaluation & Limits](#evaluation-limits) | 2 Cases |
| [Acknowledge](#acknowledge) | Credits and correction policy |

<a id="games-3d"></a>
## 🎮 Interactive Games & 3D

| Case | What it shows | Type |
|---|---|---|
| [Build a Voxel Pod Racer From One Prompt](#case-1) | Prototype a playable voxel racing scene from a short public prompt, then define the next iteration | Demo |
| [Compare Frogger Builds With the Same Prompt](#case-2) | Hold the prompt constant to inspect output differences without inventing the missing prompt | Evaluation |
| [Generate a Frogger Game and Its Recording](#case-3) | Test one-shot generation for both a game and its gameplay-recording workflow | Demo |
| [Prototype an Aircraft Carrier in Three.js](#case-4) | Probe 3D generation with a concrete launch-and-recovery scene | Demo |

<a id="case-1"></a>
### Case 1: [Build a Voxel Pod Racer From One Prompt](https://x.com/ivanfioravanti/status/2077763009657627055) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Use a short scene concept to prototype a playable voxel pod-racing experience, then plan a second pass for racers, a finish line, and detail review**

The creator reports that Kimi K3 produced version one from a single public prompt and says version two would add more racers, a finish line, and detail review

**Prompt:**

```text
Voxel star wars pod-racers run
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01-poster.jpg" alt="Case 1 voxel pod racer video poster" height="360"></a>

[Play case 1 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-2"></a>
### Case 2: [Compare Frogger Builds With the Same Prompt](https://x.com/ivanfioravanti/status/2077754781964054825) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Hold the prompt constant when comparing two model outputs so the resulting gameplay difference is easier to inspect**

The creator shares a Kimi K3 Frogger version as a same-prompt comparison between two models. The supplied source does not publish the prompt text or evaluation rubric

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02-poster.jpg" alt="Case 2 Frogger comparison video poster" height="360"></a>

[Play case 2 comparison video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-3"></a>
### Case 3: [Generate a Frogger Game and Its Recording](https://x.com/TheAhmadOsman/status/2077776567292338285) (by [@TheAhmadOsman](https://x.com/TheAhmadOsman))

**Test a one-shot game build together with a separate one-shot workflow for recording the resulting gameplay**

The creator reports that Kimi K3 produced the Frogger game in one shot and also produced the gameplay recording workflow in one shot. The exact prompts are not included

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03-poster.jpg" alt="Case 3 Frogger gameplay video poster" height="360"></a>

[Play case 3 gameplay video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-4"></a>
### Case 4: [Prototype an Aircraft Carrier in Three.js](https://x.com/HarshithLucky3/status/2077753222018814360) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**Use a concrete launch-and-recovery scene to probe Kimi K3's ability to produce an interactive Three.js 3D prototype**

The creator demonstrates a Three.js scene of fighter-jet launch and recovery on a Nimitz-class aircraft carrier and describes Kimi K3 as strong for 3D generation

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04-poster.jpg" alt="Case 4 Three.js aircraft carrier video poster" height="360"></a>

[Play case 4 Three.js demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="frontend-motion"></a>
## 🎨 Frontend & Motion Design

| Case | What it shows | Type |
|---|---|---|
| [Create an Interactive Motion Graphic Frontend](#case-5) | Build motion graphics that remain interactive when paused | Demo |
| [Produce a Synchronized Motion Graphic Ad](#case-6) | Check music, effects, and motion synchronization in a one-shot ad workflow | Demo |

<a id="case-5"></a>
### Case 5: [Create an Interactive Motion Graphic Frontend](https://x.com/chetaslua/status/2077749371144442022) (by [@chetaslua](https://x.com/chetaslua))

**Use a one-shot code-generation test to build motion graphics that remain interactive when the animation is paused**

The creator reports a 42-minute, one-shot build using simple code without a harness, MCP, or skills, and demonstrates a motion graphic whose design remains interactive when paused

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05-poster.jpg" alt="Case 5 interactive motion graphic video poster" height="360"></a>

[Play case 5 motion graphic video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-6"></a>
### Case 6: [Produce a Synchronized Motion Graphic Ad](https://x.com/abhinavflac/status/2077760297918484667) (by [@abhinavflac](https://x.com/abhinavflac))

**Evaluate a one-shot motion-graphics workflow by checking whether music, effects, and motion stay synchronized in the final ad**

The creator reports that a pure-prompt, one-shot Kimi K3 run produced a Spotify-themed motion graphic ad with synchronized music, effects, and motion. The exact prompt is not included

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06-poster.jpg" alt="Case 6 synchronized motion graphic ad video poster" height="360"></a>

[Play case 6 motion graphic ad](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="coding-integrations"></a>
## 💻 Coding & Integrations

| Case | What it shows | Type |
|---|---|---|
| [Access Kimi K3 Through Kimi CLI](#case-7) | Use Kimi CLI as one announced Kimi K3 interface without inferring missing setup steps | Integration |
| [Observe OpenRouter Throughput via Moonshot API](#case-8) | Record provider route and tokens per second while preserving the single-observation boundary | Evaluation |

<a id="case-7"></a>
### Case 7: [Access Kimi K3 Through Kimi CLI](https://x.com/TheAhmadOsman/status/2077750074608644127) (by [@TheAhmadOsman](https://x.com/TheAhmadOsman))

**Use the official Kimi CLI as one available interface for Kimi K3 after checking the current CLI documentation and model selector**

The creator announces Kimi K3 availability in Kimi CLI and shares a screenshot. This repository does not infer installation or authentication steps from the announcement

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-07.jpg" alt="Case 7 Kimi CLI source screenshot" height="360">

Type: Integration | Date: 2026-07-16

---

<a id="case-8"></a>
### Case 8: [Observe OpenRouter Throughput via Moonshot API](https://x.com/scaling01/status/2077777932341092422) (by [@scaling01](https://x.com/scaling01))

**Record provider, route, and observed tokens per second when comparing Kimi K3 serving performance**

One user reports Kimi K3 running on OpenRouter at 28 tokens per second through the Moonshot API. Treat this as a single observation, not a benchmark or service guarantee

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-08.jpg" alt="Case 8 Kimi K3 throughput source screenshot" height="360">

Type: Evaluation | Date: 2026-07-16

---

<a id="evaluation-limits"></a>
## 🧪 Evaluation & Limits

| Case | What it shows | Type |
|---|---|---|
| [Test Vision Quality on Your Own Workload](#case-9) | Scope a positive vision-quality report to one practitioner's workload | Evaluation |
| [Watch for Looping at Maximum Effort](#case-10) | Add stopping criteria when a model-and-harness run repeatedly revisits completed work | Limit |

<a id="case-9"></a>
### Case 9: [Test Vision Quality on Your Own Workload](https://x.com/mitsuhiko/status/2077770239937282526) (by [@mitsuhiko](https://x.com/mitsuhiko))

**Evaluate Kimi K3 vision on representative tasks from your own workload instead of generalizing from one user's experience**

Armin Ronacher reports that Kimi K3's vision quality felt strong for his workloads and that he would not notice the absence of a model he considers state of the art. This is a personal workload observation, not a benchmark

Type: Evaluation | Date: 2026-07-16

---

<a id="case-10"></a>
### Case 10: [Watch for Looping at Maximum Effort](https://x.com/emollick/status/2077770187521069152) (by [@emollick](https://x.com/emollick))

**Set stopping criteria and review checkpoints when a maximum-effort agent run repeatedly revisits and tweaks completed work**

Ethan Mollick reports that a Kimi K3 model-and-harness setup repeatedly looped back over tasks to tweak and change them at maximum effort. The source does not isolate whether the behavior came from the model, harness, or their interaction

Type: Limit | Date: 2026-07-16

---

## Related Resources

- [Kimi K3 model details and pricing on EvoLink](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_model) — availability, model ID, context, and pricing
- [Kimi K3 OpenAI-compatible API documentation](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_api_docs) — Chat Completions endpoint and request format
- [Learn more about Kimi K3 on EvoLink](https://evolink.ai/blog/is-kimi-k3-available-on-evolink?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_article)
- No installable EvoLink Kimi K3 skill was independently verified for this update

<a id="acknowledge"></a>
## 🙏 Acknowledge

This repository is possible because creators and practitioners shared Kimi K3 work publicly

Thanks to the source creators represented here:

- [@ivanfioravanti](https://x.com/ivanfioravanti)
- [@TheAhmadOsman](https://x.com/TheAhmadOsman)
- [@HarshithLucky3](https://x.com/HarshithLucky3)
- [@chetaslua](https://x.com/chetaslua)
- [@abhinavflac](https://x.com/abhinavflac)
- [@scaling01](https://x.com/scaling01)
- [@mitsuhiko](https://x.com/mitsuhiko)
- [@emollick](https://x.com/emollick)

We cannot guarantee that every case is attributed to the earliest original creator. If attribution or wording needs correction, please open a correction issue with a public source

To propose another source-backed Kimi K3 case, open an issue or pull request and follow the contribution checklist
