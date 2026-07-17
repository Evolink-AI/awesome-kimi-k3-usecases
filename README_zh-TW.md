<div align="center">

<a href="https://evolink.ai/kimi-k3?utm_source=github&utm_medium=banner&utm_campaign=awesome-kimi-k3-usecases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/images/zh-TW-v2.png" alt="帶月面場景與 EvoLink 使用入口的繁體中文 Kimi K3 banner" width="760"></a>

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

# Kimi K3 精選使用案例

## 🍌 簡介

歡迎來到 Kimi K3 高訊號使用案例庫

**我們收錄具有公開來源的遊戲、3D 場景、動態設計、整合、評估與實務限制**

本版收錄指定來源中全部 70 個 high-confidence 案例，並排除全部 31 個 medium-confidence 項目；標題與作者名稱都連回原始貼文與個人頁面

[EvoLink](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=introduction_cta)

## 📊 概覽

- 70 個來自創作者與實務工作者的 high-confidence 案例，完整納入且沒有挑漏
- 廣泛涵蓋互動遊戲、Three.js、動態設計、前端、研究、評估、工具整合與實務限制
- 每個案例保留來源、作者、類型、日期與 prompt 邊界
- 排除全部 31 個 medium-confidence 項目，也不把個人觀察包裝成 benchmark

> [!NOTE]
> 本案例庫優先採用具體證據，不補寫未公開的 prompt 或設定步驟

## ⚡ 快速開始

EvoLink 文件記載的模型 ID 為 `kimi-k3`，模型詳情頁與 Chat Completions API 文件均已提供

1. [查看 EvoLink 上的 Kimi K3 詳情與價格](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-kimi-k3-usecases&utm_content=model_link)
2. [建立或管理 EvoLink API 金鑰](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-kimi-k3-usecases&utm_content=api_key)
3. [查看 EvoLink Kimi K3 API 文件](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=first_run)

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
> EvoLink 模型頁與 API 文件驗證了公開路由和模型 ID，本案例庫不聲稱已獨立完成付費 API 測試

## 📑 目錄

| Section | Cases |
|---|---|
| [互動遊戲與 3D](#games-3d) | 22 |
| [前端與動態設計](#frontend-motion) | 15 |
| [程式開發與整合](#coding-integrations) | 8 |
| [評估與限制](#evaluation-limits) | 25 |
| [致謝](#acknowledge) | 致謝與更正 |

<a id="games-3d"></a>
## 🎮 互動遊戲與 3D

| Case | What it shows | Type |
|---|---|---|
| [用一個 prompt 建立 voxel pod racer](#case-1) | 從簡短場景概念做出競速原型，再界定下一輪改善內容 | Demo |
| [用相同 prompt 比較 Frogger](#case-2) | 固定 prompt 來檢查不同模型的輸出差異 | Evaluation |
| [產生 Frogger 與遊玩錄影](#case-3) | 分別以一次生成測試遊戲與錄影流程 | Demo |
| [用 Three.js 製作航空母艦原型](#case-4) | 以具體起降場景測試互動式 3D 生成 | Demo |
| [用代理工具製作 Paper Mario 風格遊戲](#case-9) | 結合 Kimi K3、代理 harness 與素材工具，同時產出 2D 與 3D 遊戲元素 | Demo |
| [生成地鐵場景第一人稱射擊遊戲](#case-11) | 用具體的地鐵場景檢視生成的第一人稱射擊遊戲成果 | Demo |
| [使用 Blender MCP 建模 V8 引擎](#case-19) | 透過 Blender MCP 與單次要求生成精細的機械 3D 模型 | Integration |
| [從一個參考建立可玩的戰鬥競技場](#case-23) | 用單一參考測試一次生成完整可玩競技場的能力 | Demo |
| [將三款自動遊玩的復古遊戲做成 HTML 檔](#case-24) | 要求在獨立 HTML 遊戲檔中包含圖形、敵人、規則與自動遊玩 | Benchmark |
| [一次生成變色龍捉迷藏遊戲](#case-27) | 生成包含顏色配對、程序式區域、聲音與多回合計分的單檔遊戲 | Benchmark |
| [用代理工具鏈建立 2.5D Paper Mario 類遊戲](#case-36) | 結合 Kimi K3、Grok Build 或 Claude Code 以及 Spriterrific，組成 2.5D 遊戲工作流程 | Tutorial |
| [建立瀏覽器版 3D 武俠 RPG](#case-43) | 結合近戰、任務、物品欄、天氣、室內探索、Blender 環境製作與改編素材 | Demo |
| [建立瀏覽器多人 Minecraft 類遊戲](#case-44) | 在有邊界的時間與成本執行中，產出可線上多人遊玩的瀏覽器遊戲 | Demo |
| [重現分割畫面合作瀏覽器遊戲](#case-48) | 用一個要求生成瀏覽器分割畫面合作玩法與即時環境互動 | Demo |
| [使用 Command Code 設計模式生成可玩遊戲](#case-49) | 用 Command Code 的 design 指令一次生成遊戲，並記錄成果是否可玩 | Demo |
| [組裝具一致性的武俠瀏覽器 RPG](#case-51) | 在一款遊戲中整合移動、戰鬥、任務、物品欄、天氣、探索與 3D 環境製作 | Demo |
| [建立可玩的 Hollow Knight 跨界遊戲](#case-54) | 使用既有遊戲素材，建立 Knight 與 Kimi 對戰的可玩遊戲 | Demo |
| [一次生成 Fall Guys 風格 3D 瀏覽器遊戲](#case-60) | 用一次生成要求製作可玩的 3D 障礙遊戲，並公開專案供檢查 | Demo |
| [建立並自行測試末日里斯本 FPS](#case-61) | 用一個 maximum-effort prompt 執行，在交付可玩 FPS 前反覆測試、截圖與迭代 | Demo |
| [從簡單要求生成 Animal Crossing 風格遊戲](#case-63) | 用極簡遊戲簡述檢視可玩性、遊戲迴圈與視差效果 | Demo |
| [從一句簡述生成 Mario 類遊戲](#case-65) | 用極簡的一次生成要求檢視可玩性、關卡設計、像素美術與視差 | Demo |
| [建立可運作的殭屍第一人稱射擊遊戲](#case-67) | 用具體的殭屍射擊目標檢視完整可玩的 FPS 成果 | Demo |

<a id="case-1"></a>
### Case 1: [用一個 prompt 建立 voxel pod racer](https://x.com/ivanfioravanti/status/2077763009657627055) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**從簡短場景概念做出競速原型，再界定下一輪改善內容**

創作者表示 Kimi K3 以一個公開 prompt 產出初版，下一版將加入更多賽車、終點線與細節檢查

**Prompt:**

```text
Voxel star wars pod-racers run
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01-poster.jpg" alt="Case 1 video poster" height="360"></a>

[Play case 1 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-2"></a>
### Case 2: [用相同 prompt 比較 Frogger](https://x.com/ivanfioravanti/status/2077754781964054825) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**固定 prompt 來檢查不同模型的輸出差異**

創作者用 Kimi K3 版本做同 prompt 比較，但來源沒有公開 prompt 內容或評分規則

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02-poster.jpg" alt="Case 2 video poster" height="360"></a>

[Play case 2 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-3"></a>
### Case 3: [產生 Frogger 與遊玩錄影](https://x.com/TheAhmadOsman/status/2077776567292338285) (by [@TheAhmadOsman](https://x.com/TheAhmadOsman))

**分別以一次生成測試遊戲與錄影流程**

創作者表示遊戲與錄影流程各由一次生成完成，但沒有公開完整 prompt

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03-poster.jpg" alt="Case 3 video poster" height="360"></a>

[Play case 3 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-4"></a>
### Case 4: [用 Three.js 製作航空母艦原型](https://x.com/HarshithLucky3/status/2077753222018814360) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**以具體起降場景測試互動式 3D 生成**

創作者展示尼米茲級航空母艦的戰機起飛與回收，並對 3D 生成給出正面評價

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04-poster.jpg" alt="Case 4 video poster" height="360"></a>

[Play case 4 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-9"></a>
### Case 9: [用代理工具製作 Paper Mario 風格遊戲](https://x.com/chongdashu/status/2077886028866531655) (by [@chongdashu](https://x.com/chongdashu))

**結合 Kimi K3、代理 harness 與素材工具，同時產出 2D 與 3D 遊戲元素**

創作者表示在 Paper Mario 風格遊戲中使用 Kimi K3 搭配 Grok Build、以 Spriterrific 製作 2D 素材，並以幾何工具製作 3D 素材；來源展示了工具與 skill 的使用，但未公開可重用的完整 prompt

Type: Demo | Date: 2026-07-16

---

<a id="case-11"></a>
### Case 11: [生成地鐵場景第一人稱射擊遊戲](https://x.com/bijanbowen/status/2077881805751873997) (by [@bijanbowen](https://x.com/bijanbowen))

**用具體的地鐵場景檢視生成的第一人稱射擊遊戲成果**

創作者展示歸因於 Kimi K3 的地鐵 FPS，並明確指出無法確定網紅身分是否影響結果；來源未提供 prompt 或可重現工作流程

Type: Demo | Date: 2026-07-16

---

<a id="case-19"></a>
### Case 19: [使用 Blender MCP 建模 V8 引擎](https://x.com/aisearchio/status/2077962156147146925) (by [@aisearchio](https://x.com/aisearchio))

**透過 Blender MCP 與單次要求生成精細的機械 3D 模型**

評論者表示 Kimi K3 以 Blender MCP 從一個 prompt 生成完整 V8 引擎；貼文連結到更完整的評論，但指定記錄未揭露完整 prompt

Type: Integration | Date: 2026-07-17

---

<a id="case-23"></a>
### Case 23: [從一個參考建立可玩的戰鬥競技場](https://x.com/VORTEX_Promos/status/2077879705378730074) (by [@VORTEX_Promos](https://x.com/VORTEX_Promos))

**用單一參考測試一次生成完整可玩競技場的能力**

創作者表示 Kimi K3 從一個參考一次生成可玩的戰鬥競技場；貼文另含排行榜主張，但具體使用案例是所展示的競技場成果

Type: Demo | Date: 2026-07-16

---

<a id="case-24"></a>
### Case 24: [將三款自動遊玩的復古遊戲做成 HTML 檔](https://x.com/rohanpaul_ai/status/2077889084761206860) (by [@rohanpaul_ai](https://x.com/rohanpaul_ai))

**要求在獨立 HTML 遊戲檔中包含圖形、敵人、規則與自動遊玩**

來源報告 Atomic Chat 的比較，模型將 Road Fighter、Battle City 與 Q*bert 製作成可自動遊玩的 HTML 檔；成本與品質比較由發布者報告，本案例庫未獨立重現

Type: Benchmark | Date: 2026-07-16

---

<a id="case-27"></a>
### Case 27: [一次生成變色龍捉迷藏遊戲](https://x.com/aimlapi/status/2077898742179459274) (by [@aimlapi](https://x.com/aimlapi))

**生成包含顏色配對、程序式區域、聲音與多回合計分的單檔遊戲**

AIMLAPI 報告以相同 prompt 一次生成捉迷藏遊戲，並列出 $3.11 對應 Kimi K3、$12.23 對應 Fable 5；功能與成本主張均為供應商報告結果

Type: Benchmark | Date: 2026-07-16

---

<a id="case-36"></a>
### Case 36: [用代理工具鏈建立 2.5D Paper Mario 類遊戲](https://x.com/chongdashu/status/2077981621223837739) (by [@chongdashu](https://x.com/chongdashu))

**結合 Kimi K3、Grok Build 或 Claude Code 以及 Spriterrific，組成 2.5D 遊戲工作流程**

創作者提供使用 Grok Build 與 Kimi K3 的完整操作示範，並展示以 Spriterrific 生成 sprite；來源標明工具，但沒有提供可重用的完整 prompt

Type: Tutorial | Date: 2026-07-17

---

<a id="case-43"></a>
### Case 43: [建立瀏覽器版 3D 武俠 RPG](https://x.com/AngryTomtweets/status/2077868163136450619) (by [@AngryTomtweets](https://x.com/AngryTomtweets))

**結合近戰、任務、物品欄、天氣、室內探索、Blender 環境製作與改編素材**

來源報告一款 Kimi K3 瀏覽器 RPG，包含近戰、任務、物品欄、動態天氣與可探索室內空間，另含 Blender 建模、碰撞改善、PBR 重新貼圖與改編開放素材

Type: Demo | Date: 2026-07-16

---

<a id="case-44"></a>
### Case 44: [建立瀏覽器多人 Minecraft 類遊戲](https://x.com/Alezander907/status/2077926014710407407) (by [@Alezander907](https://x.com/Alezander907))

**在有邊界的時間與成本執行中，產出可線上多人遊玩的瀏覽器遊戲**

創作者表示 Kimi K3 在一小時內以 $6.57 成本建立可在瀏覽器遊玩的多人 Minecraft 類遊戲；這些是單一成果的自行報告數字

Type: Demo | Date: 2026-07-17

---

<a id="case-48"></a>
### Case 48: [重現分割畫面合作瀏覽器遊戲](https://x.com/ridark_eth/status/2077882889803378969) (by [@ridark_eth](https://x.com/ridark_eth))

**用一個要求生成瀏覽器分割畫面合作玩法與即時環境互動**

創作者表示 Kimi K3 用一個 prompt 製作 It Takes Two 風格瀏覽器遊戲，Mario 與 Luigi 能以分割畫面即時彼此及與環境互動

Type: Demo | Date: 2026-07-16

---

<a id="case-49"></a>
### Case 49: [使用 Command Code 設計模式生成可玩遊戲](https://x.com/naymur_dev/status/2077873562661335207) (by [@naymur_dev](https://x.com/naymur_dev))

**用 Command Code 的 design 指令一次生成遊戲，並記錄成果是否可玩**

創作者表示使用 Command Code design 模式進行一次生成比較，Kimi K3 執行以 $0.038 產出可玩遊戲；此成本與品質結果為自行報告

Type: Demo | Date: 2026-07-16

---

<a id="case-51"></a>
### Case 51: [組裝具一致性的武俠瀏覽器 RPG](https://x.com/TokenGremlin/status/2077855657068310620) (by [@TokenGremlin](https://x.com/TokenGremlin))

**在一款遊戲中整合移動、戰鬥、任務、物品欄、天氣、探索與 3D 環境製作**

來源報告 Kimi K3 的武俠風格瀏覽器 RPG 結合近戰、任務、物品欄、動態天氣、可探索室內空間與具一致性的 3D 遊玩結構

Type: Demo | Date: 2026-07-16

---

<a id="case-54"></a>
### Case 54: [建立可玩的 Hollow Knight 跨界遊戲](https://x.com/wangfeng0315/status/2077933531200991583) (by [@wangfeng0315](https://x.com/wangfeng0315))

**使用既有遊戲素材，建立 Knight 與 Kimi 對戰的可玩遊戲**

自稱在 Kimi 工作的創作者表示使用 Hollow Knight 素材製作一款 Knight 對戰 Kimi 的遊戲，並提供公開遊玩連結；歸屬與評估應考量此從屬關係

Type: Demo | Date: 2026-07-17

---

<a id="case-60"></a>
### Case 60: [一次生成 Fall Guys 風格 3D 瀏覽器遊戲](https://x.com/aayushman2703/status/2077857886441783526) (by [@aayushman2703](https://x.com/aayushman2703))

**用一次生成要求製作可玩的 3D 障礙遊戲，並公開專案供檢查**

創作者表示 Kimi K3 一次生成 Fall Guys 風格瀏覽器遊戲，並稱來源連結了 prompt 與 GitHub 專案；此記錄未重現該 prompt

Type: Demo | Date: 2026-07-16

---

<a id="case-61"></a>
### Case 61: [建立並自行測試末日里斯本 FPS](https://x.com/goncalo_canhoto/status/2077863166655037668) (by [@goncalo_canhoto](https://x.com/goncalo_canhoto))

**用一個 maximum-effort prompt 執行，在交付可玩 FPS 前反覆測試、截圖與迭代**

創作者表示 Kimi K3 經過約一小時的反覆測試、截圖與迭代後，產出可玩的末日里斯本瀏覽器 FPS；時間與流程細節皆為自行報告

Type: Demo | Date: 2026-07-16

---

<a id="case-63"></a>
### Case 63: [從簡單要求生成 Animal Crossing 風格遊戲](https://x.com/gagarot200/status/2077949230287896830) (by [@gagarot200](https://x.com/gagarot200))

**用極簡遊戲簡述檢視可玩性、遊戲迴圈與視差效果**

創作者表示 Kimi K3 從非常簡單的 prompt 生成完全可玩的 Animal Crossing 風格遊戲，包含遊戲迴圈與視差效果；指定記錄沒有完整原文

Type: Demo | Date: 2026-07-17

---

<a id="case-65"></a>
### Case 65: [從一句簡述生成 Mario 類遊戲](https://x.com/izutorishima/status/2077939370154475992) (by [@izutorishima](https://x.com/izutorishima))

**用極簡的一次生成要求檢視可玩性、關卡設計、像素美術與視差**

創作者表示 Kimi K3 從單句簡述產出可正常運作且無明顯錯誤的 Mario 類遊戲，包含關卡結構與視差；同一份報告也批評音樂與圖像品質

Type: Demo | Date: 2026-07-17

---

<a id="case-67"></a>
### Case 67: [建立可運作的殭屍第一人稱射擊遊戲](https://x.com/X2worldtech/status/2077902793449296203) (by [@X2worldtech](https://x.com/X2worldtech))

**用具體的殭屍射擊目標檢視完整可玩的 FPS 成果**

來源展示歸因於 Kimi K3 的完整可運作殭屍 FPS；來源未提供 prompt、實作細節或外部遊玩評估

> [!WARNING]
> The original source permalink returned HTTP 404 during the 2026-07-17 audit. Attribution and evidence are preserved from the supplied high-confidence source package.

Type: Demo | Date: 2026-07-16

---


<a id="frontend-motion"></a>
## 🎨 前端與動態設計

| Case | What it shows | Type |
|---|---|---|
| [建立可互動的動態前端](#case-5) | 製作暫停動畫後仍可互動的動態圖形 | Demo |
| [製作同步的動態廣告](#case-6) | 檢查音樂、效果與動作是否同步 | Demo |
| [完全用程式碼製作動態設計](#case-14) | 測試一次生成的程式開發流程能否在沒有輔助生成工具時完成動態設計 | Demo |
| [研究人物並建立動畫個人網站](#case-15) | 提供寬泛的個人網站簡述，再檢視模型的研究、規劃、迭代與瀏覽器驗證流程 | Tutorial |
| [生成黑洞模擬](#case-17) | 用科學視覺化任務檢視生成的黑洞模擬 | Demo |
| [測試複雜前端建模、粒子與 shader](#case-22) | 使用公開前端 prompt，在一次執行中檢視建模精度、粒子效果與行內 shader 生成 | Demo |
| [一次生成程序式音樂工具](#case-26) | 測試一次生成互動式程序音樂產生器，並審慎比較可見成果 | Demo |
| [從兩張圖片建立 Three.js 產品頁](#case-33) | 使用兩張參考圖片與明確的 Three.js 要求生成產品展示頁 | Demo |
| [發明豪華麵包切割器及其產品頁](#case-39) | 在單一設計成果中結合產品構想、爆炸圖、示範與登陸頁 | Demo |
| [生成十秒遞迴鵜鶘 GIF](#case-45) | 用完整指定的循環動畫簡述，檢視 GIF 的敘事連續性與遞迴效果 | Demo |
| [生成 BMW M4 CS 側視 SVG](#case-55) | 用指定車款與視角檢視向量插畫輸出 | Demo |
| [透過截圖回饋重現 Gargantua](#case-58) | 把反覆截圖當作觀察資料，用來診斷並改善科學視覺化 | Tutorial |
| [以 62 張截圖改善黑洞視覺化](#case-66) | 使用截圖回饋迴圈，在多次迭代中讀取、診斷並修正視覺模擬 | Tutorial |
| [製作後訓練行銷 PDF](#case-68) | 用指定產品與交付格式生成行銷文件 | Demo |
| [用一個 prompt 建立使用者介面](#case-70) | 用單次要求生成並檢視完整 UI 設計 | Demo |

<a id="case-5"></a>
### Case 5: [建立可互動的動態前端](https://x.com/chetaslua/status/2077749371144442022) (by [@chetaslua](https://x.com/chetaslua))

**製作暫停動畫後仍可互動的動態圖形**

創作者表示整個製作耗時 42 分鐘、一次生成、只用簡單程式碼，沒有 harness、MCP 或 skill

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05-poster.jpg" alt="Case 5 video poster" height="360"></a>

[Play case 5 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-6"></a>
### Case 6: [製作同步的動態廣告](https://x.com/abhinavflac/status/2077760297918484667) (by [@abhinavflac](https://x.com/abhinavflac))

**檢查音樂、效果與動作是否同步**

創作者表示以純 prompt 一次產出 Spotify 風格廣告，但沒有公開完整 prompt

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06-poster.jpg" alt="Case 6 video poster" height="360"></a>

[Play case 6 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-14"></a>
### Case 14: [完全用程式碼製作動態設計](https://x.com/chetaslua/status/2077952938564354503) (by [@chetaslua](https://x.com/chetaslua))

**測試一次生成的程式開發流程能否在沒有輔助生成工具時完成動態設計**

創作者表示 Kimi K3 一次生成的動態設計完全由程式碼完成，未使用 MCP、skill、工具、影片生成或特殊 prompt；來源未提供完整 prompt

Type: Demo | Date: 2026-07-17

---

<a id="case-15"></a>
### Case 15: [研究人物並建立動畫個人網站](https://x.com/nicky_sap/status/2077857190707429411) (by [@nicky_sap](https://x.com/nicky_sap))

**提供寬泛的個人網站簡述，再檢視模型的研究、規劃、迭代與瀏覽器驗證流程**

創作者表示 Kimi K3 研究 Nick Saponaro，並依寬泛要求製作動畫個人網站，過程包含規劃、測試、迭代與瀏覽器檢查；此成果是自行報告的工作流程展示

Type: Tutorial | Date: 2026-07-16

---

<a id="case-17"></a>
### Case 17: [生成黑洞模擬](https://x.com/chetaslua/status/2077961850352971796) (by [@chetaslua](https://x.com/chetaslua))

**用科學視覺化任務檢視生成的黑洞模擬**

創作者展示歸因於 Kimi K3 的黑洞模擬，並稱其為所見最佳；來源提供可見成果，但沒有 prompt、評分標準或獨立驗證

Type: Demo | Date: 2026-07-17

---

<a id="case-22"></a>
### Case 22: [測試複雜前端建模、粒子與 shader](https://x.com/karminski3/status/2077889959223337099) (by [@karminski3](https://x.com/karminski3))

**使用公開前端 prompt，在一次執行中檢視建模精度、粒子效果與行內 shader 生成**

創作者表示 Kimi K3 一次執行的前端成果涵蓋精密建模、粒子效果與複雜行內 shader 程式碼，並指出測試 prompt 已在連結來源公開

Type: Demo | Date: 2026-07-16

---

<a id="case-26"></a>
### Case 26: [一次生成程序式音樂工具](https://x.com/mirochill/status/2077723551331758478) (by [@mirochill](https://x.com/mirochill))

**測試一次生成互動式程序音樂產生器，並審慎比較可見成果**

創作者表示 Kimi K3 一次生成程序式音樂工具，並認為其成果優於 Fable 5 與 GPT-5.6 Sol；這是創作者自己的測試集，不是標準化基準

Type: Demo | Date: 2026-07-16

---

<a id="case-33"></a>
### Case 33: [從兩張圖片建立 Three.js 產品頁](https://x.com/1littlecoder/status/2077890296806031665) (by [@1littlecoder](https://x.com/1littlecoder))

**使用兩張參考圖片與明確的 Three.js 要求生成產品展示頁**

創作者表示 Kimi K3 從兩張圖片設計產品頁，並產出明確要求的 Three.js 版本；來源未提供更多 prompt 或實作細節

Type: Demo | Date: 2026-07-16

---

<a id="case-39"></a>
### Case 39: [發明豪華麵包切割器及其產品頁](https://x.com/filicroval/status/2077871090731221438) (by [@filicroval](https://x.com/filicroval))

**在單一設計成果中結合產品構想、爆炸圖、示範與登陸頁**

創作者表示 Kimi K3 發明斷頭台式麵包切割器，將其定位為豪華產品，並產出含爆炸圖與示範的登陸頁

Type: Demo | Date: 2026-07-16

---

<a id="case-45"></a>
### Case 45: [生成十秒遞迴鵜鶘 GIF](https://x.com/1littlecoder/status/2077880380900937865) (by [@1littlecoder](https://x.com/1littlecoder))

**用完整指定的循環動畫簡述，檢視 GIF 的敘事連續性與遞迴效果**

來源包含一段 prompt，要求製作十秒循環 GIF：一隻鵜鶘騎自行車，透過簡訊收到同一支影片，鏡頭再放大；創作者展示 Kimi K3 產出的動畫

Type: Demo | Date: 2026-07-16

---

<a id="case-55"></a>
### Case 55: [生成 BMW M4 CS 側視 SVG](https://x.com/HarshithLucky3/status/2077765821380886942) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**用指定車款與視角檢視向量插畫輸出**

創作者展示歸因於 Kimi K3 Max 的 BMW M4 CS 側視 SVG；指定來源包含成果，但沒有 prompt 或製作步驟

Type: Demo | Date: 2026-07-16

---

<a id="case-58"></a>
### Case 58: [透過截圖回饋重現 Gargantua](https://x.com/AngryTomtweets/status/2077868981659324444) (by [@AngryTomtweets](https://x.com/AngryTomtweets))

**把反覆截圖當作觀察資料，用來診斷並改善科學視覺化**

來源表示 Kimi K3 透過 62 張自行截圖重現 Interstellar 的 Gargantua，每次讀取結果、診斷問題，再迭代採取行動

Type: Tutorial | Date: 2026-07-16

---

<a id="case-66"></a>
### Case 66: [以 62 張截圖改善黑洞視覺化](https://x.com/TokenGremlin/status/2077855959201042645) (by [@TokenGremlin](https://x.com/TokenGremlin))

**使用截圖回饋迴圈，在多次迭代中讀取、診斷並修正視覺模擬**

來源表示 Kimi K3 透過觀察並改善 62 張截圖的輸出，重建 Interstellar 的 Gargantua；這展示所報告的回饋迴圈，而不是獨立驗證其物理準確性

Type: Tutorial | Date: 2026-07-16

---

<a id="case-68"></a>
### Case 68: [製作後訓練行銷 PDF](https://x.com/Satvik_Pen/status/2077859673517023313) (by [@Satvik_Pen](https://x.com/Satvik_Pen))

**用指定產品與交付格式生成行銷文件**

創作者表示要求 Kimi K3 製作 Thinking Machines 的 Inkling 後訓練行銷 PDF，並分享成果，同時稱讚幕後流程；來源未提供 prompt 或評估標準

Type: Demo | Date: 2026-07-16

---

<a id="case-70"></a>
### Case 70: [用一個 prompt 建立使用者介面](https://x.com/BrianMRey/status/2077891942088671689) (by [@BrianMRey](https://x.com/BrianMRey))

**用單次要求生成並檢視完整 UI 設計**

創作者展示歸因於 Kimi K3 單一 prompt 執行的 UI 設計，並給予非常正面的主觀評價；來源未提供完整 prompt 或評分標準

Type: Demo | Date: 2026-07-16

---


<a id="coding-integrations"></a>
## 💻 程式開發與整合

| Case | What it shows | Type |
|---|---|---|
| [製作具備可用 macOS 的虛擬 MacBook](#case-18) | 結合 Three.js 硬體渲染與可互動的瀏覽器作業系統模擬 | Demo |
| [從 DSL 到 PTX 建立 GPU 編譯器](#case-25) | 用端到端編譯器任務涵蓋 DSL、編譯器 pass、PTX 生成與 Tensor Core 路徑 | Demo |
| [以 WebGL2 建立即時黑洞光線追蹤器](#case-32) | 測試用一個 prompt 在單一 HTML 檔內生成原生 WebGL2 測地線光線追蹤器 | Benchmark |
| [以 mGBA WASM 為核心建立 Game Boy Advance 模擬器](#case-46) | 整合授權 3D 模型與真正的模擬器核心，再透過遞迴方式改善介面與遊玩體驗 | Integration |
| [從中文來源研究多個主題](#case-50) | 透過長時間研究任務比較不同模型世代的完整度與延遲 | Evaluation |
| [在瀏覽器複製具可用應用程式的 macOS](#case-56) | 建立包含音樂、瀏覽器與電子郵件應用程式的瀏覽器作業系統模擬 | Demo |
| [建立 FaceTime 可運作的 macOS 模擬](#case-62) | 用虛擬作業系統任務測試生成的應用互動是否能運作 | Demo |
| [加入雙任務前端效果比較器](#case-64) | 建立工具以選取兩個已完成任務、並列顯示，並同步視角與互動 | Tutorial |

<a id="case-18"></a>
### Case 18: [製作具備可用 macOS 的虛擬 MacBook](https://x.com/scottstts/status/2077890054299541890) (by [@scottstts](https://x.com/scottstts))

**結合 Three.js 硬體渲染與可互動的瀏覽器作業系統模擬**

來源表示 Kimi K3 以 Three.js 製作虛擬 MacBook，並帶有可運作的 macOS 風格環境；來源展示成果，但未提供實作步驟

Type: Demo | Date: 2026-07-16

---

<a id="case-25"></a>
### Case 25: [從 DSL 到 PTX 建立 GPU 編譯器](https://x.com/rohanpaul_ai/status/2077886618657231220) (by [@rohanpaul_ai](https://x.com/rohanpaul_ai))

**用端到端編譯器任務涵蓋 DSL、編譯器 pass、PTX 生成與 Tensor Core 路徑**

來源表示 Kimi K3 從零建立 GPU 編譯器，涵蓋 DSL、pass 與 PTX 生成，並將其 Tensor Core 路徑與 Triton 比較；指定記錄沒有獨立基準細節

Type: Demo | Date: 2026-07-16

---

<a id="case-32"></a>
### Case 32: [以 WebGL2 建立即時黑洞光線追蹤器](https://x.com/AlicanKiraz0/status/2077885419744612597) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**測試用一個 prompt 在單一 HTML 檔內生成原生 WebGL2 測地線光線追蹤器**

作者描述一項程式開發基準，要求在單一檔案中完成可運作的原生 WebGL2 黑洞光線彎曲追蹤器；指定記錄確立任務與參與模型，但不是完整的獨立結果稽核

Type: Benchmark | Date: 2026-07-16

---

<a id="case-46"></a>
### Case 46: [以 mGBA WASM 為核心建立 Game Boy Advance 模擬器](https://x.com/teortaxesTex/status/2077925090168062272) (by [@teortaxesTex](https://x.com/teortaxesTex))

**整合授權 3D 模型與真正的模擬器核心，再透過遞迴方式改善介面與遊玩體驗**

所引述的 Kimi K3 專案改編授權的 AGB-001 模型、整合 mGBA WASM 核心，並透過遞迴式自我改善優化介面與遊玩體驗；貼文引用專案說明，並非獨立重現

Type: Integration | Date: 2026-07-17

---

<a id="case-50"></a>
### Case 50: [從中文來源研究多個主題](https://x.com/tphuang/status/2077911994607239400) (by [@tphuang](https://x.com/tphuang))

**透過長時間研究任務比較不同模型世代的完整度與延遲**

作者表示以中文來源測試 Kimi K3 的多個研究主題，認為它比 K2.6 更完整但速度較慢；貼文也指出當時服務需求量很大

Type: Evaluation | Date: 2026-07-17

---

<a id="case-56"></a>
### Case 56: [在瀏覽器複製具可用應用程式的 macOS](https://x.com/twid/status/2077924755357974989) (by [@twid](https://x.com/twid))

**建立包含音樂、瀏覽器與電子郵件應用程式的瀏覽器作業系統模擬**

來源表示 Kimi K3 被用來製作瀏覽器版 macOS 複製品，包含音樂、瀏覽器、電子郵件與其他功能；來源未提供實作細節

Type: Demo | Date: 2026-07-17

---

<a id="case-62"></a>
### Case 62: [建立 FaceTime 可運作的 macOS 模擬](https://x.com/LinearUncle/status/2077919552239997078) (by [@LinearUncle](https://x.com/LinearUncle))

**用虛擬作業系統任務測試生成的應用互動是否能運作**

創作者展示歸因於 Kimi K3 的 macOS 風格環境，並表示其 FaceTime 功能可運作；來源未提供設定或驗證步驟

Type: Demo | Date: 2026-07-17

---

<a id="case-64"></a>
### Case 64: [加入雙任務前端效果比較器](https://x.com/MinLiBuilds/status/2077939461510615376) (by [@MinLiBuilds](https://x.com/MinLiBuilds))

**建立工具以選取兩個已完成任務、並列顯示，並同步視角與互動**

創作者表示要求 Kimi K3 新增前端比較流程，包含任務選擇、雙瀏覽器窗格、物件與漫遊模式、同步視角及互動測試；貼文也指出模型更廣泛的限制

Type: Tutorial | Date: 2026-07-17

---


<a id="evaluation-limits"></a>
## 🧪 評估與限制

| Case | What it shows | Type |
|---|---|---|
| [比較 BridgeBench 熔岩燈任務的前端設計](#case-7) | 把 BridgeBench 熔岩燈任務視為有邊界的單次前端設計比較，而不是通用排名 | Benchmark |
| [對編輯語氣腳本寫作進行基準測試](#case-8) | 在明確標示的內部基準中衡量編輯語氣契合度、相對排名與每篇腳本成本 | Benchmark |
| [比較 Flappy 類遊戲的設計、成本與難度](#case-10) | 比較生成遊戲時記錄難度設定、成本、設計與遊玩功能 | Benchmark |
| [用相同設計 prompt 比較遊戲設計](#case-12) | 固定設計 prompt，分別檢視節奏、設計感與遊玩感受 | Benchmark |
| [統計稽核必須加入獨立審查](#case-13) | 在採信模型產生的統計稽核發現前，先由獨立專家或其他模型複核 | Limit |
| [評估速度慢但品質強的前端執行](#case-16) | 測試前端任務時，同時記錄完成時間與輸出品質 | Evaluation |
| [測試推理小說寫作中的伏筆缺陷](#case-20) | 評估生成的推理故事能否平衡線索、隱晦度與伏筆 | Limit |
| [比較千年鷹號的建模與動畫](#case-21) | 用相同風格要求與 effort 設定，比較 3D 建模、動畫、時間與成本 | Benchmark |
| [檢視十個 Kimi K3 專案合集](#case-28) | 用有連結的專案合集發現具體成果，再分別驗證 | Evaluation |
| [比較四個模型生成進階登陸頁](#case-29) | 固定登陸頁要求，檢視各模型輸出的動畫深度與完成度 | Evaluation |
| [對復古遊戲機制與成本進行基準測試](#case-30) | 在相同復古遊戲任務上比較遊玩、物理、機制、自動行為、token 用量與成本 | Benchmark |
| [與 Fable 5 比較遊戲生成](#case-31) | 把並列生成遊戲範例視為狹義評估，而不是廣泛模型結論 | Evaluation |
| [與 Opus 4.8 比較複雜前端及開發任務](#case-34) | 用多個複雜程式任務辨識勝負，而不是宣稱單一模型全面更強 | Evaluation |
| [檢視基準結果與登陸頁測試](#case-35) | 結合基準背景與具體登陸頁生成測試，同時把兩種證據分開 | Evaluation |
| [用圖形到公式任務評估歸納推理](#case-37) | 在一階邏輯歸納任務中衡量正確性、holdout 表現與公式複雜度 | Benchmark |
| [檢視遊戲、登陸頁、3D 與長上下文的報告成果](#case-38) | 透過多來源整理比較具體成果，並在成本主張旁記錄速度限制 | Evaluation |
| [稽核複雜計畫並質疑其補救方案](#case-40) | 用第二個模型找出被淡化的發現、錯誤補救方案與應駁回的結論 | Evaluation |
| [比較 PPO 風格強化學習 ASCII 圖](#case-41) | 固定 ASCII 圖 prompt，比較模型如何呈現強化學習迴圈 | Evaluation |
| [在 Blender 建模時追蹤容量錯誤](#case-42) | 將 Blender 的部分進度與服務可靠性一併評估，而不是只看成果 | Limit |
| [在競技場比較 Flappy Bird 生成](#case-47) | 透過競技場任務比較兩個 Flappy Bird 生成結果，同時將判斷限定於該任務 | Evaluation |
| [使用工具解答 Bongard 視覺歸納問題](#case-52) | 測試工具使用是否有助於推導 Bongard 推理任務中的視覺規則 | Evaluation |
| [比較 3D 前端品味及設計，對手為 GPT-5.6 Sol](#case-53) | 在有邊界的前端比較中檢視功能、視覺品味、優雅度與 3D 執行 | Evaluation |
| [比較三個模型生成網站](#case-57) | 用可見網站輸出比較 Kimi K3、Fable 5 與 GPT-5.6 Sol 在單次測試的表現 | Evaluation |
| [比較程序式 3D 遊戲生成與成本](#case-59) | 固定各模型的 prompt，檢視生成的輪盤、吃角子老虎與彈珠台系統及單次成本 | Benchmark |
| [比較 3D 軍火庫場景的細節與照明](#case-69) | 在有邊界的 Kimi K3 與 Opus 4.8 比較中檢視物件密度、照明與場景細節 | Evaluation |

<a id="case-7"></a>
### Case 7: [比較 BridgeBench 熔岩燈任務的前端設計](https://x.com/bridgemindai/status/2077868061953007908) (by [@bridgemindai](https://x.com/bridgemindai))

**把 BridgeBench 熔岩燈任務視為有邊界的單次前端設計比較，而不是通用排名**

BridgeMind AI 報告 Kimi K3 在其 BridgeBench 熔岩燈任務中勝過 Fable 5，並在所引述的競技場排名第一；這些都是發布者報告的比較結果

Type: Benchmark | Date: 2026-07-16

---

<a id="case-8"></a>
### Case 8: [對編輯語氣腳本寫作進行基準測試](https://x.com/Whats_AI/status/2077860441380798908) (by [@Whats_AI](https://x.com/Whats_AI))

**在明確標示的內部基準中衡量編輯語氣契合度、相對排名與每篇腳本成本**

Whats_AI 報告初步內部結果為 2,840 Elo、榜單第一，且每篇腳本約 $0.25；這是單一組織的初步基準，不是一般效能或價格保證

Type: Benchmark | Date: 2026-07-16

---

<a id="case-10"></a>
### Case 10: [比較 Flappy 類遊戲的設計、成本與難度](https://x.com/MrAhmadAwais/status/2077915347974557862) (by [@MrAhmadAwais](https://x.com/MrAhmadAwais))

**比較生成遊戲時記錄難度設定、成本、設計與遊玩功能**

Command Code 的內部 Flappy 基準報告各模型使用不同難度設定，並列出 Kimi K3 為 $0.024、Fable 5 為 $0.42、GPT-5.6 Sol 為 $0.15；設定不一致，因此這只是有邊界的內部比較

Type: Benchmark | Date: 2026-07-17

---

<a id="case-12"></a>
### Case 12: [用相同設計 prompt 比較遊戲設計](https://x.com/CommandCodeAI/status/2077921526213746948) (by [@CommandCodeAI](https://x.com/CommandCodeAI))

**固定設計 prompt，分別檢視節奏、設計感與遊玩感受**

Command Code 報告以相同 prompt 比較 Kimi K3、GPT-5.6 Sol 與 Fable 5；貼文稱 Kimi K3 的設計感表現良好，而另兩者遊玩節奏過快，這仍是發布者的評價

Type: Benchmark | Date: 2026-07-17

---

<a id="case-13"></a>
### Case 13: [統計稽核必須加入獨立審查](https://x.com/emollick/status/2077869293031624793) (by [@emollick](https://x.com/emollick))

**在採信模型產生的統計稽核發現前，先由獨立專家或其他模型複核**

Ethan Mollick 報告 Kimi K3 Max 在稽核既有學術工作時誤用統計方法，並認同另一份批評；這個反面案例支持獨立檢查，而不是未經審查便採信

Type: Limit | Date: 2026-07-16

---

<a id="case-16"></a>
### Case 16: [評估速度慢但品質強的前端執行](https://x.com/Lentils80/status/2077387333154857151) (by [@Lentils80](https://x.com/Lentils80))

**測試前端任務時，同時記錄完成時間與輸出品質**

創作者表示一次 Kimi K3 前端執行耗時 35 分鐘，並稱其輸出是該 prompt 所見最佳成果之一；速度與品質判斷都只是單一使用者的觀察

Type: Evaluation | Date: 2026-07-15

---

<a id="case-20"></a>
### Case 20: [測試推理小說寫作中的伏筆缺陷](https://x.com/emollick/status/2077951790868238616) (by [@emollick](https://x.com/emollick))

**評估生成的推理故事能否平衡線索、隱晦度與伏筆**

Ethan Mollick 表示 Kimi K3 沒有寫出好的謀殺推理故事，線索同時過度明顯又過度隱晦，而且伏筆失敗；他也指出其他模型有同樣限制

Type: Limit | Date: 2026-07-17

---

<a id="case-21"></a>
### Case 21: [比較千年鷹號的建模與動畫](https://x.com/gmi_cloud/status/2077903360263676090) (by [@gmi_cloud](https://x.com/gmi_cloud))

**用相同風格要求與 effort 設定，比較 3D 建模、動畫、時間與成本**

GMI Cloud 報告在 maximum effort 下比較 Kimi K3 與 Fable 5 重現像素風及原始風格的千年鷹號；其稱 Kimi K3 在第一次測試耗時較長但成本約為三分之一，另一次則不到一半，這些都是供應商報告的結果

Type: Benchmark | Date: 2026-07-16

---

<a id="case-28"></a>
### Case 28: [檢視十個 Kimi K3 專案合集](https://x.com/minchoi/status/2077957907857994006) (by [@minchoi](https://x.com/minchoi))

**用有連結的專案合集發現具體成果，再分別驗證**

作者整理十個附媒體的 Kimi K3 範例，其中包含 Game Boy Advance 模擬器；此記錄是合集而非單一可重現流程，因此每個連結範例都應獨立檢查

Type: Evaluation | Date: 2026-07-17

---

<a id="case-29"></a>
### Case 29: [比較四個模型生成進階登陸頁](https://x.com/doutorcaleb/status/2077904020471947773) (by [@doutorcaleb](https://x.com/doutorcaleb))

**固定登陸頁要求，檢視各模型輸出的動畫深度與完成度**

創作者表示向 Kimi K3、Fable、Grok 與 GPT Terra 提供相同的進階登陸頁 prompt，並判定 Kimi K3 成果最強；這是單一任務的自行報告比較

Type: Evaluation | Date: 2026-07-16

---

<a id="case-30"></a>
### Case 30: [對復古遊戲機制與成本進行基準測試](https://x.com/adxtyahq/status/2077860500462055570) (by [@adxtyahq](https://x.com/adxtyahq))

**在相同復古遊戲任務上比較遊玩、物理、機制、自動行為、token 用量與成本**

來源報告使用相同 prompt 測試 Road Fighter、Battle City 與 Q*bert，並列出 $0.28 對應 Kimi K3、$0.28 對應 GPT-5.6、$0.54 對應 Opus 4.8；這些是發布者的基準數字

Type: Benchmark | Date: 2026-07-16

---

<a id="case-31"></a>
### Case 31: [與 Fable 5 比較遊戲生成](https://x.com/higgsfield_ai/status/2077943629633712490) (by [@higgsfield_ai](https://x.com/higgsfield_ai))

**把並列生成遊戲範例視為狹義評估，而不是廣泛模型結論**

Higgsfield 展示 Kimi K3 與 Fable 5 的遊戲生成比較；指定記錄包含比較媒體，但沒有 prompt、評分標準或詳細條件

Type: Evaluation | Date: 2026-07-17

---

<a id="case-34"></a>
### Case 34: [與 Opus 4.8 比較複雜前端及開發任務](https://x.com/op7418/status/2077969583018066116) (by [@op7418](https://x.com/op7418))

**用多個複雜程式任務辨識勝負，而不是宣稱單一模型全面更強**

評論者報告直接測試 Kimi K3 與 Opus 4.8，認為兩者在複雜前端與開發工作上大致相當，結果互有勝負；這仍是單一評論者的評估

Type: Evaluation | Date: 2026-07-17

---

<a id="case-35"></a>
### Case 35: [檢視基準結果與登陸頁測試](https://x.com/adamuchigabriel/status/2077880433925120471) (by [@adamuchigabriel](https://x.com/adamuchigabriel))

**結合基準背景與具體登陸頁生成測試，同時把兩種證據分開**

影片介紹 Kimi K3 的基準討論、登陸頁測試與前端設計觀察；指定記錄沒有提供完整測試 prompt 或評分標準

Type: Evaluation | Date: 2026-07-16

---

<a id="case-37"></a>
### Case 37: [用圖形到公式任務評估歸納推理](https://x.com/s_batzoglou/status/2077884096307454119) (by [@s_batzoglou](https://x.com/s_batzoglou))

**在一階邏輯歸納任務中衡量正確性、holdout 表現與公式複雜度**

作者表示在 ICML INDUCTION 任務上對 Kimi K3 與其他模型進行基準測試，使用 6 至 10 個小型圖，每個含 8 至 10 個元素，以推導一階公式；貼文稱結果已從先前工作更新，本案例庫不主張新的獨立重現

Type: Benchmark | Date: 2026-07-16

---

<a id="case-38"></a>
### Case 38: [檢視遊戲、登陸頁、3D 與長上下文的報告成果](https://x.com/servasyy_ai/status/2077903775113834689) (by [@servasyy_ai](https://x.com/servasyy_ai))

**透過多來源整理比較具體成果，並在成本主張旁記錄速度限制**

作者整理各方報告的 Kimi K3 測試，涵蓋遊戲、登陸頁、3D 生成與長上下文工作，並認為它值得嘗試但尚不能取代 Fable 5；所有數字都是此整理中的二手報告

Type: Evaluation | Date: 2026-07-16

---

<a id="case-40"></a>
### Case 40: [稽核複雜計畫並質疑其補救方案](https://x.com/doodlestein/status/2077901883637665958) (by [@doodlestein](https://x.com/doodlestein))

**用第二個模型找出被淡化的發現、錯誤補救方案與應駁回的結論**

創作者表示 Kimi K3 審查一份反覆精修的計畫後，發現嚴重問題被淡化、約三分之一的建議補救方案需要修正，且一項發現遭推翻；這些是該特定稽核的結果

Type: Evaluation | Date: 2026-07-16

---

<a id="case-41"></a>
### Case 41: [比較 PPO 風格強化學習 ASCII 圖](https://x.com/dejavucoder/status/2077872015856615541) (by [@dejavucoder](https://x.com/dejavucoder))

**固定 ASCII 圖 prompt，比較模型如何呈現強化學習迴圈**

來源提供繪製 PPO 風格強化學習迴圈的 ASCII prompt，並並列 Kimi K3 Max 與 Fable 5 High；判斷仍是單一任務的視覺比較

Type: Evaluation | Date: 2026-07-16

---

<a id="case-42"></a>
### Case 42: [在 Blender 建模時追蹤容量錯誤](https://x.com/Angaisb_/status/2077910845523214668) (by [@Angaisb_](https://x.com/Angaisb_))

**將 Blender 的部分進度與服務可靠性一併評估，而不是只看成果**

創作者展示 Kimi K3 的 Blender 建模進度，也報告反覆發生容量錯誤；指定來源中的工作尚未完成，因此應同時考量部分成果與可靠性限制

Type: Limit | Date: 2026-07-17

---

<a id="case-47"></a>
### Case 47: [在競技場比較 Flappy Bird 生成](https://x.com/jun_song/status/2077396996865003739) (by [@jun_song](https://x.com/jun_song))

**透過競技場任務比較兩個 Flappy Bird 生成結果，同時將判斷限定於該任務**

創作者報告 Kimi K3 與 Opus 4.8 在 Flappy Bird 任務上的 Arena 比較，並判定 Kimi K3 明顯更好；記錄未提供完整 prompt 或評分標準

Type: Evaluation | Date: 2026-07-15

---

<a id="case-52"></a>
### Case 52: [使用工具解答 Bongard 視覺歸納問題](https://x.com/IntuitMachine/status/2077885406528311561) (by [@IntuitMachine](https://x.com/IntuitMachine))

**測試工具使用是否有助於推導 Bongard 推理任務中的視覺規則**

創作者表示 Kimi K3 使用工具解出一題 Bongard 問題，而 Grok 4.5 與 Muse Spark 1.1 在相同比較中未能解出；這是單一使用者的任務結果，不是通用推理基準

Type: Evaluation | Date: 2026-07-16

---

<a id="case-53"></a>
### Case 53: [比較 3D 前端品味及設計，對手為 GPT-5.6 Sol](https://x.com/filicroval/status/2077736407506751952) (by [@filicroval](https://x.com/filicroval))

**在有邊界的前端比較中檢視功能、視覺品味、優雅度與 3D 執行**

創作者比較 Kimi K3 與 GPT-5.6 Sol 的前端設計，判定 Kimi K3 在視覺品味、優雅度與 3D 能力上較強；此評估具主觀性，且只適用於該任務

Type: Evaluation | Date: 2026-07-16

---

<a id="case-57"></a>
### Case 57: [比較三個模型生成網站](https://x.com/pengchujin/status/2077962916226298340) (by [@pengchujin](https://x.com/pengchujin))

**用可見網站輸出比較 Kimi K3、Fable 5 與 GPT-5.6 Sol 在單次測試的表現**

創作者展示 Kimi K3、Fable 5 與 GPT-5.6 Sol 的網站生成比較；指定記錄未揭露完整 prompt 或評分標準

Type: Evaluation | Date: 2026-07-17

---

<a id="case-59"></a>
### Case 59: [比較程序式 3D 遊戲生成與成本](https://x.com/adxtyahq/status/2077958193511362856) (by [@adxtyahq](https://x.com/adxtyahq))

**固定各模型的 prompt，檢視生成的輪盤、吃角子老虎與彈珠台系統及單次成本**

發布者報告多模型程序式 3D 遊戲比較，列出的成本包括 $0.71 對應 Kimi K3，以及 $0.30 對應 Grok 4.5；所有排名與成本都應視為該發布者的執行結果

Type: Benchmark | Date: 2026-07-17

---

<a id="case-69"></a>
### Case 69: [比較 3D 軍火庫場景的細節與照明](https://x.com/hakki_alkan/status/2077887013332636032) (by [@hakki_alkan](https://x.com/hakki_alkan))

**在有邊界的 Kimi K3 與 Opus 4.8 比較中檢視物件密度、照明與場景細節**

來源表示 Kimi K3 產出細節豐富的軍火庫場景，包含擺滿物品的層架、箱子與真實照明，而 Opus 4.8 只產出稀疏房間；這是第三方比較報告，不是獨立基準

Type: Evaluation | Date: 2026-07-16

---

## 相關資源

- [查看 EvoLink 上的 Kimi K3 詳情與價格](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_model)
- [查看 EvoLink Kimi K3 API 文件](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_api_docs)
- [進一步了解 EvoLink 上的 Kimi K3](https://evolink.ai/blog/is-kimi-k3-available-on-evolink?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_article)
- EvoLink 模型頁與 API 文件已驗證，但尚未驗證可安裝的 Kimi K3 skill

<a id="acknowledge"></a>
## 🙏 致謝

感謝所有公開分享 Kimi K3 作品的創作者與實務工作者

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

*若需更正歸屬或文字，請附上公開來源建立 issue*
