<div align="center">

<a href="https://evolink.ai/kimi-k3?utm_source=github&utm_medium=banner&utm_campaign=awesome-kimi-k3-usecases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/images/ko-v2.png" alt="달 표면과 EvoLink 사용 안내가 포함된 한국어 Kimi K3 배너" width="760"></a>

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

# Kimi K3 활용 사례

## 🍌 소개

Kimi K3의 근거가 분명한 활용 사례를 모은 저장소입니다

**공개 출처에 기반한 게임, 3D, 모션 디자인, 통합, 평가와 실무적 한계를 수집합니다**

89개 사례는 모두 신뢰도 높은 공개 출처에 근거합니다. 제목과 작성자는 원문으로 연결되며 약한 후보, 중복, 근거가 부족한 후보는 제외됩니다

## 📊 개요

- 크리에이터와 실무자의 high-confidence 사례 89개
- 게임, 3D, 프론트엔드, 모션, 코딩, 연구, 평가와 한계를 폭넓게 다룸
- 각 사례에 출처, 작성자, 유형, 날짜와 프롬프트 경계 보존
- 개인 경험을 벤치마크로 일반화하지 않음

> [!NOTE]
> 구체적인 증거를 우선하며 공개되지 않은 프롬프트나 설정을 재구성하지 않습니다

<a id="quick-api-access"></a>
## ⚡ 빠른 시작

EvoLink에 문서화된 모델 ID는 `kimi-k3`이며 모델 페이지와 Chat Completions API 문서를 이용할 수 있습니다

1. [EvoLink에서 Kimi K3 세부 정보와 가격 보기](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=landing_overview)
2. [EvoLink API 키 생성 또는 관리](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-kimi-k3-usecases&utm_content=api_key)

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

[EvoLink Kimi K3 API 문서 열기](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=first_run)

> [!IMPORTANT]
> EvoLink 모델 페이지와 API 문서가 공개 경로와 ID를 확인합니다. 독립적인 Kimi K3 브라우저 또는 노코드 화면은 확인되지 않았으며, 이 저장소는 독립적인 유료 API 테스트도 주장하지 않습니다

## 📑 메뉴

| Section | Cases |
|---|---|
| [인터랙티브 게임과 3D](#games-3d) | 37 |
| [프론트엔드와 모션 디자인](#frontend-motion) | 25 |
| [코딩과 통합](#coding-integrations) | 14 |
| [평가와 한계](#evaluation-limits) | 43 |
| [관련 자료](#related-resources) | 관련 자료 |
| [빠른 시작](#quick-api-access) | 빠른 시작 |
| [감사의 말](#acknowledge) | 감사와 수정 |

| Case | Category | What it shows | Type |
|---|---|---|---|
| [하나의 프롬프트로 복셀 레이서 만들기](#case-1) | 인터랙티브 게임과 3D | 짧은 장면 아이디어로 레이싱 프로토타입을 만들고 다음 개선 범위를 정합니다 | Demo |
| [같은 프롬프트로 Frogger 비교하기](#case-2) | 인터랙티브 게임과 3D | 프롬프트를 고정해 모델 출력 차이를 살펴봅니다 | Evaluation |
| [Frogger와 플레이 녹화 생성하기](#case-3) | 인터랙티브 게임과 3D | 게임과 녹화 흐름을 각각 원샷으로 시험합니다 | Demo |
| [Three.js 항공모함 프로토타입 만들기](#case-4) | 인터랙티브 게임과 3D | 구체적인 이착함 장면으로 인터랙티브 3D 생성을 시험합니다 | Demo |
| [인터랙티브 모션 그래픽 프론트엔드 만들기](#case-5) | 프론트엔드와 모션 디자인 | 일시 정지해도 조작 가능한 그래픽을 한 번에 만듭니다 | Demo |
| [동기화된 모션 광고 제작하기](#case-6) | 프론트엔드와 모션 디자인 | 음악, 효과와 움직임의 동기화를 확인합니다 | Demo |
| [BridgeBench 라바 램프 과제로 프론트엔드 디자인 비교하기](#case-7) | 평가와 한계 | BridgeBench 라바 램프 과제를 보편적 순위가 아닌 범위가 정해진 하나의 프론트엔드 디자인 비교로 사용합니다 | Benchmark |
| [편집자 어조의 대본 작성 벤치마크하기](#case-8) | 평가와 한계 | 명확히 식별된 내부 벤치마크 안에서 편집자 어조 적합성, 상대 순위와 대본당 비용을 측정합니다 | Benchmark |
| [에이전트 도구로 Paper Mario풍 게임 만들기](#case-9) | 인터랙티브 게임과 3D | Kimi K3를 에이전트 harness와 에셋 도구에 결합해 2D와 3D 게임 요소를 모두 만듭니다 | Demo |
| [플래피 게임의 디자인, 비용과 난이도 비교하기](#case-10) | 평가와 한계 | 생성된 게임을 비교할 때 난이도 설정, 비용, 디자인과 게임플레이 기능을 기록합니다 | Benchmark |
| [지하철 배경의 1인칭 슈팅 게임 생성하기](#case-11) | 인터랙티브 게임과 3D | 구체적인 지하철 배경으로 생성된 1인칭 슈팅 결과를 살펴봅니다 | Demo |
| [같은 디자인 프롬프트로 게임 디자인 비교하기](#case-12) | 평가와 한계 | 디자인 프롬프트를 고정하고 속도, 디자인 감각과 게임플레이 느낌을 따로 살펴봅니다 | Benchmark |
| [통계 감사에 독립적 검토 요구하기](#case-13) | 평가와 한계 | 모델이 생성한 통계 감사를 신뢰하기 전에 독립 전문가나 다른 모델의 검토와 결합합니다 | Limit |
| [모션 디자인을 전적으로 코드로 만들기](#case-14) | 프론트엔드와 모션 디자인 | 보조 생성 도구 없이 원샷 코딩 워크플로가 모션 디자인을 만들 수 있는지 시험합니다 | Demo |
| [인물을 조사해 애니메이션 개인 사이트 만들기](#case-15) | 프론트엔드와 모션 디자인 | 폭넓은 개인 사이트 요청을 준 뒤 모델의 조사, 계획, 반복과 브라우저 검증을 살펴봅니다 | Tutorial |
| [느리지만 강한 프론트엔드 실행 평가하기](#case-16) | 평가와 한계 | 프론트엔드 과제를 시험할 때 출력 품질과 함께 완료 시간을 기록합니다 | Evaluation |
| [블랙홀 시뮬레이션 생성하기](#case-17) | 프론트엔드와 모션 디자인 | 과학 시각화 과제로 생성된 블랙홀 시뮬레이션을 살펴봅니다 | Demo |
| [작동하는 macOS를 갖춘 가상 MacBook 만들기](#case-18) | 코딩과 통합 | Three.js 하드웨어 렌더링과 인터랙티브 브라우저 운영체제 시뮬레이션을 결합합니다 | Demo |
| [Blender MCP로 V8 엔진 모델링하기](#case-19) | 인터랙티브 게임과 3D | Blender MCP와 하나의 요청을 사용해 세밀한 기계식 3D 모델을 생성합니다 | Integration |
| [복선 실패를 중심으로 추리소설 쓰기 시험하기](#case-20) | 평가와 한계 | 생성된 미스터리가 단서, 난해함과 복선의 균형을 맞추는지 평가합니다 | Limit |
| [Millennium Falcon 모델링과 애니메이션 비교하기](#case-21) | 평가와 한계 | 동일한 스타일 요청과 effort 설정으로 3D 모델링, 애니메이션, 시간과 비용을 비교합니다 | Benchmark |
| [복잡한 프론트엔드 모델링, 파티클과 셰이더 시험하기](#case-22) | 프론트엔드와 모션 디자인 | 공개 프론트엔드 프롬프트로 모델링 정밀도, 파티클 효과와 인라인 셰이더 생성을 한 번에 살펴봅니다 | Demo |
| [참조 하나로 플레이 가능한 전투 아레나 만들기](#case-23) | 인터랙티브 게임과 3D | 참조 하나를 사용해 완전한 플레이 가능 아레나의 원샷 생성을 시험합니다 | Demo |
| [스스로 플레이하는 레트로 게임 3개를 HTML 파일로 만들기](#case-24) | 인터랙티브 게임과 3D | 독립형 HTML 게임 파일 안에 그래픽, 적, 규칙과 자율 플레이를 요구합니다 | Benchmark |
| [DSL에서 PTX까지 GPU 컴파일러 만들기](#case-25) | 코딩과 통합 | DSL, 컴파일러 패스, PTX 생성과 Tensor Core 경로를 아우르는 엔드투엔드 컴파일러 과제를 사용합니다 | Demo |
| [한 번에 절차적 음악 도구 생성하기](#case-26) | 프론트엔드와 모션 디자인 | 인터랙티브 절차적 음악 생성기의 원샷 생성을 시험하고 보이는 결과를 신중하게 비교합니다 | Demo |
| [원샷 카멜레온 숨바꼭질 게임 만들기](#case-27) | 인터랙티브 게임과 3D | 색상 맞추기, 절차적 구역, 소리와 여러 라운드 점수를 갖춘 단일 파일 게임을 생성합니다 | Benchmark |
| [Kimi K3 프로젝트 10개 모음 검토하기](#case-28) | 평가와 한계 | 연결된 프로젝트 모음에서 구체적 결과물을 찾고 각각 별도로 검증합니다 | Evaluation |
| [고급 랜딩 페이지를 네 모델로 비교하기](#case-29) | 평가와 한계 | 랜딩 페이지 요청을 고정하고 모델 출력의 애니메이션 깊이와 완성도를 살펴봅니다 | Evaluation |
| [레트로 게임 메커니즘과 비용 벤치마크하기](#case-30) | 평가와 한계 | 동일한 레트로 게임 과제에서 게임플레이, 물리, 메커니즘, 자율 행동, 토큰 사용량과 비용을 비교합니다 | Benchmark |
| [Fable 5와 게임 생성 비교하기](#case-31) | 평가와 한계 | 나란히 제시된 생성 게임 사례를 폭넓은 모델 판정이 아닌 좁은 범위의 평가로 사용합니다 | Evaluation |
| [WebGL2로 실시간 블랙홀 레이트레이서 만들기](#case-32) | 코딩과 통합 | 단일 HTML 파일 안에서 네이티브 WebGL2 측지선 레이트레이서의 원프롬프트 생성을 시험합니다 | Benchmark |
| [이미지 두 장으로 Three.js 제품 페이지 만들기](#case-33) | 프론트엔드와 모션 디자인 | 참조 이미지 두 장과 명시적인 Three.js 요구 사항을 사용해 제품 프레젠테이션을 생성합니다 | Demo |
| [Opus 4.8과 복잡한 프론트엔드·개발 과제 비교하기](#case-34) | 평가와 한계 | 하나의 모델이 보편적으로 우월하다고 선언하지 않고 여러 복잡한 코딩 과제에서 승패를 식별합니다 | Evaluation |
| [벤치마크와 랜딩 페이지 시험 함께 검토하기](#case-35) | 평가와 한계 | 벤치마크 맥락과 구체적인 랜딩 페이지 생성 시험을 결합하되 두 근거 유형을 구분합니다 | Evaluation |
| [에이전트 툴체인으로 2.5D Paper Mario풍 게임 만들기](#case-36) | 인터랙티브 게임과 3D | Kimi K3를 Grok Build 또는 Claude Code, Spriterrific과 함께 사용해 2.5D 게임 워크플로를 구성합니다 | Tutorial |
| [그래프-수식 과제로 귀납 추론 평가하기](#case-37) | 평가와 한계 | 1차 논리 귀납 과제에서 정확도, 홀드아웃 동작과 수식 복잡도를 측정합니다 | Benchmark |
| [보고된 게임, 랜딩 페이지, 3D 작업과 긴 컨텍스트 검토하기](#case-38) | 평가와 한계 | 여러 출처의 모음으로 구체적 결과물을 비교하고 비용 주장과 함께 속도 한계를 기록합니다 | Evaluation |
| [고급 빵 절단기와 제품 페이지 발명하기](#case-39) | 프론트엔드와 모션 디자인 | 제품 아이디어, 분해도, 시연과 랜딩 페이지를 하나의 디자인 결과물로 결합합니다 | Demo |
| [복잡한 계획을 감사하고 해결책에 이의 제기하기](#case-40) | 평가와 한계 | 두 번째 모델로 축소 보고된 발견, 잘못된 해결책과 거부해야 할 결론을 식별합니다 | Evaluation |
| [PPO 방식 강화학습 ASCII 다이어그램 비교하기](#case-41) | 평가와 한계 | ASCII 다이어그램 프롬프트를 고정하고 모델이 강화학습 루프를 표현하는 방식을 비교합니다 | Evaluation |
| [용량 오류를 추적하며 Blender 모델링하기](#case-42) | 평가와 한계 | 결과물만 보지 않고 Blender의 부분적 진행 상황과 서비스 안정성을 함께 평가합니다 | Limit |
| [브라우저 기반 3D 무협 RPG 만들기](#case-43) | 인터랙티브 게임과 3D | 근접 전투, 퀘스트, 인벤토리, 날씨, 실내 공간, Blender 환경 작업과 수정된 에셋을 결합합니다 | Demo |
| [브라우저 멀티플레이 Minecraft풍 게임 만들기](#case-44) | 인터랙티브 게임과 3D | 시간과 비용 범위를 정한 실행으로 플레이 가능한 온라인 멀티플레이 브라우저 게임을 만듭니다 | Demo |
| [10초짜리 재귀적 펠리컨 GIF 생성하기](#case-45) | 프론트엔드와 모션 디자인 | 완전히 명시된 반복 애니메이션 요구로 GIF의 서사적 연속성과 재귀를 살펴봅니다 | Demo |
| [mGBA WASM 기반 Game Boy Advance 에뮬레이터 만들기](#case-46) | 코딩과 통합 | 라이선스가 있는 3D 모델과 실제 에뮬레이터 코어를 통합하고 인터페이스와 게임플레이를 재귀적으로 개선합니다 | Integration |
| [아레나에서 Flappy Bird 생성 비교하기](#case-47) | 평가와 한계 | 아레나 과제로 생성된 Flappy Bird 결과 두 개를 비교하되 판단을 해당 과제 범위로 제한합니다 | Evaluation |
| [화면 분할 협동 브라우저 게임 재현하기](#case-48) | 인터랙티브 게임과 3D | 하나의 요청으로 브라우저 기반 화면 분할 협동과 실시간 환경 상호작용을 생성합니다 | Demo |
| [Command Code 디자인 모드로 플레이 가능한 게임 생성하기](#case-49) | 인터랙티브 게임과 3D | Command Code의 디자인 명령으로 원샷 게임 빌드를 수행하고 결과가 플레이 가능한지 기록합니다 | Demo |
| [중국어 출처로 여러 주제 조사하기](#case-50) | 코딩과 통합 | 장시간 연구 과제로 모델 세대 간 조사 충실도와 지연 시간을 비교합니다 | Evaluation |
| [일관성 있는 무협 브라우저 RPG 조립하기](#case-51) | 인터랙티브 게임과 3D | 이동, 전투, 퀘스트, 인벤토리, 날씨, 탐험과 3D 환경 작업을 하나의 게임에 통합합니다 | Demo |
| [도구로 Bongard 시각 귀납 문제 풀기](#case-52) | 평가와 한계 | 도구 사용이 Bongard 추론 과제의 시각적 규칙을 도출하는 데 도움이 되는지 시험합니다 | Evaluation |
| [GPT-5.6 Sol과 프론트엔드 감각·3D 디자인 비교하기](#case-53) | 평가와 한계 | 범위가 정해진 프론트엔드 비교에서 기능, 시각적 감각, 우아함과 3D 구현을 살펴봅니다 | Evaluation |
| [플레이 가능한 Hollow Knight 크로스오버 만들기](#case-54) | 인터랙티브 게임과 3D | 기존 게임 에셋을 사용해 Knight와 Kimi가 싸우는 플레이 가능한 전투를 만듭니다 | Demo |
| [BMW M4 CS 측면 SVG 생성하기](#case-55) | 프론트엔드와 모션 디자인 | 특정 차량과 시점을 사용해 벡터 일러스트레이션 출력을 살펴봅니다 | Demo |
| [작동하는 앱이 포함된 macOS 브라우저 복제본 만들기](#case-56) | 코딩과 통합 | 음악, 브라우저와 이메일 애플리케이션을 포함하는 브라우저 운영체제 시뮬레이션을 만듭니다 | Demo |
| [세 모델의 웹사이트 생성 비교하기](#case-57) | 평가와 한계 | 눈에 보이는 웹사이트 결과로 하나의 시험에서 Kimi K3, Fable 5, GPT-5.6 Sol을 비교합니다 | Evaluation |
| [스크린샷 피드백으로 Gargantua 재현하기](#case-58) | 프론트엔드와 모션 디자인 | 반복 스크린샷을 관찰 자료로 사용해 과학 시각화를 진단하고 개선합니다 | Tutorial |
| [절차적 3D 게임 생성과 비용 비교하기](#case-59) | 평가와 한계 | 모델 간 프롬프트를 고정하고 생성된 룰렛, 슬롯머신과 핀볼 시스템을 실행당 비용과 함께 살펴봅니다 | Benchmark |
| [원샷으로 Fall Guys풍 3D 브라우저 게임 만들기](#case-60) | 인터랙티브 게임과 3D | 원샷 요청으로 플레이 가능한 3D 장애물 게임을 생성하고 프로젝트를 공개해 살펴볼 수 있게 합니다 | Demo |
| [종말 이후 Lisbon FPS 만들고 자체 시험하기](#case-61) | 인터랙티브 게임과 3D | 한 번의 최대 effort 실행으로 플레이 가능한 FPS를 제공하기 전에 테스트, 스크린샷과 반복을 수행합니다 | Demo |
| [작동하는 FaceTime이 포함된 macOS 시뮬레이션 만들기](#case-62) | 코딩과 통합 | 가상 운영체제 과제로 생성된 앱 상호작용이 작동하는지 시험합니다 | Demo |
| [간단한 요청으로 Animal Crossing풍 게임 생성하기](#case-63) | 인터랙티브 게임과 3D | 최소한의 게임 요구로 플레이 가능성, 게임플레이 루프와 패럴랙스 효과를 살펴봅니다 | Demo |
| [이중 과제 프론트엔드 효과 비교기 추가하기](#case-64) | 코딩과 통합 | 완료된 과제 두 개를 선택해 나란히 표시하고 뷰와 상호작용을 동기화하는 도구를 만듭니다 | Tutorial |
| [한 문장 요구로 Mario풍 게임 생성하기](#case-65) | 인터랙티브 게임과 3D | 최소한의 원샷 요청으로 플레이 가능성, 스테이지 디자인, 픽셀 아트와 패럴랙스를 살펴봅니다 | Demo |
| [스크린샷 62장으로 블랙홀 시각화 개선하기](#case-66) | 프론트엔드와 모션 디자인 | 스크린샷 피드백 루프로 여러 번 시각 시뮬레이션을 읽고 진단하며 수정합니다 | Tutorial |
| [작동하는 좀비 1인칭 슈팅 게임 만들기](#case-67) | 인터랙티브 게임과 3D | 구체적인 좀비 슈팅 목표로 완성된 플레이 가능 FPS 결과물을 살펴봅니다 | Demo |
| [포스트트레이닝 마케팅 PDF 만들기](#case-68) | 프론트엔드와 모션 디자인 | 명시된 제품과 결과물 형식을 사용해 마케팅 문서를 생성합니다 | Demo |
| [3D 무기고 장면의 디테일과 조명 비교하기](#case-69) | 평가와 한계 | 범위가 정해진 Kimi K3와 Opus 4.8 비교에서 객체 밀도, 조명과 장면 디테일을 살펴봅니다 | Evaluation |
| [하나의 프롬프트로 사용자 인터페이스 만들기](#case-70) | 프론트엔드와 모션 디자인 | 하나의 요청으로 완전한 UI 디자인을 생성하고 살펴봅니다 | Demo |
| [인디 우주선 게임 만들기](#case-71) | 인터랙티브 게임과 3D | Kimi K3 Standard로 첫 버전을 만든 뒤 일관성, 결함, 시각 품질, 토큰 비용을 비교합니다 | Demo |
| [동일한 Arena 프롬프트로 프런트엔드 비교](#case-72) | 평가와 한계 | 같은 프롬프트와 나란한 출력을 사용해 단일 리더보드 점수 의존을 피합니다 | Benchmark |
| [Summer Engine 게임 자체 테스트](#case-73) | 인터랙티브 게임과 3D | Kimi K3가 게임을 실행하고 스크린샷과 로그를 확인해 같은 세션에서 결함을 수정하게 합니다 | Demo |
| [코딩 에이전트에서 Kimi Code 벤치마크](#case-74) | 평가와 한계 | 여러 코딩 에이전트 테스트와 작업당 비용으로 Kimi K3를 평가하고 프런트엔드 순위 하나를 일반화하지 않습니다 | Benchmark |
| [Kimi를 Codex 서브에이전트로 설정](#case-75) | 코딩과 통합 | Codex가 오케스트레이션을 맡고 프런트엔드 실행은 Kimi K3 OpenCode 서브에이전트에 위임하며 비밀 경계를 명확히 합니다 | Tutorial |
| [Arena와 복구 하네스 결과 비교](#case-76) | 평가와 한계 | Kimi K3가 한 평가에서는 1위, 다른 평가에서는 7위일 수 있으므로 프런트엔드 선호와 저장소 복구를 함께 봅니다 | Benchmark |
| [브라우저 배틀로얄 반복 개선](#case-77) | 인터랙티브 게임과 3D | 기능이 많은 브라우저 게임에는 긴 자율 반복과 목표가 분명한 후속 프롬프트가 필요할 수 있습니다 | Demo |
| [수상작 스타일 웹사이트 만들기](#case-78) | 프론트엔드와 모션 디자인 | 최종 스크린샷뿐 아니라 전체 녹화 세션으로 Kimi K3의 웹사이트 제작 과정을 평가합니다 | Tutorial |
| [ChatLLM으로 간단한 코딩 라우팅](#case-79) | 코딩과 통합 | 간단한 코딩은 Kimi K3로 보내고 어려운 코딩과 디자인은 다른 모델에 배정합니다 | Integration |
| [Prinzbench에서 Kimi K3 벤치마크하기](#case-80) | 평가와 한계 | Prinzbench에서 Kimi K3를 OpenAI o3 등과 비교해 같은 평가표 안에서의 순위와 한계를 보여준다. | Benchmark |
| [메타볼 스크롤 프런트엔드 만들기](#case-81) | 프론트엔드와 모션 디자인 | Kimi K3가 빛나는 메타볼과 스크롤 연동 애니메이션을 포함한 세련된 웹 UI를 구성했다. | Demo |
| [개인 사이트를 여러 모델로 재설계해 비교하기](#case-82) | 프론트엔드와 모션 디자인 | 같은 개인 사이트 재설계 과제에서 Kimi K3를 다른 모델과 나란히 비교해 시각 품질과 구성 차이를 보여준다. | Evaluation |
| [우주 게임 풍경 확장하기](#case-83) | 인터랙티브 게임과 3D | Kimi K3로 우주 게임 장면을 지형, 우주선, 조명까지 포함한 넓은 비주얼로 확장했다. | Demo |
| [Three.js 물리 렌더러 문제 풀기](#case-84) | 인터랙티브 게임과 3D | Kimi K3를 구현 보조로 사용해 Three.js 물리 렌더링 문제를 진전시킨 사례다. | Demo |
| [ISS 디지털 트윈 생성 비교하기](#case-85) | 평가와 한계 | ISS 디지털 트윈 생성 과제에서 Kimi K3와 다른 모델을 비교해 복잡한 3D/과학 시각화의 출력 차이를 보여준다. | Benchmark |
| [인터랙티브 두피 탐색기 만들기](#case-86) | 프론트엔드와 모션 디자인 | Kimi K3가 교육용 인체 두피 시각화 도구를 생성해 설명형 UI 활용 가능성을 보여준다. | Demo |
| [3D 지구본 대시보드 프롬프트 공유하기](#case-87) | 프론트엔드와 모션 디자인 | 공개 프롬프트로 Kimi K3에서 3D 지구본 대시보드형 UI를 만드는 흐름을 보여준다. | Tutorial |
| [브라우저 Counter-Strike를 단일 파일로 만들기](#case-88) | 인터랙티브 게임과 3D | Kimi K3가 단일 HTML 파일로 브라우저용 FPS 스타일 게임을 만든 데모다. | Demo |
| [WebGPU 숲 월드 리뷰하기](#case-89) | 평가와 한계 | Kimi K3가 만든 WebGPU 숲 월드를 평가해 몰입형 3D 장면에서의 표현력과 한계를 보여준다. | Evaluation |
| [유리 집 프롬프트 비교](#case-90) | 평가와 한계 | 같은 건축 장면 프롬프트로 Kimi K3와 Opus 4.8의 분위기, 조명, 공간 완성도를 비교한다. | Evaluation |
| [생성 에셋으로 CS 만들기](#case-91) | 코딩과 통합 | 작은 Counter-Strike식 브라우저 게임을 프로토타이핑할 때 Kimi K3는 게임 코드, GPT Image 2는 에셋에 사용한다. | Integration |
| [복셀 축구 골 벤치마크](#case-92) | 평가와 한계 | 같은 순수 HTML/CSS/JS 축구 애니메이션 프롬프트를 두 모델에 실행해 움직임 품질과 비용을 비교한다. | Benchmark |
| [Minecraft 벤치마크 검토](#case-93) | 평가와 한계 | 출시 hype나 가격만으로 판단하기 전에 구조화된 Minecraft 리뷰를 확인한다. | Benchmark |
| [다섯 가지 UI UX 테스트 실행](#case-94) | 프론트엔드와 모션 디자인 | frontend 스크린샷 하나 대신 UI, 로고, Figma MCP 작업 여러 개로 Kimi K3를 평가한다. | Evaluation |
| [Command Code Design skill 사용](#case-95) | 코딩과 통합 | 토큰 예산 안에서 시각적 게임 프로토타입을 만들 때 Kimi K3와 Command Code의 전용 design skill을 결합한다. | Integration |
| [피라미드 탐험 게임 만들기](#case-96) | 인터랙티브 게임과 3D | Kimi K3로 하루 동안 3D 탐험 게임을 만든 뒤 퀘스트, 내부 공간, 탐험 범위를 보고 품질을 판단한다. | Demo |
| [레퍼런스로 landing 만들기](#case-97) | 프론트엔드와 모션 디자인 | 레퍼런스 보드, Figma AI, Motion Sites와 Kimi K3를 사용해 시각 방향성을 재사용 가능한 landing 섹션으로 바꾼다. | Tutorial |
| [API tier 제한 측정](#case-98) | 평가와 한계 | Kimi K3 agent 실행은 headline 가격뿐 아니라 token, tier, TPM, TPD 기준으로 예산을 잡는다. | Limit |
| [Limbo식 demo 비교](#case-99) | 평가와 한계 | 같은 게임 프로토타입에서 Kimi K3와 Fable 5를 비교하며 플레이 범위, 완성도, 비용, 버그를 본다. | Benchmark |
| [VulcanBench 비용 결과 검토](#case-100) | 평가와 한계 | 이 사례로 Kimi K3가 「VulcanBench 비용 결과 검토」 작업에서 보이는 실제 워크플로, 비용 또는 한계를 평가합니다. | Benchmark |
| [Minecraft 빌드 깊이 비교](#case-101) | 인터랙티브 게임과 3D | 이 사례로 Kimi K3가 「Minecraft 빌드 깊이 비교」 작업에서 보이는 실제 워크플로, 비용 또는 한계를 평가합니다. | Evaluation |
| [Fallout FPS 클론 제작](#case-102) | 인터랙티브 게임과 3D | 이 사례로 Kimi K3가 「Fallout FPS 클론 제작」 작업에서 보이는 실제 워크플로, 비용 또는 한계를 평가합니다. | Demo |
| [프리미엄 웹사이트 튜토리얼 따라가기](#case-103) | 프론트엔드와 모션 디자인 | 이 사례로 Kimi K3가 「프리미엄 웹사이트 튜토리얼 따라가기」 작업에서 보이는 실제 워크플로, 비용 또는 한계를 평가합니다. | Tutorial |
| [이중 진자 물리 벤치마크](#case-104) | 평가와 한계 | 이 사례로 Kimi K3가 「이중 진자 물리 벤치마크」 작업에서 보이는 실제 워크플로, 비용 또는 한계를 평가합니다. | Benchmark |
| [데이터센터 RPG 출시](#case-105) | 인터랙티브 게임과 3D | 이 사례로 Kimi K3가 「데이터센터 RPG 출시」 작업에서 보이는 실제 워크플로, 비용 또는 한계를 평가합니다. | Demo |
| [휴머노이드 프론트엔드 비용 비교](#case-106) | 프론트엔드와 모션 디자인 | 이 사례로 Kimi K3가 「휴머노이드 프론트엔드 비용 비교」 작업에서 보이는 실제 워크플로, 비용 또는 한계를 평가합니다. | Benchmark |
| [ReactBench 프로덕션 준비도 검토](#case-107) | 평가와 한계 | 이 사례로 Kimi K3가 「ReactBench 프로덕션 준비도 검토」 작업에서 보이는 실제 워크플로, 비용 또는 한계를 평가합니다. | Benchmark |
| [3D 자동차 게임 제작](#case-108) | 인터랙티브 게임과 3D | 이 사례로 Kimi K3가 「3D 자동차 게임 제작」 작업에서 보이는 실제 워크플로, 비용 또는 한계를 평가합니다. | Demo |
| [Claude Code에서 Kimi K3 실행](#case-109) | 코딩과 통합 | 이 사례로 Kimi K3가 「Claude Code에서 Kimi K3 실행」 작업에서 보이는 실제 워크플로, 비용 또는 한계를 평가합니다. | Integration |
| [AA-Briefcase에서 Kimi K3 평가](#case-110) | 평가와 한계 | 리더보드 주장에 의존하기 전에 AA-Briefcase 결과로 Kimi K3의 지식 작업 에이전트 성능을 판단한다. | Benchmark |
| [Geometry Dash 클론 비교](#case-111) | 인터랙티브 게임과 3D | 같은 요구사항의 게임 build를 비교해 Kimi K3가 모바일 스타일의 playable prototype에 충분한지 판단한다. | Evaluation |
| [Command Code 레트로 게임 테스트](#case-112) | 인터랙티브 게임과 3D | Command Code의 다중 모델 설계 실행으로 Kimi K3의 gameplay 기능과 모델별 비용을 비교한다. | Evaluation |
| [프론트엔드 순위 주의점 점검](#case-113) | 평가와 한계 | Kimi K3의 leaderboard 승리와 더 넓은 coding 및 cost 주장을 분리하는 limitation note로 사용한다. | Limit |
| [StackPerf 아키텍처 결과 비교](#case-114) | 평가와 한계 | StackPerf로 Kimi K3와 Qwen 3.8의 architecture quality, speed, tool-call behavior를 비교한다. | Benchmark |
| [Three.js Kimi-vs-GLM build 비교](#case-115) | 프론트엔드와 모션 디자인 | 같은 procedural Three.js prompts를 Kimi K3와 GLM 5.2에서 실행해 frontend와 3D build behavior를 비교한다. | Benchmark |
| [Space Discoverer 게임 벤치마크](#case-116) | 인터랙티브 게임과 3D | Space Discoverer mini-benchmark로 일반 3D browser game brief에서 모델 출력을 비교한다. | Benchmark |
| [실제 도로 주행 게임 만들기](#case-117) | 인터랙티브 게임과 3D | Kimi K3를 Blender 및 Godot와 결합해 실제 지역 도로 지도를 바탕으로 driving game을 prototype한다. | Demo |
| [Monument Valley prompt 비용 비교](#case-118) | 평가와 한계 | 하나의 Monument Valley-style prompt로 Kimi K3와 경쟁 모델의 visual quality, runtime, cost를 비교한다. | Benchmark |
| [claude-code-router로 Kimi 연결](#case-119) | 코딩과 통합 | 불필요한 proxy mode를 피하면서 claude-code-router로 기존 Claude Code workflow에서 Kimi K3를 시험한다. | Integration |

<a id="games-3d"></a>
## 🎮 인터랙티브 게임과 3D

<a id="case-1"></a>
### Case 1: [하나의 프롬프트로 복셀 레이서 만들기](https://x.com/ivanfioravanti/status/2077763009657627055) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**짧은 장면 아이디어로 레이싱 프로토타입을 만들고 다음 개선 범위를 정합니다**

제작자는 Kimi K3가 공개 프롬프트 하나로 첫 버전을 만들었고 이후 레이서, 결승선, 세부 검토를 추가할 계획이라고 말합니다

**Prompt:**

```text
Voxel star wars pod-racers run
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01-poster.jpg" alt="Case 1 source video poster" height="360"></a>

[Play case 1 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-2"></a>
### Case 2: [같은 프롬프트로 Frogger 비교하기](https://x.com/ivanfioravanti/status/2077754781964054825) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**프롬프트를 고정해 모델 출력 차이를 살펴봅니다**

제작자는 동일 프롬프트 비교로 Kimi K3 버전을 공유했지만 프롬프트 본문과 평가 기준은 공개하지 않았습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02-poster.jpg" alt="Case 2 source video poster" height="360"></a>

[Play case 2 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-3"></a>
### Case 3: [Frogger와 플레이 녹화 생성하기](https://x.com/TheAhmadOsman/status/2077776567292338285) (by [@TheAhmadOsman](https://x.com/TheAhmadOsman))

**게임과 녹화 흐름을 각각 원샷으로 시험합니다**

제작자는 게임과 녹화 흐름을 각각 한 번에 만들었다고 보고합니다. 정확한 프롬프트는 없습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03-poster.jpg" alt="Case 3 source video poster" height="360"></a>

[Play case 3 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-4"></a>
### Case 4: [Three.js 항공모함 프로토타입 만들기](https://x.com/HarshithLucky3/status/2077753222018814360) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**구체적인 이착함 장면으로 인터랙티브 3D 생성을 시험합니다**

제작자는 니미츠급 항공모함의 전투기 발진과 회수 장면을 보여 주며 3D 생성을 높이 평가합니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04-poster.jpg" alt="Case 4 source video poster" height="360"></a>

[Play case 4 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-9"></a>
### Case 9: [에이전트 도구로 Paper Mario풍 게임 만들기](https://x.com/chongdashu/status/2077886028866531655) (by [@chongdashu](https://x.com/chongdashu))

**Kimi K3를 에이전트 harness와 에셋 도구에 결합해 2D와 3D 게임 요소를 모두 만듭니다**

제작자는 Paper Mario풍 게임에 Kimi K3와 Grok Build, 2D 에셋용 Spriterrific, 3D 에셋용 geometry를 사용했다고 보고합니다. 출처는 도구와 skill 사용을 보여 주지만 재사용 가능한 정확한 프롬프트는 공개하지 않습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-09.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-09-poster.jpg" alt="Case 9 source video poster" height="360"></a>

[Play case 9 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-09.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-11"></a>
### Case 11: [지하철 배경의 1인칭 슈팅 게임 생성하기](https://x.com/bijanbowen/status/2077881805751873997) (by [@bijanbowen](https://x.com/bijanbowen))

**구체적인 지하철 배경으로 생성된 1인칭 슈팅 결과를 살펴봅니다**

제작자는 Kimi K3가 만든 것으로 표시된 지하철 FPS를 보여 주며 인플루언서 지위가 결과에 영향을 주었는지 확신할 수 없다고 명시합니다. 프롬프트나 재현 가능한 워크플로는 제공되지 않습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-11.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-11-poster.jpg" alt="Case 11 source video poster" height="360"></a>

[Play case 11 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-11.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-19"></a>
### Case 19: [Blender MCP로 V8 엔진 모델링하기](https://x.com/aisearchio/status/2077962156147146925) (by [@aisearchio](https://x.com/aisearchio))

**Blender MCP와 하나의 요청을 사용해 세밀한 기계식 3D 모델을 생성합니다**

리뷰어는 Kimi K3가 Blender MCP에서 하나의 프롬프트로 완전한 V8 엔진을 생성했다고 보고합니다. 게시물은 더 긴 리뷰로 연결되지만 제공된 기록에는 정확한 프롬프트가 공개되지 않습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-19.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-19-poster.jpg" alt="Case 19 source video poster" height="360"></a>

[Play case 19 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-19.mp4)

Type: Integration | Date: 2026-07-17

---

<a id="case-23"></a>
### Case 23: [참조 하나로 플레이 가능한 전투 아레나 만들기](https://x.com/VORTEX_Promos/status/2077879705378730074) (by [@VORTEX_Promos](https://x.com/VORTEX_Promos))

**참조 하나를 사용해 완전한 플레이 가능 아레나의 원샷 생성을 시험합니다**

제작자는 Kimi K3가 하나의 참조에서 한 번에 플레이 가능한 전투 아레나를 만들었다고 보고합니다. 게시물에 별도 리더보드 주장도 있지만 구체적 활용 사례는 시연된 아레나 결과물입니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23-poster.jpg" alt="Case 23 source video poster" height="360"></a>

[Play case 23 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23-01.jpg" alt="Case 23 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-24"></a>
### Case 24: [스스로 플레이하는 레트로 게임 3개를 HTML 파일로 만들기](https://x.com/rohanpaul_ai/status/2077889084761206860) (by [@rohanpaul_ai](https://x.com/rohanpaul_ai))

**독립형 HTML 게임 파일 안에 그래픽, 적, 규칙과 자율 플레이를 요구합니다**

출처는 모델들이 Road Fighter, Battle City, Q*bert를 스스로 플레이하는 HTML 파일로 만든 Atomic Chat 비교를 보고합니다. 비용과 품질 비교는 게시자가 보고한 것이며 여기서 독립적으로 재현하지 않았습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-24.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-24-poster.jpg" alt="Case 24 source video poster" height="360"></a>

[Play case 24 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-24.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-27"></a>
### Case 27: [원샷 카멜레온 숨바꼭질 게임 만들기](https://x.com/aimlapi/status/2077898742179459274) (by [@aimlapi](https://x.com/aimlapi))

**색상 맞추기, 절차적 구역, 소리와 여러 라운드 점수를 갖춘 단일 파일 게임을 생성합니다**

AIMLAPI는 숨바꼭질 게임을 같은 프롬프트로 한 번에 비교했다고 보고하며 Kimi K3 $3.11, Fable 5 $12.23의 비용을 제시합니다. 기능과 비용 주장은 공급자가 보고한 결과입니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-27.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-27-poster.jpg" alt="Case 27 source video poster" height="360"></a>

[Play case 27 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-27.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-36"></a>
### Case 36: [에이전트 툴체인으로 2.5D Paper Mario풍 게임 만들기](https://x.com/chongdashu/status/2077981621223837739) (by [@chongdashu](https://x.com/chongdashu))

**Kimi K3를 Grok Build 또는 Claude Code, Spriterrific과 함께 사용해 2.5D 게임 워크플로를 구성합니다**

제작자는 Grok Build와 Kimi K3를 사용하는 전체 워크스루를 제공하고 Spriterrific을 통한 스프라이트 생성을 보여 줍니다. 출처는 도구를 밝히지만 재사용 가능한 정확한 프롬프트는 제공하지 않습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-36.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-36-poster.jpg" alt="Case 36 source video poster" height="360"></a>

[Play case 36 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-36.mp4)

Type: Tutorial | Date: 2026-07-17

---

<a id="case-43"></a>
### Case 43: [브라우저 기반 3D 무협 RPG 만들기](https://x.com/AngryTomtweets/status/2077868163136450619) (by [@AngryTomtweets](https://x.com/AngryTomtweets))

**근접 전투, 퀘스트, 인벤토리, 날씨, 실내 공간, Blender 환경 작업과 수정된 에셋을 결합합니다**

출처는 근접 전투, 퀘스트, 인벤토리, 동적 날씨와 탐험 가능한 실내 공간을 갖춘 Kimi K3 브라우저 RPG를 보고하며 Blender 모델링, 충돌 개선, PBR 재텍스처링과 공개 에셋 수정도 포함한다고 설명합니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-43.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-43-poster.jpg" alt="Case 43 source video poster" height="360"></a>

[Play case 43 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-43.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-44"></a>
### Case 44: [브라우저 멀티플레이 Minecraft풍 게임 만들기](https://x.com/Alezander907/status/2077926014710407407) (by [@Alezander907](https://x.com/Alezander907))

**시간과 비용 범위를 정한 실행으로 플레이 가능한 온라인 멀티플레이 브라우저 게임을 만듭니다**

제작자는 Kimi K3가 1시간 동안 $6.57의 비용으로 브라우저에서 플레이 가능한 멀티플레이 Minecraft풍 게임을 만들었다고 보고합니다. 이는 단일 결과물에서 자체 보고한 실행 수치입니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-44.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-44-poster.jpg" alt="Case 44 source video poster" height="360"></a>

[Play case 44 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-44.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-48"></a>
### Case 48: [화면 분할 협동 브라우저 게임 재현하기](https://x.com/ridark_eth/status/2077882889803378969) (by [@ridark_eth](https://x.com/ridark_eth))

**하나의 요청으로 브라우저 기반 화면 분할 협동과 실시간 환경 상호작용을 생성합니다**

제작자는 Kimi K3가 하나의 프롬프트로 It Takes Two풍 브라우저 게임을 만들었으며 Mario와 Luigi가 화면 분할 상태에서 서로와 환경에 실시간으로 상호작용한다고 보고합니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-48.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-48-poster.jpg" alt="Case 48 source video poster" height="360"></a>

[Play case 48 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-48.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-49"></a>
### Case 49: [Command Code 디자인 모드로 플레이 가능한 게임 생성하기](https://x.com/naymur_dev/status/2077873562661335207) (by [@naymur_dev](https://x.com/naymur_dev))

**Command Code의 디자인 명령으로 원샷 게임 빌드를 수행하고 결과가 플레이 가능한지 기록합니다**

제작자는 Command Code 디자인 모드로 원샷 비교를 수행했고 Kimi K3 실행이 $0.038에 플레이 가능한 게임을 만들었다고 보고합니다. 이 비용과 품질 결과는 자체 보고입니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-49.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-49-poster.jpg" alt="Case 49 source video poster" height="360"></a>

[Play case 49 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-49.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-51"></a>
### Case 51: [일관성 있는 무협 브라우저 RPG 조립하기](https://x.com/TokenGremlin/status/2077855657068310620) (by [@TokenGremlin](https://x.com/TokenGremlin))

**이동, 전투, 퀘스트, 인벤토리, 날씨, 탐험과 3D 환경 작업을 하나의 게임에 통합합니다**

출처는 Kimi K3 무협 스타일 브라우저 RPG가 근접 전투, 퀘스트, 인벤토리, 동적 날씨, 탐험 가능한 실내 공간과 일관성 있는 3D 게임플레이 구조를 결합한다고 보고합니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-51.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-51-poster.jpg" alt="Case 51 source video poster" height="360"></a>

[Play case 51 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-51.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-54"></a>
### Case 54: [플레이 가능한 Hollow Knight 크로스오버 만들기](https://x.com/wangfeng0315/status/2077933531200991583) (by [@wangfeng0315](https://x.com/wangfeng0315))

**기존 게임 에셋을 사용해 Knight와 Kimi가 싸우는 플레이 가능한 전투를 만듭니다**

Kimi에서 일한다고 밝힌 제작자는 Hollow Knight 에셋으로 Knight가 Kimi와 싸우는 게임을 만들고 공개 플레이 링크를 제공했다고 보고합니다. 출처와 평가에서 이 소속 관계를 고려해야 합니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54-poster.jpg" alt="Case 54 source video poster" height="360"></a>

[Play case 54 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54-01.jpg" alt="Case 54 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-17

---

<a id="case-60"></a>
### Case 60: [원샷으로 Fall Guys풍 3D 브라우저 게임 만들기](https://x.com/aayushman2703/status/2077857886441783526) (by [@aayushman2703](https://x.com/aayushman2703))

**원샷 요청으로 플레이 가능한 3D 장애물 게임을 생성하고 프로젝트를 공개해 살펴볼 수 있게 합니다**

제작자는 Kimi K3로 Fall Guys풍 브라우저 게임을 한 번에 만들었으며 프롬프트와 GitHub 프로젝트가 출처에 연결되어 있다고 보고합니다. 이 기록은 해당 프롬프트를 재현하지 않습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-60.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-60-poster.jpg" alt="Case 60 source video poster" height="360"></a>

[Play case 60 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-60.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-61"></a>
### Case 61: [종말 이후 Lisbon FPS 만들고 자체 시험하기](https://x.com/goncalo_canhoto/status/2077863166655037668) (by [@goncalo_canhoto](https://x.com/goncalo_canhoto))

**한 번의 최대 effort 실행으로 플레이 가능한 FPS를 제공하기 전에 테스트, 스크린샷과 반복을 수행합니다**

제작자는 Kimi K3가 약 1시간 동안 반복적인 테스트, 스크린샷과 수정을 거쳐 플레이 가능한 종말 이후 Lisbon 브라우저 FPS를 만들었다고 보고합니다. 시간과 과정 세부 정보는 자체 보고입니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-61-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-61-01.jpg" alt="Case 61 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-63"></a>
### Case 63: [간단한 요청으로 Animal Crossing풍 게임 생성하기](https://x.com/gagarot200/status/2077949230287896830) (by [@gagarot200](https://x.com/gagarot200))

**최소한의 게임 요구로 플레이 가능성, 게임플레이 루프와 패럴랙스 효과를 살펴봅니다**

제작자는 Kimi K3가 매우 간단한 프롬프트에서 게임플레이 루프와 패럴랙스 효과를 갖춘 완전히 플레이 가능한 Animal Crossing풍 게임을 만들었다고 보고합니다. 정확한 문구는 제공된 기록에 없습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-63.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-63-poster.jpg" alt="Case 63 source video poster" height="360"></a>

[Play case 63 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-63.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-65"></a>
### Case 65: [한 문장 요구로 Mario풍 게임 생성하기](https://x.com/izutorishima/status/2077939370154475992) (by [@izutorishima](https://x.com/izutorishima))

**최소한의 원샷 요청으로 플레이 가능성, 스테이지 디자인, 픽셀 아트와 패럴랙스를 살펴봅니다**

제작자는 Kimi K3가 하나의 짧은 요구에서 뚜렷한 버그 없이 작동하는 Mario풍 게임을 만들었고 스테이지 구조와 패럴랙스도 포함했다고 보고합니다. 같은 보고는 음악과 그래픽 품질을 비판합니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-01.jpg" alt="Case 65 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-02.jpg" alt="Case 65 source image 2" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-03.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-03.jpg" alt="Case 65 source image 3" height="360"></a>

Type: Demo | Date: 2026-07-17

---

<a id="case-67"></a>
### Case 67: [작동하는 좀비 1인칭 슈팅 게임 만들기](https://x.com/X2worldtech/status/2077902793449296203) (by [@X2worldtech](https://x.com/X2worldtech))

**구체적인 좀비 슈팅 목표로 완성된 플레이 가능 FPS 결과물을 살펴봅니다**

출처는 Kimi K3가 만든 것으로 표시된 완전히 작동하는 좀비 FPS를 보여 줍니다. 프롬프트, 구현 세부 정보나 외부 게임플레이 평가는 제공하지 않습니다

> [!WARNING]
> The original source permalink returned HTTP 404 during the 2026-07-17 audit. Attribution and evidence are preserved from the supplied high-confidence source package.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-67.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-67-poster.jpg" alt="Case 67 source video poster" height="360"></a>

[Play case 67 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-67.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-71"></a>
### Case 71: [인디 우주선 게임 만들기](https://x.com/ChrisGPT/status/2078261217924087999) (by [@ChrisGPT](https://x.com/ChrisGPT))

**Kimi K3 Standard로 첫 버전을 만든 뒤 일관성, 결함, 시각 품질, 토큰 비용을 비교합니다**

ChrisGPT는 약 2.50달러의 API 토큰 비용으로 우주선 게임 첫 버전을 만들었다고 보고했습니다. GPT-5.5 첫 버전보다 일관되고 버그가 적었지만 Fable 5의 시각적 완성도가 더 높았습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-71.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-71-poster.jpg" alt="Case 71 source video poster" height="360"></a>

[Play case 71 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-71.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-73"></a>
### Case 73: [Summer Engine 게임 자체 테스트](https://x.com/MathiasHeide/status/2078231589436465199) (by [@MathiasHeide](https://x.com/MathiasHeide))

**Kimi K3가 게임을 실행하고 스크린샷과 로그를 확인해 같은 세션에서 결함을 수정하게 합니다**

Mathias Heide에 따르면 Kimi K3는 27분짜리 한 세션에서 종이비행기 게임을 만들고 실행, 스크린샷, 로그 확인, 버그 수정까지 수행했으며 검은 비행기를 흰색으로 고쳤습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-73.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-73-poster.jpg" alt="Case 73 source video poster" height="360"></a>

[Play case 73 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-73.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-77"></a>
### Case 77: [브라우저 배틀로얄 반복 개선](https://x.com/Ananth7e/status/2078158089929601203) (by [@Ananth7e](https://x.com/Ananth7e))

**기능이 많은 브라우저 게임에는 긴 자율 반복과 목표가 분명한 후속 프롬프트가 필요할 수 있습니다**

Ananth에 따르면 Kimi K3는 130분 이상, 40회 이상의 Chrome 스크린샷 반복으로 PUBG 스타일 게임을 만들고 이후 두 개의 추가 프롬프트로 남은 버그를 수정했습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-77.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-77-poster.jpg" alt="Case 77 source video poster" height="360"></a>

[Play case 77 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-77.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-83"></a>
### Case 83: [우주 게임 풍경 확장하기](https://x.com/startracker/status/2078543423167160342) (by [@startracker](https://x.com/startracker))

**Kimi K3로 우주 게임 장면을 지형, 우주선, 조명까지 포함한 넓은 비주얼로 확장했다.**

공개 이미지는 게임형 SF 장면을 보여 주며, Kimi K3가 공간 깊이, 여러 오브젝트, 색감을 함께 처리할 수 있음을 보여 주는 데모다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-83.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-83-poster.jpg" alt="Case 83 source video poster" height="360"></a>

[Play case 83 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-83.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-84"></a>
### Case 84: [Three.js 물리 렌더러 문제 풀기](https://x.com/mattwatkajtys/status/2078523373861339475) (by [@mattwatkajtys](https://x.com/mattwatkajtys))

**Kimi K3를 구현 보조로 사용해 Three.js 물리 렌더링 문제를 진전시킨 사례다.**

작성자는 막혀 있던 3D 렌더링 문제를 Kimi K3로 해결했다고 설명하고, 브라우저에서 동작하는 물리 장면을 영상으로 제시한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-84.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-84-poster.jpg" alt="Case 84 source video poster" height="360"></a>

[Play case 84 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-84.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-88"></a>
### Case 88: [브라우저 Counter-Strike를 단일 파일로 만들기](https://x.com/prasenx/status/2078453069021659477) (by [@prasenx](https://x.com/prasenx))

**Kimi K3가 단일 HTML 파일로 브라우저용 FPS 스타일 게임을 만든 데모다.**

작성자는 하나의 파일에서 실행되는 Counter-Strike 스타일 게임을 보여 주며, Kimi K3가 게임 루프, 입력, 렌더링, 간단한 UI를 함께 생성할 수 있음을 보여준다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-88.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-88-poster.jpg" alt="Case 88 source video poster" height="360"></a>

[Play case 88 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-88.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-96"></a>
### Case 96: [피라미드 탐험 게임 만들기](https://x.com/ice_bearcute/status/2078828887468056763) (by [@ice_bearcute](https://x.com/ice_bearcute))

**Kimi K3로 하루 동안 3D 탐험 게임을 만든 뒤 퀘스트, 내부 공간, 탐험 범위를 보고 품질을 판단한다.**

ice_bearcute는 Kimi K3만으로 하루 만에 3D Pyramid Expedition 게임을 만들었다고 보고했다. 단순 외부 장면이 아니라 고대 무덤을 탐험하고 퀘스트를 완료할 수 있다고 설명하며, 첨부 미디어가 gameplay 증거를 제공한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-96.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-96-poster.jpg" alt="Case 96 source video poster" height="360"></a>

[Play case 96 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-96.mp4)

Type: Demo | Date: 2026-07-19

---

<a id="case-101"></a>
### Case 101: [Minecraft 빌드 깊이 비교](https://x.com/vikktorrrre/status/2079294696459804762) (by [@vikktorrrre](https://x.com/vikktorrrre))

**이 사례로 Kimi K3가 「Minecraft 빌드 깊이 비교」 작업에서 보이는 실제 워크플로, 비용 또는 한계를 평가합니다.**

원본 게시물은 「Minecraft 빌드 깊이 비교」와 관련된 공개 근거를 제공하며 작성자 설명, 결과 미디어 또는 벤치마크/튜토리얼 정보를 포함합니다. 이 저장소는 검증 가능한 사실만 보존하고 공개되지 않은 prompt나 절차는 만들지 않습니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-101.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-101-poster.jpg" alt="Case 101 source video poster" height="360"></a>

[Play case 101 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-101.mp4)

Type: Evaluation | Date: 2026-07-20

---

<a id="case-102"></a>
### Case 102: [Fallout FPS 클론 제작](https://x.com/kirillk_web3/status/2079290747585437781) (by [@kirillk_web3](https://x.com/kirillk_web3))

**이 사례로 Kimi K3가 「Fallout FPS 클론 제작」 작업에서 보이는 실제 워크플로, 비용 또는 한계를 평가합니다.**

원본 게시물은 「Fallout FPS 클론 제작」와 관련된 공개 근거를 제공하며 작성자 설명, 결과 미디어 또는 벤치마크/튜토리얼 정보를 포함합니다. 이 저장소는 검증 가능한 사실만 보존하고 공개되지 않은 prompt나 절차는 만들지 않습니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-102.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-102-poster.jpg" alt="Case 102 source video poster" height="360"></a>

[Play case 102 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-102.mp4)

Type: Demo | Date: 2026-07-20

---

<a id="case-105"></a>
### Case 105: [데이터센터 RPG 출시](https://x.com/demian_ai/status/2079239035596218578) (by [@demian_ai](https://x.com/demian_ai))

**이 사례로 Kimi K3가 「데이터센터 RPG 출시」 작업에서 보이는 실제 워크플로, 비용 또는 한계를 평가합니다.**

원본 게시물은 「데이터센터 RPG 출시」와 관련된 공개 근거를 제공하며 작성자 설명, 결과 미디어 또는 벤치마크/튜토리얼 정보를 포함합니다. 이 저장소는 검증 가능한 사실만 보존하고 공개되지 않은 prompt나 절차는 만들지 않습니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-105.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-105-poster.jpg" alt="Case 105 source video poster" height="360"></a>

[Play case 105 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-105.mp4)

Type: Demo | Date: 2026-07-20

---

<a id="case-108"></a>
### Case 108: [3D 자동차 게임 제작](https://x.com/LexnLin/status/2079233761242235081) (by [@LexnLin](https://x.com/LexnLin))

**이 사례로 Kimi K3가 「3D 자동차 게임 제작」 작업에서 보이는 실제 워크플로, 비용 또는 한계를 평가합니다.**

원본 게시물은 「3D 자동차 게임 제작」와 관련된 공개 근거를 제공하며 작성자 설명, 결과 미디어 또는 벤치마크/튜토리얼 정보를 포함합니다. 이 저장소는 검증 가능한 사실만 보존하고 공개되지 않은 prompt나 절차는 만들지 않습니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-poster.jpg" alt="Case 108 source video poster" height="360"></a>

[Play case 108 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-01.jpg" alt="Case 108 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-02.jpg" alt="Case 108 source image 2" height="360"></a>

Type: Demo | Date: 2026-07-20

---

<a id="case-111"></a>
### Case 111: [Geometry Dash 클론 비교](https://x.com/Nekt_0/status/2079629004483465473) (by [@Nekt_0](https://x.com/Nekt_0))

**같은 요구사항의 게임 build를 비교해 Kimi K3가 모바일 스타일의 playable prototype에 충분한지 판단한다.**

Nekt는 Kimi K3가 약 30분과 200,000 tokens로 점프, 장애물, 레벨, 음악, 시각 효과를 갖춘 Geometry Dash 스타일 클론을 만들었다고 말하며, 첨부 영상에서 Claude Fable 5 build와 비교한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-111.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-111-poster.jpg" alt="Case 111 source video poster" height="360"></a>

[Play case 111 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-111.mp4)

Type: Evaluation | Date: 2026-07-21

---

<a id="case-112"></a>
### Case 112: [Command Code 레트로 게임 테스트](https://x.com/naymur_dev/status/2079627963000398334) (by [@naymur_dev](https://x.com/naymur_dev))

**Command Code의 다중 모델 설계 실행으로 Kimi K3의 gameplay 기능과 모델별 비용을 비교한다.**

Naymur는 Command Code에서 Fable 5, GPT-5.6 Sol, Grok 4.5, Kimi K3에 같은 /design prompt를 실행했다고 보고한다. 게시물은 Kimi K3가 gameplay, level up, bullets, boss fight를 갖춘 ASCII retro game을 만들었고 비용은 $0.15였다고 말한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-112.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-112-poster.jpg" alt="Case 112 source video poster" height="360"></a>

[Play case 112 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-112.mp4)

Type: Evaluation | Date: 2026-07-21

---

<a id="case-116"></a>
### Case 116: [Space Discoverer 게임 벤치마크](https://x.com/fabriciocarraro/status/2079548607393382528) (by [@fabriciocarraro](https://x.com/fabriciocarraro))

**Space Discoverer mini-benchmark로 일반 3D browser game brief에서 모델 출력을 비교한다.**

Fabricio Carraro는 Claude Fable 5, GPT-5.6 Sol, Kimi K3를 최대 reasoning settings로 비교한 mini-benchmark를 보고한다. 과제는 Space Discoverer라는 3D browser game이었고, 세 모델 모두 WebGL 2 위의 Three.js로 수렴했다고 한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-116.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-116-poster.jpg" alt="Case 116 source video poster" height="360"></a>

[Play case 116 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-116.mp4)

Type: Benchmark | Date: 2026-07-21

---

<a id="case-117"></a>
### Case 117: [실제 도로 주행 게임 만들기](https://x.com/bijanbowen/status/2079526003643179102) (by [@bijanbowen](https://x.com/bijanbowen))

**Kimi K3를 Blender 및 Godot와 결합해 실제 지역 도로 지도를 바탕으로 driving game을 prototype한다.**

Bijan Bowen은 Kimi K3가 Blender와 Godot를 사용해 creator 근처의 실제 도로 구간을 map basis로 삼은 driving game을 만드는 모습을 보여준다. 첨부 영상이 build state의 공개 증거다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-117.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-117-poster.jpg" alt="Case 117 source video poster" height="360"></a>

[Play case 117 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-117.mp4)

Type: Demo | Date: 2026-07-21

---


<a id="frontend-motion"></a>
## 🎨 프론트엔드와 모션 디자인

<a id="case-5"></a>
### Case 5: [인터랙티브 모션 그래픽 프론트엔드 만들기](https://x.com/chetaslua/status/2077749371144442022) (by [@chetaslua](https://x.com/chetaslua))

**일시 정지해도 조작 가능한 그래픽을 한 번에 만듭니다**

제작자는 42분, 단순 코드, harness·MCP·skill 없이 한 번에 만들었다고 보고합니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05-poster.jpg" alt="Case 5 source video poster" height="360"></a>

[Play case 5 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-6"></a>
### Case 6: [동기화된 모션 광고 제작하기](https://x.com/abhinavflac/status/2077760297918484667) (by [@abhinavflac](https://x.com/abhinavflac))

**음악, 효과와 움직임의 동기화를 확인합니다**

제작자는 프롬프트만으로 Spotify 스타일 광고를 한 번에 만들었다고 하지만 정확한 프롬프트는 공개하지 않았습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06-poster.jpg" alt="Case 6 source video poster" height="360"></a>

[Play case 6 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-14"></a>
### Case 14: [모션 디자인을 전적으로 코드로 만들기](https://x.com/chetaslua/status/2077952938564354503) (by [@chetaslua](https://x.com/chetaslua))

**보조 생성 도구 없이 원샷 코딩 워크플로가 모션 디자인을 만들 수 있는지 시험합니다**

제작자는 MCP, skill, 도구, 영상 생성이나 특별한 프롬프트 없이 전부 코드로 만든 원샷 Kimi K3 모션 디자인 결과라고 보고합니다. 정확한 프롬프트는 제공되지 않습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-14.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-14-poster.jpg" alt="Case 14 source video poster" height="360"></a>

[Play case 14 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-14.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-15"></a>
### Case 15: [인물을 조사해 애니메이션 개인 사이트 만들기](https://x.com/nicky_sap/status/2077857190707429411) (by [@nicky_sap](https://x.com/nicky_sap))

**폭넓은 개인 사이트 요청을 준 뒤 모델의 조사, 계획, 반복과 브라우저 검증을 살펴봅니다**

제작자는 Kimi K3가 Nick Saponaro를 조사하고 폭넓은 요청으로 애니메이션 개인 웹사이트를 만들었으며 계획, 테스트, 반복과 브라우저 확인까지 수행했다고 보고합니다. 결과는 본인이 보고한 워크플로 시연입니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-15.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-15-poster.jpg" alt="Case 15 source video poster" height="360"></a>

[Play case 15 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-15.mp4)

Type: Tutorial | Date: 2026-07-16

---

<a id="case-17"></a>
### Case 17: [블랙홀 시뮬레이션 생성하기](https://x.com/chetaslua/status/2077961850352971796) (by [@chetaslua](https://x.com/chetaslua))

**과학 시각화 과제로 생성된 블랙홀 시뮬레이션을 살펴봅니다**

제작자는 Kimi K3가 만든 것으로 표시된 블랙홀 시뮬레이션을 보여 주며 자신이 본 것 중 최고라고 말합니다. 출처에는 눈에 보이는 결과가 있지만 프롬프트, 평가 기준이나 독립적 검증은 없습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-17.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-17-poster.jpg" alt="Case 17 source video poster" height="360"></a>

[Play case 17 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-17.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-22"></a>
### Case 22: [복잡한 프론트엔드 모델링, 파티클과 셰이더 시험하기](https://x.com/karminski3/status/2077889959223337099) (by [@karminski3](https://x.com/karminski3))

**공개 프론트엔드 프롬프트로 모델링 정밀도, 파티클 효과와 인라인 셰이더 생성을 한 번에 살펴봅니다**

제작자는 정밀 모델링, 파티클 효과와 복잡한 인라인 셰이더 코드를 다룬 원패스 Kimi K3 프론트엔드 결과라고 보고하며 시험 프롬프트가 연결된 출처에 공개되어 있다고 밝힙니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-22.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-22-poster.jpg" alt="Case 22 source video poster" height="360"></a>

[Play case 22 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-22.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-26"></a>
### Case 26: [한 번에 절차적 음악 도구 생성하기](https://x.com/mirochill/status/2077723551331758478) (by [@mirochill](https://x.com/mirochill))

**인터랙티브 절차적 음악 생성기의 원샷 생성을 시험하고 보이는 결과를 신중하게 비교합니다**

제작자는 Kimi K3가 한 번의 시도로 절차적 음악 도구를 생성했으며 Fable 5와 GPT-5.6 Sol의 결과보다 좋았다고 비교합니다. 이는 제작자 자신의 시험 세트이며 표준화된 벤치마크가 아닙니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-26-poster.jpg" alt="Case 26 source video poster" height="360"></a>

[Play case 26 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-26.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-33"></a>
### Case 33: [이미지 두 장으로 Three.js 제품 페이지 만들기](https://x.com/1littlecoder/status/2077890296806031665) (by [@1littlecoder](https://x.com/1littlecoder))

**참조 이미지 두 장과 명시적인 Three.js 요구 사항을 사용해 제품 프레젠테이션을 생성합니다**

제작자는 Kimi K3가 이미지 두 장으로 제품 페이지를 디자인하고 명시적으로 요청한 Three.js 버전을 만들었다고 보고합니다. 추가 프롬프트나 구현 세부 정보는 제공되지 않습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-33.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-33-poster.jpg" alt="Case 33 source video poster" height="360"></a>

[Play case 33 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-33.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-39"></a>
### Case 39: [고급 빵 절단기와 제품 페이지 발명하기](https://x.com/filicroval/status/2077871090731221438) (by [@filicroval](https://x.com/filicroval))

**제품 아이디어, 분해도, 시연과 랜딩 페이지를 하나의 디자인 결과물로 결합합니다**

제작자는 Kimi K3가 단두대 방식의 빵 절단기를 발명해 고급 제품으로 구성하고 분해도와 시연이 포함된 랜딩 페이지를 만들었다고 보고합니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-39.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-39-poster.jpg" alt="Case 39 source video poster" height="360"></a>

[Play case 39 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-39.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-45"></a>
### Case 45: [10초짜리 재귀적 펠리컨 GIF 생성하기](https://x.com/1littlecoder/status/2077880380900937865) (by [@1littlecoder](https://x.com/1littlecoder))

**완전히 명시된 반복 애니메이션 요구로 GIF의 서사적 연속성과 재귀를 살펴봅니다**

출처에는 자전거를 타는 펠리컨이 카메라 줌인 속에서 문자 메시지로 같은 영상을 받는 10초 반복 GIF 프롬프트가 포함되어 있습니다. 제작자는 Kimi K3의 결과 애니메이션을 보여 줍니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-45.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-45-poster.jpg" alt="Case 45 source video poster" height="360"></a>

[Play case 45 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-45.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-55"></a>
### Case 55: [BMW M4 CS 측면 SVG 생성하기](https://x.com/HarshithLucky3/status/2077765821380886942) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**특정 차량과 시점을 사용해 벡터 일러스트레이션 출력을 살펴봅니다**

제작자는 Kimi K3 Max가 만든 것으로 표시된 BMW M4 CS 측면 SVG를 보여 줍니다. 제공된 출처에는 결과물이 있지만 프롬프트나 제작 단계는 없습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-55-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-55-01.jpg" alt="Case 55 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-58"></a>
### Case 58: [스크린샷 피드백으로 Gargantua 재현하기](https://x.com/AngryTomtweets/status/2077868981659324444) (by [@AngryTomtweets](https://x.com/AngryTomtweets))

**반복 스크린샷을 관찰 자료로 사용해 과학 시각화를 진단하고 개선합니다**

출처는 Kimi K3가 62장의 자체 스크린샷을 사용해 Interstellar의 Gargantua를 재현했으며 각 결과를 읽고 문제를 진단한 뒤 반복적으로 조치했다고 보고합니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-58.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-58-poster.jpg" alt="Case 58 source video poster" height="360"></a>

[Play case 58 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-58.mp4)

Type: Tutorial | Date: 2026-07-16

---

<a id="case-66"></a>
### Case 66: [스크린샷 62장으로 블랙홀 시각화 개선하기](https://x.com/TokenGremlin/status/2077855959201042645) (by [@TokenGremlin](https://x.com/TokenGremlin))

**스크린샷 피드백 루프로 여러 번 시각 시뮬레이션을 읽고 진단하며 수정합니다**

출처는 Kimi K3가 62장의 스크린샷에 걸쳐 출력을 관찰하고 개선해 Interstellar의 Gargantua를 재구성했다고 보고합니다. 이는 독립적인 물리 정확성보다 보고된 피드백 루프를 보여 줍니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-66.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-66-poster.jpg" alt="Case 66 source video poster" height="360"></a>

[Play case 66 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-66.mp4)

Type: Tutorial | Date: 2026-07-16

---

<a id="case-68"></a>
### Case 68: [포스트트레이닝 마케팅 PDF 만들기](https://x.com/Satvik_Pen/status/2077859673517023313) (by [@Satvik_Pen](https://x.com/Satvik_Pen))

**명시된 제품과 결과물 형식을 사용해 마케팅 문서를 생성합니다**

제작자는 Kimi K3에 Thinking Machines의 Inkling 포스트트레이닝에 관한 마케팅 PDF를 요청하고 결과를 공유했으며 배후 과정도 높이 평가합니다. 프롬프트나 평가 기준은 제공되지 않습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-01.png" alt="Case 68 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-02.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-02.png" alt="Case 68 source image 2" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-03.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-03.png" alt="Case 68 source image 3" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-04.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-04.png" alt="Case 68 source image 4" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-70"></a>
### Case 70: [하나의 프롬프트로 사용자 인터페이스 만들기](https://x.com/BrianMRey/status/2077891942088671689) (by [@BrianMRey](https://x.com/BrianMRey))

**하나의 요청으로 완전한 UI 디자인을 생성하고 살펴봅니다**

제작자는 원프롬프트 Kimi K3 실행으로 만든 UI 디자인을 보여 주며 매우 긍정적으로 주관 평가합니다. 정확한 프롬프트와 평가 기준은 포함되지 않습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-70.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-70-poster.jpg" alt="Case 70 source video poster" height="360"></a>

[Play case 70 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-70.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-78"></a>
### Case 78: [수상작 스타일 웹사이트 만들기](https://x.com/viktoroddy/status/2078140696910037002) (by [@viktoroddy](https://x.com/viktoroddy))

**최종 스크린샷뿐 아니라 전체 녹화 세션으로 Kimi K3의 웹사이트 제작 과정을 평가합니다**

Viktor Oddy는 Kimi K3로 수상작 스타일 웹사이트를 만드는 13분 튜토리얼을 공개해 전체 과정의 근거를 제공합니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-78.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-78-poster.jpg" alt="Case 78 source video poster" height="360"></a>

[Play case 78 tutorial video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-78.mp4)

Type: Tutorial | Date: 2026-07-17

---

<a id="case-81"></a>
### Case 81: [메타볼 스크롤 프런트엔드 만들기](https://x.com/abhinavflac/status/2078603131055993130) (by [@abhinavflac](https://x.com/abhinavflac))

**Kimi K3가 빛나는 메타볼과 스크롤 연동 애니메이션을 포함한 세련된 웹 UI를 구성했다.**

작성자는 완성된 동적 프런트엔드를 영상으로 보여 주며, 프롬프트에서 시각 효과, 레이아웃, 애니메이션까지 연결된 결과를 확인할 수 있다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-81.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-81-poster.jpg" alt="Case 81 source video poster" height="360"></a>

[Play case 81 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-81.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-82"></a>
### Case 82: [개인 사이트를 여러 모델로 재설계해 비교하기](https://x.com/fabriciocarraro/status/2078574831466078265) (by [@fabriciocarraro](https://x.com/fabriciocarraro))

**같은 개인 사이트 재설계 과제에서 Kimi K3를 다른 모델과 나란히 비교해 시각 품질과 구성 차이를 보여준다.**

게시물은 여러 모델의 결과를 함께 비교하며 Kimi K3의 디자인 판단, 섹션 구성, 마감 품질을 관찰할 수 있게 한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-82.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-82-poster.jpg" alt="Case 82 source video poster" height="360"></a>

[Play case 82 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-82.mp4)

Type: Evaluation | Date: 2026-07-18

---

<a id="case-86"></a>
### Case 86: [인터랙티브 두피 탐색기 만들기](https://x.com/MiaAI_lab/status/2078508824752017757) (by [@MiaAI_lab](https://x.com/MiaAI_lab))

**Kimi K3가 교육용 인체 두피 시각화 도구를 생성해 설명형 UI 활용 가능성을 보여준다.**

공개 데모는 두피 구조를 탐색하는 인터랙티브 화면이며, 의료·교육 설명 UI를 짧은 입력으로 만들 수 있음을 보여준다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-86.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-86-poster.jpg" alt="Case 86 source video poster" height="360"></a>

[Play case 86 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-86.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-87"></a>
### Case 87: [3D 지구본 대시보드 프롬프트 공유하기](https://x.com/hqmank/status/2078465403349840144) (by [@hqmank](https://x.com/hqmank))

**공개 프롬프트로 Kimi K3에서 3D 지구본 대시보드형 UI를 만드는 흐름을 보여준다.**

게시물에는 참조 프롬프트와 완성 영상이 포함되어 지구본, 데이터 표시, 대시보드 레이아웃을 결합하는 방식을 확인할 수 있다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-87.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-87-poster.jpg" alt="Case 87 source video poster" height="360"></a>

[Play case 87 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-87.mp4)

Type: Tutorial | Date: 2026-07-18

---

<a id="case-94"></a>
### Case 94: [다섯 가지 UI UX 테스트 실행](https://x.com/MAXdeg0/status/2078855257686196399) (by [@MAXdeg0](https://x.com/MAXdeg0))

**frontend 스크린샷 하나 대신 UI, 로고, Figma MCP 작업 여러 개로 Kimi K3를 평가한다.**

MAXdeg0는 Claude Code와 Figma MCP 서버를 사용해 Kimi K3로 다섯 가지 UI/UX 및 로고 디자인 테스트를 했다고 보고했다. 랜딩 페이지 재구성, hero section 재구성, 로고 작업 등이 포함되며, 최소한 landing 작업의 시간과 비용이 구체적으로 제시된다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-94.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-94-poster.jpg" alt="Case 94 source video poster" height="360"></a>

[Play case 94 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-94.mp4)

Type: Evaluation | Date: 2026-07-19

---

<a id="case-97"></a>
### Case 97: [레퍼런스로 landing 만들기](https://x.com/MAXdeg0/status/2078776969072877715) (by [@MAXdeg0](https://x.com/MAXdeg0))

**레퍼런스 보드, Figma AI, Motion Sites와 Kimi K3를 사용해 시각 방향성을 재사용 가능한 landing 섹션으로 바꾼다.**

MAXdeg0는 Pinterest에서 스타일 레퍼런스를 모으고 Figma AI로 룩을 리믹스하거나, UI 레퍼런스와 prompt를 Motion Sites에 넣어 Kimi K3가 페이지를 만들게 하는 흐름을 설명했다. 같은 기법을 다른 섹션에도 재사용할 수 있으며 전체 prompting guide 링크도 제공한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-97.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-97-poster.jpg" alt="Case 97 source video poster" height="360"></a>

[Play case 97 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-97.mp4)

Type: Tutorial | Date: 2026-07-19

---

<a id="case-103"></a>
### Case 103: [프리미엄 웹사이트 튜토리얼 따라가기](https://x.com/_guillecasaus/status/2079258261014908980) (by [@_guillecasaus](https://x.com/_guillecasaus))

**이 사례로 Kimi K3가 「프리미엄 웹사이트 튜토리얼 따라가기」 작업에서 보이는 실제 워크플로, 비용 또는 한계를 평가합니다.**

원본 게시물은 「프리미엄 웹사이트 튜토리얼 따라가기」와 관련된 공개 근거를 제공하며 작성자 설명, 결과 미디어 또는 벤치마크/튜토리얼 정보를 포함합니다. 이 저장소는 검증 가능한 사실만 보존하고 공개되지 않은 prompt나 절차는 만들지 않습니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-103.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-103-poster.jpg" alt="Case 103 source video poster" height="360"></a>

[Play case 103 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-103.mp4)

Type: Tutorial | Date: 2026-07-20

---

<a id="case-106"></a>
### Case 106: [휴머노이드 프론트엔드 비용 비교](https://x.com/ChrisGPT/status/2079236298464796958) (by [@ChrisGPT](https://x.com/ChrisGPT))

**이 사례로 Kimi K3가 「휴머노이드 프론트엔드 비용 비교」 작업에서 보이는 실제 워크플로, 비용 또는 한계를 평가합니다.**

원본 게시물은 「휴머노이드 프론트엔드 비용 비교」와 관련된 공개 근거를 제공하며 작성자 설명, 결과 미디어 또는 벤치마크/튜토리얼 정보를 포함합니다. 이 저장소는 검증 가능한 사실만 보존하고 공개되지 않은 prompt나 절차는 만들지 않습니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-106.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-106-poster.jpg" alt="Case 106 source video poster" height="360"></a>

[Play case 106 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-106.mp4)

Type: Benchmark | Date: 2026-07-20

---

<a id="case-115"></a>
### Case 115: [Three.js Kimi-vs-GLM build 비교](https://x.com/thehypedotnews/status/2079553731218325840) (by [@thehypedotnews](https://x.com/thehypedotnews))

**같은 procedural Three.js prompts를 Kimi K3와 GLM 5.2에서 실행해 frontend와 3D build behavior를 비교한다.**

The Hype는 Kimi K3와 GLM 5.2에 단일 HTML 및 Three.js prompt 3개를 실행했다고 말한다: live CRT canvas texture가 있는 80년대 거실, drivetrain kinematics가 있는 road bike, glass aquarium scene.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-115.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-115-poster.jpg" alt="Case 115 source video poster" height="360"></a>

[Play case 115 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-115.mp4)

Type: Benchmark | Date: 2026-07-21

---


<a id="coding-integrations"></a>
## 💻 코딩과 통합

<a id="case-18"></a>
### Case 18: [작동하는 macOS를 갖춘 가상 MacBook 만들기](https://x.com/scottstts/status/2077890054299541890) (by [@scottstts](https://x.com/scottstts))

**Three.js 하드웨어 렌더링과 인터랙티브 브라우저 운영체제 시뮬레이션을 결합합니다**

출처는 Kimi K3가 Three.js로 가상 MacBook과 작동하는 macOS 스타일 환경을 만들었다고 보고합니다. 결과물은 보여 주지만 구현 단계는 제공하지 않습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-18.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-18-poster.jpg" alt="Case 18 source video poster" height="360"></a>

[Play case 18 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-18.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-25"></a>
### Case 25: [DSL에서 PTX까지 GPU 컴파일러 만들기](https://x.com/rohanpaul_ai/status/2077886618657231220) (by [@rohanpaul_ai](https://x.com/rohanpaul_ai))

**DSL, 컴파일러 패스, PTX 생성과 Tensor Core 경로를 아우르는 엔드투엔드 컴파일러 과제를 사용합니다**

출처는 Kimi K3가 자체 DSL과 패스부터 PTX 생성까지 GPU 컴파일러를 처음부터 만들고 Tensor Core 경로를 Triton과 비교했다고 보고합니다. 제공된 기록에는 독립적인 벤치마크 세부 정보가 없습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-25-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-25-01.png" alt="Case 25 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-32"></a>
### Case 32: [WebGL2로 실시간 블랙홀 레이트레이서 만들기](https://x.com/AlicanKiraz0/status/2077885419744612597) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**단일 HTML 파일 안에서 네이티브 WebGL2 측지선 레이트레이서의 원프롬프트 생성을 시험합니다**

작성자는 네이티브 WebGL2로 작동하는 단일 파일 블랙홀 빛 굴절 레이트레이서를 요구하는 코딩 벤치마크를 설명합니다. 제공된 기록은 과제와 참여 모델을 확인하지만 완전한 독립 결과 감사는 제공하지 않습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-32.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-32-poster.jpg" alt="Case 32 source video poster" height="360"></a>

[Play case 32 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-32.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-46"></a>
### Case 46: [mGBA WASM 기반 Game Boy Advance 에뮬레이터 만들기](https://x.com/teortaxesTex/status/2077925090168062272) (by [@teortaxesTex](https://x.com/teortaxesTex))

**라이선스가 있는 3D 모델과 실제 에뮬레이터 코어를 통합하고 인터페이스와 게임플레이를 재귀적으로 개선합니다**

인용된 Kimi K3 프로젝트는 라이선스가 있는 AGB-001 모델을 수정하고 mGBA WASM 코어를 통합해 재귀적 자기 개선으로 인터페이스와 게임플레이를 향상합니다. 게시물은 독립적 재현이 아니라 프로젝트 설명을 인용합니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-46-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-46-01.jpg" alt="Case 46 source image 1" height="360"></a>

Type: Integration | Date: 2026-07-17

---

<a id="case-50"></a>
### Case 50: [중국어 출처로 여러 주제 조사하기](https://x.com/tphuang/status/2077911994607239400) (by [@tphuang](https://x.com/tphuang))

**장시간 연구 과제로 모델 세대 간 조사 충실도와 지연 시간을 비교합니다**

작성자는 중국어 출처를 사용하는 여러 연구 주제에서 Kimi K3를 시험해 K2.6보다 철저하지만 더 느렸다고 보고합니다. 당시 서비스 수요가 매우 높았다는 점도 덧붙입니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-50-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-50-01.png" alt="Case 50 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-17

---

<a id="case-56"></a>
### Case 56: [작동하는 앱이 포함된 macOS 브라우저 복제본 만들기](https://x.com/twid/status/2077924755357974989) (by [@twid](https://x.com/twid))

**음악, 브라우저와 이메일 애플리케이션을 포함하는 브라우저 운영체제 시뮬레이션을 만듭니다**

출처는 Kimi K3로 음악, 브라우저, 이메일과 기타 기능을 갖춘 브라우저 기반 macOS 복제본을 만들었다고 보고합니다. 구현 세부 정보는 제공하지 않습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-56.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-56-poster.jpg" alt="Case 56 source video poster" height="360"></a>

[Play case 56 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-56.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-62"></a>
### Case 62: [작동하는 FaceTime이 포함된 macOS 시뮬레이션 만들기](https://x.com/LinearUncle/status/2077919552239997078) (by [@LinearUncle](https://x.com/LinearUncle))

**가상 운영체제 과제로 생성된 앱 상호작용이 작동하는지 시험합니다**

제작자는 Kimi K3가 만든 것으로 표시된 macOS 스타일 환경을 보여 주고 FaceTime 기능이 작동한다고 보고합니다. 출처에는 설정이나 검증 단계가 없습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-62-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-62-01.jpg" alt="Case 62 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-17

---

<a id="case-64"></a>
### Case 64: [이중 과제 프론트엔드 효과 비교기 추가하기](https://x.com/MinLiBuilds/status/2077939461510615376) (by [@MinLiBuilds](https://x.com/MinLiBuilds))

**완료된 과제 두 개를 선택해 나란히 표시하고 뷰와 상호작용을 동기화하는 도구를 만듭니다**

제작자는 Kimi K3에 과제 선택, 이중 브라우저 패널, 객체·로밍 모드, 동기화된 시점과 상호작용 테스트를 갖춘 프론트엔드 비교 워크플로를 추가해 달라고 요청했다고 보고합니다. 게시물은 더 넓은 모델 한계도 언급합니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-64.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-64-poster.jpg" alt="Case 64 source video poster" height="360"></a>

[Play case 64 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-64.mp4)

Type: Tutorial | Date: 2026-07-17

---

<a id="case-75"></a>
### Case 75: [Kimi를 Codex 서브에이전트로 설정](https://x.com/nauczymycieAI/status/2078181182701736132) (by [@nauczymycieAI](https://x.com/nauczymycieAI))

**Codex가 오케스트레이션을 맡고 프런트엔드 실행은 Kimi K3 OpenCode 서브에이전트에 위임하며 비밀 경계를 명확히 합니다**

nauczymycieAI는 OpenCode 설치 확인, Codex에 붙여 넣지 않는 Kimi API 키 수동 생성, Kimi K3 연결, 프런트엔드 작업을 라우팅하는 전역 Codex skill 생성 절차를 공개했습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-75.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-75.jpg" alt="Case 75 source image 1" height="360"></a>

Type: Tutorial | Date: 2026-07-17

---

<a id="case-79"></a>
### Case 79: [ChatLLM으로 간단한 코딩 라우팅](https://x.com/abacusai/status/2078022418661257411) (by [@abacusai](https://x.com/abacusai))

**간단한 코딩은 Kimi K3로 보내고 어려운 코딩과 디자인은 다른 모델에 배정합니다**

Abacus AI는 ChatLLM에서 Kimi K3를 지원하며 간단한 코딩은 Kimi K3, 어려운 코딩은 Fable 5, 디자인은 GPT-5.6 Sol로 라우팅하는 예시를 제시했습니다. 같은 라우터를 ChatLLM, Abacus AI agent, Claude Code에서 사용할 수 있습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-79.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-79.jpg" alt="Case 79 source image 1" height="360"></a>

Type: Integration | Date: 2026-07-17

---

<a id="case-91"></a>
### Case 91: [생성 에셋으로 CS 만들기](https://x.com/karankendre/status/2078938615900688728) (by [@karankendre](https://x.com/karankendre))

**작은 Counter-Strike식 브라우저 게임을 프로토타이핑할 때 Kimi K3는 게임 코드, GPT Image 2는 에셋에 사용한다.**

Karan Kendre는 Counter-Strike식 프로젝트에서 Kimi K3가 게임을 만들고 GPT Image 2가 에셋을 만들었으며 총비용은 약 10달러였다고 보고했다. 소스 영상이 보이는 산출물이므로, 이 항목은 Kimi 단독 벤치마크가 아니라 도구 조합 워크플로로 기록한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-91.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-91-poster.jpg" alt="Case 91 source video poster" height="360"></a>

[Play case 91 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-91.mp4)

Type: Integration | Date: 2026-07-19

---

<a id="case-95"></a>
### Case 95: [Command Code Design skill 사용](https://x.com/MrAhmadAwais/status/2078841789205934547) (by [@MrAhmadAwais](https://x.com/MrAhmadAwais))

**토큰 예산 안에서 시각적 게임 프로토타입을 만들 때 Kimi K3와 Command Code의 전용 design skill을 결합한다.**

Ahmad Awais는 Command Code와 /design skill에서 Kimi K3를 사용해 Forza식 추격 카메라 게임을 만들었다고 보고했다. 세션 비용은 0.97달러였고 도로와 자동차 스케일, 배경, 애니메이션, 안개 수정이 포함되어 구체적인 agent harness 워크플로다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-95.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-95-poster.jpg" alt="Case 95 source video poster" height="360"></a>

[Play case 95 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-95.mp4)

Type: Integration | Date: 2026-07-19

---

<a id="case-109"></a>
### Case 109: [Claude Code에서 Kimi K3 실행](https://x.com/boxmining/status/2079115758618239337) (by [@boxmining](https://x.com/boxmining))

**이 사례로 Kimi K3가 「Claude Code에서 Kimi K3 실행」 작업에서 보이는 실제 워크플로, 비용 또는 한계를 평가합니다.**

원본 게시물은 「Claude Code에서 Kimi K3 실행」와 관련된 공개 근거를 제공하며 작성자 설명, 결과 미디어 또는 벤치마크/튜토리얼 정보를 포함합니다. 이 저장소는 검증 가능한 사실만 보존하고 공개되지 않은 prompt나 절차는 만들지 않습니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-109.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-109-poster.jpg" alt="Case 109 source video poster" height="360"></a>

[Play case 109 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-109.mp4)

Type: Integration | Date: 2026-07-20

---

<a id="case-119"></a>
### Case 119: [claude-code-router로 Kimi 연결](https://x.com/sairahul1/status/2079393675885588855) (by [@sairahul1](https://x.com/sairahul1))

**불필요한 proxy mode를 피하면서 claude-code-router로 기존 Claude Code workflow에서 Kimi K3를 시험한다.**

Sai Rahul은 Moonshot 후원의 claude-code-router Kimi K3 지원을 설명한다. built-in presets, API key 또는 subscription import, native subscription routing, balance/usage dashboard, failover, cache pricing, 그리고 필요하지 않으면 proxy mode를 끄라는 주의가 포함된다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-119.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-119-poster.jpg" alt="Case 119 source video poster" height="360"></a>

[Play case 119 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-119.mp4)

Type: Integration | Date: 2026-07-21

---


<a id="evaluation-limits"></a>
## 🧪 평가와 한계

<a id="case-7"></a>
### Case 7: [BridgeBench 라바 램프 과제로 프론트엔드 디자인 비교하기](https://x.com/bridgemindai/status/2077868061953007908) (by [@bridgemindai](https://x.com/bridgemindai))

**BridgeBench 라바 램프 과제를 보편적 순위가 아닌 범위가 정해진 하나의 프론트엔드 디자인 비교로 사용합니다**

BridgeMind AI는 Kimi K3가 자체 BridgeBench 라바 램프 과제에서 Fable 5를 앞섰고 인용된 아레나에서 1위를 차지했다고 보고합니다. 이는 게시자가 보고한 비교 결과입니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-07.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-07-poster.jpg" alt="Case 7 source video poster" height="360"></a>

[Play case 7 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-07.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-8"></a>
### Case 8: [편집자 어조의 대본 작성 벤치마크하기](https://x.com/Whats_AI/status/2077860441380798908) (by [@Whats_AI](https://x.com/Whats_AI))

**명확히 식별된 내부 벤치마크 안에서 편집자 어조 적합성, 상대 순위와 대본당 비용을 측정합니다**

Whats_AI는 초기 내부 결과로 2,840 Elo, 자체 보드 1위, 대본당 약 $0.25를 보고합니다. 이는 한 조직의 예비 벤치마크이며 일반적인 성능이나 가격 보장이 아닙니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-08-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-08-01.jpg" alt="Case 8 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-16

---

<a id="case-10"></a>
### Case 10: [플래피 게임의 디자인, 비용과 난이도 비교하기](https://x.com/MrAhmadAwais/status/2077915347974557862) (by [@MrAhmadAwais](https://x.com/MrAhmadAwais))

**생성된 게임을 비교할 때 난이도 설정, 비용, 디자인과 게임플레이 기능을 기록합니다**

Command Code의 내부 Flappy 벤치마크는 모델마다 다른 난이도 설정을 사용했으며 Kimi K3 $0.024, Fable 5 $0.42, GPT-5.6 Sol $0.15를 제시합니다. 설정이 동일하지 않으므로 범위가 제한된 내부 비교입니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-10.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-10-poster.jpg" alt="Case 10 source video poster" height="360"></a>

[Play case 10 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-10.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-12"></a>
### Case 12: [같은 디자인 프롬프트로 게임 디자인 비교하기](https://x.com/CommandCodeAI/status/2077921526213746948) (by [@CommandCodeAI](https://x.com/CommandCodeAI))

**디자인 프롬프트를 고정하고 속도, 디자인 감각과 게임플레이 느낌을 따로 살펴봅니다**

Command Code는 Kimi K3, GPT-5.6 Sol, Fable 5를 같은 프롬프트로 비교했다고 보고합니다. 게시물은 Kimi K3가 디자인 감각에서 좋은 성과를 냈고 다른 두 모델은 플레이 속도가 너무 빨랐다고 하지만 이는 게시자의 평가입니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-12.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-12-poster.jpg" alt="Case 12 source video poster" height="360"></a>

[Play case 12 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-12.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-13"></a>
### Case 13: [통계 감사에 독립적 검토 요구하기](https://x.com/emollick/status/2077869293031624793) (by [@emollick](https://x.com/emollick))

**모델이 생성한 통계 감사를 신뢰하기 전에 독립 전문가나 다른 모델의 검토와 결합합니다**

Ethan Mollick는 Kimi K3 Max가 이전 학술 연구를 감사하면서 통계를 잘못 적용했다고 보고하고 별도의 비판에 동의합니다. 이 부정적 사례는 검토 없는 수용보다 독립적 확인이 필요함을 뒷받침합니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-13-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-13-01.jpg" alt="Case 13 source image 1" height="360"></a>

Type: Limit | Date: 2026-07-16

---

<a id="case-16"></a>
### Case 16: [느리지만 강한 프론트엔드 실행 평가하기](https://x.com/Lentils80/status/2077387333154857151) (by [@Lentils80](https://x.com/Lentils80))

**프론트엔드 과제를 시험할 때 출력 품질과 함께 완료 시간을 기록합니다**

제작자는 Kimi K3 프론트엔드 실행에 35분이 걸렸고 해당 프롬프트에서 본 결과 중 최고 수준이라고 평가합니다. 속도와 품질 판단 모두 한 사용자의 관찰입니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-16.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-16-poster.jpg" alt="Case 16 source video poster" height="360"></a>

[Play case 16 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-16.mp4)

Type: Evaluation | Date: 2026-07-15

---

<a id="case-20"></a>
### Case 20: [복선 실패를 중심으로 추리소설 쓰기 시험하기](https://x.com/emollick/status/2077951790868238616) (by [@emollick](https://x.com/emollick))

**생성된 미스터리가 단서, 난해함과 복선의 균형을 맞추는지 평가합니다**

Ethan Mollick는 Kimi K3가 좋은 추리소설을 쓰지 못했고 단서를 너무 명백하면서도 너무 모호하게 만들며 복선에 실패했다고 보고합니다. 다른 모델도 이 한계를 공유한다고 덧붙입니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-01.jpg" alt="Case 20 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-02.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-02.png" alt="Case 20 source image 2" height="360"></a>

Type: Limit | Date: 2026-07-17

---

<a id="case-21"></a>
### Case 21: [Millennium Falcon 모델링과 애니메이션 비교하기](https://x.com/gmi_cloud/status/2077903360263676090) (by [@gmi_cloud](https://x.com/gmi_cloud))

**동일한 스타일 요청과 effort 설정으로 3D 모델링, 애니메이션, 시간과 비용을 비교합니다**

GMI Cloud는 최대 effort에서 픽셀 스타일과 원본 스타일의 Millennium Falcon 재현을 Kimi K3와 Fable 5로 비교했다고 보고합니다. 첫 시험에서 Kimi K3는 더 오래 걸렸지만 비용은 약 3분의 1이었고 다른 시험에서는 절반 미만이었다고 하며 이는 공급자가 보고한 결과입니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-21.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-21-poster.jpg" alt="Case 21 source video poster" height="360"></a>

[Play case 21 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-21.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-28"></a>
### Case 28: [Kimi K3 프로젝트 10개 모음 검토하기](https://x.com/minchoi/status/2077957907857994006) (by [@minchoi](https://x.com/minchoi))

**연결된 프로젝트 모음에서 구체적 결과물을 찾고 각각 별도로 검증합니다**

작성자는 Game Boy Advance 에뮬레이터를 포함해 미디어가 있는 Kimi K3 사례 10개를 큐레이션합니다. 이 기록은 하나의 재현 가능한 워크플로가 아니라 모음이므로 연결된 사례를 각각 독립적으로 확인해야 합니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-28.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-28-poster.jpg" alt="Case 28 source video poster" height="360"></a>

[Play case 28 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-28.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-29"></a>
### Case 29: [고급 랜딩 페이지를 네 모델로 비교하기](https://x.com/doutorcaleb/status/2077904020471947773) (by [@doutorcaleb](https://x.com/doutorcaleb))

**랜딩 페이지 요청을 고정하고 모델 출력의 애니메이션 깊이와 완성도를 살펴봅니다**

제작자는 Kimi K3, Fable, Grok, GPT Terra에 같은 고급 랜딩 페이지 프롬프트를 주었고 Kimi K3 결과가 가장 강했다고 평가합니다. 이는 단일 과제에 대한 자체 보고 비교입니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-29.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-29-poster.jpg" alt="Case 29 source video poster" height="360"></a>

[Play case 29 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-29.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-30"></a>
### Case 30: [레트로 게임 메커니즘과 비용 벤치마크하기](https://x.com/adxtyahq/status/2077860500462055570) (by [@adxtyahq](https://x.com/adxtyahq))

**동일한 레트로 게임 과제에서 게임플레이, 물리, 메커니즘, 자율 행동, 토큰 사용량과 비용을 비교합니다**

출처는 Road Fighter, Battle City, Q*bert의 같은 프롬프트 시험을 보고하며 Kimi K3 $0.28, GPT-5.6 $0.28, Opus 4.8 $0.54를 제시합니다. 이는 게시자의 벤치마크 수치입니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-30.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-30-poster.jpg" alt="Case 30 source video poster" height="360"></a>

[Play case 30 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-30.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-31"></a>
### Case 31: [Fable 5와 게임 생성 비교하기](https://x.com/higgsfield_ai/status/2077943629633712490) (by [@higgsfield_ai](https://x.com/higgsfield_ai))

**나란히 제시된 생성 게임 사례를 폭넓은 모델 판정이 아닌 좁은 범위의 평가로 사용합니다**

Higgsfield는 Kimi K3와 Fable 5의 게임 생성 비교를 제시합니다. 제공된 기록에는 비교 미디어가 있지만 프롬프트, 채점 기준이나 세부 조건은 없습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-31.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-31-poster.jpg" alt="Case 31 source video poster" height="360"></a>

[Play case 31 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-31.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-34"></a>
### Case 34: [Opus 4.8과 복잡한 프론트엔드·개발 과제 비교하기](https://x.com/op7418/status/2077969583018066116) (by [@op7418](https://x.com/op7418))

**하나의 모델이 보편적으로 우월하다고 선언하지 않고 여러 복잡한 코딩 과제에서 승패를 식별합니다**

리뷰어는 Kimi K3와 Opus 4.8을 복잡한 프론트엔드와 개발 과제에서 직접 시험했으며 결과가 엇갈리는 가운데 대체로 비슷하다고 평가합니다. 이는 한 리뷰어의 판단입니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-34.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-34-poster.jpg" alt="Case 34 source video poster" height="360"></a>

[Play case 34 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-34.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-35"></a>
### Case 35: [벤치마크와 랜딩 페이지 시험 함께 검토하기](https://x.com/adamuchigabriel/status/2077880433925120471) (by [@adamuchigabriel](https://x.com/adamuchigabriel))

**벤치마크 맥락과 구체적인 랜딩 페이지 생성 시험을 결합하되 두 근거 유형을 구분합니다**

영상은 Kimi K3의 벤치마크 논의, 랜딩 페이지 시험과 프론트엔드 디자인 관찰을 제시합니다. 제공된 기록에는 전체 시험 프롬프트나 채점 기준이 없습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-35.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-35-poster.jpg" alt="Case 35 source video poster" height="360"></a>

[Play case 35 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-35.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-37"></a>
### Case 37: [그래프-수식 과제로 귀납 추론 평가하기](https://x.com/s_batzoglou/status/2077884096307454119) (by [@s_batzoglou](https://x.com/s_batzoglou))

**1차 논리 귀납 과제에서 정확도, 홀드아웃 동작과 수식 복잡도를 측정합니다**

작성자는 각각 8~10개 요소를 가진 작은 그래프 6~10개에서 1차 논리 수식을 추론하는 ICML INDUCTION 과제로 Kimi K3와 다른 모델을 벤치마크했다고 보고합니다. 게시물은 이전 작업에서 결과를 갱신했다고 하며 여기서는 새로 독립 재현했다고 주장하지 않습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-37-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-37-01.png" alt="Case 37 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-16

---

<a id="case-38"></a>
### Case 38: [보고된 게임, 랜딩 페이지, 3D 작업과 긴 컨텍스트 검토하기](https://x.com/servasyy_ai/status/2077903775113834689) (by [@servasyy_ai](https://x.com/servasyy_ai))

**여러 출처의 모음으로 구체적 결과물을 비교하고 비용 주장과 함께 속도 한계를 기록합니다**

작성자는 게임, 랜딩 페이지, 3D 생성과 긴 컨텍스트 작업에 관한 Kimi K3 시험을 요약하며 시도할 가치는 있지만 아직 Fable 5를 대체하지는 못한다고 결론냅니다. 모든 수치는 이 모음에 포함된 2차 보고입니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-38-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-38-01.jpg" alt="Case 38 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-40"></a>
### Case 40: [복잡한 계획을 감사하고 해결책에 이의 제기하기](https://x.com/doodlestein/status/2077901883637665958) (by [@doodlestein](https://x.com/doodlestein))

**두 번째 모델로 축소 보고된 발견, 잘못된 해결책과 거부해야 할 결론을 식별합니다**

제작자는 Kimi K3가 충분히 다듬어진 계획을 검토해 심각한 문제가 축소 보고되었고 제안된 해결책 약 3분의 1을 수정해야 하며 한 가지 발견은 반박된다고 판단했다고 보고합니다. 이는 해당 감사에서 나온 결과입니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-40-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-40-01.jpg" alt="Case 40 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-41"></a>
### Case 41: [PPO 방식 강화학습 ASCII 다이어그램 비교하기](https://x.com/dejavucoder/status/2077872015856615541) (by [@dejavucoder](https://x.com/dejavucoder))

**ASCII 다이어그램 프롬프트를 고정하고 모델이 강화학습 루프를 표현하는 방식을 비교합니다**

출처는 PPO 방식 강화학습 루프를 ASCII로 그리라는 프롬프트를 제공하고 Kimi K3 Max와 Fable 5 High 결과를 나란히 보여 줍니다. 판단은 단일 과제의 시각적 비교입니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-01.png" alt="Case 41 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-02.jpg" alt="Case 41 source image 2" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-42"></a>
### Case 42: [용량 오류를 추적하며 Blender 모델링하기](https://x.com/Angaisb_/status/2077910845523214668) (by [@Angaisb_](https://x.com/Angaisb_))

**결과물만 보지 않고 Blender의 부분적 진행 상황과 서비스 안정성을 함께 평가합니다**

제작자는 Kimi K3의 Blender 모델링 진행 상황을 보여 주면서 반복되는 용량 오류도 보고합니다. 제공된 출처에서 작업은 미완성이므로 부분 결과와 안정성 한계를 함께 고려해야 합니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-42-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-42-01.jpg" alt="Case 42 source image 1" height="360"></a>

Type: Limit | Date: 2026-07-17

---

<a id="case-47"></a>
### Case 47: [아레나에서 Flappy Bird 생성 비교하기](https://x.com/jun_song/status/2077396996865003739) (by [@jun_song](https://x.com/jun_song))

**아레나 과제로 생성된 Flappy Bird 결과 두 개를 비교하되 판단을 해당 과제 범위로 제한합니다**

제작자는 Flappy Bird 과제에서 Kimi K3와 Opus 4.8을 비교한 Arena 결과를 보고하고 Kimi K3가 훨씬 낫다고 평가합니다. 기록에는 전체 프롬프트나 평가 기준이 없습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-47.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-47-poster.jpg" alt="Case 47 source video poster" height="360"></a>

[Play case 47 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-47.mp4)

Type: Evaluation | Date: 2026-07-15

---

<a id="case-52"></a>
### Case 52: [도구로 Bongard 시각 귀납 문제 풀기](https://x.com/IntuitMachine/status/2077885406528311561) (by [@IntuitMachine](https://x.com/IntuitMachine))

**도구 사용이 Bongard 추론 과제의 시각적 규칙을 도출하는 데 도움이 되는지 시험합니다**

제작자는 같은 비교에서 Grok 4.5와 Muse Spark 1.1이 풀지 못한 Bongard 문제를 Kimi K3가 도구를 사용해 풀었다고 보고합니다. 이는 한 사용자의 과제 결과이며 일반적인 추론 벤치마크가 아닙니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-52-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-52-01.jpg" alt="Case 52 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-53"></a>
### Case 53: [GPT-5.6 Sol과 프론트엔드 감각·3D 디자인 비교하기](https://x.com/filicroval/status/2077736407506751952) (by [@filicroval](https://x.com/filicroval))

**범위가 정해진 프론트엔드 비교에서 기능, 시각적 감각, 우아함과 3D 구현을 살펴봅니다**

제작자는 Kimi K3와 GPT-5.6 Sol의 프론트엔드 디자인을 비교하고 시각적 감각, 우아함과 3D 역량에서 Kimi K3가 더 강하다고 평가합니다. 이는 주관적이며 과제에 한정된 평가입니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-53.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-53-poster.jpg" alt="Case 53 source video poster" height="360"></a>

[Play case 53 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-53.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-57"></a>
### Case 57: [세 모델의 웹사이트 생성 비교하기](https://x.com/pengchujin/status/2077962916226298340) (by [@pengchujin](https://x.com/pengchujin))

**눈에 보이는 웹사이트 결과로 하나의 시험에서 Kimi K3, Fable 5, GPT-5.6 Sol을 비교합니다**

제작자는 Kimi K3, Fable 5, GPT-5.6 Sol의 웹사이트 생성 비교를 제시합니다. 제공된 기록에는 전체 프롬프트나 채점 기준이 공개되지 않습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-57.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-57-poster.jpg" alt="Case 57 source video poster" height="360"></a>

[Play case 57 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-57.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-59"></a>
### Case 59: [절차적 3D 게임 생성과 비용 비교하기](https://x.com/adxtyahq/status/2077958193511362856) (by [@adxtyahq](https://x.com/adxtyahq))

**모델 간 프롬프트를 고정하고 생성된 룰렛, 슬롯머신과 핀볼 시스템을 실행당 비용과 함께 살펴봅니다**

게시자는 여러 모델의 절차적 3D 게임 비교를 보고하며 Kimi K3 $0.71, Grok 4.5 $0.30 등의 비용을 제시합니다. 모든 순위와 비용은 해당 게시자의 실행 결과로 취급해야 합니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-59.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-59-poster.jpg" alt="Case 59 source video poster" height="360"></a>

[Play case 59 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-59.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-69"></a>
### Case 69: [3D 무기고 장면의 디테일과 조명 비교하기](https://x.com/hakki_alkan/status/2077887013332636032) (by [@hakki_alkan](https://x.com/hakki_alkan))

**범위가 정해진 Kimi K3와 Opus 4.8 비교에서 객체 밀도, 조명과 장면 디테일을 살펴봅니다**

출처는 Kimi K3가 물건이 채워진 선반, 상자와 사실적인 조명이 있는 세밀한 무기고를 만들었고 Opus 4.8은 빈약한 방을 만들었다고 보고합니다. 이는 독립적 벤치마크가 아닌 제3자 비교 보고입니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-69-poster.jpg" alt="Case 69 source video poster" height="360"></a>

[Play case 69 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-69.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-72"></a>
### Case 72: [동일한 Arena 프롬프트로 프런트엔드 비교](https://x.com/arena/status/2078240399517524365) (by [@arena](https://x.com/arena))

**같은 프롬프트와 나란한 출력을 사용해 단일 리더보드 점수 의존을 피합니다**

Arena.ai는 동일한 프롬프트로 Kimi K3와 Fable 5를 비교한 Frontend Code Arena 영상을 공개해 구현과 표현 차이를 같은 조건에서 살펴볼 수 있게 했습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-72.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-72-poster.jpg" alt="Case 72 source video poster" height="360"></a>

[Play case 72 comparison video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-72.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-74"></a>
### Case 74: [코딩 에이전트에서 Kimi Code 벤치마크](https://x.com/ArtificialAnlys/status/2078230240766345330) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**여러 코딩 에이전트 테스트와 작업당 비용으로 Kimi K3를 평가하고 프런트엔드 순위 하나를 일반화하지 않습니다**

Artificial Analysis는 Coding Agent Index 57점 공동 5위, Terminal-Bench v2 84%, DeepSWE 64%, SWE-Atlas-QnA 23%, 작업당 평균 비용 3.18달러를 보고했습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-74.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-74.jpg" alt="Case 74 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-17

---

<a id="case-76"></a>
### Case 76: [Arena와 복구 하네스 결과 비교](https://x.com/AlphaSignalAI/status/2078172629496746183) (by [@AlphaSignalAI](https://x.com/AlphaSignalAI))

**Kimi K3가 한 평가에서는 1위, 다른 평가에서는 7위일 수 있으므로 프런트엔드 선호와 저장소 복구를 함께 봅니다**

AlphaSignal은 Frontend Code Arena 1679점 1위와 달리 7개 모델 복구 하네스에서 67회 중 53회, 79%로 7위를 기록했다고 보고했습니다

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-76.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-76.jpg" alt="Case 76 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-17

---

<a id="case-80"></a>
### Case 80: [Prinzbench에서 Kimi K3 벤치마크하기](https://x.com/deredleritt3r/status/2078606700496773166) (by [@deredleritt3r](https://x.com/deredleritt3r))

**Prinzbench에서 Kimi K3를 OpenAI o3 등과 비교해 같은 평가표 안에서의 순위와 한계를 보여준다.**

게시물은 Kimi K3를 Prinzbench 비교표에 포함해 상위 모델과의 격차, 평가 과제에서의 상대적 강점을 공개 자료로 제시한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-80-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-80-01.png" alt="Case 80 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-18

---

<a id="case-85"></a>
### Case 85: [ISS 디지털 트윈 생성 비교하기](https://x.com/AIsaOneHQ/status/2078519527588200536) (by [@AIsaOneHQ](https://x.com/AIsaOneHQ))

**ISS 디지털 트윈 생성 과제에서 Kimi K3와 다른 모델을 비교해 복잡한 3D/과학 시각화의 출력 차이를 보여준다.**

게시물은 같은 ISS 디지털 트윈 과제에 대한 여러 모델 결과를 비교하며 Kimi K3의 구조 이해와 시각 생성 한계를 확인하게 한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-85.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-85-poster.jpg" alt="Case 85 source video poster" height="360"></a>

[Play case 85 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-85.mp4)

Type: Benchmark | Date: 2026-07-18

---

<a id="case-89"></a>
### Case 89: [WebGPU 숲 월드 리뷰하기](https://x.com/stas_sorokin_/status/2078435840728908093) (by [@stas_sorokin_](https://x.com/stas_sorokin_))

**Kimi K3가 만든 WebGPU 숲 월드를 평가해 몰입형 3D 장면에서의 표현력과 한계를 보여준다.**

게시물은 브라우저에서 동작하는 숲 3D 환경을 영상으로 보여 주며, Kimi K3의 WebGPU/3D 장면 생성 실용성을 판단할 수 있게 한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-89.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-89-poster.jpg" alt="Case 89 source video poster" height="360"></a>

[Play case 89 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-89.mp4)

Type: Evaluation | Date: 2026-07-18

---

<a id="case-90"></a>
### Case 90: [유리 집 프롬프트 비교](https://x.com/RoundtableSpace/status/2079004612070416755) (by [@RoundtableSpace](https://x.com/RoundtableSpace))

**같은 건축 장면 프롬프트로 Kimi K3와 Opus 4.8의 분위기, 조명, 공간 완성도를 비교한다.**

Roundtable Space는 비슷한 가격 조건에서 Kimi K3와 Claude Opus 4.8에 같은 프롬프트를 준 비교를 보고했다. Kimi 결과는 블루아워 유리 집, 따뜻한 실내 조명, 반사되는 수영장, 설계도 디테일로 설명되고, Opus 결과는 더 타이포그래피 중심이며 공간 완성도가 낮다고 정리된다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-90.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-90-poster.jpg" alt="Case 90 source video poster" height="360"></a>

[Play case 90 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-90.mp4)

Type: Evaluation | Date: 2026-07-20

---

<a id="case-92"></a>
### Case 92: [복셀 축구 골 벤치마크](https://x.com/0xzynex/status/2078920667542487230) (by [@0xzynex](https://x.com/0xzynex))

**같은 순수 HTML/CSS/JS 축구 애니메이션 프롬프트를 두 모델에 실행해 움직임 품질과 비용을 비교한다.**

0xzynex는 Kimi K3와 GPT-5.6 Sol High에 드리블, 골, 동적 카메라, 세리머니를 포함한 블록 스타일 축구 장면을 브라우저 코드로 만들게 한 원샷 비교를 보고했다. 게시물은 Kimi가 더 부드러운 움직임과 낮은 비용을 냈다고 말하며, 영상이 비교 산출물을 보존한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-92.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-92-poster.jpg" alt="Case 92 source video poster" height="360"></a>

[Play case 92 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-92.mp4)

Type: Benchmark | Date: 2026-07-19

---

<a id="case-93"></a>
### Case 93: [Minecraft 벤치마크 검토](https://x.com/ashen_one/status/2078892418976666071) (by [@ashen_one](https://x.com/ashen_one))

**출시 hype나 가격만으로 판단하기 전에 구조화된 Minecraft 리뷰를 확인한다.**

ashen_one은 Kimi K3 리뷰 영상을 올렸고, hype와 현실, 벤치마크, 가격, Minecraft 테스트, 첫 실행 버그, 최종 판단 챕터를 포함했다. 하나의 확인 가능한 영상 안에 벤치마크 프레임과 초기 신뢰성 메모가 함께 있어 유용하다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-93.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-93-poster.jpg" alt="Case 93 source video poster" height="360"></a>

[Play case 93 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-93.mp4)

Type: Benchmark | Date: 2026-07-19

---

<a id="case-98"></a>
### Case 98: [API tier 제한 측정](https://x.com/mnmn94253156337/status/2078739859154620497) (by [@mnmn94253156337](https://x.com/mnmn94253156337))

**Kimi K3 agent 실행은 headline 가격뿐 아니라 token, tier, TPM, TPD 기준으로 예산을 잡는다.**

중국어 소스는 5달러를 충전해 Kimi K3 API를 가볍게 시험한 뒤 설정 중 약 1.1달러가 소모되고 Tier0 제한에 걸린 개인 경험을 보고한다. 입력, 캐시 입력, 출력 가격과 TPM/TPD 같은 제한 개념을 함께 제시해 초기 제한 사례로 유용하다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-98.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-98-poster.jpg" alt="Case 98 source video poster" height="360"></a>

[Play case 98 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-98.mp4)

Type: Limit | Date: 2026-07-19

---

<a id="case-99"></a>
### Case 99: [Limbo식 demo 비교](https://x.com/ChrisGPT/status/2078679211116835017) (by [@ChrisGPT](https://x.com/ChrisGPT))

**같은 게임 프로토타입에서 Kimi K3와 Fable 5를 비교하며 플레이 범위, 완성도, 비용, 버그를 본다.**

ChrisGPT는 Limbo 클론 demo에서 Fable 5와 Kimi K3를 비교했다. Fable은 2,400줄과 24K output token에 1.20달러, Kimi는 3,000줄과 30K output token에 0.12달러였고, Kimi는 더 많은 gameplay를 추가했지만 버그도 더 많았다고 보고한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-99.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-99-poster.jpg" alt="Case 99 source video poster" height="360"></a>

[Play case 99 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-99.mp4)

Type: Benchmark | Date: 2026-07-19

---

<a id="case-100"></a>
### Case 100: [VulcanBench 비용 결과 검토](https://x.com/morganlinton/status/2079358902194569357) (by [@morganlinton](https://x.com/morganlinton))

**이 사례로 Kimi K3가 「VulcanBench 비용 결과 검토」 작업에서 보이는 실제 워크플로, 비용 또는 한계를 평가합니다.**

원본 게시물은 「VulcanBench 비용 결과 검토」와 관련된 공개 근거를 제공하며 작성자 설명, 결과 미디어 또는 벤치마크/튜토리얼 정보를 포함합니다. 이 저장소는 검증 가능한 사실만 보존하고 공개되지 않은 prompt나 절차는 만들지 않습니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-100-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-100-01.jpg" alt="Case 100 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-21

---

<a id="case-104"></a>
### Case 104: [이중 진자 물리 벤치마크](https://x.com/AlicanKiraz0/status/2079241239736504768) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**이 사례로 Kimi K3가 「이중 진자 물리 벤치마크」 작업에서 보이는 실제 워크플로, 비용 또는 한계를 평가합니다.**

원본 게시물은 「이중 진자 물리 벤치마크」와 관련된 공개 근거를 제공하며 작성자 설명, 결과 미디어 또는 벤치마크/튜토리얼 정보를 포함합니다. 이 저장소는 검증 가능한 사실만 보존하고 공개되지 않은 prompt나 절차는 만들지 않습니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-104.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-104-poster.jpg" alt="Case 104 source video poster" height="360"></a>

[Play case 104 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-104.mp4)

Type: Benchmark | Date: 2026-07-20

---

<a id="case-107"></a>
### Case 107: [ReactBench 프로덕션 준비도 검토](https://x.com/aidenybai/status/2079233934693650567) (by [@aidenybai](https://x.com/aidenybai))

**이 사례로 Kimi K3가 「ReactBench 프로덕션 준비도 검토」 작업에서 보이는 실제 워크플로, 비용 또는 한계를 평가합니다.**

원본 게시물은 「ReactBench 프로덕션 준비도 검토」와 관련된 공개 근거를 제공하며 작성자 설명, 결과 미디어 또는 벤치마크/튜토리얼 정보를 포함합니다. 이 저장소는 검증 가능한 사실만 보존하고 공개되지 않은 prompt나 절차는 만들지 않습니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-107.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-107-poster.jpg" alt="Case 107 source video poster" height="360"></a>

[Play case 107 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-107.mp4)

Type: Benchmark | Date: 2026-07-20

---

<a id="case-110"></a>
### Case 110: [AA-Briefcase에서 Kimi K3 평가](https://x.com/ArtificialAnlys/status/2079715807983210572) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**리더보드 주장에 의존하기 전에 AA-Briefcase 결과로 Kimi K3의 지식 작업 에이전트 성능을 판단한다.**

Artificial Analysis는 Kimi K3가 AA-Briefcase에서 1543 Elo를 기록해 Claude Fable 5 다음 2위였다고 보고했다. 동시에 이 벤치마크에서는 작업당 평균이 거의 1시간이고 비용이 Opus 4.8보다 높았다고 설명한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-110-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-110-01.jpg" alt="Case 110 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-21

---

<a id="case-113"></a>
### Case 113: [프론트엔드 순위 주의점 점검](https://x.com/RetroChainer/status/2079622227796885850) (by [@RetroChainer](https://x.com/RetroChainer))

**Kimi K3의 leaderboard 승리와 더 넓은 coding 및 cost 주장을 분리하는 limitation note로 사용한다.**

RetroChainer는 Frontend Code Arena 1위와 공개 pricing을 확인한 뒤, 그 순위가 특정 board 기준이고, 게시 시점에는 weights가 공개되지 않았으며, task당 절감 수치는 단일 작업에서 나온 것이고, max reasoning이 작은 작업에서도 tokens를 태울 수 있다고 지적한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-113.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-113-poster.jpg" alt="Case 113 source video poster" height="360"></a>

[Play case 113 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-113.mp4)

Type: Limit | Date: 2026-07-21

---

<a id="case-114"></a>
### Case 114: [StackPerf 아키텍처 결과 비교](https://x.com/tamsi_besson/status/2079573266855834071) (by [@tamsi_besson](https://x.com/tamsi_besson))

**StackPerf로 Kimi K3와 Qwen 3.8의 architecture quality, speed, tool-call behavior를 비교한다.**

Tamsi Besson은 Kimi K3가 StackPerf snapshot에서 Qwen 3.8 Max Preview보다 품질이 약간 높고 전체 실행도 빠르지만, Qwen은 failed tool calls가 0개이고 Kimi는 더 많은 tool calls 중 2개 실패했다고 공유한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-114-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-114-01.jpg" alt="Case 114 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-21

---

<a id="case-118"></a>
### Case 118: [Monument Valley prompt 비용 비교](https://x.com/AiHubMix/status/2079507420083294557) (by [@AiHubMix](https://x.com/AiHubMix))

**하나의 Monument Valley-style prompt로 Kimi K3와 경쟁 모델의 visual quality, runtime, cost를 비교한다.**

AiHubMix는 Claude Fable 5, Kimi K3, GPT-5.6 Sol을 하나의 Monument Valley-style prompt로 비교한다. 게시물은 Fable이 가장 coherent했고, Kimi는 52m30s와 $1.50로 가장 느렸으며, GPT-5.6 Sol은 가장 빠르고 저렴하지만 spatial logic이 약했다고 보고한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-118.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-118-poster.jpg" alt="Case 118 source video poster" height="360"></a>

[Play case 118 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-118.mp4)

Type: Benchmark | Date: 2026-07-21

---

<a id="related-resources"></a>
## 관련 자료

- [EvoLink에서 Kimi K3 세부 정보와 가격 보기](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=landing_overview)
- [EvoLink Kimi K3 API 문서 열기](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=docs_link)
- [EvoLink에서 Kimi K3 자세히 알아보기](https://evolink.ai/blog/is-kimi-k3-available-on-evolink?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_article)
- [KimiK3.io](https://kimik3.io/)
- EvoLink 모델 페이지와 API 문서는 확인되었지만 설치형 Kimi K3 skill은 확인되지 않았습니다

<a id="acknowledge"></a>
## 🙏 감사의 말

Kimi K3 작업을 공개한 모든 제작자에게 감사드립니다

[@ivanfioravanti](https://x.com/ivanfioravanti), [@TheAhmadOsman](https://x.com/TheAhmadOsman), [@HarshithLucky3](https://x.com/HarshithLucky3), [@chetaslua](https://x.com/chetaslua), [@abhinavflac](https://x.com/abhinavflac), [@bridgemindai](https://x.com/bridgemindai), [@Whats_AI](https://x.com/Whats_AI), [@chongdashu](https://x.com/chongdashu), [@MrAhmadAwais](https://x.com/MrAhmadAwais), [@bijanbowen](https://x.com/bijanbowen), [@CommandCodeAI](https://x.com/CommandCodeAI), [@emollick](https://x.com/emollick), [@nicky_sap](https://x.com/nicky_sap), [@Lentils80](https://x.com/Lentils80), [@scottstts](https://x.com/scottstts), [@aisearchio](https://x.com/aisearchio), [@gmi_cloud](https://x.com/gmi_cloud), [@karminski3](https://x.com/karminski3), [@VORTEX_Promos](https://x.com/VORTEX_Promos), [@rohanpaul_ai](https://x.com/rohanpaul_ai), [@mirochill](https://x.com/mirochill), [@aimlapi](https://x.com/aimlapi), [@minchoi](https://x.com/minchoi), [@doutorcaleb](https://x.com/doutorcaleb), [@adxtyahq](https://x.com/adxtyahq), [@higgsfield_ai](https://x.com/higgsfield_ai), [@AlicanKiraz0](https://x.com/AlicanKiraz0), [@1littlecoder](https://x.com/1littlecoder), [@op7418](https://x.com/op7418), [@adamuchigabriel](https://x.com/adamuchigabriel), [@s_batzoglou](https://x.com/s_batzoglou), [@servasyy_ai](https://x.com/servasyy_ai), [@filicroval](https://x.com/filicroval), [@doodlestein](https://x.com/doodlestein), [@dejavucoder](https://x.com/dejavucoder), [@Angaisb_](https://x.com/Angaisb_), [@AngryTomtweets](https://x.com/AngryTomtweets), [@Alezander907](https://x.com/Alezander907), [@teortaxesTex](https://x.com/teortaxesTex), [@jun_song](https://x.com/jun_song), [@ridark_eth](https://x.com/ridark_eth), [@naymur_dev](https://x.com/naymur_dev), [@tphuang](https://x.com/tphuang), [@TokenGremlin](https://x.com/TokenGremlin), [@IntuitMachine](https://x.com/IntuitMachine), [@wangfeng0315](https://x.com/wangfeng0315), [@twid](https://x.com/twid), [@pengchujin](https://x.com/pengchujin), [@aayushman2703](https://x.com/aayushman2703), [@goncalo_canhoto](https://x.com/goncalo_canhoto), [@LinearUncle](https://x.com/LinearUncle), [@gagarot200](https://x.com/gagarot200), [@MinLiBuilds](https://x.com/MinLiBuilds), [@izutorishima](https://x.com/izutorishima), [@X2worldtech](https://x.com/X2worldtech), [@Satvik_Pen](https://x.com/Satvik_Pen), [@hakki_alkan](https://x.com/hakki_alkan), [@BrianMRey](https://x.com/BrianMRey), [@ChrisGPT](https://x.com/ChrisGPT), [@arena](https://x.com/arena), [@MathiasHeide](https://x.com/MathiasHeide), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@nauczymycieAI](https://x.com/nauczymycieAI), [@AlphaSignalAI](https://x.com/AlphaSignalAI), [@Ananth7e](https://x.com/Ananth7e), [@viktoroddy](https://x.com/viktoroddy), [@abacusai](https://x.com/abacusai), [@deredleritt3r](https://x.com/deredleritt3r), [@fabriciocarraro](https://x.com/fabriciocarraro), [@startracker](https://x.com/startracker), [@mattwatkajtys](https://x.com/mattwatkajtys), [@AIsaOneHQ](https://x.com/AIsaOneHQ), [@MiaAI_lab](https://x.com/MiaAI_lab), [@hqmank](https://x.com/hqmank), [@prasenx](https://x.com/prasenx), [@stas_sorokin_](https://x.com/stas_sorokin_), [@RoundtableSpace](https://x.com/RoundtableSpace), [@karankendre](https://x.com/karankendre), [@0xzynex](https://x.com/0xzynex), [@ashen_one](https://x.com/ashen_one), [@MAXdeg0](https://x.com/MAXdeg0), [@ice_bearcute](https://x.com/ice_bearcute), [@mnmn94253156337](https://x.com/mnmn94253156337), [@morganlinton](https://x.com/morganlinton), [@vikktorrrre](https://x.com/vikktorrrre), [@kirillk_web3](https://x.com/kirillk_web3), [@_guillecasaus](https://x.com/_guillecasaus), [@demian_ai](https://x.com/demian_ai), [@aidenybai](https://x.com/aidenybai), [@LexnLin](https://x.com/LexnLin), [@boxmining](https://x.com/boxmining), [@Nekt_0](https://x.com/Nekt_0), [@RetroChainer](https://x.com/RetroChainer), [@tamsi_besson](https://x.com/tamsi_besson), [@thehypedotnews](https://x.com/thehypedotnews), [@AiHubMix](https://x.com/AiHubMix), [@sairahul1](https://x.com/sairahul1)

*출처나 설명 수정이 필요하면 공개 근거와 함께 issue를 열어 주세요*
