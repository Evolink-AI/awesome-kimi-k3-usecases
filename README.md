<div align="center">

<a href="https://evolink.ai/kimi-k3?utm_source=github&utm_medium=banner&utm_campaign=awesome-kimi-k3-usecases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/images/en-v2.png" alt="Awesome Kimi K3 usecases banner with moon landscape and EvoLink call to action" width="760"></a>

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

All 70 cases come from the supplied high-confidence source set. Case titles link to the original posts and author handles link to creator profiles

[View Kimi K3 on EvoLink](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=introduction_cta)

## 📊 Overview

- **70 high-confidence Kimi K3 cases from public creators and practitioners**
- Covers interactive games, 3D and scientific visualization, frontend and motion design, coding workflows, research, benchmarks, and practical limits
- Each case preserves its original source, creator attribution, evidence type, date, and prompt boundary
- Medium-confidence candidates and unsupported extrapolations are excluded

> [!NOTE]
> This collection favors concrete evidence over hype. It does not reconstruct missing prompts, infer unpublished setup steps, or turn one person's observation into a general benchmark

## ⚡ Quick API Access

EvoLink publishes Kimi K3 with the model ID `kimi-k3` and an OpenAI-compatible Chat Completions API

1. [View Kimi K3 details and pricing on EvoLink](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-kimi-k3-usecases&utm_content=model_link)
2. [Create or manage an EvoLink API key](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-kimi-k3-usecases&utm_content=api_key)
3. [Run your first Kimi K3 Chat Completions call](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=first_run)

```bash
curl --request POST \
  --url "https://direct.evolink.ai/v1/chat/completions" \
  --header "Authorization: Bearer $EVOLINK_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{
    "model": "kimi-k3",
    "messages": [
      {"role": "user", "content": "Introduce Kimi K3 in three sentences."}
    ]
  }'
```

> [!IMPORTANT]
> The EvoLink model page and API documentation verify the public route and model ID. This usecase repository links to those surfaces but does not claim an independent credit-consuming API smoke test

## 📑 Menu

| Section | Cases |
|---|---|
| [🎮 Interactive Games & 3D](#games-3d) | 22 Cases |
| [🎨 Frontend & Motion Design](#frontend-motion) | 15 Cases |
| [💻 Coding & Integrations](#coding-integrations) | 8 Cases |
| [🧪 Evaluation & Limits](#evaluation-limits) | 25 Cases |
| [Acknowledge](#acknowledge) | Credits and correction policy |

<a id="games-3d"></a>
## 🎮 Interactive Games & 3D

| Case | What it shows | Type |
|---|---|---|
| [Build a Voxel Pod Racer From One Prompt](#case-1) | Use a short scene concept to prototype a playable voxel pod-racing experience, then plan a second pass for racers, a finish line, and detail review. | Demo |
| [Compare Frogger Builds With the Same Prompt](#case-2) | Hold the prompt constant when comparing two model outputs so the resulting gameplay difference is easier to inspect. | Evaluation |
| [Generate a Frogger Game and Its Recording](#case-3) | Test a one-shot game build together with a separate one-shot workflow for recording the resulting gameplay. | Demo |
| [Prototype an Aircraft Carrier in Three.js](#case-4) | Use a concrete launch-and-recovery scene to probe Kimi K3's ability to produce an interactive Three.js 3D prototype. | Demo |
| [Build a Paper Mario-Inspired Game With Agent Tools](#case-9) | Combine Kimi K3 with an agent harness and asset tools to produce both 2D and 3D game elements. | Demo |
| [Generate a Subway First-Person Shooter](#case-11) | Use a concrete subway setting to inspect a generated first-person shooter result. | Demo |
| [Model a V8 Engine With Blender MCP](#case-19) | Use Blender MCP and a single request to generate a detailed mechanical 3D model. | Integration |
| [Build a Playable Battle Arena From One Reference](#case-23) | Use a single reference to test one-shot generation of a complete playable arena. | Demo |
| [Build Three Self-Playing Retro Games as HTML Files](#case-24) | Require graphics, enemies, rules, and autonomous play inside standalone HTML game files. | Benchmark |
| [Build a One-Shot Chameleon Hide-and-Seek Game](#case-27) | Generate a single-file game with color matching, procedural areas, sound, and multi-round scoring. | Benchmark |
| [Build a 2.5D Paper Mario-Like Game With an Agent Toolchain](#case-36) | Use Kimi K3 with Grok Build or Claude Code and Spriterrific to assemble a 2.5D game workflow. | Tutorial |
| [Build a Browser-Based 3D Wuxia RPG](#case-43) | Combine melee combat, quests, inventory, weather, interiors, Blender environment work, and adapted assets. | Demo |
| [Build a Browser Multiplayer Minecraft-Like Game](#case-44) | Use a bounded time-and-cost run to produce a playable online multiplayer browser game. | Demo |
| [Recreate a Split-Screen Cooperative Browser Game](#case-48) | Use one request to generate browser-based split-screen cooperation and real-time environment interaction. | Demo |
| [Generate a Playable Game With Command Code Design Mode](#case-49) | Use Command Code's design command for a one-shot game build and record whether the result is playable. | Demo |
| [Assemble a Cohesive Wuxia Browser RPG](#case-51) | Integrate traversal, combat, quests, inventory, weather, exploration, and 3D environment work in one game. | Demo |
| [Build a Playable Hollow Knight Crossover](#case-54) | Use existing game assets to create a playable battle between the Knight and Kimi. | Demo |
| [Build a Fall Guys-Style 3D Browser Game in One Shot](#case-60) | Use a one-shot request to generate a playable 3D obstacle game and expose the project for inspection. | Demo |
| [Build and Self-Test an Apocalyptic Lisbon FPS](#case-61) | Use a one-prompt maximum-effort run that tests, screenshots, and iterates before delivering a playable FPS. | Demo |
| [Generate an Animal Crossing-Style Game From a Simple Request](#case-63) | Use a minimal game brief to inspect playability, gameplay loop, and parallax effects. | Demo |
| [Generate a Mario-Like Game From a One-Sentence Brief](#case-65) | Use a minimal one-shot request to inspect playability, stage design, pixel art, and parallax. | Demo |
| [Build a Working Zombie First-Person Shooter](#case-67) | Use a concrete zombie-shooter target to inspect a complete playable FPS artifact. | Demo |

<a id="case-1"></a>
### Case 1: [Build a Voxel Pod Racer From One Prompt](https://x.com/ivanfioravanti/status/2077763009657627055) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Use a short scene concept to prototype a playable voxel pod-racing experience, then plan a second pass for racers, a finish line, and detail review.**

The creator reports that Kimi K3 produced version one from a single public prompt and says version two would add more racers, a finish line, and detail review.

**Prompt:**

```text
Voxel star wars pod-racers run
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01-poster.jpg" alt="Case 1 video poster" height="360"></a>

[Play case 1 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-2"></a>
### Case 2: [Compare Frogger Builds With the Same Prompt](https://x.com/ivanfioravanti/status/2077754781964054825) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Hold the prompt constant when comparing two model outputs so the resulting gameplay difference is easier to inspect.**

The creator shares a Kimi K3 Frogger version as a same-prompt comparison between two models. The supplied source does not publish the prompt text or evaluation rubric.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02-poster.jpg" alt="Case 2 video poster" height="360"></a>

[Play case 2 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-3"></a>
### Case 3: [Generate a Frogger Game and Its Recording](https://x.com/TheAhmadOsman/status/2077776567292338285) (by [@TheAhmadOsman](https://x.com/TheAhmadOsman))

**Test a one-shot game build together with a separate one-shot workflow for recording the resulting gameplay.**

The creator reports that Kimi K3 produced the Frogger game in one shot and also produced the gameplay recording workflow in one shot. The exact prompts are not included.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03-poster.jpg" alt="Case 3 video poster" height="360"></a>

[Play case 3 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-4"></a>
### Case 4: [Prototype an Aircraft Carrier in Three.js](https://x.com/HarshithLucky3/status/2077753222018814360) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**Use a concrete launch-and-recovery scene to probe Kimi K3's ability to produce an interactive Three.js 3D prototype.**

The creator demonstrates a Three.js scene of fighter-jet launch and recovery on a Nimitz-class aircraft carrier and describes Kimi K3 as strong for 3D generation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04-poster.jpg" alt="Case 4 video poster" height="360"></a>

[Play case 4 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-9"></a>
### Case 9: [Build a Paper Mario-Inspired Game With Agent Tools](https://x.com/chongdashu/status/2077886028866531655) (by [@chongdashu](https://x.com/chongdashu))

**Combine Kimi K3 with an agent harness and asset tools to produce both 2D and 3D game elements.**

The creator reports using Kimi K3 with Grok Build, Spriterrific for 2D assets, and geometry for 3D assets in a Paper Mario-inspired game. The source demonstrates tool and skill use but does not publish an exact reusable prompt.

Type: Demo | Date: 2026-07-16

---

<a id="case-11"></a>
### Case 11: [Generate a Subway First-Person Shooter](https://x.com/bijanbowen/status/2077881805751873997) (by [@bijanbowen](https://x.com/bijanbowen))

**Use a concrete subway setting to inspect a generated first-person shooter result.**

The creator shows a subway FPS attributed to Kimi K3 and explicitly notes uncertainty about whether influencer status affected the result. No prompt or reproducible workflow is supplied.

Type: Demo | Date: 2026-07-16

---

<a id="case-19"></a>
### Case 19: [Model a V8 Engine With Blender MCP](https://x.com/aisearchio/status/2077962156147146925) (by [@aisearchio](https://x.com/aisearchio))

**Use Blender MCP and a single request to generate a detailed mechanical 3D model.**

The reviewer reports that Kimi K3 generated a complete V8 engine with Blender MCP from one prompt. The post links a fuller review but does not expose the exact prompt in the supplied record.

Type: Integration | Date: 2026-07-17

---

<a id="case-23"></a>
### Case 23: [Build a Playable Battle Arena From One Reference](https://x.com/VORTEX_Promos/status/2077879705378730074) (by [@VORTEX_Promos](https://x.com/VORTEX_Promos))

**Use a single reference to test one-shot generation of a complete playable arena.**

The creator reports that Kimi K3 produced a playable battle arena in one shot from one reference. A separate leaderboard claim appears in the post, but the concrete use case is the demonstrated arena artifact.

Type: Demo | Date: 2026-07-16

---

<a id="case-24"></a>
### Case 24: [Build Three Self-Playing Retro Games as HTML Files](https://x.com/rohanpaul_ai/status/2077889084761206860) (by [@rohanpaul_ai](https://x.com/rohanpaul_ai))

**Require graphics, enemies, rules, and autonomous play inside standalone HTML game files.**

The source reports an Atomic Chat comparison in which models built Road Fighter, Battle City, and Q*bert as self-playing HTML files. Its cost and quality comparison is reported by the publisher and not independently reproduced here.

Type: Benchmark | Date: 2026-07-16

---

<a id="case-27"></a>
### Case 27: [Build a One-Shot Chameleon Hide-and-Seek Game](https://x.com/aimlapi/status/2077898742179459274) (by [@aimlapi](https://x.com/aimlapi))

**Generate a single-file game with color matching, procedural areas, sound, and multi-round scoring.**

AIMLAPI reports a same-prompt one-shot comparison for a hide-and-seek game and lists costs of $3.11 for Kimi K3 and $12.23 for Fable 5. The feature and cost claims are provider-reported results.

Type: Benchmark | Date: 2026-07-16

---

<a id="case-36"></a>
### Case 36: [Build a 2.5D Paper Mario-Like Game With an Agent Toolchain](https://x.com/chongdashu/status/2077981621223837739) (by [@chongdashu](https://x.com/chongdashu))

**Use Kimi K3 with Grok Build or Claude Code and Spriterrific to assemble a 2.5D game workflow.**

The creator provides a full walkthrough using Grok Build and Kimi K3 and shows sprite generation with Spriterrific. The source identifies the tools but does not supply exact reusable prompts.

Type: Tutorial | Date: 2026-07-17

---

<a id="case-43"></a>
### Case 43: [Build a Browser-Based 3D Wuxia RPG](https://x.com/AngryTomtweets/status/2077868163136450619) (by [@AngryTomtweets](https://x.com/AngryTomtweets))

**Combine melee combat, quests, inventory, weather, interiors, Blender environment work, and adapted assets.**

The source reports a Kimi K3 browser RPG with melee combat, quests, inventory, dynamic weather, and explorable interiors, plus Blender modeling, collision improvements, PBR retexturing, and adapted open assets.

Type: Demo | Date: 2026-07-16

---

<a id="case-44"></a>
### Case 44: [Build a Browser Multiplayer Minecraft-Like Game](https://x.com/Alezander907/status/2077926014710407407) (by [@Alezander907](https://x.com/Alezander907))

**Use a bounded time-and-cost run to produce a playable online multiplayer browser game.**

The creator reports that Kimi K3 built a browser-playable multiplayer Minecraft-like game in one hour at a cost of $6.57. These are self-reported run figures from one artifact.

Type: Demo | Date: 2026-07-17

---

<a id="case-48"></a>
### Case 48: [Recreate a Split-Screen Cooperative Browser Game](https://x.com/ridark_eth/status/2077882889803378969) (by [@ridark_eth](https://x.com/ridark_eth))

**Use one request to generate browser-based split-screen cooperation and real-time environment interaction.**

The creator reports that Kimi K3 produced an It Takes Two-inspired browser game in one prompt, with Mario and Luigi interacting in split-screen and with the environment in real time.

Type: Demo | Date: 2026-07-16

---

<a id="case-49"></a>
### Case 49: [Generate a Playable Game With Command Code Design Mode](https://x.com/naymur_dev/status/2077873562661335207) (by [@naymur_dev](https://x.com/naymur_dev))

**Use Command Code's design command for a one-shot game build and record whether the result is playable.**

The creator reports a one-shot comparison using Command Code design mode and says the Kimi K3 run produced a playable game for $0.038. This cost and quality result is self-reported.

Type: Demo | Date: 2026-07-16

---

<a id="case-51"></a>
### Case 51: [Assemble a Cohesive Wuxia Browser RPG](https://x.com/TokenGremlin/status/2077855657068310620) (by [@TokenGremlin](https://x.com/TokenGremlin))

**Integrate traversal, combat, quests, inventory, weather, exploration, and 3D environment work in one game.**

The source reports a Kimi K3 wuxia-style browser RPG that combines melee combat, quests, inventory, dynamic weather, explorable interiors, and a cohesive 3D gameplay structure.

Type: Demo | Date: 2026-07-16

---

<a id="case-54"></a>
### Case 54: [Build a Playable Hollow Knight Crossover](https://x.com/wangfeng0315/status/2077933531200991583) (by [@wangfeng0315](https://x.com/wangfeng0315))

**Use existing game assets to create a playable battle between the Knight and Kimi.**

The creator, who states they work at Kimi, reports building a game from Hollow Knight assets in which the Knight battles Kimi and provides a public play link. Attribution and evaluation should account for that affiliation.

Type: Demo | Date: 2026-07-17

---

<a id="case-60"></a>
### Case 60: [Build a Fall Guys-Style 3D Browser Game in One Shot](https://x.com/aayushman2703/status/2077857886441783526) (by [@aayushman2703](https://x.com/aayushman2703))

**Use a one-shot request to generate a playable 3D obstacle game and expose the project for inspection.**

The creator reports a one-shot Kimi K3 build of a Fall Guys-style browser game and says the prompt and GitHub project are linked from the source. This record does not reproduce that prompt.

Type: Demo | Date: 2026-07-16

---

<a id="case-61"></a>
### Case 61: [Build and Self-Test an Apocalyptic Lisbon FPS](https://x.com/goncalo_canhoto/status/2077863166655037668) (by [@goncalo_canhoto](https://x.com/goncalo_canhoto))

**Use a one-prompt maximum-effort run that tests, screenshots, and iterates before delivering a playable FPS.**

The creator reports that Kimi K3 produced a playable Apocalyptic Lisbon browser FPS after about one hour, with repeated tests, screenshots, and iterations. These timing and process details are self-reported.

Type: Demo | Date: 2026-07-16

---

<a id="case-63"></a>
### Case 63: [Generate an Animal Crossing-Style Game From a Simple Request](https://x.com/gagarot200/status/2077949230287896830) (by [@gagarot200](https://x.com/gagarot200))

**Use a minimal game brief to inspect playability, gameplay loop, and parallax effects.**

The creator reports that Kimi K3 generated a fully playable Animal Crossing-style game with a gameplay loop and parallax effects from a very simple prompt. The exact wording is not present in the supplied record.

Type: Demo | Date: 2026-07-17

---

<a id="case-65"></a>
### Case 65: [Generate a Mario-Like Game From a One-Sentence Brief](https://x.com/izutorishima/status/2077939370154475992) (by [@izutorishima](https://x.com/izutorishima))

**Use a minimal one-shot request to inspect playability, stage design, pixel art, and parallax.**

The creator reports that Kimi K3 produced a working Mario-like game without obvious bugs, including stage structure and parallax, from a single brief. The same report criticizes the music and graphics quality.

Type: Demo | Date: 2026-07-17

---

<a id="case-67"></a>
### Case 67: [Build a Working Zombie First-Person Shooter](https://x.com/X2worldtech/status/2077902793449296203) (by [@X2worldtech](https://x.com/X2worldtech))

**Use a concrete zombie-shooter target to inspect a complete playable FPS artifact.**

The source shows a full working zombie FPS attributed to Kimi K3. It does not provide the prompt, implementation details, or an external gameplay assessment.

> [!WARNING]
> The original source permalink returned HTTP 404 during the 2026-07-17 audit. Attribution and evidence are preserved from the supplied high-confidence source package.

Type: Demo | Date: 2026-07-16

---


<a id="frontend-motion"></a>
## 🎨 Frontend & Motion Design

| Case | What it shows | Type |
|---|---|---|
| [Create an Interactive Motion Graphic Frontend](#case-5) | Use a one-shot code-generation test to build motion graphics that remain interactive when the animation is paused. | Demo |
| [Produce a Synchronized Motion Graphic Ad](#case-6) | Evaluate a one-shot motion-graphics workflow by checking whether music, effects, and motion stay synchronized in the final ad. | Demo |
| [Create Motion Design Entirely in Code](#case-14) | Test whether a one-shot coding workflow can produce motion design without auxiliary generation tools. | Demo |
| [Research a Person and Build an Animated Personal Site](#case-15) | Give a broad personal-site brief, then inspect the model's research, planning, iteration, and browser validation. | Tutorial |
| [Generate a Black Hole Simulation](#case-17) | Use a scientific-visualization task to inspect a generated black-hole simulation. | Demo |
| [Test Complex Frontend Modeling, Particles, and Shaders](#case-22) | Use a public frontend prompt to inspect modeling precision, particle effects, and inline shader generation in one pass. | Demo |
| [Generate a Procedural Music Tool in One Attempt](#case-26) | Test one-shot generation of an interactive procedural-music generator and compare the visible result cautiously. | Demo |
| [Create a Three.js Product Page From Two Images](#case-33) | Use two reference images and an explicit Three.js requirement to generate a product presentation. | Demo |
| [Invent a Luxury Bread Cutter and Its Product Page](#case-39) | Combine product ideation, an exploded view, a demonstration, and a landing page in one design artifact. | Demo |
| [Generate a Ten-Second Recursive Pelican GIF](#case-45) | Use a fully specified looping-animation brief to inspect narrative continuity and recursion in a GIF. | Demo |
| [Generate a BMW M4 CS Side-View SVG](#case-55) | Use a specific vehicle and viewpoint to inspect vector illustration output. | Demo |
| [Recreate Gargantua Through Screenshot Feedback](#case-58) | Use repeated screenshots as observations for diagnosing and refining a scientific visualization. | Tutorial |
| [Refine a Black Hole Visualization With 62 Screenshots](#case-66) | Use a screenshot feedback loop to read, diagnose, and correct a visual simulation over many iterations. | Tutorial |
| [Create a Post-Training Marketing PDF](#case-68) | Use a named product and deliverable format to generate a marketing document. | Demo |
| [Create a User Interface From One Prompt](#case-70) | Use a single request to generate and inspect a complete UI design. | Demo |

<a id="case-5"></a>
### Case 5: [Create an Interactive Motion Graphic Frontend](https://x.com/chetaslua/status/2077749371144442022) (by [@chetaslua](https://x.com/chetaslua))

**Use a one-shot code-generation test to build motion graphics that remain interactive when the animation is paused.**

The creator reports a 42-minute, one-shot build using simple code without a harness, MCP, or skills, and demonstrates a motion graphic whose design remains interactive when paused.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05-poster.jpg" alt="Case 5 video poster" height="360"></a>

[Play case 5 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-6"></a>
### Case 6: [Produce a Synchronized Motion Graphic Ad](https://x.com/abhinavflac/status/2077760297918484667) (by [@abhinavflac](https://x.com/abhinavflac))

**Evaluate a one-shot motion-graphics workflow by checking whether music, effects, and motion stay synchronized in the final ad.**

The creator reports that a pure-prompt, one-shot Kimi K3 run produced a Spotify-themed motion graphic ad with synchronized music, effects, and motion. The exact prompt is not included.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06-poster.jpg" alt="Case 6 video poster" height="360"></a>

[Play case 6 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-14"></a>
### Case 14: [Create Motion Design Entirely in Code](https://x.com/chetaslua/status/2077952938564354503) (by [@chetaslua](https://x.com/chetaslua))

**Test whether a one-shot coding workflow can produce motion design without auxiliary generation tools.**

The creator reports a one-shot Kimi K3 motion-design result made fully in code without MCP, skills, tools, video generation, or special prompts. The exact prompt is not provided.

Type: Demo | Date: 2026-07-17

---

<a id="case-15"></a>
### Case 15: [Research a Person and Build an Animated Personal Site](https://x.com/nicky_sap/status/2077857190707429411) (by [@nicky_sap](https://x.com/nicky_sap))

**Give a broad personal-site brief, then inspect the model's research, planning, iteration, and browser validation.**

The creator reports that Kimi K3 researched Nick Saponaro and produced an animated personal website from a broad request, including planning, testing, iteration, and browser checks. The result is a self-reported workflow demonstration.

Type: Tutorial | Date: 2026-07-16

---

<a id="case-17"></a>
### Case 17: [Generate a Black Hole Simulation](https://x.com/chetaslua/status/2077961850352971796) (by [@chetaslua](https://x.com/chetaslua))

**Use a scientific-visualization task to inspect a generated black-hole simulation.**

The creator shows a black-hole simulation attributed to Kimi K3 and calls it the best they have seen. The source provides a visible result but no prompt, rubric, or independent validation.

Type: Demo | Date: 2026-07-17

---

<a id="case-22"></a>
### Case 22: [Test Complex Frontend Modeling, Particles, and Shaders](https://x.com/karminski3/status/2077889959223337099) (by [@karminski3](https://x.com/karminski3))

**Use a public frontend prompt to inspect modeling precision, particle effects, and inline shader generation in one pass.**

The creator reports a one-pass Kimi K3 frontend result covering precise modeling, particle effects, and complex inline shader code, and states that the test prompt is public at the linked source.

Type: Demo | Date: 2026-07-16

---

<a id="case-26"></a>
### Case 26: [Generate a Procedural Music Tool in One Attempt](https://x.com/mirochill/status/2077723551331758478) (by [@mirochill](https://x.com/mirochill))

**Test one-shot generation of an interactive procedural-music generator and compare the visible result cautiously.**

The creator reports that Kimi K3 generated a procedural music tool in one attempt and compares it favorably with results from Fable 5 and GPT-5.6 Sol. This is the creator's own test set, not a standardized benchmark.

Type: Demo | Date: 2026-07-16

---

<a id="case-33"></a>
### Case 33: [Create a Three.js Product Page From Two Images](https://x.com/1littlecoder/status/2077890296806031665) (by [@1littlecoder](https://x.com/1littlecoder))

**Use two reference images and an explicit Three.js requirement to generate a product presentation.**

The creator reports that Kimi K3 designed a product page from two images and produced the explicitly requested Three.js version. No further prompt or implementation details are provided.

Type: Demo | Date: 2026-07-16

---

<a id="case-39"></a>
### Case 39: [Invent a Luxury Bread Cutter and Its Product Page](https://x.com/filicroval/status/2077871090731221438) (by [@filicroval](https://x.com/filicroval))

**Combine product ideation, an exploded view, a demonstration, and a landing page in one design artifact.**

The creator reports that Kimi K3 invented a guillotine-style bread cutter, framed it as a luxury product, and produced a landing page with an exploded view and demonstration.

Type: Demo | Date: 2026-07-16

---

<a id="case-45"></a>
### Case 45: [Generate a Ten-Second Recursive Pelican GIF](https://x.com/1littlecoder/status/2077880380900937865) (by [@1littlecoder](https://x.com/1littlecoder))

**Use a fully specified looping-animation brief to inspect narrative continuity and recursion in a GIF.**

The source includes a prompt for a looping ten-second GIF of a pelican riding a bicycle and receiving the same video by text as the camera zooms in. The creator shows Kimi K3's resulting animation.

Type: Demo | Date: 2026-07-16

---

<a id="case-55"></a>
### Case 55: [Generate a BMW M4 CS Side-View SVG](https://x.com/HarshithLucky3/status/2077765821380886942) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**Use a specific vehicle and viewpoint to inspect vector illustration output.**

The creator shows a side-view BMW M4 CS SVG attributed to Kimi K3 Max. The supplied source contains the artifact but no prompt or production steps.

Type: Demo | Date: 2026-07-16

---

<a id="case-58"></a>
### Case 58: [Recreate Gargantua Through Screenshot Feedback](https://x.com/AngryTomtweets/status/2077868981659324444) (by [@AngryTomtweets](https://x.com/AngryTomtweets))

**Use repeated screenshots as observations for diagnosing and refining a scientific visualization.**

The source reports that Kimi K3 recreated Interstellar's Gargantua through 62 self-screenshots, reading each result, diagnosing problems, and acting on them iteratively.

Type: Tutorial | Date: 2026-07-16

---

<a id="case-66"></a>
### Case 66: [Refine a Black Hole Visualization With 62 Screenshots](https://x.com/TokenGremlin/status/2077855959201042645) (by [@TokenGremlin](https://x.com/TokenGremlin))

**Use a screenshot feedback loop to read, diagnose, and correct a visual simulation over many iterations.**

The source reports that Kimi K3 reconstructed Interstellar's Gargantua by observing and refining its output across 62 screenshots. This demonstrates the reported feedback loop rather than independent physical accuracy.

Type: Tutorial | Date: 2026-07-16

---

<a id="case-68"></a>
### Case 68: [Create a Post-Training Marketing PDF](https://x.com/Satvik_Pen/status/2077859673517023313) (by [@Satvik_Pen](https://x.com/Satvik_Pen))

**Use a named product and deliverable format to generate a marketing document.**

The creator reports asking Kimi K3 for a marketing PDF about Thinking Machines' Inkling post-training and shares the result, while also praising the behind-the-scenes process. No prompt or evaluation criteria are supplied.

Type: Demo | Date: 2026-07-16

---

<a id="case-70"></a>
### Case 70: [Create a User Interface From One Prompt](https://x.com/BrianMRey/status/2077891942088671689) (by [@BrianMRey](https://x.com/BrianMRey))

**Use a single request to generate and inspect a complete UI design.**

The creator shows a UI design attributed to a one-prompt Kimi K3 run and gives a strongly positive subjective assessment. The exact prompt and rubric are not included.

Type: Demo | Date: 2026-07-16

---


<a id="coding-integrations"></a>
## 💻 Coding & Integrations

| Case | What it shows | Type |
|---|---|---|
| [Build a Virtual MacBook With Functional macOS](#case-18) | Combine Three.js hardware rendering with an interactive browser operating-system simulation. | Demo |
| [Build a GPU Compiler From DSL to PTX](#case-25) | Use an end-to-end compiler task spanning a DSL, compiler passes, PTX generation, and a Tensor Core path. | Demo |
| [Build a Real-Time Black Hole Raytracer in WebGL2](#case-32) | Test one-prompt generation of a native WebGL2 geodesic raytracer inside one HTML file. | Benchmark |
| [Build a Game Boy Advance Emulator Around mGBA WASM](#case-46) | Integrate a licensed 3D model and a real emulator core, then recursively improve interface and gameplay. | Integration |
| [Research Multiple Topics From Chinese-Language Sources](#case-50) | Use long-running research tasks to compare thoroughness and latency across model generations. | Evaluation |
| [Clone macOS in the Browser With Working Apps](#case-56) | Build a browser operating-system simulation that includes music, browser, and email applications. | Demo |
| [Build a macOS Simulation With Working FaceTime](#case-62) | Use a virtual operating-system task to test whether a generated app interaction functions. | Demo |
| [Add a Dual-Task Frontend Effect Comparator](#case-64) | Build a tool that selects two completed tasks, displays them side by side, and synchronizes views and interactions. | Tutorial |

<a id="case-18"></a>
### Case 18: [Build a Virtual MacBook With Functional macOS](https://x.com/scottstts/status/2077890054299541890) (by [@scottstts](https://x.com/scottstts))

**Combine Three.js hardware rendering with an interactive browser operating-system simulation.**

The source reports that Kimi K3 created a virtual MacBook in Three.js with a functional macOS-style environment. It demonstrates the artifact but does not supply implementation steps.

Type: Demo | Date: 2026-07-16

---

<a id="case-25"></a>
### Case 25: [Build a GPU Compiler From DSL to PTX](https://x.com/rohanpaul_ai/status/2077886618657231220) (by [@rohanpaul_ai](https://x.com/rohanpaul_ai))

**Use an end-to-end compiler task spanning a DSL, compiler passes, PTX generation, and a Tensor Core path.**

The source reports that Kimi K3 built a GPU compiler from scratch, from its DSL and passes through PTX generation, and compares its Tensor Core path with Triton. No independent benchmark details are included in the supplied record.

Type: Demo | Date: 2026-07-16

---

<a id="case-32"></a>
### Case 32: [Build a Real-Time Black Hole Raytracer in WebGL2](https://x.com/AlicanKiraz0/status/2077885419744612597) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**Test one-prompt generation of a native WebGL2 geodesic raytracer inside one HTML file.**

The author describes a coding benchmark requiring a working single-file black-hole light-bending raytracer in native WebGL2. The supplied record establishes the task and participating models but not a full independent result audit.

Type: Benchmark | Date: 2026-07-16

---

<a id="case-46"></a>
### Case 46: [Build a Game Boy Advance Emulator Around mGBA WASM](https://x.com/teortaxesTex/status/2077925090168062272) (by [@teortaxesTex](https://x.com/teortaxesTex))

**Integrate a licensed 3D model and a real emulator core, then recursively improve interface and gameplay.**

The cited Kimi K3 project adapts a licensed AGB-001 model, integrates an mGBA WASM core, and improves the interface and gameplay through recursive self-improvement. The post quotes a project description rather than an independent reproduction.

Type: Integration | Date: 2026-07-17

---

<a id="case-50"></a>
### Case 50: [Research Multiple Topics From Chinese-Language Sources](https://x.com/tphuang/status/2077911994607239400) (by [@tphuang](https://x.com/tphuang))

**Use long-running research tasks to compare thoroughness and latency across model generations.**

The author reports testing Kimi K3 on many research topics using Chinese-language sources, finding it more thorough than K2.6 but slower. The post also notes heavy service demand at the time.

Type: Evaluation | Date: 2026-07-17

---

<a id="case-56"></a>
### Case 56: [Clone macOS in the Browser With Working Apps](https://x.com/twid/status/2077924755357974989) (by [@twid](https://x.com/twid))

**Build a browser operating-system simulation that includes music, browser, and email applications.**

The source reports that Kimi K3 was used to create a browser-based macOS clone with music, browser, email, and other functions. It does not provide implementation details.

Type: Demo | Date: 2026-07-17

---

<a id="case-62"></a>
### Case 62: [Build a macOS Simulation With Working FaceTime](https://x.com/LinearUncle/status/2077919552239997078) (by [@LinearUncle](https://x.com/LinearUncle))

**Use a virtual operating-system task to test whether a generated app interaction functions.**

The creator shows a macOS-style environment attributed to Kimi K3 and reports that its FaceTime feature works. The source provides no setup or validation steps.

Type: Demo | Date: 2026-07-17

---

<a id="case-64"></a>
### Case 64: [Add a Dual-Task Frontend Effect Comparator](https://x.com/MinLiBuilds/status/2077939461510615376) (by [@MinLiBuilds](https://x.com/MinLiBuilds))

**Build a tool that selects two completed tasks, displays them side by side, and synchronizes views and interactions.**

The creator reports asking Kimi K3 to add a frontend comparison workflow with task selection, dual browser panes, object and roaming modes, synchronized viewpoints, and interaction tests. The post also notes broader model limitations.

Type: Tutorial | Date: 2026-07-17

---


<a id="evaluation-limits"></a>
## 🧪 Evaluation & Limits

| Case | What it shows | Type |
|---|---|---|
| [Compare Frontend Design on the BridgeBench Lava Lamp Task](#case-7) | Use the BridgeBench lava-lamp task as one bounded frontend-design comparison rather than a universal ranking. | Benchmark |
| [Benchmark Editorial-Voice Script Writing](#case-8) | Measure editorial-voice fit, relative ranking, and per-script cost inside a clearly identified internal benchmark. | Benchmark |
| [Compare Flappy-Game Design, Cost, and Difficulty](#case-10) | Record difficulty settings, cost, design, and gameplay features when comparing generated games. | Benchmark |
| [Compare Game Design With the Same Design Prompt](#case-12) | Hold the design prompt constant and inspect pace, design sense, and gameplay feel separately. | Benchmark |
| [Require Independent Review for Statistical Auditing](#case-13) | Pair model-generated statistical audits with independent expert or model review before relying on findings. | Limit |
| [Evaluate a Slow but Strong Frontend Run](#case-16) | Record completion time alongside output quality when testing a frontend task. | Evaluation |
| [Test Murder-Mystery Writing for Foreshadowing Failures](#case-20) | Evaluate whether a generated mystery balances clues, obscurity, and foreshadowing. | Limit |
| [Compare Millennium Falcon Modeling and Animation](#case-21) | Use matched style requests and effort settings to compare 3D modeling, animation, time, and cost. | Benchmark |
| [Review a Collection of Ten Kimi K3 Projects](#case-28) | Use a linked project roundup to discover concrete artifacts for separate verification. | Evaluation |
| [Compare an Advanced Landing Page Across Four Models](#case-29) | Hold a landing-page request constant and inspect animation depth and completion across model outputs. | Evaluation |
| [Benchmark Retro-Game Mechanics and Cost](#case-30) | Compare gameplay, physics, mechanics, autonomous behavior, token use, and cost on the same retro-game tasks. | Benchmark |
| [Compare Game Generation With Fable 5](#case-31) | Use a side-by-side generated-game example as a narrow evaluation rather than a broad model verdict. | Evaluation |
| [Compare Complex Frontend and Development Tasks With Opus 4.8](#case-34) | Use multiple complex coding tasks to identify wins and losses instead of declaring one model universally superior. | Evaluation |
| [Review Benchmarks and a Landing Page Test](#case-35) | Combine benchmark context with a concrete landing-page generation test while keeping the two evidence types separate. | Evaluation |
| [Evaluate Induction Reasoning With Graph-to-Formula Tasks](#case-37) | Measure correctness, holdout behavior, and formula complexity on first-order induction tasks. | Benchmark |
| [Review Reported Games, Landing Pages, 3D Work, and Long Context](#case-38) | Use a multi-source roundup to compare concrete artifacts and note speed limitations alongside cost claims. | Evaluation |
| [Audit a Complex Plan and Challenge Its Remedies](#case-40) | Use a second model to identify understated findings, incorrect remedies, and conclusions that should be rejected. | Evaluation |
| [Compare PPO-Style Reinforcement-Learning ASCII Diagrams](#case-41) | Hold an ASCII-diagram prompt constant and compare how models represent the reinforcement-learning loop. | Evaluation |
| [Model in Blender While Tracking Capacity Errors](#case-42) | Evaluate partial Blender progress together with service reliability rather than judging only the artifact. | Limit |
| [Compare Flappy Bird Generation in an Arena](#case-47) | Use an arena task to compare two generated Flappy Bird results while keeping the judgment task-specific. | Evaluation |
| [Solve a Bongard Visual Induction Problem With a Tool](#case-52) | Test whether tool use helps derive the visual rule in a Bongard reasoning task. | Evaluation |
| [Compare Frontend Taste and 3D Design With GPT-5.6 Sol](#case-53) | Inspect features, visual taste, elegance, and 3D execution in a bounded frontend comparison. | Evaluation |
| [Compare Website Generation Across Three Models](#case-57) | Use visible website outputs to compare Kimi K3, Fable 5, and GPT-5.6 Sol on one test. | Evaluation |
| [Compare Procedural 3D Game Generation and Cost](#case-59) | Hold a prompt constant across models and inspect generated roulette, slot-machine, and pinball systems with per-run cost. | Benchmark |
| [Compare 3D Arsenal Scene Detail and Lighting](#case-69) | Inspect object density, lighting, and scene detail in a bounded Kimi K3 versus Opus 4.8 comparison. | Evaluation |

<a id="case-7"></a>
### Case 7: [Compare Frontend Design on the BridgeBench Lava Lamp Task](https://x.com/bridgemindai/status/2077868061953007908) (by [@bridgemindai](https://x.com/bridgemindai))

**Use the BridgeBench lava-lamp task as one bounded frontend-design comparison rather than a universal ranking.**

BridgeMind AI reports that Kimi K3 outperformed Fable 5 on its BridgeBench lava-lamp task and placed first in the cited arena. These are the publisher's reported comparison results.

Type: Benchmark | Date: 2026-07-16

---

<a id="case-8"></a>
### Case 8: [Benchmark Editorial-Voice Script Writing](https://x.com/Whats_AI/status/2077860441380798908) (by [@Whats_AI](https://x.com/Whats_AI))

**Measure editorial-voice fit, relative ranking, and per-script cost inside a clearly identified internal benchmark.**

Whats_AI reports early internal results of 2,840 Elo, first place on its board, and about $0.25 per script. Treat these as one organization's preliminary benchmark, not a general performance or price guarantee.

Type: Benchmark | Date: 2026-07-16

---

<a id="case-10"></a>
### Case 10: [Compare Flappy-Game Design, Cost, and Difficulty](https://x.com/MrAhmadAwais/status/2077915347974557862) (by [@MrAhmadAwais](https://x.com/MrAhmadAwais))

**Record difficulty settings, cost, design, and gameplay features when comparing generated games.**

Command Code's internal Flappy benchmark reports different difficulty settings across models and lists Kimi K3 at $0.024, Fable 5 at $0.42, and GPT-5.6 Sol at $0.15. The unequal settings make this a bounded internal comparison.

Type: Benchmark | Date: 2026-07-17

---

<a id="case-12"></a>
### Case 12: [Compare Game Design With the Same Design Prompt](https://x.com/CommandCodeAI/status/2077921526213746948) (by [@CommandCodeAI](https://x.com/CommandCodeAI))

**Hold the design prompt constant and inspect pace, design sense, and gameplay feel separately.**

Command Code reports a same-prompt comparison of Kimi K3, GPT-5.6 Sol, and Fable 5. Its post says Kimi K3 performed well on design sense while the other two played too fast; this remains the publisher's evaluation.

Type: Benchmark | Date: 2026-07-17

---

<a id="case-13"></a>
### Case 13: [Require Independent Review for Statistical Auditing](https://x.com/emollick/status/2077869293031624793) (by [@emollick](https://x.com/emollick))

**Pair model-generated statistical audits with independent expert or model review before relying on findings.**

Ethan Mollick reports that Kimi K3 Max misapplied statistics while auditing prior academic work and agrees with a separate critique. This negative example supports independent checking rather than unreviewed acceptance.

Type: Limit | Date: 2026-07-16

---

<a id="case-16"></a>
### Case 16: [Evaluate a Slow but Strong Frontend Run](https://x.com/Lentils80/status/2077387333154857151) (by [@Lentils80](https://x.com/Lentils80))

**Record completion time alongside output quality when testing a frontend task.**

The creator reports that a Kimi K3 frontend run took 35 minutes and describes the output as one of the best seen for that prompt. Both speed and quality judgments are a single user's observation.

Type: Evaluation | Date: 2026-07-15

---

<a id="case-20"></a>
### Case 20: [Test Murder-Mystery Writing for Foreshadowing Failures](https://x.com/emollick/status/2077951790868238616) (by [@emollick](https://x.com/emollick))

**Evaluate whether a generated mystery balances clues, obscurity, and foreshadowing.**

Ethan Mollick reports that Kimi K3 did not write a good murder mystery, making clues both too obvious and too obscure and failing at foreshadowing. He also notes that other models share this limitation.

Type: Limit | Date: 2026-07-17

---

<a id="case-21"></a>
### Case 21: [Compare Millennium Falcon Modeling and Animation](https://x.com/gmi_cloud/status/2077903360263676090) (by [@gmi_cloud](https://x.com/gmi_cloud))

**Use matched style requests and effort settings to compare 3D modeling, animation, time, and cost.**

GMI Cloud reports comparing Kimi K3 and Fable 5 on pixel-style and original-style Millennium Falcon recreations at maximum effort. It says Kimi K3 took longer but cost about one-third in the first test and less than half in another; these are provider-reported results.

Type: Benchmark | Date: 2026-07-16

---

<a id="case-28"></a>
### Case 28: [Review a Collection of Ten Kimi K3 Projects](https://x.com/minchoi/status/2077957907857994006) (by [@minchoi](https://x.com/minchoi))

**Use a linked project roundup to discover concrete artifacts for separate verification.**

The author curates ten Kimi K3 examples with media, including a Game Boy Advance emulator. This record is a collection rather than a single reproducible workflow, so each linked example should be checked independently.

Type: Evaluation | Date: 2026-07-17

---

<a id="case-29"></a>
### Case 29: [Compare an Advanced Landing Page Across Four Models](https://x.com/doutorcaleb/status/2077904020471947773) (by [@doutorcaleb](https://x.com/doutorcaleb))

**Hold a landing-page request constant and inspect animation depth and completion across model outputs.**

The creator reports giving the same advanced landing-page prompt to Kimi K3, Fable, Grok, and GPT Terra, and judges Kimi K3 the strongest result. This is a self-reported comparison from one task.

Type: Evaluation | Date: 2026-07-16

---

<a id="case-30"></a>
### Case 30: [Benchmark Retro-Game Mechanics and Cost](https://x.com/adxtyahq/status/2077860500462055570) (by [@adxtyahq](https://x.com/adxtyahq))

**Compare gameplay, physics, mechanics, autonomous behavior, token use, and cost on the same retro-game tasks.**

The source reports same-prompt tests for Road Fighter, Battle City, and Q*bert and lists $0.28 for Kimi K3, $0.28 for GPT-5.6, and $0.54 for Opus 4.8. These are the publisher's benchmark figures.

Type: Benchmark | Date: 2026-07-16

---

<a id="case-31"></a>
### Case 31: [Compare Game Generation With Fable 5](https://x.com/higgsfield_ai/status/2077943629633712490) (by [@higgsfield_ai](https://x.com/higgsfield_ai))

**Use a side-by-side generated-game example as a narrow evaluation rather than a broad model verdict.**

Higgsfield presents a Kimi K3 versus Fable 5 game-generation comparison. The supplied record includes the comparison media but no prompt, scoring rubric, or detailed conditions.

Type: Evaluation | Date: 2026-07-17

---

<a id="case-34"></a>
### Case 34: [Compare Complex Frontend and Development Tasks With Opus 4.8](https://x.com/op7418/status/2077969583018066116) (by [@op7418](https://x.com/op7418))

**Use multiple complex coding tasks to identify wins and losses instead of declaring one model universally superior.**

The reviewer reports direct Kimi K3 versus Opus 4.8 tests and judges them roughly comparable on complex frontend and development work, with mixed outcomes. This remains one reviewer's assessment.

Type: Evaluation | Date: 2026-07-17

---

<a id="case-35"></a>
### Case 35: [Review Benchmarks and a Landing Page Test](https://x.com/adamuchigabriel/status/2077880433925120471) (by [@adamuchigabriel](https://x.com/adamuchigabriel))

**Combine benchmark context with a concrete landing-page generation test while keeping the two evidence types separate.**

The video presents benchmark discussion, a landing-page test, and frontend-design observations for Kimi K3. The supplied record does not provide the full test prompt or scoring rubric.

Type: Evaluation | Date: 2026-07-16

---

<a id="case-37"></a>
### Case 37: [Evaluate Induction Reasoning With Graph-to-Formula Tasks](https://x.com/s_batzoglou/status/2077884096307454119) (by [@s_batzoglou](https://x.com/s_batzoglou))

**Measure correctness, holdout behavior, and formula complexity on first-order induction tasks.**

The author reports benchmarking Kimi K3 and other models on the ICML INDUCTION task using 6 to 10 small graphs with 8 to 10 elements each to infer a first-order formula. The post says results were updated from earlier work; no new independent reproduction is claimed here.

Type: Benchmark | Date: 2026-07-16

---

<a id="case-38"></a>
### Case 38: [Review Reported Games, Landing Pages, 3D Work, and Long Context](https://x.com/servasyy_ai/status/2077903775113834689) (by [@servasyy_ai](https://x.com/servasyy_ai))

**Use a multi-source roundup to compare concrete artifacts and note speed limitations alongside cost claims.**

The author summarizes reported Kimi K3 tests across games, landing pages, 3D generation, and long-context work, while concluding that it is worth trying but not yet a replacement for Fable 5. All figures are secondary reports within this roundup.

Type: Evaluation | Date: 2026-07-16

---

<a id="case-40"></a>
### Case 40: [Audit a Complex Plan and Challenge Its Remedies](https://x.com/doodlestein/status/2077901883637665958) (by [@doodlestein](https://x.com/doodlestein))

**Use a second model to identify understated findings, incorrect remedies, and conclusions that should be rejected.**

The creator reports that Kimi K3 reviewed a heavily refined plan and found that severe issues were understated, about one-third of proposed remedies needed correction, and one finding was refuted. These are results from that specific audit.

Type: Evaluation | Date: 2026-07-16

---

<a id="case-41"></a>
### Case 41: [Compare PPO-Style Reinforcement-Learning ASCII Diagrams](https://x.com/dejavucoder/status/2077872015856615541) (by [@dejavucoder](https://x.com/dejavucoder))

**Hold an ASCII-diagram prompt constant and compare how models represent the reinforcement-learning loop.**

The source supplies the prompt to draw a PPO-style reinforcement-learning loop in ASCII and shows Kimi K3 Max beside Fable 5 High. The judgment remains a visual comparison from one task.

Type: Evaluation | Date: 2026-07-16

---

<a id="case-42"></a>
### Case 42: [Model in Blender While Tracking Capacity Errors](https://x.com/Angaisb_/status/2077910845523214668) (by [@Angaisb_](https://x.com/Angaisb_))

**Evaluate partial Blender progress together with service reliability rather than judging only the artifact.**

The creator shows Blender modeling progress from Kimi K3 and also reports repeated capacity errors. The work is incomplete in the supplied source, so the partial result and reliability limitation should be considered together.

Type: Limit | Date: 2026-07-17

---

<a id="case-47"></a>
### Case 47: [Compare Flappy Bird Generation in an Arena](https://x.com/jun_song/status/2077396996865003739) (by [@jun_song](https://x.com/jun_song))

**Use an arena task to compare two generated Flappy Bird results while keeping the judgment task-specific.**

The creator reports an Arena comparison between Kimi K3 and Opus 4.8 on a Flappy Bird task and judges Kimi K3 significantly better. No full prompt or rubric is supplied in the record.

Type: Evaluation | Date: 2026-07-15

---

<a id="case-52"></a>
### Case 52: [Solve a Bongard Visual Induction Problem With a Tool](https://x.com/IntuitMachine/status/2077885406528311561) (by [@IntuitMachine](https://x.com/IntuitMachine))

**Test whether tool use helps derive the visual rule in a Bongard reasoning task.**

The creator reports that Kimi K3 used a tool to solve a Bongard problem that Grok 4.5 and Muse Spark 1.1 did not solve in the same comparison. This is one user's task result, not a general reasoning benchmark.

Type: Evaluation | Date: 2026-07-16

---

<a id="case-53"></a>
### Case 53: [Compare Frontend Taste and 3D Design With GPT-5.6 Sol](https://x.com/filicroval/status/2077736407506751952) (by [@filicroval](https://x.com/filicroval))

**Inspect features, visual taste, elegance, and 3D execution in a bounded frontend comparison.**

The creator compares Kimi K3 and GPT-5.6 Sol on frontend design and judges Kimi K3 stronger in visual taste, elegance, and 3D capability. The assessment is subjective and task-specific.

Type: Evaluation | Date: 2026-07-16

---

<a id="case-57"></a>
### Case 57: [Compare Website Generation Across Three Models](https://x.com/pengchujin/status/2077962916226298340) (by [@pengchujin](https://x.com/pengchujin))

**Use visible website outputs to compare Kimi K3, Fable 5, and GPT-5.6 Sol on one test.**

The creator presents a website-generation comparison among Kimi K3, Fable 5, and GPT-5.6 Sol. The supplied record does not expose the complete prompt or a scoring rubric.

Type: Evaluation | Date: 2026-07-17

---

<a id="case-59"></a>
### Case 59: [Compare Procedural 3D Game Generation and Cost](https://x.com/adxtyahq/status/2077958193511362856) (by [@adxtyahq](https://x.com/adxtyahq))

**Hold a prompt constant across models and inspect generated roulette, slot-machine, and pinball systems with per-run cost.**

The publisher reports a multi-model procedural 3D game comparison and lists costs including $0.71 for Kimi K3 and $0.30 for Grok 4.5. Treat all rankings and costs as results from that publisher's run.

Type: Benchmark | Date: 2026-07-17

---

<a id="case-69"></a>
### Case 69: [Compare 3D Arsenal Scene Detail and Lighting](https://x.com/hakki_alkan/status/2077887013332636032) (by [@hakki_alkan](https://x.com/hakki_alkan))

**Inspect object density, lighting, and scene detail in a bounded Kimi K3 versus Opus 4.8 comparison.**

The source reports that Kimi K3 produced a detailed arsenal scene with stocked shelves, boxes, and realistic lighting while Opus 4.8 produced a sparse room. This is a third-party comparison report, not an independent benchmark.

Type: Evaluation | Date: 2026-07-16

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
- [@bridgemindai](https://x.com/bridgemindai)
- [@Whats_AI](https://x.com/Whats_AI)
- [@chongdashu](https://x.com/chongdashu)
- [@MrAhmadAwais](https://x.com/MrAhmadAwais)
- [@bijanbowen](https://x.com/bijanbowen)
- [@CommandCodeAI](https://x.com/CommandCodeAI)
- [@emollick](https://x.com/emollick)
- [@nicky_sap](https://x.com/nicky_sap)
- [@Lentils80](https://x.com/Lentils80)
- [@scottstts](https://x.com/scottstts)
- [@aisearchio](https://x.com/aisearchio)
- [@gmi_cloud](https://x.com/gmi_cloud)
- [@karminski3](https://x.com/karminski3)
- [@VORTEX_Promos](https://x.com/VORTEX_Promos)
- [@rohanpaul_ai](https://x.com/rohanpaul_ai)
- [@mirochill](https://x.com/mirochill)
- [@aimlapi](https://x.com/aimlapi)
- [@minchoi](https://x.com/minchoi)
- [@doutorcaleb](https://x.com/doutorcaleb)
- [@adxtyahq](https://x.com/adxtyahq)
- [@higgsfield_ai](https://x.com/higgsfield_ai)
- [@AlicanKiraz0](https://x.com/AlicanKiraz0)
- [@1littlecoder](https://x.com/1littlecoder)
- [@op7418](https://x.com/op7418)
- [@adamuchigabriel](https://x.com/adamuchigabriel)
- [@s_batzoglou](https://x.com/s_batzoglou)
- [@servasyy_ai](https://x.com/servasyy_ai)
- [@filicroval](https://x.com/filicroval)
- [@doodlestein](https://x.com/doodlestein)
- [@dejavucoder](https://x.com/dejavucoder)
- [@Angaisb_](https://x.com/Angaisb_)
- [@AngryTomtweets](https://x.com/AngryTomtweets)
- [@Alezander907](https://x.com/Alezander907)
- [@teortaxesTex](https://x.com/teortaxesTex)
- [@jun_song](https://x.com/jun_song)
- [@ridark_eth](https://x.com/ridark_eth)
- [@naymur_dev](https://x.com/naymur_dev)
- [@tphuang](https://x.com/tphuang)
- [@TokenGremlin](https://x.com/TokenGremlin)
- [@IntuitMachine](https://x.com/IntuitMachine)
- [@wangfeng0315](https://x.com/wangfeng0315)
- [@twid](https://x.com/twid)
- [@pengchujin](https://x.com/pengchujin)
- [@aayushman2703](https://x.com/aayushman2703)
- [@goncalo_canhoto](https://x.com/goncalo_canhoto)
- [@LinearUncle](https://x.com/LinearUncle)
- [@gagarot200](https://x.com/gagarot200)
- [@MinLiBuilds](https://x.com/MinLiBuilds)
- [@izutorishima](https://x.com/izutorishima)
- [@X2worldtech](https://x.com/X2worldtech)
- [@Satvik_Pen](https://x.com/Satvik_Pen)
- [@hakki_alkan](https://x.com/hakki_alkan)
- [@BrianMRey](https://x.com/BrianMRey)

*We cannot guarantee that every case is attributed to the earliest original creator. If attribution or wording needs correction, please open a correction issue with a public source*

To propose another source-backed Kimi K3 case, open an issue or pull request and follow the contribution checklist
