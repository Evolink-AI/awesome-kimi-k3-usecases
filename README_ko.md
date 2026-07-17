<div align="center">

<a href="https://evolink.ai/kimi-k3?utm_source=github&utm_medium=banner&utm_campaign=awesome-kimi-k3-usecases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/images/ko-v2.png" alt="달 표면과 EvoLink 사용 안내가 포함된 한국어 Kimi K3 배너" width="760"></a>

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

# Kimi K3 활용 사례

## 🍌 소개

Kimi K3의 근거가 분명한 활용 사례를 모은 저장소입니다

**공개 출처에 기반한 게임, 3D, 모션 디자인, 통합, 평가와 실무적 한계를 수집합니다**

제공된 소스 패키지에서 high-confidence로 분류된 사례 70개를 모두 포함하고 medium-confidence 사례 31개는 제외했으며 제목과 작성자 링크는 원문으로 연결됩니다

[EvoLink](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=introduction_cta)

## 📊 개요

- 크리에이터와 실무자의 high-confidence 사례 70개 전체 수록
- 게임, 3D, 프론트엔드, 모션, 코딩, 연구, 평가와 한계를 폭넓게 다룸
- 각 사례에 출처, 작성자, 유형, 날짜와 프롬프트 경계 보존
- 개인 경험을 벤치마크로 일반화하지 않음

> [!NOTE]
> 구체적인 증거를 우선하며 공개되지 않은 프롬프트나 설정을 재구성하지 않습니다

## ⚡ 빠른 시작

EvoLink에 문서화된 모델 ID는 `kimi-k3`이며 모델 페이지와 Chat Completions API 문서를 이용할 수 있습니다

1. [EvoLink에서 Kimi K3 세부 정보와 가격 보기](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-kimi-k3-usecases&utm_content=model_link)
2. [EvoLink API 키 생성 또는 관리](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-kimi-k3-usecases&utm_content=api_key)
3. [EvoLink Kimi K3 API 문서 열기](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=first_run)

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
> EvoLink 모델 페이지와 API 문서가 공개 경로와 ID를 확인합니다. 이 저장소는 독립적인 유료 API 테스트를 주장하지 않습니다

## 📑 메뉴

| Section | Cases |
|---|---|
| [인터랙티브 게임과 3D](#games-3d) | 22 |
| [프론트엔드와 모션 디자인](#frontend-motion) | 15 |
| [코딩과 통합](#coding-integrations) | 8 |
| [평가와 한계](#evaluation-limits) | 25 |
| [감사의 말](#acknowledge) | 감사와 수정 |

<a id="games-3d"></a>
## 🎮 인터랙티브 게임과 3D

| Case | What it shows | Type |
|---|---|---|
| [하나의 프롬프트로 복셀 레이서 만들기](#case-1) | 짧은 장면 아이디어로 레이싱 프로토타입을 만들고 다음 개선 범위를 정합니다 | Demo |
| [같은 프롬프트로 Frogger 비교하기](#case-2) | 프롬프트를 고정해 모델 출력 차이를 살펴봅니다 | Evaluation |
| [Frogger와 플레이 녹화 생성하기](#case-3) | 게임과 녹화 흐름을 각각 원샷으로 시험합니다 | Demo |
| [Three.js 항공모함 프로토타입 만들기](#case-4) | 구체적인 이착함 장면으로 인터랙티브 3D 생성을 시험합니다 | Demo |
| [에이전트 도구로 Paper Mario풍 게임 만들기](#case-9) | Kimi K3를 에이전트 harness와 에셋 도구에 결합해 2D와 3D 게임 요소를 모두 만듭니다 | Demo |
| [지하철 배경의 1인칭 슈팅 게임 생성하기](#case-11) | 구체적인 지하철 배경으로 생성된 1인칭 슈팅 결과를 살펴봅니다 | Demo |
| [Blender MCP로 V8 엔진 모델링하기](#case-19) | Blender MCP와 하나의 요청을 사용해 세밀한 기계식 3D 모델을 생성합니다 | Integration |
| [참조 하나로 플레이 가능한 전투 아레나 만들기](#case-23) | 참조 하나를 사용해 완전한 플레이 가능 아레나의 원샷 생성을 시험합니다 | Demo |
| [스스로 플레이하는 레트로 게임 3개를 HTML 파일로 만들기](#case-24) | 독립형 HTML 게임 파일 안에 그래픽, 적, 규칙과 자율 플레이를 요구합니다 | Benchmark |
| [원샷 카멜레온 숨바꼭질 게임 만들기](#case-27) | 색상 맞추기, 절차적 구역, 소리와 여러 라운드 점수를 갖춘 단일 파일 게임을 생성합니다 | Benchmark |
| [에이전트 툴체인으로 2.5D Paper Mario풍 게임 만들기](#case-36) | Kimi K3를 Grok Build 또는 Claude Code, Spriterrific과 함께 사용해 2.5D 게임 워크플로를 구성합니다 | Tutorial |
| [브라우저 기반 3D 무협 RPG 만들기](#case-43) | 근접 전투, 퀘스트, 인벤토리, 날씨, 실내 공간, Blender 환경 작업과 수정된 에셋을 결합합니다 | Demo |
| [브라우저 멀티플레이 Minecraft풍 게임 만들기](#case-44) | 시간과 비용 범위를 정한 실행으로 플레이 가능한 온라인 멀티플레이 브라우저 게임을 만듭니다 | Demo |
| [화면 분할 협동 브라우저 게임 재현하기](#case-48) | 하나의 요청으로 브라우저 기반 화면 분할 협동과 실시간 환경 상호작용을 생성합니다 | Demo |
| [Command Code 디자인 모드로 플레이 가능한 게임 생성하기](#case-49) | Command Code의 디자인 명령으로 원샷 게임 빌드를 수행하고 결과가 플레이 가능한지 기록합니다 | Demo |
| [일관성 있는 무협 브라우저 RPG 조립하기](#case-51) | 이동, 전투, 퀘스트, 인벤토리, 날씨, 탐험과 3D 환경 작업을 하나의 게임에 통합합니다 | Demo |
| [플레이 가능한 Hollow Knight 크로스오버 만들기](#case-54) | 기존 게임 에셋을 사용해 Knight와 Kimi가 싸우는 플레이 가능한 전투를 만듭니다 | Demo |
| [원샷으로 Fall Guys풍 3D 브라우저 게임 만들기](#case-60) | 원샷 요청으로 플레이 가능한 3D 장애물 게임을 생성하고 프로젝트를 공개해 살펴볼 수 있게 합니다 | Demo |
| [종말 이후 Lisbon FPS 만들고 자체 시험하기](#case-61) | 한 번의 최대 effort 실행으로 플레이 가능한 FPS를 제공하기 전에 테스트, 스크린샷과 반복을 수행합니다 | Demo |
| [간단한 요청으로 Animal Crossing풍 게임 생성하기](#case-63) | 최소한의 게임 요구로 플레이 가능성, 게임플레이 루프와 패럴랙스 효과를 살펴봅니다 | Demo |
| [한 문장 요구로 Mario풍 게임 생성하기](#case-65) | 최소한의 원샷 요청으로 플레이 가능성, 스테이지 디자인, 픽셀 아트와 패럴랙스를 살펴봅니다 | Demo |
| [작동하는 좀비 1인칭 슈팅 게임 만들기](#case-67) | 구체적인 좀비 슈팅 목표로 완성된 플레이 가능 FPS 결과물을 살펴봅니다 | Demo |

<a id="case-1"></a>
### Case 1: [하나의 프롬프트로 복셀 레이서 만들기](https://x.com/ivanfioravanti/status/2077763009657627055) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**짧은 장면 아이디어로 레이싱 프로토타입을 만들고 다음 개선 범위를 정합니다**

제작자는 Kimi K3가 공개 프롬프트 하나로 첫 버전을 만들었고 이후 레이서, 결승선, 세부 검토를 추가할 계획이라고 말합니다

**Prompt:**

```text
Voxel star wars pod-racers run
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01-poster.jpg" alt="Case 1 video poster" height="360"></a>

[Play case 1 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-2"></a>
### Case 2: [같은 프롬프트로 Frogger 비교하기](https://x.com/ivanfioravanti/status/2077754781964054825) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**프롬프트를 고정해 모델 출력 차이를 살펴봅니다**

제작자는 동일 프롬프트 비교로 Kimi K3 버전을 공유했지만 프롬프트 본문과 평가 기준은 공개하지 않았습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02-poster.jpg" alt="Case 2 video poster" height="360"></a>

[Play case 2 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-3"></a>
### Case 3: [Frogger와 플레이 녹화 생성하기](https://x.com/TheAhmadOsman/status/2077776567292338285) (by [@TheAhmadOsman](https://x.com/TheAhmadOsman))

**게임과 녹화 흐름을 각각 원샷으로 시험합니다**

제작자는 게임과 녹화 흐름을 각각 한 번에 만들었다고 보고합니다. 정확한 프롬프트는 없습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03-poster.jpg" alt="Case 3 video poster" height="360"></a>

[Play case 3 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-4"></a>
### Case 4: [Three.js 항공모함 프로토타입 만들기](https://x.com/HarshithLucky3/status/2077753222018814360) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**구체적인 이착함 장면으로 인터랙티브 3D 생성을 시험합니다**

제작자는 니미츠급 항공모함의 전투기 발진과 회수 장면을 보여 주며 3D 생성을 높이 평가합니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04-poster.jpg" alt="Case 4 video poster" height="360"></a>

[Play case 4 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-9"></a>
### Case 9: [에이전트 도구로 Paper Mario풍 게임 만들기](https://x.com/chongdashu/status/2077886028866531655) (by [@chongdashu](https://x.com/chongdashu))

**Kimi K3를 에이전트 harness와 에셋 도구에 결합해 2D와 3D 게임 요소를 모두 만듭니다**

제작자는 Paper Mario풍 게임에 Kimi K3와 Grok Build, 2D 에셋용 Spriterrific, 3D 에셋용 geometry를 사용했다고 보고합니다. 출처는 도구와 skill 사용을 보여 주지만 재사용 가능한 정확한 프롬프트는 공개하지 않습니다

Type: Demo | Date: 2026-07-16

---

<a id="case-11"></a>
### Case 11: [지하철 배경의 1인칭 슈팅 게임 생성하기](https://x.com/bijanbowen/status/2077881805751873997) (by [@bijanbowen](https://x.com/bijanbowen))

**구체적인 지하철 배경으로 생성된 1인칭 슈팅 결과를 살펴봅니다**

제작자는 Kimi K3가 만든 것으로 표시된 지하철 FPS를 보여 주며 인플루언서 지위가 결과에 영향을 주었는지 확신할 수 없다고 명시합니다. 프롬프트나 재현 가능한 워크플로는 제공되지 않습니다

Type: Demo | Date: 2026-07-16

---

<a id="case-19"></a>
### Case 19: [Blender MCP로 V8 엔진 모델링하기](https://x.com/aisearchio/status/2077962156147146925) (by [@aisearchio](https://x.com/aisearchio))

**Blender MCP와 하나의 요청을 사용해 세밀한 기계식 3D 모델을 생성합니다**

리뷰어는 Kimi K3가 Blender MCP에서 하나의 프롬프트로 완전한 V8 엔진을 생성했다고 보고합니다. 게시물은 더 긴 리뷰로 연결되지만 제공된 기록에는 정확한 프롬프트가 공개되지 않습니다

Type: Integration | Date: 2026-07-17

---

<a id="case-23"></a>
### Case 23: [참조 하나로 플레이 가능한 전투 아레나 만들기](https://x.com/VORTEX_Promos/status/2077879705378730074) (by [@VORTEX_Promos](https://x.com/VORTEX_Promos))

**참조 하나를 사용해 완전한 플레이 가능 아레나의 원샷 생성을 시험합니다**

제작자는 Kimi K3가 하나의 참조에서 한 번에 플레이 가능한 전투 아레나를 만들었다고 보고합니다. 게시물에 별도 리더보드 주장도 있지만 구체적 활용 사례는 시연된 아레나 결과물입니다

Type: Demo | Date: 2026-07-16

---

<a id="case-24"></a>
### Case 24: [스스로 플레이하는 레트로 게임 3개를 HTML 파일로 만들기](https://x.com/rohanpaul_ai/status/2077889084761206860) (by [@rohanpaul_ai](https://x.com/rohanpaul_ai))

**독립형 HTML 게임 파일 안에 그래픽, 적, 규칙과 자율 플레이를 요구합니다**

출처는 모델들이 Road Fighter, Battle City, Q*bert를 스스로 플레이하는 HTML 파일로 만든 Atomic Chat 비교를 보고합니다. 비용과 품질 비교는 게시자가 보고한 것이며 여기서 독립적으로 재현하지 않았습니다

Type: Benchmark | Date: 2026-07-16

---

<a id="case-27"></a>
### Case 27: [원샷 카멜레온 숨바꼭질 게임 만들기](https://x.com/aimlapi/status/2077898742179459274) (by [@aimlapi](https://x.com/aimlapi))

**색상 맞추기, 절차적 구역, 소리와 여러 라운드 점수를 갖춘 단일 파일 게임을 생성합니다**

AIMLAPI는 숨바꼭질 게임을 같은 프롬프트로 한 번에 비교했다고 보고하며 Kimi K3 $3.11, Fable 5 $12.23의 비용을 제시합니다. 기능과 비용 주장은 공급자가 보고한 결과입니다

Type: Benchmark | Date: 2026-07-16

---

<a id="case-36"></a>
### Case 36: [에이전트 툴체인으로 2.5D Paper Mario풍 게임 만들기](https://x.com/chongdashu/status/2077981621223837739) (by [@chongdashu](https://x.com/chongdashu))

**Kimi K3를 Grok Build 또는 Claude Code, Spriterrific과 함께 사용해 2.5D 게임 워크플로를 구성합니다**

제작자는 Grok Build와 Kimi K3를 사용하는 전체 워크스루를 제공하고 Spriterrific을 통한 스프라이트 생성을 보여 줍니다. 출처는 도구를 밝히지만 재사용 가능한 정확한 프롬프트는 제공하지 않습니다

Type: Tutorial | Date: 2026-07-17

---

<a id="case-43"></a>
### Case 43: [브라우저 기반 3D 무협 RPG 만들기](https://x.com/AngryTomtweets/status/2077868163136450619) (by [@AngryTomtweets](https://x.com/AngryTomtweets))

**근접 전투, 퀘스트, 인벤토리, 날씨, 실내 공간, Blender 환경 작업과 수정된 에셋을 결합합니다**

출처는 근접 전투, 퀘스트, 인벤토리, 동적 날씨와 탐험 가능한 실내 공간을 갖춘 Kimi K3 브라우저 RPG를 보고하며 Blender 모델링, 충돌 개선, PBR 재텍스처링과 공개 에셋 수정도 포함한다고 설명합니다

Type: Demo | Date: 2026-07-16

---

<a id="case-44"></a>
### Case 44: [브라우저 멀티플레이 Minecraft풍 게임 만들기](https://x.com/Alezander907/status/2077926014710407407) (by [@Alezander907](https://x.com/Alezander907))

**시간과 비용 범위를 정한 실행으로 플레이 가능한 온라인 멀티플레이 브라우저 게임을 만듭니다**

제작자는 Kimi K3가 1시간 동안 $6.57의 비용으로 브라우저에서 플레이 가능한 멀티플레이 Minecraft풍 게임을 만들었다고 보고합니다. 이는 단일 결과물에서 자체 보고한 실행 수치입니다

Type: Demo | Date: 2026-07-17

---

<a id="case-48"></a>
### Case 48: [화면 분할 협동 브라우저 게임 재현하기](https://x.com/ridark_eth/status/2077882889803378969) (by [@ridark_eth](https://x.com/ridark_eth))

**하나의 요청으로 브라우저 기반 화면 분할 협동과 실시간 환경 상호작용을 생성합니다**

제작자는 Kimi K3가 하나의 프롬프트로 It Takes Two풍 브라우저 게임을 만들었으며 Mario와 Luigi가 화면 분할 상태에서 서로와 환경에 실시간으로 상호작용한다고 보고합니다

Type: Demo | Date: 2026-07-16

---

<a id="case-49"></a>
### Case 49: [Command Code 디자인 모드로 플레이 가능한 게임 생성하기](https://x.com/naymur_dev/status/2077873562661335207) (by [@naymur_dev](https://x.com/naymur_dev))

**Command Code의 디자인 명령으로 원샷 게임 빌드를 수행하고 결과가 플레이 가능한지 기록합니다**

제작자는 Command Code 디자인 모드로 원샷 비교를 수행했고 Kimi K3 실행이 $0.038에 플레이 가능한 게임을 만들었다고 보고합니다. 이 비용과 품질 결과는 자체 보고입니다

Type: Demo | Date: 2026-07-16

---

<a id="case-51"></a>
### Case 51: [일관성 있는 무협 브라우저 RPG 조립하기](https://x.com/TokenGremlin/status/2077855657068310620) (by [@TokenGremlin](https://x.com/TokenGremlin))

**이동, 전투, 퀘스트, 인벤토리, 날씨, 탐험과 3D 환경 작업을 하나의 게임에 통합합니다**

출처는 Kimi K3 무협 스타일 브라우저 RPG가 근접 전투, 퀘스트, 인벤토리, 동적 날씨, 탐험 가능한 실내 공간과 일관성 있는 3D 게임플레이 구조를 결합한다고 보고합니다

Type: Demo | Date: 2026-07-16

---

<a id="case-54"></a>
### Case 54: [플레이 가능한 Hollow Knight 크로스오버 만들기](https://x.com/wangfeng0315/status/2077933531200991583) (by [@wangfeng0315](https://x.com/wangfeng0315))

**기존 게임 에셋을 사용해 Knight와 Kimi가 싸우는 플레이 가능한 전투를 만듭니다**

Kimi에서 일한다고 밝힌 제작자는 Hollow Knight 에셋으로 Knight가 Kimi와 싸우는 게임을 만들고 공개 플레이 링크를 제공했다고 보고합니다. 출처와 평가에서 이 소속 관계를 고려해야 합니다

Type: Demo | Date: 2026-07-17

---

<a id="case-60"></a>
### Case 60: [원샷으로 Fall Guys풍 3D 브라우저 게임 만들기](https://x.com/aayushman2703/status/2077857886441783526) (by [@aayushman2703](https://x.com/aayushman2703))

**원샷 요청으로 플레이 가능한 3D 장애물 게임을 생성하고 프로젝트를 공개해 살펴볼 수 있게 합니다**

제작자는 Kimi K3로 Fall Guys풍 브라우저 게임을 한 번에 만들었으며 프롬프트와 GitHub 프로젝트가 출처에 연결되어 있다고 보고합니다. 이 기록은 해당 프롬프트를 재현하지 않습니다

Type: Demo | Date: 2026-07-16

---

<a id="case-61"></a>
### Case 61: [종말 이후 Lisbon FPS 만들고 자체 시험하기](https://x.com/goncalo_canhoto/status/2077863166655037668) (by [@goncalo_canhoto](https://x.com/goncalo_canhoto))

**한 번의 최대 effort 실행으로 플레이 가능한 FPS를 제공하기 전에 테스트, 스크린샷과 반복을 수행합니다**

제작자는 Kimi K3가 약 1시간 동안 반복적인 테스트, 스크린샷과 수정을 거쳐 플레이 가능한 종말 이후 Lisbon 브라우저 FPS를 만들었다고 보고합니다. 시간과 과정 세부 정보는 자체 보고입니다

Type: Demo | Date: 2026-07-16

---

<a id="case-63"></a>
### Case 63: [간단한 요청으로 Animal Crossing풍 게임 생성하기](https://x.com/gagarot200/status/2077949230287896830) (by [@gagarot200](https://x.com/gagarot200))

**최소한의 게임 요구로 플레이 가능성, 게임플레이 루프와 패럴랙스 효과를 살펴봅니다**

제작자는 Kimi K3가 매우 간단한 프롬프트에서 게임플레이 루프와 패럴랙스 효과를 갖춘 완전히 플레이 가능한 Animal Crossing풍 게임을 만들었다고 보고합니다. 정확한 문구는 제공된 기록에 없습니다

Type: Demo | Date: 2026-07-17

---

<a id="case-65"></a>
### Case 65: [한 문장 요구로 Mario풍 게임 생성하기](https://x.com/izutorishima/status/2077939370154475992) (by [@izutorishima](https://x.com/izutorishima))

**최소한의 원샷 요청으로 플레이 가능성, 스테이지 디자인, 픽셀 아트와 패럴랙스를 살펴봅니다**

제작자는 Kimi K3가 하나의 짧은 요구에서 뚜렷한 버그 없이 작동하는 Mario풍 게임을 만들었고 스테이지 구조와 패럴랙스도 포함했다고 보고합니다. 같은 보고는 음악과 그래픽 품질을 비판합니다

Type: Demo | Date: 2026-07-17

---

<a id="case-67"></a>
### Case 67: [작동하는 좀비 1인칭 슈팅 게임 만들기](https://x.com/X2worldtech/status/2077902793449296203) (by [@X2worldtech](https://x.com/X2worldtech))

**구체적인 좀비 슈팅 목표로 완성된 플레이 가능 FPS 결과물을 살펴봅니다**

출처는 Kimi K3가 만든 것으로 표시된 완전히 작동하는 좀비 FPS를 보여 줍니다. 프롬프트, 구현 세부 정보나 외부 게임플레이 평가는 제공하지 않습니다

> [!WARNING]
> The original source permalink returned HTTP 404 during the 2026-07-17 audit. Attribution and evidence are preserved from the supplied high-confidence source package.

Type: Demo | Date: 2026-07-16

---


<a id="frontend-motion"></a>
## 🎨 프론트엔드와 모션 디자인

| Case | What it shows | Type |
|---|---|---|
| [인터랙티브 모션 그래픽 프론트엔드 만들기](#case-5) | 일시 정지해도 조작 가능한 그래픽을 한 번에 만듭니다 | Demo |
| [동기화된 모션 광고 제작하기](#case-6) | 음악, 효과와 움직임의 동기화를 확인합니다 | Demo |
| [모션 디자인을 전적으로 코드로 만들기](#case-14) | 보조 생성 도구 없이 원샷 코딩 워크플로가 모션 디자인을 만들 수 있는지 시험합니다 | Demo |
| [인물을 조사해 애니메이션 개인 사이트 만들기](#case-15) | 폭넓은 개인 사이트 요청을 준 뒤 모델의 조사, 계획, 반복과 브라우저 검증을 살펴봅니다 | Tutorial |
| [블랙홀 시뮬레이션 생성하기](#case-17) | 과학 시각화 과제로 생성된 블랙홀 시뮬레이션을 살펴봅니다 | Demo |
| [복잡한 프론트엔드 모델링, 파티클과 셰이더 시험하기](#case-22) | 공개 프론트엔드 프롬프트로 모델링 정밀도, 파티클 효과와 인라인 셰이더 생성을 한 번에 살펴봅니다 | Demo |
| [한 번에 절차적 음악 도구 생성하기](#case-26) | 인터랙티브 절차적 음악 생성기의 원샷 생성을 시험하고 보이는 결과를 신중하게 비교합니다 | Demo |
| [이미지 두 장으로 Three.js 제품 페이지 만들기](#case-33) | 참조 이미지 두 장과 명시적인 Three.js 요구 사항을 사용해 제품 프레젠테이션을 생성합니다 | Demo |
| [고급 빵 절단기와 제품 페이지 발명하기](#case-39) | 제품 아이디어, 분해도, 시연과 랜딩 페이지를 하나의 디자인 결과물로 결합합니다 | Demo |
| [10초짜리 재귀적 펠리컨 GIF 생성하기](#case-45) | 완전히 명시된 반복 애니메이션 요구로 GIF의 서사적 연속성과 재귀를 살펴봅니다 | Demo |
| [BMW M4 CS 측면 SVG 생성하기](#case-55) | 특정 차량과 시점을 사용해 벡터 일러스트레이션 출력을 살펴봅니다 | Demo |
| [스크린샷 피드백으로 Gargantua 재현하기](#case-58) | 반복 스크린샷을 관찰 자료로 사용해 과학 시각화를 진단하고 개선합니다 | Tutorial |
| [스크린샷 62장으로 블랙홀 시각화 개선하기](#case-66) | 스크린샷 피드백 루프로 여러 번 시각 시뮬레이션을 읽고 진단하며 수정합니다 | Tutorial |
| [포스트트레이닝 마케팅 PDF 만들기](#case-68) | 명시된 제품과 결과물 형식을 사용해 마케팅 문서를 생성합니다 | Demo |
| [하나의 프롬프트로 사용자 인터페이스 만들기](#case-70) | 하나의 요청으로 완전한 UI 디자인을 생성하고 살펴봅니다 | Demo |

<a id="case-5"></a>
### Case 5: [인터랙티브 모션 그래픽 프론트엔드 만들기](https://x.com/chetaslua/status/2077749371144442022) (by [@chetaslua](https://x.com/chetaslua))

**일시 정지해도 조작 가능한 그래픽을 한 번에 만듭니다**

제작자는 42분, 단순 코드, harness·MCP·skill 없이 한 번에 만들었다고 보고합니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05-poster.jpg" alt="Case 5 video poster" height="360"></a>

[Play case 5 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-6"></a>
### Case 6: [동기화된 모션 광고 제작하기](https://x.com/abhinavflac/status/2077760297918484667) (by [@abhinavflac](https://x.com/abhinavflac))

**음악, 효과와 움직임의 동기화를 확인합니다**

제작자는 프롬프트만으로 Spotify 스타일 광고를 한 번에 만들었다고 하지만 정확한 프롬프트는 공개하지 않았습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06-poster.jpg" alt="Case 6 video poster" height="360"></a>

[Play case 6 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-14"></a>
### Case 14: [모션 디자인을 전적으로 코드로 만들기](https://x.com/chetaslua/status/2077952938564354503) (by [@chetaslua](https://x.com/chetaslua))

**보조 생성 도구 없이 원샷 코딩 워크플로가 모션 디자인을 만들 수 있는지 시험합니다**

제작자는 MCP, skill, 도구, 영상 생성이나 특별한 프롬프트 없이 전부 코드로 만든 원샷 Kimi K3 모션 디자인 결과라고 보고합니다. 정확한 프롬프트는 제공되지 않습니다

Type: Demo | Date: 2026-07-17

---

<a id="case-15"></a>
### Case 15: [인물을 조사해 애니메이션 개인 사이트 만들기](https://x.com/nicky_sap/status/2077857190707429411) (by [@nicky_sap](https://x.com/nicky_sap))

**폭넓은 개인 사이트 요청을 준 뒤 모델의 조사, 계획, 반복과 브라우저 검증을 살펴봅니다**

제작자는 Kimi K3가 Nick Saponaro를 조사하고 폭넓은 요청으로 애니메이션 개인 웹사이트를 만들었으며 계획, 테스트, 반복과 브라우저 확인까지 수행했다고 보고합니다. 결과는 본인이 보고한 워크플로 시연입니다

Type: Tutorial | Date: 2026-07-16

---

<a id="case-17"></a>
### Case 17: [블랙홀 시뮬레이션 생성하기](https://x.com/chetaslua/status/2077961850352971796) (by [@chetaslua](https://x.com/chetaslua))

**과학 시각화 과제로 생성된 블랙홀 시뮬레이션을 살펴봅니다**

제작자는 Kimi K3가 만든 것으로 표시된 블랙홀 시뮬레이션을 보여 주며 자신이 본 것 중 최고라고 말합니다. 출처에는 눈에 보이는 결과가 있지만 프롬프트, 평가 기준이나 독립적 검증은 없습니다

Type: Demo | Date: 2026-07-17

---

<a id="case-22"></a>
### Case 22: [복잡한 프론트엔드 모델링, 파티클과 셰이더 시험하기](https://x.com/karminski3/status/2077889959223337099) (by [@karminski3](https://x.com/karminski3))

**공개 프론트엔드 프롬프트로 모델링 정밀도, 파티클 효과와 인라인 셰이더 생성을 한 번에 살펴봅니다**

제작자는 정밀 모델링, 파티클 효과와 복잡한 인라인 셰이더 코드를 다룬 원패스 Kimi K3 프론트엔드 결과라고 보고하며 시험 프롬프트가 연결된 출처에 공개되어 있다고 밝힙니다

Type: Demo | Date: 2026-07-16

---

<a id="case-26"></a>
### Case 26: [한 번에 절차적 음악 도구 생성하기](https://x.com/mirochill/status/2077723551331758478) (by [@mirochill](https://x.com/mirochill))

**인터랙티브 절차적 음악 생성기의 원샷 생성을 시험하고 보이는 결과를 신중하게 비교합니다**

제작자는 Kimi K3가 한 번의 시도로 절차적 음악 도구를 생성했으며 Fable 5와 GPT-5.6 Sol의 결과보다 좋았다고 비교합니다. 이는 제작자 자신의 시험 세트이며 표준화된 벤치마크가 아닙니다

Type: Demo | Date: 2026-07-16

---

<a id="case-33"></a>
### Case 33: [이미지 두 장으로 Three.js 제품 페이지 만들기](https://x.com/1littlecoder/status/2077890296806031665) (by [@1littlecoder](https://x.com/1littlecoder))

**참조 이미지 두 장과 명시적인 Three.js 요구 사항을 사용해 제품 프레젠테이션을 생성합니다**

제작자는 Kimi K3가 이미지 두 장으로 제품 페이지를 디자인하고 명시적으로 요청한 Three.js 버전을 만들었다고 보고합니다. 추가 프롬프트나 구현 세부 정보는 제공되지 않습니다

Type: Demo | Date: 2026-07-16

---

<a id="case-39"></a>
### Case 39: [고급 빵 절단기와 제품 페이지 발명하기](https://x.com/filicroval/status/2077871090731221438) (by [@filicroval](https://x.com/filicroval))

**제품 아이디어, 분해도, 시연과 랜딩 페이지를 하나의 디자인 결과물로 결합합니다**

제작자는 Kimi K3가 단두대 방식의 빵 절단기를 발명해 고급 제품으로 구성하고 분해도와 시연이 포함된 랜딩 페이지를 만들었다고 보고합니다

Type: Demo | Date: 2026-07-16

---

<a id="case-45"></a>
### Case 45: [10초짜리 재귀적 펠리컨 GIF 생성하기](https://x.com/1littlecoder/status/2077880380900937865) (by [@1littlecoder](https://x.com/1littlecoder))

**완전히 명시된 반복 애니메이션 요구로 GIF의 서사적 연속성과 재귀를 살펴봅니다**

출처에는 자전거를 타는 펠리컨이 카메라 줌인 속에서 문자 메시지로 같은 영상을 받는 10초 반복 GIF 프롬프트가 포함되어 있습니다. 제작자는 Kimi K3의 결과 애니메이션을 보여 줍니다

Type: Demo | Date: 2026-07-16

---

<a id="case-55"></a>
### Case 55: [BMW M4 CS 측면 SVG 생성하기](https://x.com/HarshithLucky3/status/2077765821380886942) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**특정 차량과 시점을 사용해 벡터 일러스트레이션 출력을 살펴봅니다**

제작자는 Kimi K3 Max가 만든 것으로 표시된 BMW M4 CS 측면 SVG를 보여 줍니다. 제공된 출처에는 결과물이 있지만 프롬프트나 제작 단계는 없습니다

Type: Demo | Date: 2026-07-16

---

<a id="case-58"></a>
### Case 58: [스크린샷 피드백으로 Gargantua 재현하기](https://x.com/AngryTomtweets/status/2077868981659324444) (by [@AngryTomtweets](https://x.com/AngryTomtweets))

**반복 스크린샷을 관찰 자료로 사용해 과학 시각화를 진단하고 개선합니다**

출처는 Kimi K3가 62장의 자체 스크린샷을 사용해 Interstellar의 Gargantua를 재현했으며 각 결과를 읽고 문제를 진단한 뒤 반복적으로 조치했다고 보고합니다

Type: Tutorial | Date: 2026-07-16

---

<a id="case-66"></a>
### Case 66: [스크린샷 62장으로 블랙홀 시각화 개선하기](https://x.com/TokenGremlin/status/2077855959201042645) (by [@TokenGremlin](https://x.com/TokenGremlin))

**스크린샷 피드백 루프로 여러 번 시각 시뮬레이션을 읽고 진단하며 수정합니다**

출처는 Kimi K3가 62장의 스크린샷에 걸쳐 출력을 관찰하고 개선해 Interstellar의 Gargantua를 재구성했다고 보고합니다. 이는 독립적인 물리 정확성보다 보고된 피드백 루프를 보여 줍니다

Type: Tutorial | Date: 2026-07-16

---

<a id="case-68"></a>
### Case 68: [포스트트레이닝 마케팅 PDF 만들기](https://x.com/Satvik_Pen/status/2077859673517023313) (by [@Satvik_Pen](https://x.com/Satvik_Pen))

**명시된 제품과 결과물 형식을 사용해 마케팅 문서를 생성합니다**

제작자는 Kimi K3에 Thinking Machines의 Inkling 포스트트레이닝에 관한 마케팅 PDF를 요청하고 결과를 공유했으며 배후 과정도 높이 평가합니다. 프롬프트나 평가 기준은 제공되지 않습니다

Type: Demo | Date: 2026-07-16

---

<a id="case-70"></a>
### Case 70: [하나의 프롬프트로 사용자 인터페이스 만들기](https://x.com/BrianMRey/status/2077891942088671689) (by [@BrianMRey](https://x.com/BrianMRey))

**하나의 요청으로 완전한 UI 디자인을 생성하고 살펴봅니다**

제작자는 원프롬프트 Kimi K3 실행으로 만든 UI 디자인을 보여 주며 매우 긍정적으로 주관 평가합니다. 정확한 프롬프트와 평가 기준은 포함되지 않습니다

Type: Demo | Date: 2026-07-16

---


<a id="coding-integrations"></a>
## 💻 코딩과 통합

| Case | What it shows | Type |
|---|---|---|
| [작동하는 macOS를 갖춘 가상 MacBook 만들기](#case-18) | Three.js 하드웨어 렌더링과 인터랙티브 브라우저 운영체제 시뮬레이션을 결합합니다 | Demo |
| [DSL에서 PTX까지 GPU 컴파일러 만들기](#case-25) | DSL, 컴파일러 패스, PTX 생성과 Tensor Core 경로를 아우르는 엔드투엔드 컴파일러 과제를 사용합니다 | Demo |
| [WebGL2로 실시간 블랙홀 레이트레이서 만들기](#case-32) | 단일 HTML 파일 안에서 네이티브 WebGL2 측지선 레이트레이서의 원프롬프트 생성을 시험합니다 | Benchmark |
| [mGBA WASM 기반 Game Boy Advance 에뮬레이터 만들기](#case-46) | 라이선스가 있는 3D 모델과 실제 에뮬레이터 코어를 통합하고 인터페이스와 게임플레이를 재귀적으로 개선합니다 | Integration |
| [중국어 출처로 여러 주제 조사하기](#case-50) | 장시간 연구 과제로 모델 세대 간 조사 충실도와 지연 시간을 비교합니다 | Evaluation |
| [작동하는 앱이 포함된 macOS 브라우저 복제본 만들기](#case-56) | 음악, 브라우저와 이메일 애플리케이션을 포함하는 브라우저 운영체제 시뮬레이션을 만듭니다 | Demo |
| [작동하는 FaceTime이 포함된 macOS 시뮬레이션 만들기](#case-62) | 가상 운영체제 과제로 생성된 앱 상호작용이 작동하는지 시험합니다 | Demo |
| [이중 과제 프론트엔드 효과 비교기 추가하기](#case-64) | 완료된 과제 두 개를 선택해 나란히 표시하고 뷰와 상호작용을 동기화하는 도구를 만듭니다 | Tutorial |

<a id="case-18"></a>
### Case 18: [작동하는 macOS를 갖춘 가상 MacBook 만들기](https://x.com/scottstts/status/2077890054299541890) (by [@scottstts](https://x.com/scottstts))

**Three.js 하드웨어 렌더링과 인터랙티브 브라우저 운영체제 시뮬레이션을 결합합니다**

출처는 Kimi K3가 Three.js로 가상 MacBook과 작동하는 macOS 스타일 환경을 만들었다고 보고합니다. 결과물은 보여 주지만 구현 단계는 제공하지 않습니다

Type: Demo | Date: 2026-07-16

---

<a id="case-25"></a>
### Case 25: [DSL에서 PTX까지 GPU 컴파일러 만들기](https://x.com/rohanpaul_ai/status/2077886618657231220) (by [@rohanpaul_ai](https://x.com/rohanpaul_ai))

**DSL, 컴파일러 패스, PTX 생성과 Tensor Core 경로를 아우르는 엔드투엔드 컴파일러 과제를 사용합니다**

출처는 Kimi K3가 자체 DSL과 패스부터 PTX 생성까지 GPU 컴파일러를 처음부터 만들고 Tensor Core 경로를 Triton과 비교했다고 보고합니다. 제공된 기록에는 독립적인 벤치마크 세부 정보가 없습니다

Type: Demo | Date: 2026-07-16

---

<a id="case-32"></a>
### Case 32: [WebGL2로 실시간 블랙홀 레이트레이서 만들기](https://x.com/AlicanKiraz0/status/2077885419744612597) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**단일 HTML 파일 안에서 네이티브 WebGL2 측지선 레이트레이서의 원프롬프트 생성을 시험합니다**

작성자는 네이티브 WebGL2로 작동하는 단일 파일 블랙홀 빛 굴절 레이트레이서를 요구하는 코딩 벤치마크를 설명합니다. 제공된 기록은 과제와 참여 모델을 확인하지만 완전한 독립 결과 감사는 제공하지 않습니다

Type: Benchmark | Date: 2026-07-16

---

<a id="case-46"></a>
### Case 46: [mGBA WASM 기반 Game Boy Advance 에뮬레이터 만들기](https://x.com/teortaxesTex/status/2077925090168062272) (by [@teortaxesTex](https://x.com/teortaxesTex))

**라이선스가 있는 3D 모델과 실제 에뮬레이터 코어를 통합하고 인터페이스와 게임플레이를 재귀적으로 개선합니다**

인용된 Kimi K3 프로젝트는 라이선스가 있는 AGB-001 모델을 수정하고 mGBA WASM 코어를 통합해 재귀적 자기 개선으로 인터페이스와 게임플레이를 향상합니다. 게시물은 독립적 재현이 아니라 프로젝트 설명을 인용합니다

Type: Integration | Date: 2026-07-17

---

<a id="case-50"></a>
### Case 50: [중국어 출처로 여러 주제 조사하기](https://x.com/tphuang/status/2077911994607239400) (by [@tphuang](https://x.com/tphuang))

**장시간 연구 과제로 모델 세대 간 조사 충실도와 지연 시간을 비교합니다**

작성자는 중국어 출처를 사용하는 여러 연구 주제에서 Kimi K3를 시험해 K2.6보다 철저하지만 더 느렸다고 보고합니다. 당시 서비스 수요가 매우 높았다는 점도 덧붙입니다

Type: Evaluation | Date: 2026-07-17

---

<a id="case-56"></a>
### Case 56: [작동하는 앱이 포함된 macOS 브라우저 복제본 만들기](https://x.com/twid/status/2077924755357974989) (by [@twid](https://x.com/twid))

**음악, 브라우저와 이메일 애플리케이션을 포함하는 브라우저 운영체제 시뮬레이션을 만듭니다**

출처는 Kimi K3로 음악, 브라우저, 이메일과 기타 기능을 갖춘 브라우저 기반 macOS 복제본을 만들었다고 보고합니다. 구현 세부 정보는 제공하지 않습니다

Type: Demo | Date: 2026-07-17

---

<a id="case-62"></a>
### Case 62: [작동하는 FaceTime이 포함된 macOS 시뮬레이션 만들기](https://x.com/LinearUncle/status/2077919552239997078) (by [@LinearUncle](https://x.com/LinearUncle))

**가상 운영체제 과제로 생성된 앱 상호작용이 작동하는지 시험합니다**

제작자는 Kimi K3가 만든 것으로 표시된 macOS 스타일 환경을 보여 주고 FaceTime 기능이 작동한다고 보고합니다. 출처에는 설정이나 검증 단계가 없습니다

Type: Demo | Date: 2026-07-17

---

<a id="case-64"></a>
### Case 64: [이중 과제 프론트엔드 효과 비교기 추가하기](https://x.com/MinLiBuilds/status/2077939461510615376) (by [@MinLiBuilds](https://x.com/MinLiBuilds))

**완료된 과제 두 개를 선택해 나란히 표시하고 뷰와 상호작용을 동기화하는 도구를 만듭니다**

제작자는 Kimi K3에 과제 선택, 이중 브라우저 패널, 객체·로밍 모드, 동기화된 시점과 상호작용 테스트를 갖춘 프론트엔드 비교 워크플로를 추가해 달라고 요청했다고 보고합니다. 게시물은 더 넓은 모델 한계도 언급합니다

Type: Tutorial | Date: 2026-07-17

---


<a id="evaluation-limits"></a>
## 🧪 평가와 한계

| Case | What it shows | Type |
|---|---|---|
| [BridgeBench 라바 램프 과제로 프론트엔드 디자인 비교하기](#case-7) | BridgeBench 라바 램프 과제를 보편적 순위가 아닌 범위가 정해진 하나의 프론트엔드 디자인 비교로 사용합니다 | Benchmark |
| [편집자 어조의 대본 작성 벤치마크하기](#case-8) | 명확히 식별된 내부 벤치마크 안에서 편집자 어조 적합성, 상대 순위와 대본당 비용을 측정합니다 | Benchmark |
| [플래피 게임의 디자인, 비용과 난이도 비교하기](#case-10) | 생성된 게임을 비교할 때 난이도 설정, 비용, 디자인과 게임플레이 기능을 기록합니다 | Benchmark |
| [같은 디자인 프롬프트로 게임 디자인 비교하기](#case-12) | 디자인 프롬프트를 고정하고 속도, 디자인 감각과 게임플레이 느낌을 따로 살펴봅니다 | Benchmark |
| [통계 감사에 독립적 검토 요구하기](#case-13) | 모델이 생성한 통계 감사를 신뢰하기 전에 독립 전문가나 다른 모델의 검토와 결합합니다 | Limit |
| [느리지만 강한 프론트엔드 실행 평가하기](#case-16) | 프론트엔드 과제를 시험할 때 출력 품질과 함께 완료 시간을 기록합니다 | Evaluation |
| [복선 실패를 중심으로 추리소설 쓰기 시험하기](#case-20) | 생성된 미스터리가 단서, 난해함과 복선의 균형을 맞추는지 평가합니다 | Limit |
| [Millennium Falcon 모델링과 애니메이션 비교하기](#case-21) | 동일한 스타일 요청과 effort 설정으로 3D 모델링, 애니메이션, 시간과 비용을 비교합니다 | Benchmark |
| [Kimi K3 프로젝트 10개 모음 검토하기](#case-28) | 연결된 프로젝트 모음에서 구체적 결과물을 찾고 각각 별도로 검증합니다 | Evaluation |
| [고급 랜딩 페이지를 네 모델로 비교하기](#case-29) | 랜딩 페이지 요청을 고정하고 모델 출력의 애니메이션 깊이와 완성도를 살펴봅니다 | Evaluation |
| [레트로 게임 메커니즘과 비용 벤치마크하기](#case-30) | 동일한 레트로 게임 과제에서 게임플레이, 물리, 메커니즘, 자율 행동, 토큰 사용량과 비용을 비교합니다 | Benchmark |
| [Fable 5와 게임 생성 비교하기](#case-31) | 나란히 제시된 생성 게임 사례를 폭넓은 모델 판정이 아닌 좁은 범위의 평가로 사용합니다 | Evaluation |
| [Opus 4.8과 복잡한 프론트엔드·개발 과제 비교하기](#case-34) | 하나의 모델이 보편적으로 우월하다고 선언하지 않고 여러 복잡한 코딩 과제에서 승패를 식별합니다 | Evaluation |
| [벤치마크와 랜딩 페이지 시험 함께 검토하기](#case-35) | 벤치마크 맥락과 구체적인 랜딩 페이지 생성 시험을 결합하되 두 근거 유형을 구분합니다 | Evaluation |
| [그래프-수식 과제로 귀납 추론 평가하기](#case-37) | 1차 논리 귀납 과제에서 정확도, 홀드아웃 동작과 수식 복잡도를 측정합니다 | Benchmark |
| [보고된 게임, 랜딩 페이지, 3D 작업과 긴 컨텍스트 검토하기](#case-38) | 여러 출처의 모음으로 구체적 결과물을 비교하고 비용 주장과 함께 속도 한계를 기록합니다 | Evaluation |
| [복잡한 계획을 감사하고 해결책에 이의 제기하기](#case-40) | 두 번째 모델로 축소 보고된 발견, 잘못된 해결책과 거부해야 할 결론을 식별합니다 | Evaluation |
| [PPO 방식 강화학습 ASCII 다이어그램 비교하기](#case-41) | ASCII 다이어그램 프롬프트를 고정하고 모델이 강화학습 루프를 표현하는 방식을 비교합니다 | Evaluation |
| [용량 오류를 추적하며 Blender 모델링하기](#case-42) | 결과물만 보지 않고 Blender의 부분적 진행 상황과 서비스 안정성을 함께 평가합니다 | Limit |
| [아레나에서 Flappy Bird 생성 비교하기](#case-47) | 아레나 과제로 생성된 Flappy Bird 결과 두 개를 비교하되 판단을 해당 과제 범위로 제한합니다 | Evaluation |
| [도구로 Bongard 시각 귀납 문제 풀기](#case-52) | 도구 사용이 Bongard 추론 과제의 시각적 규칙을 도출하는 데 도움이 되는지 시험합니다 | Evaluation |
| [GPT-5.6 Sol과 프론트엔드 감각·3D 디자인 비교하기](#case-53) | 범위가 정해진 프론트엔드 비교에서 기능, 시각적 감각, 우아함과 3D 구현을 살펴봅니다 | Evaluation |
| [세 모델의 웹사이트 생성 비교하기](#case-57) | 눈에 보이는 웹사이트 결과로 하나의 시험에서 Kimi K3, Fable 5, GPT-5.6 Sol을 비교합니다 | Evaluation |
| [절차적 3D 게임 생성과 비용 비교하기](#case-59) | 모델 간 프롬프트를 고정하고 생성된 룰렛, 슬롯머신과 핀볼 시스템을 실행당 비용과 함께 살펴봅니다 | Benchmark |
| [3D 무기고 장면의 디테일과 조명 비교하기](#case-69) | 범위가 정해진 Kimi K3와 Opus 4.8 비교에서 객체 밀도, 조명과 장면 디테일을 살펴봅니다 | Evaluation |

<a id="case-7"></a>
### Case 7: [BridgeBench 라바 램프 과제로 프론트엔드 디자인 비교하기](https://x.com/bridgemindai/status/2077868061953007908) (by [@bridgemindai](https://x.com/bridgemindai))

**BridgeBench 라바 램프 과제를 보편적 순위가 아닌 범위가 정해진 하나의 프론트엔드 디자인 비교로 사용합니다**

BridgeMind AI는 Kimi K3가 자체 BridgeBench 라바 램프 과제에서 Fable 5를 앞섰고 인용된 아레나에서 1위를 차지했다고 보고합니다. 이는 게시자가 보고한 비교 결과입니다

Type: Benchmark | Date: 2026-07-16

---

<a id="case-8"></a>
### Case 8: [편집자 어조의 대본 작성 벤치마크하기](https://x.com/Whats_AI/status/2077860441380798908) (by [@Whats_AI](https://x.com/Whats_AI))

**명확히 식별된 내부 벤치마크 안에서 편집자 어조 적합성, 상대 순위와 대본당 비용을 측정합니다**

Whats_AI는 초기 내부 결과로 2,840 Elo, 자체 보드 1위, 대본당 약 $0.25를 보고합니다. 이는 한 조직의 예비 벤치마크이며 일반적인 성능이나 가격 보장이 아닙니다

Type: Benchmark | Date: 2026-07-16

---

<a id="case-10"></a>
### Case 10: [플래피 게임의 디자인, 비용과 난이도 비교하기](https://x.com/MrAhmadAwais/status/2077915347974557862) (by [@MrAhmadAwais](https://x.com/MrAhmadAwais))

**생성된 게임을 비교할 때 난이도 설정, 비용, 디자인과 게임플레이 기능을 기록합니다**

Command Code의 내부 Flappy 벤치마크는 모델마다 다른 난이도 설정을 사용했으며 Kimi K3 $0.024, Fable 5 $0.42, GPT-5.6 Sol $0.15를 제시합니다. 설정이 동일하지 않으므로 범위가 제한된 내부 비교입니다

Type: Benchmark | Date: 2026-07-17

---

<a id="case-12"></a>
### Case 12: [같은 디자인 프롬프트로 게임 디자인 비교하기](https://x.com/CommandCodeAI/status/2077921526213746948) (by [@CommandCodeAI](https://x.com/CommandCodeAI))

**디자인 프롬프트를 고정하고 속도, 디자인 감각과 게임플레이 느낌을 따로 살펴봅니다**

Command Code는 Kimi K3, GPT-5.6 Sol, Fable 5를 같은 프롬프트로 비교했다고 보고합니다. 게시물은 Kimi K3가 디자인 감각에서 좋은 성과를 냈고 다른 두 모델은 플레이 속도가 너무 빨랐다고 하지만 이는 게시자의 평가입니다

Type: Benchmark | Date: 2026-07-17

---

<a id="case-13"></a>
### Case 13: [통계 감사에 독립적 검토 요구하기](https://x.com/emollick/status/2077869293031624793) (by [@emollick](https://x.com/emollick))

**모델이 생성한 통계 감사를 신뢰하기 전에 독립 전문가나 다른 모델의 검토와 결합합니다**

Ethan Mollick는 Kimi K3 Max가 이전 학술 연구를 감사하면서 통계를 잘못 적용했다고 보고하고 별도의 비판에 동의합니다. 이 부정적 사례는 검토 없는 수용보다 독립적 확인이 필요함을 뒷받침합니다

Type: Limit | Date: 2026-07-16

---

<a id="case-16"></a>
### Case 16: [느리지만 강한 프론트엔드 실행 평가하기](https://x.com/Lentils80/status/2077387333154857151) (by [@Lentils80](https://x.com/Lentils80))

**프론트엔드 과제를 시험할 때 출력 품질과 함께 완료 시간을 기록합니다**

제작자는 Kimi K3 프론트엔드 실행에 35분이 걸렸고 해당 프롬프트에서 본 결과 중 최고 수준이라고 평가합니다. 속도와 품질 판단 모두 한 사용자의 관찰입니다

Type: Evaluation | Date: 2026-07-15

---

<a id="case-20"></a>
### Case 20: [복선 실패를 중심으로 추리소설 쓰기 시험하기](https://x.com/emollick/status/2077951790868238616) (by [@emollick](https://x.com/emollick))

**생성된 미스터리가 단서, 난해함과 복선의 균형을 맞추는지 평가합니다**

Ethan Mollick는 Kimi K3가 좋은 추리소설을 쓰지 못했고 단서를 너무 명백하면서도 너무 모호하게 만들며 복선에 실패했다고 보고합니다. 다른 모델도 이 한계를 공유한다고 덧붙입니다

Type: Limit | Date: 2026-07-17

---

<a id="case-21"></a>
### Case 21: [Millennium Falcon 모델링과 애니메이션 비교하기](https://x.com/gmi_cloud/status/2077903360263676090) (by [@gmi_cloud](https://x.com/gmi_cloud))

**동일한 스타일 요청과 effort 설정으로 3D 모델링, 애니메이션, 시간과 비용을 비교합니다**

GMI Cloud는 최대 effort에서 픽셀 스타일과 원본 스타일의 Millennium Falcon 재현을 Kimi K3와 Fable 5로 비교했다고 보고합니다. 첫 시험에서 Kimi K3는 더 오래 걸렸지만 비용은 약 3분의 1이었고 다른 시험에서는 절반 미만이었다고 하며 이는 공급자가 보고한 결과입니다

Type: Benchmark | Date: 2026-07-16

---

<a id="case-28"></a>
### Case 28: [Kimi K3 프로젝트 10개 모음 검토하기](https://x.com/minchoi/status/2077957907857994006) (by [@minchoi](https://x.com/minchoi))

**연결된 프로젝트 모음에서 구체적 결과물을 찾고 각각 별도로 검증합니다**

작성자는 Game Boy Advance 에뮬레이터를 포함해 미디어가 있는 Kimi K3 사례 10개를 큐레이션합니다. 이 기록은 하나의 재현 가능한 워크플로가 아니라 모음이므로 연결된 사례를 각각 독립적으로 확인해야 합니다

Type: Evaluation | Date: 2026-07-17

---

<a id="case-29"></a>
### Case 29: [고급 랜딩 페이지를 네 모델로 비교하기](https://x.com/doutorcaleb/status/2077904020471947773) (by [@doutorcaleb](https://x.com/doutorcaleb))

**랜딩 페이지 요청을 고정하고 모델 출력의 애니메이션 깊이와 완성도를 살펴봅니다**

제작자는 Kimi K3, Fable, Grok, GPT Terra에 같은 고급 랜딩 페이지 프롬프트를 주었고 Kimi K3 결과가 가장 강했다고 평가합니다. 이는 단일 과제에 대한 자체 보고 비교입니다

Type: Evaluation | Date: 2026-07-16

---

<a id="case-30"></a>
### Case 30: [레트로 게임 메커니즘과 비용 벤치마크하기](https://x.com/adxtyahq/status/2077860500462055570) (by [@adxtyahq](https://x.com/adxtyahq))

**동일한 레트로 게임 과제에서 게임플레이, 물리, 메커니즘, 자율 행동, 토큰 사용량과 비용을 비교합니다**

출처는 Road Fighter, Battle City, Q*bert의 같은 프롬프트 시험을 보고하며 Kimi K3 $0.28, GPT-5.6 $0.28, Opus 4.8 $0.54를 제시합니다. 이는 게시자의 벤치마크 수치입니다

Type: Benchmark | Date: 2026-07-16

---

<a id="case-31"></a>
### Case 31: [Fable 5와 게임 생성 비교하기](https://x.com/higgsfield_ai/status/2077943629633712490) (by [@higgsfield_ai](https://x.com/higgsfield_ai))

**나란히 제시된 생성 게임 사례를 폭넓은 모델 판정이 아닌 좁은 범위의 평가로 사용합니다**

Higgsfield는 Kimi K3와 Fable 5의 게임 생성 비교를 제시합니다. 제공된 기록에는 비교 미디어가 있지만 프롬프트, 채점 기준이나 세부 조건은 없습니다

Type: Evaluation | Date: 2026-07-17

---

<a id="case-34"></a>
### Case 34: [Opus 4.8과 복잡한 프론트엔드·개발 과제 비교하기](https://x.com/op7418/status/2077969583018066116) (by [@op7418](https://x.com/op7418))

**하나의 모델이 보편적으로 우월하다고 선언하지 않고 여러 복잡한 코딩 과제에서 승패를 식별합니다**

리뷰어는 Kimi K3와 Opus 4.8을 복잡한 프론트엔드와 개발 과제에서 직접 시험했으며 결과가 엇갈리는 가운데 대체로 비슷하다고 평가합니다. 이는 한 리뷰어의 판단입니다

Type: Evaluation | Date: 2026-07-17

---

<a id="case-35"></a>
### Case 35: [벤치마크와 랜딩 페이지 시험 함께 검토하기](https://x.com/adamuchigabriel/status/2077880433925120471) (by [@adamuchigabriel](https://x.com/adamuchigabriel))

**벤치마크 맥락과 구체적인 랜딩 페이지 생성 시험을 결합하되 두 근거 유형을 구분합니다**

영상은 Kimi K3의 벤치마크 논의, 랜딩 페이지 시험과 프론트엔드 디자인 관찰을 제시합니다. 제공된 기록에는 전체 시험 프롬프트나 채점 기준이 없습니다

Type: Evaluation | Date: 2026-07-16

---

<a id="case-37"></a>
### Case 37: [그래프-수식 과제로 귀납 추론 평가하기](https://x.com/s_batzoglou/status/2077884096307454119) (by [@s_batzoglou](https://x.com/s_batzoglou))

**1차 논리 귀납 과제에서 정확도, 홀드아웃 동작과 수식 복잡도를 측정합니다**

작성자는 각각 8~10개 요소를 가진 작은 그래프 6~10개에서 1차 논리 수식을 추론하는 ICML INDUCTION 과제로 Kimi K3와 다른 모델을 벤치마크했다고 보고합니다. 게시물은 이전 작업에서 결과를 갱신했다고 하며 여기서는 새로 독립 재현했다고 주장하지 않습니다

Type: Benchmark | Date: 2026-07-16

---

<a id="case-38"></a>
### Case 38: [보고된 게임, 랜딩 페이지, 3D 작업과 긴 컨텍스트 검토하기](https://x.com/servasyy_ai/status/2077903775113834689) (by [@servasyy_ai](https://x.com/servasyy_ai))

**여러 출처의 모음으로 구체적 결과물을 비교하고 비용 주장과 함께 속도 한계를 기록합니다**

작성자는 게임, 랜딩 페이지, 3D 생성과 긴 컨텍스트 작업에 관한 Kimi K3 시험을 요약하며 시도할 가치는 있지만 아직 Fable 5를 대체하지는 못한다고 결론냅니다. 모든 수치는 이 모음에 포함된 2차 보고입니다

Type: Evaluation | Date: 2026-07-16

---

<a id="case-40"></a>
### Case 40: [복잡한 계획을 감사하고 해결책에 이의 제기하기](https://x.com/doodlestein/status/2077901883637665958) (by [@doodlestein](https://x.com/doodlestein))

**두 번째 모델로 축소 보고된 발견, 잘못된 해결책과 거부해야 할 결론을 식별합니다**

제작자는 Kimi K3가 충분히 다듬어진 계획을 검토해 심각한 문제가 축소 보고되었고 제안된 해결책 약 3분의 1을 수정해야 하며 한 가지 발견은 반박된다고 판단했다고 보고합니다. 이는 해당 감사에서 나온 결과입니다

Type: Evaluation | Date: 2026-07-16

---

<a id="case-41"></a>
### Case 41: [PPO 방식 강화학습 ASCII 다이어그램 비교하기](https://x.com/dejavucoder/status/2077872015856615541) (by [@dejavucoder](https://x.com/dejavucoder))

**ASCII 다이어그램 프롬프트를 고정하고 모델이 강화학습 루프를 표현하는 방식을 비교합니다**

출처는 PPO 방식 강화학습 루프를 ASCII로 그리라는 프롬프트를 제공하고 Kimi K3 Max와 Fable 5 High 결과를 나란히 보여 줍니다. 판단은 단일 과제의 시각적 비교입니다

Type: Evaluation | Date: 2026-07-16

---

<a id="case-42"></a>
### Case 42: [용량 오류를 추적하며 Blender 모델링하기](https://x.com/Angaisb_/status/2077910845523214668) (by [@Angaisb_](https://x.com/Angaisb_))

**결과물만 보지 않고 Blender의 부분적 진행 상황과 서비스 안정성을 함께 평가합니다**

제작자는 Kimi K3의 Blender 모델링 진행 상황을 보여 주면서 반복되는 용량 오류도 보고합니다. 제공된 출처에서 작업은 미완성이므로 부분 결과와 안정성 한계를 함께 고려해야 합니다

Type: Limit | Date: 2026-07-17

---

<a id="case-47"></a>
### Case 47: [아레나에서 Flappy Bird 생성 비교하기](https://x.com/jun_song/status/2077396996865003739) (by [@jun_song](https://x.com/jun_song))

**아레나 과제로 생성된 Flappy Bird 결과 두 개를 비교하되 판단을 해당 과제 범위로 제한합니다**

제작자는 Flappy Bird 과제에서 Kimi K3와 Opus 4.8을 비교한 Arena 결과를 보고하고 Kimi K3가 훨씬 낫다고 평가합니다. 기록에는 전체 프롬프트나 평가 기준이 없습니다

Type: Evaluation | Date: 2026-07-15

---

<a id="case-52"></a>
### Case 52: [도구로 Bongard 시각 귀납 문제 풀기](https://x.com/IntuitMachine/status/2077885406528311561) (by [@IntuitMachine](https://x.com/IntuitMachine))

**도구 사용이 Bongard 추론 과제의 시각적 규칙을 도출하는 데 도움이 되는지 시험합니다**

제작자는 같은 비교에서 Grok 4.5와 Muse Spark 1.1이 풀지 못한 Bongard 문제를 Kimi K3가 도구를 사용해 풀었다고 보고합니다. 이는 한 사용자의 과제 결과이며 일반적인 추론 벤치마크가 아닙니다

Type: Evaluation | Date: 2026-07-16

---

<a id="case-53"></a>
### Case 53: [GPT-5.6 Sol과 프론트엔드 감각·3D 디자인 비교하기](https://x.com/filicroval/status/2077736407506751952) (by [@filicroval](https://x.com/filicroval))

**범위가 정해진 프론트엔드 비교에서 기능, 시각적 감각, 우아함과 3D 구현을 살펴봅니다**

제작자는 Kimi K3와 GPT-5.6 Sol의 프론트엔드 디자인을 비교하고 시각적 감각, 우아함과 3D 역량에서 Kimi K3가 더 강하다고 평가합니다. 이는 주관적이며 과제에 한정된 평가입니다

Type: Evaluation | Date: 2026-07-16

---

<a id="case-57"></a>
### Case 57: [세 모델의 웹사이트 생성 비교하기](https://x.com/pengchujin/status/2077962916226298340) (by [@pengchujin](https://x.com/pengchujin))

**눈에 보이는 웹사이트 결과로 하나의 시험에서 Kimi K3, Fable 5, GPT-5.6 Sol을 비교합니다**

제작자는 Kimi K3, Fable 5, GPT-5.6 Sol의 웹사이트 생성 비교를 제시합니다. 제공된 기록에는 전체 프롬프트나 채점 기준이 공개되지 않습니다

Type: Evaluation | Date: 2026-07-17

---

<a id="case-59"></a>
### Case 59: [절차적 3D 게임 생성과 비용 비교하기](https://x.com/adxtyahq/status/2077958193511362856) (by [@adxtyahq](https://x.com/adxtyahq))

**모델 간 프롬프트를 고정하고 생성된 룰렛, 슬롯머신과 핀볼 시스템을 실행당 비용과 함께 살펴봅니다**

게시자는 여러 모델의 절차적 3D 게임 비교를 보고하며 Kimi K3 $0.71, Grok 4.5 $0.30 등의 비용을 제시합니다. 모든 순위와 비용은 해당 게시자의 실행 결과로 취급해야 합니다

Type: Benchmark | Date: 2026-07-17

---

<a id="case-69"></a>
### Case 69: [3D 무기고 장면의 디테일과 조명 비교하기](https://x.com/hakki_alkan/status/2077887013332636032) (by [@hakki_alkan](https://x.com/hakki_alkan))

**범위가 정해진 Kimi K3와 Opus 4.8 비교에서 객체 밀도, 조명과 장면 디테일을 살펴봅니다**

출처는 Kimi K3가 물건이 채워진 선반, 상자와 사실적인 조명이 있는 세밀한 무기고를 만들었고 Opus 4.8은 빈약한 방을 만들었다고 보고합니다. 이는 독립적 벤치마크가 아닌 제3자 비교 보고입니다

Type: Evaluation | Date: 2026-07-16

---

## 관련 자료

- [EvoLink에서 Kimi K3 세부 정보와 가격 보기](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_model)
- [EvoLink Kimi K3 API 문서 열기](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_api_docs)
- [EvoLink에서 Kimi K3 자세히 알아보기](https://evolink.ai/blog/is-kimi-k3-available-on-evolink?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_article)
- EvoLink 모델 페이지와 API 문서는 확인되었지만 설치형 Kimi K3 skill은 확인되지 않았습니다

<a id="acknowledge"></a>
## 🙏 감사의 말

Kimi K3 작업을 공개한 모든 제작자에게 감사드립니다

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

*출처나 설명 수정이 필요하면 공개 근거와 함께 issue를 열어 주세요*
