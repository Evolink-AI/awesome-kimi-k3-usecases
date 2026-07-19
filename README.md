<div align="center">

<a href="https://evolink.ai/kimi-k3?utm_source=github&utm_medium=banner&utm_campaign=awesome-kimi-k3-usecases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/images/en-v2.png" alt="Awesome Kimi K3 usecases banner with moon landscape and EvoLink call to action" width="760"></a>

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)
[![API Quick Start](https://img.shields.io/badge/Kimi_K3-API_Quick_Start-22c55e)](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=docs_link)

[![🇺🇸 English](https://img.shields.io/badge/🇺🇸_English-English-111111)](README.md)
[![🇪🇸 Español](https://img.shields.io/badge/🇪🇸_Español-Español-ffb703)](README_es.md)
[![🇵🇹 Português](https://img.shields.io/badge/🇵🇹_Português-Português-2a9d8f)](README_pt.md)
[![🇯🇵 日本語](https://img.shields.io/badge/🇯🇵_日本語-日本語-52b788)](README_ja.md)
[![🇰🇷 한국어](https://img.shields.io/badge/🇰🇷_한국어-한국어-4ea8de)](README_ko.md)
[![🇩🇪 Deutsch](https://img.shields.io/badge/🇩🇪_Deutsch-Deutsch-f4a261)](README_de.md)
[![🇫🇷 Français](https://img.shields.io/badge/🇫🇷_Français-Français-e76f51)](README_fr.md)
[![🇹🇷 Türkçe](https://img.shields.io/badge/🇹🇷_Türkçe-Türkçe-d62828)](README_tr.md)
[![🇹🇼 繁體中文](https://img.shields.io/badge/🇹🇼_繁體中文-繁體中文-8338ec)](README_zh-TW.md)
[![🇨🇳 简体中文](https://img.shields.io/badge/🇨🇳_简体中文-简体中文-ef476f)](README_zh-CN.md)
[![🇷🇺 Русский](https://img.shields.io/badge/🇷🇺_Русский-Русский-577590)](README_ru.md)

</div>

# Awesome Kimi K3 Use Cases

## 🍌 Introduction

Welcome to the Kimi K3 high-signal usecase repository

**We collect source-backed Kimi K3 games, 3D builds, motion designs, integrations, evaluations, and practical limits from public creator evidence**

All 89 cases come from high-confidence public sources. Case titles link to the original posts and author handles link to creator profiles

## 📊 Overview

- **89 high-confidence Kimi K3 cases from public creators and practitioners**
- Covers interactive games, 3D and scientific visualization, frontend and motion design, coding workflows, research, benchmarks, and practical limits
- Each case preserves its original source, creator attribution, evidence type, date, and prompt boundary
- Medium-confidence candidates and unsupported extrapolations are excluded

> [!NOTE]
> This collection favors concrete evidence over hype. It does not reconstruct missing prompts, infer unpublished setup steps, or turn one person's observation into a general benchmark

<a id="quick-api-access"></a>
## ⚡ Quick API Access

EvoLink publishes Kimi K3 with the model ID `kimi-k3` and an OpenAI-compatible Chat Completions API

1. [View Kimi K3 details and pricing on EvoLink](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=landing_overview)
2. [Create or manage an EvoLink API key](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-kimi-k3-usecases&utm_content=api_key)

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

Endpoint: `POST https://direct.evolink.ai/v1/chat/completions`

[Read the Kimi K3 API documentation](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=first_run)

> [!IMPORTANT]
> The EvoLink model page and API documentation verify the public route and model ID. This usecase repository links to those surfaces but does not claim an independent credit-consuming API smoke test

## 📑 Menu

| Section | Cases |
|---|---|
| [🎮 Interactive Games & 3D](#games-3d) | 28 Cases |
| [🎨 Frontend & Motion Design](#frontend-motion) | 20 Cases |
| [💻 Coding & Integrations](#coding-integrations) | 10 Cases |
| [🧪 Evaluation & Limits](#evaluation-limits) | 31 Cases |
| [Related Resources](#related-resources) | Model and ecosystem links |
| [Quick API Access](#quick-api-access) | Model, API key, docs, and first call |
| [Acknowledge](#acknowledge) | Credits and correction policy |

| Case | Category | What it shows | Type |
|---|---|---|---|
| [Build a Voxel Pod Racer From One Prompt](#case-1) | Interactive Games & 3D | Use a short scene concept to prototype a playable voxel pod-racing experience, then plan a second pass for racers, a finish line, and detail review. | Demo |
| [Compare Frogger Builds With the Same Prompt](#case-2) | Interactive Games & 3D | Hold the prompt constant when comparing two model outputs so the resulting gameplay difference is easier to inspect. | Evaluation |
| [Generate a Frogger Game and Its Recording](#case-3) | Interactive Games & 3D | Test a one-shot game build together with a separate one-shot workflow for recording the resulting gameplay. | Demo |
| [Prototype an Aircraft Carrier in Three.js](#case-4) | Interactive Games & 3D | Use a concrete launch-and-recovery scene to probe Kimi K3's ability to produce an interactive Three.js 3D prototype. | Demo |
| [Create an Interactive Motion Graphic Frontend](#case-5) | Frontend & Motion Design | Use a one-shot code-generation test to build motion graphics that remain interactive when the animation is paused. | Demo |
| [Produce a Synchronized Motion Graphic Ad](#case-6) | Frontend & Motion Design | Evaluate a one-shot motion-graphics workflow by checking whether music, effects, and motion stay synchronized in the final ad. | Demo |
| [Compare Frontend Design on the BridgeBench Lava Lamp Task](#case-7) | Evaluation & Limits | Use the BridgeBench lava-lamp task as one bounded frontend-design comparison rather than a universal ranking. | Benchmark |
| [Benchmark Editorial-Voice Script Writing](#case-8) | Evaluation & Limits | Measure editorial-voice fit, relative ranking, and per-script cost inside a clearly identified internal benchmark. | Benchmark |
| [Build a Paper Mario-Inspired Game With Agent Tools](#case-9) | Interactive Games & 3D | Combine Kimi K3 with an agent harness and asset tools to produce both 2D and 3D game elements. | Demo |
| [Compare Flappy-Game Design, Cost, and Difficulty](#case-10) | Evaluation & Limits | Record difficulty settings, cost, design, and gameplay features when comparing generated games. | Benchmark |
| [Generate a Subway First-Person Shooter](#case-11) | Interactive Games & 3D | Use a concrete subway setting to inspect a generated first-person shooter result. | Demo |
| [Compare Game Design With the Same Design Prompt](#case-12) | Evaluation & Limits | Hold the design prompt constant and inspect pace, design sense, and gameplay feel separately. | Benchmark |
| [Require Independent Review for Statistical Auditing](#case-13) | Evaluation & Limits | Pair model-generated statistical audits with independent expert or model review before relying on findings. | Limit |
| [Create Motion Design Entirely in Code](#case-14) | Frontend & Motion Design | Test whether a one-shot coding workflow can produce motion design without auxiliary generation tools. | Demo |
| [Research a Person and Build an Animated Personal Site](#case-15) | Frontend & Motion Design | Give a broad personal-site brief, then inspect the model's research, planning, iteration, and browser validation. | Tutorial |
| [Evaluate a Slow but Strong Frontend Run](#case-16) | Evaluation & Limits | Record completion time alongside output quality when testing a frontend task. | Evaluation |
| [Generate a Black Hole Simulation](#case-17) | Frontend & Motion Design | Use a scientific-visualization task to inspect a generated black-hole simulation. | Demo |
| [Build a Virtual MacBook With Functional macOS](#case-18) | Coding & Integrations | Combine Three.js hardware rendering with an interactive browser operating-system simulation. | Demo |
| [Model a V8 Engine With Blender MCP](#case-19) | Interactive Games & 3D | Use Blender MCP and a single request to generate a detailed mechanical 3D model. | Integration |
| [Test Murder-Mystery Writing for Foreshadowing Failures](#case-20) | Evaluation & Limits | Evaluate whether a generated mystery balances clues, obscurity, and foreshadowing. | Limit |
| [Compare Millennium Falcon Modeling and Animation](#case-21) | Evaluation & Limits | Use matched style requests and effort settings to compare 3D modeling, animation, time, and cost. | Benchmark |
| [Test Complex Frontend Modeling, Particles, and Shaders](#case-22) | Frontend & Motion Design | Use a public frontend prompt to inspect modeling precision, particle effects, and inline shader generation in one pass. | Demo |
| [Build a Playable Battle Arena From One Reference](#case-23) | Interactive Games & 3D | Use a single reference to test one-shot generation of a complete playable arena. | Demo |
| [Build Three Self-Playing Retro Games as HTML Files](#case-24) | Interactive Games & 3D | Require graphics, enemies, rules, and autonomous play inside standalone HTML game files. | Benchmark |
| [Build a GPU Compiler From DSL to PTX](#case-25) | Coding & Integrations | Use an end-to-end compiler task spanning a DSL, compiler passes, PTX generation, and a Tensor Core path. | Demo |
| [Generate a Procedural Music Tool in One Attempt](#case-26) | Frontend & Motion Design | Test one-shot generation of an interactive procedural-music generator and compare the visible result cautiously. | Demo |
| [Build a One-Shot Chameleon Hide-and-Seek Game](#case-27) | Interactive Games & 3D | Generate a single-file game with color matching, procedural areas, sound, and multi-round scoring. | Benchmark |
| [Review a Collection of Ten Kimi K3 Projects](#case-28) | Evaluation & Limits | Use a linked project roundup to discover concrete artifacts for separate verification. | Evaluation |
| [Compare an Advanced Landing Page Across Four Models](#case-29) | Evaluation & Limits | Hold a landing-page request constant and inspect animation depth and completion across model outputs. | Evaluation |
| [Benchmark Retro-Game Mechanics and Cost](#case-30) | Evaluation & Limits | Compare gameplay, physics, mechanics, autonomous behavior, token use, and cost on the same retro-game tasks. | Benchmark |
| [Compare Game Generation With Fable 5](#case-31) | Evaluation & Limits | Use a side-by-side generated-game example as a narrow evaluation rather than a broad model verdict. | Evaluation |
| [Build a Real-Time Black Hole Raytracer in WebGL2](#case-32) | Coding & Integrations | Test one-prompt generation of a native WebGL2 geodesic raytracer inside one HTML file. | Benchmark |
| [Create a Three.js Product Page From Two Images](#case-33) | Frontend & Motion Design | Use two reference images and an explicit Three.js requirement to generate a product presentation. | Demo |
| [Compare Complex Frontend and Development Tasks With Opus 4.8](#case-34) | Evaluation & Limits | Use multiple complex coding tasks to identify wins and losses instead of declaring one model universally superior. | Evaluation |
| [Review Benchmarks and a Landing Page Test](#case-35) | Evaluation & Limits | Combine benchmark context with a concrete landing-page generation test while keeping the two evidence types separate. | Evaluation |
| [Build a 2.5D Paper Mario-Like Game With an Agent Toolchain](#case-36) | Interactive Games & 3D | Use Kimi K3 with Grok Build or Claude Code and Spriterrific to assemble a 2.5D game workflow. | Tutorial |
| [Evaluate Induction Reasoning With Graph-to-Formula Tasks](#case-37) | Evaluation & Limits | Measure correctness, holdout behavior, and formula complexity on first-order induction tasks. | Benchmark |
| [Review Reported Games, Landing Pages, 3D Work, and Long Context](#case-38) | Evaluation & Limits | Use a multi-source roundup to compare concrete artifacts and note speed limitations alongside cost claims. | Evaluation |
| [Invent a Luxury Bread Cutter and Its Product Page](#case-39) | Frontend & Motion Design | Combine product ideation, an exploded view, a demonstration, and a landing page in one design artifact. | Demo |
| [Audit a Complex Plan and Challenge Its Remedies](#case-40) | Evaluation & Limits | Use a second model to identify understated findings, incorrect remedies, and conclusions that should be rejected. | Evaluation |
| [Compare PPO-Style Reinforcement-Learning ASCII Diagrams](#case-41) | Evaluation & Limits | Hold an ASCII-diagram prompt constant and compare how models represent the reinforcement-learning loop. | Evaluation |
| [Model in Blender While Tracking Capacity Errors](#case-42) | Evaluation & Limits | Evaluate partial Blender progress together with service reliability rather than judging only the artifact. | Limit |
| [Build a Browser-Based 3D Wuxia RPG](#case-43) | Interactive Games & 3D | Combine melee combat, quests, inventory, weather, interiors, Blender environment work, and adapted assets. | Demo |
| [Build a Browser Multiplayer Minecraft-Like Game](#case-44) | Interactive Games & 3D | Use a bounded time-and-cost run to produce a playable online multiplayer browser game. | Demo |
| [Generate a Ten-Second Recursive Pelican GIF](#case-45) | Frontend & Motion Design | Use a fully specified looping-animation brief to inspect narrative continuity and recursion in a GIF. | Demo |
| [Build a Game Boy Advance Emulator Around mGBA WASM](#case-46) | Coding & Integrations | Integrate a licensed 3D model and a real emulator core, then recursively improve interface and gameplay. | Integration |
| [Compare Flappy Bird Generation in an Arena](#case-47) | Evaluation & Limits | Use an arena task to compare two generated Flappy Bird results while keeping the judgment task-specific. | Evaluation |
| [Recreate a Split-Screen Cooperative Browser Game](#case-48) | Interactive Games & 3D | Use one request to generate browser-based split-screen cooperation and real-time environment interaction. | Demo |
| [Generate a Playable Game With Command Code Design Mode](#case-49) | Interactive Games & 3D | Use Command Code's design command for a one-shot game build and record whether the result is playable. | Demo |
| [Research Multiple Topics From Chinese-Language Sources](#case-50) | Coding & Integrations | Use long-running research tasks to compare thoroughness and latency across model generations. | Evaluation |
| [Assemble a Cohesive Wuxia Browser RPG](#case-51) | Interactive Games & 3D | Integrate traversal, combat, quests, inventory, weather, exploration, and 3D environment work in one game. | Demo |
| [Solve a Bongard Visual Induction Problem With a Tool](#case-52) | Evaluation & Limits | Test whether tool use helps derive the visual rule in a Bongard reasoning task. | Evaluation |
| [Compare Frontend Taste and 3D Design With GPT-5.6 Sol](#case-53) | Evaluation & Limits | Inspect features, visual taste, elegance, and 3D execution in a bounded frontend comparison. | Evaluation |
| [Build a Playable Hollow Knight Crossover](#case-54) | Interactive Games & 3D | Use existing game assets to create a playable battle between the Knight and Kimi. | Demo |
| [Generate a BMW M4 CS Side-View SVG](#case-55) | Frontend & Motion Design | Use a specific vehicle and viewpoint to inspect vector illustration output. | Demo |
| [Clone macOS in the Browser With Working Apps](#case-56) | Coding & Integrations | Build a browser operating-system simulation that includes music, browser, and email applications. | Demo |
| [Compare Website Generation Across Three Models](#case-57) | Evaluation & Limits | Use visible website outputs to compare Kimi K3, Fable 5, and GPT-5.6 Sol on one test. | Evaluation |
| [Recreate Gargantua Through Screenshot Feedback](#case-58) | Frontend & Motion Design | Use repeated screenshots as observations for diagnosing and refining a scientific visualization. | Tutorial |
| [Compare Procedural 3D Game Generation and Cost](#case-59) | Evaluation & Limits | Hold a prompt constant across models and inspect generated roulette, slot-machine, and pinball systems with per-run cost. | Benchmark |
| [Build a Fall Guys-Style 3D Browser Game in One Shot](#case-60) | Interactive Games & 3D | Use a one-shot request to generate a playable 3D obstacle game and expose the project for inspection. | Demo |
| [Build and Self-Test an Apocalyptic Lisbon FPS](#case-61) | Interactive Games & 3D | Use a one-prompt maximum-effort run that tests, screenshots, and iterates before delivering a playable FPS. | Demo |
| [Build a macOS Simulation With Working FaceTime](#case-62) | Coding & Integrations | Use a virtual operating-system task to test whether a generated app interaction functions. | Demo |
| [Generate an Animal Crossing-Style Game From a Simple Request](#case-63) | Interactive Games & 3D | Use a minimal game brief to inspect playability, gameplay loop, and parallax effects. | Demo |
| [Add a Dual-Task Frontend Effect Comparator](#case-64) | Coding & Integrations | Build a tool that selects two completed tasks, displays them side by side, and synchronizes views and interactions. | Tutorial |
| [Generate a Mario-Like Game From a One-Sentence Brief](#case-65) | Interactive Games & 3D | Use a minimal one-shot request to inspect playability, stage design, pixel art, and parallax. | Demo |
| [Refine a Black Hole Visualization With 62 Screenshots](#case-66) | Frontend & Motion Design | Use a screenshot feedback loop to read, diagnose, and correct a visual simulation over many iterations. | Tutorial |
| [Build a Working Zombie First-Person Shooter](#case-67) | Interactive Games & 3D | Use a concrete zombie-shooter target to inspect a complete playable FPS artifact. | Demo |
| [Create a Post-Training Marketing PDF](#case-68) | Frontend & Motion Design | Use a named product and deliverable format to generate a marketing document. | Demo |
| [Compare 3D Arsenal Scene Detail and Lighting](#case-69) | Evaluation & Limits | Inspect object density, lighting, and scene detail in a bounded Kimi K3 versus Opus 4.8 comparison. | Evaluation |
| [Create a User Interface From One Prompt](#case-70) | Frontend & Motion Design | Use a single request to generate and inspect a complete UI design. | Demo |
| [Build an Indie Spaceship Game](#case-71) | Interactive Games & 3D | Use Kimi K3 Standard for a first-pass indie game prototype, then compare cohesion, defects, visual polish, and token cost before choosing a model for later iterations. | Demo |
| [Compare Frontends With Identical Arena Prompts](#case-72) | Evaluation & Limits | Use identical prompts and side-by-side outputs to compare Kimi K3 with Fable 5 on frontend implementation instead of relying on one leaderboard number. | Benchmark |
| [Self-Test a Summer Engine Game](#case-73) | Interactive Games & 3D | Let Kimi K3 run a game, inspect screenshots and logs, and fix visible defects inside one engine session instead of stopping at initial code generation. | Demo |
| [Benchmark Kimi Code on Coding Agents](#case-74) | Evaluation & Limits | Compare Kimi K3 across multiple coding-agent suites and per-task cost before treating a single frontend leaderboard as general coding-agent performance. | Benchmark |
| [Configure Kimi as a Codex Subagent](#case-75) | Coding & Integrations | Keep Codex responsible for orchestration and delegate frontend execution to a Kimi K3 OpenCode subagent with an explicit secret-handling boundary. | Tutorial |
| [Compare Arena and Repair Harness Results](#case-76) | Evaluation & Limits | Use both frontend preference and repository-repair evaluations because Kimi K3 can rank first on one surface and last in a seven-model repair harness. | Benchmark |
| [Iterate a Browser Battle Royale](#case-77) | Interactive Games & 3D | Expect long autonomous iteration plus targeted follow-up prompts when building a feature-rich browser game instead of treating the first visible output as finished. | Demo |
| [Build an Award-Winning Website](#case-78) | Frontend & Motion Design | Follow a complete recorded session when evaluating Kimi K3 for a polished website build so the process can be inspected beyond a final screenshot. | Tutorial |
| [Route Simple Coding Through ChatLLM](#case-79) | Coding & Integrations | Create a task router that sends simple coding to Kimi K3 while reserving harder coding and design work for different models. | Integration |
| [Benchmark Kimi K3 on Prinzbench](#case-80) | Evaluation & Limits | Use an independent benchmark update to compare Kimi K3 with open and frontier models across search, reasoning, and consistency. | Benchmark |
| [Build a Metaball Scroll Frontend](#case-81) | Frontend & Motion Design | Ask Kimi K3 for an Awwwards-style scrolling page and inspect whether mathematical effects can replace heavy mesh or texture assets. | Demo |
| [Redesign a Personal Site Across Models](#case-82) | Frontend & Motion Design | Run the same site-redesign brief through multiple coding harnesses and compare execution time, visual direction, and fit to the existing identity. | Evaluation |
| [Expand a Space Game Landscape](#case-83) | Interactive Games & 3D | Use Kimi K3 as a long-running pass to replace placeholder terrain with a larger real-world-inspired game environment. | Demo |
| [Unblock a Three.js Physics Renderer](#case-84) | Interactive Games & 3D | Bring Kimi K3 into a stalled Three.js physics project when the math works but the render pipeline needs progress. | Demo |
| [Compare ISS Digital Twin Generation](#case-85) | Evaluation & Limits | Use a same-prompt 3D modeling challenge to compare Kimi K3 and GPT-5.6 Sol on reconstruction, controls, labels, and visual detail. | Benchmark |
| [Build an Interactive Human Scalp Explorer](#case-86) | Frontend & Motion Design | Use Kimi K3 for a single-shot educational 3D scene with anatomical layers, responsive hair strands, and interactive hotspots. | Demo |
| [Share a 3D Globe Dashboard Prompt](#case-87) | Frontend & Motion Design | Study a shared prompt and reference-image setup for a Kimi K3 3D globe dashboard instead of inferring the workflow from the final image alone. | Tutorial |
| [Build Browser Counter-Strike in One File](#case-88) | Interactive Games & 3D | Use Kimi K3 to generate a single-file browser FPS and check whether the result covers map layout, bots, weapons, round rules, and procedural audio. | Demo |
| [Review a WebGPU Forest World](#case-89) | Evaluation & Limits | Evaluate Kimi K3 as a coding-agent brain on a long-horizon Three.js and WebGPU world build, including quality, speed, consistency, and edit rate. | Evaluation |

<a id="games-3d"></a>
## 🎮 Interactive Games & 3D

<a id="case-1"></a>
### Case 1: [Build a Voxel Pod Racer From One Prompt](https://x.com/ivanfioravanti/status/2077763009657627055) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Use a short scene concept to prototype a playable voxel pod-racing experience, then plan a second pass for racers, a finish line, and detail review.**

The creator reports that Kimi K3 produced version one from a single public prompt and says version two would add more racers, a finish line, and detail review.

**Prompt:**

```text
Voxel star wars pod-racers run
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01-poster.jpg" alt="Case 1 source video poster" height="360"></a>

[Play case 1 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-2"></a>
### Case 2: [Compare Frogger Builds With the Same Prompt](https://x.com/ivanfioravanti/status/2077754781964054825) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Hold the prompt constant when comparing two model outputs so the resulting gameplay difference is easier to inspect.**

The creator shares a Kimi K3 Frogger version as a same-prompt comparison between two models. The supplied source does not publish the prompt text or evaluation rubric.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02-poster.jpg" alt="Case 2 source video poster" height="360"></a>

[Play case 2 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-3"></a>
### Case 3: [Generate a Frogger Game and Its Recording](https://x.com/TheAhmadOsman/status/2077776567292338285) (by [@TheAhmadOsman](https://x.com/TheAhmadOsman))

**Test a one-shot game build together with a separate one-shot workflow for recording the resulting gameplay.**

The creator reports that Kimi K3 produced the Frogger game in one shot and also produced the gameplay recording workflow in one shot. The exact prompts are not included.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03-poster.jpg" alt="Case 3 source video poster" height="360"></a>

[Play case 3 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-4"></a>
### Case 4: [Prototype an Aircraft Carrier in Three.js](https://x.com/HarshithLucky3/status/2077753222018814360) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**Use a concrete launch-and-recovery scene to probe Kimi K3's ability to produce an interactive Three.js 3D prototype.**

The creator demonstrates a Three.js scene of fighter-jet launch and recovery on a Nimitz-class aircraft carrier and describes Kimi K3 as strong for 3D generation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04-poster.jpg" alt="Case 4 source video poster" height="360"></a>

[Play case 4 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-9"></a>
### Case 9: [Build a Paper Mario-Inspired Game With Agent Tools](https://x.com/chongdashu/status/2077886028866531655) (by [@chongdashu](https://x.com/chongdashu))

**Combine Kimi K3 with an agent harness and asset tools to produce both 2D and 3D game elements.**

The creator reports using Kimi K3 with Grok Build, Spriterrific for 2D assets, and geometry for 3D assets in a Paper Mario-inspired game. The source demonstrates tool and skill use but does not publish an exact reusable prompt.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-09.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-09-poster.jpg" alt="Case 9 source video poster" height="360"></a>

[Play case 9 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-09.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-11"></a>
### Case 11: [Generate a Subway First-Person Shooter](https://x.com/bijanbowen/status/2077881805751873997) (by [@bijanbowen](https://x.com/bijanbowen))

**Use a concrete subway setting to inspect a generated first-person shooter result.**

The creator shows a subway FPS attributed to Kimi K3 and explicitly notes uncertainty about whether influencer status affected the result. No prompt or reproducible workflow is supplied.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-11.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-11-poster.jpg" alt="Case 11 source video poster" height="360"></a>

[Play case 11 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-11.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-19"></a>
### Case 19: [Model a V8 Engine With Blender MCP](https://x.com/aisearchio/status/2077962156147146925) (by [@aisearchio](https://x.com/aisearchio))

**Use Blender MCP and a single request to generate a detailed mechanical 3D model.**

The reviewer reports that Kimi K3 generated a complete V8 engine with Blender MCP from one prompt. The post links a fuller review but does not expose the exact prompt in the supplied record.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-19.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-19-poster.jpg" alt="Case 19 source video poster" height="360"></a>

[Play case 19 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-19.mp4)

Type: Integration | Date: 2026-07-17

---

<a id="case-23"></a>
### Case 23: [Build a Playable Battle Arena From One Reference](https://x.com/VORTEX_Promos/status/2077879705378730074) (by [@VORTEX_Promos](https://x.com/VORTEX_Promos))

**Use a single reference to test one-shot generation of a complete playable arena.**

The creator reports that Kimi K3 produced a playable battle arena in one shot from one reference. A separate leaderboard claim appears in the post, but the concrete use case is the demonstrated arena artifact.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23-poster.jpg" alt="Case 23 source video poster" height="360"></a>

[Play case 23 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23-01.jpg" alt="Case 23 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-24"></a>
### Case 24: [Build Three Self-Playing Retro Games as HTML Files](https://x.com/rohanpaul_ai/status/2077889084761206860) (by [@rohanpaul_ai](https://x.com/rohanpaul_ai))

**Require graphics, enemies, rules, and autonomous play inside standalone HTML game files.**

The source reports an Atomic Chat comparison in which models built Road Fighter, Battle City, and Q*bert as self-playing HTML files. Its cost and quality comparison is reported by the publisher and not independently reproduced here.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-24.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-24-poster.jpg" alt="Case 24 source video poster" height="360"></a>

[Play case 24 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-24.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-27"></a>
### Case 27: [Build a One-Shot Chameleon Hide-and-Seek Game](https://x.com/aimlapi/status/2077898742179459274) (by [@aimlapi](https://x.com/aimlapi))

**Generate a single-file game with color matching, procedural areas, sound, and multi-round scoring.**

AIMLAPI reports a same-prompt one-shot comparison for a hide-and-seek game and lists costs of $3.11 for Kimi K3 and $12.23 for Fable 5. The feature and cost claims are provider-reported results.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-27.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-27-poster.jpg" alt="Case 27 source video poster" height="360"></a>

[Play case 27 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-27.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-36"></a>
### Case 36: [Build a 2.5D Paper Mario-Like Game With an Agent Toolchain](https://x.com/chongdashu/status/2077981621223837739) (by [@chongdashu](https://x.com/chongdashu))

**Use Kimi K3 with Grok Build or Claude Code and Spriterrific to assemble a 2.5D game workflow.**

The creator provides a full walkthrough using Grok Build and Kimi K3 and shows sprite generation with Spriterrific. The source identifies the tools but does not supply exact reusable prompts.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-36.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-36-poster.jpg" alt="Case 36 source video poster" height="360"></a>

[Play case 36 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-36.mp4)

Type: Tutorial | Date: 2026-07-17

---

<a id="case-43"></a>
### Case 43: [Build a Browser-Based 3D Wuxia RPG](https://x.com/AngryTomtweets/status/2077868163136450619) (by [@AngryTomtweets](https://x.com/AngryTomtweets))

**Combine melee combat, quests, inventory, weather, interiors, Blender environment work, and adapted assets.**

The source reports a Kimi K3 browser RPG with melee combat, quests, inventory, dynamic weather, and explorable interiors, plus Blender modeling, collision improvements, PBR retexturing, and adapted open assets.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-43.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-43-poster.jpg" alt="Case 43 source video poster" height="360"></a>

[Play case 43 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-43.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-44"></a>
### Case 44: [Build a Browser Multiplayer Minecraft-Like Game](https://x.com/Alezander907/status/2077926014710407407) (by [@Alezander907](https://x.com/Alezander907))

**Use a bounded time-and-cost run to produce a playable online multiplayer browser game.**

The creator reports that Kimi K3 built a browser-playable multiplayer Minecraft-like game in one hour at a cost of $6.57. These are self-reported run figures from one artifact.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-44.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-44-poster.jpg" alt="Case 44 source video poster" height="360"></a>

[Play case 44 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-44.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-48"></a>
### Case 48: [Recreate a Split-Screen Cooperative Browser Game](https://x.com/ridark_eth/status/2077882889803378969) (by [@ridark_eth](https://x.com/ridark_eth))

**Use one request to generate browser-based split-screen cooperation and real-time environment interaction.**

The creator reports that Kimi K3 produced an It Takes Two-inspired browser game in one prompt, with Mario and Luigi interacting in split-screen and with the environment in real time.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-48.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-48-poster.jpg" alt="Case 48 source video poster" height="360"></a>

[Play case 48 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-48.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-49"></a>
### Case 49: [Generate a Playable Game With Command Code Design Mode](https://x.com/naymur_dev/status/2077873562661335207) (by [@naymur_dev](https://x.com/naymur_dev))

**Use Command Code's design command for a one-shot game build and record whether the result is playable.**

The creator reports a one-shot comparison using Command Code design mode and says the Kimi K3 run produced a playable game for $0.038. This cost and quality result is self-reported.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-49.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-49-poster.jpg" alt="Case 49 source video poster" height="360"></a>

[Play case 49 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-49.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-51"></a>
### Case 51: [Assemble a Cohesive Wuxia Browser RPG](https://x.com/TokenGremlin/status/2077855657068310620) (by [@TokenGremlin](https://x.com/TokenGremlin))

**Integrate traversal, combat, quests, inventory, weather, exploration, and 3D environment work in one game.**

The source reports a Kimi K3 wuxia-style browser RPG that combines melee combat, quests, inventory, dynamic weather, explorable interiors, and a cohesive 3D gameplay structure.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-51.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-51-poster.jpg" alt="Case 51 source video poster" height="360"></a>

[Play case 51 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-51.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-54"></a>
### Case 54: [Build a Playable Hollow Knight Crossover](https://x.com/wangfeng0315/status/2077933531200991583) (by [@wangfeng0315](https://x.com/wangfeng0315))

**Use existing game assets to create a playable battle between the Knight and Kimi.**

The creator, who states they work at Kimi, reports building a game from Hollow Knight assets in which the Knight battles Kimi and provides a public play link. Attribution and evaluation should account for that affiliation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54-poster.jpg" alt="Case 54 source video poster" height="360"></a>

[Play case 54 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54-01.jpg" alt="Case 54 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-17

---

<a id="case-60"></a>
### Case 60: [Build a Fall Guys-Style 3D Browser Game in One Shot](https://x.com/aayushman2703/status/2077857886441783526) (by [@aayushman2703](https://x.com/aayushman2703))

**Use a one-shot request to generate a playable 3D obstacle game and expose the project for inspection.**

The creator reports a one-shot Kimi K3 build of a Fall Guys-style browser game and says the prompt and GitHub project are linked from the source. This record does not reproduce that prompt.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-60.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-60-poster.jpg" alt="Case 60 source video poster" height="360"></a>

[Play case 60 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-60.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-61"></a>
### Case 61: [Build and Self-Test an Apocalyptic Lisbon FPS](https://x.com/goncalo_canhoto/status/2077863166655037668) (by [@goncalo_canhoto](https://x.com/goncalo_canhoto))

**Use a one-prompt maximum-effort run that tests, screenshots, and iterates before delivering a playable FPS.**

The creator reports that Kimi K3 produced a playable Apocalyptic Lisbon browser FPS after about one hour, with repeated tests, screenshots, and iterations. These timing and process details are self-reported.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-61-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-61-01.jpg" alt="Case 61 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-63"></a>
### Case 63: [Generate an Animal Crossing-Style Game From a Simple Request](https://x.com/gagarot200/status/2077949230287896830) (by [@gagarot200](https://x.com/gagarot200))

**Use a minimal game brief to inspect playability, gameplay loop, and parallax effects.**

The creator reports that Kimi K3 generated a fully playable Animal Crossing-style game with a gameplay loop and parallax effects from a very simple prompt. The exact wording is not present in the supplied record.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-63.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-63-poster.jpg" alt="Case 63 source video poster" height="360"></a>

[Play case 63 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-63.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-65"></a>
### Case 65: [Generate a Mario-Like Game From a One-Sentence Brief](https://x.com/izutorishima/status/2077939370154475992) (by [@izutorishima](https://x.com/izutorishima))

**Use a minimal one-shot request to inspect playability, stage design, pixel art, and parallax.**

The creator reports that Kimi K3 produced a working Mario-like game without obvious bugs, including stage structure and parallax, from a single brief. The same report criticizes the music and graphics quality.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-01.jpg" alt="Case 65 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-02.jpg" alt="Case 65 source image 2" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-03.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-03.jpg" alt="Case 65 source image 3" height="360"></a>

Type: Demo | Date: 2026-07-17

---

<a id="case-67"></a>
### Case 67: [Build a Working Zombie First-Person Shooter](https://x.com/X2worldtech/status/2077902793449296203) (by [@X2worldtech](https://x.com/X2worldtech))

**Use a concrete zombie-shooter target to inspect a complete playable FPS artifact.**

The source shows a full working zombie FPS attributed to Kimi K3. It does not provide the prompt, implementation details, or an external gameplay assessment.

> [!WARNING]
> The original source permalink returned HTTP 404 during the 2026-07-17 audit. Attribution and evidence are preserved from the supplied high-confidence source package.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-67.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-67-poster.jpg" alt="Case 67 source video poster" height="360"></a>

[Play case 67 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-67.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-71"></a>
### Case 71: [Build an Indie Spaceship Game](https://x.com/ChrisGPT/status/2078261217924087999) (by [@ChrisGPT](https://x.com/ChrisGPT))

**Use Kimi K3 Standard for a first-pass indie game prototype, then compare cohesion, defects, visual polish, and token cost before choosing a model for later iterations.**

ChrisGPT reports that Kimi K3 Standard produced the first pass of an indie spaceship game for an estimated $2.50 in API tokens. The creator judged the result more cohesive and less buggy than a GPT-5.5 first pass while noting that Fable 5 still looked more polished and would require further Kimi iterations to match.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-71.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-71-poster.jpg" alt="Case 71 source video poster" height="360"></a>

[Play case 71 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-71.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-73"></a>
### Case 73: [Self-Test a Summer Engine Game](https://x.com/MathiasHeide/status/2078231589436465199) (by [@MathiasHeide](https://x.com/MathiasHeide))

**Let Kimi K3 run a game, inspect screenshots and logs, and fix visible defects inside one engine session instead of stopping at initial code generation.**

Mathias Heide reports that Kimi K3 built a working paper-plane game in Summer Engine in 27 minutes and one session. The model launched the game, watched it run, captured screenshots, read logs, fixed bugs, and corrected the plane color after noticing that paper should be white rather than black.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-73.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-73-poster.jpg" alt="Case 73 source video poster" height="360"></a>

[Play case 73 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-73.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-77"></a>
### Case 77: [Iterate a Browser Battle Royale](https://x.com/Ananth7e/status/2078158089929601203) (by [@Ananth7e](https://x.com/Ananth7e))

**Expect long autonomous iteration plus targeted follow-up prompts when building a feature-rich browser game instead of treating the first visible output as finished.**

Ananth reports that Kimi K3 spent more than 130 minutes and over 40 rounds taking Chrome screenshots, finding issues, and fixing them before producing a PUBG-style browser game. The result included terrain, buildings, two gun types, loot, bots, kill updates, and a shrinking zone, then needed two additional prompts to fix remaining bugs.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-77.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-77-poster.jpg" alt="Case 77 source video poster" height="360"></a>

[Play case 77 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-77.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-83"></a>
### Case 83: [Expand a Space Game Landscape](https://x.com/startracker/status/2078543423167160342) (by [@startracker](https://x.com/startracker))

**Use Kimi K3 as a long-running pass to replace placeholder terrain with a larger real-world-inspired game environment.**

The creator describes day two of a space-game build where Kimi K3 replaced a small placeholder coast with an 8 x 8 km Iceland-inspired landscape, added coastline-aware animated ocean, rebuilt the spacecraft exterior, and generated additional environment assets for a later pass. The source also notes slow, deliberate execution and remaining frame-capture issues.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-83.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-83-poster.jpg" alt="Case 83 source video poster" height="360"></a>

[Play case 83 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-83.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-84"></a>
### Case 84: [Unblock a Three.js Physics Renderer](https://x.com/mattwatkajtys/status/2078523373861339475) (by [@mattwatkajtys](https://x.com/mattwatkajtys))

**Bring Kimi K3 into a stalled Three.js physics project when the math works but the render pipeline needs progress.**

The creator reports that a physics world builder had been stuck for months because the render pipeline was not progressing, while the underlying math and physics already worked. The Kimi K3 pass moved the project forward and the attached video shows the current interactive result.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-84.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-84-poster.jpg" alt="Case 84 source video poster" height="360"></a>

[Play case 84 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-84.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-88"></a>
### Case 88: [Build Browser Counter-Strike in One File](https://x.com/prasenx/status/2078453069021659477) (by [@prasenx](https://x.com/prasenx))

**Use Kimi K3 to generate a single-file browser FPS and check whether the result covers map layout, bots, weapons, round rules, and procedural audio.**

The creator reports building a Counter-Strike-like browser game with Kimi K3 in one HTML file of more than 3,700 lines and no build step. The described artifact includes a Dust2-inspired map, several weapons, reloads, patrolling and pushing bots, headshots, kill feed, a two-minute round, procedural audio, Three.js, PBR, and under-$5 API cost.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-88.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-88-poster.jpg" alt="Case 88 source video poster" height="360"></a>

[Play case 88 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-88.mp4)

Type: Demo | Date: 2026-07-18

---


<a id="frontend-motion"></a>
## 🎨 Frontend & Motion Design

<a id="case-5"></a>
### Case 5: [Create an Interactive Motion Graphic Frontend](https://x.com/chetaslua/status/2077749371144442022) (by [@chetaslua](https://x.com/chetaslua))

**Use a one-shot code-generation test to build motion graphics that remain interactive when the animation is paused.**

The creator reports a 42-minute, one-shot build using simple code without a harness, MCP, or skills, and demonstrates a motion graphic whose design remains interactive when paused.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05-poster.jpg" alt="Case 5 source video poster" height="360"></a>

[Play case 5 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-6"></a>
### Case 6: [Produce a Synchronized Motion Graphic Ad](https://x.com/abhinavflac/status/2077760297918484667) (by [@abhinavflac](https://x.com/abhinavflac))

**Evaluate a one-shot motion-graphics workflow by checking whether music, effects, and motion stay synchronized in the final ad.**

The creator reports that a pure-prompt, one-shot Kimi K3 run produced a Spotify-themed motion graphic ad with synchronized music, effects, and motion. The exact prompt is not included.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06-poster.jpg" alt="Case 6 source video poster" height="360"></a>

[Play case 6 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-14"></a>
### Case 14: [Create Motion Design Entirely in Code](https://x.com/chetaslua/status/2077952938564354503) (by [@chetaslua](https://x.com/chetaslua))

**Test whether a one-shot coding workflow can produce motion design without auxiliary generation tools.**

The creator reports a one-shot Kimi K3 motion-design result made fully in code without MCP, skills, tools, video generation, or special prompts. The exact prompt is not provided.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-14.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-14-poster.jpg" alt="Case 14 source video poster" height="360"></a>

[Play case 14 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-14.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-15"></a>
### Case 15: [Research a Person and Build an Animated Personal Site](https://x.com/nicky_sap/status/2077857190707429411) (by [@nicky_sap](https://x.com/nicky_sap))

**Give a broad personal-site brief, then inspect the model's research, planning, iteration, and browser validation.**

The creator reports that Kimi K3 researched Nick Saponaro and produced an animated personal website from a broad request, including planning, testing, iteration, and browser checks. The result is a self-reported workflow demonstration.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-15.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-15-poster.jpg" alt="Case 15 source video poster" height="360"></a>

[Play case 15 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-15.mp4)

Type: Tutorial | Date: 2026-07-16

---

<a id="case-17"></a>
### Case 17: [Generate a Black Hole Simulation](https://x.com/chetaslua/status/2077961850352971796) (by [@chetaslua](https://x.com/chetaslua))

**Use a scientific-visualization task to inspect a generated black-hole simulation.**

The creator shows a black-hole simulation attributed to Kimi K3 and calls it the best they have seen. The source provides a visible result but no prompt, rubric, or independent validation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-17.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-17-poster.jpg" alt="Case 17 source video poster" height="360"></a>

[Play case 17 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-17.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-22"></a>
### Case 22: [Test Complex Frontend Modeling, Particles, and Shaders](https://x.com/karminski3/status/2077889959223337099) (by [@karminski3](https://x.com/karminski3))

**Use a public frontend prompt to inspect modeling precision, particle effects, and inline shader generation in one pass.**

The creator reports a one-pass Kimi K3 frontend result covering precise modeling, particle effects, and complex inline shader code, and states that the test prompt is public at the linked source.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-22.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-22-poster.jpg" alt="Case 22 source video poster" height="360"></a>

[Play case 22 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-22.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-26"></a>
### Case 26: [Generate a Procedural Music Tool in One Attempt](https://x.com/mirochill/status/2077723551331758478) (by [@mirochill](https://x.com/mirochill))

**Test one-shot generation of an interactive procedural-music generator and compare the visible result cautiously.**

The creator reports that Kimi K3 generated a procedural music tool in one attempt and compares it favorably with results from Fable 5 and GPT-5.6 Sol. This is the creator's own test set, not a standardized benchmark.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-26-poster.jpg" alt="Case 26 source video poster" height="360"></a>

[Play case 26 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-26.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-33"></a>
### Case 33: [Create a Three.js Product Page From Two Images](https://x.com/1littlecoder/status/2077890296806031665) (by [@1littlecoder](https://x.com/1littlecoder))

**Use two reference images and an explicit Three.js requirement to generate a product presentation.**

The creator reports that Kimi K3 designed a product page from two images and produced the explicitly requested Three.js version. No further prompt or implementation details are provided.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-33.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-33-poster.jpg" alt="Case 33 source video poster" height="360"></a>

[Play case 33 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-33.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-39"></a>
### Case 39: [Invent a Luxury Bread Cutter and Its Product Page](https://x.com/filicroval/status/2077871090731221438) (by [@filicroval](https://x.com/filicroval))

**Combine product ideation, an exploded view, a demonstration, and a landing page in one design artifact.**

The creator reports that Kimi K3 invented a guillotine-style bread cutter, framed it as a luxury product, and produced a landing page with an exploded view and demonstration.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-39.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-39-poster.jpg" alt="Case 39 source video poster" height="360"></a>

[Play case 39 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-39.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-45"></a>
### Case 45: [Generate a Ten-Second Recursive Pelican GIF](https://x.com/1littlecoder/status/2077880380900937865) (by [@1littlecoder](https://x.com/1littlecoder))

**Use a fully specified looping-animation brief to inspect narrative continuity and recursion in a GIF.**

The source includes a prompt for a looping ten-second GIF of a pelican riding a bicycle and receiving the same video by text as the camera zooms in. The creator shows Kimi K3's resulting animation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-45.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-45-poster.jpg" alt="Case 45 source video poster" height="360"></a>

[Play case 45 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-45.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-55"></a>
### Case 55: [Generate a BMW M4 CS Side-View SVG](https://x.com/HarshithLucky3/status/2077765821380886942) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**Use a specific vehicle and viewpoint to inspect vector illustration output.**

The creator shows a side-view BMW M4 CS SVG attributed to Kimi K3 Max. The supplied source contains the artifact but no prompt or production steps.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-55-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-55-01.jpg" alt="Case 55 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-58"></a>
### Case 58: [Recreate Gargantua Through Screenshot Feedback](https://x.com/AngryTomtweets/status/2077868981659324444) (by [@AngryTomtweets](https://x.com/AngryTomtweets))

**Use repeated screenshots as observations for diagnosing and refining a scientific visualization.**

The source reports that Kimi K3 recreated Interstellar's Gargantua through 62 self-screenshots, reading each result, diagnosing problems, and acting on them iteratively.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-58.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-58-poster.jpg" alt="Case 58 source video poster" height="360"></a>

[Play case 58 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-58.mp4)

Type: Tutorial | Date: 2026-07-16

---

<a id="case-66"></a>
### Case 66: [Refine a Black Hole Visualization With 62 Screenshots](https://x.com/TokenGremlin/status/2077855959201042645) (by [@TokenGremlin](https://x.com/TokenGremlin))

**Use a screenshot feedback loop to read, diagnose, and correct a visual simulation over many iterations.**

The source reports that Kimi K3 reconstructed Interstellar's Gargantua by observing and refining its output across 62 screenshots. This demonstrates the reported feedback loop rather than independent physical accuracy.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-66.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-66-poster.jpg" alt="Case 66 source video poster" height="360"></a>

[Play case 66 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-66.mp4)

Type: Tutorial | Date: 2026-07-16

---

<a id="case-68"></a>
### Case 68: [Create a Post-Training Marketing PDF](https://x.com/Satvik_Pen/status/2077859673517023313) (by [@Satvik_Pen](https://x.com/Satvik_Pen))

**Use a named product and deliverable format to generate a marketing document.**

The creator reports asking Kimi K3 for a marketing PDF about Thinking Machines' Inkling post-training and shares the result, while also praising the behind-the-scenes process. No prompt or evaluation criteria are supplied.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-01.png" alt="Case 68 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-02.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-02.png" alt="Case 68 source image 2" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-03.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-03.png" alt="Case 68 source image 3" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-04.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-04.png" alt="Case 68 source image 4" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-70"></a>
### Case 70: [Create a User Interface From One Prompt](https://x.com/BrianMRey/status/2077891942088671689) (by [@BrianMRey](https://x.com/BrianMRey))

**Use a single request to generate and inspect a complete UI design.**

The creator shows a UI design attributed to a one-prompt Kimi K3 run and gives a strongly positive subjective assessment. The exact prompt and rubric are not included.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-70.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-70-poster.jpg" alt="Case 70 source video poster" height="360"></a>

[Play case 70 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-70.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-78"></a>
### Case 78: [Build an Award-Winning Website](https://x.com/viktoroddy/status/2078140696910037002) (by [@viktoroddy](https://x.com/viktoroddy))

**Follow a complete recorded session when evaluating Kimi K3 for a polished website build so the process can be inspected beyond a final screenshot.**

Viktor Oddy publishes a 13-minute tutorial showing how to create an award-style website with Kimi K3. The full-length source video provides a process-oriented reference for frontend builders and is stronger evidence than a short launch montage or isolated finished image.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-78.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-78-poster.jpg" alt="Case 78 source video poster" height="360"></a>

[Play case 78 tutorial video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-78.mp4)

Type: Tutorial | Date: 2026-07-17

---

<a id="case-81"></a>
### Case 81: [Build a Metaball Scroll Frontend](https://x.com/abhinavflac/status/2078603131055993130) (by [@abhinavflac](https://x.com/abhinavflac))

**Ask Kimi K3 for an Awwwards-style scrolling page and inspect whether mathematical effects can replace heavy mesh or texture assets.**

The creator reports one Kimi K3 frontend session that produced a scrolling metaball-style site using math-driven visual behavior rather than meshes or textures. The attached source video is the visible artifact; no reusable prompt or implementation steps are published.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-81.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-81-poster.jpg" alt="Case 81 source video poster" height="360"></a>

[Play case 81 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-81.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-82"></a>
### Case 82: [Redesign a Personal Site Across Models](https://x.com/fabriciocarraro/status/2078574831466078265) (by [@fabriciocarraro](https://x.com/fabriciocarraro))

**Run the same site-redesign brief through multiple coding harnesses and compare execution time, visual direction, and fit to the existing identity.**

The creator reports testing Fable 5, GPT-5.6 Sol, and Kimi K3 on a personal-site redesign using each model's official harness and maximum effort mode. Kimi K3 took about 50 minutes, while Fable took 35 minutes and Sol took about 70 minutes; the post frames the outcome as a task-specific mini benchmark rather than a general leaderboard.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-82.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-82-poster.jpg" alt="Case 82 source video poster" height="360"></a>

[Play case 82 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-82.mp4)

Type: Evaluation | Date: 2026-07-18

---

<a id="case-86"></a>
### Case 86: [Build an Interactive Human Scalp Explorer](https://x.com/MiaAI_lab/status/2078508824752017757) (by [@MiaAI_lab](https://x.com/MiaAI_lab))

**Use Kimi K3 for a single-shot educational 3D scene with anatomical layers, responsive hair strands, and interactive hotspots.**

The creator reports that Kimi K3 single-shot a realistic 3D human scalp explorer using about 105k tokens, with cinematic lighting, layered anatomy, responsive hair strands, cross-sections, and educational hotspots. The source says the result was impressive but not cheap, and links a try-it-yourself target.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-86.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-86-poster.jpg" alt="Case 86 source video poster" height="360"></a>

[Play case 86 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-86.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-87"></a>
### Case 87: [Share a 3D Globe Dashboard Prompt](https://x.com/hqmank/status/2078465403349840144) (by [@hqmank](https://x.com/hqmank))

**Study a shared prompt and reference-image setup for a Kimi K3 3D globe dashboard instead of inferring the workflow from the final image alone.**

The creator responds to requests for the prompt and reference image behind a Kimi K3 3D globe dashboard demo and shares both in attached source images. The repo records the source as a tutorial-style prompt boundary but does not transcribe prompt text from images.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-87.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-87-poster.jpg" alt="Case 87 source video poster" height="360"></a>

[Play case 87 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-87.mp4)

Type: Tutorial | Date: 2026-07-18

---


<a id="coding-integrations"></a>
## 💻 Coding & Integrations

<a id="case-18"></a>
### Case 18: [Build a Virtual MacBook With Functional macOS](https://x.com/scottstts/status/2077890054299541890) (by [@scottstts](https://x.com/scottstts))

**Combine Three.js hardware rendering with an interactive browser operating-system simulation.**

The source reports that Kimi K3 created a virtual MacBook in Three.js with a functional macOS-style environment. It demonstrates the artifact but does not supply implementation steps.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-18.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-18-poster.jpg" alt="Case 18 source video poster" height="360"></a>

[Play case 18 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-18.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-25"></a>
### Case 25: [Build a GPU Compiler From DSL to PTX](https://x.com/rohanpaul_ai/status/2077886618657231220) (by [@rohanpaul_ai](https://x.com/rohanpaul_ai))

**Use an end-to-end compiler task spanning a DSL, compiler passes, PTX generation, and a Tensor Core path.**

The source reports that Kimi K3 built a GPU compiler from scratch, from its DSL and passes through PTX generation, and compares its Tensor Core path with Triton. No independent benchmark details are included in the supplied record.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-25-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-25-01.png" alt="Case 25 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-32"></a>
### Case 32: [Build a Real-Time Black Hole Raytracer in WebGL2](https://x.com/AlicanKiraz0/status/2077885419744612597) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**Test one-prompt generation of a native WebGL2 geodesic raytracer inside one HTML file.**

The author describes a coding benchmark requiring a working single-file black-hole light-bending raytracer in native WebGL2. The supplied record establishes the task and participating models but not a full independent result audit.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-32.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-32-poster.jpg" alt="Case 32 source video poster" height="360"></a>

[Play case 32 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-32.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-46"></a>
### Case 46: [Build a Game Boy Advance Emulator Around mGBA WASM](https://x.com/teortaxesTex/status/2077925090168062272) (by [@teortaxesTex](https://x.com/teortaxesTex))

**Integrate a licensed 3D model and a real emulator core, then recursively improve interface and gameplay.**

The cited Kimi K3 project adapts a licensed AGB-001 model, integrates an mGBA WASM core, and improves the interface and gameplay through recursive self-improvement. The post quotes a project description rather than an independent reproduction.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-46-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-46-01.jpg" alt="Case 46 source image 1" height="360"></a>

Type: Integration | Date: 2026-07-17

---

<a id="case-50"></a>
### Case 50: [Research Multiple Topics From Chinese-Language Sources](https://x.com/tphuang/status/2077911994607239400) (by [@tphuang](https://x.com/tphuang))

**Use long-running research tasks to compare thoroughness and latency across model generations.**

The author reports testing Kimi K3 on many research topics using Chinese-language sources, finding it more thorough than K2.6 but slower. The post also notes heavy service demand at the time.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-50-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-50-01.png" alt="Case 50 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-17

---

<a id="case-56"></a>
### Case 56: [Clone macOS in the Browser With Working Apps](https://x.com/twid/status/2077924755357974989) (by [@twid](https://x.com/twid))

**Build a browser operating-system simulation that includes music, browser, and email applications.**

The source reports that Kimi K3 was used to create a browser-based macOS clone with music, browser, email, and other functions. It does not provide implementation details.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-56.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-56-poster.jpg" alt="Case 56 source video poster" height="360"></a>

[Play case 56 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-56.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-62"></a>
### Case 62: [Build a macOS Simulation With Working FaceTime](https://x.com/LinearUncle/status/2077919552239997078) (by [@LinearUncle](https://x.com/LinearUncle))

**Use a virtual operating-system task to test whether a generated app interaction functions.**

The creator shows a macOS-style environment attributed to Kimi K3 and reports that its FaceTime feature works. The source provides no setup or validation steps.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-62-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-62-01.jpg" alt="Case 62 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-17

---

<a id="case-64"></a>
### Case 64: [Add a Dual-Task Frontend Effect Comparator](https://x.com/MinLiBuilds/status/2077939461510615376) (by [@MinLiBuilds](https://x.com/MinLiBuilds))

**Build a tool that selects two completed tasks, displays them side by side, and synchronizes views and interactions.**

The creator reports asking Kimi K3 to add a frontend comparison workflow with task selection, dual browser panes, object and roaming modes, synchronized viewpoints, and interaction tests. The post also notes broader model limitations.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-64.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-64-poster.jpg" alt="Case 64 source video poster" height="360"></a>

[Play case 64 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-64.mp4)

Type: Tutorial | Date: 2026-07-17

---

<a id="case-75"></a>
### Case 75: [Configure Kimi as a Codex Subagent](https://x.com/nauczymycieAI/status/2078181182701736132) (by [@nauczymycieAI](https://x.com/nauczymycieAI))

**Keep Codex responsible for orchestration and delegate frontend execution to a Kimi K3 OpenCode subagent with an explicit secret-handling boundary.**

nauczymycieAI publishes a three-stage setup: install and verify OpenCode, create a Kimi API key manually without pasting it into Codex, connect OpenCode to Kimi K3, and create a global Codex skill that routes frontend, UI, layout, presentation, and animation tasks to the subagent while Codex keeps logic and orchestration responsibility.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-75.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-75.jpg" alt="Case 75 source image 1" height="360"></a>

Type: Tutorial | Date: 2026-07-17

---

<a id="case-79"></a>
### Case 79: [Route Simple Coding Through ChatLLM](https://x.com/abacusai/status/2078022418661257411) (by [@abacusai](https://x.com/abacusai))

**Create a task router that sends simple coding to Kimi K3 while reserving harder coding and design work for different models.**

Abacus AI announces Kimi K3 availability in ChatLLM and gives an explicit routing example: simple coding to Kimi K3, hard coding to Fable 5, and design to GPT-5.6 Sol. The source says the same custom router can be used in ChatLLM, an Abacus AI agent, or Claude Code.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-79.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-79.jpg" alt="Case 79 source image 1" height="360"></a>

Type: Integration | Date: 2026-07-17

---


<a id="evaluation-limits"></a>
## 🧪 Evaluation & Limits

<a id="case-7"></a>
### Case 7: [Compare Frontend Design on the BridgeBench Lava Lamp Task](https://x.com/bridgemindai/status/2077868061953007908) (by [@bridgemindai](https://x.com/bridgemindai))

**Use the BridgeBench lava-lamp task as one bounded frontend-design comparison rather than a universal ranking.**

BridgeMind AI reports that Kimi K3 outperformed Fable 5 on its BridgeBench lava-lamp task and placed first in the cited arena. These are the publisher's reported comparison results.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-07.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-07-poster.jpg" alt="Case 7 source video poster" height="360"></a>

[Play case 7 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-07.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-8"></a>
### Case 8: [Benchmark Editorial-Voice Script Writing](https://x.com/Whats_AI/status/2077860441380798908) (by [@Whats_AI](https://x.com/Whats_AI))

**Measure editorial-voice fit, relative ranking, and per-script cost inside a clearly identified internal benchmark.**

Whats_AI reports early internal results of 2,840 Elo, first place on its board, and about $0.25 per script. Treat these as one organization's preliminary benchmark, not a general performance or price guarantee.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-08-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-08-01.jpg" alt="Case 8 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-16

---

<a id="case-10"></a>
### Case 10: [Compare Flappy-Game Design, Cost, and Difficulty](https://x.com/MrAhmadAwais/status/2077915347974557862) (by [@MrAhmadAwais](https://x.com/MrAhmadAwais))

**Record difficulty settings, cost, design, and gameplay features when comparing generated games.**

Command Code's internal Flappy benchmark reports different difficulty settings across models and lists Kimi K3 at $0.024, Fable 5 at $0.42, and GPT-5.6 Sol at $0.15. The unequal settings make this a bounded internal comparison.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-10.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-10-poster.jpg" alt="Case 10 source video poster" height="360"></a>

[Play case 10 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-10.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-12"></a>
### Case 12: [Compare Game Design With the Same Design Prompt](https://x.com/CommandCodeAI/status/2077921526213746948) (by [@CommandCodeAI](https://x.com/CommandCodeAI))

**Hold the design prompt constant and inspect pace, design sense, and gameplay feel separately.**

Command Code reports a same-prompt comparison of Kimi K3, GPT-5.6 Sol, and Fable 5. Its post says Kimi K3 performed well on design sense while the other two played too fast; this remains the publisher's evaluation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-12.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-12-poster.jpg" alt="Case 12 source video poster" height="360"></a>

[Play case 12 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-12.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-13"></a>
### Case 13: [Require Independent Review for Statistical Auditing](https://x.com/emollick/status/2077869293031624793) (by [@emollick](https://x.com/emollick))

**Pair model-generated statistical audits with independent expert or model review before relying on findings.**

Ethan Mollick reports that Kimi K3 Max misapplied statistics while auditing prior academic work and agrees with a separate critique. This negative example supports independent checking rather than unreviewed acceptance.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-13-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-13-01.jpg" alt="Case 13 source image 1" height="360"></a>

Type: Limit | Date: 2026-07-16

---

<a id="case-16"></a>
### Case 16: [Evaluate a Slow but Strong Frontend Run](https://x.com/Lentils80/status/2077387333154857151) (by [@Lentils80](https://x.com/Lentils80))

**Record completion time alongside output quality when testing a frontend task.**

The creator reports that a Kimi K3 frontend run took 35 minutes and describes the output as one of the best seen for that prompt. Both speed and quality judgments are a single user's observation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-16.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-16-poster.jpg" alt="Case 16 source video poster" height="360"></a>

[Play case 16 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-16.mp4)

Type: Evaluation | Date: 2026-07-15

---

<a id="case-20"></a>
### Case 20: [Test Murder-Mystery Writing for Foreshadowing Failures](https://x.com/emollick/status/2077951790868238616) (by [@emollick](https://x.com/emollick))

**Evaluate whether a generated mystery balances clues, obscurity, and foreshadowing.**

Ethan Mollick reports that Kimi K3 did not write a good murder mystery, making clues both too obvious and too obscure and failing at foreshadowing. He also notes that other models share this limitation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-01.jpg" alt="Case 20 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-02.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-02.png" alt="Case 20 source image 2" height="360"></a>

Type: Limit | Date: 2026-07-17

---

<a id="case-21"></a>
### Case 21: [Compare Millennium Falcon Modeling and Animation](https://x.com/gmi_cloud/status/2077903360263676090) (by [@gmi_cloud](https://x.com/gmi_cloud))

**Use matched style requests and effort settings to compare 3D modeling, animation, time, and cost.**

GMI Cloud reports comparing Kimi K3 and Fable 5 on pixel-style and original-style Millennium Falcon recreations at maximum effort. It says Kimi K3 took longer but cost about one-third in the first test and less than half in another; these are provider-reported results.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-21.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-21-poster.jpg" alt="Case 21 source video poster" height="360"></a>

[Play case 21 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-21.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-28"></a>
### Case 28: [Review a Collection of Ten Kimi K3 Projects](https://x.com/minchoi/status/2077957907857994006) (by [@minchoi](https://x.com/minchoi))

**Use a linked project roundup to discover concrete artifacts for separate verification.**

The author curates ten Kimi K3 examples with media, including a Game Boy Advance emulator. This record is a collection rather than a single reproducible workflow, so each linked example should be checked independently.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-28.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-28-poster.jpg" alt="Case 28 source video poster" height="360"></a>

[Play case 28 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-28.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-29"></a>
### Case 29: [Compare an Advanced Landing Page Across Four Models](https://x.com/doutorcaleb/status/2077904020471947773) (by [@doutorcaleb](https://x.com/doutorcaleb))

**Hold a landing-page request constant and inspect animation depth and completion across model outputs.**

The creator reports giving the same advanced landing-page prompt to Kimi K3, Fable, Grok, and GPT Terra, and judges Kimi K3 the strongest result. This is a self-reported comparison from one task.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-29.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-29-poster.jpg" alt="Case 29 source video poster" height="360"></a>

[Play case 29 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-29.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-30"></a>
### Case 30: [Benchmark Retro-Game Mechanics and Cost](https://x.com/adxtyahq/status/2077860500462055570) (by [@adxtyahq](https://x.com/adxtyahq))

**Compare gameplay, physics, mechanics, autonomous behavior, token use, and cost on the same retro-game tasks.**

The source reports same-prompt tests for Road Fighter, Battle City, and Q*bert and lists $0.28 for Kimi K3, $0.28 for GPT-5.6, and $0.54 for Opus 4.8. These are the publisher's benchmark figures.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-30.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-30-poster.jpg" alt="Case 30 source video poster" height="360"></a>

[Play case 30 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-30.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-31"></a>
### Case 31: [Compare Game Generation With Fable 5](https://x.com/higgsfield_ai/status/2077943629633712490) (by [@higgsfield_ai](https://x.com/higgsfield_ai))

**Use a side-by-side generated-game example as a narrow evaluation rather than a broad model verdict.**

Higgsfield presents a Kimi K3 versus Fable 5 game-generation comparison. The supplied record includes the comparison media but no prompt, scoring rubric, or detailed conditions.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-31.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-31-poster.jpg" alt="Case 31 source video poster" height="360"></a>

[Play case 31 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-31.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-34"></a>
### Case 34: [Compare Complex Frontend and Development Tasks With Opus 4.8](https://x.com/op7418/status/2077969583018066116) (by [@op7418](https://x.com/op7418))

**Use multiple complex coding tasks to identify wins and losses instead of declaring one model universally superior.**

The reviewer reports direct Kimi K3 versus Opus 4.8 tests and judges them roughly comparable on complex frontend and development work, with mixed outcomes. This remains one reviewer's assessment.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-34.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-34-poster.jpg" alt="Case 34 source video poster" height="360"></a>

[Play case 34 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-34.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-35"></a>
### Case 35: [Review Benchmarks and a Landing Page Test](https://x.com/adamuchigabriel/status/2077880433925120471) (by [@adamuchigabriel](https://x.com/adamuchigabriel))

**Combine benchmark context with a concrete landing-page generation test while keeping the two evidence types separate.**

The video presents benchmark discussion, a landing-page test, and frontend-design observations for Kimi K3. The supplied record does not provide the full test prompt or scoring rubric.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-35.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-35-poster.jpg" alt="Case 35 source video poster" height="360"></a>

[Play case 35 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-35.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-37"></a>
### Case 37: [Evaluate Induction Reasoning With Graph-to-Formula Tasks](https://x.com/s_batzoglou/status/2077884096307454119) (by [@s_batzoglou](https://x.com/s_batzoglou))

**Measure correctness, holdout behavior, and formula complexity on first-order induction tasks.**

The author reports benchmarking Kimi K3 and other models on the ICML INDUCTION task using 6 to 10 small graphs with 8 to 10 elements each to infer a first-order formula. The post says results were updated from earlier work; no new independent reproduction is claimed here.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-37-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-37-01.png" alt="Case 37 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-16

---

<a id="case-38"></a>
### Case 38: [Review Reported Games, Landing Pages, 3D Work, and Long Context](https://x.com/servasyy_ai/status/2077903775113834689) (by [@servasyy_ai](https://x.com/servasyy_ai))

**Use a multi-source roundup to compare concrete artifacts and note speed limitations alongside cost claims.**

The author summarizes reported Kimi K3 tests across games, landing pages, 3D generation, and long-context work, while concluding that it is worth trying but not yet a replacement for Fable 5. All figures are secondary reports within this roundup.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-38-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-38-01.jpg" alt="Case 38 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-40"></a>
### Case 40: [Audit a Complex Plan and Challenge Its Remedies](https://x.com/doodlestein/status/2077901883637665958) (by [@doodlestein](https://x.com/doodlestein))

**Use a second model to identify understated findings, incorrect remedies, and conclusions that should be rejected.**

The creator reports that Kimi K3 reviewed a heavily refined plan and found that severe issues were understated, about one-third of proposed remedies needed correction, and one finding was refuted. These are results from that specific audit.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-40-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-40-01.jpg" alt="Case 40 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-41"></a>
### Case 41: [Compare PPO-Style Reinforcement-Learning ASCII Diagrams](https://x.com/dejavucoder/status/2077872015856615541) (by [@dejavucoder](https://x.com/dejavucoder))

**Hold an ASCII-diagram prompt constant and compare how models represent the reinforcement-learning loop.**

The source supplies the prompt to draw a PPO-style reinforcement-learning loop in ASCII and shows Kimi K3 Max beside Fable 5 High. The judgment remains a visual comparison from one task.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-01.png" alt="Case 41 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-02.jpg" alt="Case 41 source image 2" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-42"></a>
### Case 42: [Model in Blender While Tracking Capacity Errors](https://x.com/Angaisb_/status/2077910845523214668) (by [@Angaisb_](https://x.com/Angaisb_))

**Evaluate partial Blender progress together with service reliability rather than judging only the artifact.**

The creator shows Blender modeling progress from Kimi K3 and also reports repeated capacity errors. The work is incomplete in the supplied source, so the partial result and reliability limitation should be considered together.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-42-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-42-01.jpg" alt="Case 42 source image 1" height="360"></a>

Type: Limit | Date: 2026-07-17

---

<a id="case-47"></a>
### Case 47: [Compare Flappy Bird Generation in an Arena](https://x.com/jun_song/status/2077396996865003739) (by [@jun_song](https://x.com/jun_song))

**Use an arena task to compare two generated Flappy Bird results while keeping the judgment task-specific.**

The creator reports an Arena comparison between Kimi K3 and Opus 4.8 on a Flappy Bird task and judges Kimi K3 significantly better. No full prompt or rubric is supplied in the record.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-47.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-47-poster.jpg" alt="Case 47 source video poster" height="360"></a>

[Play case 47 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-47.mp4)

Type: Evaluation | Date: 2026-07-15

---

<a id="case-52"></a>
### Case 52: [Solve a Bongard Visual Induction Problem With a Tool](https://x.com/IntuitMachine/status/2077885406528311561) (by [@IntuitMachine](https://x.com/IntuitMachine))

**Test whether tool use helps derive the visual rule in a Bongard reasoning task.**

The creator reports that Kimi K3 used a tool to solve a Bongard problem that Grok 4.5 and Muse Spark 1.1 did not solve in the same comparison. This is one user's task result, not a general reasoning benchmark.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-52-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-52-01.jpg" alt="Case 52 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-53"></a>
### Case 53: [Compare Frontend Taste and 3D Design With GPT-5.6 Sol](https://x.com/filicroval/status/2077736407506751952) (by [@filicroval](https://x.com/filicroval))

**Inspect features, visual taste, elegance, and 3D execution in a bounded frontend comparison.**

The creator compares Kimi K3 and GPT-5.6 Sol on frontend design and judges Kimi K3 stronger in visual taste, elegance, and 3D capability. The assessment is subjective and task-specific.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-53.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-53-poster.jpg" alt="Case 53 source video poster" height="360"></a>

[Play case 53 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-53.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-57"></a>
### Case 57: [Compare Website Generation Across Three Models](https://x.com/pengchujin/status/2077962916226298340) (by [@pengchujin](https://x.com/pengchujin))

**Use visible website outputs to compare Kimi K3, Fable 5, and GPT-5.6 Sol on one test.**

The creator presents a website-generation comparison among Kimi K3, Fable 5, and GPT-5.6 Sol. The supplied record does not expose the complete prompt or a scoring rubric.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-57.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-57-poster.jpg" alt="Case 57 source video poster" height="360"></a>

[Play case 57 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-57.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-59"></a>
### Case 59: [Compare Procedural 3D Game Generation and Cost](https://x.com/adxtyahq/status/2077958193511362856) (by [@adxtyahq](https://x.com/adxtyahq))

**Hold a prompt constant across models and inspect generated roulette, slot-machine, and pinball systems with per-run cost.**

The publisher reports a multi-model procedural 3D game comparison and lists costs including $0.71 for Kimi K3 and $0.30 for Grok 4.5. Treat all rankings and costs as results from that publisher's run.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-59.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-59-poster.jpg" alt="Case 59 source video poster" height="360"></a>

[Play case 59 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-59.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-69"></a>
### Case 69: [Compare 3D Arsenal Scene Detail and Lighting](https://x.com/hakki_alkan/status/2077887013332636032) (by [@hakki_alkan](https://x.com/hakki_alkan))

**Inspect object density, lighting, and scene detail in a bounded Kimi K3 versus Opus 4.8 comparison.**

The source reports that Kimi K3 produced a detailed arsenal scene with stocked shelves, boxes, and realistic lighting while Opus 4.8 produced a sparse room. This is a third-party comparison report, not an independent benchmark.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-69-poster.jpg" alt="Case 69 source video poster" height="360"></a>

[Play case 69 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-69.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-72"></a>
### Case 72: [Compare Frontends With Identical Arena Prompts](https://x.com/arena/status/2078240399517524365) (by [@arena](https://x.com/arena))

**Use identical prompts and side-by-side outputs to compare Kimi K3 with Fable 5 on frontend implementation instead of relying on one leaderboard number.**

Arena.ai publishes a head-to-head Frontend Code Arena comparison between Kimi K3 and Fable 5 using identical prompts. The video preserves both outputs, making the case useful for inspecting implementation and presentation differences while keeping the prompt condition fixed.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-72.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-72-poster.jpg" alt="Case 72 source video poster" height="360"></a>

[Play case 72 comparison video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-72.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-74"></a>
### Case 74: [Benchmark Kimi Code on Coding Agents](https://x.com/ArtificialAnlys/status/2078230240766345330) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Compare Kimi K3 across multiple coding-agent suites and per-task cost before treating a single frontend leaderboard as general coding-agent performance.**

Artificial Analysis reports Kimi K3 in Kimi Code CLI at 57 on its Coding Agent Index, tied for fifth overall. The post breaks the result into Terminal-Bench v2 at 84%, DeepSWE at 64%, and SWE-Atlas-QnA at 23%, with an average reported cost of $3.18 per task and named comparisons against other frontier models.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-74.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-74.jpg" alt="Case 74 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-17

---

<a id="case-76"></a>
### Case 76: [Compare Arena and Repair Harness Results](https://x.com/AlphaSignalAI/status/2078172629496746183) (by [@AlphaSignalAI](https://x.com/AlphaSignalAI))

**Use both frontend preference and repository-repair evaluations because Kimi K3 can rank first on one surface and last in a seven-model repair harness.**

AlphaSignal reports Kimi K3 at 1,679 and first place on Frontend Code Arena, then tests it on a coding-agent repair harness against six peers. In that separate harness Kimi completed 53 of 67 attempts, or 79%, and ranked seventh, illustrating how evaluation format changes the conclusion.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-76.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-76.jpg" alt="Case 76 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-17

---

<a id="case-80"></a>
### Case 80: [Benchmark Kimi K3 on Prinzbench](https://x.com/deredleritt3r/status/2078606700496773166) (by [@deredleritt3r](https://x.com/deredleritt3r))

**Use an independent benchmark update to compare Kimi K3 with open and frontier models across search, reasoning, and consistency.**

The author adds Kimi K3 to Prinzbench and reports an overall score of 47/99, above GLM-5.2 at 30/99 and near an older Gemini 3.1 Pro result at 50/99. The post highlights strong search performance, weaker logical reasoning, and higher inconsistency than comparable frontier models.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-80-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-80-01.png" alt="Case 80 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-18

---

<a id="case-85"></a>
### Case 85: [Compare ISS Digital Twin Generation](https://x.com/AIsaOneHQ/status/2078519527588200536) (by [@AIsaOneHQ](https://x.com/AIsaOneHQ))

**Use a same-prompt 3D modeling challenge to compare Kimi K3 and GPT-5.6 Sol on reconstruction, controls, labels, and visual detail.**

AIsaOneHQ reports a one-shot benchmark where both models had to reconstruct an interactive International Space Station digital twin without a prebuilt model, including Earth, orbital lighting, cinematic controls, labels, guided tours, exploded view, testing, and refinement. The post says Kimi K3 finished faster, cost less, and delivered stronger rendering in that run.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-85.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-85-poster.jpg" alt="Case 85 source video poster" height="360"></a>

[Play case 85 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-85.mp4)

Type: Benchmark | Date: 2026-07-18

---

<a id="case-89"></a>
### Case 89: [Review a WebGPU Forest World](https://x.com/stas_sorokin_/status/2078435840728908093) (by [@stas_sorokin_](https://x.com/stas_sorokin_))

**Evaluate Kimi K3 as a coding-agent brain on a long-horizon Three.js and WebGPU world build, including quality, speed, consistency, and edit rate.**

The creator reports a deep Kimi K3 coding-agent review using a dreamlike Three.js and WebGPU forest-lake world with living water, weather, wildlife, time-of-day changes, and cinematic cameras. The post says Kimi K3 produced very high quality, ran slower than a comparable GPT-5.6 Sol generation, kept consistency over a long horizon, and needed only one manual luminosity tweak.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-89.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-89-poster.jpg" alt="Case 89 source video poster" height="360"></a>

[Play case 89 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-89.mp4)

Type: Evaluation | Date: 2026-07-18

---

<a id="related-resources"></a>
## Related Resources

- [Kimi K3 model overview on EvoLink](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=landing_overview) — availability, model ID, context, and pricing
- [Kimi K3 OpenAI-compatible API documentation](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=docs_link) — Chat Completions endpoint and request format
- [Learn more about Kimi K3 on EvoLink](https://evolink.ai/blog/is-kimi-k3-available-on-evolink?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_article)
- [KimiK3.io](https://kimik3.io/)
- No installable EvoLink Kimi K3 skill was independently verified for this update

<a id="acknowledge"></a>
## 🙏 Acknowledge

This repository is possible because creators and practitioners shared Kimi K3 work publicly

Thanks to the source creators represented here:

[@ivanfioravanti](https://x.com/ivanfioravanti), [@TheAhmadOsman](https://x.com/TheAhmadOsman), [@HarshithLucky3](https://x.com/HarshithLucky3), [@chetaslua](https://x.com/chetaslua), [@abhinavflac](https://x.com/abhinavflac), [@bridgemindai](https://x.com/bridgemindai), [@Whats_AI](https://x.com/Whats_AI), [@chongdashu](https://x.com/chongdashu), [@MrAhmadAwais](https://x.com/MrAhmadAwais), [@bijanbowen](https://x.com/bijanbowen), [@CommandCodeAI](https://x.com/CommandCodeAI), [@emollick](https://x.com/emollick), [@nicky_sap](https://x.com/nicky_sap), [@Lentils80](https://x.com/Lentils80), [@scottstts](https://x.com/scottstts), [@aisearchio](https://x.com/aisearchio), [@gmi_cloud](https://x.com/gmi_cloud), [@karminski3](https://x.com/karminski3), [@VORTEX_Promos](https://x.com/VORTEX_Promos), [@rohanpaul_ai](https://x.com/rohanpaul_ai), [@mirochill](https://x.com/mirochill), [@aimlapi](https://x.com/aimlapi), [@minchoi](https://x.com/minchoi), [@doutorcaleb](https://x.com/doutorcaleb), [@adxtyahq](https://x.com/adxtyahq), [@higgsfield_ai](https://x.com/higgsfield_ai), [@AlicanKiraz0](https://x.com/AlicanKiraz0), [@1littlecoder](https://x.com/1littlecoder), [@op7418](https://x.com/op7418), [@adamuchigabriel](https://x.com/adamuchigabriel), [@s_batzoglou](https://x.com/s_batzoglou), [@servasyy_ai](https://x.com/servasyy_ai), [@filicroval](https://x.com/filicroval), [@doodlestein](https://x.com/doodlestein), [@dejavucoder](https://x.com/dejavucoder), [@Angaisb_](https://x.com/Angaisb_), [@AngryTomtweets](https://x.com/AngryTomtweets), [@Alezander907](https://x.com/Alezander907), [@teortaxesTex](https://x.com/teortaxesTex), [@jun_song](https://x.com/jun_song), [@ridark_eth](https://x.com/ridark_eth), [@naymur_dev](https://x.com/naymur_dev), [@tphuang](https://x.com/tphuang), [@TokenGremlin](https://x.com/TokenGremlin), [@IntuitMachine](https://x.com/IntuitMachine), [@wangfeng0315](https://x.com/wangfeng0315), [@twid](https://x.com/twid), [@pengchujin](https://x.com/pengchujin), [@aayushman2703](https://x.com/aayushman2703), [@goncalo_canhoto](https://x.com/goncalo_canhoto), [@LinearUncle](https://x.com/LinearUncle), [@gagarot200](https://x.com/gagarot200), [@MinLiBuilds](https://x.com/MinLiBuilds), [@izutorishima](https://x.com/izutorishima), [@X2worldtech](https://x.com/X2worldtech), [@Satvik_Pen](https://x.com/Satvik_Pen), [@hakki_alkan](https://x.com/hakki_alkan), [@BrianMRey](https://x.com/BrianMRey), [@ChrisGPT](https://x.com/ChrisGPT), [@arena](https://x.com/arena), [@MathiasHeide](https://x.com/MathiasHeide), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@nauczymycieAI](https://x.com/nauczymycieAI), [@AlphaSignalAI](https://x.com/AlphaSignalAI), [@Ananth7e](https://x.com/Ananth7e), [@viktoroddy](https://x.com/viktoroddy), [@abacusai](https://x.com/abacusai), [@deredleritt3r](https://x.com/deredleritt3r), [@fabriciocarraro](https://x.com/fabriciocarraro), [@startracker](https://x.com/startracker), [@mattwatkajtys](https://x.com/mattwatkajtys), [@AIsaOneHQ](https://x.com/AIsaOneHQ), [@MiaAI_lab](https://x.com/MiaAI_lab), [@hqmank](https://x.com/hqmank), [@prasenx](https://x.com/prasenx), [@stas_sorokin_](https://x.com/stas_sorokin_)

*We cannot guarantee that every case is attributed to the earliest original creator. If attribution or wording needs correction, please open a correction issue with a public source*

To propose another source-backed Kimi K3 case, open an issue or pull request and follow the contribution checklist
