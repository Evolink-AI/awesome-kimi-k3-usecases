<div align="center">

<a href="https://evolink.ai/kimi-k3?utm_source=github&utm_medium=banner&utm_campaign=awesome-kimi-k3-usecases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/images/zh-TW-v2.png" alt="帶月面場景與 EvoLink 使用入口的繁體中文 Kimi K3 banner" width="760"></a>

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

# Kimi K3 精選使用案例

## 🍌 簡介

歡迎來到 Kimi K3 高訊號使用案例庫

**我們收錄具有公開來源的遊戲、3D 場景、動態設計、整合、評估與實務限制**

全部 129 個案例都來自高置信度公開來源。標題和作者連結指向原始來源；弱證據、重複或無法充分核驗的候選不會收錄

## 📊 概覽

- 來自公開創作者和實踐者的 129 個高置信度案例
- 廣泛涵蓋互動遊戲、Three.js、動態設計、前端、研究、評估、工具整合與實務限制
- 每個案例保留來源、作者、類型、日期與 prompt 邊界
- 排除全部 31 個 medium-confidence 項目，也不把個人觀察包裝成 benchmark

> [!NOTE]
> 本案例庫優先採用具體證據，不補寫未公開的 prompt 或設定步驟

<a id="quick-api-access"></a>
## ⚡ 快速開始

EvoLink 文件記載的模型 ID 為 `kimi-k3`，模型詳情頁與 Chat Completions API 文件均已提供

1. [查看 EvoLink 上的 Kimi K3 詳情與價格](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=landing_overview)
2. [建立或管理 EvoLink API 金鑰](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-kimi-k3-usecases&utm_content=api_key)

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

[查看 EvoLink Kimi K3 API 文件](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=first_run)

> [!IMPORTANT]
> EvoLink 模型頁與 API 文件驗證了公開路由和模型 ID；目前未驗證獨立的 Kimi K3 瀏覽器或無程式碼試用介面，本案例庫也不聲稱已獨立完成付費 API 測試

## 📑 目錄

| Section | Cases |
|---|---|
| [互動遊戲與 3D](#games-3d) | 39 |
| [前端與動態設計](#frontend-motion) | 27 |
| [程式開發與整合](#coding-integrations) | 16 |
| [評估與限制](#evaluation-limits) | 47 |
| [相關資源](#related-resources) | 相關資源 |
| [快速開始](#quick-api-access) | 快速開始 |
| [致謝](#acknowledge) | 致謝與更正 |

| Case | Category | What it shows | Type |
|---|---|---|---|
| [用一個 prompt 建立 voxel pod racer](#case-1) | 互動遊戲與 3D | 從簡短場景概念做出競速原型，再界定下一輪改善內容 | Demo |
| [用相同 prompt 比較 Frogger](#case-2) | 互動遊戲與 3D | 固定 prompt 來檢查不同模型的輸出差異 | Evaluation |
| [產生 Frogger 與遊玩錄影](#case-3) | 互動遊戲與 3D | 分別以一次生成測試遊戲與錄影流程 | Demo |
| [用 Three.js 製作航空母艦原型](#case-4) | 互動遊戲與 3D | 以具體起降場景測試互動式 3D 生成 | Demo |
| [建立可互動的動態前端](#case-5) | 前端與動態設計 | 製作暫停動畫後仍可互動的動態圖形 | Demo |
| [製作同步的動態廣告](#case-6) | 前端與動態設計 | 檢查音樂、效果與動作是否同步 | Demo |
| [比較 BridgeBench 熔岩燈任務的前端設計](#case-7) | 評估與限制 | 把 BridgeBench 熔岩燈任務視為有邊界的單次前端設計比較，而不是通用排名 | Benchmark |
| [對編輯語氣腳本寫作進行基準測試](#case-8) | 評估與限制 | 在明確標示的內部基準中衡量編輯語氣契合度、相對排名與每篇腳本成本 | Benchmark |
| [用代理工具製作 Paper Mario 風格遊戲](#case-9) | 互動遊戲與 3D | 結合 Kimi K3、代理 harness 與素材工具，同時產出 2D 與 3D 遊戲元素 | Demo |
| [比較 Flappy 類遊戲的設計、成本與難度](#case-10) | 評估與限制 | 比較生成遊戲時記錄難度設定、成本、設計與遊玩功能 | Benchmark |
| [生成地鐵場景第一人稱射擊遊戲](#case-11) | 互動遊戲與 3D | 用具體的地鐵場景檢視生成的第一人稱射擊遊戲成果 | Demo |
| [用相同設計 prompt 比較遊戲設計](#case-12) | 評估與限制 | 固定設計 prompt，分別檢視節奏、設計感與遊玩感受 | Benchmark |
| [統計稽核必須加入獨立審查](#case-13) | 評估與限制 | 在採信模型產生的統計稽核發現前，先由獨立專家或其他模型複核 | Limit |
| [完全用程式碼製作動態設計](#case-14) | 前端與動態設計 | 測試一次生成的程式開發流程能否在沒有輔助生成工具時完成動態設計 | Demo |
| [研究人物並建立動畫個人網站](#case-15) | 前端與動態設計 | 提供寬泛的個人網站簡述，再檢視模型的研究、規劃、迭代與瀏覽器驗證流程 | Tutorial |
| [評估速度慢但品質強的前端執行](#case-16) | 評估與限制 | 測試前端任務時，同時記錄完成時間與輸出品質 | Evaluation |
| [生成黑洞模擬](#case-17) | 前端與動態設計 | 用科學視覺化任務檢視生成的黑洞模擬 | Demo |
| [製作具備可用 macOS 的虛擬 MacBook](#case-18) | 程式開發與整合 | 結合 Three.js 硬體渲染與可互動的瀏覽器作業系統模擬 | Demo |
| [使用 Blender MCP 建模 V8 引擎](#case-19) | 互動遊戲與 3D | 透過 Blender MCP 與單次要求生成精細的機械 3D 模型 | Integration |
| [測試推理小說寫作中的伏筆缺陷](#case-20) | 評估與限制 | 評估生成的推理故事能否平衡線索、隱晦度與伏筆 | Limit |
| [比較千年鷹號的建模與動畫](#case-21) | 評估與限制 | 用相同風格要求與 effort 設定，比較 3D 建模、動畫、時間與成本 | Benchmark |
| [測試複雜前端建模、粒子與 shader](#case-22) | 前端與動態設計 | 使用公開前端 prompt，在一次執行中檢視建模精度、粒子效果與行內 shader 生成 | Demo |
| [從一個參考建立可玩的戰鬥競技場](#case-23) | 互動遊戲與 3D | 用單一參考測試一次生成完整可玩競技場的能力 | Demo |
| [將三款自動遊玩的復古遊戲做成 HTML 檔](#case-24) | 互動遊戲與 3D | 要求在獨立 HTML 遊戲檔中包含圖形、敵人、規則與自動遊玩 | Benchmark |
| [從 DSL 到 PTX 建立 GPU 編譯器](#case-25) | 程式開發與整合 | 用端到端編譯器任務涵蓋 DSL、編譯器 pass、PTX 生成與 Tensor Core 路徑 | Demo |
| [一次生成程序式音樂工具](#case-26) | 前端與動態設計 | 測試一次生成互動式程序音樂產生器，並審慎比較可見成果 | Demo |
| [一次生成變色龍捉迷藏遊戲](#case-27) | 互動遊戲與 3D | 生成包含顏色配對、程序式區域、聲音與多回合計分的單檔遊戲 | Benchmark |
| [檢視十個 Kimi K3 專案合集](#case-28) | 評估與限制 | 用有連結的專案合集發現具體成果，再分別驗證 | Evaluation |
| [比較四個模型生成進階登陸頁](#case-29) | 評估與限制 | 固定登陸頁要求，檢視各模型輸出的動畫深度與完成度 | Evaluation |
| [對復古遊戲機制與成本進行基準測試](#case-30) | 評估與限制 | 在相同復古遊戲任務上比較遊玩、物理、機制、自動行為、token 用量與成本 | Benchmark |
| [與 Fable 5 比較遊戲生成](#case-31) | 評估與限制 | 把並列生成遊戲範例視為狹義評估，而不是廣泛模型結論 | Evaluation |
| [以 WebGL2 建立即時黑洞光線追蹤器](#case-32) | 程式開發與整合 | 測試用一個 prompt 在單一 HTML 檔內生成原生 WebGL2 測地線光線追蹤器 | Benchmark |
| [從兩張圖片建立 Three.js 產品頁](#case-33) | 前端與動態設計 | 使用兩張參考圖片與明確的 Three.js 要求生成產品展示頁 | Demo |
| [與 Opus 4.8 比較複雜前端及開發任務](#case-34) | 評估與限制 | 用多個複雜程式任務辨識勝負，而不是宣稱單一模型全面更強 | Evaluation |
| [檢視基準結果與登陸頁測試](#case-35) | 評估與限制 | 結合基準背景與具體登陸頁生成測試，同時把兩種證據分開 | Evaluation |
| [用代理工具鏈建立 2.5D Paper Mario 類遊戲](#case-36) | 互動遊戲與 3D | 結合 Kimi K3、Grok Build 或 Claude Code 以及 Spriterrific，組成 2.5D 遊戲工作流程 | Tutorial |
| [用圖形到公式任務評估歸納推理](#case-37) | 評估與限制 | 在一階邏輯歸納任務中衡量正確性、holdout 表現與公式複雜度 | Benchmark |
| [檢視遊戲、登陸頁、3D 與長上下文的報告成果](#case-38) | 評估與限制 | 透過多來源整理比較具體成果，並在成本主張旁記錄速度限制 | Evaluation |
| [發明豪華麵包切割器及其產品頁](#case-39) | 前端與動態設計 | 在單一設計成果中結合產品構想、爆炸圖、示範與登陸頁 | Demo |
| [稽核複雜計畫並質疑其補救方案](#case-40) | 評估與限制 | 用第二個模型找出被淡化的發現、錯誤補救方案與應駁回的結論 | Evaluation |
| [比較 PPO 風格強化學習 ASCII 圖](#case-41) | 評估與限制 | 固定 ASCII 圖 prompt，比較模型如何呈現強化學習迴圈 | Evaluation |
| [在 Blender 建模時追蹤容量錯誤](#case-42) | 評估與限制 | 將 Blender 的部分進度與服務可靠性一併評估，而不是只看成果 | Limit |
| [建立瀏覽器版 3D 武俠 RPG](#case-43) | 互動遊戲與 3D | 結合近戰、任務、物品欄、天氣、室內探索、Blender 環境製作與改編素材 | Demo |
| [建立瀏覽器多人 Minecraft 類遊戲](#case-44) | 互動遊戲與 3D | 在有邊界的時間與成本執行中，產出可線上多人遊玩的瀏覽器遊戲 | Demo |
| [生成十秒遞迴鵜鶘 GIF](#case-45) | 前端與動態設計 | 用完整指定的循環動畫簡述，檢視 GIF 的敘事連續性與遞迴效果 | Demo |
| [以 mGBA WASM 為核心建立 Game Boy Advance 模擬器](#case-46) | 程式開發與整合 | 整合授權 3D 模型與真正的模擬器核心，再透過遞迴方式改善介面與遊玩體驗 | Integration |
| [在競技場比較 Flappy Bird 生成](#case-47) | 評估與限制 | 透過競技場任務比較兩個 Flappy Bird 生成結果，同時將判斷限定於該任務 | Evaluation |
| [重現分割畫面合作瀏覽器遊戲](#case-48) | 互動遊戲與 3D | 用一個要求生成瀏覽器分割畫面合作玩法與即時環境互動 | Demo |
| [使用 Command Code 設計模式生成可玩遊戲](#case-49) | 互動遊戲與 3D | 用 Command Code 的 design 指令一次生成遊戲，並記錄成果是否可玩 | Demo |
| [從中文來源研究多個主題](#case-50) | 程式開發與整合 | 透過長時間研究任務比較不同模型世代的完整度與延遲 | Evaluation |
| [組裝具一致性的武俠瀏覽器 RPG](#case-51) | 互動遊戲與 3D | 在一款遊戲中整合移動、戰鬥、任務、物品欄、天氣、探索與 3D 環境製作 | Demo |
| [使用工具解答 Bongard 視覺歸納問題](#case-52) | 評估與限制 | 測試工具使用是否有助於推導 Bongard 推理任務中的視覺規則 | Evaluation |
| [比較 3D 前端品味及設計，對手為 GPT-5.6 Sol](#case-53) | 評估與限制 | 在有邊界的前端比較中檢視功能、視覺品味、優雅度與 3D 執行 | Evaluation |
| [建立可玩的 Hollow Knight 跨界遊戲](#case-54) | 互動遊戲與 3D | 使用既有遊戲素材，建立 Knight 與 Kimi 對戰的可玩遊戲 | Demo |
| [生成 BMW M4 CS 側視 SVG](#case-55) | 前端與動態設計 | 用指定車款與視角檢視向量插畫輸出 | Demo |
| [在瀏覽器複製具可用應用程式的 macOS](#case-56) | 程式開發與整合 | 建立包含音樂、瀏覽器與電子郵件應用程式的瀏覽器作業系統模擬 | Demo |
| [比較三個模型生成網站](#case-57) | 評估與限制 | 用可見網站輸出比較 Kimi K3、Fable 5 與 GPT-5.6 Sol 在單次測試的表現 | Evaluation |
| [透過截圖回饋重現 Gargantua](#case-58) | 前端與動態設計 | 把反覆截圖當作觀察資料，用來診斷並改善科學視覺化 | Tutorial |
| [比較程序式 3D 遊戲生成與成本](#case-59) | 評估與限制 | 固定各模型的 prompt，檢視生成的輪盤、吃角子老虎與彈珠台系統及單次成本 | Benchmark |
| [一次生成 Fall Guys 風格 3D 瀏覽器遊戲](#case-60) | 互動遊戲與 3D | 用一次生成要求製作可玩的 3D 障礙遊戲，並公開專案供檢查 | Demo |
| [建立並自行測試末日里斯本 FPS](#case-61) | 互動遊戲與 3D | 用一個 maximum-effort prompt 執行，在交付可玩 FPS 前反覆測試、截圖與迭代 | Demo |
| [建立 FaceTime 可運作的 macOS 模擬](#case-62) | 程式開發與整合 | 用虛擬作業系統任務測試生成的應用互動是否能運作 | Demo |
| [從簡單要求生成 Animal Crossing 風格遊戲](#case-63) | 互動遊戲與 3D | 用極簡遊戲簡述檢視可玩性、遊戲迴圈與視差效果 | Demo |
| [加入雙任務前端效果比較器](#case-64) | 程式開發與整合 | 建立工具以選取兩個已完成任務、並列顯示，並同步視角與互動 | Tutorial |
| [從一句簡述生成 Mario 類遊戲](#case-65) | 互動遊戲與 3D | 用極簡的一次生成要求檢視可玩性、關卡設計、像素美術與視差 | Demo |
| [以 62 張截圖改善黑洞視覺化](#case-66) | 前端與動態設計 | 使用截圖回饋迴圈，在多次迭代中讀取、診斷並修正視覺模擬 | Tutorial |
| [建立可運作的殭屍第一人稱射擊遊戲](#case-67) | 互動遊戲與 3D | 用具體的殭屍射擊目標檢視完整可玩的 FPS 成果 | Demo |
| [製作後訓練行銷 PDF](#case-68) | 前端與動態設計 | 用指定產品與交付格式生成行銷文件 | Demo |
| [比較 3D 軍火庫場景的細節與照明](#case-69) | 評估與限制 | 在有邊界的 Kimi K3 與 Opus 4.8 比較中檢視物件密度、照明與場景細節 | Evaluation |
| [用一個 prompt 建立使用者介面](#case-70) | 前端與動態設計 | 用單次要求生成並檢視完整 UI 設計 | Demo |
| [建立獨立太空船遊戲](#case-71) | 互動遊戲與 3D | 先用 Kimi K3 Standard 製作遊戲初版，再比較一致性、缺陷、視覺品質與 token 成本 | Demo |
| [用相同 Arena prompt 比較前端](#case-72) | 評估與限制 | 固定 prompt 並並排檢查輸出，比只看一個排行榜分數更可靠 | Benchmark |
| [讓 Summer Engine 遊戲自測](#case-73) | 互動遊戲與 3D | 讓 Kimi K3 執行遊戲、檢查截圖與日誌，並在同一會話中修復可見缺陷 | Demo |
| [評測 Kimi Code 編碼 agent](#case-74) | 評估與限制 | 結合多個編碼 agent 測試集與單任務成本評估 Kimi K3，不把單一前端榜單當成整體能力 | Benchmark |
| [將 Kimi 設定為 Codex 子 agent](#case-75) | 程式開發與整合 | 讓 Codex 保留編排職責，把前端執行交給 Kimi K3 OpenCode 子 agent，並明確密鑰邊界 | Tutorial |
| [比較 Arena 與修復測試結果](#case-76) | 評估與限制 | 同時看前端偏好與儲存庫修復評測，因為 Kimi K3 可在一個榜單第一、在另一測試中第七 | Benchmark |
| [迭代瀏覽器大逃殺遊戲](#case-77) | 互動遊戲與 3D | 建立功能豐富的瀏覽器遊戲時，要預期長時間自主迭代與有針對性的後續 prompt | Demo |
| [建立獲獎風格網站](#case-78) | 前端與動態設計 | 透過完整錄影評估 Kimi K3 的精緻網站建立過程，而不只看最終截圖 | Tutorial |
| [透過 ChatLLM 路由簡單編碼](#case-79) | 程式開發與整合 | 建立任務路由，將簡單編碼交給 Kimi K3，把困難編碼與設計保留給其他模型 | Integration |
| [用 Prinzbench 評估 Kimi K3](#case-80) | 評估與限制 | 用独立 benchmark 更新对比 Kimi K3 与開源、前沿模型在搜索、推理和一致性上的表现。 | Benchmark |
| [構建滾动 Metaball 前端](#case-81) | 前端與動態設計 | 让 Kimi K3 生成 Awwwards 风格滚动页面，并檢查数学效果是否能替代重型 mesh 或貼圖资源。 | Demo |
| [跨模型重设计個人網站](#case-82) | 前端與動態設計 | 用多个 coding harness 執行同一个網站重设计 brief，并比较耗時、视觉方向和与现有身份的匹配度。 | Evaluation |
| [擴展太空游戏地形](#case-83) | 互動遊戲與 3D | 把 Kimi K3 作为长時间构建 pass，把佔位地形替换成更大的真实地貌启髮游戏環境。 | Demo |
| [解鎖 Three.js 物理渲染器](#case-84) | 互動遊戲與 3D | 当数学和物理邏辑可用但渲染管线停滯時，把 Kimi K3 引入 Three.js 物理项目。 | Demo |
| [对比 ISS 数字孪生生成](#case-85) | 評估與限制 | 用同 prompt 3D 挑战，对比 Kimi K3 与 GPT-5.6 Sol 在重建、控制、標签和视觉细节上的表现。 | Benchmark |
| [構建交互式頭皮探索器](#case-86) | 前端與動態設計 | 用 Kimi K3 一次生成包含解剖层、響应式髮丝和交互热点的 3D 教育场景。 | Demo |
| [分享 3D 地球儀儀表盘 Prompt](#case-87) | 前端與動態設計 | 研究 Kimi K3 3D 地球儀儀表盤的 prompt 与参考圖设置，而不是只从最终圖反推工作流。 | Tutorial |
| [用单文件構建瀏覽器 Counter-Strike](#case-88) | 互動遊戲與 3D | 用 Kimi K3 生成单文件瀏覽器 FPS，并檢查地圖、机器人、武器、回合规则和程序化音频是否完整。 | Demo |
| [評测 WebGPU 森林世界](#case-89) | 評估與限制 | 在长周期 Three.js 与 WebGPU 世界构建中，把 Kimi K3 作为 coding agent brain，从质量、速度、一致性和人工修改率評估它。 | Evaluation |
| [比較玻璃屋同題提示](#case-90) | 評估與限制 | 用同一個建築場景提示比較 Kimi K3 與 Opus 4.8 在氛圍、光照和空間完整度上的差異。 | Evaluation |
| [用生成資產建構 CS](#case-91) | 程式開發與整合 | 原型化小型 Counter-Strike 風格瀏覽器遊戲時，用 Kimi K3 寫遊戲程式碼，用 GPT Image 2 生成資產。 | Integration |
| [評測體素足球進球](#case-92) | 評估與限制 | 把同一個純 HTML/CSS/JS 足球動畫提示交給兩個模型，比較動作品質和成本。 | Benchmark |
| [審看 Minecraft benchmark](#case-93) | 評估與限制 | 在把發布 hype 或模型價格當作證據前，先看結構化 Minecraft 測評。 | Benchmark |
| [執行五項 UI UX 測試](#case-94) | 前端與動態設計 | 不要只看一張 frontend 截圖，而是用多項 UI、Logo 和 Figma MCP 任務評估 Kimi K3。 | Evaluation |
| [使用 Command Code Design skill](#case-95) | 程式開發與整合 | 在 token 預算內建構視覺遊戲原型時，把 Kimi K3 與 Command Code 的專用 design skill 結合使用。 | Integration |
| [建構金字塔探險遊戲](#case-96) | 互動遊戲與 3D | 用 Kimi K3 做一次完整的一日 3D 探索遊戲建構，再檢查任務、室內空間和探索範圍後評價品質。 | Demo |
| [從參考圖建立 landing](#case-97) | 前端與動態設計 | 用參考圖板、Figma AI、Motion Sites 與 Kimi K3，把視覺方向轉成可複用的 landing page section。 | Tutorial |
| [衡量 API 檔位限制](#case-98) | 評估與限制 | 規劃 Kimi K3 agent run 時，要看 token、tier、TPM 和 TPD，不只看模型標價。 | Limit |
| [比較 Limbo 風格 demo](#case-99) | 評估與限制 | 在同一個遊戲原型上比較 Kimi K3 與 Fable 5 的可玩範圍、視覺打磨、成本和 bug。 | Benchmark |
| [審查 VulcanBench 成本結果](#case-100) | 評估與限制 | 用这个案例评估 Kimi K3 在「審查 VulcanBench 成本結果」任务中的实际工作流、成本或限制。 | Benchmark |
| [比較 Minecraft 構建深度](#case-101) | 互動遊戲與 3D | 用这个案例评估 Kimi K3 在「比較 Minecraft 構建深度」任务中的实际工作流、成本或限制。 | Evaluation |
| [構建 Fallout FPS 複製版](#case-102) | 互動遊戲與 3D | 用这个案例评估 Kimi K3 在「構建 Fallout FPS 複製版」任务中的实际工作流、成本或限制。 | Demo |
| [跟做高級網站教學](#case-103) | 前端與動態設計 | 用这个案例评估 Kimi K3 在「跟做高級網站教學」任务中的实际工作流、成本或限制。 | Tutorial |
| [評測雙擺物理模擬](#case-104) | 評估與限制 | 用这个案例评估 Kimi K3 在「評測雙擺物理模擬」任务中的实际工作流、成本或限制。 | Benchmark |
| [交付資料中心 RPG](#case-105) | 互動遊戲與 3D | 用这个案例评估 Kimi K3 在「交付資料中心 RPG」任务中的实际工作流、成本或限制。 | Demo |
| [比較人形機器人前端成本](#case-106) | 前端與動態設計 | 用这个案例评估 Kimi K3 在「比較人形機器人前端成本」任务中的实际工作流、成本或限制。 | Benchmark |
| [檢視 ReactBench 生產就緒度](#case-107) | 評估與限制 | 用这个案例评估 Kimi K3 在「檢視 ReactBench 生產就緒度」任务中的实际工作流、成本或限制。 | Benchmark |
| [構建 3D 賽車遊戲](#case-108) | 互動遊戲與 3D | 用这个案例评估 Kimi K3 在「構建 3D 賽車遊戲」任务中的实际工作流、成本或限制。 | Demo |
| [在 Claude Code 中執行 Kimi K3](#case-109) | 程式開發與整合 | 用这个案例评估 Kimi K3 在「在 Claude Code 中執行 Kimi K3」任务中的实际工作流、成本或限制。 | Integration |
| [用 AA-Briefcase 評估 Kimi K3](#case-110) | 評估與限制 | 先用 AA-Briefcase 結果判斷 Kimi K3 的知識工作 agent 任務表現，再相信排行榜敘事。 | Benchmark |
| [對比 Geometry Dash 複製版](#case-111) | 互動遊戲與 3D | 用同一需求的遊戲 build 對比，判斷 Kimi K3 是否足夠做可玩的行動風格原型。 | Evaluation |
| [執行 Command Code 復古遊戲測試](#case-112) | 互動遊戲與 3D | 用 Command Code 的多模型設計測試對比 Kimi K3 的 gameplay 功能和各模型成本。 | Evaluation |
| [審計前端榜單限制](#case-113) | 評估與限制 | 用這條限制說明區分 Kimi K3 的榜單勝利和更寬泛的 coding、成本主張。 | Limit |
| [對比 StackPerf 架構結果](#case-114) | 評估與限制 | 用 StackPerf 對比 Kimi K3 和 Qwen 3.8 的架構品質、速度和 tool call 行為。 | Benchmark |
| [對比 Three.js Kimi-vs-GLM 建構](#case-115) | 前端與動態設計 | 用同一組程序化 Three.js prompts 跑 Kimi K3 和 GLM 5.2，比較前端與 3D build 行為。 | Benchmark |
| [評測 Space Discoverer 遊戲](#case-116) | 互動遊戲與 3D | 用 Space Discoverer 小基準比較模型在通用 3D 瀏覽器遊戲 brief 下的輸出。 | Benchmark |
| [建構真實道路駕駛遊戲](#case-117) | 互動遊戲與 3D | 把 Kimi K3 與 Blender、Godot 結合，用真實本地道路地圖原型化一個駕駛遊戲。 | Demo |
| [對比 Monument Valley prompt 成本](#case-118) | 評估與限制 | 用單個 Monument Valley 風格 prompt 對比 Kimi K3 與其他模型的視覺品質、執行時間和成本。 | Benchmark |
| [透過 claude-code-router 路由 Kimi](#case-119) | 程式開發與整合 | 在現有 Claude Code workflow 中透過 claude-code-router 試用 Kimi K3，同時避免不必要的 proxy mode。 | Integration |
| [用 Surge 指数評估 Kimi K3](#case-120) | 評估與限制 | 用 SurgeAI 的分项结果区分 Kimi K3 在日常聊天中的优势，以及在企业 agent 和科学任務中的弱项。 | Benchmark |
| [用参考图生成落地页](#case-121) | 前端與動態設計 | 測試落地页生成时，给 Kimi K3 提供强视觉参考和分轮指导。 | Demo |
| [建構纵向平台游戏](#case-122) | 互動遊戲與 3D | 用简洁游戏 brief 測試 Kimi K3 能否返回单文件浏览器原型。 | Demo |
| [評估 PDE 求解错误](#case-123) | 評估與限制 | 用 PDE benchmark 失败案例判断 Kimi K3 在符号或数值任務中哪些环节需要额外驗證。 | Benchmark |
| [复查 ClinicalBench EHR 案例](#case-124) | 評估與限制 | 用 ClinicalBench 的 EHR 案例检查 Kimi K3 哪些地方成功，哪些诊断推理仍会失败。 | Benchmark |
| [執行开源 agent harness](#case-125) | 程式開發與整合 | 用共享 agent harness 对比 Kimi K3 与其他前沿模型在工具调用任務中的表现。 | Benchmark |
| [評估报税计算能力](#case-126) | 評估與限制 | 不要假设前端强项会迁移到税务计算；应单独測試 Kimi K3 的该类负载。 | Limit |
| [驗證 Geometry Dash 生成结果](#case-127) | 互動遊戲與 3D | 把 Kimi K3 游戏构建与 solver 和浏览器回放測試结合，再判断它是否可作为完成原型。 | Benchmark |
| [模拟 3D 粒子系统](#case-128) | 前端與動態設計 | 用粒子模拟 prompt 对比 Kimi K3 与闭源模型的运动质量。 | Evaluation |
| [通过 Codex OAuth 執行 Kimi](#case-129) | 程式開發與整合 | 当 Kimi K3 编码工作流需要避免手动配置 API key 时，使用 Codex OAuth 路径。 | Integration |

<a id="games-3d"></a>
## 🎮 互動遊戲與 3D

<a id="case-1"></a>
### Case 1: [用一個 prompt 建立 voxel pod racer](https://x.com/ivanfioravanti/status/2077763009657627055) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**從簡短場景概念做出競速原型，再界定下一輪改善內容**

創作者表示 Kimi K3 以一個公開 prompt 產出初版，下一版將加入更多賽車、終點線與細節檢查

**Prompt:**

```text
Voxel star wars pod-racers run
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01-poster.jpg" alt="Case 1 source video poster" height="360"></a>

[Play case 1 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-2"></a>
### Case 2: [用相同 prompt 比較 Frogger](https://x.com/ivanfioravanti/status/2077754781964054825) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**固定 prompt 來檢查不同模型的輸出差異**

創作者用 Kimi K3 版本做同 prompt 比較，但來源沒有公開 prompt 內容或評分規則

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02-poster.jpg" alt="Case 2 source video poster" height="360"></a>

[Play case 2 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-3"></a>
### Case 3: [產生 Frogger 與遊玩錄影](https://x.com/TheAhmadOsman/status/2077776567292338285) (by [@TheAhmadOsman](https://x.com/TheAhmadOsman))

**分別以一次生成測試遊戲與錄影流程**

創作者表示遊戲與錄影流程各由一次生成完成，但沒有公開完整 prompt

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03-poster.jpg" alt="Case 3 source video poster" height="360"></a>

[Play case 3 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-4"></a>
### Case 4: [用 Three.js 製作航空母艦原型](https://x.com/HarshithLucky3/status/2077753222018814360) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**以具體起降場景測試互動式 3D 生成**

創作者展示尼米茲級航空母艦的戰機起飛與回收，並對 3D 生成給出正面評價

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04-poster.jpg" alt="Case 4 source video poster" height="360"></a>

[Play case 4 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-9"></a>
### Case 9: [用代理工具製作 Paper Mario 風格遊戲](https://x.com/chongdashu/status/2077886028866531655) (by [@chongdashu](https://x.com/chongdashu))

**結合 Kimi K3、代理 harness 與素材工具，同時產出 2D 與 3D 遊戲元素**

創作者表示在 Paper Mario 風格遊戲中使用 Kimi K3 搭配 Grok Build、以 Spriterrific 製作 2D 素材，並以幾何工具製作 3D 素材；來源展示了工具與 skill 的使用，但未公開可重用的完整 prompt

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-09.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-09-poster.jpg" alt="Case 9 source video poster" height="360"></a>

[Play case 9 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-09.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-11"></a>
### Case 11: [生成地鐵場景第一人稱射擊遊戲](https://x.com/bijanbowen/status/2077881805751873997) (by [@bijanbowen](https://x.com/bijanbowen))

**用具體的地鐵場景檢視生成的第一人稱射擊遊戲成果**

創作者展示歸因於 Kimi K3 的地鐵 FPS，並明確指出無法確定網紅身分是否影響結果；來源未提供 prompt 或可重現工作流程

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-11.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-11-poster.jpg" alt="Case 11 source video poster" height="360"></a>

[Play case 11 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-11.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-19"></a>
### Case 19: [使用 Blender MCP 建模 V8 引擎](https://x.com/aisearchio/status/2077962156147146925) (by [@aisearchio](https://x.com/aisearchio))

**透過 Blender MCP 與單次要求生成精細的機械 3D 模型**

評論者表示 Kimi K3 以 Blender MCP 從一個 prompt 生成完整 V8 引擎；貼文連結到更完整的評論，但指定記錄未揭露完整 prompt

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-19.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-19-poster.jpg" alt="Case 19 source video poster" height="360"></a>

[Play case 19 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-19.mp4)

Type: Integration | Date: 2026-07-17

---

<a id="case-23"></a>
### Case 23: [從一個參考建立可玩的戰鬥競技場](https://x.com/VORTEX_Promos/status/2077879705378730074) (by [@VORTEX_Promos](https://x.com/VORTEX_Promos))

**用單一參考測試一次生成完整可玩競技場的能力**

創作者表示 Kimi K3 從一個參考一次生成可玩的戰鬥競技場；貼文另含排行榜主張，但具體使用案例是所展示的競技場成果

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23-poster.jpg" alt="Case 23 source video poster" height="360"></a>

[Play case 23 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23-01.jpg" alt="Case 23 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-24"></a>
### Case 24: [將三款自動遊玩的復古遊戲做成 HTML 檔](https://x.com/rohanpaul_ai/status/2077889084761206860) (by [@rohanpaul_ai](https://x.com/rohanpaul_ai))

**要求在獨立 HTML 遊戲檔中包含圖形、敵人、規則與自動遊玩**

來源報告 Atomic Chat 的比較，模型將 Road Fighter、Battle City 與 Q*bert 製作成可自動遊玩的 HTML 檔；成本與品質比較由發布者報告，本案例庫未獨立重現

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-24.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-24-poster.jpg" alt="Case 24 source video poster" height="360"></a>

[Play case 24 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-24.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-27"></a>
### Case 27: [一次生成變色龍捉迷藏遊戲](https://x.com/aimlapi/status/2077898742179459274) (by [@aimlapi](https://x.com/aimlapi))

**生成包含顏色配對、程序式區域、聲音與多回合計分的單檔遊戲**

AIMLAPI 報告以相同 prompt 一次生成捉迷藏遊戲，並列出 $3.11 對應 Kimi K3、$12.23 對應 Fable 5；功能與成本主張均為供應商報告結果

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-27.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-27-poster.jpg" alt="Case 27 source video poster" height="360"></a>

[Play case 27 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-27.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-36"></a>
### Case 36: [用代理工具鏈建立 2.5D Paper Mario 類遊戲](https://x.com/chongdashu/status/2077981621223837739) (by [@chongdashu](https://x.com/chongdashu))

**結合 Kimi K3、Grok Build 或 Claude Code 以及 Spriterrific，組成 2.5D 遊戲工作流程**

創作者提供使用 Grok Build 與 Kimi K3 的完整操作示範，並展示以 Spriterrific 生成 sprite；來源標明工具，但沒有提供可重用的完整 prompt

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-36.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-36-poster.jpg" alt="Case 36 source video poster" height="360"></a>

[Play case 36 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-36.mp4)

Type: Tutorial | Date: 2026-07-17

---

<a id="case-43"></a>
### Case 43: [建立瀏覽器版 3D 武俠 RPG](https://x.com/AngryTomtweets/status/2077868163136450619) (by [@AngryTomtweets](https://x.com/AngryTomtweets))

**結合近戰、任務、物品欄、天氣、室內探索、Blender 環境製作與改編素材**

來源報告一款 Kimi K3 瀏覽器 RPG，包含近戰、任務、物品欄、動態天氣與可探索室內空間，另含 Blender 建模、碰撞改善、PBR 重新貼圖與改編開放素材

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-43.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-43-poster.jpg" alt="Case 43 source video poster" height="360"></a>

[Play case 43 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-43.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-44"></a>
### Case 44: [建立瀏覽器多人 Minecraft 類遊戲](https://x.com/Alezander907/status/2077926014710407407) (by [@Alezander907](https://x.com/Alezander907))

**在有邊界的時間與成本執行中，產出可線上多人遊玩的瀏覽器遊戲**

創作者表示 Kimi K3 在一小時內以 $6.57 成本建立可在瀏覽器遊玩的多人 Minecraft 類遊戲；這些是單一成果的自行報告數字

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-44.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-44-poster.jpg" alt="Case 44 source video poster" height="360"></a>

[Play case 44 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-44.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-48"></a>
### Case 48: [重現分割畫面合作瀏覽器遊戲](https://x.com/ridark_eth/status/2077882889803378969) (by [@ridark_eth](https://x.com/ridark_eth))

**用一個要求生成瀏覽器分割畫面合作玩法與即時環境互動**

創作者表示 Kimi K3 用一個 prompt 製作 It Takes Two 風格瀏覽器遊戲，Mario 與 Luigi 能以分割畫面即時彼此及與環境互動

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-48.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-48-poster.jpg" alt="Case 48 source video poster" height="360"></a>

[Play case 48 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-48.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-49"></a>
### Case 49: [使用 Command Code 設計模式生成可玩遊戲](https://x.com/naymur_dev/status/2077873562661335207) (by [@naymur_dev](https://x.com/naymur_dev))

**用 Command Code 的 design 指令一次生成遊戲，並記錄成果是否可玩**

創作者表示使用 Command Code design 模式進行一次生成比較，Kimi K3 執行以 $0.038 產出可玩遊戲；此成本與品質結果為自行報告

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-49.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-49-poster.jpg" alt="Case 49 source video poster" height="360"></a>

[Play case 49 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-49.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-51"></a>
### Case 51: [組裝具一致性的武俠瀏覽器 RPG](https://x.com/TokenGremlin/status/2077855657068310620) (by [@TokenGremlin](https://x.com/TokenGremlin))

**在一款遊戲中整合移動、戰鬥、任務、物品欄、天氣、探索與 3D 環境製作**

來源報告 Kimi K3 的武俠風格瀏覽器 RPG 結合近戰、任務、物品欄、動態天氣、可探索室內空間與具一致性的 3D 遊玩結構

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-51.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-51-poster.jpg" alt="Case 51 source video poster" height="360"></a>

[Play case 51 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-51.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-54"></a>
### Case 54: [建立可玩的 Hollow Knight 跨界遊戲](https://x.com/wangfeng0315/status/2077933531200991583) (by [@wangfeng0315](https://x.com/wangfeng0315))

**使用既有遊戲素材，建立 Knight 與 Kimi 對戰的可玩遊戲**

自稱在 Kimi 工作的創作者表示使用 Hollow Knight 素材製作一款 Knight 對戰 Kimi 的遊戲，並提供公開遊玩連結；歸屬與評估應考量此從屬關係

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54-poster.jpg" alt="Case 54 source video poster" height="360"></a>

[Play case 54 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54-01.jpg" alt="Case 54 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-17

---

<a id="case-60"></a>
### Case 60: [一次生成 Fall Guys 風格 3D 瀏覽器遊戲](https://x.com/aayushman2703/status/2077857886441783526) (by [@aayushman2703](https://x.com/aayushman2703))

**用一次生成要求製作可玩的 3D 障礙遊戲，並公開專案供檢查**

創作者表示 Kimi K3 一次生成 Fall Guys 風格瀏覽器遊戲，並稱來源連結了 prompt 與 GitHub 專案；此記錄未重現該 prompt

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-60.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-60-poster.jpg" alt="Case 60 source video poster" height="360"></a>

[Play case 60 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-60.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-61"></a>
### Case 61: [建立並自行測試末日里斯本 FPS](https://x.com/goncalo_canhoto/status/2077863166655037668) (by [@goncalo_canhoto](https://x.com/goncalo_canhoto))

**用一個 maximum-effort prompt 執行，在交付可玩 FPS 前反覆測試、截圖與迭代**

創作者表示 Kimi K3 經過約一小時的反覆測試、截圖與迭代後，產出可玩的末日里斯本瀏覽器 FPS；時間與流程細節皆為自行報告

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-61-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-61-01.jpg" alt="Case 61 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-63"></a>
### Case 63: [從簡單要求生成 Animal Crossing 風格遊戲](https://x.com/gagarot200/status/2077949230287896830) (by [@gagarot200](https://x.com/gagarot200))

**用極簡遊戲簡述檢視可玩性、遊戲迴圈與視差效果**

創作者表示 Kimi K3 從非常簡單的 prompt 生成完全可玩的 Animal Crossing 風格遊戲，包含遊戲迴圈與視差效果；指定記錄沒有完整原文

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-63.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-63-poster.jpg" alt="Case 63 source video poster" height="360"></a>

[Play case 63 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-63.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-65"></a>
### Case 65: [從一句簡述生成 Mario 類遊戲](https://x.com/izutorishima/status/2077939370154475992) (by [@izutorishima](https://x.com/izutorishima))

**用極簡的一次生成要求檢視可玩性、關卡設計、像素美術與視差**

創作者表示 Kimi K3 從單句簡述產出可正常運作且無明顯錯誤的 Mario 類遊戲，包含關卡結構與視差；同一份報告也批評音樂與圖像品質

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-01.jpg" alt="Case 65 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-02.jpg" alt="Case 65 source image 2" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-03.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-03.jpg" alt="Case 65 source image 3" height="360"></a>

Type: Demo | Date: 2026-07-17

---

<a id="case-67"></a>
### Case 67: [建立可運作的殭屍第一人稱射擊遊戲](https://x.com/X2worldtech/status/2077902793449296203) (by [@X2worldtech](https://x.com/X2worldtech))

**用具體的殭屍射擊目標檢視完整可玩的 FPS 成果**

來源展示歸因於 Kimi K3 的完整可運作殭屍 FPS；來源未提供 prompt、實作細節或外部遊玩評估

> [!WARNING]
> The original source permalink returned HTTP 404 during the 2026-07-17 audit. Attribution and evidence are preserved from the supplied high-confidence source package.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-67.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-67-poster.jpg" alt="Case 67 source video poster" height="360"></a>

[Play case 67 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-67.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-71"></a>
### Case 71: [建立獨立太空船遊戲](https://x.com/ChrisGPT/status/2078261217924087999) (by [@ChrisGPT](https://x.com/ChrisGPT))

**先用 Kimi K3 Standard 製作遊戲初版，再比較一致性、缺陷、視覺品質與 token 成本**

ChrisGPT 報告 Kimi K3 Standard 以約 2.50 美元 API token 成本完成獨立太空船遊戲初版；它比 GPT-5.5 初版更連貫、bug 更少，但 Fable 5 的視覺效果仍更精緻

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-71.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-71-poster.jpg" alt="Case 71 source video poster" height="360"></a>

[Play case 71 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-71.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-73"></a>
### Case 73: [讓 Summer Engine 遊戲自測](https://x.com/MathiasHeide/status/2078231589436465199) (by [@MathiasHeide](https://x.com/MathiasHeide))

**讓 Kimi K3 執行遊戲、檢查截圖與日誌，並在同一會話中修復可見缺陷**

Mathias Heide 報告 Kimi K3 在 27 分鐘的一次會話中建立可執行的紙飛機遊戲；模型啟動遊戲、截圖、讀取日誌、修復 bug，並把黑色紙飛機改為白色

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-73.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-73-poster.jpg" alt="Case 73 source video poster" height="360"></a>

[Play case 73 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-73.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-77"></a>
### Case 77: [迭代瀏覽器大逃殺遊戲](https://x.com/Ananth7e/status/2078158089929601203) (by [@Ananth7e](https://x.com/Ananth7e))

**建立功能豐富的瀏覽器遊戲時，要預期長時間自主迭代與有針對性的後續 prompt**

Ananth 報告 Kimi K3 用 130 多分鐘與 40 多輪 Chrome 截圖回饋建立 PUBG 風格遊戲，之後又用兩個 prompt 修復剩餘 bug

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-77.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-77-poster.jpg" alt="Case 77 source video poster" height="360"></a>

[Play case 77 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-77.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-83"></a>
### Case 83: [擴展太空游戏地形](https://x.com/startracker/status/2078543423167160342) (by [@startracker](https://x.com/startracker))

**把 Kimi K3 作为长時间构建 pass，把佔位地形替换成更大的真实地貌启髮游戏環境。**

創作者描述太空游戏第二天進展：Kimi K3 将小型占位海岸替换为 8 x 8 km 的冰岛启发地形，加入海岸感知的动画海洋，重建飛船外观，并生成下一步要用的环境資產。来源也说明执行较慢，錄制帧率问题仍待解决。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-83.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-83-poster.jpg" alt="Case 83 source video poster" height="360"></a>

[Play case 83 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-83.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-84"></a>
### Case 84: [解鎖 Three.js 物理渲染器](https://x.com/mattwatkajtys/status/2078523373861339475) (by [@mattwatkajtys](https://x.com/mattwatkajtys))

**当数学和物理邏辑可用但渲染管线停滯時，把 Kimi K3 引入 Three.js 物理项目。**

創作者表示物理世界构建器已停滞數月，底层数学和物理可用，但渲染管线无法推進。Kimi K3 的一次 pass 推动项目继续前進，影片展示了当前交互结果。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-84.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-84-poster.jpg" alt="Case 84 source video poster" height="360"></a>

[Play case 84 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-84.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-88"></a>
### Case 88: [用单文件構建瀏覽器 Counter-Strike](https://x.com/prasenx/status/2078453069021659477) (by [@prasenx](https://x.com/prasenx))

**用 Kimi K3 生成单文件瀏覽器 FPS，并檢查地圖、机器人、武器、回合规则和程序化音频是否完整。**

創作者報告用 Kimi K3 在一个超过 3,700 行的 HTML 文件里构建了类 Counter-Strike 瀏覽器游戏，无需 build step。成品包含 Dust2 风格地图、多种武器、换弹、巡逻与推進機器人、爆头、擊殺信息、两分鐘回合、程式化音频、Three.js、PBR，API 成本低于 5 美元。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-88.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-88-poster.jpg" alt="Case 88 source video poster" height="360"></a>

[Play case 88 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-88.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-96"></a>
### Case 96: [建構金字塔探險遊戲](https://x.com/ice_bearcute/status/2078828887468056763) (by [@ice_bearcute](https://x.com/ice_bearcute))

**用 Kimi K3 做一次完整的一日 3D 探索遊戲建構，再檢查任務、室內空間和探索範圍後評價品質。**

ice_bearcute 報告一天內完全用 Kimi K3 建構了 3D Pyramid Expedition 遊戲。來源說明這不是簡單外景，玩家可以探索古墓並完成任務；附帶媒體提供了可見 gameplay 證據。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-96.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-96-poster.jpg" alt="Case 96 source video poster" height="360"></a>

[Play case 96 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-96.mp4)

Type: Demo | Date: 2026-07-19

---

<a id="case-101"></a>
### Case 101: [比較 Minecraft 構建深度](https://x.com/vikktorrrre/status/2079294696459804762) (by [@vikktorrrre](https://x.com/vikktorrrre))

**用这个案例评估 Kimi K3 在「比較 Minecraft 構建深度」任务中的实际工作流、成本或限制。**

来源帖提供了与 比較 Minecraft 構建深度 相关的公开证据，包括作者描述、结果媒体或基准/教程信息；本仓库只保留可核验事实，不补写未公开的 prompt 或步骤。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-101.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-101-poster.jpg" alt="Case 101 source video poster" height="360"></a>

[Play case 101 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-101.mp4)

Type: Evaluation | Date: 2026-07-20

---

<a id="case-102"></a>
### Case 102: [構建 Fallout FPS 複製版](https://x.com/kirillk_web3/status/2079290747585437781) (by [@kirillk_web3](https://x.com/kirillk_web3))

**用这个案例评估 Kimi K3 在「構建 Fallout FPS 複製版」任务中的实际工作流、成本或限制。**

来源帖提供了与 構建 Fallout FPS 複製版 相关的公开证据，包括作者描述、结果媒体或基准/教程信息；本仓库只保留可核验事实，不补写未公开的 prompt 或步骤。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-102.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-102-poster.jpg" alt="Case 102 source video poster" height="360"></a>

[Play case 102 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-102.mp4)

Type: Demo | Date: 2026-07-20

---

<a id="case-105"></a>
### Case 105: [交付資料中心 RPG](https://x.com/demian_ai/status/2079239035596218578) (by [@demian_ai](https://x.com/demian_ai))

**用这个案例评估 Kimi K3 在「交付資料中心 RPG」任务中的实际工作流、成本或限制。**

来源帖提供了与 交付資料中心 RPG 相关的公开证据，包括作者描述、结果媒体或基准/教程信息；本仓库只保留可核验事实，不补写未公开的 prompt 或步骤。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-105.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-105-poster.jpg" alt="Case 105 source video poster" height="360"></a>

[Play case 105 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-105.mp4)

Type: Demo | Date: 2026-07-20

---

<a id="case-108"></a>
### Case 108: [構建 3D 賽車遊戲](https://x.com/LexnLin/status/2079233761242235081) (by [@LexnLin](https://x.com/LexnLin))

**用这个案例评估 Kimi K3 在「構建 3D 賽車遊戲」任务中的实际工作流、成本或限制。**

来源帖提供了与 構建 3D 賽車遊戲 相关的公开证据，包括作者描述、结果媒体或基准/教程信息；本仓库只保留可核验事实，不补写未公开的 prompt 或步骤。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-poster.jpg" alt="Case 108 source video poster" height="360"></a>

[Play case 108 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-01.jpg" alt="Case 108 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-02.jpg" alt="Case 108 source image 2" height="360"></a>

Type: Demo | Date: 2026-07-20

---

<a id="case-111"></a>
### Case 111: [對比 Geometry Dash 複製版](https://x.com/Nekt_0/status/2079629004483465473) (by [@Nekt_0](https://x.com/Nekt_0))

**用同一需求的遊戲 build 對比，判斷 Kimi K3 是否足夠做可玩的行動風格原型。**

Nekt 表示 Kimi K3 用約 30 分鐘和 20 萬 tokens 建構了 Geometry Dash 風格複製版，包含跳躍、障礙、關卡、音樂和視覺效果，並在公開影片中與 Claude Fable 5 的 build 對比。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-111.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-111-poster.jpg" alt="Case 111 source video poster" height="360"></a>

[Play case 111 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-111.mp4)

Type: Evaluation | Date: 2026-07-21

---

<a id="case-112"></a>
### Case 112: [執行 Command Code 復古遊戲測試](https://x.com/naymur_dev/status/2079627963000398334) (by [@naymur_dev](https://x.com/naymur_dev))

**用 Command Code 的多模型設計測試對比 Kimi K3 的 gameplay 功能和各模型成本。**

Naymur 稱在 Command Code 中對 Fable 5、GPT-5.6 Sol、Grok 4.5 和 Kimi K3 執行同一個 /design prompt。貼文說 Kimi K3 生成了有 gameplay、升級、子彈和 boss 戰的 ASCII 復古遊戲，報告成本為 $0.15。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-112.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-112-poster.jpg" alt="Case 112 source video poster" height="360"></a>

[Play case 112 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-112.mp4)

Type: Evaluation | Date: 2026-07-21

---

<a id="case-116"></a>
### Case 116: [評測 Space Discoverer 遊戲](https://x.com/fabriciocarraro/status/2079548607393382528) (by [@fabriciocarraro](https://x.com/fabriciocarraro))

**用 Space Discoverer 小基準比較模型在通用 3D 瀏覽器遊戲 brief 下的輸出。**

Fabricio Carraro 報告了 Claude Fable 5、GPT-5.6 Sol 和 Kimi K3 在最高 reasoning 設定下的小基準。任務是名為 Space Discoverer 的 3D 瀏覽器遊戲，貼文稱三個模型都收斂到 WebGL 2 上的 Three.js。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-116.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-116-poster.jpg" alt="Case 116 source video poster" height="360"></a>

[Play case 116 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-116.mp4)

Type: Benchmark | Date: 2026-07-21

---

<a id="case-117"></a>
### Case 117: [建構真實道路駕駛遊戲](https://x.com/bijanbowen/status/2079526003643179102) (by [@bijanbowen](https://x.com/bijanbowen))

**把 Kimi K3 與 Blender、Godot 結合，用真實本地道路地圖原型化一個駕駛遊戲。**

Bijan Bowen 展示 Kimi K3 使用 Blender 和 Godot 製作駕駛遊戲，並以作者附近的一段真實道路作為地圖基礎。附帶影片是該 build 狀態的公開證據。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-117.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-117-poster.jpg" alt="Case 117 source video poster" height="360"></a>

[Play case 117 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-117.mp4)

Type: Demo | Date: 2026-07-21

---

<a id="case-122"></a>
### Case 122: [建構纵向平台游戏](https://x.com/diegocabezas01/status/2079946676270219488) (by [@diegocabezas01](https://x.com/diegocabezas01))

**用简洁游戏 brief 測試 Kimi K3 能否返回单文件浏览器原型。**

Diego Cabezas 展示了 Kimi K3 Max 生成纵向平台游戏的執行結果，玩家会在移动平台上不断向上跳。帖子记录这是一次生成的单 HTML 結果。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-122.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-122-poster.jpg" alt="Case 122 source video poster" height="360"></a>

[Play case 122 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-122.mp4)

Type: Demo | Date: 2026-07-22

---

<a id="case-127"></a>
### Case 127: [驗證 Geometry Dash 生成结果](https://x.com/Kirratr/status/2079902410042909108) (by [@Kirratr](https://x.com/Kirratr))

**把 Kimi K3 游戏构建与 solver 和浏览器回放測試结合，再判断它是否可作为完成原型。**

Kirratr 報告 Kimi K3 在同一个 Geometry Dash 风格 brief 上耗时 36 分 53 秒。來源称 beam-search solver 找到 64 跳通关路径，并在真实浏览器中回放，移动视口測試无控制台錯誤。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-127.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-127-poster.jpg" alt="Case 127 source video poster" height="360"></a>

[Play case 127 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-127.mp4)

Type: Benchmark | Date: 2026-07-22

---


<a id="frontend-motion"></a>
## 🎨 前端與動態設計

<a id="case-5"></a>
### Case 5: [建立可互動的動態前端](https://x.com/chetaslua/status/2077749371144442022) (by [@chetaslua](https://x.com/chetaslua))

**製作暫停動畫後仍可互動的動態圖形**

創作者表示整個製作耗時 42 分鐘、一次生成、只用簡單程式碼，沒有 harness、MCP 或 skill

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05-poster.jpg" alt="Case 5 source video poster" height="360"></a>

[Play case 5 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-6"></a>
### Case 6: [製作同步的動態廣告](https://x.com/abhinavflac/status/2077760297918484667) (by [@abhinavflac](https://x.com/abhinavflac))

**檢查音樂、效果與動作是否同步**

創作者表示以純 prompt 一次產出 Spotify 風格廣告，但沒有公開完整 prompt

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06-poster.jpg" alt="Case 6 source video poster" height="360"></a>

[Play case 6 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-14"></a>
### Case 14: [完全用程式碼製作動態設計](https://x.com/chetaslua/status/2077952938564354503) (by [@chetaslua](https://x.com/chetaslua))

**測試一次生成的程式開發流程能否在沒有輔助生成工具時完成動態設計**

創作者表示 Kimi K3 一次生成的動態設計完全由程式碼完成，未使用 MCP、skill、工具、影片生成或特殊 prompt；來源未提供完整 prompt

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-14.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-14-poster.jpg" alt="Case 14 source video poster" height="360"></a>

[Play case 14 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-14.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-15"></a>
### Case 15: [研究人物並建立動畫個人網站](https://x.com/nicky_sap/status/2077857190707429411) (by [@nicky_sap](https://x.com/nicky_sap))

**提供寬泛的個人網站簡述，再檢視模型的研究、規劃、迭代與瀏覽器驗證流程**

創作者表示 Kimi K3 研究 Nick Saponaro，並依寬泛要求製作動畫個人網站，過程包含規劃、測試、迭代與瀏覽器檢查；此成果是自行報告的工作流程展示

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-15.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-15-poster.jpg" alt="Case 15 source video poster" height="360"></a>

[Play case 15 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-15.mp4)

Type: Tutorial | Date: 2026-07-16

---

<a id="case-17"></a>
### Case 17: [生成黑洞模擬](https://x.com/chetaslua/status/2077961850352971796) (by [@chetaslua](https://x.com/chetaslua))

**用科學視覺化任務檢視生成的黑洞模擬**

創作者展示歸因於 Kimi K3 的黑洞模擬，並稱其為所見最佳；來源提供可見成果，但沒有 prompt、評分標準或獨立驗證

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-17.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-17-poster.jpg" alt="Case 17 source video poster" height="360"></a>

[Play case 17 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-17.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-22"></a>
### Case 22: [測試複雜前端建模、粒子與 shader](https://x.com/karminski3/status/2077889959223337099) (by [@karminski3](https://x.com/karminski3))

**使用公開前端 prompt，在一次執行中檢視建模精度、粒子效果與行內 shader 生成**

創作者表示 Kimi K3 一次執行的前端成果涵蓋精密建模、粒子效果與複雜行內 shader 程式碼，並指出測試 prompt 已在連結來源公開

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-22.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-22-poster.jpg" alt="Case 22 source video poster" height="360"></a>

[Play case 22 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-22.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-26"></a>
### Case 26: [一次生成程序式音樂工具](https://x.com/mirochill/status/2077723551331758478) (by [@mirochill](https://x.com/mirochill))

**測試一次生成互動式程序音樂產生器，並審慎比較可見成果**

創作者表示 Kimi K3 一次生成程序式音樂工具，並認為其成果優於 Fable 5 與 GPT-5.6 Sol；這是創作者自己的測試集，不是標準化基準

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-26-poster.jpg" alt="Case 26 source video poster" height="360"></a>

[Play case 26 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-26.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-33"></a>
### Case 33: [從兩張圖片建立 Three.js 產品頁](https://x.com/1littlecoder/status/2077890296806031665) (by [@1littlecoder](https://x.com/1littlecoder))

**使用兩張參考圖片與明確的 Three.js 要求生成產品展示頁**

創作者表示 Kimi K3 從兩張圖片設計產品頁，並產出明確要求的 Three.js 版本；來源未提供更多 prompt 或實作細節

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-33.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-33-poster.jpg" alt="Case 33 source video poster" height="360"></a>

[Play case 33 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-33.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-39"></a>
### Case 39: [發明豪華麵包切割器及其產品頁](https://x.com/filicroval/status/2077871090731221438) (by [@filicroval](https://x.com/filicroval))

**在單一設計成果中結合產品構想、爆炸圖、示範與登陸頁**

創作者表示 Kimi K3 發明斷頭台式麵包切割器，將其定位為豪華產品，並產出含爆炸圖與示範的登陸頁

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-39.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-39-poster.jpg" alt="Case 39 source video poster" height="360"></a>

[Play case 39 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-39.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-45"></a>
### Case 45: [生成十秒遞迴鵜鶘 GIF](https://x.com/1littlecoder/status/2077880380900937865) (by [@1littlecoder](https://x.com/1littlecoder))

**用完整指定的循環動畫簡述，檢視 GIF 的敘事連續性與遞迴效果**

來源包含一段 prompt，要求製作十秒循環 GIF：一隻鵜鶘騎自行車，透過簡訊收到同一支影片，鏡頭再放大；創作者展示 Kimi K3 產出的動畫

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-45.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-45-poster.jpg" alt="Case 45 source video poster" height="360"></a>

[Play case 45 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-45.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-55"></a>
### Case 55: [生成 BMW M4 CS 側視 SVG](https://x.com/HarshithLucky3/status/2077765821380886942) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**用指定車款與視角檢視向量插畫輸出**

創作者展示歸因於 Kimi K3 Max 的 BMW M4 CS 側視 SVG；指定來源包含成果，但沒有 prompt 或製作步驟

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-55-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-55-01.jpg" alt="Case 55 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-58"></a>
### Case 58: [透過截圖回饋重現 Gargantua](https://x.com/AngryTomtweets/status/2077868981659324444) (by [@AngryTomtweets](https://x.com/AngryTomtweets))

**把反覆截圖當作觀察資料，用來診斷並改善科學視覺化**

來源表示 Kimi K3 透過 62 張自行截圖重現 Interstellar 的 Gargantua，每次讀取結果、診斷問題，再迭代採取行動

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-58.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-58-poster.jpg" alt="Case 58 source video poster" height="360"></a>

[Play case 58 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-58.mp4)

Type: Tutorial | Date: 2026-07-16

---

<a id="case-66"></a>
### Case 66: [以 62 張截圖改善黑洞視覺化](https://x.com/TokenGremlin/status/2077855959201042645) (by [@TokenGremlin](https://x.com/TokenGremlin))

**使用截圖回饋迴圈，在多次迭代中讀取、診斷並修正視覺模擬**

來源表示 Kimi K3 透過觀察並改善 62 張截圖的輸出，重建 Interstellar 的 Gargantua；這展示所報告的回饋迴圈，而不是獨立驗證其物理準確性

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-66.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-66-poster.jpg" alt="Case 66 source video poster" height="360"></a>

[Play case 66 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-66.mp4)

Type: Tutorial | Date: 2026-07-16

---

<a id="case-68"></a>
### Case 68: [製作後訓練行銷 PDF](https://x.com/Satvik_Pen/status/2077859673517023313) (by [@Satvik_Pen](https://x.com/Satvik_Pen))

**用指定產品與交付格式生成行銷文件**

創作者表示要求 Kimi K3 製作 Thinking Machines 的 Inkling 後訓練行銷 PDF，並分享成果，同時稱讚幕後流程；來源未提供 prompt 或評估標準

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-01.png" alt="Case 68 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-02.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-02.png" alt="Case 68 source image 2" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-03.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-03.png" alt="Case 68 source image 3" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-04.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-04.png" alt="Case 68 source image 4" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-70"></a>
### Case 70: [用一個 prompt 建立使用者介面](https://x.com/BrianMRey/status/2077891942088671689) (by [@BrianMRey](https://x.com/BrianMRey))

**用單次要求生成並檢視完整 UI 設計**

創作者展示歸因於 Kimi K3 單一 prompt 執行的 UI 設計，並給予非常正面的主觀評價；來源未提供完整 prompt 或評分標準

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-70.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-70-poster.jpg" alt="Case 70 source video poster" height="360"></a>

[Play case 70 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-70.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-78"></a>
### Case 78: [建立獲獎風格網站](https://x.com/viktoroddy/status/2078140696910037002) (by [@viktoroddy](https://x.com/viktoroddy))

**透過完整錄影評估 Kimi K3 的精緻網站建立過程，而不只看最終截圖**

Viktor Oddy 發布 13 分鐘教學，展示如何用 Kimi K3 建立獲獎風格網站；完整影片提供過程證據

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-78.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-78-poster.jpg" alt="Case 78 source video poster" height="360"></a>

[Play case 78 tutorial video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-78.mp4)

Type: Tutorial | Date: 2026-07-17

---

<a id="case-81"></a>
### Case 81: [構建滾动 Metaball 前端](https://x.com/abhinavflac/status/2078603131055993130) (by [@abhinavflac](https://x.com/abhinavflac))

**让 Kimi K3 生成 Awwwards 风格滚动页面，并檢查数学效果是否能替代重型 mesh 或貼圖资源。**

創作者報告一次 Kimi K3 前端会话生成了隨滚动反应的 metaball 網站，视觉行为由数学驱动，没有使用 mesh 或貼图。附带影片是可见成品；来源没有公开可复用 prompt 或實作步骤。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-81.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-81-poster.jpg" alt="Case 81 source video poster" height="360"></a>

[Play case 81 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-81.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-82"></a>
### Case 82: [跨模型重设计個人網站](https://x.com/fabriciocarraro/status/2078574831466078265) (by [@fabriciocarraro](https://x.com/fabriciocarraro))

**用多个 coding harness 執行同一个網站重设计 brief，并比较耗時、视觉方向和与现有身份的匹配度。**

創作者用官方 harness 和最高 effort 模式測試 Fable 5、GPT-5.6 Sol 与 Kimi K3 重设计个人網站。Kimi K3 用时約 50 分鐘，Fable 約 35 分鐘，Sol 約 70 分鐘；帖子把它定位为单任务 mini benchmark。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-82.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-82-poster.jpg" alt="Case 82 source video poster" height="360"></a>

[Play case 82 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-82.mp4)

Type: Evaluation | Date: 2026-07-18

---

<a id="case-86"></a>
### Case 86: [構建交互式頭皮探索器](https://x.com/MiaAI_lab/status/2078508824752017757) (by [@MiaAI_lab](https://x.com/MiaAI_lab))

**用 Kimi K3 一次生成包含解剖层、響应式髮丝和交互热点的 3D 教育场景。**

創作者報告 Kimi K3 用約 105k tokens 一次生成真实感頭皮探索器，包含电影级光照、分层解剖结构、響應式髮絲、橫截面和教育热点。来源称效果令人印象深刻但成本不低，并提供可试用链接。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-86.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-86-poster.jpg" alt="Case 86 source video poster" height="360"></a>

[Play case 86 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-86.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-87"></a>
### Case 87: [分享 3D 地球儀儀表盘 Prompt](https://x.com/hqmank/status/2078465403349840144) (by [@hqmank](https://x.com/hqmank))

**研究 Kimi K3 3D 地球儀儀表盤的 prompt 与参考圖设置，而不是只从最终圖反推工作流。**

創作者回应他人对 Kimi K3 3D 地球仪儀表板 demo 的 prompt 与参考图请求，并在附图中公开两者。本仓库将其记錄为教程型 prompt 边界，但不从图片中转錄 prompt 文本。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-87.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-87-poster.jpg" alt="Case 87 source video poster" height="360"></a>

[Play case 87 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-87.mp4)

Type: Tutorial | Date: 2026-07-18

---

<a id="case-94"></a>
### Case 94: [執行五項 UI UX 測試](https://x.com/MAXdeg0/status/2078855257686196399) (by [@MAXdeg0](https://x.com/MAXdeg0))

**不要只看一張 frontend 截圖，而是用多項 UI、Logo 和 Figma MCP 任務評估 Kimi K3。**

MAXdeg0 報告用 Claude Code 和 Figma MCP server 對 Kimi K3 做了五項 UI/UX 與 logo 設計測試。來源列出 landing page 重建、hero section 重建和品牌設計等任務，並至少給出了 landing pass 的時間與成本。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-94.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-94-poster.jpg" alt="Case 94 source video poster" height="360"></a>

[Play case 94 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-94.mp4)

Type: Evaluation | Date: 2026-07-19

---

<a id="case-97"></a>
### Case 97: [從參考圖建立 landing](https://x.com/MAXdeg0/status/2078776969072877715) (by [@MAXdeg0](https://x.com/MAXdeg0))

**用參考圖板、Figma AI、Motion Sites 與 Kimi K3，把視覺方向轉成可複用的 landing page section。**

MAXdeg0 描述了一個 landing page workflow：從 Pinterest 拉取風格參考，用 Figma AI remix 質感，或把 UI reference 加 prompt 貼進 Motion Sites，讓 Kimi K3 建構頁面。貼文還說該方法可複用於更多 section，並連結完整 prompting guide。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-97.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-97-poster.jpg" alt="Case 97 source video poster" height="360"></a>

[Play case 97 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-97.mp4)

Type: Tutorial | Date: 2026-07-19

---

<a id="case-103"></a>
### Case 103: [跟做高級網站教學](https://x.com/_guillecasaus/status/2079258261014908980) (by [@_guillecasaus](https://x.com/_guillecasaus))

**用这个案例评估 Kimi K3 在「跟做高級網站教學」任务中的实际工作流、成本或限制。**

来源帖提供了与 跟做高級網站教學 相关的公开证据，包括作者描述、结果媒体或基准/教程信息；本仓库只保留可核验事实，不补写未公开的 prompt 或步骤。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-103.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-103-poster.jpg" alt="Case 103 source video poster" height="360"></a>

[Play case 103 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-103.mp4)

Type: Tutorial | Date: 2026-07-20

---

<a id="case-106"></a>
### Case 106: [比較人形機器人前端成本](https://x.com/ChrisGPT/status/2079236298464796958) (by [@ChrisGPT](https://x.com/ChrisGPT))

**用这个案例评估 Kimi K3 在「比較人形機器人前端成本」任务中的实际工作流、成本或限制。**

来源帖提供了与 比較人形機器人前端成本 相关的公开证据，包括作者描述、结果媒体或基准/教程信息；本仓库只保留可核验事实，不补写未公开的 prompt 或步骤。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-106.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-106-poster.jpg" alt="Case 106 source video poster" height="360"></a>

[Play case 106 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-106.mp4)

Type: Benchmark | Date: 2026-07-20

---

<a id="case-115"></a>
### Case 115: [對比 Three.js Kimi-vs-GLM 建構](https://x.com/thehypedotnews/status/2079553731218325840) (by [@thehypedotnews](https://x.com/thehypedotnews))

**用同一組程序化 Three.js prompts 跑 Kimi K3 和 GLM 5.2，比較前端與 3D build 行為。**

The Hype 稱對 Kimi K3 和 GLM 5.2 執行了三個單檔 HTML + Three.js prompts：帶 CRT canvas texture 的 80 年代客廳、帶傳動系統運動學的公路車，以及玻璃水族箱場景。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-115.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-115-poster.jpg" alt="Case 115 source video poster" height="360"></a>

[Play case 115 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-115.mp4)

Type: Benchmark | Date: 2026-07-21

---

<a id="case-121"></a>
### Case 121: [用参考图生成落地页](https://x.com/Oluwaphilemon1/status/2079951300108697683) (by [@Oluwaphilemon1](https://x.com/Oluwaphilemon1))

**測試落地页生成时，给 Kimi K3 提供强视觉参考和分轮指导。**

Oluwaphilemon 描述了给 Kimi K3 一张图片参考和详细 prompt 来生成落地页的过程。來源指出 Kimi 起初尝试把自行车做成 3D 模型，经过几轮指导后得到更干净的結果。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-121.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-121-poster.jpg" alt="Case 121 source video poster" height="360"></a>

[Play case 121 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-121.mp4)

Type: Demo | Date: 2026-07-22

---

<a id="case-128"></a>
### Case 128: [模拟 3D 粒子系统](https://x.com/jadeferrara_/status/2079884161251262540) (by [@jadeferrara_](https://x.com/jadeferrara_))

**用粒子模拟 prompt 对比 Kimi K3 与闭源模型的运动质量。**

Jade Ferrara 報告给 Kimi K3 和 Opus 4.8 相同的 3D 粒子系统 prompt。來源称 Kimi 的分布更自然、运动更平滑、聚集和漂移更像物理过程，同时 API 成本更低。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-128.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-128-poster.jpg" alt="Case 128 source video poster" height="360"></a>

[Play case 128 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-128.mp4)

Type: Evaluation | Date: 2026-07-22

---


<a id="coding-integrations"></a>
## 💻 程式開發與整合

<a id="case-18"></a>
### Case 18: [製作具備可用 macOS 的虛擬 MacBook](https://x.com/scottstts/status/2077890054299541890) (by [@scottstts](https://x.com/scottstts))

**結合 Three.js 硬體渲染與可互動的瀏覽器作業系統模擬**

來源表示 Kimi K3 以 Three.js 製作虛擬 MacBook，並帶有可運作的 macOS 風格環境；來源展示成果，但未提供實作步驟

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-18.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-18-poster.jpg" alt="Case 18 source video poster" height="360"></a>

[Play case 18 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-18.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-25"></a>
### Case 25: [從 DSL 到 PTX 建立 GPU 編譯器](https://x.com/rohanpaul_ai/status/2077886618657231220) (by [@rohanpaul_ai](https://x.com/rohanpaul_ai))

**用端到端編譯器任務涵蓋 DSL、編譯器 pass、PTX 生成與 Tensor Core 路徑**

來源表示 Kimi K3 從零建立 GPU 編譯器，涵蓋 DSL、pass 與 PTX 生成，並將其 Tensor Core 路徑與 Triton 比較；指定記錄沒有獨立基準細節

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-25-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-25-01.png" alt="Case 25 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-32"></a>
### Case 32: [以 WebGL2 建立即時黑洞光線追蹤器](https://x.com/AlicanKiraz0/status/2077885419744612597) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**測試用一個 prompt 在單一 HTML 檔內生成原生 WebGL2 測地線光線追蹤器**

作者描述一項程式開發基準，要求在單一檔案中完成可運作的原生 WebGL2 黑洞光線彎曲追蹤器；指定記錄確立任務與參與模型，但不是完整的獨立結果稽核

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-32.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-32-poster.jpg" alt="Case 32 source video poster" height="360"></a>

[Play case 32 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-32.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-46"></a>
### Case 46: [以 mGBA WASM 為核心建立 Game Boy Advance 模擬器](https://x.com/teortaxesTex/status/2077925090168062272) (by [@teortaxesTex](https://x.com/teortaxesTex))

**整合授權 3D 模型與真正的模擬器核心，再透過遞迴方式改善介面與遊玩體驗**

所引述的 Kimi K3 專案改編授權的 AGB-001 模型、整合 mGBA WASM 核心，並透過遞迴式自我改善優化介面與遊玩體驗；貼文引用專案說明，並非獨立重現

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-46-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-46-01.jpg" alt="Case 46 source image 1" height="360"></a>

Type: Integration | Date: 2026-07-17

---

<a id="case-50"></a>
### Case 50: [從中文來源研究多個主題](https://x.com/tphuang/status/2077911994607239400) (by [@tphuang](https://x.com/tphuang))

**透過長時間研究任務比較不同模型世代的完整度與延遲**

作者表示以中文來源測試 Kimi K3 的多個研究主題，認為它比 K2.6 更完整但速度較慢；貼文也指出當時服務需求量很大

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-50-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-50-01.png" alt="Case 50 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-17

---

<a id="case-56"></a>
### Case 56: [在瀏覽器複製具可用應用程式的 macOS](https://x.com/twid/status/2077924755357974989) (by [@twid](https://x.com/twid))

**建立包含音樂、瀏覽器與電子郵件應用程式的瀏覽器作業系統模擬**

來源表示 Kimi K3 被用來製作瀏覽器版 macOS 複製品，包含音樂、瀏覽器、電子郵件與其他功能；來源未提供實作細節

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-56.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-56-poster.jpg" alt="Case 56 source video poster" height="360"></a>

[Play case 56 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-56.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-62"></a>
### Case 62: [建立 FaceTime 可運作的 macOS 模擬](https://x.com/LinearUncle/status/2077919552239997078) (by [@LinearUncle](https://x.com/LinearUncle))

**用虛擬作業系統任務測試生成的應用互動是否能運作**

創作者展示歸因於 Kimi K3 的 macOS 風格環境，並表示其 FaceTime 功能可運作；來源未提供設定或驗證步驟

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-62-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-62-01.jpg" alt="Case 62 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-17

---

<a id="case-64"></a>
### Case 64: [加入雙任務前端效果比較器](https://x.com/MinLiBuilds/status/2077939461510615376) (by [@MinLiBuilds](https://x.com/MinLiBuilds))

**建立工具以選取兩個已完成任務、並列顯示，並同步視角與互動**

創作者表示要求 Kimi K3 新增前端比較流程，包含任務選擇、雙瀏覽器窗格、物件與漫遊模式、同步視角及互動測試；貼文也指出模型更廣泛的限制

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-64.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-64-poster.jpg" alt="Case 64 source video poster" height="360"></a>

[Play case 64 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-64.mp4)

Type: Tutorial | Date: 2026-07-17

---

<a id="case-75"></a>
### Case 75: [將 Kimi 設定為 Codex 子 agent](https://x.com/nauczymycieAI/status/2078181182701736132) (by [@nauczymycieAI](https://x.com/nauczymycieAI))

**讓 Codex 保留編排職責，把前端執行交給 Kimi K3 OpenCode 子 agent，並明確密鑰邊界**

nauczymycieAI 提供三階段教學：安裝並驗證 OpenCode，手動建立且不貼入 Codex 的 Kimi API Key，連接 Kimi K3，並建立全域 Codex skill 路由前端任務

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-75.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-75.jpg" alt="Case 75 source image 1" height="360"></a>

Type: Tutorial | Date: 2026-07-17

---

<a id="case-79"></a>
### Case 79: [透過 ChatLLM 路由簡單編碼](https://x.com/abacusai/status/2078022418661257411) (by [@abacusai](https://x.com/abacusai))

**建立任務路由，將簡單編碼交給 Kimi K3，把困難編碼與設計保留給其他模型**

Abacus AI 宣布 ChatLLM 支援 Kimi K3：簡單編碼用 Kimi K3、困難編碼用 Fable 5、設計用 GPT-5.6 Sol；同一路由可用於 ChatLLM、Abacus AI agent 或 Claude Code

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-79.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-79.jpg" alt="Case 79 source image 1" height="360"></a>

Type: Integration | Date: 2026-07-17

---

<a id="case-91"></a>
### Case 91: [用生成資產建構 CS](https://x.com/karankendre/status/2078938615900688728) (by [@karankendre](https://x.com/karankendre))

**原型化小型 Counter-Strike 風格瀏覽器遊戲時，用 Kimi K3 寫遊戲程式碼，用 GPT Image 2 生成資產。**

Karan Kendre 報告使用 Kimi K3 建構遊戲、GPT Image 2 建構資產，做出一個 Counter-Strike 風格專案，總成本約 10 美元。來源影片是可見成品，因此該記錄更適合作為多工具組合 workflow，而不是 Kimi 單模型 benchmark。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-91.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-91-poster.jpg" alt="Case 91 source video poster" height="360"></a>

[Play case 91 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-91.mp4)

Type: Integration | Date: 2026-07-19

---

<a id="case-95"></a>
### Case 95: [使用 Command Code Design skill](https://x.com/MrAhmadAwais/status/2078841789205934547) (by [@MrAhmadAwais](https://x.com/MrAhmadAwais))

**在 token 預算內建構視覺遊戲原型時，把 Kimi K3 與 Command Code 的專用 design skill 結合使用。**

Ahmad Awais 報告用 Kimi K3、Command Code 和 /design skill 建構 Forza 風追車視角遊戲。貼文稱整次 session 成本 0.97 美元，並包含道路/車輛比例、背景、動畫、霧效等修復步驟，是具體的 agent harness workflow。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-95.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-95-poster.jpg" alt="Case 95 source video poster" height="360"></a>

[Play case 95 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-95.mp4)

Type: Integration | Date: 2026-07-19

---

<a id="case-109"></a>
### Case 109: [在 Claude Code 中執行 Kimi K3](https://x.com/boxmining/status/2079115758618239337) (by [@boxmining](https://x.com/boxmining))

**用这个案例评估 Kimi K3 在「在 Claude Code 中執行 Kimi K3」任务中的实际工作流、成本或限制。**

来源帖提供了与 在 Claude Code 中執行 Kimi K3 相关的公开证据，包括作者描述、结果媒体或基准/教程信息；本仓库只保留可核验事实，不补写未公开的 prompt 或步骤。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-109.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-109-poster.jpg" alt="Case 109 source video poster" height="360"></a>

[Play case 109 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-109.mp4)

Type: Integration | Date: 2026-07-20

---

<a id="case-119"></a>
### Case 119: [透過 claude-code-router 路由 Kimi](https://x.com/sairahul1/status/2079393675885588855) (by [@sairahul1](https://x.com/sairahul1))

**在現有 Claude Code workflow 中透過 claude-code-router 試用 Kimi K3，同時避免不必要的 proxy mode。**

Sai Rahul 描述 Moonshot 贊助的 claude-code-router Kimi K3 支援，包括內建 presets、API key 或訂閱匯入、原生訂閱路由、餘額和用量 dashboard、failover、快取價格，並提醒除非需要否則保持 proxy mode 關閉。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-119.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-119-poster.jpg" alt="Case 119 source video poster" height="360"></a>

[Play case 119 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-119.mp4)

Type: Integration | Date: 2026-07-21

---

<a id="case-125"></a>
### Case 125: [執行开源 agent harness](https://x.com/ShenSeanChen/status/2079914609222221976) (by [@ShenSeanChen](https://x.com/ShenSeanChen))

**用共享 agent harness 对比 Kimi K3 与其他前沿模型在工具调用任務中的表现。**

Sean Chen 描述了在开源 AI agent harness 中让 Kimi K3 与多种模型竞赛：包含 agent loop、memory retrieval gate、工具调用、eval、tracing 和实时成本面板。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-125.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-125-poster.jpg" alt="Case 125 source video poster" height="360"></a>

[Play case 125 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-125.mp4)

Type: Benchmark | Date: 2026-07-22

---

<a id="case-129"></a>
### Case 129: [通过 Codex OAuth 執行 Kimi](https://x.com/biscuitweb3/status/2079844959843197342) (by [@biscuitweb3](https://x.com/biscuitweb3))

**当 Kimi K3 编码工作流需要避免手动配置 API key 时，使用 Codex OAuth 路径。**

biscuitweb3 報告 Kimi K3 已可通过 OAuth 在 Codex 内執行，无需额外 API key 设置。附图提供了该集成界面的证据。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-129-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-129-01.jpg" alt="Case 129 source image 1" height="360"></a>

Type: Integration | Date: 2026-07-22

---


<a id="evaluation-limits"></a>
## 🧪 評估與限制

<a id="case-7"></a>
### Case 7: [比較 BridgeBench 熔岩燈任務的前端設計](https://x.com/bridgemindai/status/2077868061953007908) (by [@bridgemindai](https://x.com/bridgemindai))

**把 BridgeBench 熔岩燈任務視為有邊界的單次前端設計比較，而不是通用排名**

BridgeMind AI 報告 Kimi K3 在其 BridgeBench 熔岩燈任務中勝過 Fable 5，並在所引述的競技場排名第一；這些都是發布者報告的比較結果

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-07.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-07-poster.jpg" alt="Case 7 source video poster" height="360"></a>

[Play case 7 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-07.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-8"></a>
### Case 8: [對編輯語氣腳本寫作進行基準測試](https://x.com/Whats_AI/status/2077860441380798908) (by [@Whats_AI](https://x.com/Whats_AI))

**在明確標示的內部基準中衡量編輯語氣契合度、相對排名與每篇腳本成本**

Whats_AI 報告初步內部結果為 2,840 Elo、榜單第一，且每篇腳本約 $0.25；這是單一組織的初步基準，不是一般效能或價格保證

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-08-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-08-01.jpg" alt="Case 8 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-16

---

<a id="case-10"></a>
### Case 10: [比較 Flappy 類遊戲的設計、成本與難度](https://x.com/MrAhmadAwais/status/2077915347974557862) (by [@MrAhmadAwais](https://x.com/MrAhmadAwais))

**比較生成遊戲時記錄難度設定、成本、設計與遊玩功能**

Command Code 的內部 Flappy 基準報告各模型使用不同難度設定，並列出 Kimi K3 為 $0.024、Fable 5 為 $0.42、GPT-5.6 Sol 為 $0.15；設定不一致，因此這只是有邊界的內部比較

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-10.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-10-poster.jpg" alt="Case 10 source video poster" height="360"></a>

[Play case 10 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-10.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-12"></a>
### Case 12: [用相同設計 prompt 比較遊戲設計](https://x.com/CommandCodeAI/status/2077921526213746948) (by [@CommandCodeAI](https://x.com/CommandCodeAI))

**固定設計 prompt，分別檢視節奏、設計感與遊玩感受**

Command Code 報告以相同 prompt 比較 Kimi K3、GPT-5.6 Sol 與 Fable 5；貼文稱 Kimi K3 的設計感表現良好，而另兩者遊玩節奏過快，這仍是發布者的評價

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-12.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-12-poster.jpg" alt="Case 12 source video poster" height="360"></a>

[Play case 12 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-12.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-13"></a>
### Case 13: [統計稽核必須加入獨立審查](https://x.com/emollick/status/2077869293031624793) (by [@emollick](https://x.com/emollick))

**在採信模型產生的統計稽核發現前，先由獨立專家或其他模型複核**

Ethan Mollick 報告 Kimi K3 Max 在稽核既有學術工作時誤用統計方法，並認同另一份批評；這個反面案例支持獨立檢查，而不是未經審查便採信

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-13-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-13-01.jpg" alt="Case 13 source image 1" height="360"></a>

Type: Limit | Date: 2026-07-16

---

<a id="case-16"></a>
### Case 16: [評估速度慢但品質強的前端執行](https://x.com/Lentils80/status/2077387333154857151) (by [@Lentils80](https://x.com/Lentils80))

**測試前端任務時，同時記錄完成時間與輸出品質**

創作者表示一次 Kimi K3 前端執行耗時 35 分鐘，並稱其輸出是該 prompt 所見最佳成果之一；速度與品質判斷都只是單一使用者的觀察

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-16.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-16-poster.jpg" alt="Case 16 source video poster" height="360"></a>

[Play case 16 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-16.mp4)

Type: Evaluation | Date: 2026-07-15

---

<a id="case-20"></a>
### Case 20: [測試推理小說寫作中的伏筆缺陷](https://x.com/emollick/status/2077951790868238616) (by [@emollick](https://x.com/emollick))

**評估生成的推理故事能否平衡線索、隱晦度與伏筆**

Ethan Mollick 表示 Kimi K3 沒有寫出好的謀殺推理故事，線索同時過度明顯又過度隱晦，而且伏筆失敗；他也指出其他模型有同樣限制

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-01.jpg" alt="Case 20 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-02.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-02.png" alt="Case 20 source image 2" height="360"></a>

Type: Limit | Date: 2026-07-17

---

<a id="case-21"></a>
### Case 21: [比較千年鷹號的建模與動畫](https://x.com/gmi_cloud/status/2077903360263676090) (by [@gmi_cloud](https://x.com/gmi_cloud))

**用相同風格要求與 effort 設定，比較 3D 建模、動畫、時間與成本**

GMI Cloud 報告在 maximum effort 下比較 Kimi K3 與 Fable 5 重現像素風及原始風格的千年鷹號；其稱 Kimi K3 在第一次測試耗時較長但成本約為三分之一，另一次則不到一半，這些都是供應商報告的結果

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-21.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-21-poster.jpg" alt="Case 21 source video poster" height="360"></a>

[Play case 21 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-21.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-28"></a>
### Case 28: [檢視十個 Kimi K3 專案合集](https://x.com/minchoi/status/2077957907857994006) (by [@minchoi](https://x.com/minchoi))

**用有連結的專案合集發現具體成果，再分別驗證**

作者整理十個附媒體的 Kimi K3 範例，其中包含 Game Boy Advance 模擬器；此記錄是合集而非單一可重現流程，因此每個連結範例都應獨立檢查

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-28.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-28-poster.jpg" alt="Case 28 source video poster" height="360"></a>

[Play case 28 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-28.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-29"></a>
### Case 29: [比較四個模型生成進階登陸頁](https://x.com/doutorcaleb/status/2077904020471947773) (by [@doutorcaleb](https://x.com/doutorcaleb))

**固定登陸頁要求，檢視各模型輸出的動畫深度與完成度**

創作者表示向 Kimi K3、Fable、Grok 與 GPT Terra 提供相同的進階登陸頁 prompt，並判定 Kimi K3 成果最強；這是單一任務的自行報告比較

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-29.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-29-poster.jpg" alt="Case 29 source video poster" height="360"></a>

[Play case 29 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-29.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-30"></a>
### Case 30: [對復古遊戲機制與成本進行基準測試](https://x.com/adxtyahq/status/2077860500462055570) (by [@adxtyahq](https://x.com/adxtyahq))

**在相同復古遊戲任務上比較遊玩、物理、機制、自動行為、token 用量與成本**

來源報告使用相同 prompt 測試 Road Fighter、Battle City 與 Q*bert，並列出 $0.28 對應 Kimi K3、$0.28 對應 GPT-5.6、$0.54 對應 Opus 4.8；這些是發布者的基準數字

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-30.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-30-poster.jpg" alt="Case 30 source video poster" height="360"></a>

[Play case 30 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-30.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-31"></a>
### Case 31: [與 Fable 5 比較遊戲生成](https://x.com/higgsfield_ai/status/2077943629633712490) (by [@higgsfield_ai](https://x.com/higgsfield_ai))

**把並列生成遊戲範例視為狹義評估，而不是廣泛模型結論**

Higgsfield 展示 Kimi K3 與 Fable 5 的遊戲生成比較；指定記錄包含比較媒體，但沒有 prompt、評分標準或詳細條件

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-31.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-31-poster.jpg" alt="Case 31 source video poster" height="360"></a>

[Play case 31 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-31.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-34"></a>
### Case 34: [與 Opus 4.8 比較複雜前端及開發任務](https://x.com/op7418/status/2077969583018066116) (by [@op7418](https://x.com/op7418))

**用多個複雜程式任務辨識勝負，而不是宣稱單一模型全面更強**

評論者報告直接測試 Kimi K3 與 Opus 4.8，認為兩者在複雜前端與開發工作上大致相當，結果互有勝負；這仍是單一評論者的評估

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-34.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-34-poster.jpg" alt="Case 34 source video poster" height="360"></a>

[Play case 34 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-34.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-35"></a>
### Case 35: [檢視基準結果與登陸頁測試](https://x.com/adamuchigabriel/status/2077880433925120471) (by [@adamuchigabriel](https://x.com/adamuchigabriel))

**結合基準背景與具體登陸頁生成測試，同時把兩種證據分開**

影片介紹 Kimi K3 的基準討論、登陸頁測試與前端設計觀察；指定記錄沒有提供完整測試 prompt 或評分標準

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-35.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-35-poster.jpg" alt="Case 35 source video poster" height="360"></a>

[Play case 35 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-35.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-37"></a>
### Case 37: [用圖形到公式任務評估歸納推理](https://x.com/s_batzoglou/status/2077884096307454119) (by [@s_batzoglou](https://x.com/s_batzoglou))

**在一階邏輯歸納任務中衡量正確性、holdout 表現與公式複雜度**

作者表示在 ICML INDUCTION 任務上對 Kimi K3 與其他模型進行基準測試，使用 6 至 10 個小型圖，每個含 8 至 10 個元素，以推導一階公式；貼文稱結果已從先前工作更新，本案例庫不主張新的獨立重現

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-37-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-37-01.png" alt="Case 37 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-16

---

<a id="case-38"></a>
### Case 38: [檢視遊戲、登陸頁、3D 與長上下文的報告成果](https://x.com/servasyy_ai/status/2077903775113834689) (by [@servasyy_ai](https://x.com/servasyy_ai))

**透過多來源整理比較具體成果，並在成本主張旁記錄速度限制**

作者整理各方報告的 Kimi K3 測試，涵蓋遊戲、登陸頁、3D 生成與長上下文工作，並認為它值得嘗試但尚不能取代 Fable 5；所有數字都是此整理中的二手報告

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-38-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-38-01.jpg" alt="Case 38 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-40"></a>
### Case 40: [稽核複雜計畫並質疑其補救方案](https://x.com/doodlestein/status/2077901883637665958) (by [@doodlestein](https://x.com/doodlestein))

**用第二個模型找出被淡化的發現、錯誤補救方案與應駁回的結論**

創作者表示 Kimi K3 審查一份反覆精修的計畫後，發現嚴重問題被淡化、約三分之一的建議補救方案需要修正，且一項發現遭推翻；這些是該特定稽核的結果

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-40-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-40-01.jpg" alt="Case 40 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-41"></a>
### Case 41: [比較 PPO 風格強化學習 ASCII 圖](https://x.com/dejavucoder/status/2077872015856615541) (by [@dejavucoder](https://x.com/dejavucoder))

**固定 ASCII 圖 prompt，比較模型如何呈現強化學習迴圈**

來源提供繪製 PPO 風格強化學習迴圈的 ASCII prompt，並並列 Kimi K3 Max 與 Fable 5 High；判斷仍是單一任務的視覺比較

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-01.png" alt="Case 41 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-02.jpg" alt="Case 41 source image 2" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-42"></a>
### Case 42: [在 Blender 建模時追蹤容量錯誤](https://x.com/Angaisb_/status/2077910845523214668) (by [@Angaisb_](https://x.com/Angaisb_))

**將 Blender 的部分進度與服務可靠性一併評估，而不是只看成果**

創作者展示 Kimi K3 的 Blender 建模進度，也報告反覆發生容量錯誤；指定來源中的工作尚未完成，因此應同時考量部分成果與可靠性限制

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-42-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-42-01.jpg" alt="Case 42 source image 1" height="360"></a>

Type: Limit | Date: 2026-07-17

---

<a id="case-47"></a>
### Case 47: [在競技場比較 Flappy Bird 生成](https://x.com/jun_song/status/2077396996865003739) (by [@jun_song](https://x.com/jun_song))

**透過競技場任務比較兩個 Flappy Bird 生成結果，同時將判斷限定於該任務**

創作者報告 Kimi K3 與 Opus 4.8 在 Flappy Bird 任務上的 Arena 比較，並判定 Kimi K3 明顯更好；記錄未提供完整 prompt 或評分標準

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-47.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-47-poster.jpg" alt="Case 47 source video poster" height="360"></a>

[Play case 47 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-47.mp4)

Type: Evaluation | Date: 2026-07-15

---

<a id="case-52"></a>
### Case 52: [使用工具解答 Bongard 視覺歸納問題](https://x.com/IntuitMachine/status/2077885406528311561) (by [@IntuitMachine](https://x.com/IntuitMachine))

**測試工具使用是否有助於推導 Bongard 推理任務中的視覺規則**

創作者表示 Kimi K3 使用工具解出一題 Bongard 問題，而 Grok 4.5 與 Muse Spark 1.1 在相同比較中未能解出；這是單一使用者的任務結果，不是通用推理基準

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-52-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-52-01.jpg" alt="Case 52 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-53"></a>
### Case 53: [比較 3D 前端品味及設計，對手為 GPT-5.6 Sol](https://x.com/filicroval/status/2077736407506751952) (by [@filicroval](https://x.com/filicroval))

**在有邊界的前端比較中檢視功能、視覺品味、優雅度與 3D 執行**

創作者比較 Kimi K3 與 GPT-5.6 Sol 的前端設計，判定 Kimi K3 在視覺品味、優雅度與 3D 能力上較強；此評估具主觀性，且只適用於該任務

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-53.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-53-poster.jpg" alt="Case 53 source video poster" height="360"></a>

[Play case 53 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-53.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-57"></a>
### Case 57: [比較三個模型生成網站](https://x.com/pengchujin/status/2077962916226298340) (by [@pengchujin](https://x.com/pengchujin))

**用可見網站輸出比較 Kimi K3、Fable 5 與 GPT-5.6 Sol 在單次測試的表現**

創作者展示 Kimi K3、Fable 5 與 GPT-5.6 Sol 的網站生成比較；指定記錄未揭露完整 prompt 或評分標準

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-57.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-57-poster.jpg" alt="Case 57 source video poster" height="360"></a>

[Play case 57 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-57.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-59"></a>
### Case 59: [比較程序式 3D 遊戲生成與成本](https://x.com/adxtyahq/status/2077958193511362856) (by [@adxtyahq](https://x.com/adxtyahq))

**固定各模型的 prompt，檢視生成的輪盤、吃角子老虎與彈珠台系統及單次成本**

發布者報告多模型程序式 3D 遊戲比較，列出的成本包括 $0.71 對應 Kimi K3，以及 $0.30 對應 Grok 4.5；所有排名與成本都應視為該發布者的執行結果

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-59.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-59-poster.jpg" alt="Case 59 source video poster" height="360"></a>

[Play case 59 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-59.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-69"></a>
### Case 69: [比較 3D 軍火庫場景的細節與照明](https://x.com/hakki_alkan/status/2077887013332636032) (by [@hakki_alkan](https://x.com/hakki_alkan))

**在有邊界的 Kimi K3 與 Opus 4.8 比較中檢視物件密度、照明與場景細節**

來源表示 Kimi K3 產出細節豐富的軍火庫場景，包含擺滿物品的層架、箱子與真實照明，而 Opus 4.8 只產出稀疏房間；這是第三方比較報告，不是獨立基準

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-69-poster.jpg" alt="Case 69 source video poster" height="360"></a>

[Play case 69 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-69.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-72"></a>
### Case 72: [用相同 Arena prompt 比較前端](https://x.com/arena/status/2078240399517524365) (by [@arena](https://x.com/arena))

**固定 prompt 並並排檢查輸出，比只看一個排行榜分數更可靠**

Arena.ai 發布 Kimi K3 與 Fable 5 的 Frontend Code Arena 對比，雙方使用相同 prompt；影片保留兩側輸出，便於檢查實作與呈現差異

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-72.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-72-poster.jpg" alt="Case 72 source video poster" height="360"></a>

[Play case 72 comparison video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-72.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-74"></a>
### Case 74: [評測 Kimi Code 編碼 agent](https://x.com/ArtificialAnlys/status/2078230240766345330) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**結合多個編碼 agent 測試集與單任務成本評估 Kimi K3，不把單一前端榜單當成整體能力**

Artificial Analysis 報告 Kimi K3 在 Coding Agent Index 得分 57、並列第五；Terminal-Bench v2 為 84%，DeepSWE 為 64%，SWE-Atlas-QnA 為 23%，平均每任務成本 3.18 美元

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-74.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-74.jpg" alt="Case 74 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-17

---

<a id="case-76"></a>
### Case 76: [比較 Arena 與修復測試結果](https://x.com/AlphaSignalAI/status/2078172629496746183) (by [@AlphaSignalAI](https://x.com/AlphaSignalAI))

**同時看前端偏好與儲存庫修復評測，因為 Kimi K3 可在一個榜單第一、在另一測試中第七**

AlphaSignal 報告 Kimi K3 在 Frontend Code Arena 以 1679 分排名第一，但在編碼 agent 修復測試中只完成 67 次嘗試中的 53 次，即 79%，排名第七

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-76.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-76.jpg" alt="Case 76 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-17

---

<a id="case-80"></a>
### Case 80: [用 Prinzbench 評估 Kimi K3](https://x.com/deredleritt3r/status/2078606700496773166) (by [@deredleritt3r](https://x.com/deredleritt3r))

**用独立 benchmark 更新对比 Kimi K3 与開源、前沿模型在搜索、推理和一致性上的表现。**

作者把 Kimi K3 加入 Prinzbench，并報告總分 47/99，高於 GLM-5.2 的 30/99，接近舊版 Gemini 3.1 Pro 的 50/99。帖子强调它搜索能力强，但逻輯推理较弱，穩定性也不如可比前沿模型。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-80-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-80-01.png" alt="Case 80 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-18

---

<a id="case-85"></a>
### Case 85: [对比 ISS 数字孪生生成](https://x.com/AIsaOneHQ/status/2078519527588200536) (by [@AIsaOneHQ](https://x.com/AIsaOneHQ))

**用同 prompt 3D 挑战，对比 Kimi K3 与 GPT-5.6 Sol 在重建、控制、標签和视觉细节上的表现。**

AIsaOneHQ 報告一个 one-shot benchmark：两个模型都需要在没有预建模型的情况下重建可交互國際太空站數位孿生，包括地球、轨道光照、控制、標籤、導覽、爆炸視圖、測試和優化。帖子称 Kimi K3 在该轮更快、更便宜，渲染效果更强。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-85.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-85-poster.jpg" alt="Case 85 source video poster" height="360"></a>

[Play case 85 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-85.mp4)

Type: Benchmark | Date: 2026-07-18

---

<a id="case-89"></a>
### Case 89: [評测 WebGPU 森林世界](https://x.com/stas_sorokin_/status/2078435840728908093) (by [@stas_sorokin_](https://x.com/stas_sorokin_))

**在长周期 Three.js 与 WebGPU 世界构建中，把 Kimi K3 作为 coding agent brain，从质量、速度、一致性和人工修改率評估它。**

創作者用一个梦幻森林湖泊世界深度評測 Kimi K3，場景包含動態水体、天气、野生动物、晝夜变化和电影鏡頭。帖子称 Kimi K3 质量很高，比类似 GPT-5.6 Sol 生成更慢，但长周期一致性好，只手动調整了一次湖面亮度。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-89.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-89-poster.jpg" alt="Case 89 source video poster" height="360"></a>

[Play case 89 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-89.mp4)

Type: Evaluation | Date: 2026-07-18

---

<a id="case-90"></a>
### Case 90: [比較玻璃屋同題提示](https://x.com/RoundtableSpace/status/2079004612070416755) (by [@RoundtableSpace](https://x.com/RoundtableSpace))

**用同一個建築場景提示比較 Kimi K3 與 Opus 4.8 在氛圍、光照和空間完整度上的差異。**

Roundtable Space 報告 Kimi K3 與 Claude Opus 4.8 在接近價格下的同提示對比。Kimi 的結果被描述為藍調時刻的玻璃屋、溫暖室內光、反射水池和藍圖細節；Opus 的結果更偏字體設計，空間完成度較弱。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-90.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-90-poster.jpg" alt="Case 90 source video poster" height="360"></a>

[Play case 90 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-90.mp4)

Type: Evaluation | Date: 2026-07-20

---

<a id="case-92"></a>
### Case 92: [評測體素足球進球](https://x.com/0xzynex/status/2078920667542487230) (by [@0xzynex](https://x.com/0xzynex))

**把同一個純 HTML/CSS/JS 足球動畫提示交給兩個模型，比較動作品質和成本。**

0xzynex 報告了一次同提示、一次生成、無重試的比較：Kimi K3 與 GPT-5.6 Sol High 都要在瀏覽器程式碼中生成方塊風足球高光，包含盤帶、進球、動態鏡頭和慶祝。貼文稱 Kimi 動作更流暢且成本更低，影片保留了對比結果。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-92.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-92-poster.jpg" alt="Case 92 source video poster" height="360"></a>

[Play case 92 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-92.mp4)

Type: Benchmark | Date: 2026-07-19

---

<a id="case-93"></a>
### Case 93: [審看 Minecraft benchmark](https://x.com/ashen_one/status/2078892418976666071) (by [@ashen_one](https://x.com/ashen_one))

**在把發布 hype 或模型價格當作證據前，先看結構化 Minecraft 測評。**

ashen_one 發布了 Kimi K3 錄影測評，章節包括 hype 與現實、benchmark、定價、Minecraft 測試、首次執行 bug 和最終判斷。這個來源把測評框架和早期可靠性問題放進一個可審看的影片中。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-93.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-93-poster.jpg" alt="Case 93 source video poster" height="360"></a>

[Play case 93 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-93.mp4)

Type: Benchmark | Date: 2026-07-19

---

<a id="case-98"></a>
### Case 98: [衡量 API 檔位限制](https://x.com/mnmn94253156337/status/2078739859154620497) (by [@mnmn94253156337](https://x.com/mnmn94253156337))

**規劃 Kimi K3 agent run 時，要看 token、tier、TPM 和 TPD，不只看模型標價。**

中文來源記錄了一次個人 Kimi K3 API 試用：充值 5 美元後，setup 階段約消耗 1.1 美元，隨後觸發 Tier0 限制。它列出輸入、快取輸入、輸出價格，以及 TPM/TPD 等限額概念，因此適合作為早期限制案例而非普遍定價結論。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-98.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-98-poster.jpg" alt="Case 98 source video poster" height="360"></a>

[Play case 98 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-98.mp4)

Type: Limit | Date: 2026-07-19

---

<a id="case-99"></a>
### Case 99: [比較 Limbo 風格 demo](https://x.com/ChrisGPT/status/2078679211116835017) (by [@ChrisGPT](https://x.com/ChrisGPT))

**在同一個遊戲原型上比較 Kimi K3 與 Fable 5 的可玩範圍、視覺打磨、成本和 bug。**

ChrisGPT 比較了 Fable 5 與 Kimi K3 的 Limbo clone demo。貼文稱 Fable 輸出 2,400 行程式碼、24K output tokens，成本 1.20 美元；Kimi 輸出 3,000 行和 30K tokens，成本 0.12 美元，Kimi 增加了更多 gameplay，但 bug 也更多。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-99.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-99-poster.jpg" alt="Case 99 source video poster" height="360"></a>

[Play case 99 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-99.mp4)

Type: Benchmark | Date: 2026-07-19

---

<a id="case-100"></a>
### Case 100: [審查 VulcanBench 成本結果](https://x.com/morganlinton/status/2079358902194569357) (by [@morganlinton](https://x.com/morganlinton))

**用这个案例评估 Kimi K3 在「審查 VulcanBench 成本結果」任务中的实际工作流、成本或限制。**

来源帖提供了与 審查 VulcanBench 成本結果 相关的公开证据，包括作者描述、结果媒体或基准/教程信息；本仓库只保留可核验事实，不补写未公开的 prompt 或步骤。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-100-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-100-01.jpg" alt="Case 100 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-21

---

<a id="case-104"></a>
### Case 104: [評測雙擺物理模擬](https://x.com/AlicanKiraz0/status/2079241239736504768) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**用这个案例评估 Kimi K3 在「評測雙擺物理模擬」任务中的实际工作流、成本或限制。**

来源帖提供了与 評測雙擺物理模擬 相关的公开证据，包括作者描述、结果媒体或基准/教程信息；本仓库只保留可核验事实，不补写未公开的 prompt 或步骤。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-104.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-104-poster.jpg" alt="Case 104 source video poster" height="360"></a>

[Play case 104 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-104.mp4)

Type: Benchmark | Date: 2026-07-20

---

<a id="case-107"></a>
### Case 107: [檢視 ReactBench 生產就緒度](https://x.com/aidenybai/status/2079233934693650567) (by [@aidenybai](https://x.com/aidenybai))

**用这个案例评估 Kimi K3 在「檢視 ReactBench 生產就緒度」任务中的实际工作流、成本或限制。**

来源帖提供了与 檢視 ReactBench 生產就緒度 相关的公开证据，包括作者描述、结果媒体或基准/教程信息；本仓库只保留可核验事实，不补写未公开的 prompt 或步骤。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-107.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-107-poster.jpg" alt="Case 107 source video poster" height="360"></a>

[Play case 107 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-107.mp4)

Type: Benchmark | Date: 2026-07-20

---

<a id="case-110"></a>
### Case 110: [用 AA-Briefcase 評估 Kimi K3](https://x.com/ArtificialAnlys/status/2079715807983210572) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**先用 AA-Briefcase 結果判斷 Kimi K3 的知識工作 agent 任務表現，再相信排行榜敘事。**

Artificial Analysis 報告稱，Kimi K3 在 AA-Briefcase 上得到 1543 Elo，位列 Claude Fable 5 之後第二；同時該模型在這個基準中平均每個任務接近一小時，成本高於 Opus 4.8。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-110-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-110-01.jpg" alt="Case 110 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-21

---

<a id="case-113"></a>
### Case 113: [審計前端榜單限制](https://x.com/RetroChainer/status/2079622227796885850) (by [@RetroChainer](https://x.com/RetroChainer))

**用這條限制說明區分 Kimi K3 的榜單勝利和更寬泛的 coding、成本主張。**

RetroChainer 核實了 Frontend Code Arena 第一和公開價格，同時指出：該排名只適用單一榜單；發文時權重尚未公開；每任務節省來自單一任務；max reasoning 可能在小任務上消耗大量 tokens。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-113.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-113-poster.jpg" alt="Case 113 source video poster" height="360"></a>

[Play case 113 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-113.mp4)

Type: Limit | Date: 2026-07-21

---

<a id="case-114"></a>
### Case 114: [對比 StackPerf 架構結果](https://x.com/tamsi_besson/status/2079573266855834071) (by [@tamsi_besson](https://x.com/tamsi_besson))

**用 StackPerf 對比 Kimi K3 和 Qwen 3.8 的架構品質、速度和 tool call 行為。**

Tamsi Besson 分享的 StackPerf 快照顯示，Kimi K3 在品質上略高於 Qwen 3.8 Max Preview，總體速度更快；但 Qwen 的失敗 tool call 為 0，而 Kimi 雖呼叫更多工具卻有 2 次失敗。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-114-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-114-01.jpg" alt="Case 114 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-21

---

<a id="case-118"></a>
### Case 118: [對比 Monument Valley prompt 成本](https://x.com/AiHubMix/status/2079507420083294557) (by [@AiHubMix](https://x.com/AiHubMix))

**用單個 Monument Valley 風格 prompt 對比 Kimi K3 與其他模型的視覺品質、執行時間和成本。**

AiHubMix 用一個 Monument Valley 風格 prompt 對比 Claude Fable 5、Kimi K3 和 GPT-5.6 Sol。貼文稱 Fable 最連貫，Kimi 最慢為 52m30s 且花費 $1.50，GPT-5.6 Sol 最快最便宜但空間邏輯較弱。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-118.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-118-poster.jpg" alt="Case 118 source video poster" height="360"></a>

[Play case 118 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-118.mp4)

Type: Benchmark | Date: 2026-07-21

---

<a id="case-120"></a>
### Case 120: [用 Surge 指数評估 Kimi K3](https://x.com/echen/status/2080021575190110523) (by [@echen](https://x.com/echen))

**用 SurgeAI 的分项结果区分 Kimi K3 在日常聊天中的优势，以及在企业 agent 和科学任務中的弱项。**

Eric Chen 報告 SurgeAI 在覆盖日常聊天机器人、企业 agent、深度推理和前沿科学的指数中測試了 Kimi K3。來源称 Kimi K3 在日常聊天上有竞争力，但在企业 agent 和科学任務上落后于 Fable 与 Sol。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-120-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-120-01.jpg" alt="Case 120 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-22

---

<a id="case-123"></a>
### Case 123: [評估 PDE 求解错误](https://x.com/lanyon_ai/status/2079931884511887740) (by [@lanyon_ai](https://x.com/lanyon_ai))

**用 PDE benchmark 失败案例判断 Kimi K3 在符号或数值任務中哪些环节需要额外驗證。**

Lanyon AI 将其神经符号架构与包括 Kimi K3 在内的前沿模型，在简单线性 PDE 上进行比较。來源称，即使给出详细 prompt，前沿模型仍出现数学、算法和计算錯誤。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-123-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-123-01.jpg" alt="Case 123 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-22

---

<a id="case-124"></a>
### Case 124: [复查 ClinicalBench EHR 案例](https://x.com/mkurman88/status/2079918374977413534) (by [@mkurman88](https://x.com/mkurman88))

**用 ClinicalBench 的 EHR 案例检查 Kimi K3 哪些地方成功，哪些诊断推理仍会失败。**

Michael Kurman 報告 Kimi K3 在虚拟 EHR 沙盒中 10 个急诊案例的 ClinicalBench v0.0.4 結果。來源称 Kimi K3 解出 7/10，在第 6 个案例上耗时且未准确诊断。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-124-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-124-01.jpg" alt="Case 124 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-124-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-124-02.jpg" alt="Case 124 source image 2" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-124-03.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-124-03.jpg" alt="Case 124 source image 3" height="360"></a>

Type: Benchmark | Date: 2026-07-22

---

<a id="case-126"></a>
### Case 126: [評估报税计算能力](https://x.com/michaelrbock/status/2079913117698666964) (by [@michaelrbock](https://x.com/michaelrbock))

**不要假设前端强项会迁移到税务计算；应单独測試 Kimi K3 的该类负载。**

Michael Bock 報告用 50 份高度真实的联邦和州税表測試 Kimi K3。來源称 Kimi K3 在严格 TaxCalcBench 中得分 6%，GPT-5.6 Sol 为 58%，Fable 5 为 4%。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-126-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-126-01.jpg" alt="Case 126 source image 1" height="360"></a>

Type: Limit | Date: 2026-07-22

---

<a id="related-resources"></a>
## 相關資源

- [查看 EvoLink 上的 Kimi K3 詳情與價格](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=landing_overview)
- [查看 EvoLink Kimi K3 API 文件](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=docs_link)
- [進一步了解 EvoLink 上的 Kimi K3](https://evolink.ai/blog/is-kimi-k3-available-on-evolink?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_article)
- [KimiK3.io](https://kimik3.io/zh)
- EvoLink 模型頁與 API 文件已驗證，但尚未驗證可安裝的 Kimi K3 skill

<a id="acknowledge"></a>
## 🙏 致謝

感謝所有公開分享 Kimi K3 作品的創作者與實務工作者

[@ivanfioravanti](https://x.com/ivanfioravanti), [@TheAhmadOsman](https://x.com/TheAhmadOsman), [@HarshithLucky3](https://x.com/HarshithLucky3), [@chetaslua](https://x.com/chetaslua), [@abhinavflac](https://x.com/abhinavflac), [@bridgemindai](https://x.com/bridgemindai), [@Whats_AI](https://x.com/Whats_AI), [@chongdashu](https://x.com/chongdashu), [@MrAhmadAwais](https://x.com/MrAhmadAwais), [@bijanbowen](https://x.com/bijanbowen), [@CommandCodeAI](https://x.com/CommandCodeAI), [@emollick](https://x.com/emollick), [@nicky_sap](https://x.com/nicky_sap), [@Lentils80](https://x.com/Lentils80), [@scottstts](https://x.com/scottstts), [@aisearchio](https://x.com/aisearchio), [@gmi_cloud](https://x.com/gmi_cloud), [@karminski3](https://x.com/karminski3), [@VORTEX_Promos](https://x.com/VORTEX_Promos), [@rohanpaul_ai](https://x.com/rohanpaul_ai), [@mirochill](https://x.com/mirochill), [@aimlapi](https://x.com/aimlapi), [@minchoi](https://x.com/minchoi), [@doutorcaleb](https://x.com/doutorcaleb), [@adxtyahq](https://x.com/adxtyahq), [@higgsfield_ai](https://x.com/higgsfield_ai), [@AlicanKiraz0](https://x.com/AlicanKiraz0), [@1littlecoder](https://x.com/1littlecoder), [@op7418](https://x.com/op7418), [@adamuchigabriel](https://x.com/adamuchigabriel), [@s_batzoglou](https://x.com/s_batzoglou), [@servasyy_ai](https://x.com/servasyy_ai), [@filicroval](https://x.com/filicroval), [@doodlestein](https://x.com/doodlestein), [@dejavucoder](https://x.com/dejavucoder), [@Angaisb_](https://x.com/Angaisb_), [@AngryTomtweets](https://x.com/AngryTomtweets), [@Alezander907](https://x.com/Alezander907), [@teortaxesTex](https://x.com/teortaxesTex), [@jun_song](https://x.com/jun_song), [@ridark_eth](https://x.com/ridark_eth), [@naymur_dev](https://x.com/naymur_dev), [@tphuang](https://x.com/tphuang), [@TokenGremlin](https://x.com/TokenGremlin), [@IntuitMachine](https://x.com/IntuitMachine), [@wangfeng0315](https://x.com/wangfeng0315), [@twid](https://x.com/twid), [@pengchujin](https://x.com/pengchujin), [@aayushman2703](https://x.com/aayushman2703), [@goncalo_canhoto](https://x.com/goncalo_canhoto), [@LinearUncle](https://x.com/LinearUncle), [@gagarot200](https://x.com/gagarot200), [@MinLiBuilds](https://x.com/MinLiBuilds), [@izutorishima](https://x.com/izutorishima), [@X2worldtech](https://x.com/X2worldtech), [@Satvik_Pen](https://x.com/Satvik_Pen), [@hakki_alkan](https://x.com/hakki_alkan), [@BrianMRey](https://x.com/BrianMRey), [@ChrisGPT](https://x.com/ChrisGPT), [@arena](https://x.com/arena), [@MathiasHeide](https://x.com/MathiasHeide), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@nauczymycieAI](https://x.com/nauczymycieAI), [@AlphaSignalAI](https://x.com/AlphaSignalAI), [@Ananth7e](https://x.com/Ananth7e), [@viktoroddy](https://x.com/viktoroddy), [@abacusai](https://x.com/abacusai), [@deredleritt3r](https://x.com/deredleritt3r), [@fabriciocarraro](https://x.com/fabriciocarraro), [@startracker](https://x.com/startracker), [@mattwatkajtys](https://x.com/mattwatkajtys), [@AIsaOneHQ](https://x.com/AIsaOneHQ), [@MiaAI_lab](https://x.com/MiaAI_lab), [@hqmank](https://x.com/hqmank), [@prasenx](https://x.com/prasenx), [@stas_sorokin_](https://x.com/stas_sorokin_), [@RoundtableSpace](https://x.com/RoundtableSpace), [@karankendre](https://x.com/karankendre), [@0xzynex](https://x.com/0xzynex), [@ashen_one](https://x.com/ashen_one), [@MAXdeg0](https://x.com/MAXdeg0), [@ice_bearcute](https://x.com/ice_bearcute), [@mnmn94253156337](https://x.com/mnmn94253156337), [@morganlinton](https://x.com/morganlinton), [@vikktorrrre](https://x.com/vikktorrrre), [@kirillk_web3](https://x.com/kirillk_web3), [@_guillecasaus](https://x.com/_guillecasaus), [@demian_ai](https://x.com/demian_ai), [@aidenybai](https://x.com/aidenybai), [@LexnLin](https://x.com/LexnLin), [@boxmining](https://x.com/boxmining), [@Nekt_0](https://x.com/Nekt_0), [@RetroChainer](https://x.com/RetroChainer), [@tamsi_besson](https://x.com/tamsi_besson), [@thehypedotnews](https://x.com/thehypedotnews), [@AiHubMix](https://x.com/AiHubMix), [@sairahul1](https://x.com/sairahul1), [@echen](https://x.com/echen), [@Oluwaphilemon1](https://x.com/Oluwaphilemon1), [@diegocabezas01](https://x.com/diegocabezas01), [@lanyon_ai](https://x.com/lanyon_ai), [@mkurman88](https://x.com/mkurman88), [@ShenSeanChen](https://x.com/ShenSeanChen), [@michaelrbock](https://x.com/michaelrbock), [@Kirratr](https://x.com/Kirratr), [@jadeferrara_](https://x.com/jadeferrara_), [@biscuitweb3](https://x.com/biscuitweb3)

*若需更正歸屬或文字，請附上公開來源建立 issue*
