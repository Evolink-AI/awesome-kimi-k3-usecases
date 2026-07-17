<div align="center">

<a href="https://evolink.ai/kimi-k3?utm_source=github&utm_medium=banner&utm_campaign=awesome-kimi-k3-usecases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/images/ja.png" alt="Kimi K3 usecase repository banner" width="760"></a>

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

# Kimi K3 活用事例集

## 🍌 はじめに

Kimi K3 の実例を厳選したリポジトリです

**公開情報に基づくゲーム、3D、モーションデザイン、統合、評価、実用上の制約を収録します**

初版の10件は提供されたソースパッケージのみから選定し、タイトルと著者名から原典へ移動できます

[EvoLink](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=introduction_cta)

## 📊 概要

- クリエイターと実務家による10件の事例
- ゲーム、Three.js、モーション、CLI、速度、ビジョン、エージェント制約を収録
- 各事例で出典、著者、種別、日付、プロンプト境界を保持
- 個人の報告をベンチマークとして扱いません

> [!NOTE]
> 具体的な証拠を優先し、未公開のプロンプトや手順を補完しません

## ⚡ クイックスタート

EvoLinkの文書化されたモデルIDは `kimi-k3` で、モデルページとChat Completions API文書が利用できます

1. [EvoLinkでKimi K3の詳細と料金を見る](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-kimi-k3-usecases&utm_content=model_link)
2. [EvoLink APIキーを作成・管理](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-kimi-k3-usecases&utm_content=api_key)
3. [EvoLinkのKimi K3 API文書を開く](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=first_run)

> [!IMPORTANT]
> EvoLinkのモデルページとAPI文書が公開ルートとIDを確認しています。本リポジトリは独自の有料APIテストを主張しません

## 📑 目次

| Section | Cases |
|---|---|
| [インタラクティブゲームと3D](#games-3d) | 4 |
| [フロントエンドとモーションデザイン](#frontend-motion) | 2 |
| [コーディングと統合](#coding-integrations) | 2 |
| [評価と制約](#evaluation-limits) | 2 |
| [謝辞](#acknowledge) | 謝辞と訂正 |

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

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01-poster.jpg" alt="Case 1 video poster" height="360"></a>

[Play case 1 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-2"></a>
### Case 2: [同じプロンプトでFroggerを比較する](https://x.com/ivanfioravanti/status/2077754781964054825) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**プロンプトを固定してモデル間の差を確認します**

作者は同一プロンプト比較としてKimi K3版を公開しましたが、プロンプト本文と評価基準は未公開です

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02-poster.jpg" alt="Case 2 video poster" height="360"></a>

[Play case 2 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-3"></a>
### Case 3: [Froggerと録画を生成する](https://x.com/TheAhmadOsman/status/2077776567292338285) (by [@TheAhmadOsman](https://x.com/TheAhmadOsman))

**ゲームとプレイ録画の両方をワンショットで試します**

作者はゲームと録画工程をそれぞれ一度で生成したと報告しています。正確なプロンプトはありません

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03-poster.jpg" alt="Case 3 video poster" height="360"></a>

[Play case 3 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-4"></a>
### Case 4: [Three.jsで空母を試作する](https://x.com/HarshithLucky3/status/2077753222018814360) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**具体的な発着艦シーンで対話型3D生成を試します**

作者はニミッツ級空母での戦闘機の発艦と回収を示し、3D生成を高く評価しています

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04-poster.jpg" alt="Case 4 video poster" height="360"></a>

[Play case 4 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04.mp4)

Type: Demo | Date: 2026-07-16

---


<a id="frontend-motion"></a>
## 🎨 フロントエンドとモーションデザイン

<a id="case-5"></a>
### Case 5: [対話できるモーショングラフィックを作る](https://x.com/chetaslua/status/2077749371144442022) (by [@chetaslua](https://x.com/chetaslua))

**停止中も操作できるグラフィックをワンショットで構築します**

作者は42分、単純なコード、harness・MCP・skillなしの一回生成と報告しています

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05-poster.jpg" alt="Case 5 video poster" height="360"></a>

[Play case 5 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-6"></a>
### Case 6: [同期したモーション広告を作る](https://x.com/abhinavflac/status/2077760297918484667) (by [@abhinavflac](https://x.com/abhinavflac))

**音楽、効果、動きの同期を確認します**

作者はSpotify風広告をプロンプトだけで一回生成したと報告していますが、正確なプロンプトは未公開です

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06-poster.jpg" alt="Case 6 video poster" height="360"></a>

[Play case 6 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06.mp4)

Type: Demo | Date: 2026-07-16

---


<a id="coding-integrations"></a>
## 💻 コーディングと統合

<a id="case-7"></a>
### Case 7: [Kimi CLIからKimi K3を使う](https://x.com/TheAhmadOsman/status/2077750074608644127) (by [@TheAhmadOsman](https://x.com/TheAhmadOsman))

**最新の文書とモデル選択を確認してCLIを使います**

作者はKimi CLIでの提供を告知しています。本リポジトリは導入や認証手順を推測しません

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-07.jpg" alt="Case 7 source media" height="360">

Type: Integration | Date: 2026-07-16

---

<a id="case-8"></a>
### Case 8: [Moonshot API経由の速度を観測する](https://x.com/scaling01/status/2077777932341092422) (by [@scaling01](https://x.com/scaling01))

**プロバイダー、経路、毎秒トークン数を記録します**

利用者1名が毎秒28トークンを報告しています。単一観測であり、ベンチマークや保証ではありません

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-08.jpg" alt="Case 8 source media" height="360">

Type: Evaluation | Date: 2026-07-16

---


<a id="evaluation-limits"></a>
## 🧪 評価と制約

<a id="case-9"></a>
### Case 9: [自分の業務でビジョンを試す](https://x.com/mitsuhiko/status/2077770239937282526) (by [@mitsuhiko](https://x.com/mitsuhiko))

**代表的な作業で評価してから一般化します**

Armin Ronacherは自身の作業で高い視覚品質を報告しました。個人的な観測でありベンチマークではありません

Type: Evaluation | Date: 2026-07-16

---

<a id="case-10"></a>
### Case 10: [最大努力時のループを監視する](https://x.com/emollick/status/2077770187521069152) (by [@emollick](https://x.com/emollick))

**完了済み作業を再訪する場合は停止条件を設けます**

Ethan Mollickは反復修正を報告しました。原因がモデル、harness、相互作用のどれかは分離されていません

Type: Limit | Date: 2026-07-16

---

## 関連リソース

- [EvoLinkでKimi K3の詳細と料金を見る](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_model)
- [EvoLinkのKimi K3 API文書を開く](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_api_docs)
- EvoLinkのモデルページとAPI文書は確認済みですが、インストール可能なKimi K3 skillは未確認です

<a id="acknowledge"></a>
## 🙏 謝辞

Kimi K3の成果を公開した皆さまに感謝します

- [@ivanfioravanti](https://x.com/ivanfioravanti)
- [@TheAhmadOsman](https://x.com/TheAhmadOsman)
- [@HarshithLucky3](https://x.com/HarshithLucky3)
- [@chetaslua](https://x.com/chetaslua)
- [@abhinavflac](https://x.com/abhinavflac)
- [@scaling01](https://x.com/scaling01)
- [@mitsuhiko](https://x.com/mitsuhiko)
- [@emollick](https://x.com/emollick)

帰属や記述の訂正は公開ソースを添えてissueを作成してください
