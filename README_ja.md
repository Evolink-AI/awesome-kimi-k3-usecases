<div align="center">

<a href="https://evolink.ai/kimi-k3?utm_source=github&utm_medium=banner&utm_campaign=awesome-kimi-k3-usecases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/images/ja-v2.png" alt="月面風景とEvoLinkの案内を含む日本語版Kimi K3バナー" width="760"></a>

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

# Kimi K3 活用事例集

## 🍌 はじめに

Kimi K3 の実例を厳選したリポジトリです

**公開情報に基づくゲーム、3D、モーションデザイン、統合、評価、実用上の制約を収録します**

89件はいずれも信頼度の高い公開ソースに基づきます。タイトルと著者名から原典へ移動でき、弱い候補、重複、証拠不足の候補は除外しています

## 📊 概要

- クリエイターと実務家によるhigh-confidenceの89事例
- ゲーム、Three.js、モーション、フロントエンド、コーディング、研究、評価、実用上の制約を幅広く収録
- 各事例で出典、著者、種別、日付、プロンプト境界を保持
- 個人の報告をベンチマークとして扱いません

> [!NOTE]
> 具体的な証拠を優先し、未公開のプロンプトや手順を補完しません

<a id="quick-api-access"></a>
## ⚡ クイックスタート

EvoLinkの文書化されたモデルIDは `kimi-k3` で、モデルページとChat Completions API文書が利用できます

1. [EvoLinkでKimi K3の詳細と料金を見る](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=landing_overview)
2. [EvoLink APIキーを作成・管理](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-kimi-k3-usecases&utm_content=api_key)

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

[EvoLinkのKimi K3 API文書を開く](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=first_run)

> [!IMPORTANT]
> EvoLinkのモデルページとAPI文書が公開ルートとIDを確認しています。独立したKimi K3のブラウザ／ノーコード画面は確認できておらず、本リポジトリは独自の有料APIテストも主張しません

## 📑 目次

| Section | Cases |
|---|---|
| [インタラクティブゲームと3D](#games-3d) | 33 |
| [フロントエンドとモーションデザイン](#frontend-motion) | 24 |
| [コーディングと統合](#coding-integrations) | 13 |
| [評価と制約](#evaluation-limits) | 39 |
| [関連リソース](#related-resources) | 関連リソース |
| [クイックスタート](#quick-api-access) | クイックスタート |
| [謝辞](#acknowledge) | 謝辞と訂正 |

| Case | Category | What it shows | Type |
|---|---|---|---|
| [1つのプロンプトでボクセルレースを作る](#case-1) | インタラクティブゲームと3D | 短いアイデアからレースを試作し、次の改善範囲を決めます | Demo |
| [同じプロンプトでFroggerを比較する](#case-2) | インタラクティブゲームと3D | プロンプトを固定してモデル間の差を確認します | Evaluation |
| [Froggerと録画を生成する](#case-3) | インタラクティブゲームと3D | ゲームとプレイ録画の両方をワンショットで試します | Demo |
| [Three.jsで空母を試作する](#case-4) | インタラクティブゲームと3D | 具体的な発着艦シーンで対話型3D生成を試します | Demo |
| [対話できるモーショングラフィックを作る](#case-5) | フロントエンドとモーションデザイン | 停止中も操作できるグラフィックをワンショットで構築します | Demo |
| [同期したモーション広告を作る](#case-6) | フロントエンドとモーションデザイン | 音楽、効果、動きの同期を確認します | Demo |
| [BridgeBenchの溶岩ランプ課題でフロントエンドデザインを比較する](#case-7) | 評価と制約 | BridgeBenchの溶岩ランプ課題を、普遍的な順位ではなく範囲を限定した比較として使います | Benchmark |
| [編集方針に沿う台本執筆をベンチマークする](#case-8) | 評価と制約 | 明示した社内ベンチマーク内で、編集トーンへの適合度、相対順位、台本1本当たりの費用を測定します | Benchmark |
| [エージェントツールでPaper Mario風ゲームを作る](#case-9) | インタラクティブゲームと3D | Kimi K3をエージェントharnessやアセットツールと組み合わせ、2Dと3Dのゲーム要素を生成します | Demo |
| [Flappy系ゲームのデザイン、費用、難易度を比較する](#case-10) | 評価と制約 | 生成ゲームの比較では難易度設定、費用、デザイン、ゲームプレイ機能を記録します | Benchmark |
| [地下鉄を舞台にした一人称シューティングを生成する](#case-11) | インタラクティブゲームと3D | 具体的な地下鉄という舞台を使い、生成されたFPSの結果を確認します | Demo |
| [同じデザインプロンプトでゲーム設計を比較する](#case-12) | 評価と制約 | デザインプロンプトを固定し、進行速度、デザイン感覚、プレイ感を分けて確認します | Benchmark |
| [統計監査には独立したレビューを必須にする](#case-13) | 評価と制約 | モデルが生成した統計監査は、知見を採用する前に独立した専門家または別モデルのレビューと組み合わせます | Limit |
| [モーションデザインをすべてコードで制作する](#case-14) | フロントエンドとモーションデザイン | 補助的な生成ツールなしのワンショット・コーディングでモーションデザインを作れるか試します | Demo |
| [人物を調査してアニメーション付き個人サイトを作る](#case-15) | フロントエンドとモーションデザイン | 広い個人サイト要件を与え、モデルの調査、計画、反復、ブラウザ検証を確認します | Tutorial |
| [遅いが高品質なフロントエンド実行を評価する](#case-16) | 評価と制約 | フロントエンド課題では出力品質とともに完了時間を記録します | Evaluation |
| [ブラックホール・シミュレーションを生成する](#case-17) | フロントエンドとモーションデザイン | 科学可視化課題を使い、生成されたブラックホール・シミュレーションを確認します | Demo |
| [動作するmacOSを備えた仮想MacBookを作る](#case-18) | コーディングと統合 | Three.jsのハードウェア描画とブラウザ上で操作できるOSシミュレーションを組み合わせます | Demo |
| [Blender MCPでV8エンジンをモデリングする](#case-19) | インタラクティブゲームと3D | Blender MCPと1回の依頼を使って精密な機械3Dモデルを生成します | Integration |
| [殺人ミステリー執筆で伏線の失敗を検証する](#case-20) | 評価と制約 | 生成ミステリーが手がかり、難解さ、伏線のバランスを取れているか評価します | Limit |
| [ミレニアム・ファルコンのモデリングとアニメーションを比較する](#case-21) | 評価と制約 | 同じスタイル要件とeffort設定で、3Dモデリング、アニメーション、時間、費用を比較します | Benchmark |
| [複雑なフロントエンドのモデリング、粒子、シェーダーを試す](#case-22) | フロントエンドとモーションデザイン | 公開プロンプトを使い、1回の実行でモデリング精度、粒子効果、インラインシェーダー生成を確認します | Demo |
| [1つの参照からプレイ可能なバトルアリーナを作る](#case-23) | インタラクティブゲームと3D | 単一の参照を使い、完全にプレイ可能なアリーナのワンショット生成を試します | Demo |
| [自動プレイするレトロゲーム3本をHTMLファイルで作る](#case-24) | インタラクティブゲームと3D | 単体HTMLゲーム内にグラフィック、敵、ルール、自動プレイを実装させます | Benchmark |
| [DSLからPTXまでのGPUコンパイラを作る](#case-25) | コーディングと統合 | DSL、コンパイラパス、PTX生成、Tensor Core経路を含むエンドツーエンド課題を使います | Demo |
| [手続き型音楽ツールを1回で生成する](#case-26) | フロントエンドとモーションデザイン | 対話型の手続き型音楽生成器をワンショットで作り、可視結果は慎重に比較します | Demo |
| [ワンショットでカメレオンのかくれんぼゲームを作る](#case-27) | インタラクティブゲームと3D | 色合わせ、手続き生成エリア、音声、複数ラウンド得点を備えた単一ファイルゲームを生成します | Benchmark |
| [Kimi K3プロジェクト10件のコレクションをレビューする](#case-28) | 評価と制約 | リンク付きまとめから具体的な成果物を見つけ、個別に検証します | Evaluation |
| [高度なランディングページを4モデルで比較する](#case-29) | 評価と制約 | 要件を固定し、モデル出力間でアニメーションの深さと完成度を確認します | Evaluation |
| [レトロゲームの仕組みと費用をベンチマークする](#case-30) | 評価と制約 | 同じ課題でプレイ、物理、仕組み、自律動作、トークン使用量、費用を比較します | Benchmark |
| [Fable 5とゲーム生成を比較する](#case-31) | 評価と制約 | 生成ゲームの並列例を、モデル全般の結論ではなく狭い範囲の評価として使います | Evaluation |
| [WebGL2でリアルタイム・ブラックホール光線追跡を作る](#case-32) | コーディングと統合 | 単一HTML内でネイティブWebGL2の測地線光線追跡を1プロンプトで生成できるか試します | Benchmark |
| [2枚の画像からThree.js製品ページを作る](#case-33) | フロントエンドとモーションデザイン | 2枚の参照画像と明示的なThree.js要件で製品プレゼンテーションを生成します | Demo |
| [複雑なフロントエンドと開発課題をOpus 4.8と比較する](#case-34) | 評価と制約 | 複数の複雑な課題で勝敗を確認し、一方を普遍的に優れているとは断定しません | Evaluation |
| [ベンチマークとランディングページテストをレビューする](#case-35) | 評価と制約 | ベンチマーク文脈と具体的テストを組み合わせつつ、2種類の証拠を分けて扱います | Evaluation |
| [エージェント・ツールチェーンでPaper Mario風2.5Dゲームを作る](#case-36) | インタラクティブゲームと3D | Kimi K3をGrok BuildまたはClaude Code、Spriterrificと組み合わせます | Tutorial |
| [グラフから論理式を導く課題で帰納推論を評価する](#case-37) | 評価と制約 | 一階論理の帰納課題で正答率、ホールドアウト挙動、論理式の複雑さを測定します | Benchmark |
| [報告されたゲーム、ランディングページ、3D、長文脈をレビューする](#case-38) | 評価と制約 | 複数ソースのまとめで成果物を比較し、費用主張と速度制約を記録します | Evaluation |
| [高級パン切り器と製品ページを発案する](#case-39) | フロントエンドとモーションデザイン | 製品発案、分解図、実演、ランディングページを1つの成果物にまとめます | Demo |
| [複雑な計画を監査して改善策に異議を唱える](#case-40) | 評価と制約 | 第2のモデルで過小評価された指摘、誤った改善策、退けるべき結論を特定します | Evaluation |
| [PPO型強化学習のASCII図を比較する](#case-41) | 評価と制約 | ASCII図のプロンプトを固定し、各モデルが強化学習ループをどう表現するか比較します | Evaluation |
| [容量エラーを記録しながらBlenderでモデリングする](#case-42) | 評価と制約 | 成果物だけでなくBlenderの部分的進捗とサービス信頼性を合わせて評価します | Limit |
| [ブラウザで動く3D武侠RPGを作る](#case-43) | インタラクティブゲームと3D | 近接戦闘、クエスト、インベントリ、天候、屋内探索、Blender環境制作、アセット調整を組み合わせます | Demo |
| [ブラウザで動くMinecraft風マルチプレイゲームを作る](#case-44) | インタラクティブゲームと3D | 時間と費用を限定した実行でオンラインマルチプレイのブラウザゲームを生成します | Demo |
| [10秒の再帰的ペリカンGIFを生成する](#case-45) | フロントエンドとモーションデザイン | 完全指定したループアニメーション要件で物語的連続性と再帰構造を確認します | Demo |
| [mGBA WASMを使ってGame Boy Advanceエミュレーターを作る](#case-46) | コーディングと統合 | ライセンス済み3Dモデルと実在のエミュレーターコアを統合し、UIとプレイ体験を再帰的に改善します | Integration |
| [ArenaでFlappy Bird生成を比較する](#case-47) | 評価と制約 | Arena課題で2つの生成結果を比較し、判断をその課題だけに限定します | Evaluation |
| [画面分割の協力型ブラウザゲームを再現する](#case-48) | インタラクティブゲームと3D | 1回の依頼で画面分割協力プレイとリアルタイム環境操作を生成します | Demo |
| [Command Codeのdesignモードでプレイ可能なゲームを生成する](#case-49) | インタラクティブゲームと3D | designコマンドをワンショット制作に使い、プレイ可能か記録します | Demo |
| [中国語ソースから複数テーマを調査する](#case-50) | コーディングと統合 | 長時間の調査課題でモデル世代間の網羅性と待ち時間を比較します | Evaluation |
| [一体感のある武侠ブラウザRPGを構築する](#case-51) | インタラクティブゲームと3D | 移動、戦闘、クエスト、インベントリ、天候、探索、3D環境制作を1つに統合します | Demo |
| [ツールを使ってBongard視覚帰納問題を解く](#case-52) | 評価と制約 | ツール利用がBongard推論課題の視覚規則導出に役立つか試します | Evaluation |
| [フロントエンドの美的感覚と3DデザインをGPT-5.6 Solと比較する](#case-53) | 評価と制約 | 限定的な比較で機能、視覚的な好み、洗練度、3D表現を確認します | Evaluation |
| [プレイ可能なHollow Knightクロスオーバーを作る](#case-54) | インタラクティブゲームと3D | 既存ゲームのアセットでKnightとKimiが戦うゲームを制作します | Demo |
| [BMW M4 CSの側面SVGを生成する](#case-55) | フロントエンドとモーションデザイン | 特定の車種と視点を指定し、ベクターイラスト出力を確認します | Demo |
| [動作するアプリ付きmacOSをブラウザに再現する](#case-56) | コーディングと統合 | 音楽、ブラウザ、メールの各アプリを含むブラウザOSシミュレーションを作ります | Demo |
| [3モデルのウェブサイト生成を比較する](#case-57) | 評価と制約 | 可視化された出力を使い、1テストでKimi K3、Fable 5、GPT-5.6 Solを比較します | Evaluation |
| [スクリーンショットのフィードバックでGargantuaを再現する](#case-58) | フロントエンドとモーションデザイン | 繰り返すスクリーンショットを観測情報に使い、科学可視化を診断・改善します | Tutorial |
| [手続き型3Dゲーム生成と費用を比較する](#case-59) | 評価と制約 | プロンプトを固定し、ルーレット、スロット、ピンボールと各実行費用を確認します | Benchmark |
| [Fall Guys風3Dブラウザゲームをワンショットで作る](#case-60) | インタラクティブゲームと3D | 1回の依頼でプレイ可能な3D障害物ゲームを生成し、プロジェクトを確認可能にします | Demo |
| [終末後のLisbon FPSを作って自己テストする](#case-61) | インタラクティブゲームと3D | 最大effortの1プロンプト実行で、提供までテスト、撮影、反復させます | Demo |
| [動作するFaceTime付きmacOSシミュレーションを作る](#case-62) | コーディングと統合 | 仮想OS課題で生成されたアプリ操作が機能するか試します | Demo |
| [簡単な依頼からAnimal Crossing風ゲームを生成する](#case-63) | インタラクティブゲームと3D | 最小限の要件からプレイ可能性、ゲームループ、パララックス効果を確認します | Demo |
| [2つのタスクを並べるフロントエンド効果比較機能を追加する](#case-64) | コーディングと統合 | 完了済みタスクを2つ選び、横並び表示し、ビューと操作を同期するツールを作ります | Tutorial |
| [1文の要件からMario風ゲームを生成する](#case-65) | インタラクティブゲームと3D | 最小限のワンショット依頼でプレイ可能性、ステージ設計、ピクセルアート、パララックスを確認します | Demo |
| [62枚のスクリーンショットでブラックホール可視化を改善する](#case-66) | フロントエンドとモーションデザイン | スクリーンショットのフィードバックループで、多数の反復を通じてシミュレーションを診断・修正します | Tutorial |
| [動作するゾンビFPSを作る](#case-67) | インタラクティブゲームと3D | 具体的なゾンビシューティング目標で、完全にプレイ可能なFPSを確認します | Demo |
| [ポストトレーニング製品のマーケティングPDFを作る](#case-68) | フロントエンドとモーションデザイン | 製品名と納品形式を指定してマーケティング文書を生成します | Demo |
| [3D兵器庫シーンの密度と照明を比較する](#case-69) | 評価と制約 | 限定的なKimi K3とOpus 4.8の比較で、物体密度、照明、シーン詳細を確認します | Evaluation |
| [1つのプロンプトからユーザーインターフェースを作る](#case-70) | フロントエンドとモーションデザイン | 1回の依頼で完全なUIデザインを生成し、結果を確認します | Demo |
| [インディー宇宙船ゲームを作る](#case-71) | インタラクティブゲームと3D | Kimi K3 Standardで初版を作り、一貫性、不具合、視覚品質、トークン費用を比較します | Demo |
| [同一Arenaプロンプトでフロントエンドを比較](#case-72) | 評価と制約 | 同じプロンプトと並列出力で比較し、単一のランキング値への依存を避けます | Benchmark |
| [Summer Engineゲームを自己テスト](#case-73) | インタラクティブゲームと3D | Kimi K3にゲームを実行させ、スクリーンショットとログを確認し、同じセッションで欠陥を修正させます | Demo |
| [Kimi Codeをコーディングエージェントで評価](#case-74) | 評価と制約 | 複数のテスト群とタスク単価でKimi K3を評価し、フロントエンド順位だけを総合能力と見なしません | Benchmark |
| [KimiをCodexサブエージェントに設定](#case-75) | コーディングと統合 | Codexが統括を担い、フロントエンド実行をKimi K3 OpenCodeサブエージェントに委任し、秘密情報の境界を明確にします | Tutorial |
| [Arenaと修復ハーネスの結果を比較](#case-76) | 評価と制約 | Kimi K3が一方で1位、別の評価で7位になり得るため、フロントエンド選好とリポジトリ修復の両方を見ます | Benchmark |
| [ブラウザ版バトルロイヤルを反復改善](#case-77) | インタラクティブゲームと3D | 機能の多いブラウザゲームでは、長い自律反復と的を絞った追加プロンプトを見込みます | Demo |
| [受賞級スタイルのWebサイトを作る](#case-78) | フロントエンドとモーションデザイン | 最終画像だけでなく、完全な録画セッションでKimi K3のWeb制作工程を評価します | Tutorial |
| [ChatLLMで簡単なコーディングをルーティング](#case-79) | コーディングと統合 | 簡単なコーディングをKimi K3に送り、難しいコーディングとデザインを別モデルに割り当てます | Integration |
| [PrinzbenchでKimi K3をベンチマークする](#case-80) | 評価と制約 | PrinzbenchでKimi K3をOpenAI o3などと比較し、同じ評価ベンチでの順位と限界を示す。 | Benchmark |
| [メタボールのスクロール連動フロントエンドを作る](#case-81) | フロントエンドとモーションデザイン | Kimi K3が、発光するメタボールとスクロール連動アニメーションを含む洗練されたWeb UIを組み立てた。 | Demo |
| [個人サイトを複数モデルで再設計して比較する](#case-82) | フロントエンドとモーションデザイン | 同じ個人サイト再設計タスクでKimi K3を他モデルと並べ、ビジュアル品質と構成の違いを比較している。 | Evaluation |
| [宇宙ゲームの景観を拡張する](#case-83) | インタラクティブゲームと3D | Kimi K3で一枚の宇宙ゲーム風景を、地形・宇宙船・ライティングを含む広いビジュアルへ展開した。 | Demo |
| [Three.js物理レンダラーの詰まりを解消する](#case-84) | インタラクティブゲームと3D | Kimi K3を実装支援に使い、Three.jsの物理レンダリング問題を前進させた事例。 | Demo |
| [ISSデジタルツイン生成を比較する](#case-85) | 評価と制約 | ISSデジタルツイン生成タスクでKimi K3と他モデルを比較し、複雑な3D/科学ビジュアルでの出力差を示す。 | Benchmark |
| [インタラクティブな頭皮エクスプローラーを作る](#case-86) | フロントエンドとモーションデザイン | Kimi K3が教育用途の人体頭皮ビジュアライザーを生成し、視覚化UIの使い道を示した。 | Demo |
| [3D地球儀ダッシュボードのプロンプトを共有する](#case-87) | フロントエンドとモーションデザイン | 公開プロンプトを使い、Kimi K3で3D地球儀ダッシュボード風のUIを作る流れを示している。 | Tutorial |
| [ブラウザ版Counter-Strikeを単一ファイルで作る](#case-88) | インタラクティブゲームと3D | Kimi K3が単一HTMLファイルでブラウザ向けFPS風ゲームを構築したデモ。 | Demo |
| [WebGPUの森ワールドをレビューする](#case-89) | 評価と制約 | Kimi K3生成のWebGPU森ワールドを評価し、没入型3Dシーンでの表現力と限界を示す。 | Evaluation |
| [ガラスハウスのプロンプト比較](#case-90) | 評価と制約 | 同じ建築シーンのプロンプトで Kimi K3 と Opus 4.8 の雰囲気、照明、空間の完成度を比較する。 | Evaluation |
| [生成アセットで CS を作る](#case-91) | コーディングと統合 | 小さな Counter-Strike 風ブラウザゲームを試作するとき、ゲームコードに Kimi K3、アセットに GPT Image 2 を組み合わせる。 | Integration |
| [ボクセルサッカー得点を評価](#case-92) | 評価と制約 | 同じ純粋な HTML/CSS/JS のサッカーアニメーションプロンプトを二つのモデルで走らせ、動きの品質とコストを比較する。 | Benchmark |
| [Minecraft ベンチを確認](#case-93) | 評価と制約 | ローンチ時の評判や価格だけを根拠にせず、構造化された Minecraft レビューを確認する。 | Benchmark |
| [五つの UI UX テストを行う](#case-94) | フロントエンドとモーションデザイン | 単一の frontend 画像ではなく、UI、ロゴ、Figma MCP の複数タスクで Kimi K3 を評価する。 | Evaluation |
| [Command Code の Design skill を使う](#case-95) | コーディングと統合 | トークン予算内で視覚的なゲーム試作を作るとき、Kimi K3 と Command Code の専用 design skill を組み合わせる。 | Integration |
| [ピラミッド探索ゲームを作る](#case-96) | インタラクティブゲームと3D | Kimi K3 で一日かけて 3D 探索ゲームを作り、クエスト、内部空間、探索範囲を見て品質を判断する。 | Demo |
| [参照から landing を作る](#case-97) | フロントエンドとモーションデザイン | Pinterest の参照、Figma AI、Motion Sites と Kimi K3 を使い、ビジュアル方向性を再利用可能な landing page セクションに変える。 | Tutorial |
| [API tier 制限を測る](#case-98) | 評価と制約 | Kimi K3 の agent 実行は、見出し価格だけでなく token、tier、TPM、TPD に基づいて予算化する。 | Limit |
| [Limbo 風 demo を比較](#case-99) | 評価と制約 | 同じゲーム試作で Kimi K3 と Fable 5 を比べ、遊べる範囲、仕上がり、コスト、バグを見る。 | Benchmark |
| [VulcanBenchのコスト結果を確認](#case-100) | 評価と制約 | この事例で、Kimi K3の「VulcanBenchのコスト結果を確認」における実ワークフロー、コスト、または制約を確認できます。 | Benchmark |
| [Minecraft構築の深さを比較](#case-101) | インタラクティブゲームと3D | この事例で、Kimi K3の「Minecraft構築の深さを比較」における実ワークフロー、コスト、または制約を確認できます。 | Evaluation |
| [Fallout風FPSを構築](#case-102) | インタラクティブゲームと3D | この事例で、Kimi K3の「Fallout風FPSを構築」における実ワークフロー、コスト、または制約を確認できます。 | Demo |
| [高品質Webサイトのチュートリアルを追う](#case-103) | フロントエンドとモーションデザイン | この事例で、Kimi K3の「高品質Webサイトのチュートリアルを追う」における実ワークフロー、コスト、または制約を確認できます。 | Tutorial |
| [二重振り子物理を評価](#case-104) | 評価と制約 | この事例で、Kimi K3の「二重振り子物理を評価」における実ワークフロー、コスト、または制約を確認できます。 | Benchmark |
| [データセンターRPGを出荷](#case-105) | インタラクティブゲームと3D | この事例で、Kimi K3の「データセンターRPGを出荷」における実ワークフロー、コスト、または制約を確認できます。 | Demo |
| [ヒューマノイドFrontend費用を比較](#case-106) | フロントエンドとモーションデザイン | この事例で、Kimi K3の「ヒューマノイドFrontend費用を比較」における実ワークフロー、コスト、または制約を確認できます。 | Benchmark |
| [ReactBenchの実運用度を確認](#case-107) | 評価と制約 | この事例で、Kimi K3の「ReactBenchの実運用度を確認」における実ワークフロー、コスト、または制約を確認できます。 | Benchmark |
| [3Dカーゲームを構築](#case-108) | インタラクティブゲームと3D | この事例で、Kimi K3の「3Dカーゲームを構築」における実ワークフロー、コスト、または制約を確認できます。 | Demo |
| [Claude CodeでKimi K3を動かす](#case-109) | コーディングと統合 | この事例で、Kimi K3の「Claude CodeでKimi K3を動かす」における実ワークフロー、コスト、または制約を確認できます。 | Integration |

<a id="games-3d"></a>
## 🎮 インタラクティブゲームと3D

<a id="case-1"></a>
### Case 1: [1つのプロンプトでボクセルレースを作る](https://x.com/ivanfioravanti/status/2077763009657627055) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**短いアイデアからレースを試作し、次の改善範囲を決めます**

作者はKimi K3が公開プロンプト1つで初版を作り、次版でレーサー、ゴール、詳細確認を追加すると報告しています

**Prompt:**

```text
Voxel star wars pod-racers run
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01-poster.jpg" alt="Case 1 source video poster" height="360"></a>

[Play case 1 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-2"></a>
### Case 2: [同じプロンプトでFroggerを比較する](https://x.com/ivanfioravanti/status/2077754781964054825) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**プロンプトを固定してモデル間の差を確認します**

作者は同一プロンプト比較としてKimi K3版を公開しましたが、プロンプト本文と評価基準は未公開です

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02-poster.jpg" alt="Case 2 source video poster" height="360"></a>

[Play case 2 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-3"></a>
### Case 3: [Froggerと録画を生成する](https://x.com/TheAhmadOsman/status/2077776567292338285) (by [@TheAhmadOsman](https://x.com/TheAhmadOsman))

**ゲームとプレイ録画の両方をワンショットで試します**

作者はゲームと録画工程をそれぞれ一度で生成したと報告しています。正確なプロンプトはありません

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03-poster.jpg" alt="Case 3 source video poster" height="360"></a>

[Play case 3 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-4"></a>
### Case 4: [Three.jsで空母を試作する](https://x.com/HarshithLucky3/status/2077753222018814360) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**具体的な発着艦シーンで対話型3D生成を試します**

作者はニミッツ級空母での戦闘機の発艦と回収を示し、3D生成を高く評価しています

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04-poster.jpg" alt="Case 4 source video poster" height="360"></a>

[Play case 4 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-9"></a>
### Case 9: [エージェントツールでPaper Mario風ゲームを作る](https://x.com/chongdashu/status/2077886028866531655) (by [@chongdashu](https://x.com/chongdashu))

**Kimi K3をエージェントharnessやアセットツールと組み合わせ、2Dと3Dのゲーム要素を生成します**

作者はPaper Mario風ゲームでKimi K3、Grok Build、2D用Spriterrific、3D用geometryを使ったと報告しています。ツール利用は示されていますが、正確な再利用可能プロンプトはありません

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-09.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-09-poster.jpg" alt="Case 9 source video poster" height="360"></a>

[Play case 9 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-09.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-11"></a>
### Case 11: [地下鉄を舞台にした一人称シューティングを生成する](https://x.com/bijanbowen/status/2077881805751873997) (by [@bijanbowen](https://x.com/bijanbowen))

**具体的な地下鉄という舞台を使い、生成されたFPSの結果を確認します**

作者はKimi K3による地下鉄FPSを示し、インフルエンサーであることが結果に影響した可能性を明記しています。プロンプトや再現可能な手順はありません

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-11.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-11-poster.jpg" alt="Case 11 source video poster" height="360"></a>

[Play case 11 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-11.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-19"></a>
### Case 19: [Blender MCPでV8エンジンをモデリングする](https://x.com/aisearchio/status/2077962156147146925) (by [@aisearchio](https://x.com/aisearchio))

**Blender MCPと1回の依頼を使って精密な機械3Dモデルを生成します**

レビュー担当者はKimi K3がBlender MCPと1つのプロンプトから完全なV8エンジンを生成したと報告しています。詳細レビューへのリンクはありますが正確なプロンプトはありません

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-19.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-19-poster.jpg" alt="Case 19 source video poster" height="360"></a>

[Play case 19 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-19.mp4)

Type: Integration | Date: 2026-07-17

---

<a id="case-23"></a>
### Case 23: [1つの参照からプレイ可能なバトルアリーナを作る](https://x.com/VORTEX_Promos/status/2077879705378730074) (by [@VORTEX_Promos](https://x.com/VORTEX_Promos))

**単一の参照を使い、完全にプレイ可能なアリーナのワンショット生成を試します**

作者はKimi K3が1つの参照からワンショットでアリーナを生成したと報告しています。別のランキング主張もありますが、具体的な活用例は実演された成果物です

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23-poster.jpg" alt="Case 23 source video poster" height="360"></a>

[Play case 23 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23-01.jpg" alt="Case 23 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-24"></a>
### Case 24: [自動プレイするレトロゲーム3本をHTMLファイルで作る](https://x.com/rohanpaul_ai/status/2077889084761206860) (by [@rohanpaul_ai](https://x.com/rohanpaul_ai))

**単体HTMLゲーム内にグラフィック、敵、ルール、自動プレイを実装させます**

Atomic Chatの比較ではRoad Fighter、Battle City、Q*bertを自動プレイHTMLとして作ったと報告されています。費用と品質は公開元の報告で、ここでは独立再現していません

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-24.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-24-poster.jpg" alt="Case 24 source video poster" height="360"></a>

[Play case 24 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-24.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-27"></a>
### Case 27: [ワンショットでカメレオンのかくれんぼゲームを作る](https://x.com/aimlapi/status/2077898742179459274) (by [@aimlapi](https://x.com/aimlapi))

**色合わせ、手続き生成エリア、音声、複数ラウンド得点を備えた単一ファイルゲームを生成します**

AIMLAPIは同じプロンプトのワンショット比較で、費用をKimi K3が3.11ドル、Fable 5が12.23ドルと報告しています。機能と費用はプロバイダー報告です

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-27.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-27-poster.jpg" alt="Case 27 source video poster" height="360"></a>

[Play case 27 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-27.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-36"></a>
### Case 36: [エージェント・ツールチェーンでPaper Mario風2.5Dゲームを作る](https://x.com/chongdashu/status/2077981621223837739) (by [@chongdashu](https://x.com/chongdashu))

**Kimi K3をGrok BuildまたはClaude Code、Spriterrificと組み合わせます**

作者はGrok BuildとKimi K3の手順とSpriterrificによるスプライト生成を示しています。ツールは特定されていますが正確な再利用プロンプトはありません

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-36.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-36-poster.jpg" alt="Case 36 source video poster" height="360"></a>

[Play case 36 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-36.mp4)

Type: Tutorial | Date: 2026-07-17

---

<a id="case-43"></a>
### Case 43: [ブラウザで動く3D武侠RPGを作る](https://x.com/AngryTomtweets/status/2077868163136450619) (by [@AngryTomtweets](https://x.com/AngryTomtweets))

**近接戦闘、クエスト、インベントリ、天候、屋内探索、Blender環境制作、アセット調整を組み合わせます**

ソースは近接戦闘、クエスト、インベントリ、動的天候、屋内に加え、Blenderモデリング、衝突判定改善、PBR再テクスチャリング、公開アセット調整を報告しています

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-43.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-43-poster.jpg" alt="Case 43 source video poster" height="360"></a>

[Play case 43 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-43.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-44"></a>
### Case 44: [ブラウザで動くMinecraft風マルチプレイゲームを作る](https://x.com/Alezander907/status/2077926014710407407) (by [@Alezander907](https://x.com/Alezander907))

**時間と費用を限定した実行でオンラインマルチプレイのブラウザゲームを生成します**

作者はKimi K3がゲームを1時間、6.57ドルで作ったと報告しています。1成果物の自己申告数値です

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-44.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-44-poster.jpg" alt="Case 44 source video poster" height="360"></a>

[Play case 44 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-44.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-48"></a>
### Case 48: [画面分割の協力型ブラウザゲームを再現する](https://x.com/ridark_eth/status/2077882889803378969) (by [@ridark_eth](https://x.com/ridark_eth))

**1回の依頼で画面分割協力プレイとリアルタイム環境操作を生成します**

作者はKimi K3がIt Takes Two風ゲームを1プロンプトで生成し、MarioとLuigiが画面分割で環境とリアルタイムに相互作用すると報告しています

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-48.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-48-poster.jpg" alt="Case 48 source video poster" height="360"></a>

[Play case 48 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-48.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-49"></a>
### Case 49: [Command Codeのdesignモードでプレイ可能なゲームを生成する](https://x.com/naymur_dev/status/2077873562661335207) (by [@naymur_dev](https://x.com/naymur_dev))

**designコマンドをワンショット制作に使い、プレイ可能か記録します**

作者はCommand Codeのdesignモード比較で、Kimi K3が0.038ドルでプレイ可能なゲームを生成したと報告しています。費用と品質は自己申告です

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-49.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-49-poster.jpg" alt="Case 49 source video poster" height="360"></a>

[Play case 49 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-49.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-51"></a>
### Case 51: [一体感のある武侠ブラウザRPGを構築する](https://x.com/TokenGremlin/status/2077855657068310620) (by [@TokenGremlin](https://x.com/TokenGremlin))

**移動、戦闘、クエスト、インベントリ、天候、探索、3D環境制作を1つに統合します**

ソースは近接戦闘、クエスト、インベントリ、動的天候、探索可能な屋内、一体感のある3D構造を組み合わせたRPGを報告しています

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-51.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-51-poster.jpg" alt="Case 51 source video poster" height="360"></a>

[Play case 51 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-51.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-54"></a>
### Case 54: [プレイ可能なHollow Knightクロスオーバーを作る](https://x.com/wangfeng0315/status/2077933531200991583) (by [@wangfeng0315](https://x.com/wangfeng0315))

**既存ゲームのアセットでKnightとKimiが戦うゲームを制作します**

Kimi勤務と明記する作者はHollow Knightのアセットからゲームを作り、公開プレイリンクを提供しています。帰属と評価では所属関係を考慮します

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54-poster.jpg" alt="Case 54 source video poster" height="360"></a>

[Play case 54 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54-01.jpg" alt="Case 54 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-17

---

<a id="case-60"></a>
### Case 60: [Fall Guys風3Dブラウザゲームをワンショットで作る](https://x.com/aayushman2703/status/2077857886441783526) (by [@aayushman2703](https://x.com/aayushman2703))

**1回の依頼でプレイ可能な3D障害物ゲームを生成し、プロジェクトを確認可能にします**

作者はワンショット制作を報告し、プロンプトとGitHubプロジェクトをソースから参照できるとしています。この記録ではプロンプトを転載していません

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-60.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-60-poster.jpg" alt="Case 60 source video poster" height="360"></a>

[Play case 60 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-60.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-61"></a>
### Case 61: [終末後のLisbon FPSを作って自己テストする](https://x.com/goncalo_canhoto/status/2077863166655037668) (by [@goncalo_canhoto](https://x.com/goncalo_canhoto))

**最大effortの1プロンプト実行で、提供までテスト、撮影、反復させます**

作者はKimi K3がテスト、スクリーンショット、反復を重ね、約1時間でプレイ可能なLisbonブラウザFPSを生成したと報告しています。時間と工程は自己申告です

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-61-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-61-01.jpg" alt="Case 61 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-63"></a>
### Case 63: [簡単な依頼からAnimal Crossing風ゲームを生成する](https://x.com/gagarot200/status/2077949230287896830) (by [@gagarot200](https://x.com/gagarot200))

**最小限の要件からプレイ可能性、ゲームループ、パララックス効果を確認します**

作者は非常に簡単なプロンプトから、ゲームループとパララックスを備えた完全にプレイ可能なゲームを生成したと報告しています。正確な文言は記録にありません

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-63.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-63-poster.jpg" alt="Case 63 source video poster" height="360"></a>

[Play case 63 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-63.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-65"></a>
### Case 65: [1文の要件からMario風ゲームを生成する](https://x.com/izutorishima/status/2077939370154475992) (by [@izutorishima](https://x.com/izutorishima))

**最小限のワンショット依頼でプレイ可能性、ステージ設計、ピクセルアート、パララックスを確認します**

作者は明らかなバグのないゲームを生成し、ステージ構造とパララックスも備えたと報告しています。同時に音楽とグラフィック品質を批判しています

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-01.jpg" alt="Case 65 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-02.jpg" alt="Case 65 source image 2" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-03.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-03.jpg" alt="Case 65 source image 3" height="360"></a>

Type: Demo | Date: 2026-07-17

---

<a id="case-67"></a>
### Case 67: [動作するゾンビFPSを作る](https://x.com/X2worldtech/status/2077902793449296203) (by [@X2worldtech](https://x.com/X2worldtech))

**具体的なゾンビシューティング目標で、完全にプレイ可能なFPSを確認します**

ソースはKimi K3による完全動作のゾンビFPSを示しています。プロンプト、実装詳細、外部評価はありません

> [!WARNING]
> The original source permalink returned HTTP 404 during the 2026-07-17 audit. Attribution and evidence are preserved from the supplied high-confidence source package.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-67.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-67-poster.jpg" alt="Case 67 source video poster" height="360"></a>

[Play case 67 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-67.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-71"></a>
### Case 71: [インディー宇宙船ゲームを作る](https://x.com/ChrisGPT/status/2078261217924087999) (by [@ChrisGPT](https://x.com/ChrisGPT))

**Kimi K3 Standardで初版を作り、一貫性、不具合、視覚品質、トークン費用を比較します**

ChrisGPTは約2.50ドルのAPIトークン費用で宇宙船ゲームの初版を作成したと報告しています。GPT-5.5の初版より一貫性が高く不具合が少ない一方、Fable 5の方が視覚的に洗練されていました

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-71.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-71-poster.jpg" alt="Case 71 source video poster" height="360"></a>

[Play case 71 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-71.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-73"></a>
### Case 73: [Summer Engineゲームを自己テスト](https://x.com/MathiasHeide/status/2078231589436465199) (by [@MathiasHeide](https://x.com/MathiasHeide))

**Kimi K3にゲームを実行させ、スクリーンショットとログを確認し、同じセッションで欠陥を修正させます**

Mathias Heideによると、Kimi K3は27分の1セッションで紙飛行機ゲームを構築し、実行、スクリーンショット、ログ確認、バグ修正を行い、黒い機体を白に直しました

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-73.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-73-poster.jpg" alt="Case 73 source video poster" height="360"></a>

[Play case 73 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-73.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-77"></a>
### Case 77: [ブラウザ版バトルロイヤルを反復改善](https://x.com/Ananth7e/status/2078158089929601203) (by [@Ananth7e](https://x.com/Ananth7e))

**機能の多いブラウザゲームでは、長い自律反復と的を絞った追加プロンプトを見込みます**

Ananthによると、Kimi K3は130分以上、40回以上のChromeスクリーンショット反復でPUBG風ゲームを作り、その後さらに2つのプロンプトで残るバグを直しました

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-77.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-77-poster.jpg" alt="Case 77 source video poster" height="360"></a>

[Play case 77 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-77.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-83"></a>
### Case 83: [宇宙ゲームの景観を拡張する](https://x.com/startracker/status/2078543423167160342) (by [@startracker](https://x.com/startracker))

**Kimi K3で一枚の宇宙ゲーム風景を、地形・宇宙船・ライティングを含む広いビジュアルへ展開した。**

公開画像はゲーム的なSFシーンを示し、Kimi K3が空間の奥行き、複数オブジェクト、色調をまとめて扱えることを示すデモになっている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-83.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-83-poster.jpg" alt="Case 83 source video poster" height="360"></a>

[Play case 83 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-83.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-84"></a>
### Case 84: [Three.js物理レンダラーの詰まりを解消する](https://x.com/mattwatkajtys/status/2078523373861339475) (by [@mattwatkajtys](https://x.com/mattwatkajtys))

**Kimi K3を実装支援に使い、Three.jsの物理レンダリング問題を前進させた事例。**

作者は詰まっていた3Dレンダリングの問題をKimi K3で解決したと報告し、ブラウザ上の物理シーンを映像で示している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-84.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-84-poster.jpg" alt="Case 84 source video poster" height="360"></a>

[Play case 84 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-84.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-88"></a>
### Case 88: [ブラウザ版Counter-Strikeを単一ファイルで作る](https://x.com/prasenx/status/2078453069021659477) (by [@prasenx](https://x.com/prasenx))

**Kimi K3が単一HTMLファイルでブラウザ向けFPS風ゲームを構築したデモ。**

作者は一つのファイルで動くCounter-Strike風ゲームを示し、Kimi K3がゲームループ、入力、描画、簡易UIをまとめて生成できることを示している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-88.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-88-poster.jpg" alt="Case 88 source video poster" height="360"></a>

[Play case 88 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-88.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-96"></a>
### Case 96: [ピラミッド探索ゲームを作る](https://x.com/ice_bearcute/status/2078828887468056763) (by [@ice_bearcute](https://x.com/ice_bearcute))

**Kimi K3 で一日かけて 3D 探索ゲームを作り、クエスト、内部空間、探索範囲を見て品質を判断する。**

ice_bearcute は Kimi K3 だけで Pyramid Expedition という 3D ゲームを一日で作ったと報告している。単なる外観シーンではなく、古代の墓を探索しクエストを完了できると説明され、添付メディアが gameplay の証拠になっている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-96.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-96-poster.jpg" alt="Case 96 source video poster" height="360"></a>

[Play case 96 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-96.mp4)

Type: Demo | Date: 2026-07-19

---

<a id="case-101"></a>
### Case 101: [Minecraft構築の深さを比較](https://x.com/vikktorrrre/status/2079294696459804762) (by [@vikktorrrre](https://x.com/vikktorrrre))

**この事例で、Kimi K3の「Minecraft構築の深さを比較」における実ワークフロー、コスト、または制約を確認できます。**

元投稿は「Minecraft構築の深さを比較」に関する公開証拠を示し、作者の説明、結果メディア、またはベンチマーク/チュートリアル情報を含みます。このリポジトリは検証可能な事実だけを残し、未公開のpromptや手順は補いません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-101.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-101-poster.jpg" alt="Case 101 source video poster" height="360"></a>

[Play case 101 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-101.mp4)

Type: Evaluation | Date: 2026-07-20

---

<a id="case-102"></a>
### Case 102: [Fallout風FPSを構築](https://x.com/kirillk_web3/status/2079290747585437781) (by [@kirillk_web3](https://x.com/kirillk_web3))

**この事例で、Kimi K3の「Fallout風FPSを構築」における実ワークフロー、コスト、または制約を確認できます。**

元投稿は「Fallout風FPSを構築」に関する公開証拠を示し、作者の説明、結果メディア、またはベンチマーク/チュートリアル情報を含みます。このリポジトリは検証可能な事実だけを残し、未公開のpromptや手順は補いません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-102.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-102-poster.jpg" alt="Case 102 source video poster" height="360"></a>

[Play case 102 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-102.mp4)

Type: Demo | Date: 2026-07-20

---

<a id="case-105"></a>
### Case 105: [データセンターRPGを出荷](https://x.com/demian_ai/status/2079239035596218578) (by [@demian_ai](https://x.com/demian_ai))

**この事例で、Kimi K3の「データセンターRPGを出荷」における実ワークフロー、コスト、または制約を確認できます。**

元投稿は「データセンターRPGを出荷」に関する公開証拠を示し、作者の説明、結果メディア、またはベンチマーク/チュートリアル情報を含みます。このリポジトリは検証可能な事実だけを残し、未公開のpromptや手順は補いません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-105.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-105-poster.jpg" alt="Case 105 source video poster" height="360"></a>

[Play case 105 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-105.mp4)

Type: Demo | Date: 2026-07-20

---

<a id="case-108"></a>
### Case 108: [3Dカーゲームを構築](https://x.com/LexnLin/status/2079233761242235081) (by [@LexnLin](https://x.com/LexnLin))

**この事例で、Kimi K3の「3Dカーゲームを構築」における実ワークフロー、コスト、または制約を確認できます。**

元投稿は「3Dカーゲームを構築」に関する公開証拠を示し、作者の説明、結果メディア、またはベンチマーク/チュートリアル情報を含みます。このリポジトリは検証可能な事実だけを残し、未公開のpromptや手順は補いません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-poster.jpg" alt="Case 108 source video poster" height="360"></a>

[Play case 108 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-01.jpg" alt="Case 108 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-02.jpg" alt="Case 108 source image 2" height="360"></a>

Type: Demo | Date: 2026-07-20

---


<a id="frontend-motion"></a>
## 🎨 フロントエンドとモーションデザイン

<a id="case-5"></a>
### Case 5: [対話できるモーショングラフィックを作る](https://x.com/chetaslua/status/2077749371144442022) (by [@chetaslua](https://x.com/chetaslua))

**停止中も操作できるグラフィックをワンショットで構築します**

作者は42分、単純なコード、harness・MCP・skillなしの一回生成と報告しています

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05-poster.jpg" alt="Case 5 source video poster" height="360"></a>

[Play case 5 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-6"></a>
### Case 6: [同期したモーション広告を作る](https://x.com/abhinavflac/status/2077760297918484667) (by [@abhinavflac](https://x.com/abhinavflac))

**音楽、効果、動きの同期を確認します**

作者はSpotify風広告をプロンプトだけで一回生成したと報告していますが、正確なプロンプトは未公開です

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06-poster.jpg" alt="Case 6 source video poster" height="360"></a>

[Play case 6 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-14"></a>
### Case 14: [モーションデザインをすべてコードで制作する](https://x.com/chetaslua/status/2077952938564354503) (by [@chetaslua](https://x.com/chetaslua))

**補助的な生成ツールなしのワンショット・コーディングでモーションデザインを作れるか試します**

作者はMCP、skill、ツール、動画生成、特別なプロンプトを使わず、すべてコードで作ったKimi K3のワンショット結果を報告しています。正確なプロンプトはありません

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-14.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-14-poster.jpg" alt="Case 14 source video poster" height="360"></a>

[Play case 14 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-14.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-15"></a>
### Case 15: [人物を調査してアニメーション付き個人サイトを作る](https://x.com/nicky_sap/status/2077857190707429411) (by [@nicky_sap](https://x.com/nicky_sap))

**広い個人サイト要件を与え、モデルの調査、計画、反復、ブラウザ検証を確認します**

作者はKimi K3がNick Saponaroを調査し、幅広い依頼からサイトを作成し、計画、テスト、反復、ブラウザ確認まで行ったと報告しています。自己申告の実演です

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-15.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-15-poster.jpg" alt="Case 15 source video poster" height="360"></a>

[Play case 15 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-15.mp4)

Type: Tutorial | Date: 2026-07-16

---

<a id="case-17"></a>
### Case 17: [ブラックホール・シミュレーションを生成する](https://x.com/chetaslua/status/2077961850352971796) (by [@chetaslua](https://x.com/chetaslua))

**科学可視化課題を使い、生成されたブラックホール・シミュレーションを確認します**

作者はKimi K3による成果物を示し、これまで見た中で最高と評価しています。可視結果はありますが、プロンプト、基準、独立検証はありません

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-17.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-17-poster.jpg" alt="Case 17 source video poster" height="360"></a>

[Play case 17 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-17.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-22"></a>
### Case 22: [複雑なフロントエンドのモデリング、粒子、シェーダーを試す](https://x.com/karminski3/status/2077889959223337099) (by [@karminski3](https://x.com/karminski3))

**公開プロンプトを使い、1回の実行でモデリング精度、粒子効果、インラインシェーダー生成を確認します**

作者は精密なモデリング、粒子効果、複雑なインラインシェーダーコードを含む1回実行結果を報告し、テスト用プロンプトはリンク先で公開されていると述べています

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-22.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-22-poster.jpg" alt="Case 22 source video poster" height="360"></a>

[Play case 22 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-22.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-26"></a>
### Case 26: [手続き型音楽ツールを1回で生成する](https://x.com/mirochill/status/2077723551331758478) (by [@mirochill](https://x.com/mirochill))

**対話型の手続き型音楽生成器をワンショットで作り、可視結果は慎重に比較します**

作者はKimi K3が1回で生成し、Fable 5とGPT-5.6 Solより良かったと報告しています。標準化ベンチマークではなく作者自身のテストセットです

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-26-poster.jpg" alt="Case 26 source video poster" height="360"></a>

[Play case 26 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-26.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-33"></a>
### Case 33: [2枚の画像からThree.js製品ページを作る](https://x.com/1littlecoder/status/2077890296806031665) (by [@1littlecoder](https://x.com/1littlecoder))

**2枚の参照画像と明示的なThree.js要件で製品プレゼンテーションを生成します**

作者はKimi K3が2枚の画像から製品ページを設計し、依頼したThree.js版を生成したと報告しています。追加のプロンプトや実装詳細はありません

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-33.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-33-poster.jpg" alt="Case 33 source video poster" height="360"></a>

[Play case 33 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-33.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-39"></a>
### Case 39: [高級パン切り器と製品ページを発案する](https://x.com/filicroval/status/2077871090731221438) (by [@filicroval](https://x.com/filicroval))

**製品発案、分解図、実演、ランディングページを1つの成果物にまとめます**

作者はKimi K3がギロチン式パン切り器を発案し、高級品として位置付け、分解図と実演を含むページを作ったと報告しています

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-39.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-39-poster.jpg" alt="Case 39 source video poster" height="360"></a>

[Play case 39 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-39.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-45"></a>
### Case 45: [10秒の再帰的ペリカンGIFを生成する](https://x.com/1littlecoder/status/2077880380900937865) (by [@1littlecoder](https://x.com/1littlecoder))

**完全指定したループアニメーション要件で物語的連続性と再帰構造を確認します**

ソースには、自転車に乗ったペリカンが同じ動画をテキストで受け取り、カメラがズームする10秒ループGIFのプロンプトがあり、Kimi K3の結果も示されています

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-45.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-45-poster.jpg" alt="Case 45 source video poster" height="360"></a>

[Play case 45 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-45.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-55"></a>
### Case 55: [BMW M4 CSの側面SVGを生成する](https://x.com/HarshithLucky3/status/2077765821380886942) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**特定の車種と視点を指定し、ベクターイラスト出力を確認します**

作者はKimi K3 MaxによるBMW M4 CSの側面SVGを示しています。成果物はありますが、プロンプトや制作手順はありません

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-55-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-55-01.jpg" alt="Case 55 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-58"></a>
### Case 58: [スクリーンショットのフィードバックでGargantuaを再現する](https://x.com/AngryTomtweets/status/2077868981659324444) (by [@AngryTomtweets](https://x.com/AngryTomtweets))

**繰り返すスクリーンショットを観測情報に使い、科学可視化を診断・改善します**

ソースはKimi K3が62枚の自己取得スクリーンショットを読み、問題を診断し、反復的に対応してInterstellarのGargantuaを再現したと報告しています

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-58.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-58-poster.jpg" alt="Case 58 source video poster" height="360"></a>

[Play case 58 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-58.mp4)

Type: Tutorial | Date: 2026-07-16

---

<a id="case-66"></a>
### Case 66: [62枚のスクリーンショットでブラックホール可視化を改善する](https://x.com/TokenGremlin/status/2077855959201042645) (by [@TokenGremlin](https://x.com/TokenGremlin))

**スクリーンショットのフィードバックループで、多数の反復を通じてシミュレーションを診断・修正します**

ソースはKimi K3が62枚のスクリーンショットにわたりInterstellarのGargantuaを再構築したと報告しています。独立した物理精度ではなく、報告された反復手順を示します

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-66.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-66-poster.jpg" alt="Case 66 source video poster" height="360"></a>

[Play case 66 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-66.mp4)

Type: Tutorial | Date: 2026-07-16

---

<a id="case-68"></a>
### Case 68: [ポストトレーニング製品のマーケティングPDFを作る](https://x.com/Satvik_Pen/status/2077859673517023313) (by [@Satvik_Pen](https://x.com/Satvik_Pen))

**製品名と納品形式を指定してマーケティング文書を生成します**

作者はThinking MachinesのInklingポストトレーニングに関するPDFを依頼し、結果と制作過程を高く評価しています。プロンプトや評価基準はありません

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-01.png" alt="Case 68 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-02.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-02.png" alt="Case 68 source image 2" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-03.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-03.png" alt="Case 68 source image 3" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-04.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-04.png" alt="Case 68 source image 4" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-70"></a>
### Case 70: [1つのプロンプトからユーザーインターフェースを作る](https://x.com/BrianMRey/status/2077891942088671689) (by [@BrianMRey](https://x.com/BrianMRey))

**1回の依頼で完全なUIデザインを生成し、結果を確認します**

作者は1プロンプトのKimi K3実行によるUIを示し、主観的に非常に高く評価しています。正確なプロンプトと評価基準はありません

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-70.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-70-poster.jpg" alt="Case 70 source video poster" height="360"></a>

[Play case 70 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-70.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-78"></a>
### Case 78: [受賞級スタイルのWebサイトを作る](https://x.com/viktoroddy/status/2078140696910037002) (by [@viktoroddy](https://x.com/viktoroddy))

**最終画像だけでなく、完全な録画セッションでKimi K3のWeb制作工程を評価します**

Viktor OddyはKimi K3で受賞級スタイルのWebサイトを作る13分のチュートリアルを公開し、工程全体の証拠を提供しています

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-78.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-78-poster.jpg" alt="Case 78 source video poster" height="360"></a>

[Play case 78 tutorial video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-78.mp4)

Type: Tutorial | Date: 2026-07-17

---

<a id="case-81"></a>
### Case 81: [メタボールのスクロール連動フロントエンドを作る](https://x.com/abhinavflac/status/2078603131055993130) (by [@abhinavflac](https://x.com/abhinavflac))

**Kimi K3が、発光するメタボールとスクロール連動アニメーションを含む洗練されたWeb UIを組み立てた。**

作者は完成した動的フロントエンドを映像で示しており、プロンプトから視覚演出、レイアウト、アニメーションまで一体で生成されたことが確認できる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-81.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-81-poster.jpg" alt="Case 81 source video poster" height="360"></a>

[Play case 81 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-81.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-82"></a>
### Case 82: [個人サイトを複数モデルで再設計して比較する](https://x.com/fabriciocarraro/status/2078574831466078265) (by [@fabriciocarraro](https://x.com/fabriciocarraro))

**同じ個人サイト再設計タスクでKimi K3を他モデルと並べ、ビジュアル品質と構成の違いを比較している。**

投稿は複数モデルの出力をまとめて比較し、Kimi K3のデザイン判断、セクション構成、仕上げの傾向を観察できる素材になっている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-82.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-82-poster.jpg" alt="Case 82 source video poster" height="360"></a>

[Play case 82 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-82.mp4)

Type: Evaluation | Date: 2026-07-18

---

<a id="case-86"></a>
### Case 86: [インタラクティブな頭皮エクスプローラーを作る](https://x.com/MiaAI_lab/status/2078508824752017757) (by [@MiaAI_lab](https://x.com/MiaAI_lab))

**Kimi K3が教育用途の人体頭皮ビジュアライザーを生成し、視覚化UIの使い道を示した。**

公開デモは頭皮構造を探索するインタラクティブ画面で、医療・教育系の説明UIを短い入力から作れる可能性を示している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-86.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-86-poster.jpg" alt="Case 86 source video poster" height="360"></a>

[Play case 86 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-86.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-87"></a>
### Case 87: [3D地球儀ダッシュボードのプロンプトを共有する](https://x.com/hqmank/status/2078465403349840144) (by [@hqmank](https://x.com/hqmank))

**公開プロンプトを使い、Kimi K3で3D地球儀ダッシュボード風のUIを作る流れを示している。**

投稿には参照プロンプトと完成映像が含まれ、Kimi K3で地球儀、データ表示、ダッシュボード風レイアウトを組み合わせる方法を確認できる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-87.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-87-poster.jpg" alt="Case 87 source video poster" height="360"></a>

[Play case 87 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-87.mp4)

Type: Tutorial | Date: 2026-07-18

---

<a id="case-94"></a>
### Case 94: [五つの UI UX テストを行う](https://x.com/MAXdeg0/status/2078855257686196399) (by [@MAXdeg0](https://x.com/MAXdeg0))

**単一の frontend 画像ではなく、UI、ロゴ、Figma MCP の複数タスクで Kimi K3 を評価する。**

MAXdeg0 は Claude Code と Figma MCP サーバーを使い、Kimi K3 で五つの UI/UX とロゴデザインテストを行ったと報告している。ランディングページ再構築、ヒーローセクション再構築、ロゴ作業などが挙げられ、少なくとも landing の時間とコストが示されている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-94.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-94-poster.jpg" alt="Case 94 source video poster" height="360"></a>

[Play case 94 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-94.mp4)

Type: Evaluation | Date: 2026-07-19

---

<a id="case-97"></a>
### Case 97: [参照から landing を作る](https://x.com/MAXdeg0/status/2078776969072877715) (by [@MAXdeg0](https://x.com/MAXdeg0))

**Pinterest の参照、Figma AI、Motion Sites と Kimi K3 を使い、ビジュアル方向性を再利用可能な landing page セクションに変える。**

MAXdeg0 は、Pinterest からスタイル参照を取り、Figma AI で見た目をリミックスし、または UI 参照と prompt を Motion Sites に貼って Kimi K3 にページを作らせる流れを説明している。さらに、この手法は追加セクションにも再利用でき、完全な prompting guide へのリンクがある。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-97.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-97-poster.jpg" alt="Case 97 source video poster" height="360"></a>

[Play case 97 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-97.mp4)

Type: Tutorial | Date: 2026-07-19

---

<a id="case-103"></a>
### Case 103: [高品質Webサイトのチュートリアルを追う](https://x.com/_guillecasaus/status/2079258261014908980) (by [@_guillecasaus](https://x.com/_guillecasaus))

**この事例で、Kimi K3の「高品質Webサイトのチュートリアルを追う」における実ワークフロー、コスト、または制約を確認できます。**

元投稿は「高品質Webサイトのチュートリアルを追う」に関する公開証拠を示し、作者の説明、結果メディア、またはベンチマーク/チュートリアル情報を含みます。このリポジトリは検証可能な事実だけを残し、未公開のpromptや手順は補いません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-103.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-103-poster.jpg" alt="Case 103 source video poster" height="360"></a>

[Play case 103 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-103.mp4)

Type: Tutorial | Date: 2026-07-20

---

<a id="case-106"></a>
### Case 106: [ヒューマノイドFrontend費用を比較](https://x.com/ChrisGPT/status/2079236298464796958) (by [@ChrisGPT](https://x.com/ChrisGPT))

**この事例で、Kimi K3の「ヒューマノイドFrontend費用を比較」における実ワークフロー、コスト、または制約を確認できます。**

元投稿は「ヒューマノイドFrontend費用を比較」に関する公開証拠を示し、作者の説明、結果メディア、またはベンチマーク/チュートリアル情報を含みます。このリポジトリは検証可能な事実だけを残し、未公開のpromptや手順は補いません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-106.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-106-poster.jpg" alt="Case 106 source video poster" height="360"></a>

[Play case 106 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-106.mp4)

Type: Benchmark | Date: 2026-07-20

---


<a id="coding-integrations"></a>
## 💻 コーディングと統合

<a id="case-18"></a>
### Case 18: [動作するmacOSを備えた仮想MacBookを作る](https://x.com/scottstts/status/2077890054299541890) (by [@scottstts](https://x.com/scottstts))

**Three.jsのハードウェア描画とブラウザ上で操作できるOSシミュレーションを組み合わせます**

ソースはKimi K3がThree.jsで仮想MacBookと動作するmacOS風環境を作成したと報告しています。成果物は示されていますが実装手順はありません

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-18.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-18-poster.jpg" alt="Case 18 source video poster" height="360"></a>

[Play case 18 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-18.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-25"></a>
### Case 25: [DSLからPTXまでのGPUコンパイラを作る](https://x.com/rohanpaul_ai/status/2077886618657231220) (by [@rohanpaul_ai](https://x.com/rohanpaul_ai))

**DSL、コンパイラパス、PTX生成、Tensor Core経路を含むエンドツーエンド課題を使います**

ソースはKimi K3がDSLと各パスからPTX生成までGPUコンパイラを一から構築し、そのTensor Core経路をTritonと比較したと報告しています。独立ベンチマーク詳細はありません

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-25-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-25-01.png" alt="Case 25 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-32"></a>
### Case 32: [WebGL2でリアルタイム・ブラックホール光線追跡を作る](https://x.com/AlicanKiraz0/status/2077885419744612597) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**単一HTML内でネイティブWebGL2の測地線光線追跡を1プロンプトで生成できるか試します**

作者は動作するブラックホール光曲がり光線追跡を求めるベンチマークを説明しています。課題と参加モデルは確認できますが、完全で独立した結果監査はありません

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-32.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-32-poster.jpg" alt="Case 32 source video poster" height="360"></a>

[Play case 32 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-32.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-46"></a>
### Case 46: [mGBA WASMを使ってGame Boy Advanceエミュレーターを作る](https://x.com/teortaxesTex/status/2077925090168062272) (by [@teortaxesTex](https://x.com/teortaxesTex))

**ライセンス済み3Dモデルと実在のエミュレーターコアを統合し、UIとプレイ体験を再帰的に改善します**

プロジェクトはライセンス済みAGB-001モデルを調整し、mGBA WASMコアを統合し、再帰的自己改善を行っています。独立再現ではなくプロジェクト説明の引用です

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-46-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-46-01.jpg" alt="Case 46 source image 1" height="360"></a>

Type: Integration | Date: 2026-07-17

---

<a id="case-50"></a>
### Case 50: [中国語ソースから複数テーマを調査する](https://x.com/tphuang/status/2077911994607239400) (by [@tphuang](https://x.com/tphuang))

**長時間の調査課題でモデル世代間の網羅性と待ち時間を比較します**

作者は多くのテーマを中国語ソースで試し、K2.6より詳細だが遅いと報告しています。当時はサービス需要が高かったことも記しています

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-50-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-50-01.png" alt="Case 50 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-17

---

<a id="case-56"></a>
### Case 56: [動作するアプリ付きmacOSをブラウザに再現する](https://x.com/twid/status/2077924755357974989) (by [@twid](https://x.com/twid))

**音楽、ブラウザ、メールの各アプリを含むブラウザOSシミュレーションを作ります**

ソースはKimi K3で音楽、ブラウザ、メールなどを備えたブラウザ版macOSクローンを作成したと報告しています。実装詳細はありません

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-56.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-56-poster.jpg" alt="Case 56 source video poster" height="360"></a>

[Play case 56 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-56.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-62"></a>
### Case 62: [動作するFaceTime付きmacOSシミュレーションを作る](https://x.com/LinearUncle/status/2077919552239997078) (by [@LinearUncle](https://x.com/LinearUncle))

**仮想OS課題で生成されたアプリ操作が機能するか試します**

作者はmacOS風環境を示し、FaceTime機能が動作すると報告しています。セットアップや検証手順はありません

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-62-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-62-01.jpg" alt="Case 62 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-17

---

<a id="case-64"></a>
### Case 64: [2つのタスクを並べるフロントエンド効果比較機能を追加する](https://x.com/MinLiBuilds/status/2077939461510615376) (by [@MinLiBuilds](https://x.com/MinLiBuilds))

**完了済みタスクを2つ選び、横並び表示し、ビューと操作を同期するツールを作ります**

作者はタスク選択、2つのブラウザペイン、objectとroamingモード、視点同期、操作テストを備えた比較ワークフローを追加させたと報告しています。投稿はモデル制約にも触れています

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-64.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-64-poster.jpg" alt="Case 64 source video poster" height="360"></a>

[Play case 64 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-64.mp4)

Type: Tutorial | Date: 2026-07-17

---

<a id="case-75"></a>
### Case 75: [KimiをCodexサブエージェントに設定](https://x.com/nauczymycieAI/status/2078181182701736132) (by [@nauczymycieAI](https://x.com/nauczymycieAI))

**Codexが統括を担い、フロントエンド実行をKimi K3 OpenCodeサブエージェントに委任し、秘密情報の境界を明確にします**

nauczymycieAIはOpenCodeの導入確認、Codexに貼らずにKimi APIキーを手動作成、Kimi K3への接続、フロントエンド作業を委任するグローバルCodex skill作成という手順を公開しています

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-75.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-75.jpg" alt="Case 75 source image 1" height="360"></a>

Type: Tutorial | Date: 2026-07-17

---

<a id="case-79"></a>
### Case 79: [ChatLLMで簡単なコーディングをルーティング](https://x.com/abacusai/status/2078022418661257411) (by [@abacusai](https://x.com/abacusai))

**簡単なコーディングをKimi K3に送り、難しいコーディングとデザインを別モデルに割り当てます**

Abacus AIはChatLLMでKimi K3を提供し、簡単なコーディングはKimi K3、難しい作業はFable 5、デザインはGPT-5.6 Solというルートを示しています。同じルーターはChatLLM、Abacus AI agent、Claude Codeで使えます

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-79.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-79.jpg" alt="Case 79 source image 1" height="360"></a>

Type: Integration | Date: 2026-07-17

---

<a id="case-91"></a>
### Case 91: [生成アセットで CS を作る](https://x.com/karankendre/status/2078938615900688728) (by [@karankendre](https://x.com/karankendre))

**小さな Counter-Strike 風ブラウザゲームを試作するとき、ゲームコードに Kimi K3、アセットに GPT Image 2 を組み合わせる。**

Karan Kendre は、Counter-Strike 風プロジェクトで Kimi K3 がゲームを作り、GPT Image 2 がアセットを作ったと報告し、総コストを約10ドルとしている。ソース動画が可視成果物なので、これは Kimi 単独ベンチマークではなくツール連携ワークフローとして扱う。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-91.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-91-poster.jpg" alt="Case 91 source video poster" height="360"></a>

[Play case 91 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-91.mp4)

Type: Integration | Date: 2026-07-19

---

<a id="case-95"></a>
### Case 95: [Command Code の Design skill を使う](https://x.com/MrAhmadAwais/status/2078841789205934547) (by [@MrAhmadAwais](https://x.com/MrAhmadAwais))

**トークン予算内で視覚的なゲーム試作を作るとき、Kimi K3 と Command Code の専用 design skill を組み合わせる。**

Ahmad Awais は Command Code と /design skill で Kimi K3 を使い、Forza 風の追走カメラゲームを作ったと報告している。セッション費用は0.97ドルで、道路と車のスケール、背景、アニメーション、霧の修正を含むため、具体的な agent harness ワークフローとして扱える。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-95.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-95-poster.jpg" alt="Case 95 source video poster" height="360"></a>

[Play case 95 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-95.mp4)

Type: Integration | Date: 2026-07-19

---

<a id="case-109"></a>
### Case 109: [Claude CodeでKimi K3を動かす](https://x.com/boxmining/status/2079115758618239337) (by [@boxmining](https://x.com/boxmining))

**この事例で、Kimi K3の「Claude CodeでKimi K3を動かす」における実ワークフロー、コスト、または制約を確認できます。**

元投稿は「Claude CodeでKimi K3を動かす」に関する公開証拠を示し、作者の説明、結果メディア、またはベンチマーク/チュートリアル情報を含みます。このリポジトリは検証可能な事実だけを残し、未公開のpromptや手順は補いません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-109.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-109-poster.jpg" alt="Case 109 source video poster" height="360"></a>

[Play case 109 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-109.mp4)

Type: Integration | Date: 2026-07-20

---


<a id="evaluation-limits"></a>
## 🧪 評価と制約

<a id="case-7"></a>
### Case 7: [BridgeBenchの溶岩ランプ課題でフロントエンドデザインを比較する](https://x.com/bridgemindai/status/2077868061953007908) (by [@bridgemindai](https://x.com/bridgemindai))

**BridgeBenchの溶岩ランプ課題を、普遍的な順位ではなく範囲を限定した比較として使います**

BridgeMind AIはKimi K3が同課題でFable 5を上回り、引用されたArenaで1位になったと報告しています。公開元が報告した比較結果です

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-07.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-07-poster.jpg" alt="Case 7 source video poster" height="360"></a>

[Play case 7 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-07.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-8"></a>
### Case 8: [編集方針に沿う台本執筆をベンチマークする](https://x.com/Whats_AI/status/2077860441380798908) (by [@Whats_AI](https://x.com/Whats_AI))

**明示した社内ベンチマーク内で、編集トーンへの適合度、相対順位、台本1本当たりの費用を測定します**

Whats_AIは初期社内結果として2,840 Elo、1位、台本1本当たり約0.25ドルと報告しています。一般性能や価格の保証ではなく、1組織の予備的ベンチマークです

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-08-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-08-01.jpg" alt="Case 8 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-16

---

<a id="case-10"></a>
### Case 10: [Flappy系ゲームのデザイン、費用、難易度を比較する](https://x.com/MrAhmadAwais/status/2077915347974557862) (by [@MrAhmadAwais](https://x.com/MrAhmadAwais))

**生成ゲームの比較では難易度設定、費用、デザイン、ゲームプレイ機能を記録します**

Command Codeの社内ベンチマークは異なる難易度設定でKimi K3を0.024ドル、Fable 5を0.42ドル、GPT-5.6 Solを0.15ドルとしています。設定が同一でない限定的な社内比較です

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-10.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-10-poster.jpg" alt="Case 10 source video poster" height="360"></a>

[Play case 10 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-10.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-12"></a>
### Case 12: [同じデザインプロンプトでゲーム設計を比較する](https://x.com/CommandCodeAI/status/2077921526213746948) (by [@CommandCodeAI](https://x.com/CommandCodeAI))

**デザインプロンプトを固定し、進行速度、デザイン感覚、プレイ感を分けて確認します**

Command CodeはKimi K3、GPT-5.6 Sol、Fable 5を同じプロンプトで比較し、Kimi K3のデザイン感覚を高く、他2つの速度を速すぎると評価しています。公開元による評価です

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-12.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-12-poster.jpg" alt="Case 12 source video poster" height="360"></a>

[Play case 12 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-12.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-13"></a>
### Case 13: [統計監査には独立したレビューを必須にする](https://x.com/emollick/status/2077869293031624793) (by [@emollick](https://x.com/emollick))

**モデルが生成した統計監査は、知見を採用する前に独立した専門家または別モデルのレビューと組み合わせます**

Ethan MollickはKimi K3 Maxが過去研究の監査で統計を誤用したと報告し、別の批判にも同意しています。この否定的事例は独立検証の必要性を示します

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-13-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-13-01.jpg" alt="Case 13 source image 1" height="360"></a>

Type: Limit | Date: 2026-07-16

---

<a id="case-16"></a>
### Case 16: [遅いが高品質なフロントエンド実行を評価する](https://x.com/Lentils80/status/2077387333154857151) (by [@Lentils80](https://x.com/Lentils80))

**フロントエンド課題では出力品質とともに完了時間を記録します**

作者は実行に35分かかり、そのプロンプトで見た中でも最高水準の出力だったと報告しています。速度と品質はいずれも1利用者の観測です

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-16.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-16-poster.jpg" alt="Case 16 source video poster" height="360"></a>

[Play case 16 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-16.mp4)

Type: Evaluation | Date: 2026-07-15

---

<a id="case-20"></a>
### Case 20: [殺人ミステリー執筆で伏線の失敗を検証する](https://x.com/emollick/status/2077951790868238616) (by [@emollick](https://x.com/emollick))

**生成ミステリーが手がかり、難解さ、伏線のバランスを取れているか評価します**

Ethan MollickはKimi K3が良い殺人ミステリーを書けず、手がかりを明白すぎる一方で難解にもして、伏線にも失敗したと報告しています。他モデルにも同じ制約があると述べています

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-01.jpg" alt="Case 20 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-02.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-02.png" alt="Case 20 source image 2" height="360"></a>

Type: Limit | Date: 2026-07-17

---

<a id="case-21"></a>
### Case 21: [ミレニアム・ファルコンのモデリングとアニメーションを比較する](https://x.com/gmi_cloud/status/2077903360263676090) (by [@gmi_cloud](https://x.com/gmi_cloud))

**同じスタイル要件とeffort設定で、3Dモデリング、アニメーション、時間、費用を比較します**

GMI Cloudは最大effortでKimi K3とFable 5を比較し、Kimi K3は時間が長かったものの、最初のテストでは約3分の1、別のテストでは半分未満の費用だったとしています。プロバイダー報告です

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-21.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-21-poster.jpg" alt="Case 21 source video poster" height="360"></a>

[Play case 21 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-21.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-28"></a>
### Case 28: [Kimi K3プロジェクト10件のコレクションをレビューする](https://x.com/minchoi/status/2077957907857994006) (by [@minchoi](https://x.com/minchoi))

**リンク付きまとめから具体的な成果物を見つけ、個別に検証します**

作者はGame Boy Advanceエミュレーターを含む、メディア付き事例10件をまとめています。単一の再現可能な手順ではないため、各リンク先を個別に確認する必要があります

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-28.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-28-poster.jpg" alt="Case 28 source video poster" height="360"></a>

[Play case 28 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-28.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-29"></a>
### Case 29: [高度なランディングページを4モデルで比較する](https://x.com/doutorcaleb/status/2077904020471947773) (by [@doutorcaleb](https://x.com/doutorcaleb))

**要件を固定し、モデル出力間でアニメーションの深さと完成度を確認します**

作者はKimi K3、Fable、Grok、GPT Terraに同じ高度なプロンプトを与え、Kimi K3を最も良いと評価しています。1課題の自己申告比較です

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-29.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-29-poster.jpg" alt="Case 29 source video poster" height="360"></a>

[Play case 29 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-29.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-30"></a>
### Case 30: [レトロゲームの仕組みと費用をベンチマークする](https://x.com/adxtyahq/status/2077860500462055570) (by [@adxtyahq](https://x.com/adxtyahq))

**同じ課題でプレイ、物理、仕組み、自律動作、トークン使用量、費用を比較します**

ソースはRoad Fighter、Battle City、Q*bertを同じプロンプトで試し、Kimi K3を0.28ドル、GPT-5.6を0.28ドル、Opus 4.8を0.54ドルと報告しています。公開元の数値です

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-30.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-30-poster.jpg" alt="Case 30 source video poster" height="360"></a>

[Play case 30 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-30.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-31"></a>
### Case 31: [Fable 5とゲーム生成を比較する](https://x.com/higgsfield_ai/status/2077943629633712490) (by [@higgsfield_ai](https://x.com/higgsfield_ai))

**生成ゲームの並列例を、モデル全般の結論ではなく狭い範囲の評価として使います**

HiggsfieldはKimi K3とFable 5の比較を提示しています。メディアはありますが、プロンプト、採点基準、詳細条件はありません

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-31.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-31-poster.jpg" alt="Case 31 source video poster" height="360"></a>

[Play case 31 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-31.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-34"></a>
### Case 34: [複雑なフロントエンドと開発課題をOpus 4.8と比較する](https://x.com/op7418/status/2077969583018066116) (by [@op7418](https://x.com/op7418))

**複数の複雑な課題で勝敗を確認し、一方を普遍的に優れているとは断定しません**

レビュー担当者は直接比較し、勝敗は混在するものの概ね同等と評価しています。1人のレビュー担当者による評価です

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-34.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-34-poster.jpg" alt="Case 34 source video poster" height="360"></a>

[Play case 34 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-34.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-35"></a>
### Case 35: [ベンチマークとランディングページテストをレビューする](https://x.com/adamuchigabriel/status/2077880433925120471) (by [@adamuchigabriel](https://x.com/adamuchigabriel))

**ベンチマーク文脈と具体的テストを組み合わせつつ、2種類の証拠を分けて扱います**

動画はベンチマーク議論、ランディングページテスト、フロントエンド所見を提示しています。完全なテストプロンプトや採点基準はありません

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-35.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-35-poster.jpg" alt="Case 35 source video poster" height="360"></a>

[Play case 35 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-35.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-37"></a>
### Case 37: [グラフから論理式を導く課題で帰納推論を評価する](https://x.com/s_batzoglou/status/2077884096307454119) (by [@s_batzoglou](https://x.com/s_batzoglou))

**一階論理の帰納課題で正答率、ホールドアウト挙動、論理式の複雑さを測定します**

作者はICML INDUCTION課題で、それぞれ8〜10要素を持つ6〜10個の小規模グラフから一階論理式を推論させたと報告しています。以前の研究からの更新で、ここでは独立再現を主張しません

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-37-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-37-01.png" alt="Case 37 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-16

---

<a id="case-38"></a>
### Case 38: [報告されたゲーム、ランディングページ、3D、長文脈をレビューする](https://x.com/servasyy_ai/status/2077903775113834689) (by [@servasyy_ai](https://x.com/servasyy_ai))

**複数ソースのまとめで成果物を比較し、費用主張と速度制約を記録します**

作者は複数領域の報告済みテストをまとめ、試す価値はあるがFable 5の代替にはまだならないと結論しています。数値は二次報告です

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-38-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-38-01.jpg" alt="Case 38 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-40"></a>
### Case 40: [複雑な計画を監査して改善策に異議を唱える](https://x.com/doodlestein/status/2077901883637665958) (by [@doodlestein](https://x.com/doodlestein))

**第2のモデルで過小評価された指摘、誤った改善策、退けるべき結論を特定します**

作者はKimi K3が重大問題の過小評価を見つけ、提案改善策の約3分の1に修正が必要で、1つの指摘を否定したと報告しています。特定の監査結果です

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-40-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-40-01.jpg" alt="Case 40 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-41"></a>
### Case 41: [PPO型強化学習のASCII図を比較する](https://x.com/dejavucoder/status/2077872015856615541) (by [@dejavucoder](https://x.com/dejavucoder))

**ASCII図のプロンプトを固定し、各モデルが強化学習ループをどう表現するか比較します**

ソースはPPO型強化学習ループをASCIIで描くプロンプトを公開し、Kimi K3 MaxとFable 5 Highを並べています。1課題の視覚比較です

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-01.png" alt="Case 41 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-02.jpg" alt="Case 41 source image 2" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-42"></a>
### Case 42: [容量エラーを記録しながらBlenderでモデリングする](https://x.com/Angaisb_/status/2077910845523214668) (by [@Angaisb_](https://x.com/Angaisb_))

**成果物だけでなくBlenderの部分的進捗とサービス信頼性を合わせて評価します**

作者はモデリング進捗と、繰り返す容量エラーを報告しています。作業は未完了なので部分結果と信頼性制約を合わせて考慮します

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-42-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-42-01.jpg" alt="Case 42 source image 1" height="360"></a>

Type: Limit | Date: 2026-07-17

---

<a id="case-47"></a>
### Case 47: [ArenaでFlappy Bird生成を比較する](https://x.com/jun_song/status/2077396996865003739) (by [@jun_song](https://x.com/jun_song))

**Arena課題で2つの生成結果を比較し、判断をその課題だけに限定します**

作者はKimi K3とOpus 4.8を比較し、Kimi K3が大幅に良かったと評価しています。完全なプロンプトや基準はありません

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-47.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-47-poster.jpg" alt="Case 47 source video poster" height="360"></a>

[Play case 47 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-47.mp4)

Type: Evaluation | Date: 2026-07-15

---

<a id="case-52"></a>
### Case 52: [ツールを使ってBongard視覚帰納問題を解く](https://x.com/IntuitMachine/status/2077885406528311561) (by [@IntuitMachine](https://x.com/IntuitMachine))

**ツール利用がBongard推論課題の視覚規則導出に役立つか試します**

作者は同じ比較でGrok 4.5とMuse Spark 1.1が解けなかった問題をKimi K3がツールで解いたと報告しています。一般ベンチマークではなく1利用者の結果です

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-52-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-52-01.jpg" alt="Case 52 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-53"></a>
### Case 53: [フロントエンドの美的感覚と3DデザインをGPT-5.6 Solと比較する](https://x.com/filicroval/status/2077736407506751952) (by [@filicroval](https://x.com/filicroval))

**限定的な比較で機能、視覚的な好み、洗練度、3D表現を確認します**

作者はKimi K3を視覚的な好み、洗練度、3D能力で高く評価しています。主観的かつ課題固有の評価です

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-53.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-53-poster.jpg" alt="Case 53 source video poster" height="360"></a>

[Play case 53 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-53.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-57"></a>
### Case 57: [3モデルのウェブサイト生成を比較する](https://x.com/pengchujin/status/2077962916226298340) (by [@pengchujin](https://x.com/pengchujin))

**可視化された出力を使い、1テストでKimi K3、Fable 5、GPT-5.6 Solを比較します**

作者は3モデルの比較を提示しています。完全なプロンプトや採点基準はありません

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-57.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-57-poster.jpg" alt="Case 57 source video poster" height="360"></a>

[Play case 57 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-57.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-59"></a>
### Case 59: [手続き型3Dゲーム生成と費用を比較する](https://x.com/adxtyahq/status/2077958193511362856) (by [@adxtyahq](https://x.com/adxtyahq))

**プロンプトを固定し、ルーレット、スロット、ピンボールと各実行費用を確認します**

公開元は複数モデル比較でKimi K3を0.71ドル、Grok 4.5を0.30ドルなどと報告しています。順位と費用は公開元の実行結果です

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-59.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-59-poster.jpg" alt="Case 59 source video poster" height="360"></a>

[Play case 59 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-59.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-69"></a>
### Case 69: [3D兵器庫シーンの密度と照明を比較する](https://x.com/hakki_alkan/status/2077887013332636032) (by [@hakki_alkan](https://x.com/hakki_alkan))

**限定的なKimi K3とOpus 4.8の比較で、物体密度、照明、シーン詳細を確認します**

ソースはKimi K3が商品棚、箱、現実的な照明を備えた詳細な兵器庫を、Opus 4.8が疎な部屋を生成したと報告しています。独立ベンチマークではなく第三者報告です

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-69-poster.jpg" alt="Case 69 source video poster" height="360"></a>

[Play case 69 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-69.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-72"></a>
### Case 72: [同一Arenaプロンプトでフロントエンドを比較](https://x.com/arena/status/2078240399517524365) (by [@arena](https://x.com/arena))

**同じプロンプトと並列出力で比較し、単一のランキング値への依存を避けます**

Arena.aiは同一プロンプトでKimi K3とFable 5を比較するFrontend Code Arena動画を公開し、実装と表現の違いを同じ条件で確認できるようにしています

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-72.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-72-poster.jpg" alt="Case 72 source video poster" height="360"></a>

[Play case 72 comparison video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-72.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-74"></a>
### Case 74: [Kimi Codeをコーディングエージェントで評価](https://x.com/ArtificialAnlys/status/2078230240766345330) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**複数のテスト群とタスク単価でKimi K3を評価し、フロントエンド順位だけを総合能力と見なしません**

Artificial AnalysisはCoding Agent Indexで57点、同率5位と報告しています。Terminal-Bench v2は84%、DeepSWEは64%、SWE-Atlas-QnAは23%、平均費用は1タスク3.18ドルです

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-74.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-74.jpg" alt="Case 74 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-17

---

<a id="case-76"></a>
### Case 76: [Arenaと修復ハーネスの結果を比較](https://x.com/AlphaSignalAI/status/2078172629496746183) (by [@AlphaSignalAI](https://x.com/AlphaSignalAI))

**Kimi K3が一方で1位、別の評価で7位になり得るため、フロントエンド選好とリポジトリ修復の両方を見ます**

AlphaSignalはFrontend Code Arenaで1679点の1位と報告する一方、7モデルの修復ハーネスでは67試行中53件、79%で7位だったと報告しています

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-76.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-76.jpg" alt="Case 76 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-17

---

<a id="case-80"></a>
### Case 80: [PrinzbenchでKimi K3をベンチマークする](https://x.com/deredleritt3r/status/2078606700496773166) (by [@deredleritt3r](https://x.com/deredleritt3r))

**PrinzbenchでKimi K3をOpenAI o3などと比較し、同じ評価ベンチでの順位と限界を示す。**

投稿はKimi K3をPrinzbenchの比較表に入れ、トップ層モデルとの差と、評価タスクにおける相対的な強みを公開している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-80-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-80-01.png" alt="Case 80 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-18

---

<a id="case-85"></a>
### Case 85: [ISSデジタルツイン生成を比較する](https://x.com/AIsaOneHQ/status/2078519527588200536) (by [@AIsaOneHQ](https://x.com/AIsaOneHQ))

**ISSデジタルツイン生成タスクでKimi K3と他モデルを比較し、複雑な3D/科学ビジュアルでの出力差を示す。**

投稿は同じISSデジタルツイン課題に対する複数モデルの結果を比較しており、Kimi K3の構造把握とビジュアル生成の限界を確認できる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-85.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-85-poster.jpg" alt="Case 85 source video poster" height="360"></a>

[Play case 85 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-85.mp4)

Type: Benchmark | Date: 2026-07-18

---

<a id="case-89"></a>
### Case 89: [WebGPUの森ワールドをレビューする](https://x.com/stas_sorokin_/status/2078435840728908093) (by [@stas_sorokin_](https://x.com/stas_sorokin_))

**Kimi K3生成のWebGPU森ワールドを評価し、没入型3Dシーンでの表現力と限界を示す。**

投稿はブラウザ内で動く森の3D環境を映像で示し、Kimi K3のWebGPU/3Dシーン生成の実用性を評価する材料になる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-89.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-89-poster.jpg" alt="Case 89 source video poster" height="360"></a>

[Play case 89 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-89.mp4)

Type: Evaluation | Date: 2026-07-18

---

<a id="case-90"></a>
### Case 90: [ガラスハウスのプロンプト比較](https://x.com/RoundtableSpace/status/2079004612070416755) (by [@RoundtableSpace](https://x.com/RoundtableSpace))

**同じ建築シーンのプロンプトで Kimi K3 と Opus 4.8 の雰囲気、照明、空間の完成度を比較する。**

Roundtable Space は、ほぼ同じ価格帯で Kimi K3 と Claude Opus 4.8 に同一プロンプトを与えた比較を報告している。Kimi の出力はブルーアワーのガラスハウス、暖かい室内光、反射するプール、設計図のディテールとして説明され、Opus はよりタイポグラフィ寄りで空間性が弱いとされている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-90.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-90-poster.jpg" alt="Case 90 source video poster" height="360"></a>

[Play case 90 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-90.mp4)

Type: Evaluation | Date: 2026-07-20

---

<a id="case-92"></a>
### Case 92: [ボクセルサッカー得点を評価](https://x.com/0xzynex/status/2078920667542487230) (by [@0xzynex](https://x.com/0xzynex))

**同じ純粋な HTML/CSS/JS のサッカーアニメーションプロンプトを二つのモデルで走らせ、動きの品質とコストを比較する。**

0xzynex は、Kimi K3 と GPT-5.6 Sol High にブロック風サッカーのドリブル、ゴール、動的カメラ、祝福演出をブラウザコードで作らせた一発比較を報告している。投稿では Kimi の方が滑らかで低コストだったとされ、動画が比較成果物を保存している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-92.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-92-poster.jpg" alt="Case 92 source video poster" height="360"></a>

[Play case 92 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-92.mp4)

Type: Benchmark | Date: 2026-07-19

---

<a id="case-93"></a>
### Case 93: [Minecraft ベンチを確認](https://x.com/ashen_one/status/2078892418976666071) (by [@ashen_one](https://x.com/ashen_one))

**ローンチ時の評判や価格だけを根拠にせず、構造化された Minecraft レビューを確認する。**

ashen_one は Kimi K3 の録画レビューを公開し、期待と現実、ベンチマーク、価格、Minecraft テスト、初回実行バグ、最終判断の章を含めている。ベンチマークの枠組みと初期信頼性の注意点を一つの動画で確認できる点が有用である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-93.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-93-poster.jpg" alt="Case 93 source video poster" height="360"></a>

[Play case 93 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-93.mp4)

Type: Benchmark | Date: 2026-07-19

---

<a id="case-98"></a>
### Case 98: [API tier 制限を測る](https://x.com/mnmn94253156337/status/2078739859154620497) (by [@mnmn94253156337](https://x.com/mnmn94253156337))

**Kimi K3 の agent 実行は、見出し価格だけでなく token、tier、TPM、TPD に基づいて予算化する。**

中国語のソースは、5ドルをチャージして Kimi K3 API を軽く試し、セットアップ中に約1.1ドルが消費され、その後 Tier0 制限に達した個人体験を報告している。入力、キャッシュ入力、出力価格と TPM/TPD などの制限概念が挙げられ、初期の制約レポートとして有用である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-98.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-98-poster.jpg" alt="Case 98 source video poster" height="360"></a>

[Play case 98 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-98.mp4)

Type: Limit | Date: 2026-07-19

---

<a id="case-99"></a>
### Case 99: [Limbo 風 demo を比較](https://x.com/ChrisGPT/status/2078679211116835017) (by [@ChrisGPT](https://x.com/ChrisGPT))

**同じゲーム試作で Kimi K3 と Fable 5 を比べ、遊べる範囲、仕上がり、コスト、バグを見る。**

ChrisGPT は Limbo クローン demo で Fable 5 と Kimi K3 を比較している。Fable は2,400行、24K output token、1.20ドル、Kimi は3,000行、30K output token、0.12ドルとされ、Kimi は gameplay を多く追加した一方でバグも多かった。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-99.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-99-poster.jpg" alt="Case 99 source video poster" height="360"></a>

[Play case 99 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-99.mp4)

Type: Benchmark | Date: 2026-07-19

---

<a id="case-100"></a>
### Case 100: [VulcanBenchのコスト結果を確認](https://x.com/morganlinton/status/2079358902194569357) (by [@morganlinton](https://x.com/morganlinton))

**この事例で、Kimi K3の「VulcanBenchのコスト結果を確認」における実ワークフロー、コスト、または制約を確認できます。**

元投稿は「VulcanBenchのコスト結果を確認」に関する公開証拠を示し、作者の説明、結果メディア、またはベンチマーク/チュートリアル情報を含みます。このリポジトリは検証可能な事実だけを残し、未公開のpromptや手順は補いません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-100-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-100-01.jpg" alt="Case 100 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-21

---

<a id="case-104"></a>
### Case 104: [二重振り子物理を評価](https://x.com/AlicanKiraz0/status/2079241239736504768) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**この事例で、Kimi K3の「二重振り子物理を評価」における実ワークフロー、コスト、または制約を確認できます。**

元投稿は「二重振り子物理を評価」に関する公開証拠を示し、作者の説明、結果メディア、またはベンチマーク/チュートリアル情報を含みます。このリポジトリは検証可能な事実だけを残し、未公開のpromptや手順は補いません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-104.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-104-poster.jpg" alt="Case 104 source video poster" height="360"></a>

[Play case 104 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-104.mp4)

Type: Benchmark | Date: 2026-07-20

---

<a id="case-107"></a>
### Case 107: [ReactBenchの実運用度を確認](https://x.com/aidenybai/status/2079233934693650567) (by [@aidenybai](https://x.com/aidenybai))

**この事例で、Kimi K3の「ReactBenchの実運用度を確認」における実ワークフロー、コスト、または制約を確認できます。**

元投稿は「ReactBenchの実運用度を確認」に関する公開証拠を示し、作者の説明、結果メディア、またはベンチマーク/チュートリアル情報を含みます。このリポジトリは検証可能な事実だけを残し、未公開のpromptや手順は補いません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-107.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-107-poster.jpg" alt="Case 107 source video poster" height="360"></a>

[Play case 107 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-107.mp4)

Type: Benchmark | Date: 2026-07-20

---

<a id="related-resources"></a>
## 関連リソース

- [EvoLinkでKimi K3の詳細と料金を見る](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=landing_overview)
- [EvoLinkのKimi K3 API文書を開く](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=docs_link)
- [EvoLinkでKimi K3の詳細を確認](https://evolink.ai/blog/is-kimi-k3-available-on-evolink?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_article)
- [KimiK3.io](https://kimik3.io/)
- EvoLinkのモデルページとAPI文書は確認済みですが、インストール可能なKimi K3 skillは未確認です

<a id="acknowledge"></a>
## 🙏 謝辞

Kimi K3の成果を公開した皆さまに感謝します

[@ivanfioravanti](https://x.com/ivanfioravanti), [@TheAhmadOsman](https://x.com/TheAhmadOsman), [@HarshithLucky3](https://x.com/HarshithLucky3), [@chetaslua](https://x.com/chetaslua), [@abhinavflac](https://x.com/abhinavflac), [@bridgemindai](https://x.com/bridgemindai), [@Whats_AI](https://x.com/Whats_AI), [@chongdashu](https://x.com/chongdashu), [@MrAhmadAwais](https://x.com/MrAhmadAwais), [@bijanbowen](https://x.com/bijanbowen), [@CommandCodeAI](https://x.com/CommandCodeAI), [@emollick](https://x.com/emollick), [@nicky_sap](https://x.com/nicky_sap), [@Lentils80](https://x.com/Lentils80), [@scottstts](https://x.com/scottstts), [@aisearchio](https://x.com/aisearchio), [@gmi_cloud](https://x.com/gmi_cloud), [@karminski3](https://x.com/karminski3), [@VORTEX_Promos](https://x.com/VORTEX_Promos), [@rohanpaul_ai](https://x.com/rohanpaul_ai), [@mirochill](https://x.com/mirochill), [@aimlapi](https://x.com/aimlapi), [@minchoi](https://x.com/minchoi), [@doutorcaleb](https://x.com/doutorcaleb), [@adxtyahq](https://x.com/adxtyahq), [@higgsfield_ai](https://x.com/higgsfield_ai), [@AlicanKiraz0](https://x.com/AlicanKiraz0), [@1littlecoder](https://x.com/1littlecoder), [@op7418](https://x.com/op7418), [@adamuchigabriel](https://x.com/adamuchigabriel), [@s_batzoglou](https://x.com/s_batzoglou), [@servasyy_ai](https://x.com/servasyy_ai), [@filicroval](https://x.com/filicroval), [@doodlestein](https://x.com/doodlestein), [@dejavucoder](https://x.com/dejavucoder), [@Angaisb_](https://x.com/Angaisb_), [@AngryTomtweets](https://x.com/AngryTomtweets), [@Alezander907](https://x.com/Alezander907), [@teortaxesTex](https://x.com/teortaxesTex), [@jun_song](https://x.com/jun_song), [@ridark_eth](https://x.com/ridark_eth), [@naymur_dev](https://x.com/naymur_dev), [@tphuang](https://x.com/tphuang), [@TokenGremlin](https://x.com/TokenGremlin), [@IntuitMachine](https://x.com/IntuitMachine), [@wangfeng0315](https://x.com/wangfeng0315), [@twid](https://x.com/twid), [@pengchujin](https://x.com/pengchujin), [@aayushman2703](https://x.com/aayushman2703), [@goncalo_canhoto](https://x.com/goncalo_canhoto), [@LinearUncle](https://x.com/LinearUncle), [@gagarot200](https://x.com/gagarot200), [@MinLiBuilds](https://x.com/MinLiBuilds), [@izutorishima](https://x.com/izutorishima), [@X2worldtech](https://x.com/X2worldtech), [@Satvik_Pen](https://x.com/Satvik_Pen), [@hakki_alkan](https://x.com/hakki_alkan), [@BrianMRey](https://x.com/BrianMRey), [@ChrisGPT](https://x.com/ChrisGPT), [@arena](https://x.com/arena), [@MathiasHeide](https://x.com/MathiasHeide), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@nauczymycieAI](https://x.com/nauczymycieAI), [@AlphaSignalAI](https://x.com/AlphaSignalAI), [@Ananth7e](https://x.com/Ananth7e), [@viktoroddy](https://x.com/viktoroddy), [@abacusai](https://x.com/abacusai), [@deredleritt3r](https://x.com/deredleritt3r), [@fabriciocarraro](https://x.com/fabriciocarraro), [@startracker](https://x.com/startracker), [@mattwatkajtys](https://x.com/mattwatkajtys), [@AIsaOneHQ](https://x.com/AIsaOneHQ), [@MiaAI_lab](https://x.com/MiaAI_lab), [@hqmank](https://x.com/hqmank), [@prasenx](https://x.com/prasenx), [@stas_sorokin_](https://x.com/stas_sorokin_), [@RoundtableSpace](https://x.com/RoundtableSpace), [@karankendre](https://x.com/karankendre), [@0xzynex](https://x.com/0xzynex), [@ashen_one](https://x.com/ashen_one), [@MAXdeg0](https://x.com/MAXdeg0), [@ice_bearcute](https://x.com/ice_bearcute), [@mnmn94253156337](https://x.com/mnmn94253156337), [@morganlinton](https://x.com/morganlinton), [@vikktorrrre](https://x.com/vikktorrrre), [@kirillk_web3](https://x.com/kirillk_web3), [@_guillecasaus](https://x.com/_guillecasaus), [@demian_ai](https://x.com/demian_ai), [@aidenybai](https://x.com/aidenybai), [@LexnLin](https://x.com/LexnLin), [@boxmining](https://x.com/boxmining)

*帰属や記述の訂正は公開ソースを添えてissueを作成してください*
