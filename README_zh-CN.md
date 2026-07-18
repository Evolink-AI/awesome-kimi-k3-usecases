<div align="center">

<a href="https://evolink.ai/kimi-k3?utm_source=github&utm_medium=banner&utm_campaign=awesome-kimi-k3-usecases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/images/zh-v2.png" alt="带月面场景与 EvoLink 使用入口的简体中文 Kimi K3 banner" width="760"></a>

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

# Kimi K3 精选使用案例

## 🍌 简介

欢迎来到 Kimi K3 高信号使用案例库

**我们收录有公开来源支持的游戏、3D 场景、动态设计、集成、评估与实际限制**

本案例库收录指定来源中的全部 70 个高置信案例，排除 31 个中等置信案例，并保留广泛的使用场景覆盖

[EvoLink](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=introduction_cta)

## 📊 概览

- 70 个来自创作者和从业者的高置信案例，未遗漏任何高置信条目
- 覆盖互动游戏、3D、前端与动态设计、编程、研究、评估、可视化和代理限制
- 每个案例保留来源、作者、类型、日期和 prompt 边界
- 不把个人观察包装成 benchmark

> [!NOTE]
> 本案例库优先采用具体证据，不补写未公开的 prompt 或配置步骤

**1. [查看 EvoLink 上的 Kimi K3 详情与价格](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-kimi-k3-usecases&utm_content=model_link) · 2. [创建或管理 EvoLink API 密钥](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-kimi-k3-usecases&utm_content=api_key) · 3. [查看 EvoLink Kimi K3 API 文档](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=first_run)**

## 📑 目录

| Section | Cases |
|---|---|
| [互动游戏与 3D](#games-3d) | 22 |
| [前端与动态设计](#frontend-motion) | 15 |
| [编程与集成](#coding-integrations) | 8 |
| [评估与限制](#evaluation-limits) | 25 |
| [相关资源](#related-resources) | 相关资源 |
| [快速开始](#quick-api-access) | 快速开始 |
| [致谢](#acknowledge) | 致谢与更正 |

| Case | Category | What it shows | Type |
|---|---|---|---|
| [用一个 prompt 构建 voxel pod racer](#case-1) | 互动游戏与 3D | 从简短场景概念做出竞速原型，再确定下一轮改进范围 | Demo |
| [用相同 prompt 比较 Frogger](#case-2) | 互动游戏与 3D | 固定 prompt 以检查不同模型的输出差异 | Evaluation |
| [生成 Frogger 与游戏录屏](#case-3) | 互动游戏与 3D | 分别用一次生成测试游戏与录屏流程 | Demo |
| [用 Three.js 制作航空母舰原型](#case-4) | 互动游戏与 3D | 以具体起降场景测试交互式 3D 生成 | Demo |
| [创建可交互的动态前端](#case-5) | 前端与动态设计 | 制作暂停动画后仍可交互的动态图形 | Demo |
| [制作同步的动态广告](#case-6) | 前端与动态设计 | 检查音乐、效果与动作是否同步 | Demo |
| [在 BridgeBench 熔岩灯任务上比较前端设计](#case-7) | 评估与限制 | 将 BridgeBench 熔岩灯任务视为一次有边界的前端设计比较，而非通用排名 | Benchmark |
| [评测编辑语调脚本写作](#case-8) | 评估与限制 | 在明确标识的内部评测中衡量编辑语调契合度、相对排名与单篇脚本成本 | Benchmark |
| [使用代理工具构建《纸片马力欧》风格游戏](#case-9) | 互动游戏与 3D | 将 Kimi K3 与代理框架及素材工具结合，同时制作 2D 与 3D 游戏元素 | Demo |
| [比较 Flappy 游戏的设计、成本与难度](#case-10) | 评估与限制 | 比较生成游戏时记录难度设置、成本、设计和玩法特征 | Benchmark |
| [生成地铁第一人称射击游戏](#case-11) | 互动游戏与 3D | 用具体的地铁场景检查生成的第一人称射击游戏结果 | Demo |
| [用相同设计 prompt 比较游戏设计](#case-12) | 评估与限制 | 固定设计 prompt，分别检查节奏、设计感与玩法体验 | Benchmark |
| [统计审计必须经过独立复核](#case-13) | 评估与限制 | 在依赖模型生成的统计审计结论前，先由独立专家或其他模型复核 | Limit |
| [完全使用代码创作动态设计](#case-14) | 前端与动态设计 | 测试一次性编程工作流能否在没有辅助生成工具的情况下产出动态设计 | Demo |
| [研究人物并构建动态个人网站](#case-15) | 前端与动态设计 | 给出宽泛的个人网站需求，再检查模型的研究、规划、迭代与浏览器验证过程 | Tutorial |
| [评估速度慢但效果强的前端生成](#case-16) | 评估与限制 | 测试前端任务时同时记录完成时间与输出质量 | Evaluation |
| [生成黑洞模拟](#case-17) | 前端与动态设计 | 通过科学可视化任务检查生成的黑洞模拟 | Demo |
| [构建运行 macOS 的虚拟 MacBook](#case-18) | 编程与集成 | 将 Three.js 硬件渲染与可交互的浏览器操作系统模拟结合 | Demo |
| [使用 Blender MCP 建模 V8 发动机](#case-19) | 互动游戏与 3D | 使用 Blender MCP 和单次请求生成细致的机械 3D 模型 | Integration |
| [测试悬疑写作中的伏笔失误](#case-20) | 评估与限制 | 评估生成的悬疑故事能否平衡线索、隐蔽性与伏笔 | Limit |
| [比较千年隼号的建模与动画](#case-21) | 评估与限制 | 用匹配的风格请求与工作强度设置比较 3D 建模、动画、时间与成本 | Benchmark |
| [测试复杂前端建模、粒子与着色器](#case-22) | 前端与动态设计 | 使用公开前端 prompt，一次检查建模精度、粒子效果与内联着色器生成 | Demo |
| [用一张参考图构建可玩战斗竞技场](#case-23) | 互动游戏与 3D | 使用单一参考测试一次生成完整可玩竞技场 | Demo |
| [用 HTML 文件构建三款自动游玩的复古游戏](#case-24) | 互动游戏与 3D | 要求在独立 HTML 游戏文件中包含图形、敌人、规则与自动游玩 | Benchmark |
| [构建从 DSL 到 PTX 的 GPU 编译器](#case-25) | 编程与集成 | 用端到端编译器任务覆盖 DSL、编译过程、PTX 生成与 Tensor Core 路径 | Demo |
| [一次生成程序化音乐工具](#case-26) | 前端与动态设计 | 测试一次生成交互式程序化音乐生成器，并谨慎比较可见结果 | Demo |
| [一次构建变色龙捉迷藏游戏](#case-27) | 互动游戏与 3D | 生成包含颜色匹配、程序化区域、声音和多轮计分的单文件游戏 | Benchmark |
| [回顾十个 Kimi K3 项目合集](#case-28) | 评估与限制 | 通过带链接的项目合集发现可供分别验证的具体产物 | Evaluation |
| [在四款模型间比较高级落地页](#case-29) | 评估与限制 | 固定落地页请求，检查不同模型输出的动画深度与完成度 | Evaluation |
| [评测复古游戏机制与成本](#case-30) | 评估与限制 | 在相同复古游戏任务上比较玩法、物理、机制、自动行为、token 用量与成本 | Benchmark |
| [与 Fable 5 比较游戏生成](#case-31) | 评估与限制 | 将并列展示的生成游戏视为有限评估，而非宽泛的模型结论 | Evaluation |
| [在 WebGL2 中构建实时黑洞光线追踪器](#case-32) | 编程与集成 | 测试用一个 prompt 在单个 HTML 文件中生成原生 WebGL2 测地线光线追踪器 | Benchmark |
| [用两张图片创建 Three.js 产品页](#case-33) | 前端与动态设计 | 使用两张参考图和明确的 Three.js 要求生成产品展示 | Demo |
| [与 Opus 4.8 比较复杂前端和开发任务](#case-34) | 评估与限制 | 通过多项复杂编程任务识别胜负，而非宣称某一模型普遍更优 | Evaluation |
| [评述 benchmark 与落地页测试](#case-35) | 评估与限制 | 将 benchmark 背景与具体落地页生成测试结合，同时区分两类证据 | Evaluation |
| [使用代理工具链构建 2.5D《纸片马力欧》风格游戏](#case-36) | 互动游戏与 3D | 结合 Kimi K3、Grok Build 或 Claude Code 与 Spriterrific，组装 2.5D 游戏工作流 | Tutorial |
| [用图到公式任务评估归纳推理](#case-37) | 评估与限制 | 在一阶归纳任务上衡量正确率、留出集表现与公式复杂度 | Benchmark |
| [回顾已报告的游戏、落地页、3D 工作和长上下文表现](#case-38) | 评估与限制 | 通过多来源汇总比较具体产物，并在成本说法之外注明速度限制 | Evaluation |
| [发明奢华面包切割器及其产品页](#case-39) | 前端与动态设计 | 在一个设计产物中结合产品创意、爆炸图、演示与落地页 | Demo |
| [审计复杂计划并质疑补救措施](#case-40) | 评估与限制 | 使用第二个模型找出被淡化的问题、错误的补救措施和应被否定的结论 | Evaluation |
| [比较 PPO 风格强化学习 ASCII 图](#case-41) | 评估与限制 | 固定 ASCII 图 prompt，比较模型如何表示强化学习循环 | Evaluation |
| [在 Blender 建模时跟踪容量错误](#case-42) | 评估与限制 | 将 Blender 的阶段性进展与服务可靠性一起评估，而非只判断产物 | Limit |
| [构建浏览器 3D 武侠角色扮演游戏](#case-43) | 互动游戏与 3D | 结合近战、任务、背包、天气、室内探索、Blender 环境制作与素材改造 | Demo |
| [构建浏览器多人《我的世界》风格游戏](#case-44) | 互动游戏与 3D | 在限定时间与成本的运行中制作可在线游玩的多人浏览器游戏 | Demo |
| [生成十秒递归鹈鹕 GIF](#case-45) | 前端与动态设计 | 用完整指定的循环动画需求检查 GIF 的叙事连续性与递归效果 | Demo |
| [围绕 mGBA WASM 构建 Game Boy Advance 模拟器](#case-46) | 编程与集成 | 整合获许可的 3D 模型与真实模拟器核心，再递归改进界面与游戏体验 | Integration |
| [在竞技场比较 Flappy Bird 生成](#case-47) | 评估与限制 | 通过竞技场任务比较两个 Flappy Bird 生成结果，同时将判断限定在该任务 | Evaluation |
| [复刻分屏合作浏览器游戏](#case-48) | 互动游戏与 3D | 用一个请求生成浏览器分屏合作与实时环境互动 | Demo |
| [使用 Command Code 设计模式生成可玩游戏](#case-49) | 互动游戏与 3D | 使用 Command Code 的 design 命令一次构建游戏，并记录结果是否可玩 | Demo |
| [使用中文来源研究多个主题](#case-50) | 编程与集成 | 通过长时间研究任务比较不同代际模型的详尽程度与延迟 | Evaluation |
| [组装完整统一的武侠浏览器角色扮演游戏](#case-51) | 互动游戏与 3D | 在一个游戏中整合移动、战斗、任务、背包、天气、探索与 3D 环境制作 | Demo |
| [借助工具解决 Bongard 视觉归纳问题](#case-52) | 评估与限制 | 测试工具使用是否有助于推导 Bongard 推理任务中的视觉规则 | Evaluation |
| [与 GPT-5.6 Sol 比较前端审美和 3D 设计](#case-53) | 评估与限制 | 在有边界的前端比较中检查功能、视觉审美、优雅程度与 3D 执行 | Evaluation |
| [构建可玩的《空洞骑士》跨界游戏](#case-54) | 互动游戏与 3D | 使用现有游戏素材制作骑士与 Kimi 对战的可玩游戏 | Demo |
| [生成 BMW M4 CS 侧视图 SVG](#case-55) | 前端与动态设计 | 通过指定车型与视角检查矢量插画输出 | Demo |
| [在浏览器中克隆带可用应用的 macOS](#case-56) | 编程与集成 | 构建包含音乐、浏览器与电子邮件应用的浏览器操作系统模拟 | Demo |
| [比较三款模型的网站生成](#case-57) | 评估与限制 | 通过可见的网站输出比较 Kimi K3、Fable 5 与 GPT-5.6 Sol 在一次测试中的表现 | Evaluation |
| [通过截图反馈复刻卡冈图雅](#case-58) | 前端与动态设计 | 反复将截图作为观察结果，用于诊断并改进科学可视化 | Tutorial |
| [比较程序化 3D 游戏生成与成本](#case-59) | 评估与限制 | 在模型间固定 prompt，检查生成的轮盘、老虎机与弹球系统及单次运行成本 | Benchmark |
| [一次构建《糖豆人》风格 3D 浏览器游戏](#case-60) | 互动游戏与 3D | 用一次请求生成可玩的 3D 障碍游戏，并开放项目供检查 | Demo |
| [构建并自测末日里斯本第一人称射击游戏](#case-61) | 互动游戏与 3D | 使用单 prompt 最大工作强度运行，在交付可玩 FPS 前测试、截图并迭代 | Demo |
| [构建 FaceTime 可用的 macOS 模拟](#case-62) | 编程与集成 | 使用虚拟操作系统任务测试生成的应用交互是否真正可用 | Demo |
| [用简单请求生成《动物森友会》风格游戏](#case-63) | 互动游戏与 3D | 使用最小化游戏需求检查可玩性、玩法循环与视差效果 | Demo |
| [添加双任务前端效果比较器](#case-64) | 编程与集成 | 构建可选择两个已完成任务、并列显示且同步视图与交互的工具 | Tutorial |
| [用一句话需求生成马力欧风格游戏](#case-65) | 互动游戏与 3D | 使用最小化的一次请求检查可玩性、关卡设计、像素美术与视差 | Demo |
| [用 62 张截图改进黑洞可视化](#case-66) | 前端与动态设计 | 通过截图反馈循环，在多次迭代中读取、诊断并修正视觉模拟 | Tutorial |
| [构建可运行的僵尸第一人称射击游戏](#case-67) | 互动游戏与 3D | 以具体的僵尸射击目标检查完整可玩的 FPS 产物 | Demo |
| [制作后训练营销 PDF](#case-68) | 前端与动态设计 | 使用明确的产品名称与交付格式生成营销文档 | Demo |
| [比较 3D 军械库场景细节与照明](#case-69) | 评估与限制 | 在有边界的 Kimi K3 与 Opus 4.8 比较中检查物体密度、照明与场景细节 | Evaluation |
| [用一个 prompt 创建用户界面](#case-70) | 前端与动态设计 | 使用单次请求生成并检查完整 UI 设计 | Demo |

<a id="games-3d"></a>
## 🎮 互动游戏与 3D

<a id="case-1"></a>
### Case 1: [用一个 prompt 构建 voxel pod racer](https://x.com/ivanfioravanti/status/2077763009657627055) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**从简短场景概念做出竞速原型，再确定下一轮改进范围**

创作者表示 Kimi K3 用一个公开 prompt 产出初版，下一版将增加更多赛车、终点线与细节检查

**Prompt:**

```text
Voxel star wars pod-racers run
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01-poster.jpg" alt="Case 1 source video poster" height="360"></a>

[Play case 1 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-2"></a>
### Case 2: [用相同 prompt 比较 Frogger](https://x.com/ivanfioravanti/status/2077754781964054825) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**固定 prompt 以检查不同模型的输出差异**

创作者用 Kimi K3 版本做相同 prompt 比较，但来源没有公开 prompt 内容或评分规则

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02-poster.jpg" alt="Case 2 source video poster" height="360"></a>

[Play case 2 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-3"></a>
### Case 3: [生成 Frogger 与游戏录屏](https://x.com/TheAhmadOsman/status/2077776567292338285) (by [@TheAhmadOsman](https://x.com/TheAhmadOsman))

**分别用一次生成测试游戏与录屏流程**

创作者表示游戏与录屏流程各由一次生成完成，但没有公开完整 prompt

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03-poster.jpg" alt="Case 3 source video poster" height="360"></a>

[Play case 3 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-4"></a>
### Case 4: [用 Three.js 制作航空母舰原型](https://x.com/HarshithLucky3/status/2077753222018814360) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**以具体起降场景测试交互式 3D 生成**

创作者展示尼米兹级航空母舰上的战机起飞与回收，并对 3D 生成给出正面评价

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04-poster.jpg" alt="Case 4 source video poster" height="360"></a>

[Play case 4 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-9"></a>
### Case 9: [使用代理工具构建《纸片马力欧》风格游戏](https://x.com/chongdashu/status/2077886028866531655) (by [@chongdashu](https://x.com/chongdashu))

**将 Kimi K3 与代理框架及素材工具结合，同时制作 2D 与 3D 游戏元素**

创作者称在《纸片马力欧》风格游戏中使用 Kimi K3、Grok Build、用于 2D 素材的 Spriterrific 及用于 3D 素材的 geometry，来源展示了工具与 skill 的使用，但没有公开可复用的完整 prompt

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-09.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-09-poster.jpg" alt="Case 9 source video poster" height="360"></a>

[Play case 9 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-09.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-11"></a>
### Case 11: [生成地铁第一人称射击游戏](https://x.com/bijanbowen/status/2077881805751873997) (by [@bijanbowen](https://x.com/bijanbowen))

**用具体的地铁场景检查生成的第一人称射击游戏结果**

创作者展示了一款归因于 Kimi K3 的地铁 FPS，并明确表示不确定其网红身份是否影响结果，来源未提供 prompt 或可复现工作流

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-11.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-11-poster.jpg" alt="Case 11 source video poster" height="360"></a>

[Play case 11 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-11.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-19"></a>
### Case 19: [使用 Blender MCP 建模 V8 发动机](https://x.com/aisearchio/status/2077962156147146925) (by [@aisearchio](https://x.com/aisearchio))

**使用 Blender MCP 和单次请求生成细致的机械 3D 模型**

评测者称 Kimi K3 通过一个 prompt 和 Blender MCP 生成了完整的 V8 发动机，帖子链接了更完整的评测，但所提供记录未公开完整 prompt

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-19.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-19-poster.jpg" alt="Case 19 source video poster" height="360"></a>

[Play case 19 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-19.mp4)

Type: Integration | Date: 2026-07-17

---

<a id="case-23"></a>
### Case 23: [用一张参考图构建可玩战斗竞技场](https://x.com/VORTEX_Promos/status/2077879705378730074) (by [@VORTEX_Promos](https://x.com/VORTEX_Promos))

**使用单一参考测试一次生成完整可玩竞技场**

创作者称 Kimi K3 根据一张参考图一次生成了可玩的战斗竞技场，帖子还包含另一项榜单说法，但具体 use case 是已展示的竞技场产物

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23-poster.jpg" alt="Case 23 source video poster" height="360"></a>

[Play case 23 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23-01.jpg" alt="Case 23 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-24"></a>
### Case 24: [用 HTML 文件构建三款自动游玩的复古游戏](https://x.com/rohanpaul_ai/status/2077889084761206860) (by [@rohanpaul_ai](https://x.com/rohanpaul_ai))

**要求在独立 HTML 游戏文件中包含图形、敌人、规则与自动游玩**

来源报告了一项 Atomic Chat 比较，模型将 Road Fighter、Battle City 与 Q*bert 制作为自动游玩的 HTML 文件，其成本与质量比较由发布方报告，未在此独立复现

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-24.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-24-poster.jpg" alt="Case 24 source video poster" height="360"></a>

[Play case 24 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-24.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-27"></a>
### Case 27: [一次构建变色龙捉迷藏游戏](https://x.com/aimlapi/status/2077898742179459274) (by [@aimlapi](https://x.com/aimlapi))

**生成包含颜色匹配、程序化区域、声音和多轮计分的单文件游戏**

AIMLAPI 报告了同 prompt 的一次性捉迷藏游戏比较，并列出 Kimi K3 成本 $3.11、Fable 5 成本 $12.23，功能与成本说法均为服务商报告的结果

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-27.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-27-poster.jpg" alt="Case 27 source video poster" height="360"></a>

[Play case 27 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-27.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-36"></a>
### Case 36: [使用代理工具链构建 2.5D《纸片马力欧》风格游戏](https://x.com/chongdashu/status/2077981621223837739) (by [@chongdashu](https://x.com/chongdashu))

**结合 Kimi K3、Grok Build 或 Claude Code 与 Spriterrific，组装 2.5D 游戏工作流**

创作者提供了使用 Grok Build 与 Kimi K3 的完整演示，并展示用 Spriterrific 生成精灵图，来源说明了所用工具，但没有提供可复用的完整 prompt

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-36.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-36-poster.jpg" alt="Case 36 source video poster" height="360"></a>

[Play case 36 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-36.mp4)

Type: Tutorial | Date: 2026-07-17

---

<a id="case-43"></a>
### Case 43: [构建浏览器 3D 武侠角色扮演游戏](https://x.com/AngryTomtweets/status/2077868163136450619) (by [@AngryTomtweets](https://x.com/AngryTomtweets))

**结合近战、任务、背包、天气、室内探索、Blender 环境制作与素材改造**

来源称 Kimi K3 浏览器 RPG 包含近战、任务、背包、动态天气和可探索室内空间，以及 Blender 建模、碰撞改进、PBR 重贴图与开放素材改造

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-43.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-43-poster.jpg" alt="Case 43 source video poster" height="360"></a>

[Play case 43 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-43.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-44"></a>
### Case 44: [构建浏览器多人《我的世界》风格游戏](https://x.com/Alezander907/status/2077926014710407407) (by [@Alezander907](https://x.com/Alezander907))

**在限定时间与成本的运行中制作可在线游玩的多人浏览器游戏**

创作者称 Kimi K3 在一小时内以 $6.57 的成本构建了可在浏览器游玩的多人《我的世界》风格游戏，这些均为单个产物的自述运行数据

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-44.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-44-poster.jpg" alt="Case 44 source video poster" height="360"></a>

[Play case 44 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-44.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-48"></a>
### Case 48: [复刻分屏合作浏览器游戏](https://x.com/ridark_eth/status/2077882889803378969) (by [@ridark_eth](https://x.com/ridark_eth))

**用一个请求生成浏览器分屏合作与实时环境互动**

创作者称 Kimi K3 用一个 prompt 制作了受《双人成行》启发的浏览器游戏，Mario 与 Luigi 可分屏游玩并与环境实时互动

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-48.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-48-poster.jpg" alt="Case 48 source video poster" height="360"></a>

[Play case 48 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-48.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-49"></a>
### Case 49: [使用 Command Code 设计模式生成可玩游戏](https://x.com/naymur_dev/status/2077873562661335207) (by [@naymur_dev](https://x.com/naymur_dev))

**使用 Command Code 的 design 命令一次构建游戏，并记录结果是否可玩**

创作者称使用 Command Code 设计模式进行一次生成比较，Kimi K3 运行以 $0.038 生成了可玩的游戏，这一成本与质量结果为自述数据

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-49.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-49-poster.jpg" alt="Case 49 source video poster" height="360"></a>

[Play case 49 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-49.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-51"></a>
### Case 51: [组装完整统一的武侠浏览器角色扮演游戏](https://x.com/TokenGremlin/status/2077855657068310620) (by [@TokenGremlin](https://x.com/TokenGremlin))

**在一个游戏中整合移动、战斗、任务、背包、天气、探索与 3D 环境制作**

来源称一款 Kimi K3 武侠风浏览器 RPG 结合了近战、任务、背包、动态天气、可探索室内空间与完整统一的 3D 游戏结构

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-51.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-51-poster.jpg" alt="Case 51 source video poster" height="360"></a>

[Play case 51 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-51.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-54"></a>
### Case 54: [构建可玩的《空洞骑士》跨界游戏](https://x.com/wangfeng0315/status/2077933531200991583) (by [@wangfeng0315](https://x.com/wangfeng0315))

**使用现有游戏素材制作骑士与 Kimi 对战的可玩游戏**

创作者自称在 Kimi 工作，并表示使用《空洞骑士》素材制作了骑士与 Kimi 对战的游戏，同时提供公开试玩链接，归因与评价应考虑该关联关系

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54-poster.jpg" alt="Case 54 source video poster" height="360"></a>

[Play case 54 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54-01.jpg" alt="Case 54 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-17

---

<a id="case-60"></a>
### Case 60: [一次构建《糖豆人》风格 3D 浏览器游戏](https://x.com/aayushman2703/status/2077857886441783526) (by [@aayushman2703](https://x.com/aayushman2703))

**用一次请求生成可玩的 3D 障碍游戏，并开放项目供检查**

创作者称 Kimi K3 一次构建了《糖豆人》风格浏览器游戏，并表示来源中链接了 prompt 与 GitHub 项目，本记录未复现该 prompt

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-60.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-60-poster.jpg" alt="Case 60 source video poster" height="360"></a>

[Play case 60 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-60.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-61"></a>
### Case 61: [构建并自测末日里斯本第一人称射击游戏](https://x.com/goncalo_canhoto/status/2077863166655037668) (by [@goncalo_canhoto](https://x.com/goncalo_canhoto))

**使用单 prompt 最大工作强度运行，在交付可玩 FPS 前测试、截图并迭代**

创作者称 Kimi K3 在约一小时后制作出可玩的末日里斯本浏览器 FPS，期间反复测试、截图与迭代，这些时间和流程细节均为自述

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-61-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-61-01.jpg" alt="Case 61 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-63"></a>
### Case 63: [用简单请求生成《动物森友会》风格游戏](https://x.com/gagarot200/status/2077949230287896830) (by [@gagarot200](https://x.com/gagarot200))

**使用最小化游戏需求检查可玩性、玩法循环与视差效果**

创作者称 Kimi K3 根据一个非常简单的 prompt 生成了完整可玩的《动物森友会》风格游戏，包含玩法循环与视差效果，所提供记录中没有完整措辞

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-63.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-63-poster.jpg" alt="Case 63 source video poster" height="360"></a>

[Play case 63 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-63.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-65"></a>
### Case 65: [用一句话需求生成马力欧风格游戏](https://x.com/izutorishima/status/2077939370154475992) (by [@izutorishima](https://x.com/izutorishima))

**使用最小化的一次请求检查可玩性、关卡设计、像素美术与视差**

创作者称 Kimi K3 根据单句需求生成了没有明显 bug 的可运行马力欧风格游戏，包含关卡结构与视差，同一报告也批评了音乐和图像质量

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-01.jpg" alt="Case 65 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-02.jpg" alt="Case 65 source image 2" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-03.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-03.jpg" alt="Case 65 source image 3" height="360"></a>

Type: Demo | Date: 2026-07-17

---

<a id="case-67"></a>
### Case 67: [构建可运行的僵尸第一人称射击游戏](https://x.com/X2worldtech/status/2077902793449296203) (by [@X2worldtech](https://x.com/X2worldtech))

**以具体的僵尸射击目标检查完整可玩的 FPS 产物**

来源展示了一款归因于 Kimi K3 的完整可运行僵尸 FPS，但未提供 prompt、实现细节或外部玩法评价

> [!WARNING]
> The original source permalink returned HTTP 404 during the 2026-07-17 audit. Attribution and evidence are preserved from the supplied high-confidence source package.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-67.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-67-poster.jpg" alt="Case 67 source video poster" height="360"></a>

[Play case 67 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-67.mp4)

Type: Demo | Date: 2026-07-16

---


<a id="frontend-motion"></a>
## 🎨 前端与动态设计

<a id="case-5"></a>
### Case 5: [创建可交互的动态前端](https://x.com/chetaslua/status/2077749371144442022) (by [@chetaslua](https://x.com/chetaslua))

**制作暂停动画后仍可交互的动态图形**

创作者表示制作耗时 42 分钟、一次生成、只用简单代码，没有 harness、MCP 或 skill

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05-poster.jpg" alt="Case 5 source video poster" height="360"></a>

[Play case 5 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-6"></a>
### Case 6: [制作同步的动态广告](https://x.com/abhinavflac/status/2077760297918484667) (by [@abhinavflac](https://x.com/abhinavflac))

**检查音乐、效果与动作是否同步**

创作者表示用纯 prompt 一次产出 Spotify 风格广告，但没有公开完整 prompt

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06-poster.jpg" alt="Case 6 source video poster" height="360"></a>

[Play case 6 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-14"></a>
### Case 14: [完全使用代码创作动态设计](https://x.com/chetaslua/status/2077952938564354503) (by [@chetaslua](https://x.com/chetaslua))

**测试一次性编程工作流能否在没有辅助生成工具的情况下产出动态设计**

创作者报告称，Kimi K3 一次生成了完全由代码制作的动态设计，未使用 MCP、skill、工具、视频生成或特殊 prompt，但未提供完整 prompt

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-14.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-14-poster.jpg" alt="Case 14 source video poster" height="360"></a>

[Play case 14 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-14.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-15"></a>
### Case 15: [研究人物并构建动态个人网站](https://x.com/nicky_sap/status/2077857190707429411) (by [@nicky_sap](https://x.com/nicky_sap))

**给出宽泛的个人网站需求，再检查模型的研究、规划、迭代与浏览器验证过程**

创作者称 Kimi K3 研究了 Nick Saponaro，并根据宽泛请求制作了动态个人网站，过程包括规划、测试、迭代和浏览器检查，结果属于自述式工作流展示

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-15.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-15-poster.jpg" alt="Case 15 source video poster" height="360"></a>

[Play case 15 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-15.mp4)

Type: Tutorial | Date: 2026-07-16

---

<a id="case-17"></a>
### Case 17: [生成黑洞模拟](https://x.com/chetaslua/status/2077961850352971796) (by [@chetaslua](https://x.com/chetaslua))

**通过科学可视化任务检查生成的黑洞模拟**

创作者展示了归因于 Kimi K3 的黑洞模拟，并称其为自己见过的最佳结果，来源有可见产物，但没有 prompt、评分标准或独立验证

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-17.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-17-poster.jpg" alt="Case 17 source video poster" height="360"></a>

[Play case 17 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-17.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-22"></a>
### Case 22: [测试复杂前端建模、粒子与着色器](https://x.com/karminski3/status/2077889959223337099) (by [@karminski3](https://x.com/karminski3))

**使用公开前端 prompt，一次检查建模精度、粒子效果与内联着色器生成**

创作者称 Kimi K3 一次生成的前端结果涵盖精确建模、粒子效果与复杂内联着色器代码，并表示测试 prompt 已在链接来源中公开

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-22.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-22-poster.jpg" alt="Case 22 source video poster" height="360"></a>

[Play case 22 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-22.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-26"></a>
### Case 26: [一次生成程序化音乐工具](https://x.com/mirochill/status/2077723551331758478) (by [@mirochill](https://x.com/mirochill))

**测试一次生成交互式程序化音乐生成器，并谨慎比较可见结果**

创作者称 Kimi K3 一次生成了程序化音乐工具，并认为结果优于 Fable 5 和 GPT-5.6 Sol，这是创作者自己的测试集，而非标准化评测

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-26-poster.jpg" alt="Case 26 source video poster" height="360"></a>

[Play case 26 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-26.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-33"></a>
### Case 33: [用两张图片创建 Three.js 产品页](https://x.com/1littlecoder/status/2077890296806031665) (by [@1littlecoder](https://x.com/1littlecoder))

**使用两张参考图和明确的 Three.js 要求生成产品展示**

创作者称 Kimi K3 根据两张图片设计了产品页，并生成明确要求的 Three.js 版本，未提供更多 prompt 或实现细节

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-33.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-33-poster.jpg" alt="Case 33 source video poster" height="360"></a>

[Play case 33 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-33.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-39"></a>
### Case 39: [发明奢华面包切割器及其产品页](https://x.com/filicroval/status/2077871090731221438) (by [@filicroval](https://x.com/filicroval))

**在一个设计产物中结合产品创意、爆炸图、演示与落地页**

创作者称 Kimi K3 发明了一款断头台式面包切割器，将其包装为奢侈品，并制作了包含爆炸图和演示的落地页

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-39.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-39-poster.jpg" alt="Case 39 source video poster" height="360"></a>

[Play case 39 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-39.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-45"></a>
### Case 45: [生成十秒递归鹈鹕 GIF](https://x.com/1littlecoder/status/2077880380900937865) (by [@1littlecoder](https://x.com/1littlecoder))

**用完整指定的循环动画需求检查 GIF 的叙事连续性与递归效果**

来源包含一个十秒循环 GIF prompt，内容为鹈鹕骑自行车，镜头放大时它通过短信收到同一段视频，创作者展示了 Kimi K3 生成的动画

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-45.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-45-poster.jpg" alt="Case 45 source video poster" height="360"></a>

[Play case 45 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-45.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-55"></a>
### Case 55: [生成 BMW M4 CS 侧视图 SVG](https://x.com/HarshithLucky3/status/2077765821380886942) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**通过指定车型与视角检查矢量插画输出**

创作者展示了归因于 Kimi K3 Max 的 BMW M4 CS 侧视图 SVG，所提供来源包含产物，但没有 prompt 或制作步骤

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-55-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-55-01.jpg" alt="Case 55 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-58"></a>
### Case 58: [通过截图反馈复刻卡冈图雅](https://x.com/AngryTomtweets/status/2077868981659324444) (by [@AngryTomtweets](https://x.com/AngryTomtweets))

**反复将截图作为观察结果，用于诊断并改进科学可视化**

来源称 Kimi K3 通过 62 张自我截图复刻了《星际穿越》中的卡冈图雅，每次读取结果、诊断问题并迭代采取行动

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-58.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-58-poster.jpg" alt="Case 58 source video poster" height="360"></a>

[Play case 58 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-58.mp4)

Type: Tutorial | Date: 2026-07-16

---

<a id="case-66"></a>
### Case 66: [用 62 张截图改进黑洞可视化](https://x.com/TokenGremlin/status/2077855959201042645) (by [@TokenGremlin](https://x.com/TokenGremlin))

**通过截图反馈循环，在多次迭代中读取、诊断并修正视觉模拟**

来源称 Kimi K3 通过观察并改进 62 张截图中的输出，重建了《星际穿越》的卡冈图雅，这展示的是已报告的反馈循环，而非独立物理精度验证

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-66.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-66-poster.jpg" alt="Case 66 source video poster" height="360"></a>

[Play case 66 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-66.mp4)

Type: Tutorial | Date: 2026-07-16

---

<a id="case-68"></a>
### Case 68: [制作后训练营销 PDF](https://x.com/Satvik_Pen/status/2077859673517023313) (by [@Satvik_Pen](https://x.com/Satvik_Pen))

**使用明确的产品名称与交付格式生成营销文档**

创作者称让 Kimi K3 为 Thinking Machines 的后训练产品 Inkling 制作营销 PDF 并分享了结果，同时称赞其幕后过程，来源未提供 prompt 或评价标准

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-01.png" alt="Case 68 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-02.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-02.png" alt="Case 68 source image 2" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-03.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-03.png" alt="Case 68 source image 3" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-04.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-04.png" alt="Case 68 source image 4" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-70"></a>
### Case 70: [用一个 prompt 创建用户界面](https://x.com/BrianMRey/status/2077891942088671689) (by [@BrianMRey](https://x.com/BrianMRey))

**使用单次请求生成并检查完整 UI 设计**

创作者展示了归因于 Kimi K3 单 prompt 运行的 UI 设计，并给出强烈正面的主观评价，来源未提供完整 prompt 或评分标准

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-70.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-70-poster.jpg" alt="Case 70 source video poster" height="360"></a>

[Play case 70 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-70.mp4)

Type: Demo | Date: 2026-07-16

---


<a id="coding-integrations"></a>
## 💻 编程与集成

<a id="case-18"></a>
### Case 18: [构建运行 macOS 的虚拟 MacBook](https://x.com/scottstts/status/2077890054299541890) (by [@scottstts](https://x.com/scottstts))

**将 Three.js 硬件渲染与可交互的浏览器操作系统模拟结合**

来源称 Kimi K3 使用 Three.js 创建了虚拟 MacBook，并配有可运行的 macOS 风格环境，展示了产物但未提供实现步骤

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-18.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-18-poster.jpg" alt="Case 18 source video poster" height="360"></a>

[Play case 18 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-18.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-25"></a>
### Case 25: [构建从 DSL 到 PTX 的 GPU 编译器](https://x.com/rohanpaul_ai/status/2077886618657231220) (by [@rohanpaul_ai](https://x.com/rohanpaul_ai))

**用端到端编译器任务覆盖 DSL、编译过程、PTX 生成与 Tensor Core 路径**

来源称 Kimi K3 从零构建了 GPU 编译器，涵盖 DSL、各编译过程与 PTX 生成，并将其 Tensor Core 路径与 Triton 比较，所提供记录不含独立评测细节

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-25-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-25-01.png" alt="Case 25 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-32"></a>
### Case 32: [在 WebGL2 中构建实时黑洞光线追踪器](https://x.com/AlicanKiraz0/status/2077885419744612597) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**测试用一个 prompt 在单个 HTML 文件中生成原生 WebGL2 测地线光线追踪器**

作者描述了一项编程评测，要求在原生 WebGL2 中制作可运行的单文件黑洞光线弯曲追踪器，所提供记录确认了任务和参与模型，但不包含完整的独立结果审计

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-32.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-32-poster.jpg" alt="Case 32 source video poster" height="360"></a>

[Play case 32 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-32.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-46"></a>
### Case 46: [围绕 mGBA WASM 构建 Game Boy Advance 模拟器](https://x.com/teortaxesTex/status/2077925090168062272) (by [@teortaxesTex](https://x.com/teortaxesTex))

**整合获许可的 3D 模型与真实模拟器核心，再递归改进界面与游戏体验**

所引 Kimi K3 项目改造了获许可的 AGB-001 模型，整合 mGBA WASM 核心，并通过递归式自我改进优化界面和游戏体验，帖子引用的是项目说明而非独立复现

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-46-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-46-01.jpg" alt="Case 46 source image 1" height="360"></a>

Type: Integration | Date: 2026-07-17

---

<a id="case-50"></a>
### Case 50: [使用中文来源研究多个主题](https://x.com/tphuang/status/2077911994607239400) (by [@tphuang](https://x.com/tphuang))

**通过长时间研究任务比较不同代际模型的详尽程度与延迟**

作者称使用中文来源测试 Kimi K3 的多个研究主题，认为它比 K2.6 更详尽但更慢，帖子还指出当时服务需求很高

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-50-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-50-01.png" alt="Case 50 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-17

---

<a id="case-56"></a>
### Case 56: [在浏览器中克隆带可用应用的 macOS](https://x.com/twid/status/2077924755357974989) (by [@twid](https://x.com/twid))

**构建包含音乐、浏览器与电子邮件应用的浏览器操作系统模拟**

来源称使用 Kimi K3 创建了基于浏览器的 macOS 克隆，包含音乐、浏览器、邮件及其他功能，但未提供实现细节

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-56.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-56-poster.jpg" alt="Case 56 source video poster" height="360"></a>

[Play case 56 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-56.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-62"></a>
### Case 62: [构建 FaceTime 可用的 macOS 模拟](https://x.com/LinearUncle/status/2077919552239997078) (by [@LinearUncle](https://x.com/LinearUncle))

**使用虚拟操作系统任务测试生成的应用交互是否真正可用**

创作者展示了归因于 Kimi K3 的 macOS 风格环境，并称其中 FaceTime 功能可用，来源未提供设置或验证步骤

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-62-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-62-01.jpg" alt="Case 62 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-17

---

<a id="case-64"></a>
### Case 64: [添加双任务前端效果比较器](https://x.com/MinLiBuilds/status/2077939461510615376) (by [@MinLiBuilds](https://x.com/MinLiBuilds))

**构建可选择两个已完成任务、并列显示且同步视图与交互的工具**

创作者称要求 Kimi K3 添加前端比较工作流，包括任务选择、双浏览器窗格、物体与漫游模式、同步视角和交互测试，帖子也提到了更广泛的模型局限

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-64.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-64-poster.jpg" alt="Case 64 source video poster" height="360"></a>

[Play case 64 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-64.mp4)

Type: Tutorial | Date: 2026-07-17

---


<a id="evaluation-limits"></a>
## 🧪 评估与限制

<a id="case-7"></a>
### Case 7: [在 BridgeBench 熔岩灯任务上比较前端设计](https://x.com/bridgemindai/status/2077868061953007908) (by [@bridgemindai](https://x.com/bridgemindai))

**将 BridgeBench 熔岩灯任务视为一次有边界的前端设计比较，而非通用排名**

BridgeMind AI 报告称，Kimi K3 在其 BridgeBench 熔岩灯任务中优于 Fable 5，并在所述竞技场中排名第一，这些均为发布方报告的比较结果

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-07.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-07-poster.jpg" alt="Case 7 source video poster" height="360"></a>

[Play case 7 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-07.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-8"></a>
### Case 8: [评测编辑语调脚本写作](https://x.com/Whats_AI/status/2077860441380798908) (by [@Whats_AI](https://x.com/Whats_AI))

**在明确标识的内部评测中衡量编辑语调契合度、相对排名与单篇脚本成本**

Whats_AI 报告的早期内部结果为 2,840 Elo、榜单第一、每篇脚本约 $0.25，应将其视为单一机构的初步评测，而非普遍性能或价格保证

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-08-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-08-01.jpg" alt="Case 8 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-16

---

<a id="case-10"></a>
### Case 10: [比较 Flappy 游戏的设计、成本与难度](https://x.com/MrAhmadAwais/status/2077915347974557862) (by [@MrAhmadAwais](https://x.com/MrAhmadAwais))

**比较生成游戏时记录难度设置、成本、设计和玩法特征**

Command Code 的内部 Flappy 评测对不同模型采用了不同难度，并列出 Kimi K3 为 $0.024、Fable 5 为 $0.42、GPT-5.6 Sol 为 $0.15，因此这是一次条件不等的有限内部比较

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-10.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-10-poster.jpg" alt="Case 10 source video poster" height="360"></a>

[Play case 10 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-10.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-12"></a>
### Case 12: [用相同设计 prompt 比较游戏设计](https://x.com/CommandCodeAI/status/2077921526213746948) (by [@CommandCodeAI](https://x.com/CommandCodeAI))

**固定设计 prompt，分别检查节奏、设计感与玩法体验**

Command Code 报告了 Kimi K3、GPT-5.6 Sol 与 Fable 5 的同 prompt 比较，帖子称 Kimi K3 的设计感表现良好，而另外两款游戏节奏过快，这仍是发布方的评价

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-12.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-12-poster.jpg" alt="Case 12 source video poster" height="360"></a>

[Play case 12 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-12.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-13"></a>
### Case 13: [统计审计必须经过独立复核](https://x.com/emollick/status/2077869293031624793) (by [@emollick](https://x.com/emollick))

**在依赖模型生成的统计审计结论前，先由独立专家或其他模型复核**

Ethan Mollick 报告称 Kimi K3 Max 在审计既往学术工作时误用了统计方法，并认同另一份批评意见，这一负面案例支持独立核查而非未经复核直接接受

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-13-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-13-01.jpg" alt="Case 13 source image 1" height="360"></a>

Type: Limit | Date: 2026-07-16

---

<a id="case-16"></a>
### Case 16: [评估速度慢但效果强的前端生成](https://x.com/Lentils80/status/2077387333154857151) (by [@Lentils80](https://x.com/Lentils80))

**测试前端任务时同时记录完成时间与输出质量**

创作者称一次 Kimi K3 前端生成耗时 35 分钟，并认为结果是该 prompt 下见过的最佳作品之一，速度和质量判断均为单个用户的观察

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-16.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-16-poster.jpg" alt="Case 16 source video poster" height="360"></a>

[Play case 16 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-16.mp4)

Type: Evaluation | Date: 2026-07-15

---

<a id="case-20"></a>
### Case 20: [测试悬疑写作中的伏笔失误](https://x.com/emollick/status/2077951790868238616) (by [@emollick](https://x.com/emollick))

**评估生成的悬疑故事能否平衡线索、隐蔽性与伏笔**

Ethan Mollick 报告称 Kimi K3 未能写出优秀的谋杀悬疑故事，线索既过于明显又过于隐晦，且伏笔处理失败，他也指出其他模型存在同类局限

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-01.jpg" alt="Case 20 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-02.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-02.png" alt="Case 20 source image 2" height="360"></a>

Type: Limit | Date: 2026-07-17

---

<a id="case-21"></a>
### Case 21: [比较千年隼号的建模与动画](https://x.com/gmi_cloud/status/2077903360263676090) (by [@gmi_cloud](https://x.com/gmi_cloud))

**用匹配的风格请求与工作强度设置比较 3D 建模、动画、时间与成本**

GMI Cloud 报告称，在最大工作强度下比较 Kimi K3 与 Fable 5 制作像素风和原始风格的千年隼号时，Kimi K3 耗时更长，但第一次测试成本约为三分之一，另一次不到一半，这些均为服务商报告的结果

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-21.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-21-poster.jpg" alt="Case 21 source video poster" height="360"></a>

[Play case 21 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-21.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-28"></a>
### Case 28: [回顾十个 Kimi K3 项目合集](https://x.com/minchoi/status/2077957907857994006) (by [@minchoi](https://x.com/minchoi))

**通过带链接的项目合集发现可供分别验证的具体产物**

作者整理了十个带媒体的 Kimi K3 示例，其中包括 Game Boy Advance 模拟器，本条是合集而非单一可复现工作流，因此每个链接示例都应单独核查

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-28.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-28-poster.jpg" alt="Case 28 source video poster" height="360"></a>

[Play case 28 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-28.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-29"></a>
### Case 29: [在四款模型间比较高级落地页](https://x.com/doutorcaleb/status/2077904020471947773) (by [@doutorcaleb](https://x.com/doutorcaleb))

**固定落地页请求，检查不同模型输出的动画深度与完成度**

创作者称向 Kimi K3、Fable、Grok 与 GPT Terra 提交了相同的高级落地页 prompt，并认为 Kimi K3 结果最佳，这是针对单个任务的自述比较

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-29.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-29-poster.jpg" alt="Case 29 source video poster" height="360"></a>

[Play case 29 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-29.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-30"></a>
### Case 30: [评测复古游戏机制与成本](https://x.com/adxtyahq/status/2077860500462055570) (by [@adxtyahq](https://x.com/adxtyahq))

**在相同复古游戏任务上比较玩法、物理、机制、自动行为、token 用量与成本**

来源报告了 Road Fighter、Battle City 与 Q*bert 的同 prompt 测试，并列出 Kimi K3 为 $0.28、GPT-5.6 为 $0.28、Opus 4.8 为 $0.54，这些均为发布方的评测数据

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-30.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-30-poster.jpg" alt="Case 30 source video poster" height="360"></a>

[Play case 30 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-30.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-31"></a>
### Case 31: [与 Fable 5 比较游戏生成](https://x.com/higgsfield_ai/status/2077943629633712490) (by [@higgsfield_ai](https://x.com/higgsfield_ai))

**将并列展示的生成游戏视为有限评估，而非宽泛的模型结论**

Higgsfield 展示了 Kimi K3 与 Fable 5 的游戏生成比较，所提供记录包含比较媒体，但没有 prompt、评分标准或详细条件

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-31.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-31-poster.jpg" alt="Case 31 source video poster" height="360"></a>

[Play case 31 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-31.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-34"></a>
### Case 34: [与 Opus 4.8 比较复杂前端和开发任务](https://x.com/op7418/status/2077969583018066116) (by [@op7418](https://x.com/op7418))

**通过多项复杂编程任务识别胜负，而非宣称某一模型普遍更优**

评测者报告了 Kimi K3 与 Opus 4.8 的直接测试，认为二者在复杂前端和开发工作上大致相当，结果有胜有负，这仍是单一评测者的判断

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-34.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-34-poster.jpg" alt="Case 34 source video poster" height="360"></a>

[Play case 34 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-34.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-35"></a>
### Case 35: [评述 benchmark 与落地页测试](https://x.com/adamuchigabriel/status/2077880433925120471) (by [@adamuchigabriel](https://x.com/adamuchigabriel))

**将 benchmark 背景与具体落地页生成测试结合，同时区分两类证据**

视频介绍了 Kimi K3 的 benchmark 讨论、落地页测试和前端设计观察，所提供记录没有完整测试 prompt 或评分标准

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-35.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-35-poster.jpg" alt="Case 35 source video poster" height="360"></a>

[Play case 35 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-35.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-37"></a>
### Case 37: [用图到公式任务评估归纳推理](https://x.com/s_batzoglou/status/2077884096307454119) (by [@s_batzoglou](https://x.com/s_batzoglou))

**在一阶归纳任务上衡量正确率、留出集表现与公式复杂度**

作者报告称在 ICML INDUCTION 任务上评测 Kimi K3 等模型，使用 6 至 10 个小图，每个包含 8 至 10 个元素，以推断一阶公式，帖子称结果基于早期工作更新，本案例不声称进行了新的独立复现

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-37-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-37-01.png" alt="Case 37 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-16

---

<a id="case-38"></a>
### Case 38: [回顾已报告的游戏、落地页、3D 工作和长上下文表现](https://x.com/servasyy_ai/status/2077903775113834689) (by [@servasyy_ai](https://x.com/servasyy_ai))

**通过多来源汇总比较具体产物，并在成本说法之外注明速度限制**

作者汇总了 Kimi K3 在游戏、落地页、3D 生成和长上下文工作中的已报告测试，结论是值得尝试但尚不能替代 Fable 5，所有数据均为该汇总中的二手报告

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-38-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-38-01.jpg" alt="Case 38 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-40"></a>
### Case 40: [审计复杂计划并质疑补救措施](https://x.com/doodlestein/status/2077901883637665958) (by [@doodlestein](https://x.com/doodlestein))

**使用第二个模型找出被淡化的问题、错误的补救措施和应被否定的结论**

创作者称 Kimi K3 审查了一份经过大量打磨的计划，发现严重问题被淡化、约三分之一的拟议补救措施需纠正，且有一项发现被推翻，这些是该次特定审计的结果

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-40-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-40-01.jpg" alt="Case 40 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-41"></a>
### Case 41: [比较 PPO 风格强化学习 ASCII 图](https://x.com/dejavucoder/status/2077872015856615541) (by [@dejavucoder](https://x.com/dejavucoder))

**固定 ASCII 图 prompt，比较模型如何表示强化学习循环**

来源提供了以 ASCII 绘制 PPO 风格强化学习循环的 prompt，并并列展示 Kimi K3 Max 与 Fable 5 High，判断仍来自单个任务的视觉比较

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-01.png" alt="Case 41 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-02.jpg" alt="Case 41 source image 2" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-42"></a>
### Case 42: [在 Blender 建模时跟踪容量错误](https://x.com/Angaisb_/status/2077910845523214668) (by [@Angaisb_](https://x.com/Angaisb_))

**将 Blender 的阶段性进展与服务可靠性一起评估，而非只判断产物**

创作者展示了 Kimi K3 在 Blender 中的建模进展，也报告了反复出现的容量错误，所提供来源中的工作尚未完成，因此应同时考虑阶段性结果与可靠性限制

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-42-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-42-01.jpg" alt="Case 42 source image 1" height="360"></a>

Type: Limit | Date: 2026-07-17

---

<a id="case-47"></a>
### Case 47: [在竞技场比较 Flappy Bird 生成](https://x.com/jun_song/status/2077396996865003739) (by [@jun_song](https://x.com/jun_song))

**通过竞技场任务比较两个 Flappy Bird 生成结果，同时将判断限定在该任务**

创作者报告了 Kimi K3 与 Opus 4.8 在 Flappy Bird 任务上的 Arena 比较，并认为 Kimi K3 明显更好，记录中未提供完整 prompt 或评分标准

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-47.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-47-poster.jpg" alt="Case 47 source video poster" height="360"></a>

[Play case 47 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-47.mp4)

Type: Evaluation | Date: 2026-07-15

---

<a id="case-52"></a>
### Case 52: [借助工具解决 Bongard 视觉归纳问题](https://x.com/IntuitMachine/status/2077885406528311561) (by [@IntuitMachine](https://x.com/IntuitMachine))

**测试工具使用是否有助于推导 Bongard 推理任务中的视觉规则**

创作者称 Kimi K3 使用工具解决了一个 Bongard 问题，而在同一次比较中 Grok 4.5 与 Muse Spark 1.1 未能解决，这是单个用户的任务结果，而非普遍推理 benchmark

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-52-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-52-01.jpg" alt="Case 52 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-53"></a>
### Case 53: [与 GPT-5.6 Sol 比较前端审美和 3D 设计](https://x.com/filicroval/status/2077736407506751952) (by [@filicroval](https://x.com/filicroval))

**在有边界的前端比较中检查功能、视觉审美、优雅程度与 3D 执行**

创作者比较了 Kimi K3 与 GPT-5.6 Sol 的前端设计，并认为 Kimi K3 在视觉审美、优雅程度和 3D 能力上更强，该评价主观且仅适用于特定任务

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-53.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-53-poster.jpg" alt="Case 53 source video poster" height="360"></a>

[Play case 53 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-53.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-57"></a>
### Case 57: [比较三款模型的网站生成](https://x.com/pengchujin/status/2077962916226298340) (by [@pengchujin](https://x.com/pengchujin))

**通过可见的网站输出比较 Kimi K3、Fable 5 与 GPT-5.6 Sol 在一次测试中的表现**

创作者展示了 Kimi K3、Fable 5 与 GPT-5.6 Sol 的网站生成比较，所提供记录未公开完整 prompt 或评分标准

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-57.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-57-poster.jpg" alt="Case 57 source video poster" height="360"></a>

[Play case 57 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-57.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-59"></a>
### Case 59: [比较程序化 3D 游戏生成与成本](https://x.com/adxtyahq/status/2077958193511362856) (by [@adxtyahq](https://x.com/adxtyahq))

**在模型间固定 prompt，检查生成的轮盘、老虎机与弹球系统及单次运行成本**

发布方报告了多模型程序化 3D 游戏比较，并列出 Kimi K3 为 $0.71、Grok 4.5 为 $0.30 等成本，所有排名与成本都应视为该发布方运行的结果

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-59.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-59-poster.jpg" alt="Case 59 source video poster" height="360"></a>

[Play case 59 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-59.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-69"></a>
### Case 69: [比较 3D 军械库场景细节与照明](https://x.com/hakki_alkan/status/2077887013332636032) (by [@hakki_alkan](https://x.com/hakki_alkan))

**在有边界的 Kimi K3 与 Opus 4.8 比较中检查物体密度、照明与场景细节**

来源称 Kimi K3 生成了包含摆满物品的货架、箱子和真实照明的细致军械库场景，而 Opus 4.8 只生成了空旷房间，这是第三方比较报告而非独立 benchmark

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-69-poster.jpg" alt="Case 69 source video poster" height="360"></a>

[Play case 69 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-69.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="related-resources"></a>
## 相关资源

- [查看 EvoLink 上的 Kimi K3 详情与价格](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_model)
- [查看 EvoLink Kimi K3 API 文档](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_api_docs)
- [进一步了解 EvoLink 上的 Kimi K3](https://evolink.ai/blog/is-kimi-k3-available-on-evolink?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_article)
- [KimiK3.io](https://kimik3.io/zh)
- EvoLink 模型页与 API 文档已验证，但尚未验证可安装的 Kimi K3 skill

<a id="quick-api-access"></a>
## ⚡ 快速开始

EvoLink 文档记录的模型 ID 为 `kimi-k3`，模型详情页与 Chat Completions API 文档均已提供

1. [查看 EvoLink 上的 Kimi K3 详情与价格](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-kimi-k3-usecases&utm_content=model_link)
2. [创建或管理 EvoLink API 密钥](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-kimi-k3-usecases&utm_content=api_key)
3. [查看 EvoLink Kimi K3 API 文档](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=first_run)

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
> EvoLink 模型页与 API 文档验证了公开路由和模型 ID，本案例库不声称已独立完成付费 API 测试

<a id="acknowledge"></a>
## 🙏 致谢

感谢所有公开分享 Kimi K3 作品的创作者与从业者

[@ivanfioravanti](https://x.com/ivanfioravanti), [@TheAhmadOsman](https://x.com/TheAhmadOsman), [@HarshithLucky3](https://x.com/HarshithLucky3), [@chetaslua](https://x.com/chetaslua), [@abhinavflac](https://x.com/abhinavflac), [@bridgemindai](https://x.com/bridgemindai), [@Whats_AI](https://x.com/Whats_AI), [@chongdashu](https://x.com/chongdashu), [@MrAhmadAwais](https://x.com/MrAhmadAwais), [@bijanbowen](https://x.com/bijanbowen), [@CommandCodeAI](https://x.com/CommandCodeAI), [@emollick](https://x.com/emollick), [@nicky_sap](https://x.com/nicky_sap), [@Lentils80](https://x.com/Lentils80), [@scottstts](https://x.com/scottstts), [@aisearchio](https://x.com/aisearchio), [@gmi_cloud](https://x.com/gmi_cloud), [@karminski3](https://x.com/karminski3), [@VORTEX_Promos](https://x.com/VORTEX_Promos), [@rohanpaul_ai](https://x.com/rohanpaul_ai), [@mirochill](https://x.com/mirochill), [@aimlapi](https://x.com/aimlapi), [@minchoi](https://x.com/minchoi), [@doutorcaleb](https://x.com/doutorcaleb), [@adxtyahq](https://x.com/adxtyahq), [@higgsfield_ai](https://x.com/higgsfield_ai), [@AlicanKiraz0](https://x.com/AlicanKiraz0), [@1littlecoder](https://x.com/1littlecoder), [@op7418](https://x.com/op7418), [@adamuchigabriel](https://x.com/adamuchigabriel), [@s_batzoglou](https://x.com/s_batzoglou), [@servasyy_ai](https://x.com/servasyy_ai), [@filicroval](https://x.com/filicroval), [@doodlestein](https://x.com/doodlestein), [@dejavucoder](https://x.com/dejavucoder), [@Angaisb_](https://x.com/Angaisb_), [@AngryTomtweets](https://x.com/AngryTomtweets), [@Alezander907](https://x.com/Alezander907), [@teortaxesTex](https://x.com/teortaxesTex), [@jun_song](https://x.com/jun_song), [@ridark_eth](https://x.com/ridark_eth), [@naymur_dev](https://x.com/naymur_dev), [@tphuang](https://x.com/tphuang), [@TokenGremlin](https://x.com/TokenGremlin), [@IntuitMachine](https://x.com/IntuitMachine), [@wangfeng0315](https://x.com/wangfeng0315), [@twid](https://x.com/twid), [@pengchujin](https://x.com/pengchujin), [@aayushman2703](https://x.com/aayushman2703), [@goncalo_canhoto](https://x.com/goncalo_canhoto), [@LinearUncle](https://x.com/LinearUncle), [@gagarot200](https://x.com/gagarot200), [@MinLiBuilds](https://x.com/MinLiBuilds), [@izutorishima](https://x.com/izutorishima), [@X2worldtech](https://x.com/X2worldtech), [@Satvik_Pen](https://x.com/Satvik_Pen), [@hakki_alkan](https://x.com/hakki_alkan), [@BrianMRey](https://x.com/BrianMRey)

*如需更正归属或文字，请附公开来源创建 issue*
