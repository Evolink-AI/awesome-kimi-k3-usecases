<div align="center">

<a href="https://evolink.ai/kimi-k3?utm_source=github&utm_medium=banner&utm_campaign=awesome-kimi-k3-usecases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/images/zh-v2.png" alt="带月面场景与 EvoLink 使用入口的简体中文 Kimi K3 banner" width="760"></a>

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

# Kimi K3 精选使用案例

## 🍌 简介

欢迎来到 Kimi K3 高信号使用案例库

**我们收录有公开来源支持的游戏、3D 场景、动态设计、集成、评估与实际限制**

全部 129 个案例都来自高置信度公开来源。标题和作者链接指向原始来源；弱证据、重复或无法充分核验的候选不会收录

## 📊 概览

- 来自公开创作者和实践者的 129 个高置信度案例
- 覆盖互动游戏、3D、前端与动态设计、编程、研究、评估、可视化和代理限制
- 每个案例保留来源、作者、类型、日期和 prompt 边界
- 不把个人观察包装成 benchmark

> [!NOTE]
> 本案例库优先采用具体证据，不补写未公开的 prompt 或配置步骤

<a id="quick-api-access"></a>
## ⚡ 快速开始

EvoLink 文档记录的模型 ID 为 `kimi-k3`，模型详情页与 Chat Completions API 文档均已提供

1. [查看 EvoLink 上的 Kimi K3 详情与价格](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=landing_overview)
2. [创建或管理 EvoLink API 密钥](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-kimi-k3-usecases&utm_content=api_key)

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

[查看 EvoLink Kimi K3 API 文档](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=first_run)

> [!IMPORTANT]
> EvoLink 模型页与 API 文档验证了公开路由和模型 ID；目前未验证独立的 Kimi K3 浏览器或无代码试用界面，本案例库也不声称已独立完成付费 API 测试

## 📑 目录

| Section | Cases |
|---|---|
| [互动游戏与 3D](#games-3d) | 41 |
| [前端与动态设计](#frontend-motion) | 32 |
| [编程与集成](#coding-integrations) | 18 |
| [评估与限制](#evaluation-limits) | 48 |
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
| [构建独立太空飞船游戏](#case-71) | 互动游戏与 3D | 先用 Kimi K3 Standard 制作游戏初版，再比较一致性、缺陷、视觉质量和 token 成本 | Demo |
| [用相同 Arena prompt 比较前端](#case-72) | 评估与限制 | 固定 prompt 并并排检查输出，比只看一个排行榜分数更可靠 | Benchmark |
| [让 Summer Engine 游戏自测](#case-73) | 互动游戏与 3D | 让 Kimi K3 运行游戏、检查截图和日志并在同一会话中修复可见缺陷 | Demo |
| [评测 Kimi Code 编码 agent](#case-74) | 评估与限制 | 结合多个编码 agent 测试集和单任务成本评估 Kimi K3，不把单一前端榜单当成总体能力 | Benchmark |
| [将 Kimi 配置为 Codex 子 agent](#case-75) | 编程与集成 | 让 Codex 保持编排职责，把前端执行交给 Kimi K3 OpenCode 子 agent，并明确密钥边界 | Tutorial |
| [比较 Arena 与修复测试结果](#case-76) | 评估与限制 | 同时看前端偏好和仓库修复评测，因为 Kimi K3 可在一个榜单第一、在另一测试中第七 | Benchmark |
| [迭代浏览器大逃杀游戏](#case-77) | 互动游戏与 3D | 构建功能丰富的浏览器游戏时，要预期长时间自主迭代和有针对性的后续 prompt | Demo |
| [构建获奖风格网站](#case-78) | 前端与动态设计 | 通过完整录屏评估 Kimi K3 的精致网站构建过程，而不只看最终截图 | Tutorial |
| [通过 ChatLLM 路由简单编码](#case-79) | 编程与集成 | 创建任务路由，将简单编码交给 Kimi K3，把困难编码和设计保留给其他模型 | Integration |
| [用 Prinzbench 评估 Kimi K3](#case-80) | 评估与限制 | 用独立 benchmark 更新对比 Kimi K3 与开源、前沿模型在搜索、推理和一致性上的表现。 | Benchmark |
| [构建滚动 Metaball 前端](#case-81) | 前端与动态设计 | 让 Kimi K3 生成 Awwwards 风格滚动页面，并检查数学效果是否能替代重型 mesh 或贴图资源。 | Demo |
| [跨模型重设计个人网站](#case-82) | 前端与动态设计 | 用多个 coding harness 执行同一个网站重设计 brief，并比较耗时、视觉方向和与现有身份的匹配度。 | Evaluation |
| [扩展太空游戏地形](#case-83) | 互动游戏与 3D | 把 Kimi K3 作为长时间构建 pass，把占位地形替换成更大的真实地貌启发游戏环境。 | Demo |
| [解锁 Three.js 物理渲染器](#case-84) | 互动游戏与 3D | 当数学和物理逻辑可用但渲染管线停滞时，把 Kimi K3 引入 Three.js 物理项目。 | Demo |
| [对比 ISS 数字孪生生成](#case-85) | 评估与限制 | 用同 prompt 3D 挑战，对比 Kimi K3 与 GPT-5.6 Sol 在重建、控制、标签和视觉细节上的表现。 | Benchmark |
| [构建交互式头皮探索器](#case-86) | 前端与动态设计 | 用 Kimi K3 一次生成包含解剖层、响应式发丝和交互热点的 3D 教育场景。 | Demo |
| [分享 3D 地球仪仪表盘 Prompt](#case-87) | 前端与动态设计 | 研究 Kimi K3 3D 地球仪仪表盘的 prompt 与参考图设置，而不是只从最终图反推工作流。 | Tutorial |
| [用单文件构建浏览器 Counter-Strike](#case-88) | 互动游戏与 3D | 用 Kimi K3 生成单文件浏览器 FPS，并检查地图、机器人、武器、回合规则和程序化音频是否完整。 | Demo |
| [评测 WebGPU 森林世界](#case-89) | 评估与限制 | 在长周期 Three.js 与 WebGPU 世界构建中，把 Kimi K3 作为 coding agent brain，从质量、速度、一致性和人工修改率评估它。 | Evaluation |
| [比较玻璃屋同题提示](#case-90) | 评估与限制 | 用同一个建筑场景提示比较 Kimi K3 与 Opus 4.8 在氛围、光照和空间完整度上的差异。 | Evaluation |
| [用生成资产构建 CS](#case-91) | 编程与集成 | 原型化小型 Counter-Strike 风格浏览器游戏时，用 Kimi K3 写游戏代码，用 GPT Image 2 生成资产。 | Integration |
| [评测体素足球进球](#case-92) | 评估与限制 | 把同一个纯 HTML/CSS/JS 足球动画提示交给两个模型，比较运动质量和成本。 | Benchmark |
| [审看 Minecraft benchmark](#case-93) | 评估与限制 | 在把发布 hype 或模型价格当作证据前，先看结构化 Minecraft 测评。 | Benchmark |
| [执行五项 UI UX 测试](#case-94) | 前端与动态设计 | 不要只看一张 frontend 截图，而是用多项 UI、Logo 和 Figma MCP 任务评估 Kimi K3。 | Evaluation |
| [使用 Command Code Design skill](#case-95) | 编程与集成 | 在 token 预算内构建视觉游戏原型时，把 Kimi K3 与 Command Code 的专用 design skill 结合使用。 | Integration |
| [构建金字塔探险游戏](#case-96) | 互动游戏与 3D | 用 Kimi K3 做一次完整的一日 3D 探索游戏构建，再检查任务、室内空间和探索范围后评价质量。 | Demo |
| [从参考图创建 landing](#case-97) | 前端与动态设计 | 用参考图板、Figma AI、Motion Sites 与 Kimi K3，把视觉方向转成可复用的 landing page section。 | Tutorial |
| [衡量 API 档位限制](#case-98) | 评估与限制 | 规划 Kimi K3 agent run 时，要看 token、tier、TPM 和 TPD，不只看模型标价。 | Limit |
| [比较 Limbo 风格 demo](#case-99) | 评估与限制 | 在同一个游戏原型上比较 Kimi K3 与 Fable 5 的可玩范围、视觉打磨、成本和 bug。 | Benchmark |
| [审查 VulcanBench 成本结果](#case-100) | 评估与限制 | 用这个案例评估 Kimi K3 在「审查 VulcanBench 成本结果」任务中的实际工作流、成本或限制。 | Benchmark |
| [比较 Minecraft 构建深度](#case-101) | 互动游戏与 3D | 用这个案例评估 Kimi K3 在「比较 Minecraft 构建深度」任务中的实际工作流、成本或限制。 | Evaluation |
| [构建 Fallout FPS 克隆](#case-102) | 互动游戏与 3D | 用这个案例评估 Kimi K3 在「构建 Fallout FPS 克隆」任务中的实际工作流、成本或限制。 | Demo |
| [跟做高级网站教程](#case-103) | 前端与动态设计 | 用这个案例评估 Kimi K3 在「跟做高级网站教程」任务中的实际工作流、成本或限制。 | Tutorial |
| [评测双摆物理模拟](#case-104) | 评估与限制 | 用这个案例评估 Kimi K3 在「评测双摆物理模拟」任务中的实际工作流、成本或限制。 | Benchmark |
| [交付数据中心 RPG](#case-105) | 互动游戏与 3D | 用这个案例评估 Kimi K3 在「交付数据中心 RPG」任务中的实际工作流、成本或限制。 | Demo |
| [比较人形机器人前端成本](#case-106) | 前端与动态设计 | 用这个案例评估 Kimi K3 在「比较人形机器人前端成本」任务中的实际工作流、成本或限制。 | Benchmark |
| [审查 ReactBench 生产就绪度](#case-107) | 评估与限制 | 用这个案例评估 Kimi K3 在「审查 ReactBench 生产就绪度」任务中的实际工作流、成本或限制。 | Benchmark |
| [构建 3D 赛车游戏](#case-108) | 互动游戏与 3D | 用这个案例评估 Kimi K3 在「构建 3D 赛车游戏」任务中的实际工作流、成本或限制。 | Demo |
| [在 Claude Code 中运行 Kimi K3](#case-109) | 编程与集成 | 用这个案例评估 Kimi K3 在「在 Claude Code 中运行 Kimi K3」任务中的实际工作流、成本或限制。 | Integration |
| [用 AA-Briefcase 评估 Kimi K3](#case-110) | 评估与限制 | 先用 AA-Briefcase 结果判断 Kimi K3 的知识工作 agent 任务表现，再相信排行榜叙事。 | Benchmark |
| [对比 Geometry Dash 克隆](#case-111) | 互动游戏与 3D | 用同一需求的游戏 build 对比，判断 Kimi K3 是否足够做可玩的移动风格原型。 | Evaluation |
| [运行 Command Code 复古游戏测试](#case-112) | 互动游戏与 3D | 用 Command Code 的多模型设计测试对比 Kimi K3 的 gameplay 功能和各模型成本。 | Evaluation |
| [审计前端榜单限制](#case-113) | 评估与限制 | 用这条限制说明区分 Kimi K3 的榜单胜利和更宽泛的 coding、成本主张。 | Limit |
| [对比 StackPerf 架构结果](#case-114) | 评估与限制 | 用 StackPerf 对比 Kimi K3 和 Qwen 3.8 的架构质量、速度和 tool call 行为。 | Benchmark |
| [对比 Three.js Kimi-vs-GLM 构建](#case-115) | 前端与动态设计 | 用同一组程序化 Three.js prompts 跑 Kimi K3 和 GLM 5.2，比较前端与 3D build 行为。 | Benchmark |
| [评测 Space Discoverer 游戏](#case-116) | 互动游戏与 3D | 用 Space Discoverer 小基准比较模型在通用 3D 浏览器游戏 brief 下的输出。 | Benchmark |
| [构建真实道路驾驶游戏](#case-117) | 互动游戏与 3D | 把 Kimi K3 与 Blender、Godot 结合，用真实本地道路地图原型化一个驾驶游戏。 | Demo |
| [对比 Monument Valley prompt 成本](#case-118) | 评估与限制 | 用单个 Monument Valley 风格 prompt 对比 Kimi K3 与其他模型的视觉质量、运行时间和成本。 | Benchmark |
| [通过 claude-code-router 路由 Kimi](#case-119) | 编程与集成 | 在现有 Claude Code workflow 中通过 claude-code-router 试用 Kimi K3，同时避免不必要的 proxy mode。 | Integration |
| [用 Surge 指数评估 Kimi K3](#case-120) | 评估与限制 | 用 SurgeAI 的分项结果区分 Kimi K3 在日常聊天中的优势，以及在企业 agent 和科学任务中的弱项。 | Benchmark |
| [用参考图生成落地页](#case-121) | 前端与动态设计 | 测试落地页生成时，给 Kimi K3 提供强视觉参考和分轮指导。 | Demo |
| [构建纵向平台游戏](#case-122) | 互动游戏与 3D | 用简洁游戏 brief 测试 Kimi K3 能否返回单文件浏览器原型。 | Demo |
| [评估 PDE 求解错误](#case-123) | 评估与限制 | 用 PDE benchmark 失败案例判断 Kimi K3 在符号或数值任务中哪些环节需要额外验证。 | Benchmark |
| [复查 ClinicalBench EHR 案例](#case-124) | 评估与限制 | 用 ClinicalBench 的 EHR 案例检查 Kimi K3 哪些地方成功，哪些诊断推理仍会失败。 | Benchmark |
| [运行开源 agent harness](#case-125) | 编程与集成 | 用共享 agent harness 对比 Kimi K3 与其他前沿模型在工具调用任务中的表现。 | Benchmark |
| [评估报税计算能力](#case-126) | 评估与限制 | 不要假设前端强项会迁移到税务计算；应单独测试 Kimi K3 的该类负载。 | Limit |
| [验证 Geometry Dash 生成结果](#case-127) | 互动游戏与 3D | 把 Kimi K3 游戏构建与 solver 和浏览器回放测试结合，再判断它是否可作为完成原型。 | Benchmark |
| [模拟 3D 粒子系统](#case-128) | 前端与动态设计 | 用粒子模拟 prompt 对比 Kimi K3 与闭源模型的运动质量。 | Evaluation |
| [通过 Codex OAuth 运行 Kimi](#case-129) | 编程与集成 | 当 Kimi K3 编码工作流需要避免手动配置 API key 时，使用 Codex OAuth 路径。 | Integration |
| [复合 computer use 基准测试](#case-130) | 评估与限制 | 不只看合成分数，而是在复合 computer use 任务中比较 Kimi K3。 | Benchmark |
| [构建深海解说流水线](#case-131) | 前端与动态设计 | 把叙事型 prompt 转成包含场景、文字、运动和解释结构的可视化流水线。 | Demo |
| [模拟六足机器人](#case-132) | 互动游戏与 3D | 用 Kimi K3 原型化一个带腿部运动和可见行为的 3D 机器人场景。 | Demo |
| [盲测落地页输出](#case-133) | 前端与动态设计 | 在不揭示模型名称的 landing page 对比中评估 Kimi K3 的 frontend 输出。 | Benchmark |
| [原型化机械 3D 细节](#case-134) | 前端与动态设计 | 让 Kimi K3 生成带视觉细节和渲染约束的小型机械 3D 场景。 | Demo |
| [复刻 Expo 移动端 UI](#case-135) | 前端与动态设计 | 用移动 Expo UI 检查 Kimi K3 的结构、组件组织和视觉完成度。 | Evaluation |
| [压力测试生产后端](#case-136) | 编程与集成 | 在更真实的 backend 流程中观察 Kimi K3 的集成、代码推理和限制。 | Evaluation |
| [通过 opencodex 路由 Codex](#case-137) | 编程与集成 | 把 Kimi K3 接入 Codex/opencodex 循环，做一个具体的 agent routing 集成实验。 | Integration |
| [自动化游戏调参循环](#case-138) | 互动游戏与 3D | 构建一个会录制 gameplay、分析结果、调整参数并重新测试的 harness。 | Integration |
| [跟随网页设计教程](#case-139) | 前端与动态设计 | 用完整 tutorial 观察 Kimi K3 如何搭建 layout、动效和视觉 polish。 | Tutorial |

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

<a id="case-71"></a>
### Case 71: [构建独立太空飞船游戏](https://x.com/ChrisGPT/status/2078261217924087999) (by [@ChrisGPT](https://x.com/ChrisGPT))

**先用 Kimi K3 Standard 制作游戏初版，再比较一致性、缺陷、视觉质量和 token 成本**

ChrisGPT 报告 Kimi K3 Standard 以约 2.50 美元 API token 成本完成独立太空飞船游戏初版；它比 GPT-5.5 初版更连贯、bug 更少，但 Fable 5 的视觉效果仍更精致

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-71.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-71-poster.jpg" alt="Case 71 source video poster" height="360"></a>

[Play case 71 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-71.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-73"></a>
### Case 73: [让 Summer Engine 游戏自测](https://x.com/MathiasHeide/status/2078231589436465199) (by [@MathiasHeide](https://x.com/MathiasHeide))

**让 Kimi K3 运行游戏、检查截图和日志并在同一会话中修复可见缺陷**

Mathias Heide 报告 Kimi K3 在 27 分钟的一次会话中构建可运行的纸飞机游戏；模型启动游戏、截图、读取日志、修复 bug，并把错误的黑色纸飞机改为白色

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-73.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-73-poster.jpg" alt="Case 73 source video poster" height="360"></a>

[Play case 73 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-73.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-77"></a>
### Case 77: [迭代浏览器大逃杀游戏](https://x.com/Ananth7e/status/2078158089929601203) (by [@Ananth7e](https://x.com/Ananth7e))

**构建功能丰富的浏览器游戏时，要预期长时间自主迭代和有针对性的后续 prompt**

Ananth 报告 Kimi K3 用 130 多分钟和 40 多轮 Chrome 截图反馈构建 PUBG 风格游戏，并在首个输出后又用两个 prompt 修复剩余 bug

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-77.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-77-poster.jpg" alt="Case 77 source video poster" height="360"></a>

[Play case 77 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-77.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-83"></a>
### Case 83: [扩展太空游戏地形](https://x.com/startracker/status/2078543423167160342) (by [@startracker](https://x.com/startracker))

**把 Kimi K3 作为长时间构建 pass，把占位地形替换成更大的真实地貌启发游戏环境。**

创作者描述太空游戏第二天进展：Kimi K3 将小型占位海岸替换为 8 x 8 km 的冰岛启发地形，加入海岸感知的动画海洋，重建飞船外观，并生成下一步要用的环境资产。来源也说明执行较慢，录制帧率问题仍待解决。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-83.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-83-poster.jpg" alt="Case 83 source video poster" height="360"></a>

[Play case 83 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-83.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-84"></a>
### Case 84: [解锁 Three.js 物理渲染器](https://x.com/mattwatkajtys/status/2078523373861339475) (by [@mattwatkajtys](https://x.com/mattwatkajtys))

**当数学和物理逻辑可用但渲染管线停滞时，把 Kimi K3 引入 Three.js 物理项目。**

创作者表示物理世界构建器已停滞数月，底层数学和物理可用，但渲染管线无法推进。Kimi K3 的一次 pass 推动项目继续前进，视频展示了当前交互结果。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-84.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-84-poster.jpg" alt="Case 84 source video poster" height="360"></a>

[Play case 84 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-84.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-88"></a>
### Case 88: [用单文件构建浏览器 Counter-Strike](https://x.com/prasenx/status/2078453069021659477) (by [@prasenx](https://x.com/prasenx))

**用 Kimi K3 生成单文件浏览器 FPS，并检查地图、机器人、武器、回合规则和程序化音频是否完整。**

创作者报告用 Kimi K3 在一个超过 3,700 行的 HTML 文件里构建了类 Counter-Strike 浏览器游戏，无需 build step。成品包含 Dust2 风格地图、多种武器、换弹、巡逻与推进机器人、爆头、击杀信息、两分钟回合、程序化音频、Three.js、PBR，API 成本低于 5 美元。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-88.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-88-poster.jpg" alt="Case 88 source video poster" height="360"></a>

[Play case 88 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-88.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-96"></a>
### Case 96: [构建金字塔探险游戏](https://x.com/ice_bearcute/status/2078828887468056763) (by [@ice_bearcute](https://x.com/ice_bearcute))

**用 Kimi K3 做一次完整的一日 3D 探索游戏构建，再检查任务、室内空间和探索范围后评价质量。**

ice_bearcute 报告一天内完全用 Kimi K3 构建了 3D Pyramid Expedition 游戏。来源说明这不是简单外景，玩家可以探索古墓并完成任务；附带媒体提供了可见 gameplay 证据。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-96.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-96-poster.jpg" alt="Case 96 source video poster" height="360"></a>

[Play case 96 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-96.mp4)

Type: Demo | Date: 2026-07-19

---

<a id="case-101"></a>
### Case 101: [比较 Minecraft 构建深度](https://x.com/vikktorrrre/status/2079294696459804762) (by [@vikktorrrre](https://x.com/vikktorrrre))

**用这个案例评估 Kimi K3 在「比较 Minecraft 构建深度」任务中的实际工作流、成本或限制。**

来源帖提供了与 比较 Minecraft 构建深度 相关的公开证据，包括作者描述、结果媒体或基准/教程信息；本仓库只保留可核验事实，不补写未公开的 prompt 或步骤。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-101.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-101-poster.jpg" alt="Case 101 source video poster" height="360"></a>

[Play case 101 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-101.mp4)

Type: Evaluation | Date: 2026-07-20

---

<a id="case-102"></a>
### Case 102: [构建 Fallout FPS 克隆](https://x.com/kirillk_web3/status/2079290747585437781) (by [@kirillk_web3](https://x.com/kirillk_web3))

**用这个案例评估 Kimi K3 在「构建 Fallout FPS 克隆」任务中的实际工作流、成本或限制。**

来源帖提供了与 构建 Fallout FPS 克隆 相关的公开证据，包括作者描述、结果媒体或基准/教程信息；本仓库只保留可核验事实，不补写未公开的 prompt 或步骤。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-102.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-102-poster.jpg" alt="Case 102 source video poster" height="360"></a>

[Play case 102 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-102.mp4)

Type: Demo | Date: 2026-07-20

---

<a id="case-105"></a>
### Case 105: [交付数据中心 RPG](https://x.com/demian_ai/status/2079239035596218578) (by [@demian_ai](https://x.com/demian_ai))

**用这个案例评估 Kimi K3 在「交付数据中心 RPG」任务中的实际工作流、成本或限制。**

来源帖提供了与 交付数据中心 RPG 相关的公开证据，包括作者描述、结果媒体或基准/教程信息；本仓库只保留可核验事实，不补写未公开的 prompt 或步骤。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-105.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-105-poster.jpg" alt="Case 105 source video poster" height="360"></a>

[Play case 105 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-105.mp4)

Type: Demo | Date: 2026-07-20

---

<a id="case-108"></a>
### Case 108: [构建 3D 赛车游戏](https://x.com/LexnLin/status/2079233761242235081) (by [@LexnLin](https://x.com/LexnLin))

**用这个案例评估 Kimi K3 在「构建 3D 赛车游戏」任务中的实际工作流、成本或限制。**

来源帖提供了与 构建 3D 赛车游戏 相关的公开证据，包括作者描述、结果媒体或基准/教程信息；本仓库只保留可核验事实，不补写未公开的 prompt 或步骤。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-poster.jpg" alt="Case 108 source video poster" height="360"></a>

[Play case 108 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-01.jpg" alt="Case 108 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-02.jpg" alt="Case 108 source image 2" height="360"></a>

Type: Demo | Date: 2026-07-20

---

<a id="case-111"></a>
### Case 111: [对比 Geometry Dash 克隆](https://x.com/Nekt_0/status/2079629004483465473) (by [@Nekt_0](https://x.com/Nekt_0))

**用同一需求的游戏 build 对比，判断 Kimi K3 是否足够做可玩的移动风格原型。**

Nekt 表示 Kimi K3 用约 30 分钟和 20 万 tokens 构建了一个 Geometry Dash 风格克隆，包含跳跃、障碍、关卡、音乐和视觉效果，并在公开视频中与 Claude Fable 5 的 build 对比。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-111.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-111-poster.jpg" alt="Case 111 source video poster" height="360"></a>

[Play case 111 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-111.mp4)

Type: Evaluation | Date: 2026-07-21

---

<a id="case-112"></a>
### Case 112: [运行 Command Code 复古游戏测试](https://x.com/naymur_dev/status/2079627963000398334) (by [@naymur_dev](https://x.com/naymur_dev))

**用 Command Code 的多模型设计测试对比 Kimi K3 的 gameplay 功能和各模型成本。**

Naymur 称在 Command Code 中对 Fable 5、GPT-5.6 Sol、Grok 4.5 和 Kimi K3 运行了同一个 /design prompt。帖子说 Kimi K3 生成了带 gameplay、升级、子弹和 boss 战的 ASCII 复古游戏，报告成本为 $0.15。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-112.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-112-poster.jpg" alt="Case 112 source video poster" height="360"></a>

[Play case 112 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-112.mp4)

Type: Evaluation | Date: 2026-07-21

---

<a id="case-116"></a>
### Case 116: [评测 Space Discoverer 游戏](https://x.com/fabriciocarraro/status/2079548607393382528) (by [@fabriciocarraro](https://x.com/fabriciocarraro))

**用 Space Discoverer 小基准比较模型在通用 3D 浏览器游戏 brief 下的输出。**

Fabricio Carraro 报告了 Claude Fable 5、GPT-5.6 Sol 和 Kimi K3 在最高 reasoning 设置下的小基准。任务是名为 Space Discoverer 的 3D 浏览器游戏，帖子称三个模型都收敛到 WebGL 2 上的 Three.js。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-116.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-116-poster.jpg" alt="Case 116 source video poster" height="360"></a>

[Play case 116 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-116.mp4)

Type: Benchmark | Date: 2026-07-21

---

<a id="case-117"></a>
### Case 117: [构建真实道路驾驶游戏](https://x.com/bijanbowen/status/2079526003643179102) (by [@bijanbowen](https://x.com/bijanbowen))

**把 Kimi K3 与 Blender、Godot 结合，用真实本地道路地图原型化一个驾驶游戏。**

Bijan Bowen 展示 Kimi K3 使用 Blender 和 Godot 制作驾驶游戏，并以作者附近的一段真实道路作为地图基础。附带视频是该 build 状态的公开证据。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-117.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-117-poster.jpg" alt="Case 117 source video poster" height="360"></a>

[Play case 117 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-117.mp4)

Type: Demo | Date: 2026-07-21

---

<a id="case-122"></a>
### Case 122: [构建纵向平台游戏](https://x.com/diegocabezas01/status/2079946676270219488) (by [@diegocabezas01](https://x.com/diegocabezas01))

**用简洁游戏 brief 测试 Kimi K3 能否返回单文件浏览器原型。**

Diego Cabezas 展示了 Kimi K3 Max 生成纵向平台游戏的运行结果，玩家会在移动平台上不断向上跳。帖子记录这是一次生成的单 HTML 结果。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-122.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-122-poster.jpg" alt="Case 122 source video poster" height="360"></a>

[Play case 122 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-122.mp4)

Type: Demo | Date: 2026-07-22

---

<a id="case-127"></a>
### Case 127: [验证 Geometry Dash 生成结果](https://x.com/Kirratr/status/2079902410042909108) (by [@Kirratr](https://x.com/Kirratr))

**把 Kimi K3 游戏构建与 solver 和浏览器回放测试结合，再判断它是否可作为完成原型。**

Kirratr 报告 Kimi K3 在同一个 Geometry Dash 风格 brief 上耗时 36 分 53 秒。来源称 beam-search solver 找到 64 跳通关路径，并在真实浏览器中回放，移动视口测试无控制台错误。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-127.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-127-poster.jpg" alt="Case 127 source video poster" height="360"></a>

[Play case 127 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-127.mp4)

Type: Benchmark | Date: 2026-07-22

---

<a id="case-132"></a>
### Case 132: [模拟六足机器人](https://x.com/DilumSanjaya/status/2080335531108716750) (by [@DilumSanjaya](https://x.com/DilumSanjaya))

**用 Kimi K3 原型化一个带腿部运动和可见行为的 3D 机器人场景。**

来源：DilumSanjaya 分享了一个用 Kimi K3 做出的六足机器人模拟。这里按交互式 3D demo 收录，不外推为物理机器人验证。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-132.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-132-poster.jpg" alt="Case 132 source video poster" height="360"></a>

[Play case 132 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-132.mp4)

Type: Demo | Date: 2026-07-23

---

<a id="case-138"></a>
### Case 138: [自动化游戏调参循环](https://x.com/Oluwaphilemon1/status/2080187637806043200) (by [@Oluwaphilemon1](https://x.com/Oluwaphilemon1))

**构建一个会录制 gameplay、分析结果、调整参数并重新测试的 harness。**

来源：Oluwaphilemon1 描述了 Kimi K3 在 Three.js 项目中的用法，并提到游戏内调参循环。该流程减少手工 playtesting，但仅按公开帖可验证范围收录。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-138.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-138-poster.jpg" alt="Case 138 source video poster" height="360"></a>

[Play case 138 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-138.mp4)

Type: Integration | Date: 2026-07-23

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

<a id="case-78"></a>
### Case 78: [构建获奖风格网站](https://x.com/viktoroddy/status/2078140696910037002) (by [@viktoroddy](https://x.com/viktoroddy))

**通过完整录屏评估 Kimi K3 的精致网站构建过程，而不只看最终截图**

Viktor Oddy 发布 13 分钟教程，展示如何用 Kimi K3 构建获奖风格网站；完整视频提供了过程证据

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-78.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-78-poster.jpg" alt="Case 78 source video poster" height="360"></a>

[Play case 78 tutorial video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-78.mp4)

Type: Tutorial | Date: 2026-07-17

---

<a id="case-81"></a>
### Case 81: [构建滚动 Metaball 前端](https://x.com/abhinavflac/status/2078603131055993130) (by [@abhinavflac](https://x.com/abhinavflac))

**让 Kimi K3 生成 Awwwards 风格滚动页面，并检查数学效果是否能替代重型 mesh 或贴图资源。**

创作者报告一次 Kimi K3 前端会话生成了随滚动反应的 metaball 网站，视觉行为由数学驱动，没有使用 mesh 或贴图。附带视频是可见成品；来源没有公开可复用 prompt 或实现步骤。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-81.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-81-poster.jpg" alt="Case 81 source video poster" height="360"></a>

[Play case 81 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-81.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-82"></a>
### Case 82: [跨模型重设计个人网站](https://x.com/fabriciocarraro/status/2078574831466078265) (by [@fabriciocarraro](https://x.com/fabriciocarraro))

**用多个 coding harness 执行同一个网站重设计 brief，并比较耗时、视觉方向和与现有身份的匹配度。**

创作者用官方 harness 和最高 effort 模式测试 Fable 5、GPT-5.6 Sol 与 Kimi K3 重设计个人网站。Kimi K3 用时约 50 分钟，Fable 约 35 分钟，Sol 约 70 分钟；帖子把它定位为单任务 mini benchmark。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-82.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-82-poster.jpg" alt="Case 82 source video poster" height="360"></a>

[Play case 82 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-82.mp4)

Type: Evaluation | Date: 2026-07-18

---

<a id="case-86"></a>
### Case 86: [构建交互式头皮探索器](https://x.com/MiaAI_lab/status/2078508824752017757) (by [@MiaAI_lab](https://x.com/MiaAI_lab))

**用 Kimi K3 一次生成包含解剖层、响应式发丝和交互热点的 3D 教育场景。**

创作者报告 Kimi K3 用约 105k tokens 一次生成真实感头皮探索器，包含电影级光照、分层解剖结构、响应式发丝、横截面和教育热点。来源称效果令人印象深刻但成本不低，并提供可试用链接。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-86.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-86-poster.jpg" alt="Case 86 source video poster" height="360"></a>

[Play case 86 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-86.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-87"></a>
### Case 87: [分享 3D 地球仪仪表盘 Prompt](https://x.com/hqmank/status/2078465403349840144) (by [@hqmank](https://x.com/hqmank))

**研究 Kimi K3 3D 地球仪仪表盘的 prompt 与参考图设置，而不是只从最终图反推工作流。**

创作者回应他人对 Kimi K3 3D 地球仪仪表盘 demo 的 prompt 与参考图请求，并在附图中公开两者。本仓库将其记录为教程型 prompt 边界，但不从图片中转录 prompt 文本。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-87.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-87-poster.jpg" alt="Case 87 source video poster" height="360"></a>

[Play case 87 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-87.mp4)

Type: Tutorial | Date: 2026-07-18

---

<a id="case-94"></a>
### Case 94: [执行五项 UI UX 测试](https://x.com/MAXdeg0/status/2078855257686196399) (by [@MAXdeg0](https://x.com/MAXdeg0))

**不要只看一张 frontend 截图，而是用多项 UI、Logo 和 Figma MCP 任务评估 Kimi K3。**

MAXdeg0 报告用 Claude Code 和 Figma MCP server 对 Kimi K3 做了五项 UI/UX 与 logo 设计测试。来源列出 landing page 重建、hero section 重建和品牌设计等任务，并至少给出了 landing pass 的时间与成本。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-94.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-94-poster.jpg" alt="Case 94 source video poster" height="360"></a>

[Play case 94 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-94.mp4)

Type: Evaluation | Date: 2026-07-19

---

<a id="case-97"></a>
### Case 97: [从参考图创建 landing](https://x.com/MAXdeg0/status/2078776969072877715) (by [@MAXdeg0](https://x.com/MAXdeg0))

**用参考图板、Figma AI、Motion Sites 与 Kimi K3，把视觉方向转成可复用的 landing page section。**

MAXdeg0 描述了一个 landing page workflow：从 Pinterest 拉取风格参考，用 Figma AI remix 质感，或把 UI reference 加 prompt 粘进 Motion Sites，让 Kimi K3 构建页面。帖子还说该方法可复用于更多 section，并链接完整 prompting guide。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-97.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-97-poster.jpg" alt="Case 97 source video poster" height="360"></a>

[Play case 97 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-97.mp4)

Type: Tutorial | Date: 2026-07-19

---

<a id="case-103"></a>
### Case 103: [跟做高级网站教程](https://x.com/_guillecasaus/status/2079258261014908980) (by [@_guillecasaus](https://x.com/_guillecasaus))

**用这个案例评估 Kimi K3 在「跟做高级网站教程」任务中的实际工作流、成本或限制。**

来源帖提供了与 跟做高级网站教程 相关的公开证据，包括作者描述、结果媒体或基准/教程信息；本仓库只保留可核验事实，不补写未公开的 prompt 或步骤。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-103.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-103-poster.jpg" alt="Case 103 source video poster" height="360"></a>

[Play case 103 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-103.mp4)

Type: Tutorial | Date: 2026-07-20

---

<a id="case-106"></a>
### Case 106: [比较人形机器人前端成本](https://x.com/ChrisGPT/status/2079236298464796958) (by [@ChrisGPT](https://x.com/ChrisGPT))

**用这个案例评估 Kimi K3 在「比较人形机器人前端成本」任务中的实际工作流、成本或限制。**

来源帖提供了与 比较人形机器人前端成本 相关的公开证据，包括作者描述、结果媒体或基准/教程信息；本仓库只保留可核验事实，不补写未公开的 prompt 或步骤。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-106.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-106-poster.jpg" alt="Case 106 source video poster" height="360"></a>

[Play case 106 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-106.mp4)

Type: Benchmark | Date: 2026-07-20

---

<a id="case-115"></a>
### Case 115: [对比 Three.js Kimi-vs-GLM 构建](https://x.com/thehypedotnews/status/2079553731218325840) (by [@thehypedotnews](https://x.com/thehypedotnews))

**用同一组程序化 Three.js prompts 跑 Kimi K3 和 GLM 5.2，比较前端与 3D build 行为。**

The Hype 称对 Kimi K3 和 GLM 5.2 运行了三个单文件 HTML + Three.js prompts：带 CRT canvas texture 的 80 年代客厅、带传动系统运动学的公路车、以及玻璃水族箱场景。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-115.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-115-poster.jpg" alt="Case 115 source video poster" height="360"></a>

[Play case 115 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-115.mp4)

Type: Benchmark | Date: 2026-07-21

---

<a id="case-121"></a>
### Case 121: [用参考图生成落地页](https://x.com/Oluwaphilemon1/status/2079951300108697683) (by [@Oluwaphilemon1](https://x.com/Oluwaphilemon1))

**测试落地页生成时，给 Kimi K3 提供强视觉参考和分轮指导。**

Oluwaphilemon 描述了给 Kimi K3 一张图片参考和详细 prompt 来生成落地页的过程。来源指出 Kimi 起初尝试把自行车做成 3D 模型，经过几轮指导后得到更干净的结果。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-121.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-121-poster.jpg" alt="Case 121 source video poster" height="360"></a>

[Play case 121 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-121.mp4)

Type: Demo | Date: 2026-07-22

---

<a id="case-128"></a>
### Case 128: [模拟 3D 粒子系统](https://x.com/jadeferrara_/status/2079884161251262540) (by [@jadeferrara_](https://x.com/jadeferrara_))

**用粒子模拟 prompt 对比 Kimi K3 与闭源模型的运动质量。**

Jade Ferrara 报告给 Kimi K3 和 Opus 4.8 相同的 3D 粒子系统 prompt。来源称 Kimi 的分布更自然、运动更平滑、聚集和漂移更像物理过程，同时 API 成本更低。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-128.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-128-poster.jpg" alt="Case 128 source video poster" height="360"></a>

[Play case 128 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-128.mp4)

Type: Evaluation | Date: 2026-07-22

---

<a id="case-131"></a>
### Case 131: [构建深海解说流水线](https://x.com/N01ennn/status/2080391368644657460) (by [@N01ennn](https://x.com/N01ennn))

**把叙事型 prompt 转成包含场景、文字、运动和解释结构的可视化流水线。**

来源：N01ennn 展示了用 Kimi K3 生成深海主题解说内容的流程。该帖的有效信号是把叙事结构、视觉和动画串成一个具体 demo。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-131.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-131-poster.jpg" alt="Case 131 source video poster" height="360"></a>

[Play case 131 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-131.mp4)

Type: Demo | Date: 2026-07-23

---

<a id="case-133"></a>
### Case 133: [盲测落地页输出](https://x.com/contraben/status/2080329043639947338) (by [@contraben](https://x.com/contraben))

**在不揭示模型名称的 landing page 对比中评估 Kimi K3 的 frontend 输出。**

来源：contraben 发布了多个模型生成 landing page 的盲测。该案例记录一种视觉评估方法，不把它包装成通用 benchmark。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-133.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-133-poster.jpg" alt="Case 133 source video poster" height="360"></a>

[Play case 133 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-133.mp4)

Type: Benchmark | Date: 2026-07-23

---

<a id="case-134"></a>
### Case 134: [原型化机械 3D 细节](https://x.com/0xDominiqq/status/2080316573210784230) (by [@0xDominiqq](https://x.com/0xDominiqq))

**让 Kimi K3 生成带视觉细节和渲染约束的小型机械 3D 场景。**

来源：0xDominiqq 展示了用 Kimi K3 生成的机械或工业部件。有效信号限定为公开 demo 能支持的精细视觉原型能力。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-134.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-134-poster.jpg" alt="Case 134 source video poster" height="360"></a>

[Play case 134 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-134.mp4)

Type: Demo | Date: 2026-07-23

---

<a id="case-135"></a>
### Case 135: [复刻 Expo 移动端 UI](https://x.com/thebuggeddev/status/2080295524142587933) (by [@thebuggeddev](https://x.com/thebuggeddev))

**用移动 Expo UI 检查 Kimi K3 的结构、组件组织和视觉完成度。**

来源：thebuggeddev 分享了用 Kimi K3 复刻移动端界面的结果。该案例是 frontend 输出评估，不声称覆盖完整生产质量。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-135.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-135-poster.jpg" alt="Case 135 source video poster" height="360"></a>

[Play case 135 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-135.mp4)

Type: Evaluation | Date: 2026-07-23

---

<a id="case-139"></a>
### Case 139: [跟随网页设计教程](https://x.com/cyrilXBT/status/2080176332890345501) (by [@cyrilXBT](https://x.com/cyrilXBT))

**用完整 tutorial 观察 Kimi K3 如何搭建 layout、动效和视觉 polish。**

来源：cyrilXBT 分享了一个 13 分钟的 Kimi K3 自定义网站教程。该案例是 source-backed 教学 workflow，不是 prompt gallery。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-139.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-139-poster.jpg" alt="Case 139 source video poster" height="360"></a>

[Play case 139 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-139.mp4)

Type: Tutorial | Date: 2026-07-23

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

<a id="case-75"></a>
### Case 75: [将 Kimi 配置为 Codex 子 agent](https://x.com/nauczymycieAI/status/2078181182701736132) (by [@nauczymycieAI](https://x.com/nauczymycieAI))

**让 Codex 保持编排职责，把前端执行交给 Kimi K3 OpenCode 子 agent，并明确密钥边界**

nauczymycieAI 给出三阶段教程：安装并验证 OpenCode，手动创建且不粘贴到 Codex 的 Kimi API Key，连接 Kimi K3，并创建全局 Codex skill 路由前端任务

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-75.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-75.jpg" alt="Case 75 source image 1" height="360"></a>

Type: Tutorial | Date: 2026-07-17

---

<a id="case-79"></a>
### Case 79: [通过 ChatLLM 路由简单编码](https://x.com/abacusai/status/2078022418661257411) (by [@abacusai](https://x.com/abacusai))

**创建任务路由，将简单编码交给 Kimi K3，把困难编码和设计保留给其他模型**

Abacus AI 宣布 ChatLLM 支持 Kimi K3：简单编码用 Kimi K3，困难编码用 Fable 5，设计用 GPT-5.6 Sol；同一路由可用于 ChatLLM、Abacus AI agent 或 Claude Code

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-79.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-79.jpg" alt="Case 79 source image 1" height="360"></a>

Type: Integration | Date: 2026-07-17

---

<a id="case-91"></a>
### Case 91: [用生成资产构建 CS](https://x.com/karankendre/status/2078938615900688728) (by [@karankendre](https://x.com/karankendre))

**原型化小型 Counter-Strike 风格浏览器游戏时，用 Kimi K3 写游戏代码，用 GPT Image 2 生成资产。**

Karan Kendre 报告使用 Kimi K3 构建游戏、GPT Image 2 构建资产，做出一个 Counter-Strike 风格项目，总成本约 10 美元。源视频是可见成品，因此该记录更适合作为多工具组合 workflow，而不是 Kimi 单模型 benchmark。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-91.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-91-poster.jpg" alt="Case 91 source video poster" height="360"></a>

[Play case 91 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-91.mp4)

Type: Integration | Date: 2026-07-19

---

<a id="case-95"></a>
### Case 95: [使用 Command Code Design skill](https://x.com/MrAhmadAwais/status/2078841789205934547) (by [@MrAhmadAwais](https://x.com/MrAhmadAwais))

**在 token 预算内构建视觉游戏原型时，把 Kimi K3 与 Command Code 的专用 design skill 结合使用。**

Ahmad Awais 报告用 Kimi K3、Command Code 和 /design skill 构建 Forza 风追车视角游戏。帖子称整次 session 成本 0.97 美元，并包含道路/车辆比例、背景、动画、雾效等修复步骤，是具体的 agent harness workflow。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-95.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-95-poster.jpg" alt="Case 95 source video poster" height="360"></a>

[Play case 95 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-95.mp4)

Type: Integration | Date: 2026-07-19

---

<a id="case-109"></a>
### Case 109: [在 Claude Code 中运行 Kimi K3](https://x.com/boxmining/status/2079115758618239337) (by [@boxmining](https://x.com/boxmining))

**用这个案例评估 Kimi K3 在「在 Claude Code 中运行 Kimi K3」任务中的实际工作流、成本或限制。**

来源帖提供了与 在 Claude Code 中运行 Kimi K3 相关的公开证据，包括作者描述、结果媒体或基准/教程信息；本仓库只保留可核验事实，不补写未公开的 prompt 或步骤。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-109.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-109-poster.jpg" alt="Case 109 source video poster" height="360"></a>

[Play case 109 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-109.mp4)

Type: Integration | Date: 2026-07-20

---

<a id="case-119"></a>
### Case 119: [通过 claude-code-router 路由 Kimi](https://x.com/sairahul1/status/2079393675885588855) (by [@sairahul1](https://x.com/sairahul1))

**在现有 Claude Code workflow 中通过 claude-code-router 试用 Kimi K3，同时避免不必要的 proxy mode。**

Sai Rahul 描述 Moonshot 赞助的 claude-code-router Kimi K3 支持，包括内置 presets、API key 或订阅导入、原生订阅路由、余额和用量 dashboard、failover、缓存价格，并提醒除非需要否则保持 proxy mode 关闭。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-119.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-119-poster.jpg" alt="Case 119 source video poster" height="360"></a>

[Play case 119 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-119.mp4)

Type: Integration | Date: 2026-07-21

---

<a id="case-125"></a>
### Case 125: [运行开源 agent harness](https://x.com/ShenSeanChen/status/2079914609222221976) (by [@ShenSeanChen](https://x.com/ShenSeanChen))

**用共享 agent harness 对比 Kimi K3 与其他前沿模型在工具调用任务中的表现。**

Sean Chen 描述了在开源 AI agent harness 中让 Kimi K3 与多种模型竞赛：包含 agent loop、memory retrieval gate、工具调用、eval、tracing 和实时成本面板。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-125.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-125-poster.jpg" alt="Case 125 source video poster" height="360"></a>

[Play case 125 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-125.mp4)

Type: Benchmark | Date: 2026-07-22

---

<a id="case-129"></a>
### Case 129: [通过 Codex OAuth 运行 Kimi](https://x.com/biscuitweb3/status/2079844959843197342) (by [@biscuitweb3](https://x.com/biscuitweb3))

**当 Kimi K3 编码工作流需要避免手动配置 API key 时，使用 Codex OAuth 路径。**

biscuitweb3 报告 Kimi K3 已可通过 OAuth 在 Codex 内运行，无需额外 API key 设置。附图提供了该集成界面的证据。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-129-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-129-01.jpg" alt="Case 129 source image 1" height="360"></a>

Type: Integration | Date: 2026-07-22

---

<a id="case-136"></a>
### Case 136: [压力测试生产后端](https://x.com/hqmank/status/2080267878256005255) (by [@hqmank](https://x.com/hqmank))

**在更真实的 backend 流程中观察 Kimi K3 的集成、代码推理和限制。**

来源：hqmank 描述了在 production backend 场景中试用 Kimi K3。该案例按代码集成评估收录；本次没有执行独立付费 runtime test。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-136.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-136-poster.jpg" alt="Case 136 source video poster" height="360"></a>

[Play case 136 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-136.mp4)

Type: Evaluation | Date: 2026-07-23

---

<a id="case-137"></a>
### Case 137: [通过 opencodex 路由 Codex](https://x.com/cyrilXBT/status/2080252333829628163) (by [@cyrilXBT](https://x.com/cyrilXBT))

**把 Kimi K3 接入 Codex/opencodex 循环，做一个具体的 agent routing 集成实验。**

来源：cyrilXBT 分享了使用 Kimi K3 的 opencodex 配置。该案例记录工具集成，同时保留“公开配置”和“本地验证”之间的边界。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-137.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-137-poster.jpg" alt="Case 137 source video poster" height="360"></a>

[Play case 137 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-137.mp4)

Type: Integration | Date: 2026-07-23

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

<a id="case-72"></a>
### Case 72: [用相同 Arena prompt 比较前端](https://x.com/arena/status/2078240399517524365) (by [@arena](https://x.com/arena))

**固定 prompt 并并排检查输出，比只看一个排行榜分数更可靠**

Arena.ai 发布 Kimi K3 与 Fable 5 的 Frontend Code Arena 对比，并声明双方使用相同 prompt；视频保留两侧输出，便于检查实现和呈现差异

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-72.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-72-poster.jpg" alt="Case 72 source video poster" height="360"></a>

[Play case 72 comparison video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-72.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-74"></a>
### Case 74: [评测 Kimi Code 编码 agent](https://x.com/ArtificialAnlys/status/2078230240766345330) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**结合多个编码 agent 测试集和单任务成本评估 Kimi K3，不把单一前端榜单当成总体能力**

Artificial Analysis 报告 Kimi K3 在 Coding Agent Index 得分 57、并列第五；Terminal-Bench v2 为 84%，DeepSWE 为 64%，SWE-Atlas-QnA 为 23%，平均每任务成本 3.18 美元

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-74.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-74.jpg" alt="Case 74 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-17

---

<a id="case-76"></a>
### Case 76: [比较 Arena 与修复测试结果](https://x.com/AlphaSignalAI/status/2078172629496746183) (by [@AlphaSignalAI](https://x.com/AlphaSignalAI))

**同时看前端偏好和仓库修复评测，因为 Kimi K3 可在一个榜单第一、在另一测试中第七**

AlphaSignal 报告 Kimi K3 在 Frontend Code Arena 以 1679 分排名第一，但在编码 agent 修复测试中只完成 67 次尝试中的 53 次，即 79%，排名第七

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-76.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-76.jpg" alt="Case 76 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-17

---

<a id="case-80"></a>
### Case 80: [用 Prinzbench 评估 Kimi K3](https://x.com/deredleritt3r/status/2078606700496773166) (by [@deredleritt3r](https://x.com/deredleritt3r))

**用独立 benchmark 更新对比 Kimi K3 与开源、前沿模型在搜索、推理和一致性上的表现。**

作者把 Kimi K3 加入 Prinzbench，并报告总分 47/99，高于 GLM-5.2 的 30/99，接近旧版 Gemini 3.1 Pro 的 50/99。帖子强调它搜索能力强，但逻辑推理较弱，稳定性也不如可比前沿模型。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-80-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-80-01.png" alt="Case 80 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-18

---

<a id="case-85"></a>
### Case 85: [对比 ISS 数字孪生生成](https://x.com/AIsaOneHQ/status/2078519527588200536) (by [@AIsaOneHQ](https://x.com/AIsaOneHQ))

**用同 prompt 3D 挑战，对比 Kimi K3 与 GPT-5.6 Sol 在重建、控制、标签和视觉细节上的表现。**

AIsaOneHQ 报告一个 one-shot benchmark：两个模型都需要在没有预建模型的情况下重建可交互国际空间站数字孪生，包括地球、轨道光照、控制、标签、导览、爆炸视图、测试和优化。帖子称 Kimi K3 在该轮更快、更便宜，渲染效果更强。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-85.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-85-poster.jpg" alt="Case 85 source video poster" height="360"></a>

[Play case 85 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-85.mp4)

Type: Benchmark | Date: 2026-07-18

---

<a id="case-89"></a>
### Case 89: [评测 WebGPU 森林世界](https://x.com/stas_sorokin_/status/2078435840728908093) (by [@stas_sorokin_](https://x.com/stas_sorokin_))

**在长周期 Three.js 与 WebGPU 世界构建中，把 Kimi K3 作为 coding agent brain，从质量、速度、一致性和人工修改率评估它。**

创作者用一个梦幻森林湖泊世界深度评测 Kimi K3，场景包含动态水体、天气、野生动物、昼夜变化和电影镜头。帖子称 Kimi K3 质量很高，比类似 GPT-5.6 Sol 生成更慢，但长周期一致性好，只手动调整了一次湖面亮度。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-89.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-89-poster.jpg" alt="Case 89 source video poster" height="360"></a>

[Play case 89 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-89.mp4)

Type: Evaluation | Date: 2026-07-18

---

<a id="case-90"></a>
### Case 90: [比较玻璃屋同题提示](https://x.com/RoundtableSpace/status/2079004612070416755) (by [@RoundtableSpace](https://x.com/RoundtableSpace))

**用同一个建筑场景提示比较 Kimi K3 与 Opus 4.8 在氛围、光照和空间完整度上的差异。**

Roundtable Space 报告了 Kimi K3 与 Claude Opus 4.8 在接近价格下的同提示对比。Kimi 的结果被描述为蓝调时刻的玻璃屋、温暖室内光、反射水池和蓝图细节；Opus 的结果更偏字体设计，空间完成度较弱。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-90.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-90-poster.jpg" alt="Case 90 source video poster" height="360"></a>

[Play case 90 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-90.mp4)

Type: Evaluation | Date: 2026-07-20

---

<a id="case-92"></a>
### Case 92: [评测体素足球进球](https://x.com/0xzynex/status/2078920667542487230) (by [@0xzynex](https://x.com/0xzynex))

**把同一个纯 HTML/CSS/JS 足球动画提示交给两个模型，比较运动质量和成本。**

0xzynex 报告了一次同提示、一次生成、无重试的比较：Kimi K3 与 GPT-5.6 Sol High 都要在浏览器代码中生成方块风足球高光，包含盘带、进球、动态镜头和庆祝。帖子称 Kimi 动作更流畅且成本更低，视频保留了对比结果。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-92.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-92-poster.jpg" alt="Case 92 source video poster" height="360"></a>

[Play case 92 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-92.mp4)

Type: Benchmark | Date: 2026-07-19

---

<a id="case-93"></a>
### Case 93: [审看 Minecraft benchmark](https://x.com/ashen_one/status/2078892418976666071) (by [@ashen_one](https://x.com/ashen_one))

**在把发布 hype 或模型价格当作证据前，先看结构化 Minecraft 测评。**

ashen_one 发布了 Kimi K3 录屏测评，章节包括 hype 与现实、benchmark、定价、Minecraft 测试、首次运行 bug 和最终判断。这个来源把测评框架和早期可靠性问题放进一个可审看的视频中。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-93.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-93-poster.jpg" alt="Case 93 source video poster" height="360"></a>

[Play case 93 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-93.mp4)

Type: Benchmark | Date: 2026-07-19

---

<a id="case-98"></a>
### Case 98: [衡量 API 档位限制](https://x.com/mnmn94253156337/status/2078739859154620497) (by [@mnmn94253156337](https://x.com/mnmn94253156337))

**规划 Kimi K3 agent run 时，要看 token、tier、TPM 和 TPD，不只看模型标价。**

中文来源记录了一次个人 Kimi K3 API 试用：充值 5 美元后，setup 阶段约消耗 1.1 美元，随后触发 Tier0 限制。它列出输入、缓存输入、输出价格，以及 TPM/TPD 等限额概念，因此适合作为早期限制案例而非普遍定价结论。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-98.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-98-poster.jpg" alt="Case 98 source video poster" height="360"></a>

[Play case 98 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-98.mp4)

Type: Limit | Date: 2026-07-19

---

<a id="case-99"></a>
### Case 99: [比较 Limbo 风格 demo](https://x.com/ChrisGPT/status/2078679211116835017) (by [@ChrisGPT](https://x.com/ChrisGPT))

**在同一个游戏原型上比较 Kimi K3 与 Fable 5 的可玩范围、视觉打磨、成本和 bug。**

ChrisGPT 比较了 Fable 5 与 Kimi K3 的 Limbo clone demo。帖子称 Fable 输出 2,400 行代码、24K output tokens，成本 1.20 美元；Kimi 输出 3,000 行和 30K tokens，成本 0.12 美元，Kimi 增加了更多 gameplay，但 bug 也更多。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-99.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-99-poster.jpg" alt="Case 99 source video poster" height="360"></a>

[Play case 99 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-99.mp4)

Type: Benchmark | Date: 2026-07-19

---

<a id="case-100"></a>
### Case 100: [审查 VulcanBench 成本结果](https://x.com/morganlinton/status/2079358902194569357) (by [@morganlinton](https://x.com/morganlinton))

**用这个案例评估 Kimi K3 在「审查 VulcanBench 成本结果」任务中的实际工作流、成本或限制。**

来源帖提供了与 审查 VulcanBench 成本结果 相关的公开证据，包括作者描述、结果媒体或基准/教程信息；本仓库只保留可核验事实，不补写未公开的 prompt 或步骤。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-100-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-100-01.jpg" alt="Case 100 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-21

---

<a id="case-104"></a>
### Case 104: [评测双摆物理模拟](https://x.com/AlicanKiraz0/status/2079241239736504768) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**用这个案例评估 Kimi K3 在「评测双摆物理模拟」任务中的实际工作流、成本或限制。**

来源帖提供了与 评测双摆物理模拟 相关的公开证据，包括作者描述、结果媒体或基准/教程信息；本仓库只保留可核验事实，不补写未公开的 prompt 或步骤。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-104.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-104-poster.jpg" alt="Case 104 source video poster" height="360"></a>

[Play case 104 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-104.mp4)

Type: Benchmark | Date: 2026-07-20

---

<a id="case-107"></a>
### Case 107: [审查 ReactBench 生产就绪度](https://x.com/aidenybai/status/2079233934693650567) (by [@aidenybai](https://x.com/aidenybai))

**用这个案例评估 Kimi K3 在「审查 ReactBench 生产就绪度」任务中的实际工作流、成本或限制。**

来源帖提供了与 审查 ReactBench 生产就绪度 相关的公开证据，包括作者描述、结果媒体或基准/教程信息；本仓库只保留可核验事实，不补写未公开的 prompt 或步骤。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-107.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-107-poster.jpg" alt="Case 107 source video poster" height="360"></a>

[Play case 107 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-107.mp4)

Type: Benchmark | Date: 2026-07-20

---

<a id="case-110"></a>
### Case 110: [用 AA-Briefcase 评估 Kimi K3](https://x.com/ArtificialAnlys/status/2079715807983210572) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**先用 AA-Briefcase 结果判断 Kimi K3 的知识工作 agent 任务表现，再相信排行榜叙事。**

Artificial Analysis 报告称，Kimi K3 在 AA-Briefcase 上得到 1543 Elo，位列 Claude Fable 5 之后第二；同时该模型在这个基准中平均每个任务接近一小时，成本高于 Opus 4.8。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-110-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-110-01.jpg" alt="Case 110 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-21

---

<a id="case-113"></a>
### Case 113: [审计前端榜单限制](https://x.com/RetroChainer/status/2079622227796885850) (by [@RetroChainer](https://x.com/RetroChainer))

**用这条限制说明区分 Kimi K3 的榜单胜利和更宽泛的 coding、成本主张。**

RetroChainer 核实了 Frontend Code Arena 第一和公开价格，同时指出：该排名只适用于单一榜单；发帖时权重尚未公开；每任务节省来自单个任务；max reasoning 可能在小任务上消耗大量 tokens。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-113.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-113-poster.jpg" alt="Case 113 source video poster" height="360"></a>

[Play case 113 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-113.mp4)

Type: Limit | Date: 2026-07-21

---

<a id="case-114"></a>
### Case 114: [对比 StackPerf 架构结果](https://x.com/tamsi_besson/status/2079573266855834071) (by [@tamsi_besson](https://x.com/tamsi_besson))

**用 StackPerf 对比 Kimi K3 和 Qwen 3.8 的架构质量、速度和 tool call 行为。**

Tamsi Besson 分享的 StackPerf 快照显示，Kimi K3 在质量上略高于 Qwen 3.8 Max Preview，总体速度更快；但 Qwen 的失败 tool call 为 0，而 Kimi 虽调用更多工具却有 2 次失败。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-114-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-114-01.jpg" alt="Case 114 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-21

---

<a id="case-118"></a>
### Case 118: [对比 Monument Valley prompt 成本](https://x.com/AiHubMix/status/2079507420083294557) (by [@AiHubMix](https://x.com/AiHubMix))

**用单个 Monument Valley 风格 prompt 对比 Kimi K3 与其他模型的视觉质量、运行时间和成本。**

AiHubMix 用一个 Monument Valley 风格 prompt 对比 Claude Fable 5、Kimi K3 和 GPT-5.6 Sol。帖子称 Fable 最连贯，Kimi 最慢为 52m30s 且花费 $1.50，GPT-5.6 Sol 最快最便宜但空间逻辑较弱。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-118.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-118-poster.jpg" alt="Case 118 source video poster" height="360"></a>

[Play case 118 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-118.mp4)

Type: Benchmark | Date: 2026-07-21

---

<a id="case-120"></a>
### Case 120: [用 Surge 指数评估 Kimi K3](https://x.com/echen/status/2080021575190110523) (by [@echen](https://x.com/echen))

**用 SurgeAI 的分项结果区分 Kimi K3 在日常聊天中的优势，以及在企业 agent 和科学任务中的弱项。**

Eric Chen 报告 SurgeAI 在覆盖日常聊天机器人、企业 agent、深度推理和前沿科学的指数中测试了 Kimi K3。来源称 Kimi K3 在日常聊天上有竞争力，但在企业 agent 和科学任务上落后于 Fable 与 Sol。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-120-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-120-01.jpg" alt="Case 120 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-22

---

<a id="case-123"></a>
### Case 123: [评估 PDE 求解错误](https://x.com/lanyon_ai/status/2079931884511887740) (by [@lanyon_ai](https://x.com/lanyon_ai))

**用 PDE benchmark 失败案例判断 Kimi K3 在符号或数值任务中哪些环节需要额外验证。**

Lanyon AI 将其神经符号架构与包括 Kimi K3 在内的前沿模型，在简单线性 PDE 上进行比较。来源称，即使给出详细 prompt，前沿模型仍出现数学、算法和计算错误。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-123-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-123-01.jpg" alt="Case 123 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-22

---

<a id="case-124"></a>
### Case 124: [复查 ClinicalBench EHR 案例](https://x.com/mkurman88/status/2079918374977413534) (by [@mkurman88](https://x.com/mkurman88))

**用 ClinicalBench 的 EHR 案例检查 Kimi K3 哪些地方成功，哪些诊断推理仍会失败。**

Michael Kurman 报告 Kimi K3 在虚拟 EHR 沙盒中 10 个急诊案例的 ClinicalBench v0.0.4 结果。来源称 Kimi K3 解出 7/10，在第 6 个案例上耗时且未准确诊断。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-124-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-124-01.jpg" alt="Case 124 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-124-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-124-02.jpg" alt="Case 124 source image 2" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-124-03.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-124-03.jpg" alt="Case 124 source image 3" height="360"></a>

Type: Benchmark | Date: 2026-07-22

---

<a id="case-126"></a>
### Case 126: [评估报税计算能力](https://x.com/michaelrbock/status/2079913117698666964) (by [@michaelrbock](https://x.com/michaelrbock))

**不要假设前端强项会迁移到税务计算；应单独测试 Kimi K3 的该类负载。**

Michael Bock 报告用 50 份高度真实的联邦和州税表测试 Kimi K3。来源称 Kimi K3 在严格 TaxCalcBench 中得分 6%，GPT-5.6 Sol 为 58%，Fable 5 为 4%。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-126-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-126-01.jpg" alt="Case 126 source image 1" height="360"></a>

Type: Limit | Date: 2026-07-22

---

<a id="case-130"></a>
### Case 130: [复合 computer use 基准测试](https://x.com/YangFanYun/status/2080442432794325003) (by [@YangFanYun](https://x.com/YangFanYun))

**不只看合成分数，而是在复合 computer use 任务中比较 Kimi K3。**

来源：YangFanYun 把 Kimi K3 放在 Gemini 3、GPT-5 和 GLM 4.6 同场的复合 computer use benchmark 中。该案例作为自报告评测保留，用于观察长任务中的实际边界。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-130-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-130-01.jpg" alt="Case 130 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-23

---

<a id="related-resources"></a>
## 相关资源

- [查看 EvoLink 上的 Kimi K3 详情与价格](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=landing_overview)
- [查看 EvoLink Kimi K3 API 文档](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=docs_link)
- [进一步了解 EvoLink 上的 Kimi K3](https://evolink.ai/blog/is-kimi-k3-available-on-evolink?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_article)
- [KimiK3.io](https://kimik3.io/zh)
- EvoLink 模型页与 API 文档已验证，但尚未验证可安装的 Kimi K3 skill

<a id="acknowledge"></a>
## 🙏 致谢

感谢所有公开分享 Kimi K3 作品的创作者与从业者

[@ivanfioravanti](https://x.com/ivanfioravanti), [@TheAhmadOsman](https://x.com/TheAhmadOsman), [@HarshithLucky3](https://x.com/HarshithLucky3), [@chetaslua](https://x.com/chetaslua), [@abhinavflac](https://x.com/abhinavflac), [@bridgemindai](https://x.com/bridgemindai), [@Whats_AI](https://x.com/Whats_AI), [@chongdashu](https://x.com/chongdashu), [@MrAhmadAwais](https://x.com/MrAhmadAwais), [@bijanbowen](https://x.com/bijanbowen), [@CommandCodeAI](https://x.com/CommandCodeAI), [@emollick](https://x.com/emollick), [@nicky_sap](https://x.com/nicky_sap), [@Lentils80](https://x.com/Lentils80), [@scottstts](https://x.com/scottstts), [@aisearchio](https://x.com/aisearchio), [@gmi_cloud](https://x.com/gmi_cloud), [@karminski3](https://x.com/karminski3), [@VORTEX_Promos](https://x.com/VORTEX_Promos), [@rohanpaul_ai](https://x.com/rohanpaul_ai), [@mirochill](https://x.com/mirochill), [@aimlapi](https://x.com/aimlapi), [@minchoi](https://x.com/minchoi), [@doutorcaleb](https://x.com/doutorcaleb), [@adxtyahq](https://x.com/adxtyahq), [@higgsfield_ai](https://x.com/higgsfield_ai), [@AlicanKiraz0](https://x.com/AlicanKiraz0), [@1littlecoder](https://x.com/1littlecoder), [@op7418](https://x.com/op7418), [@adamuchigabriel](https://x.com/adamuchigabriel), [@s_batzoglou](https://x.com/s_batzoglou), [@servasyy_ai](https://x.com/servasyy_ai), [@filicroval](https://x.com/filicroval), [@doodlestein](https://x.com/doodlestein), [@dejavucoder](https://x.com/dejavucoder), [@Angaisb_](https://x.com/Angaisb_), [@AngryTomtweets](https://x.com/AngryTomtweets), [@Alezander907](https://x.com/Alezander907), [@teortaxesTex](https://x.com/teortaxesTex), [@jun_song](https://x.com/jun_song), [@ridark_eth](https://x.com/ridark_eth), [@naymur_dev](https://x.com/naymur_dev), [@tphuang](https://x.com/tphuang), [@TokenGremlin](https://x.com/TokenGremlin), [@IntuitMachine](https://x.com/IntuitMachine), [@wangfeng0315](https://x.com/wangfeng0315), [@twid](https://x.com/twid), [@pengchujin](https://x.com/pengchujin), [@aayushman2703](https://x.com/aayushman2703), [@goncalo_canhoto](https://x.com/goncalo_canhoto), [@LinearUncle](https://x.com/LinearUncle), [@gagarot200](https://x.com/gagarot200), [@MinLiBuilds](https://x.com/MinLiBuilds), [@izutorishima](https://x.com/izutorishima), [@X2worldtech](https://x.com/X2worldtech), [@Satvik_Pen](https://x.com/Satvik_Pen), [@hakki_alkan](https://x.com/hakki_alkan), [@BrianMRey](https://x.com/BrianMRey), [@ChrisGPT](https://x.com/ChrisGPT), [@arena](https://x.com/arena), [@MathiasHeide](https://x.com/MathiasHeide), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@nauczymycieAI](https://x.com/nauczymycieAI), [@AlphaSignalAI](https://x.com/AlphaSignalAI), [@Ananth7e](https://x.com/Ananth7e), [@viktoroddy](https://x.com/viktoroddy), [@abacusai](https://x.com/abacusai), [@deredleritt3r](https://x.com/deredleritt3r), [@fabriciocarraro](https://x.com/fabriciocarraro), [@startracker](https://x.com/startracker), [@mattwatkajtys](https://x.com/mattwatkajtys), [@AIsaOneHQ](https://x.com/AIsaOneHQ), [@MiaAI_lab](https://x.com/MiaAI_lab), [@hqmank](https://x.com/hqmank), [@prasenx](https://x.com/prasenx), [@stas_sorokin_](https://x.com/stas_sorokin_), [@RoundtableSpace](https://x.com/RoundtableSpace), [@karankendre](https://x.com/karankendre), [@0xzynex](https://x.com/0xzynex), [@ashen_one](https://x.com/ashen_one), [@MAXdeg0](https://x.com/MAXdeg0), [@ice_bearcute](https://x.com/ice_bearcute), [@mnmn94253156337](https://x.com/mnmn94253156337), [@morganlinton](https://x.com/morganlinton), [@vikktorrrre](https://x.com/vikktorrrre), [@kirillk_web3](https://x.com/kirillk_web3), [@_guillecasaus](https://x.com/_guillecasaus), [@demian_ai](https://x.com/demian_ai), [@aidenybai](https://x.com/aidenybai), [@LexnLin](https://x.com/LexnLin), [@boxmining](https://x.com/boxmining), [@Nekt_0](https://x.com/Nekt_0), [@RetroChainer](https://x.com/RetroChainer), [@tamsi_besson](https://x.com/tamsi_besson), [@thehypedotnews](https://x.com/thehypedotnews), [@AiHubMix](https://x.com/AiHubMix), [@sairahul1](https://x.com/sairahul1), [@echen](https://x.com/echen), [@Oluwaphilemon1](https://x.com/Oluwaphilemon1), [@diegocabezas01](https://x.com/diegocabezas01), [@lanyon_ai](https://x.com/lanyon_ai), [@mkurman88](https://x.com/mkurman88), [@ShenSeanChen](https://x.com/ShenSeanChen), [@michaelrbock](https://x.com/michaelrbock), [@Kirratr](https://x.com/Kirratr), [@jadeferrara_](https://x.com/jadeferrara_), [@biscuitweb3](https://x.com/biscuitweb3), [@YangFanYun](https://x.com/YangFanYun), [@N01ennn](https://x.com/N01ennn), [@DilumSanjaya](https://x.com/DilumSanjaya), [@contraben](https://x.com/contraben), [@0xDominiqq](https://x.com/0xDominiqq), [@thebuggeddev](https://x.com/thebuggeddev), [@cyrilXBT](https://x.com/cyrilXBT)

*如需更正归属或文字，请附公开来源创建 issue*
