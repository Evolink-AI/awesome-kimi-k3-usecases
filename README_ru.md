<div align="center">

<a href="https://evolink.ai/kimi-k3?utm_source=github&utm_medium=banner&utm_campaign=awesome-kimi-k3-usecases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/images/ru-v2.png" alt="Локализованный баннер Kimi K3 с лунным пейзажем и призывом EvoLink" width="760"></a>

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

# Лучшие сценарии использования Kimi K3

## 🍌 Введение

Добро пожаловать в подборку содержательных сценариев Kimi K3

**Мы собираем игры, 3D-сцены, motion-дизайн, интеграции, оценки и практические ограничения, подтвержденные публичными источниками**

Все 129 кейсов взяты из публичных источников с высокой уверенностью. Названия и авторы ведут к оригиналам; слабые, повторные или недостаточно подтвержденные кандидаты исключены

## 📊 Обзор

- 129 надежных кейсов от публичных авторов и практиков
- Игры, 3D, frontend, motion-графика, код, исследования, дизайн и оценка ограничений
- Для каждого сценария сохранены источник, автор, тип, дата и граница prompt
- 31 сценарий со средней достоверностью исключен; отдельные наблюдения не выдаются за benchmark

> [!NOTE]
> Подборка отдает приоритет конкретным доказательствам и не восстанавливает отсутствующие prompts или шаги настройки

<a id="quick-api-access"></a>
## ⚡ Быстрый старт

Документированный EvoLink ID модели — `kimi-k3`; доступны страница модели и документация Chat Completions API

1. [Посмотреть Kimi K3 и цены на EvoLink](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=landing_overview)
2. [Создать или настроить ключ EvoLink API](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-kimi-k3-usecases&utm_content=api_key)

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

[Открыть документацию EvoLink Kimi K3 API](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=first_run)

> [!IMPORTANT]
> Страница модели и документация EvoLink подтверждают публичный маршрут и ID. Отдельная браузерная или no-code поверхность Kimi K3 не подтверждена, и репозиторий не заявляет о независимом платном API-тесте

## 📑 Меню

| Section | Cases |
|---|---|
| [Интерактивные игры и 3D](#games-3d) | 39 |
| [Frontend и motion-дизайн](#frontend-motion) | 27 |
| [Код и интеграции](#coding-integrations) | 16 |
| [Оценка и ограничения](#evaluation-limits) | 47 |
| [Связанные ресурсы](#related-resources) | Связанные ресурсы |
| [Быстрый старт](#quick-api-access) | Быстрый старт |
| [Благодарности](#acknowledge) | Благодарности и исправления |

| Case | Category | What it shows | Type |
|---|---|---|---|
| [Создать voxel pod racer одним prompt](#case-1) | Интерактивные игры и 3D | Использовать короткую идею для прототипа гонки и определить следующую итерацию | Demo |
| [Сравнить Frogger на одном prompt](#case-2) | Интерактивные игры и 3D | Зафиксировать prompt и сравнить различия между моделями | Evaluation |
| [Создать Frogger и запись игры](#case-3) | Интерактивные игры и 3D | Отдельно проверить одношаговую генерацию игры и записи | Demo |
| [Создать прототип авианосца в Three.js](#case-4) | Интерактивные игры и 3D | Проверить интерактивное 3D на конкретной сцене запуска и посадки | Demo |
| [Создать интерактивный motion-frontend](#case-5) | Frontend и motion-дизайн | Сделать графику, которая остается интерактивной на паузе | Demo |
| [Создать синхронизированную motion-рекламу](#case-6) | Frontend и motion-дизайн | Проверить синхронизацию музыки, эффектов и движения | Demo |
| [Сравнить frontend-дизайн в задании BridgeBench с лавовой лампой](#case-7) | Оценка и ограничения | Использовать задание BridgeBench с лавовой лампой как ограниченное сравнение frontend-дизайна, а не универсальный рейтинг | Benchmark |
| [Оценить написание сценариев в редакционном стиле](#case-8) | Оценка и ограничения | Измерять соответствие редакционному голосу, относительное место и стоимость сценария внутри четко обозначенного внутреннего benchmark | Benchmark |
| [Создать игру в духе Paper Mario с агентскими инструментами](#case-9) | Интерактивные игры и 3D | Объединить Kimi K3 с агентским harness и инструментами для ассетов, чтобы получить игровые элементы в 2D и 3D | Demo |
| [Сравнить дизайн, стоимость и сложность игры типа Flappy](#case-10) | Оценка и ограничения | При сравнении сгенерированных игр записывать настройки сложности, стоимость, дизайн и игровые возможности | Benchmark |
| [Создать шутер от первого лица в метро](#case-11) | Интерактивные игры и 3D | Использовать конкретную обстановку метро для проверки сгенерированного шутера от первого лица | Demo |
| [Сравнить игровой дизайн с одним и тем же design prompt](#case-12) | Оценка и ограничения | Зафиксировать design prompt и отдельно проверять темп, чувство дизайна и игровой процесс | Benchmark |
| [Требовать независимую проверку статистического аудита](#case-13) | Оценка и ограничения | Перед использованием выводов дополнять статистический аудит модели независимой экспертной проверкой или проверкой другой моделью | Limit |
| [Создать motion-дизайн полностью кодом](#case-14) | Frontend и motion-дизайн | Проверить, способен ли одношаговый coding workflow создать motion-дизайн без вспомогательных инструментов генерации | Demo |
| [Исследовать человека и создать анимированный персональный сайт](#case-15) | Frontend и motion-дизайн | Дать широкое задание на персональный сайт, затем проверить исследование, планирование, итерации и browser validation модели | Tutorial |
| [Оценить медленный, но сильный frontend-запуск](#case-16) | Оценка и ограничения | При тестировании frontend-задачи записывать время выполнения вместе с качеством результата | Evaluation |
| [Создать симуляцию черной дыры](#case-17) | Frontend и motion-дизайн | Использовать задачу научной визуализации для проверки сгенерированной симуляции черной дыры | Demo |
| [Создать виртуальный MacBook с работающей macOS](#case-18) | Код и интеграции | Объединить Three.js-рендеринг устройства с интерактивной симуляцией операционной системы в браузере | Demo |
| [Смоделировать двигатель V8 через Blender MCP](#case-19) | Интерактивные игры и 3D | Использовать Blender MCP и один запрос для генерации детальной механической 3D-модели | Integration |
| [Проверить детективный текст на провалы с предзнаменованиями](#case-20) | Оценка и ограничения | Оценить, балансирует ли сгенерированный детектив между подсказками, неочевидностью и предзнаменованиями | Limit |
| [Сравнить моделирование и анимацию Millennium Falcon](#case-21) | Оценка и ограничения | Использовать одинаковые запросы по стилю и настройки усилий для сравнения 3D-моделирования, анимации, времени и стоимости | Benchmark |
| [Проверить сложное frontend-моделирование, частицы и shaders](#case-22) | Frontend и motion-дизайн | Использовать публичный frontend prompt, чтобы за один проход проверить точность моделирования, эффекты частиц и генерацию inline shaders | Demo |
| [Создать игровую боевую арену по одному reference](#case-23) | Интерактивные игры и 3D | Использовать один reference для проверки одношаговой генерации полной игровой арены | Demo |
| [Создать три самостоятельно играющие ретроигры в HTML-файлах](#case-24) | Интерактивные игры и 3D | Требовать графику, врагов, правила и автономную игру внутри самостоятельных HTML-файлов | Benchmark |
| [Создать GPU-компилятор от DSL до PTX](#case-25) | Код и интеграции | Использовать сквозную задачу компилятора, охватывающую DSL, compiler passes, генерацию PTX и путь Tensor Core | Demo |
| [Создать инструмент процедурной музыки с одной попытки](#case-26) | Frontend и motion-дизайн | Проверить одношаговую генерацию интерактивного генератора процедурной музыки и осторожно сравнить видимый результат | Demo |
| [Создать одношаговую игру в прятки с хамелеоном](#case-27) | Интерактивные игры и 3D | Создать однофайловую игру с подбором цвета, процедурными зонами, звуком и подсчетом очков по раундам | Benchmark |
| [Обозреть подборку из десяти проектов Kimi K3](#case-28) | Оценка и ограничения | Использовать связанную подборку проектов для поиска конкретных артефактов, которые затем проверяются отдельно | Evaluation |
| [Сравнить продвинутый landing page у четырех моделей](#case-29) | Оценка и ограничения | Зафиксировать запрос на landing page и сравнить глубину анимации и завершенность результатов моделей | Evaluation |
| [Оценить механику и стоимость ретроигр](#case-30) | Оценка и ограничения | Сравнивать игровой процесс, физику, механику, автономное поведение, расход tokens и стоимость на одинаковых ретроигровых задачах | Benchmark |
| [Сравнить генерацию игр с Fable 5](#case-31) | Оценка и ограничения | Использовать параллельный пример сгенерированных игр как узкую оценку, а не общий вердикт о модели | Evaluation |
| [Создать WebGL2 raytracer черной дыры в реальном времени](#case-32) | Код и интеграции | Проверить генерацию по одному prompt нативного WebGL2 geodesic raytracer в одном HTML-файле | Benchmark |
| [Создать product page в Three.js по двум изображениям](#case-33) | Frontend и motion-дизайн | Использовать два reference-изображения и явное требование Three.js для создания презентации продукта | Demo |
| [Сравнить сложные frontend- и development-задачи с Opus 4.8](#case-34) | Оценка и ограничения | Использовать несколько сложных coding-задач для поиска побед и проигрышей, не объявляя одну модель универсально лучшей | Evaluation |
| [Рассмотреть benchmarks и тест landing page](#case-35) | Оценка и ограничения | Объединить контекст benchmark с конкретным тестом генерации landing page, сохраняя раздельность двух типов доказательств | Evaluation |
| [Создать игру в духе Paper Mario в 2.5D с агентским toolchain](#case-36) | Интерактивные игры и 3D | Использовать Kimi K3 с Grok Build или Claude Code и Spriterrific для сборки 2.5D game workflow | Tutorial |
| [Оценить индуктивное рассуждение на задачах граф-в-формулу](#case-37) | Оценка и ограничения | Измерять правильность, поведение на holdout и сложность формулы в задачах first-order induction | Benchmark |
| [Обозреть заявленные игры, landing pages, 3D-работы и long context](#case-38) | Оценка и ограничения | Использовать мульти-source roundup для сравнения конкретных артефактов и отмечать ограничения скорости рядом с заявлениями о стоимости | Evaluation |
| [Изобрести роскошный резак для хлеба и его product page](#case-39) | Frontend и motion-дизайн | Объединить идею продукта, exploded view, демонстрацию и landing page в одном дизайн-артефакте | Demo |
| [Проверить сложный план и оспорить его способы исправления](#case-40) | Оценка и ограничения | Использовать вторую модель для поиска заниженных выводов, неверных remedies и заключений, которые следует отвергнуть | Evaluation |
| [Сравнить ASCII-диаграммы reinforcement-learning цикла в стиле PPO](#case-41) | Оценка и ограничения | Зафиксировать prompt ASCII-диаграммы и сравнить представление reinforcement-learning цикла моделями | Evaluation |
| [Моделировать в Blender с учетом ошибок capacity](#case-42) | Оценка и ограничения | Оценивать частичный прогресс Blender вместе с надежностью сервиса, а не только артефакт | Limit |
| [Создать браузерную 3D wuxia RPG](#case-43) | Интерактивные игры и 3D | Объединить ближний бой, quests, inventory, погоду, interiors, работу со средой Blender и адаптированные assets | Demo |
| [Создать браузерную multiplayer-игру в духе Minecraft](#case-44) | Интерактивные игры и 3D | В ограниченном по времени и стоимости запуске создать игровую онлайн multiplayer-игру для браузера | Demo |
| [Создать десятисекундный рекурсивный GIF с пеликаном](#case-45) | Frontend и motion-дизайн | Использовать полностью заданное описание зацикленной анимации для проверки непрерывности сюжета и рекурсии GIF | Demo |
| [Создать эмулятор Game Boy Advance на основе mGBA WASM](#case-46) | Код и интеграции | Интегрировать лицензированную 3D-модель и настоящее ядро эмулятора, затем рекурсивно улучшать интерфейс и игровой процесс | Integration |
| [Сравнить генерацию Flappy Bird на арене](#case-47) | Оценка и ограничения | Использовать arena-задачу для сравнения двух результатов Flappy Bird, сохраняя оценку специфичной для этой задачи | Evaluation |
| [Воссоздать браузерную кооперативную игру с разделенным экраном](#case-48) | Интерактивные игры и 3D | Одним запросом создать браузерную кооперацию с разделенным экраном и взаимодействием с окружением в реальном времени | Demo |
| [Создать играбельную игру через Design Mode в Command Code](#case-49) | Интерактивные игры и 3D | Использовать design command Command Code для одношаговой сборки игры и записывать, является ли результат играбельным | Demo |
| [Исследовать несколько тем по китайскоязычным источникам](#case-50) | Код и интеграции | Использовать длительные research-задачи для сравнения полноты и latency разных поколений моделей | Evaluation |
| [Собрать целостную браузерную wuxia RPG](#case-51) | Интерактивные игры и 3D | Интегрировать перемещение, бой, quests, inventory, погоду, исследование и работу над 3D-средой в одной игре | Demo |
| [Решить визуальную индуктивную задачу Bongard с инструментом](#case-52) | Оценка и ограничения | Проверить, помогает ли использование инструмента вывести визуальное правило в задаче рассуждения Bongard | Evaluation |
| [Сравнить frontend-вкус и 3D-дизайн с GPT-5.6 Sol](#case-53) | Оценка и ограничения | Проверять возможности, визуальный вкус, элегантность и 3D-исполнение в ограниченном frontend-сравнении | Evaluation |
| [Создать игровую crossover-игру Hollow Knight](#case-54) | Интерактивные игры и 3D | Использовать существующие game assets для создания игровой битвы Knight против Kimi | Demo |
| [Создать SVG BMW M4 CS в боковом ракурсе](#case-55) | Frontend и motion-дизайн | Использовать конкретный автомобиль и ракурс для проверки векторной иллюстрации | Demo |
| [Клонировать macOS в браузере с работающими приложениями](#case-56) | Код и интеграции | Создать браузерную симуляцию операционной системы с приложениями музыки, браузера и email | Demo |
| [Сравнить генерацию сайтов у трех моделей](#case-57) | Оценка и ограничения | Использовать видимые результаты сайтов для сравнения Kimi K3, Fable 5 и GPT-5.6 Sol в одном тесте | Evaluation |
| [Воссоздать Gargantua через обратную связь по скриншотам](#case-58) | Frontend и motion-дизайн | Использовать последовательные скриншоты как наблюдения для диагностики и улучшения научной визуализации | Tutorial |
| [Сравнить процедурную генерацию 3D-игр и стоимость](#case-59) | Оценка и ограничения | Зафиксировать prompt между моделями и проверять сгенерированные системы рулетки, slot machine и pinball со стоимостью каждого запуска | Benchmark |
| [Создать 3D-браузерную игру в духе Fall Guys за один проход](#case-60) | Интерактивные игры и 3D | Одним запросом создать игровую 3D-игру с препятствиями и открыть проект для проверки | Demo |
| [Создать и самостоятельно протестировать апокалиптический FPS в Лиссабоне](#case-61) | Интерактивные игры и 3D | Использовать запуск максимального усилия по одному prompt, который тестирует, делает скриншоты и итерирует до выдачи играбельного FPS | Demo |
| [Создать симуляцию macOS с работающим FaceTime](#case-62) | Код и интеграции | Использовать задачу виртуальной ОС, чтобы проверить работу сгенерированного взаимодействия приложения | Demo |
| [Создать игру в стиле Animal Crossing по простому запросу](#case-63) | Интерактивные игры и 3D | Использовать минимальный game brief для проверки играбельности, gameplay loop и parallax-эффектов | Demo |
| [Добавить frontend-компаратор эффектов двух задач](#case-64) | Код и интеграции | Создать инструмент, который выбирает две завершенные задачи, показывает их рядом и синхронизирует views и interactions | Tutorial |
| [Создать игру в духе Mario по brief из одного предложения](#case-65) | Интерактивные игры и 3D | Минимальным одношаговым запросом проверить играбельность, дизайн уровня, pixel art и parallax | Demo |
| [Улучшить визуализацию черной дыры с помощью 62 скриншотов](#case-66) | Frontend и motion-дизайн | Использовать цикл обратной связи по скриншотам для чтения, диагностики и исправления визуальной симуляции на множестве итераций | Tutorial |
| [Создать работающий zombie-шутер от первого лица](#case-67) | Интерактивные игры и 3D | Использовать конкретную цель zombie-shooter для проверки полного игрового FPS-артефакта | Demo |
| [Создать маркетинговый PDF о post-training](#case-68) | Frontend и motion-дизайн | Использовать названный продукт и формат результата для генерации маркетингового документа | Demo |
| [Сравнить детализацию и освещение 3D-сцены арсенала](#case-69) | Оценка и ограничения | Проверять плотность объектов, освещение и детализацию сцены в ограниченном сравнении Kimi K3 и Opus 4.8 | Evaluation |
| [Создать пользовательский интерфейс по одному prompt](#case-70) | Frontend и motion-дизайн | Использовать один запрос для генерации и проверки полного UI-дизайна | Demo |
| [Создать инди-игру про космический корабль](#case-71) | Интерактивные игры и 3D | Сделать первую версию на Kimi K3 Standard и сравнить связность, ошибки, визуальное качество и стоимость токенов | Demo |
| [Сравнить фронтенды на одинаковых prompt Arena](#case-72) | Оценка и ограничения | Использовать одинаковые prompt и параллельные результаты вместо одного места в рейтинге | Benchmark |
| [Самотестирование игры в Summer Engine](#case-73) | Интерактивные игры и 3D | Дать Kimi K3 запустить игру, проверить скриншоты и логи и исправить видимые дефекты в той же сессии | Demo |
| [Оценить Kimi Code на coding-агентах](#case-74) | Оценка и ограничения | Оценивать Kimi K3 по нескольким тестам и стоимости задачи, не обобщая один frontend-рейтинг | Benchmark |
| [Настроить Kimi как субагента Codex](#case-75) | Код и интеграции | Оставить оркестрацию Codex, а frontend передать субагенту Kimi K3 OpenCode с четкой границей секретов | Tutorial |
| [Сравнить Arena и repair harness](#case-76) | Оценка и ограничения | Смотреть и frontend-предпочтения, и ремонт репозитория, поскольку Kimi K3 может быть первым в одном и седьмым в другом | Benchmark |
| [Итеративно создать браузерную battle royale](#case-77) | Интерактивные игры и 3D | Планировать долгие автономные итерации и точечные дополнительные prompt для функциональной браузерной игры | Demo |
| [Создать сайт в наградном стиле](#case-78) | Frontend и motion-дизайн | Оценивать полную записанную сессию, а не только финальный скриншот | Tutorial |
| [Маршрутизировать простой код через ChatLLM](#case-79) | Код и интеграции | Отправлять простой код Kimi K3, а сложный код и дизайн — другим моделям | Integration |
| [Проверить Kimi K3 в Prinzbench](#case-80) | Оценка и ограничения | Prinzbench сравнивает Kimi K3 с OpenAI o3 и другими моделями, показывая место и ограничения в одном бенчмарке. | Benchmark |
| [Собрать frontend с metaball-анимацией при прокрутке](#case-81) | Frontend и motion-дизайн | Kimi K3 создает аккуратный веб-интерфейс со светящимися metaball-элементами и scroll-анимацией. | Demo |
| [Сравнить редизайн личного сайта между моделями](#case-82) | Frontend и motion-дизайн | Одна задача редизайна личного сайта сравнивает Kimi K3 с другими моделями по визуальному качеству и структуре. | Evaluation |
| [Расширить пейзаж космической игры](#case-83) | Интерактивные игры и 3D | Kimi K3 превращает сцену космической игры в более широкое изображение с ландшафтом, кораблями и освещением. | Demo |
| [Разблокировать Three.js physics renderer](#case-84) | Интерактивные игры и 3D | Kimi K3 использован как помощник в реализации, чтобы продвинуть проблему физического рендера на Three.js. | Demo |
| [Сравнить генерацию цифрового двойника МКС](#case-85) | Оценка и ограничения | Kimi K3 сравнивается с другими моделями на задаче цифрового двойника МКС, показывая различия в сложной 3D-визуализации. | Benchmark |
| [Создать интерактивный исследователь кожи головы](#case-86) | Frontend и motion-дизайн | Kimi K3 генерирует образовательный визуализатор кожи головы и показывает применение для объясняющих интерфейсов. | Demo |
| [Поделиться prompt для 3D-глобус dashboard](#case-87) | Frontend и motion-дизайн | Публичный prompt показывает, как создать в Kimi K3 интерфейс dashboard с 3D-глобусом. | Tutorial |
| [Собрать браузерный Counter-Strike в одном файле](#case-88) | Интерактивные игры и 3D | Kimi K3 создает FPS-игру в стиле Counter-Strike как один HTML-файл. | Demo |
| [Оценить WebGPU-лес](#case-89) | Оценка и ограничения | Лесная WebGPU-сцена, созданная Kimi K3, оценивается по выразительности и ограничениям иммерсивного 3D. | Evaluation |
| [Сравнить промпты стеклянного дома](#case-90) | Оценка и ограничения | Используйте одну архитектурную сцену, чтобы сравнить Kimi K3 и Opus 4.8 по атмосфере, свету и пространственной завершенности. | Evaluation |
| [Собрать CS с генеративными ассетами](#case-91) | Код и интеграции | Совмещайте Kimi K3 для кода игры и GPT Image 2 для ассетов при прототипировании небольшого браузерного проекта в стиле Counter-Strike. | Integration |
| [Проверить voxel-футбольный гол](#case-92) | Оценка и ограничения | Запустите один и тот же prompt для футбольной анимации на чистом HTML/CSS/JS в двух моделях, чтобы сравнить движение и стоимость. | Benchmark |
| [Разобрать Minecraft benchmark](#case-93) | Оценка и ограничения | Посмотрите структурированный Minecraft-обзор, прежде чем считать хайп запуска или цену достаточным доказательством. | Benchmark |
| [Провести пять UI UX тестов](#case-94) | Frontend и motion-дизайн | Оценивайте Kimi K3 на нескольких задачах UI, logo и Figma MCP, а не по одному frontend-скриншоту. | Evaluation |
| [Использовать Design skill Command Code](#case-95) | Код и интеграции | Соединяйте Kimi K3 с выделенным design skill в Command Code, когда делаете визуальный игровой прототип под token budget. | Integration |
| [Построить игру про пирамиду](#case-96) | Интерактивные игры и 3D | Используйте Kimi K3 для однодневной 3D exploration game итерации, затем проверяйте quests, interiors и scope перед оценкой качества. | Demo |
| [Создавать landing из референсов](#case-97) | Frontend и motion-дизайн | Используйте reference boards, Figma AI и Motion Sites с Kimi K3, чтобы превращать visual direction в переиспользуемые landing sections. | Tutorial |
| [Измерить API tier limits](#case-98) | Оценка и ограничения | Планируйте Kimi K3 agent runs по tokens, tier, TPM и TPD, а не только по headline model pricing. | Limit |
| [Сравнить Limbo-style demo](#case-99) | Оценка и ограничения | Сравнивайте playable scope, polish, cost и bugs при тестировании Kimi K3 против Fable 5 на одном игровом prototype. | Benchmark |
| [Проверить затраты VulcanBench](#case-100) | Оценка и ограничения | Используйте этот кейс, чтобы оценить реальный workflow, стоимость или ограничения Kimi K3 в задаче «Проверить затраты VulcanBench».  | Benchmark |
| [Сравнить глубину Minecraft-сборки](#case-101) | Интерактивные игры и 3D | Используйте этот кейс, чтобы оценить реальный workflow, стоимость или ограничения Kimi K3 в задаче «Сравнить глубину Minecraft-сборки».  | Evaluation |
| [Создать FPS-клон Fallout](#case-102) | Интерактивные игры и 3D | Используйте этот кейс, чтобы оценить реальный workflow, стоимость или ограничения Kimi K3 в задаче «Создать FPS-клон Fallout».  | Demo |
| [Пройти премиальный веб-туториал](#case-103) | Frontend и motion-дизайн | Используйте этот кейс, чтобы оценить реальный workflow, стоимость или ограничения Kimi K3 в задаче «Пройти премиальный веб-туториал».  | Tutorial |
| [Оценить физику двойного маятника](#case-104) | Оценка и ограничения | Используйте этот кейс, чтобы оценить реальный workflow, стоимость или ограничения Kimi K3 в задаче «Оценить физику двойного маятника».  | Benchmark |
| [Выпустить RPG про дата-центр](#case-105) | Интерактивные игры и 3D | Используйте этот кейс, чтобы оценить реальный workflow, стоимость или ограничения Kimi K3 в задаче «Выпустить RPG про дата-центр».  | Demo |
| [Сравнить стоимость humanoid frontend](#case-106) | Frontend и motion-дизайн | Используйте этот кейс, чтобы оценить реальный workflow, стоимость или ограничения Kimi K3 в задаче «Сравнить стоимость humanoid frontend».  | Benchmark |
| [Проверить готовность ReactBench](#case-107) | Оценка и ограничения | Используйте этот кейс, чтобы оценить реальный workflow, стоимость или ограничения Kimi K3 в задаче «Проверить готовность ReactBench».  | Benchmark |
| [Создать 3D-игру с машиной](#case-108) | Интерактивные игры и 3D | Используйте этот кейс, чтобы оценить реальный workflow, стоимость или ограничения Kimi K3 в задаче «Создать 3D-игру с машиной».  | Demo |
| [Запустить Kimi K3 в Claude Code](#case-109) | Код и интеграции | Используйте этот кейс, чтобы оценить реальный workflow, стоимость или ограничения Kimi K3 в задаче «Запустить Kimi K3 в Claude Code».  | Integration |
| [Оценить Kimi K3 на AA-Briefcase](#case-110) | Оценка и ограничения | Используйте результаты AA-Briefcase, чтобы оценить Kimi K3 в agentic knowledge-work задачах до доверия лидербордам. | Benchmark |
| [Сравнить клоны Geometry Dash](#case-111) | Интерактивные игры и 3D | Сравните игровые build по одному brief, чтобы понять, подходит ли Kimi K3 для playable mobile-style прототипов. | Evaluation |
| [Проверить ретро-игру в Command Code](#case-112) | Интерактивные игры и 3D | Используйте multi-model design run в Command Code, чтобы сравнить gameplay Kimi K3 и стоимость моделей. | Evaluation |
| [Проверить оговорки frontend leaderboard](#case-113) | Оценка и ограничения | Используйте эту limitation note, чтобы отделить победы Kimi K3 в leaderboard от широких claim про coding и cost. | Limit |
| [Сравнить StackPerf architecture results](#case-114) | Оценка и ограничения | Используйте StackPerf для сравнения Kimi K3 и Qwen 3.8 по architecture quality, speed и tool-call behavior. | Benchmark |
| [Сравнить Three.js Kimi-vs-GLM](#case-115) | Frontend и motion-дизайн | Запустите одинаковые procedural Three.js prompts на Kimi K3 и GLM 5.2, чтобы сравнить frontend и 3D build behavior. | Benchmark |
| [Бенчмарк игры Space Discoverer](#case-116) | Интерактивные игры и 3D | Используйте mini-benchmark Space Discoverer, чтобы сравнить outputs моделей на generic 3D browser-game brief. | Benchmark |
| [Собрать driving game по реальной дороге](#case-117) | Интерактивные игры и 3D | Прототипируйте driving game, сочетая Kimi K3 с Blender и Godot вокруг карты реального локального участка дороги. | Demo |
| [Сравнить cost prompt Monument Valley](#case-118) | Оценка и ограничения | Используйте один Monument Valley-style prompt, чтобы сравнить visual quality, runtime и cost Kimi K3 и других моделей. | Benchmark |
| [Маршрутизировать Kimi через claude-code-router](#case-119) | Код и интеграции | Попробуйте Kimi K3 в существующем Claude Code workflow через claude-code-router, избегая ненужного proxy mode. | Integration |
| [Оценить Kimi K3 в индексе Surge](#case-120) | Оценка и ограничения | Используйте раздельные результаты SurgeAI, чтобы отделить силу Kimi K3 в обычном чате от слабых мест в агентных и научных задачах. | Benchmark |
| [Создать лендинг по референсу](#case-121) | Frontend и motion-дизайн | Давайте Kimi K3 сильные визуальные референсы и итеративные указания при тесте генерации лендингов. | Demo |
| [Создать вертикальный платформер](#case-122) | Интерактивные игры и 3D | Используйте короткий игровой brief, чтобы проверить, вернет ли Kimi K3 браузерный прототип одним HTML-файлом. | Demo |
| [Оценить ошибки PDE solver](#case-123) | Оценка и ограничения | Используйте ошибки PDE-бенчмарка, чтобы понять, где символические и численные задачи с Kimi K3 требуют проверки. | Benchmark |
| [Разобрать EHR кейсы ClinicalBench](#case-124) | Оценка и ограничения | Используйте EHR кейсы ClinicalBench, чтобы увидеть, где Kimi K3 справляется и где диагностическое рассуждение еще дает сбой. | Benchmark |
| [Запустить открытый agent harness](#case-125) | Код и интеграции | Используйте общий agent harness, чтобы сравнить Kimi K3 с другими frontier-моделями на задачах с инструментами. | Benchmark |
| [Оценить налоговые расчеты](#case-126) | Оценка и ограничения | Тестируйте Kimi K3 отдельно на налоговых задачах, не предполагая перенос силы во frontend. | Limit |
| [Проверить созданный Geometry Dash](#case-127) | Интерактивные игры и 3D | Совмещайте игру Kimi K3 с solver и браузерными playtests, прежде чем считать прототип готовым. | Benchmark |
| [Смоделировать 3D систему частиц](#case-128) | Frontend и motion-дизайн | Используйте prompts для симуляции частиц, чтобы сравнить качество движения Kimi K3 с закрытыми моделями. | Evaluation |
| [Запустить Kimi через Codex OAuth](#case-129) | Код и интеграции | Используйте маршрут Codex OAuth, когда coding workflow с Kimi K3 должен обойти ручную настройку API key. | Integration |

<a id="games-3d"></a>
## 🎮 Интерактивные игры и 3D

<a id="case-1"></a>
### Case 1: [Создать voxel pod racer одним prompt](https://x.com/ivanfioravanti/status/2077763009657627055) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Использовать короткую идею для прототипа гонки и определить следующую итерацию**

Автор сообщает, что Kimi K3 создал первую версию по одному публичному prompt, а дальше планируются новые гонщики, финиш и проверка деталей

**Prompt:**

```text
Voxel star wars pod-racers run
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01-poster.jpg" alt="Case 1 source video poster" height="360"></a>

[Play case 1 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-2"></a>
### Case 2: [Сравнить Frogger на одном prompt](https://x.com/ivanfioravanti/status/2077754781964054825) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Зафиксировать prompt и сравнить различия между моделями**

Автор показывает версию Kimi K3 как сравнение. Текст prompt и критерии оценки не опубликованы

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02-poster.jpg" alt="Case 2 source video poster" height="360"></a>

[Play case 2 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-3"></a>
### Case 3: [Создать Frogger и запись игры](https://x.com/TheAhmadOsman/status/2077776567292338285) (by [@TheAhmadOsman](https://x.com/TheAhmadOsman))

**Отдельно проверить одношаговую генерацию игры и записи**

Автор сообщает об одном проходе для игры и одном для записи. Точные prompts отсутствуют

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03-poster.jpg" alt="Case 3 source video poster" height="360"></a>

[Play case 3 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-4"></a>
### Case 4: [Создать прототип авианосца в Three.js](https://x.com/HarshithLucky3/status/2077753222018814360) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**Проверить интерактивное 3D на конкретной сцене запуска и посадки**

Автор показывает запуск и возвращение самолетов на авианосце класса Nimitz и положительно оценивает 3D-генерацию

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04-poster.jpg" alt="Case 4 source video poster" height="360"></a>

[Play case 4 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-9"></a>
### Case 9: [Создать игру в духе Paper Mario с агентскими инструментами](https://x.com/chongdashu/status/2077886028866531655) (by [@chongdashu](https://x.com/chongdashu))

**Объединить Kimi K3 с агентским harness и инструментами для ассетов, чтобы получить игровые элементы в 2D и 3D**

Автор сообщает об использовании Kimi K3 с Grok Build, Spriterrific для 2D-ассетов и геометрией для 3D-ассетов в игре в духе Paper Mario. Источник демонстрирует инструменты и skills, но не публикует точный повторно используемый prompt

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-09.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-09-poster.jpg" alt="Case 9 source video poster" height="360"></a>

[Play case 9 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-09.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-11"></a>
### Case 11: [Создать шутер от первого лица в метро](https://x.com/bijanbowen/status/2077881805751873997) (by [@bijanbowen](https://x.com/bijanbowen))

**Использовать конкретную обстановку метро для проверки сгенерированного шутера от первого лица**

Автор показывает FPS в метро, приписанный Kimi K3, и прямо отмечает неопределенность в том, повлиял ли на результат статус инфлюенсера. Prompt и воспроизводимый workflow отсутствуют

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-11.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-11-poster.jpg" alt="Case 11 source video poster" height="360"></a>

[Play case 11 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-11.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-19"></a>
### Case 19: [Смоделировать двигатель V8 через Blender MCP](https://x.com/aisearchio/status/2077962156147146925) (by [@aisearchio](https://x.com/aisearchio))

**Использовать Blender MCP и один запрос для генерации детальной механической 3D-модели**

Обозреватель сообщает, что Kimi K3 по одному prompt создал полный двигатель V8 с Blender MCP. Публикация ссылается на более полный обзор, но в предоставленной записи точный prompt не раскрыт

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-19.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-19-poster.jpg" alt="Case 19 source video poster" height="360"></a>

[Play case 19 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-19.mp4)

Type: Integration | Date: 2026-07-17

---

<a id="case-23"></a>
### Case 23: [Создать игровую боевую арену по одному reference](https://x.com/VORTEX_Promos/status/2077879705378730074) (by [@VORTEX_Promos](https://x.com/VORTEX_Promos))

**Использовать один reference для проверки одношаговой генерации полной игровой арены**

Автор сообщает, что Kimi K3 за один проход создал игровую боевую арену по одному reference. Публикация также содержит отдельное утверждение о leaderboard, но конкретный use case — показанный артефакт арены

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23-poster.jpg" alt="Case 23 source video poster" height="360"></a>

[Play case 23 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23-01.jpg" alt="Case 23 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-24"></a>
### Case 24: [Создать три самостоятельно играющие ретроигры в HTML-файлах](https://x.com/rohanpaul_ai/status/2077889084761206860) (by [@rohanpaul_ai](https://x.com/rohanpaul_ai))

**Требовать графику, врагов, правила и автономную игру внутри самостоятельных HTML-файлов**

Источник сообщает о сравнении Atomic Chat, где модели создали Road Fighter, Battle City и Q*bert как самостоятельно играющие HTML-файлы. Сравнение цены и качества дано издателем и независимо здесь не воспроизводилось

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-24.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-24-poster.jpg" alt="Case 24 source video poster" height="360"></a>

[Play case 24 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-24.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-27"></a>
### Case 27: [Создать одношаговую игру в прятки с хамелеоном](https://x.com/aimlapi/status/2077898742179459274) (by [@aimlapi](https://x.com/aimlapi))

**Создать однофайловую игру с подбором цвета, процедурными зонами, звуком и подсчетом очков по раундам**

AIMLAPI сообщает об одношаговом сравнении игры в прятки с одним prompt и указывает стоимость $3.11 для Kimi K3 и $12.23 для Fable 5. Возможности и стоимость заявлены провайдером

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-27.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-27-poster.jpg" alt="Case 27 source video poster" height="360"></a>

[Play case 27 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-27.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-36"></a>
### Case 36: [Создать игру в духе Paper Mario в 2.5D с агентским toolchain](https://x.com/chongdashu/status/2077981621223837739) (by [@chongdashu](https://x.com/chongdashu))

**Использовать Kimi K3 с Grok Build или Claude Code и Spriterrific для сборки 2.5D game workflow**

Автор дает полный walkthrough с Grok Build и Kimi K3 и показывает генерацию sprites через Spriterrific. Источник называет инструменты, но не предоставляет точные повторно используемые prompts

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-36.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-36-poster.jpg" alt="Case 36 source video poster" height="360"></a>

[Play case 36 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-36.mp4)

Type: Tutorial | Date: 2026-07-17

---

<a id="case-43"></a>
### Case 43: [Создать браузерную 3D wuxia RPG](https://x.com/AngryTomtweets/status/2077868163136450619) (by [@AngryTomtweets](https://x.com/AngryTomtweets))

**Объединить ближний бой, quests, inventory, погоду, interiors, работу со средой Blender и адаптированные assets**

Источник сообщает о браузерной RPG Kimi K3 с ближним боем, quests, inventory, динамической погодой и исследуемыми interiors, а также Blender-моделированием, улучшением collision, PBR retexturing и адаптированными открытыми assets

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-43.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-43-poster.jpg" alt="Case 43 source video poster" height="360"></a>

[Play case 43 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-43.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-44"></a>
### Case 44: [Создать браузерную multiplayer-игру в духе Minecraft](https://x.com/Alezander907/status/2077926014710407407) (by [@Alezander907](https://x.com/Alezander907))

**В ограниченном по времени и стоимости запуске создать игровую онлайн multiplayer-игру для браузера**

Автор сообщает, что Kimi K3 за один час и $6.57 создал доступную в браузере multiplayer-игру в духе Minecraft. Это самостоятельно заявленные параметры одного запуска

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-44.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-44-poster.jpg" alt="Case 44 source video poster" height="360"></a>

[Play case 44 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-44.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-48"></a>
### Case 48: [Воссоздать браузерную кооперативную игру с разделенным экраном](https://x.com/ridark_eth/status/2077882889803378969) (by [@ridark_eth](https://x.com/ridark_eth))

**Одним запросом создать браузерную кооперацию с разделенным экраном и взаимодействием с окружением в реальном времени**

Автор сообщает, что Kimi K3 по одному prompt создал браузерную игру в духе It Takes Two, где Mario и Luigi взаимодействуют в split-screen и с окружением в реальном времени

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-48.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-48-poster.jpg" alt="Case 48 source video poster" height="360"></a>

[Play case 48 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-48.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-49"></a>
### Case 49: [Создать играбельную игру через Design Mode в Command Code](https://x.com/naymur_dev/status/2077873562661335207) (by [@naymur_dev](https://x.com/naymur_dev))

**Использовать design command Command Code для одношаговой сборки игры и записывать, является ли результат играбельным**

Автор сообщает об одношаговом сравнении в design mode Command Code и говорит, что запуск Kimi K3 создал играбельную игру за $0.038. Эти стоимость и качество заявлены самим автором

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-49.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-49-poster.jpg" alt="Case 49 source video poster" height="360"></a>

[Play case 49 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-49.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-51"></a>
### Case 51: [Собрать целостную браузерную wuxia RPG](https://x.com/TokenGremlin/status/2077855657068310620) (by [@TokenGremlin](https://x.com/TokenGremlin))

**Интегрировать перемещение, бой, quests, inventory, погоду, исследование и работу над 3D-средой в одной игре**

Источник сообщает о wuxia-style браузерной RPG Kimi K3, объединяющей ближний бой, quests, inventory, динамическую погоду, исследуемые interiors и целостную структуру 3D gameplay

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-51.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-51-poster.jpg" alt="Case 51 source video poster" height="360"></a>

[Play case 51 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-51.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-54"></a>
### Case 54: [Создать игровую crossover-игру Hollow Knight](https://x.com/wangfeng0315/status/2077933531200991583) (by [@wangfeng0315](https://x.com/wangfeng0315))

**Использовать существующие game assets для создания игровой битвы Knight против Kimi**

Автор, заявляющий о работе в Kimi, сообщает о создании игры из assets Hollow Knight, где Knight сражается с Kimi, и дает публичную ссылку. При атрибуции и оценке следует учитывать эту связь

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54-poster.jpg" alt="Case 54 source video poster" height="360"></a>

[Play case 54 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54-01.jpg" alt="Case 54 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-17

---

<a id="case-60"></a>
### Case 60: [Создать 3D-браузерную игру в духе Fall Guys за один проход](https://x.com/aayushman2703/status/2077857886441783526) (by [@aayushman2703](https://x.com/aayushman2703))

**Одним запросом создать игровую 3D-игру с препятствиями и открыть проект для проверки**

Автор сообщает об одношаговой сборке Kimi K3 браузерной игры в духе Fall Guys и говорит, что prompt и GitHub-проект доступны по ссылке источника. Эта запись prompt не воспроизводит

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-60.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-60-poster.jpg" alt="Case 60 source video poster" height="360"></a>

[Play case 60 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-60.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-61"></a>
### Case 61: [Создать и самостоятельно протестировать апокалиптический FPS в Лиссабоне](https://x.com/goncalo_canhoto/status/2077863166655037668) (by [@goncalo_canhoto](https://x.com/goncalo_canhoto))

**Использовать запуск максимального усилия по одному prompt, который тестирует, делает скриншоты и итерирует до выдачи играбельного FPS**

Автор сообщает, что Kimi K3 примерно за один час создал играбельный браузерный FPS Apocalyptic Lisbon, многократно тестируя, делая скриншоты и итерируя. Время и процесс заявлены самим автором

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-61-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-61-01.jpg" alt="Case 61 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-63"></a>
### Case 63: [Создать игру в стиле Animal Crossing по простому запросу](https://x.com/gagarot200/status/2077949230287896830) (by [@gagarot200](https://x.com/gagarot200))

**Использовать минимальный game brief для проверки играбельности, gameplay loop и parallax-эффектов**

Автор сообщает, что Kimi K3 по очень простому prompt создал полностью игровую игру в стиле Animal Crossing с gameplay loop и parallax-эффектами. Точная формулировка в записи отсутствует

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-63.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-63-poster.jpg" alt="Case 63 source video poster" height="360"></a>

[Play case 63 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-63.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-65"></a>
### Case 65: [Создать игру в духе Mario по brief из одного предложения](https://x.com/izutorishima/status/2077939370154475992) (by [@izutorishima](https://x.com/izutorishima))

**Минимальным одношаговым запросом проверить играбельность, дизайн уровня, pixel art и parallax**

Автор сообщает, что Kimi K3 по одному brief создал работающую игру в духе Mario без очевидных ошибок, со структурой уровня и parallax. В том же отчете критикуется качество музыки и графики

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-01.jpg" alt="Case 65 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-02.jpg" alt="Case 65 source image 2" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-03.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-03.jpg" alt="Case 65 source image 3" height="360"></a>

Type: Demo | Date: 2026-07-17

---

<a id="case-67"></a>
### Case 67: [Создать работающий zombie-шутер от первого лица](https://x.com/X2worldtech/status/2077902793449296203) (by [@X2worldtech](https://x.com/X2worldtech))

**Использовать конкретную цель zombie-shooter для проверки полного игрового FPS-артефакта**

Источник показывает полностью работающий zombie FPS, приписанный Kimi K3. Prompt, детали реализации и внешняя оценка gameplay отсутствуют

> [!WARNING]
> The original source permalink returned HTTP 404 during the 2026-07-17 audit. Attribution and evidence are preserved from the supplied high-confidence source package.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-67.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-67-poster.jpg" alt="Case 67 source video poster" height="360"></a>

[Play case 67 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-67.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-71"></a>
### Case 71: [Создать инди-игру про космический корабль](https://x.com/ChrisGPT/status/2078261217924087999) (by [@ChrisGPT](https://x.com/ChrisGPT))

**Сделать первую версию на Kimi K3 Standard и сравнить связность, ошибки, визуальное качество и стоимость токенов**

ChrisGPT сообщает о первой версии игры примерно за 2,50 доллара API-токенов. Она была связнее и содержала меньше ошибок, чем версия GPT-5.5, но Fable 5 оставался визуально лучше

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-71.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-71-poster.jpg" alt="Case 71 source video poster" height="360"></a>

[Play case 71 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-71.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-73"></a>
### Case 73: [Самотестирование игры в Summer Engine](https://x.com/MathiasHeide/status/2078231589436465199) (by [@MathiasHeide](https://x.com/MathiasHeide))

**Дать Kimi K3 запустить игру, проверить скриншоты и логи и исправить видимые дефекты в той же сессии**

Mathias Heide сообщает, что Kimi K3 за одну 27-минутную сессию создал игру с бумажным самолетом, проверил скриншоты и логи, исправил ошибки и сменил черный самолет на белый

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-73.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-73-poster.jpg" alt="Case 73 source video poster" height="360"></a>

[Play case 73 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-73.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-77"></a>
### Case 77: [Итеративно создать браузерную battle royale](https://x.com/Ananth7e/status/2078158089929601203) (by [@Ananth7e](https://x.com/Ananth7e))

**Планировать долгие автономные итерации и точечные дополнительные prompt для функциональной браузерной игры**

Ananth сообщает о более чем 130 минутах и 40 циклах скриншотов Chrome для игры в стиле PUBG, после чего еще два prompt исправили оставшиеся ошибки

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-77.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-77-poster.jpg" alt="Case 77 source video poster" height="360"></a>

[Play case 77 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-77.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-83"></a>
### Case 83: [Расширить пейзаж космической игры](https://x.com/startracker/status/2078543423167160342) (by [@startracker](https://x.com/startracker))

**Kimi K3 превращает сцену космической игры в более широкое изображение с ландшафтом, кораблями и освещением.**

Публичное изображение показывает игровую sci-fi сцену и демонстрирует работу Kimi K3 с глубиной, объектами и цветом.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-83.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-83-poster.jpg" alt="Case 83 source video poster" height="360"></a>

[Play case 83 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-83.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-84"></a>
### Case 84: [Разблокировать Three.js physics renderer](https://x.com/mattwatkajtys/status/2078523373861339475) (by [@mattwatkajtys](https://x.com/mattwatkajtys))

**Kimi K3 использован как помощник в реализации, чтобы продвинуть проблему физического рендера на Three.js.**

Автор сообщает, что решил блокирующую 3D-проблему с Kimi K3, и показывает физическую сцену в браузере на видео.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-84.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-84-poster.jpg" alt="Case 84 source video poster" height="360"></a>

[Play case 84 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-84.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-88"></a>
### Case 88: [Собрать браузерный Counter-Strike в одном файле](https://x.com/prasenx/status/2078453069021659477) (by [@prasenx](https://x.com/prasenx))

**Kimi K3 создает FPS-игру в стиле Counter-Strike как один HTML-файл.**

Автор показывает игру, запускаемую из одного файла, с игровым циклом, вводом, рендером и простой UI.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-88.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-88-poster.jpg" alt="Case 88 source video poster" height="360"></a>

[Play case 88 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-88.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-96"></a>
### Case 96: [Построить игру про пирамиду](https://x.com/ice_bearcute/status/2078828887468056763) (by [@ice_bearcute](https://x.com/ice_bearcute))

**Используйте Kimi K3 для однодневной 3D exploration game итерации, затем проверяйте quests, interiors и scope перед оценкой качества.**

ice_bearcute сообщает, что за день построил 3D игру Pyramid Expedition с Kimi K3. Источник говорит, что это не просто внешняя сцена: игрок может исследовать древнюю гробницу и выполнять задания, а приложенное media дает видимое доказательство gameplay.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-96.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-96-poster.jpg" alt="Case 96 source video poster" height="360"></a>

[Play case 96 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-96.mp4)

Type: Demo | Date: 2026-07-19

---

<a id="case-101"></a>
### Case 101: [Сравнить глубину Minecraft-сборки](https://x.com/vikktorrrre/status/2079294696459804762) (by [@vikktorrrre](https://x.com/vikktorrrre))

**Используйте этот кейс, чтобы оценить реальный workflow, стоимость или ограничения Kimi K3 в задаче «Сравнить глубину Minecraft-сборки». **

Исходный пост дает публичные доказательства по теме «Сравнить глубину Minecraft-сборки»: описание автора, медиа результата или данные benchmark/tutorial. Репозиторий сохраняет только проверяемые факты и не восстанавливает закрытые prompts или шаги.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-101.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-101-poster.jpg" alt="Case 101 source video poster" height="360"></a>

[Play case 101 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-101.mp4)

Type: Evaluation | Date: 2026-07-20

---

<a id="case-102"></a>
### Case 102: [Создать FPS-клон Fallout](https://x.com/kirillk_web3/status/2079290747585437781) (by [@kirillk_web3](https://x.com/kirillk_web3))

**Используйте этот кейс, чтобы оценить реальный workflow, стоимость или ограничения Kimi K3 в задаче «Создать FPS-клон Fallout». **

Исходный пост дает публичные доказательства по теме «Создать FPS-клон Fallout»: описание автора, медиа результата или данные benchmark/tutorial. Репозиторий сохраняет только проверяемые факты и не восстанавливает закрытые prompts или шаги.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-102.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-102-poster.jpg" alt="Case 102 source video poster" height="360"></a>

[Play case 102 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-102.mp4)

Type: Demo | Date: 2026-07-20

---

<a id="case-105"></a>
### Case 105: [Выпустить RPG про дата-центр](https://x.com/demian_ai/status/2079239035596218578) (by [@demian_ai](https://x.com/demian_ai))

**Используйте этот кейс, чтобы оценить реальный workflow, стоимость или ограничения Kimi K3 в задаче «Выпустить RPG про дата-центр». **

Исходный пост дает публичные доказательства по теме «Выпустить RPG про дата-центр»: описание автора, медиа результата или данные benchmark/tutorial. Репозиторий сохраняет только проверяемые факты и не восстанавливает закрытые prompts или шаги.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-105.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-105-poster.jpg" alt="Case 105 source video poster" height="360"></a>

[Play case 105 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-105.mp4)

Type: Demo | Date: 2026-07-20

---

<a id="case-108"></a>
### Case 108: [Создать 3D-игру с машиной](https://x.com/LexnLin/status/2079233761242235081) (by [@LexnLin](https://x.com/LexnLin))

**Используйте этот кейс, чтобы оценить реальный workflow, стоимость или ограничения Kimi K3 в задаче «Создать 3D-игру с машиной». **

Исходный пост дает публичные доказательства по теме «Создать 3D-игру с машиной»: описание автора, медиа результата или данные benchmark/tutorial. Репозиторий сохраняет только проверяемые факты и не восстанавливает закрытые prompts или шаги.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-poster.jpg" alt="Case 108 source video poster" height="360"></a>

[Play case 108 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-01.jpg" alt="Case 108 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-02.jpg" alt="Case 108 source image 2" height="360"></a>

Type: Demo | Date: 2026-07-20

---

<a id="case-111"></a>
### Case 111: [Сравнить клоны Geometry Dash](https://x.com/Nekt_0/status/2079629004483465473) (by [@Nekt_0](https://x.com/Nekt_0))

**Сравните игровые build по одному brief, чтобы понять, подходит ли Kimi K3 для playable mobile-style прототипов.**

Nekt пишет, что Kimi K3 потратил около 30 минут и 200 000 tokens на клон Geometry Dash с прыжками, препятствиями, уровнями, музыкой и визуальными эффектами, а в видео сравнивает его с build Claude Fable 5.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-111.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-111-poster.jpg" alt="Case 111 source video poster" height="360"></a>

[Play case 111 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-111.mp4)

Type: Evaluation | Date: 2026-07-21

---

<a id="case-112"></a>
### Case 112: [Проверить ретро-игру в Command Code](https://x.com/naymur_dev/status/2079627963000398334) (by [@naymur_dev](https://x.com/naymur_dev))

**Используйте multi-model design run в Command Code, чтобы сравнить gameplay Kimi K3 и стоимость моделей.**

Naymur сообщает, что запускал один /design prompt в Command Code через Fable 5, GPT-5.6 Sol, Grok 4.5 и Kimi K3. По посту, Kimi K3 сделал ASCII retro game с gameplay, уровнями, пулями и boss fights за $0.15.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-112.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-112-poster.jpg" alt="Case 112 source video poster" height="360"></a>

[Play case 112 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-112.mp4)

Type: Evaluation | Date: 2026-07-21

---

<a id="case-116"></a>
### Case 116: [Бенчмарк игры Space Discoverer](https://x.com/fabriciocarraro/status/2079548607393382528) (by [@fabriciocarraro](https://x.com/fabriciocarraro))

**Используйте mini-benchmark Space Discoverer, чтобы сравнить outputs моделей на generic 3D browser-game brief.**

Fabricio Carraro сообщает о mini-benchmark Claude Fable 5, GPT-5.6 Sol и Kimi K3 на максимальных reasoning settings. Задача была 3D browser game Space Discoverer, и все три модели сошлись на Three.js поверх WebGL 2.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-116.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-116-poster.jpg" alt="Case 116 source video poster" height="360"></a>

[Play case 116 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-116.mp4)

Type: Benchmark | Date: 2026-07-21

---

<a id="case-117"></a>
### Case 117: [Собрать driving game по реальной дороге](https://x.com/bijanbowen/status/2079526003643179102) (by [@bijanbowen](https://x.com/bijanbowen))

**Прототипируйте driving game, сочетая Kimi K3 с Blender и Godot вокруг карты реального локального участка дороги.**

Bijan Bowen показывает, как Kimi K3 делает driving game с Blender и Godot, используя реальный участок дороги рядом с автором как основу карты. Приложенное видео является публичным evidence состояния build.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-117.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-117-poster.jpg" alt="Case 117 source video poster" height="360"></a>

[Play case 117 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-117.mp4)

Type: Demo | Date: 2026-07-21

---

<a id="case-122"></a>
### Case 122: [Создать вертикальный платформер](https://x.com/diegocabezas01/status/2079946676270219488) (by [@diegocabezas01](https://x.com/diegocabezas01))

**Используйте короткий игровой brief, чтобы проверить, вернет ли Kimi K3 браузерный прототип одним HTML-файлом.**

Diego Cabezas показывает запуск Kimi K3 Max для вертикального платформера, где игрок постоянно прыгает выше по движущимся платформам. Пост фиксирует one-shot результат в одном HTML.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-122.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-122-poster.jpg" alt="Case 122 source video poster" height="360"></a>

[Play case 122 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-122.mp4)

Type: Demo | Date: 2026-07-22

---

<a id="case-127"></a>
### Case 127: [Проверить созданный Geometry Dash](https://x.com/Kirratr/status/2079902410042909108) (by [@Kirratr](https://x.com/Kirratr))

**Совмещайте игру Kimi K3 с solver и браузерными playtests, прежде чем считать прототип готовым.**

Kirratr сообщает, что Kimi K3 потратил 36:53 на тот же Geometry Dash brief. Beam-search solver нашел победный путь из 64 прыжков, воспроизвел его в браузере и не увидел ошибок консоли.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-127.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-127-poster.jpg" alt="Case 127 source video poster" height="360"></a>

[Play case 127 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-127.mp4)

Type: Benchmark | Date: 2026-07-22

---


<a id="frontend-motion"></a>
## 🎨 Frontend и motion-дизайн

<a id="case-5"></a>
### Case 5: [Создать интерактивный motion-frontend](https://x.com/chetaslua/status/2077749371144442022) (by [@chetaslua](https://x.com/chetaslua))

**Сделать графику, которая остается интерактивной на паузе**

Автор указывает 42 минуты, один проход, простой код и отсутствие harness, MCP и skills

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05-poster.jpg" alt="Case 5 source video poster" height="360"></a>

[Play case 5 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-6"></a>
### Case 6: [Создать синхронизированную motion-рекламу](https://x.com/abhinavflac/status/2077760297918484667) (by [@abhinavflac](https://x.com/abhinavflac))

**Проверить синхронизацию музыки, эффектов и движения**

Автор сообщает о рекламе в стиле Spotify, созданной одним prompt. Точный prompt не опубликован

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06-poster.jpg" alt="Case 6 source video poster" height="360"></a>

[Play case 6 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-14"></a>
### Case 14: [Создать motion-дизайн полностью кодом](https://x.com/chetaslua/status/2077952938564354503) (by [@chetaslua](https://x.com/chetaslua))

**Проверить, способен ли одношаговый coding workflow создать motion-дизайн без вспомогательных инструментов генерации**

Автор сообщает об одношаговом результате Kimi K3, полностью созданном кодом без MCP, skills, инструментов, генерации видео и специальных prompts. Точный prompt не приведен

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-14.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-14-poster.jpg" alt="Case 14 source video poster" height="360"></a>

[Play case 14 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-14.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-15"></a>
### Case 15: [Исследовать человека и создать анимированный персональный сайт](https://x.com/nicky_sap/status/2077857190707429411) (by [@nicky_sap](https://x.com/nicky_sap))

**Дать широкое задание на персональный сайт, затем проверить исследование, планирование, итерации и browser validation модели**

Автор сообщает, что Kimi K3 исследовал Nick Saponaro и по широкому запросу создал анимированный персональный сайт, включая планирование, тестирование, итерации и проверки в браузере. Это самостоятельно заявленная демонстрация workflow

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-15.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-15-poster.jpg" alt="Case 15 source video poster" height="360"></a>

[Play case 15 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-15.mp4)

Type: Tutorial | Date: 2026-07-16

---

<a id="case-17"></a>
### Case 17: [Создать симуляцию черной дыры](https://x.com/chetaslua/status/2077961850352971796) (by [@chetaslua](https://x.com/chetaslua))

**Использовать задачу научной визуализации для проверки сгенерированной симуляции черной дыры**

Автор показывает симуляцию черной дыры, приписанную Kimi K3, и называет ее лучшей из увиденных. Источник дает видимый результат, но не prompt, rubric или независимую проверку

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-17.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-17-poster.jpg" alt="Case 17 source video poster" height="360"></a>

[Play case 17 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-17.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-22"></a>
### Case 22: [Проверить сложное frontend-моделирование, частицы и shaders](https://x.com/karminski3/status/2077889959223337099) (by [@karminski3](https://x.com/karminski3))

**Использовать публичный frontend prompt, чтобы за один проход проверить точность моделирования, эффекты частиц и генерацию inline shaders**

Автор сообщает об однопроходном frontend-результате Kimi K3 с точным моделированием, эффектами частиц и сложным кодом inline shader и указывает, что тестовый prompt опубликован по ссылке источника

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-22.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-22-poster.jpg" alt="Case 22 source video poster" height="360"></a>

[Play case 22 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-22.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-26"></a>
### Case 26: [Создать инструмент процедурной музыки с одной попытки](https://x.com/mirochill/status/2077723551331758478) (by [@mirochill](https://x.com/mirochill))

**Проверить одношаговую генерацию интерактивного генератора процедурной музыки и осторожно сравнить видимый результат**

Автор сообщает, что Kimi K3 с одной попытки создал инструмент процедурной музыки, и положительно сравнивает его с результатами Fable 5 и GPT-5.6 Sol. Это собственный набор тестов автора, а не стандартизированный benchmark

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-26-poster.jpg" alt="Case 26 source video poster" height="360"></a>

[Play case 26 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-26.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-33"></a>
### Case 33: [Создать product page в Three.js по двум изображениям](https://x.com/1littlecoder/status/2077890296806031665) (by [@1littlecoder](https://x.com/1littlecoder))

**Использовать два reference-изображения и явное требование Three.js для создания презентации продукта**

Автор сообщает, что Kimi K3 разработал product page по двум изображениям и создал явно запрошенную версию на Three.js. Дополнительные детали prompt или реализации не приведены

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-33.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-33-poster.jpg" alt="Case 33 source video poster" height="360"></a>

[Play case 33 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-33.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-39"></a>
### Case 39: [Изобрести роскошный резак для хлеба и его product page](https://x.com/filicroval/status/2077871090731221438) (by [@filicroval](https://x.com/filicroval))

**Объединить идею продукта, exploded view, демонстрацию и landing page в одном дизайн-артефакте**

Автор сообщает, что Kimi K3 изобрел гильотинный резак для хлеба, представил его как люксовый продукт и создал landing page с exploded view и демонстрацией

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-39.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-39-poster.jpg" alt="Case 39 source video poster" height="360"></a>

[Play case 39 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-39.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-45"></a>
### Case 45: [Создать десятисекундный рекурсивный GIF с пеликаном](https://x.com/1littlecoder/status/2077880380900937865) (by [@1littlecoder](https://x.com/1littlecoder))

**Использовать полностью заданное описание зацикленной анимации для проверки непрерывности сюжета и рекурсии GIF**

Источник содержит prompt на зацикленный десятисекундный GIF: пеликан едет на велосипеде и при приближении камеры получает текстовым сообщением то же видео. Автор показывает полученную анимацию Kimi K3

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-45.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-45-poster.jpg" alt="Case 45 source video poster" height="360"></a>

[Play case 45 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-45.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-55"></a>
### Case 55: [Создать SVG BMW M4 CS в боковом ракурсе](https://x.com/HarshithLucky3/status/2077765821380886942) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**Использовать конкретный автомобиль и ракурс для проверки векторной иллюстрации**

Автор показывает SVG BMW M4 CS сбоку, приписанный Kimi K3 Max. В источнике есть артефакт, но нет prompt или производственных шагов

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-55-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-55-01.jpg" alt="Case 55 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-58"></a>
### Case 58: [Воссоздать Gargantua через обратную связь по скриншотам](https://x.com/AngryTomtweets/status/2077868981659324444) (by [@AngryTomtweets](https://x.com/AngryTomtweets))

**Использовать последовательные скриншоты как наблюдения для диагностики и улучшения научной визуализации**

Источник сообщает, что Kimi K3 воссоздал Gargantua из Interstellar через 62 собственных скриншота, читая каждый результат, диагностируя проблемы и итеративно действуя

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-58.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-58-poster.jpg" alt="Case 58 source video poster" height="360"></a>

[Play case 58 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-58.mp4)

Type: Tutorial | Date: 2026-07-16

---

<a id="case-66"></a>
### Case 66: [Улучшить визуализацию черной дыры с помощью 62 скриншотов](https://x.com/TokenGremlin/status/2077855959201042645) (by [@TokenGremlin](https://x.com/TokenGremlin))

**Использовать цикл обратной связи по скриншотам для чтения, диагностики и исправления визуальной симуляции на множестве итераций**

Источник сообщает, что Kimi K3 реконструировал Gargantua из Interstellar, наблюдая и улучшая результат на протяжении 62 скриншотов. Это демонстрирует заявленный цикл обратной связи, а не независимую физическую точность

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-66.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-66-poster.jpg" alt="Case 66 source video poster" height="360"></a>

[Play case 66 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-66.mp4)

Type: Tutorial | Date: 2026-07-16

---

<a id="case-68"></a>
### Case 68: [Создать маркетинговый PDF о post-training](https://x.com/Satvik_Pen/status/2077859673517023313) (by [@Satvik_Pen](https://x.com/Satvik_Pen))

**Использовать названный продукт и формат результата для генерации маркетингового документа**

Автор сообщает, что запросил у Kimi K3 маркетинговый PDF о post-training Inkling компании Thinking Machines, показывает результат и хвалит внутренний процесс. Prompt и критерии оценки не приведены

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-01.png" alt="Case 68 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-02.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-02.png" alt="Case 68 source image 2" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-03.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-03.png" alt="Case 68 source image 3" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-04.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-04.png" alt="Case 68 source image 4" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-70"></a>
### Case 70: [Создать пользовательский интерфейс по одному prompt](https://x.com/BrianMRey/status/2077891942088671689) (by [@BrianMRey](https://x.com/BrianMRey))

**Использовать один запрос для генерации и проверки полного UI-дизайна**

Автор показывает UI-дизайн, приписанный одношаговому запуску Kimi K3, и дает резко положительную субъективную оценку. Точный prompt и rubric отсутствуют

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-70.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-70-poster.jpg" alt="Case 70 source video poster" height="360"></a>

[Play case 70 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-70.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-78"></a>
### Case 78: [Создать сайт в наградном стиле](https://x.com/viktoroddy/status/2078140696910037002) (by [@viktoroddy](https://x.com/viktoroddy))

**Оценивать полную записанную сессию, а не только финальный скриншот**

Viktor Oddy публикует 13-минутный tutorial по созданию сайта наградного уровня с Kimi K3 и показывает весь процесс

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-78.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-78-poster.jpg" alt="Case 78 source video poster" height="360"></a>

[Play case 78 tutorial video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-78.mp4)

Type: Tutorial | Date: 2026-07-17

---

<a id="case-81"></a>
### Case 81: [Собрать frontend с metaball-анимацией при прокрутке](https://x.com/abhinavflac/status/2078603131055993130) (by [@abhinavflac](https://x.com/abhinavflac))

**Kimi K3 создает аккуратный веб-интерфейс со светящимися metaball-элементами и scroll-анимацией.**

Видео показывает готовый динамический frontend, где визуальные эффекты, компоновка и движение собраны из одного задания.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-81.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-81-poster.jpg" alt="Case 81 source video poster" height="360"></a>

[Play case 81 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-81.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-82"></a>
### Case 82: [Сравнить редизайн личного сайта между моделями](https://x.com/fabriciocarraro/status/2078574831466078265) (by [@fabriciocarraro](https://x.com/fabriciocarraro))

**Одна задача редизайна личного сайта сравнивает Kimi K3 с другими моделями по визуальному качеству и структуре.**

Пост показывает несколько результатов рядом и помогает оценить дизайн-решения, структуру секций и уровень отделки Kimi K3.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-82.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-82-poster.jpg" alt="Case 82 source video poster" height="360"></a>

[Play case 82 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-82.mp4)

Type: Evaluation | Date: 2026-07-18

---

<a id="case-86"></a>
### Case 86: [Создать интерактивный исследователь кожи головы](https://x.com/MiaAI_lab/status/2078508824752017757) (by [@MiaAI_lab](https://x.com/MiaAI_lab))

**Kimi K3 генерирует образовательный визуализатор кожи головы и показывает применение для объясняющих интерфейсов.**

Демо показывает интерактивный экран для изучения структур кожи головы, с понятным медицинским и учебным контекстом.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-86.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-86-poster.jpg" alt="Case 86 source video poster" height="360"></a>

[Play case 86 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-86.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-87"></a>
### Case 87: [Поделиться prompt для 3D-глобус dashboard](https://x.com/hqmank/status/2078465403349840144) (by [@hqmank](https://x.com/hqmank))

**Публичный prompt показывает, как создать в Kimi K3 интерфейс dashboard с 3D-глобусом.**

Пост содержит prompt и итоговое видео, где глобус, данные и dashboard-композиция собраны вместе.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-87.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-87-poster.jpg" alt="Case 87 source video poster" height="360"></a>

[Play case 87 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-87.mp4)

Type: Tutorial | Date: 2026-07-18

---

<a id="case-94"></a>
### Case 94: [Провести пять UI UX тестов](https://x.com/MAXdeg0/status/2078855257686196399) (by [@MAXdeg0](https://x.com/MAXdeg0))

**Оценивайте Kimi K3 на нескольких задачах UI, logo и Figma MCP, а не по одному frontend-скриншоту.**

MAXdeg0 сообщает о пяти UI/UX и logo design тестах Kimi K3 с Claude Code и сервером Figma MCP. Источник перечисляет задачи вроде landing page rebuild, hero section rebuild и logo/design work, а также дает конкретные время и стоимость как минимум для landing.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-94.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-94-poster.jpg" alt="Case 94 source video poster" height="360"></a>

[Play case 94 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-94.mp4)

Type: Evaluation | Date: 2026-07-19

---

<a id="case-97"></a>
### Case 97: [Создавать landing из референсов](https://x.com/MAXdeg0/status/2078776969072877715) (by [@MAXdeg0](https://x.com/MAXdeg0))

**Используйте reference boards, Figma AI и Motion Sites с Kimi K3, чтобы превращать visual direction в переиспользуемые landing sections.**

MAXdeg0 описывает landing-page workflow: брать style references из Pinterest, remix через Figma AI или вставлять UI reference плюс prompt в Motion Sites, чтобы Kimi K3 построил страницу. Пост также говорит, что метод можно повторять для новых sections, и ссылается на полный prompting guide.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-97.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-97-poster.jpg" alt="Case 97 source video poster" height="360"></a>

[Play case 97 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-97.mp4)

Type: Tutorial | Date: 2026-07-19

---

<a id="case-103"></a>
### Case 103: [Пройти премиальный веб-туториал](https://x.com/_guillecasaus/status/2079258261014908980) (by [@_guillecasaus](https://x.com/_guillecasaus))

**Используйте этот кейс, чтобы оценить реальный workflow, стоимость или ограничения Kimi K3 в задаче «Пройти премиальный веб-туториал». **

Исходный пост дает публичные доказательства по теме «Пройти премиальный веб-туториал»: описание автора, медиа результата или данные benchmark/tutorial. Репозиторий сохраняет только проверяемые факты и не восстанавливает закрытые prompts или шаги.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-103.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-103-poster.jpg" alt="Case 103 source video poster" height="360"></a>

[Play case 103 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-103.mp4)

Type: Tutorial | Date: 2026-07-20

---

<a id="case-106"></a>
### Case 106: [Сравнить стоимость humanoid frontend](https://x.com/ChrisGPT/status/2079236298464796958) (by [@ChrisGPT](https://x.com/ChrisGPT))

**Используйте этот кейс, чтобы оценить реальный workflow, стоимость или ограничения Kimi K3 в задаче «Сравнить стоимость humanoid frontend». **

Исходный пост дает публичные доказательства по теме «Сравнить стоимость humanoid frontend»: описание автора, медиа результата или данные benchmark/tutorial. Репозиторий сохраняет только проверяемые факты и не восстанавливает закрытые prompts или шаги.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-106.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-106-poster.jpg" alt="Case 106 source video poster" height="360"></a>

[Play case 106 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-106.mp4)

Type: Benchmark | Date: 2026-07-20

---

<a id="case-115"></a>
### Case 115: [Сравнить Three.js Kimi-vs-GLM](https://x.com/thehypedotnews/status/2079553731218325840) (by [@thehypedotnews](https://x.com/thehypedotnews))

**Запустите одинаковые procedural Three.js prompts на Kimi K3 и GLM 5.2, чтобы сравнить frontend и 3D build behavior.**

The Hype пишет, что тестировал Kimi K3 и GLM 5.2 на трех single-file HTML и Three.js prompts: гостиная 80-х с live CRT canvas texture, road bike с drivetrain kinematics и glass aquarium scene.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-115.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-115-poster.jpg" alt="Case 115 source video poster" height="360"></a>

[Play case 115 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-115.mp4)

Type: Benchmark | Date: 2026-07-21

---

<a id="case-121"></a>
### Case 121: [Создать лендинг по референсу](https://x.com/Oluwaphilemon1/status/2079951300108697683) (by [@Oluwaphilemon1](https://x.com/Oluwaphilemon1))

**Давайте Kimi K3 сильные визуальные референсы и итеративные указания при тесте генерации лендингов.**

Oluwaphilemon описывает лендинг с изображением-референсом и подробным prompt. Источник отмечает, что Kimi сначала пытался сделать велосипед как 3D-модель, а после нескольких уточнений пришел к более чистому результату.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-121.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-121-poster.jpg" alt="Case 121 source video poster" height="360"></a>

[Play case 121 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-121.mp4)

Type: Demo | Date: 2026-07-22

---

<a id="case-128"></a>
### Case 128: [Смоделировать 3D систему частиц](https://x.com/jadeferrara_/status/2079884161251262540) (by [@jadeferrara_](https://x.com/jadeferrara_))

**Используйте prompts для симуляции частиц, чтобы сравнить качество движения Kimi K3 с закрытыми моделями.**

Jade Ferrara сообщает, что дала Kimi K3 и Opus 4.8 один и тот же prompt 3D particle system. Kimi показал более органичное распределение, плавное движение и меньшую стоимость API.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-128.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-128-poster.jpg" alt="Case 128 source video poster" height="360"></a>

[Play case 128 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-128.mp4)

Type: Evaluation | Date: 2026-07-22

---


<a id="coding-integrations"></a>
## 💻 Код и интеграции

<a id="case-18"></a>
### Case 18: [Создать виртуальный MacBook с работающей macOS](https://x.com/scottstts/status/2077890054299541890) (by [@scottstts](https://x.com/scottstts))

**Объединить Three.js-рендеринг устройства с интерактивной симуляцией операционной системы в браузере**

Источник сообщает, что Kimi K3 создал виртуальный MacBook в Three.js с функциональной средой в стиле macOS. Артефакт показан, но шаги реализации отсутствуют

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-18.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-18-poster.jpg" alt="Case 18 source video poster" height="360"></a>

[Play case 18 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-18.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-25"></a>
### Case 25: [Создать GPU-компилятор от DSL до PTX](https://x.com/rohanpaul_ai/status/2077886618657231220) (by [@rohanpaul_ai](https://x.com/rohanpaul_ai))

**Использовать сквозную задачу компилятора, охватывающую DSL, compiler passes, генерацию PTX и путь Tensor Core**

Источник сообщает, что Kimi K3 с нуля создал GPU-компилятор: от DSL и passes до генерации PTX, а также сравнил путь Tensor Core с Triton. Независимые подробности benchmark в предоставленной записи отсутствуют

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-25-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-25-01.png" alt="Case 25 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-32"></a>
### Case 32: [Создать WebGL2 raytracer черной дыры в реальном времени](https://x.com/AlicanKiraz0/status/2077885419744612597) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**Проверить генерацию по одному prompt нативного WebGL2 geodesic raytracer в одном HTML-файле**

Автор описывает coding benchmark: рабочий однофайловый raytracer искривления света черной дырой на нативном WebGL2. Запись подтверждает задачу и участвующие модели, но не полный независимый аудит результатов

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-32.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-32-poster.jpg" alt="Case 32 source video poster" height="360"></a>

[Play case 32 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-32.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-46"></a>
### Case 46: [Создать эмулятор Game Boy Advance на основе mGBA WASM](https://x.com/teortaxesTex/status/2077925090168062272) (by [@teortaxesTex](https://x.com/teortaxesTex))

**Интегрировать лицензированную 3D-модель и настоящее ядро эмулятора, затем рекурсивно улучшать интерфейс и игровой процесс**

Указанный проект Kimi K3 адаптирует лицензированную модель AGB-001, интегрирует ядро mGBA WASM и улучшает интерфейс и игровой процесс через recursive self-improvement. Публикация цитирует описание проекта, а не независимое воспроизведение

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-46-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-46-01.jpg" alt="Case 46 source image 1" height="360"></a>

Type: Integration | Date: 2026-07-17

---

<a id="case-50"></a>
### Case 50: [Исследовать несколько тем по китайскоязычным источникам](https://x.com/tphuang/status/2077911994607239400) (by [@tphuang](https://x.com/tphuang))

**Использовать длительные research-задачи для сравнения полноты и latency разных поколений моделей**

Автор сообщает о тестировании Kimi K3 на множестве research-тем по китайскоязычным источникам: результат оказался полнее K2.6, но медленнее. В публикации также отмечается высокая нагрузка на сервис в тот момент

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-50-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-50-01.png" alt="Case 50 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-17

---

<a id="case-56"></a>
### Case 56: [Клонировать macOS в браузере с работающими приложениями](https://x.com/twid/status/2077924755357974989) (by [@twid](https://x.com/twid))

**Создать браузерную симуляцию операционной системы с приложениями музыки, браузера и email**

Источник сообщает, что Kimi K3 использовали для создания браузерного клона macOS с музыкой, браузером, email и другими функциями. Детали реализации не приведены

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-56.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-56-poster.jpg" alt="Case 56 source video poster" height="360"></a>

[Play case 56 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-56.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-62"></a>
### Case 62: [Создать симуляцию macOS с работающим FaceTime](https://x.com/LinearUncle/status/2077919552239997078) (by [@LinearUncle](https://x.com/LinearUncle))

**Использовать задачу виртуальной ОС, чтобы проверить работу сгенерированного взаимодействия приложения**

Автор показывает среду в стиле macOS, приписанную Kimi K3, и сообщает, что функция FaceTime работает. Шаги настройки или проверки отсутствуют

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-62-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-62-01.jpg" alt="Case 62 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-17

---

<a id="case-64"></a>
### Case 64: [Добавить frontend-компаратор эффектов двух задач](https://x.com/MinLiBuilds/status/2077939461510615376) (by [@MinLiBuilds](https://x.com/MinLiBuilds))

**Создать инструмент, который выбирает две завершенные задачи, показывает их рядом и синхронизирует views и interactions**

Автор сообщает о запросе Kimi K3 на frontend workflow сравнения с выбором задач, двумя browser panes, object и roaming modes, синхронизированными viewpoints и тестами interactions. Публикация также отмечает более широкие ограничения модели

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-64.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-64-poster.jpg" alt="Case 64 source video poster" height="360"></a>

[Play case 64 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-64.mp4)

Type: Tutorial | Date: 2026-07-17

---

<a id="case-75"></a>
### Case 75: [Настроить Kimi как субагента Codex](https://x.com/nauczymycieAI/status/2078181182701736132) (by [@nauczymycieAI](https://x.com/nauczymycieAI))

**Оставить оркестрацию Codex, а frontend передать субагенту Kimi K3 OpenCode с четкой границей секретов**

nauczymycieAI описывает установку OpenCode, ручное создание Kimi API key без вставки в Codex, подключение Kimi K3 и глобальный Codex skill для маршрутизации frontend-задач

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-75.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-75.jpg" alt="Case 75 source image 1" height="360"></a>

Type: Tutorial | Date: 2026-07-17

---

<a id="case-79"></a>
### Case 79: [Маршрутизировать простой код через ChatLLM](https://x.com/abacusai/status/2078022418661257411) (by [@abacusai](https://x.com/abacusai))

**Отправлять простой код Kimi K3, а сложный код и дизайн — другим моделям**

Abacus AI объявляет Kimi K3 в ChatLLM: простой код — Kimi K3, сложный — Fable 5, дизайн — GPT-5.6 Sol. Роутер работает в ChatLLM, Abacus AI Agent и Claude Code

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-79.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-79.jpg" alt="Case 79 source image 1" height="360"></a>

Type: Integration | Date: 2026-07-17

---

<a id="case-91"></a>
### Case 91: [Собрать CS с генеративными ассетами](https://x.com/karankendre/status/2078938615900688728) (by [@karankendre](https://x.com/karankendre))

**Совмещайте Kimi K3 для кода игры и GPT Image 2 для ассетов при прототипировании небольшого браузерного проекта в стиле Counter-Strike.**

Karan Kendre сообщает, что Kimi K3 собрал игру, а GPT Image 2 создал ассеты для проекта в стиле Counter-Strike с общей стоимостью около 10 долларов. Видео является видимым артефактом, поэтому кейс полезен как workflow сочетания инструментов, а не как чистый benchmark Kimi.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-91.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-91-poster.jpg" alt="Case 91 source video poster" height="360"></a>

[Play case 91 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-91.mp4)

Type: Integration | Date: 2026-07-19

---

<a id="case-95"></a>
### Case 95: [Использовать Design skill Command Code](https://x.com/MrAhmadAwais/status/2078841789205934547) (by [@MrAhmadAwais](https://x.com/MrAhmadAwais))

**Соединяйте Kimi K3 с выделенным design skill в Command Code, когда делаете визуальный игровой прототип под token budget.**

Ahmad Awais сообщает об использовании Kimi K3 с Command Code и /design skill для игры с chase camera в стиле Forza. Пост указывает стоимость сессии 0,97 доллара и исправления масштаба дороги и машины, фона, анимации и тумана, поэтому это конкретный agent-harness workflow.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-95.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-95-poster.jpg" alt="Case 95 source video poster" height="360"></a>

[Play case 95 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-95.mp4)

Type: Integration | Date: 2026-07-19

---

<a id="case-109"></a>
### Case 109: [Запустить Kimi K3 в Claude Code](https://x.com/boxmining/status/2079115758618239337) (by [@boxmining](https://x.com/boxmining))

**Используйте этот кейс, чтобы оценить реальный workflow, стоимость или ограничения Kimi K3 в задаче «Запустить Kimi K3 в Claude Code». **

Исходный пост дает публичные доказательства по теме «Запустить Kimi K3 в Claude Code»: описание автора, медиа результата или данные benchmark/tutorial. Репозиторий сохраняет только проверяемые факты и не восстанавливает закрытые prompts или шаги.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-109.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-109-poster.jpg" alt="Case 109 source video poster" height="360"></a>

[Play case 109 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-109.mp4)

Type: Integration | Date: 2026-07-20

---

<a id="case-119"></a>
### Case 119: [Маршрутизировать Kimi через claude-code-router](https://x.com/sairahul1/status/2079393675885588855) (by [@sairahul1](https://x.com/sairahul1))

**Попробуйте Kimi K3 в существующем Claude Code workflow через claude-code-router, избегая ненужного proxy mode.**

Sai Rahul описывает поддержку Kimi K3 в claude-code-router, спонсированную Moonshot: presets, импорт API key или subscription, native routing, dashboard balance/usage, failover, cache pricing и совет держать proxy mode выключенным без необходимости.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-119.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-119-poster.jpg" alt="Case 119 source video poster" height="360"></a>

[Play case 119 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-119.mp4)

Type: Integration | Date: 2026-07-21

---

<a id="case-125"></a>
### Case 125: [Запустить открытый agent harness](https://x.com/ShenSeanChen/status/2079914609222221976) (by [@ShenSeanChen](https://x.com/ShenSeanChen))

**Используйте общий agent harness, чтобы сравнить Kimi K3 с другими frontier-моделями на задачах с инструментами.**

Sean Chen описывает open-source harness с agent loop, memory retrieval gate, tool calls, evaluation, tracing и cost board, где Kimi K3 соревнуется с несколькими моделями.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-125.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-125-poster.jpg" alt="Case 125 source video poster" height="360"></a>

[Play case 125 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-125.mp4)

Type: Benchmark | Date: 2026-07-22

---

<a id="case-129"></a>
### Case 129: [Запустить Kimi через Codex OAuth](https://x.com/biscuitweb3/status/2079844959843197342) (by [@biscuitweb3](https://x.com/biscuitweb3))

**Используйте маршрут Codex OAuth, когда coding workflow с Kimi K3 должен обойти ручную настройку API key.**

biscuitweb3 сообщает, что Kimi K3 работает внутри Codex через OAuth без дополнительной настройки API key. Приложенный скриншот подтверждает интеграцию.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-129-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-129-01.jpg" alt="Case 129 source image 1" height="360"></a>

Type: Integration | Date: 2026-07-22

---


<a id="evaluation-limits"></a>
## 🧪 Оценка и ограничения

<a id="case-7"></a>
### Case 7: [Сравнить frontend-дизайн в задании BridgeBench с лавовой лампой](https://x.com/bridgemindai/status/2077868061953007908) (by [@bridgemindai](https://x.com/bridgemindai))

**Использовать задание BridgeBench с лавовой лампой как ограниченное сравнение frontend-дизайна, а не универсальный рейтинг**

BridgeMind AI сообщает, что Kimi K3 обошел Fable 5 в задании BridgeBench с лавовой лампой и занял первое место на указанной арене. Это результаты сравнения по данным издателя

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-07.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-07-poster.jpg" alt="Case 7 source video poster" height="360"></a>

[Play case 7 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-07.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-8"></a>
### Case 8: [Оценить написание сценариев в редакционном стиле](https://x.com/Whats_AI/status/2077860441380798908) (by [@Whats_AI](https://x.com/Whats_AI))

**Измерять соответствие редакционному голосу, относительное место и стоимость сценария внутри четко обозначенного внутреннего benchmark**

Whats_AI сообщает о ранних внутренних результатах: 2,840 Elo, первое место в своей таблице и около $0.25 за сценарий. Это предварительный benchmark одной организации, а не общая гарантия производительности или цены

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-08-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-08-01.jpg" alt="Case 8 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-16

---

<a id="case-10"></a>
### Case 10: [Сравнить дизайн, стоимость и сложность игры типа Flappy](https://x.com/MrAhmadAwais/status/2077915347974557862) (by [@MrAhmadAwais](https://x.com/MrAhmadAwais))

**При сравнении сгенерированных игр записывать настройки сложности, стоимость, дизайн и игровые возможности**

Внутренний Flappy benchmark Command Code сообщает о разных настройках сложности у моделей и указывает $0.024 для Kimi K3, $0.42 для Fable 5 и $0.15 для GPT-5.6 Sol. Неравные настройки ограничивают применимость этого внутреннего сравнения

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-10.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-10-poster.jpg" alt="Case 10 source video poster" height="360"></a>

[Play case 10 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-10.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-12"></a>
### Case 12: [Сравнить игровой дизайн с одним и тем же design prompt](https://x.com/CommandCodeAI/status/2077921526213746948) (by [@CommandCodeAI](https://x.com/CommandCodeAI))

**Зафиксировать design prompt и отдельно проверять темп, чувство дизайна и игровой процесс**

Command Code сообщает о сравнении Kimi K3, GPT-5.6 Sol и Fable 5 с одним prompt. По данным публикации, Kimi K3 показал хорошее чувство дизайна, а две другие модели играли слишком быстро; это оценка издателя

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-12.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-12-poster.jpg" alt="Case 12 source video poster" height="360"></a>

[Play case 12 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-12.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-13"></a>
### Case 13: [Требовать независимую проверку статистического аудита](https://x.com/emollick/status/2077869293031624793) (by [@emollick](https://x.com/emollick))

**Перед использованием выводов дополнять статистический аудит модели независимой экспертной проверкой или проверкой другой моделью**

Ethan Mollick сообщает, что Kimi K3 Max неверно применил статистику при аудите прежней академической работы, и соглашается с отдельной критикой. Этот отрицательный пример говорит в пользу независимой проверки

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-13-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-13-01.jpg" alt="Case 13 source image 1" height="360"></a>

Type: Limit | Date: 2026-07-16

---

<a id="case-16"></a>
### Case 16: [Оценить медленный, но сильный frontend-запуск](https://x.com/Lentils80/status/2077387333154857151) (by [@Lentils80](https://x.com/Lentils80))

**При тестировании frontend-задачи записывать время выполнения вместе с качеством результата**

Автор сообщает, что frontend-запуск Kimi K3 занял 35 минут, и называет результат одним из лучших для этого prompt. И скорость, и оценка качества являются наблюдением одного пользователя

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-16.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-16-poster.jpg" alt="Case 16 source video poster" height="360"></a>

[Play case 16 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-16.mp4)

Type: Evaluation | Date: 2026-07-15

---

<a id="case-20"></a>
### Case 20: [Проверить детективный текст на провалы с предзнаменованиями](https://x.com/emollick/status/2077951790868238616) (by [@emollick](https://x.com/emollick))

**Оценить, балансирует ли сгенерированный детектив между подсказками, неочевидностью и предзнаменованиями**

Ethan Mollick сообщает, что Kimi K3 не написал хороший детектив: подсказки были одновременно слишком очевидными и слишком туманными, а предзнаменования не сработали. Он также отмечает это ограничение у других моделей

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-01.jpg" alt="Case 20 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-02.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-02.png" alt="Case 20 source image 2" height="360"></a>

Type: Limit | Date: 2026-07-17

---

<a id="case-21"></a>
### Case 21: [Сравнить моделирование и анимацию Millennium Falcon](https://x.com/gmi_cloud/status/2077903360263676090) (by [@gmi_cloud](https://x.com/gmi_cloud))

**Использовать одинаковые запросы по стилю и настройки усилий для сравнения 3D-моделирования, анимации, времени и стоимости**

GMI Cloud сообщает о сравнении Kimi K3 и Fable 5 при воссоздании Millennium Falcon в пиксельном и оригинальном стилях с максимальным усилием. По их данным, Kimi K3 работал дольше, но стоил около одной трети в первом тесте и менее половины в другом; это результаты провайдера

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-21.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-21-poster.jpg" alt="Case 21 source video poster" height="360"></a>

[Play case 21 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-21.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-28"></a>
### Case 28: [Обозреть подборку из десяти проектов Kimi K3](https://x.com/minchoi/status/2077957907857994006) (by [@minchoi](https://x.com/minchoi))

**Использовать связанную подборку проектов для поиска конкретных артефактов, которые затем проверяются отдельно**

Автор собрал десять примеров Kimi K3 с медиа, включая эмулятор Game Boy Advance. Это коллекция, а не единый воспроизводимый workflow, поэтому каждый связанный пример следует проверять отдельно

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-28.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-28-poster.jpg" alt="Case 28 source video poster" height="360"></a>

[Play case 28 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-28.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-29"></a>
### Case 29: [Сравнить продвинутый landing page у четырех моделей](https://x.com/doutorcaleb/status/2077904020471947773) (by [@doutorcaleb](https://x.com/doutorcaleb))

**Зафиксировать запрос на landing page и сравнить глубину анимации и завершенность результатов моделей**

Автор сообщает, что дал один продвинутый prompt на landing page моделям Kimi K3, Fable, Grok и GPT Terra и считает результат Kimi K3 сильнейшим. Это самостоятельно заявленное сравнение одной задачи

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-29.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-29-poster.jpg" alt="Case 29 source video poster" height="360"></a>

[Play case 29 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-29.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-30"></a>
### Case 30: [Оценить механику и стоимость ретроигр](https://x.com/adxtyahq/status/2077860500462055570) (by [@adxtyahq](https://x.com/adxtyahq))

**Сравнивать игровой процесс, физику, механику, автономное поведение, расход tokens и стоимость на одинаковых ретроигровых задачах**

Источник сообщает о тестах Road Fighter, Battle City и Q*bert с одним prompt и указывает $0.28 для Kimi K3, $0.28 для GPT-5.6 и $0.54 для Opus 4.8. Это benchmark-цифры издателя

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-30.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-30-poster.jpg" alt="Case 30 source video poster" height="360"></a>

[Play case 30 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-30.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-31"></a>
### Case 31: [Сравнить генерацию игр с Fable 5](https://x.com/higgsfield_ai/status/2077943629633712490) (by [@higgsfield_ai](https://x.com/higgsfield_ai))

**Использовать параллельный пример сгенерированных игр как узкую оценку, а не общий вердикт о модели**

Higgsfield представляет сравнение генерации игр Kimi K3 и Fable 5. В предоставленной записи есть сравнительное медиа, но нет prompt, scoring rubric или подробных условий

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-31.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-31-poster.jpg" alt="Case 31 source video poster" height="360"></a>

[Play case 31 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-31.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-34"></a>
### Case 34: [Сравнить сложные frontend- и development-задачи с Opus 4.8](https://x.com/op7418/status/2077969583018066116) (by [@op7418](https://x.com/op7418))

**Использовать несколько сложных coding-задач для поиска побед и проигрышей, не объявляя одну модель универсально лучшей**

Обозреватель сообщает о прямых тестах Kimi K3 и Opus 4.8 и считает их примерно сопоставимыми на сложных frontend- и development-задачах, со смешанными результатами. Это оценка одного обозревателя

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-34.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-34-poster.jpg" alt="Case 34 source video poster" height="360"></a>

[Play case 34 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-34.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-35"></a>
### Case 35: [Рассмотреть benchmarks и тест landing page](https://x.com/adamuchigabriel/status/2077880433925120471) (by [@adamuchigabriel](https://x.com/adamuchigabriel))

**Объединить контекст benchmark с конкретным тестом генерации landing page, сохраняя раздельность двух типов доказательств**

Видео обсуждает benchmarks, тест landing page и наблюдения о frontend-дизайне Kimi K3. Полный тестовый prompt и scoring rubric в предоставленной записи отсутствуют

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-35.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-35-poster.jpg" alt="Case 35 source video poster" height="360"></a>

[Play case 35 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-35.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-37"></a>
### Case 37: [Оценить индуктивное рассуждение на задачах граф-в-формулу](https://x.com/s_batzoglou/status/2077884096307454119) (by [@s_batzoglou](https://x.com/s_batzoglou))

**Измерять правильность, поведение на holdout и сложность формулы в задачах first-order induction**

Автор сообщает о benchmark Kimi K3 и других моделей на задаче ICML INDUCTION: по 6–10 малым графам с 8–10 элементами нужно вывести формулу первого порядка. Публикация обновляет более ранние результаты; независимое воспроизведение здесь не заявляется

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-37-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-37-01.png" alt="Case 37 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-16

---

<a id="case-38"></a>
### Case 38: [Обозреть заявленные игры, landing pages, 3D-работы и long context](https://x.com/servasyy_ai/status/2077903775113834689) (by [@servasyy_ai](https://x.com/servasyy_ai))

**Использовать мульти-source roundup для сравнения конкретных артефактов и отмечать ограничения скорости рядом с заявлениями о стоимости**

Автор суммирует опубликованные тесты Kimi K3 по играм, landing pages, 3D-генерации и long-context работе и заключает, что модель стоит попробовать, но она пока не заменяет Fable 5. Все цифры — вторичные сообщения этого roundup

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-38-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-38-01.jpg" alt="Case 38 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-40"></a>
### Case 40: [Проверить сложный план и оспорить его способы исправления](https://x.com/doodlestein/status/2077901883637665958) (by [@doodlestein](https://x.com/doodlestein))

**Использовать вторую модель для поиска заниженных выводов, неверных remedies и заключений, которые следует отвергнуть**

Автор сообщает, что Kimi K3 проверил тщательно доработанный план и обнаружил занижение серьезных проблем, необходимость исправить около одной трети предложенных remedies и опровержение одного вывода. Это результаты конкретного аудита

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-40-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-40-01.jpg" alt="Case 40 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-41"></a>
### Case 41: [Сравнить ASCII-диаграммы reinforcement-learning цикла в стиле PPO](https://x.com/dejavucoder/status/2077872015856615541) (by [@dejavucoder](https://x.com/dejavucoder))

**Зафиксировать prompt ASCII-диаграммы и сравнить представление reinforcement-learning цикла моделями**

Источник публикует prompt на ASCII-схему reinforcement-learning цикла в стиле PPO и показывает Kimi K3 Max рядом с Fable 5 High. Оценка остается визуальным сравнением одной задачи

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-01.png" alt="Case 41 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-02.jpg" alt="Case 41 source image 2" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-42"></a>
### Case 42: [Моделировать в Blender с учетом ошибок capacity](https://x.com/Angaisb_/status/2077910845523214668) (by [@Angaisb_](https://x.com/Angaisb_))

**Оценивать частичный прогресс Blender вместе с надежностью сервиса, а не только артефакт**

Автор показывает прогресс моделирования Kimi K3 в Blender и сообщает о повторяющихся ошибках capacity. Работа в источнике не завершена, поэтому частичный результат и ограничение надежности следует рассматривать вместе

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-42-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-42-01.jpg" alt="Case 42 source image 1" height="360"></a>

Type: Limit | Date: 2026-07-17

---

<a id="case-47"></a>
### Case 47: [Сравнить генерацию Flappy Bird на арене](https://x.com/jun_song/status/2077396996865003739) (by [@jun_song](https://x.com/jun_song))

**Использовать arena-задачу для сравнения двух результатов Flappy Bird, сохраняя оценку специфичной для этой задачи**

Автор сообщает о сравнении Kimi K3 и Opus 4.8 на задаче Flappy Bird в Arena и оценивает Kimi K3 значительно выше. Полный prompt или rubric в записи отсутствует

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-47.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-47-poster.jpg" alt="Case 47 source video poster" height="360"></a>

[Play case 47 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-47.mp4)

Type: Evaluation | Date: 2026-07-15

---

<a id="case-52"></a>
### Case 52: [Решить визуальную индуктивную задачу Bongard с инструментом](https://x.com/IntuitMachine/status/2077885406528311561) (by [@IntuitMachine](https://x.com/IntuitMachine))

**Проверить, помогает ли использование инструмента вывести визуальное правило в задаче рассуждения Bongard**

Автор сообщает, что Kimi K3 с помощью инструмента решил задачу Bongard, которую Grok 4.5 и Muse Spark 1.1 не решили в том же сравнении. Это результат одной пользовательской задачи, а не общий reasoning benchmark

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-52-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-52-01.jpg" alt="Case 52 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-53"></a>
### Case 53: [Сравнить frontend-вкус и 3D-дизайн с GPT-5.6 Sol](https://x.com/filicroval/status/2077736407506751952) (by [@filicroval](https://x.com/filicroval))

**Проверять возможности, визуальный вкус, элегантность и 3D-исполнение в ограниченном frontend-сравнении**

Автор сравнивает Kimi K3 и GPT-5.6 Sol во frontend-дизайне и считает Kimi K3 сильнее по визуальному вкусу, элегантности и 3D-возможностям. Оценка субъективна и специфична для задачи

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-53.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-53-poster.jpg" alt="Case 53 source video poster" height="360"></a>

[Play case 53 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-53.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-57"></a>
### Case 57: [Сравнить генерацию сайтов у трех моделей](https://x.com/pengchujin/status/2077962916226298340) (by [@pengchujin](https://x.com/pengchujin))

**Использовать видимые результаты сайтов для сравнения Kimi K3, Fable 5 и GPT-5.6 Sol в одном тесте**

Автор представляет сравнение генерации сайтов Kimi K3, Fable 5 и GPT-5.6 Sol. Полный prompt и scoring rubric в предоставленной записи не раскрыты

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-57.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-57-poster.jpg" alt="Case 57 source video poster" height="360"></a>

[Play case 57 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-57.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-59"></a>
### Case 59: [Сравнить процедурную генерацию 3D-игр и стоимость](https://x.com/adxtyahq/status/2077958193511362856) (by [@adxtyahq](https://x.com/adxtyahq))

**Зафиксировать prompt между моделями и проверять сгенерированные системы рулетки, slot machine и pinball со стоимостью каждого запуска**

Издатель сообщает о многомодельном сравнении процедурных 3D-игр и указывает стоимость, включая $0.71 для Kimi K3 и $0.30 для Grok 4.5. Все рейтинги и цены относятся к запуску этого издателя

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-59.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-59-poster.jpg" alt="Case 59 source video poster" height="360"></a>

[Play case 59 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-59.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-69"></a>
### Case 69: [Сравнить детализацию и освещение 3D-сцены арсенала](https://x.com/hakki_alkan/status/2077887013332636032) (by [@hakki_alkan](https://x.com/hakki_alkan))

**Проверять плотность объектов, освещение и детализацию сцены в ограниченном сравнении Kimi K3 и Opus 4.8**

Источник сообщает, что Kimi K3 создал детальную сцену арсенала с заполненными полками, коробками и реалистичным освещением, а Opus 4.8 — пустую комнату. Это сторонний отчет о сравнении, не независимый benchmark

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-69-poster.jpg" alt="Case 69 source video poster" height="360"></a>

[Play case 69 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-69.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-72"></a>
### Case 72: [Сравнить фронтенды на одинаковых prompt Arena](https://x.com/arena/status/2078240399517524365) (by [@arena](https://x.com/arena))

**Использовать одинаковые prompt и параллельные результаты вместо одного места в рейтинге**

Arena.ai публикует сравнение Kimi K3 и Fable 5 в Frontend Code Arena на одинаковых prompt. Видео сохраняет оба результата в одинаковых условиях

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-72.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-72-poster.jpg" alt="Case 72 source video poster" height="360"></a>

[Play case 72 comparison video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-72.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-74"></a>
### Case 74: [Оценить Kimi Code на coding-агентах](https://x.com/ArtificialAnlys/status/2078230240766345330) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Оценивать Kimi K3 по нескольким тестам и стоимости задачи, не обобщая один frontend-рейтинг**

Artificial Analysis сообщает 57 баллов и совместное пятое место: 84% в Terminal-Bench v2, 64% в DeepSWE, 23% в SWE-Atlas-QnA и 3,18 доллара за задачу

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-74.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-74.jpg" alt="Case 74 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-17

---

<a id="case-76"></a>
### Case 76: [Сравнить Arena и repair harness](https://x.com/AlphaSignalAI/status/2078172629496746183) (by [@AlphaSignalAI](https://x.com/AlphaSignalAI))

**Смотреть и frontend-предпочтения, и ремонт репозитория, поскольку Kimi K3 может быть первым в одном и седьмым в другом**

AlphaSignal сообщает первое место с 1679 баллами в Frontend Code Arena, но 53 успеха из 67, то есть 79%, и седьмое место в тесте ремонта coding-агентов

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-76.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-76.jpg" alt="Case 76 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-17

---

<a id="case-80"></a>
### Case 80: [Проверить Kimi K3 в Prinzbench](https://x.com/deredleritt3r/status/2078606700496773166) (by [@deredleritt3r](https://x.com/deredleritt3r))

**Prinzbench сравнивает Kimi K3 с OpenAI o3 и другими моделями, показывая место и ограничения в одном бенчмарке.**

Пост включает Kimi K3 в таблицу Prinzbench и показывает разрыв с ведущими моделями, а также относительные сильные стороны в задачах оценки.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-80-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-80-01.png" alt="Case 80 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-18

---

<a id="case-85"></a>
### Case 85: [Сравнить генерацию цифрового двойника МКС](https://x.com/AIsaOneHQ/status/2078519527588200536) (by [@AIsaOneHQ](https://x.com/AIsaOneHQ))

**Kimi K3 сравнивается с другими моделями на задаче цифрового двойника МКС, показывая различия в сложной 3D-визуализации.**

Пост сравнивает несколько результатов для одной задачи про МКС и помогает увидеть структурное понимание и визуальные ограничения Kimi K3.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-85.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-85-poster.jpg" alt="Case 85 source video poster" height="360"></a>

[Play case 85 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-85.mp4)

Type: Benchmark | Date: 2026-07-18

---

<a id="case-89"></a>
### Case 89: [Оценить WebGPU-лес](https://x.com/stas_sorokin_/status/2078435840728908093) (by [@stas_sorokin_](https://x.com/stas_sorokin_))

**Лесная WebGPU-сцена, созданная Kimi K3, оценивается по выразительности и ограничениям иммерсивного 3D.**

Видео показывает лесное окружение в браузере и служит доказательством возможностей Kimi K3 для WebGPU/3D-сцен.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-89.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-89-poster.jpg" alt="Case 89 source video poster" height="360"></a>

[Play case 89 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-89.mp4)

Type: Evaluation | Date: 2026-07-18

---

<a id="case-90"></a>
### Case 90: [Сравнить промпты стеклянного дома](https://x.com/RoundtableSpace/status/2079004612070416755) (by [@RoundtableSpace](https://x.com/RoundtableSpace))

**Используйте одну архитектурную сцену, чтобы сравнить Kimi K3 и Opus 4.8 по атмосфере, свету и пространственной завершенности.**

Roundtable Space сообщает о сравнении Kimi K3 и Claude Opus 4.8 на одном промпте и примерно близкой цене. Результат Kimi описан как стеклянный дом в синий час с теплым внутренним светом, отражающим бассейном и чертежами, тогда как Opus выглядит более типографическим и менее пространственно полным.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-90.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-90-poster.jpg" alt="Case 90 source video poster" height="360"></a>

[Play case 90 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-90.mp4)

Type: Evaluation | Date: 2026-07-20

---

<a id="case-92"></a>
### Case 92: [Проверить voxel-футбольный гол](https://x.com/0xzynex/status/2078920667542487230) (by [@0xzynex](https://x.com/0xzynex))

**Запустите один и тот же prompt для футбольной анимации на чистом HTML/CSS/JS в двух моделях, чтобы сравнить движение и стоимость.**

0xzynex сообщает об one-shot сравнении без повторов: Kimi K3 и GPT-5.6 Sol High строили блочную футбольную сцену с дриблингом, голом, динамичной камерой и празднованием в браузерном коде. В посте сказано, что Kimi дал более плавное движение и меньшую стоимость; видео сохраняет артефакт сравнения.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-92.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-92-poster.jpg" alt="Case 92 source video poster" height="360"></a>

[Play case 92 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-92.mp4)

Type: Benchmark | Date: 2026-07-19

---

<a id="case-93"></a>
### Case 93: [Разобрать Minecraft benchmark](https://x.com/ashen_one/status/2078892418976666071) (by [@ashen_one](https://x.com/ashen_one))

**Посмотрите структурированный Minecraft-обзор, прежде чем считать хайп запуска или цену достаточным доказательством.**

ashen_one публикует записанный обзор Kimi K3 с разделами о hype versus reality, benchmarks, pricing, Minecraft test, first-run bugs и final verdict. Источник полезен тем, что объединяет рамку benchmark и ранние заметки о надежности в одном проверяемом видео.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-93.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-93-poster.jpg" alt="Case 93 source video poster" height="360"></a>

[Play case 93 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-93.mp4)

Type: Benchmark | Date: 2026-07-19

---

<a id="case-98"></a>
### Case 98: [Измерить API tier limits](https://x.com/mnmn94253156337/status/2078739859154620497) (by [@mnmn94253156337](https://x.com/mnmn94253156337))

**Планируйте Kimi K3 agent runs по tokens, tier, TPM и TPD, а не только по headline model pricing.**

Китайскоязычный источник описывает личный тест Kimi K3 API после пополнения на 5 долларов: около 1,1 доллара ушло во время настройки, затем сработали Tier0 limits. Он перечисляет цены input, cached input и output, а также TPM/TPD, поэтому это ранний отчет об ограничениях.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-98.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-98-poster.jpg" alt="Case 98 source video poster" height="360"></a>

[Play case 98 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-98.mp4)

Type: Limit | Date: 2026-07-19

---

<a id="case-99"></a>
### Case 99: [Сравнить Limbo-style demo](https://x.com/ChrisGPT/status/2078679211116835017) (by [@ChrisGPT](https://x.com/ChrisGPT))

**Сравнивайте playable scope, polish, cost и bugs при тестировании Kimi K3 против Fable 5 на одном игровом prototype.**

ChrisGPT сравнивает Fable 5 и Kimi K3 на Limbo clone demo. В посте указано: Fable дал 2 400 lines и 24K output tokens за 1,20 доллара, Kimi дал 3 000 lines и 30K tokens за 0,12 доллара; Kimi добавил больше gameplay, но и больше bugs.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-99.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-99-poster.jpg" alt="Case 99 source video poster" height="360"></a>

[Play case 99 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-99.mp4)

Type: Benchmark | Date: 2026-07-19

---

<a id="case-100"></a>
### Case 100: [Проверить затраты VulcanBench](https://x.com/morganlinton/status/2079358902194569357) (by [@morganlinton](https://x.com/morganlinton))

**Используйте этот кейс, чтобы оценить реальный workflow, стоимость или ограничения Kimi K3 в задаче «Проверить затраты VulcanBench». **

Исходный пост дает публичные доказательства по теме «Проверить затраты VulcanBench»: описание автора, медиа результата или данные benchmark/tutorial. Репозиторий сохраняет только проверяемые факты и не восстанавливает закрытые prompts или шаги.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-100-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-100-01.jpg" alt="Case 100 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-21

---

<a id="case-104"></a>
### Case 104: [Оценить физику двойного маятника](https://x.com/AlicanKiraz0/status/2079241239736504768) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**Используйте этот кейс, чтобы оценить реальный workflow, стоимость или ограничения Kimi K3 в задаче «Оценить физику двойного маятника». **

Исходный пост дает публичные доказательства по теме «Оценить физику двойного маятника»: описание автора, медиа результата или данные benchmark/tutorial. Репозиторий сохраняет только проверяемые факты и не восстанавливает закрытые prompts или шаги.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-104.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-104-poster.jpg" alt="Case 104 source video poster" height="360"></a>

[Play case 104 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-104.mp4)

Type: Benchmark | Date: 2026-07-20

---

<a id="case-107"></a>
### Case 107: [Проверить готовность ReactBench](https://x.com/aidenybai/status/2079233934693650567) (by [@aidenybai](https://x.com/aidenybai))

**Используйте этот кейс, чтобы оценить реальный workflow, стоимость или ограничения Kimi K3 в задаче «Проверить готовность ReactBench». **

Исходный пост дает публичные доказательства по теме «Проверить готовность ReactBench»: описание автора, медиа результата или данные benchmark/tutorial. Репозиторий сохраняет только проверяемые факты и не восстанавливает закрытые prompts или шаги.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-107.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-107-poster.jpg" alt="Case 107 source video poster" height="360"></a>

[Play case 107 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-107.mp4)

Type: Benchmark | Date: 2026-07-20

---

<a id="case-110"></a>
### Case 110: [Оценить Kimi K3 на AA-Briefcase](https://x.com/ArtificialAnlys/status/2079715807983210572) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Используйте результаты AA-Briefcase, чтобы оценить Kimi K3 в agentic knowledge-work задачах до доверия лидербордам.**

Artificial Analysis сообщает, что Kimi K3 набрал 1543 Elo на AA-Briefcase и занял второе место после Claude Fable 5, но также отмечает почти час на задачу и стоимость выше Opus 4.8 в этом бенчмарке.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-110-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-110-01.jpg" alt="Case 110 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-21

---

<a id="case-113"></a>
### Case 113: [Проверить оговорки frontend leaderboard](https://x.com/RetroChainer/status/2079622227796885850) (by [@RetroChainer](https://x.com/RetroChainer))

**Используйте эту limitation note, чтобы отделить победы Kimi K3 в leaderboard от широких claim про coding и cost.**

RetroChainer подтверждает лидерство в Frontend Code Arena и цены, но отмечает ограничения: рейтинг относится к одному board, weights на момент поста не были публичны, savings per job основаны на одной задаче, а max reasoning может сжигать tokens на малой работе.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-113.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-113-poster.jpg" alt="Case 113 source video poster" height="360"></a>

[Play case 113 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-113.mp4)

Type: Limit | Date: 2026-07-21

---

<a id="case-114"></a>
### Case 114: [Сравнить StackPerf architecture results](https://x.com/tamsi_besson/status/2079573266855834071) (by [@tamsi_besson](https://x.com/tamsi_besson))

**Используйте StackPerf для сравнения Kimi K3 и Qwen 3.8 по architecture quality, speed и tool-call behavior.**

Tamsi Besson делится snapshot StackPerf, где Kimi K3 слегка обходит Qwen 3.8 Max Preview по качеству и быстрее в сумме, тогда как у Qwen 0 failed tool calls против 2 у Kimi, хотя Kimi сделал больше calls.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-114-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-114-01.jpg" alt="Case 114 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-21

---

<a id="case-118"></a>
### Case 118: [Сравнить cost prompt Monument Valley](https://x.com/AiHubMix/status/2079507420083294557) (by [@AiHubMix](https://x.com/AiHubMix))

**Используйте один Monument Valley-style prompt, чтобы сравнить visual quality, runtime и cost Kimi K3 и других моделей.**

AiHubMix сравнивает Claude Fable 5, Kimi K3 и GPT-5.6 Sol на одном Monument Valley-style prompt. Пост называет Fable самым coherent, Kimi самым медленным при 52m30s и $1.50, а GPT-5.6 Sol самым быстрым и дешевым, но слабее в spatial logic.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-118.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-118-poster.jpg" alt="Case 118 source video poster" height="360"></a>

[Play case 118 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-118.mp4)

Type: Benchmark | Date: 2026-07-21

---

<a id="case-120"></a>
### Case 120: [Оценить Kimi K3 в индексе Surge](https://x.com/echen/status/2080021575190110523) (by [@echen](https://x.com/echen))

**Используйте раздельные результаты SurgeAI, чтобы отделить силу Kimi K3 в обычном чате от слабых мест в агентных и научных задачах.**

Eric Chen сообщает, что SurgeAI проверила Kimi K3 на индексе с обычными чатботами, корпоративными агентами, глубоким рассуждением и frontier science. Пост говорит, что Kimi силен в обычном чате, но уступает Fable и Sol в агентных и научных задачах.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-120-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-120-01.jpg" alt="Case 120 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-22

---

<a id="case-123"></a>
### Case 123: [Оценить ошибки PDE solver](https://x.com/lanyon_ai/status/2079931884511887740) (by [@lanyon_ai](https://x.com/lanyon_ai))

**Используйте ошибки PDE-бенчмарка, чтобы понять, где символические и численные задачи с Kimi K3 требуют проверки.**

Lanyon AI сравнивает свою нейросимвольную архитектуру с frontier-моделями, включая Kimi K3, на простых линейных PDE. Источник сообщает о математических, алгоритмических и вычислительных ошибках даже при подробных prompts.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-123-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-123-01.jpg" alt="Case 123 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-22

---

<a id="case-124"></a>
### Case 124: [Разобрать EHR кейсы ClinicalBench](https://x.com/mkurman88/status/2079918374977413534) (by [@mkurman88](https://x.com/mkurman88))

**Используйте EHR кейсы ClinicalBench, чтобы увидеть, где Kimi K3 справляется и где диагностическое рассуждение еще дает сбой.**

Michael Kurman сообщает результаты ClinicalBench v0.0.4 для Kimi K3 в виртуальной EHR-песочнице с 10 случаями отделения неотложной помощи. Kimi решил 7 из 10 и затруднился с шестым случаем.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-124-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-124-01.jpg" alt="Case 124 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-124-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-124-02.jpg" alt="Case 124 source image 2" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-124-03.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-124-03.jpg" alt="Case 124 source image 3" height="360"></a>

Type: Benchmark | Date: 2026-07-22

---

<a id="case-126"></a>
### Case 126: [Оценить налоговые расчеты](https://x.com/michaelrbock/status/2079913117698666964) (by [@michaelrbock](https://x.com/michaelrbock))

**Тестируйте Kimi K3 отдельно на налоговых задачах, не предполагая перенос силы во frontend.**

Michael Bock сообщает тест на 50 реалистичных федеральных и штатных налоговых декларациях. Источник дает Kimi K3 6% в TaxCalcBench, против 58% у GPT-5.6 Sol и 4% у Fable 5.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-126-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-126-01.jpg" alt="Case 126 source image 1" height="360"></a>

Type: Limit | Date: 2026-07-22

---

<a id="related-resources"></a>
## Связанные ресурсы

- [Посмотреть Kimi K3 и цены на EvoLink](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=landing_overview)
- [Открыть документацию EvoLink Kimi K3 API](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=docs_link)
- [Подробнее о Kimi K3 на EvoLink](https://evolink.ai/blog/is-kimi-k3-available-on-evolink?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_article)
- [KimiK3.io](https://kimik3.io/ru/)
- Страница модели и документация EvoLink API проверены; устанавливаемый skill Kimi K3 не проверен

<a id="acknowledge"></a>
## 🙏 Благодарности

Спасибо всем, кто публично поделился работами с Kimi K3

[@ivanfioravanti](https://x.com/ivanfioravanti), [@TheAhmadOsman](https://x.com/TheAhmadOsman), [@HarshithLucky3](https://x.com/HarshithLucky3), [@chetaslua](https://x.com/chetaslua), [@abhinavflac](https://x.com/abhinavflac), [@bridgemindai](https://x.com/bridgemindai), [@Whats_AI](https://x.com/Whats_AI), [@chongdashu](https://x.com/chongdashu), [@MrAhmadAwais](https://x.com/MrAhmadAwais), [@bijanbowen](https://x.com/bijanbowen), [@CommandCodeAI](https://x.com/CommandCodeAI), [@emollick](https://x.com/emollick), [@nicky_sap](https://x.com/nicky_sap), [@Lentils80](https://x.com/Lentils80), [@scottstts](https://x.com/scottstts), [@aisearchio](https://x.com/aisearchio), [@gmi_cloud](https://x.com/gmi_cloud), [@karminski3](https://x.com/karminski3), [@VORTEX_Promos](https://x.com/VORTEX_Promos), [@rohanpaul_ai](https://x.com/rohanpaul_ai), [@mirochill](https://x.com/mirochill), [@aimlapi](https://x.com/aimlapi), [@minchoi](https://x.com/minchoi), [@doutorcaleb](https://x.com/doutorcaleb), [@adxtyahq](https://x.com/adxtyahq), [@higgsfield_ai](https://x.com/higgsfield_ai), [@AlicanKiraz0](https://x.com/AlicanKiraz0), [@1littlecoder](https://x.com/1littlecoder), [@op7418](https://x.com/op7418), [@adamuchigabriel](https://x.com/adamuchigabriel), [@s_batzoglou](https://x.com/s_batzoglou), [@servasyy_ai](https://x.com/servasyy_ai), [@filicroval](https://x.com/filicroval), [@doodlestein](https://x.com/doodlestein), [@dejavucoder](https://x.com/dejavucoder), [@Angaisb_](https://x.com/Angaisb_), [@AngryTomtweets](https://x.com/AngryTomtweets), [@Alezander907](https://x.com/Alezander907), [@teortaxesTex](https://x.com/teortaxesTex), [@jun_song](https://x.com/jun_song), [@ridark_eth](https://x.com/ridark_eth), [@naymur_dev](https://x.com/naymur_dev), [@tphuang](https://x.com/tphuang), [@TokenGremlin](https://x.com/TokenGremlin), [@IntuitMachine](https://x.com/IntuitMachine), [@wangfeng0315](https://x.com/wangfeng0315), [@twid](https://x.com/twid), [@pengchujin](https://x.com/pengchujin), [@aayushman2703](https://x.com/aayushman2703), [@goncalo_canhoto](https://x.com/goncalo_canhoto), [@LinearUncle](https://x.com/LinearUncle), [@gagarot200](https://x.com/gagarot200), [@MinLiBuilds](https://x.com/MinLiBuilds), [@izutorishima](https://x.com/izutorishima), [@X2worldtech](https://x.com/X2worldtech), [@Satvik_Pen](https://x.com/Satvik_Pen), [@hakki_alkan](https://x.com/hakki_alkan), [@BrianMRey](https://x.com/BrianMRey), [@ChrisGPT](https://x.com/ChrisGPT), [@arena](https://x.com/arena), [@MathiasHeide](https://x.com/MathiasHeide), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@nauczymycieAI](https://x.com/nauczymycieAI), [@AlphaSignalAI](https://x.com/AlphaSignalAI), [@Ananth7e](https://x.com/Ananth7e), [@viktoroddy](https://x.com/viktoroddy), [@abacusai](https://x.com/abacusai), [@deredleritt3r](https://x.com/deredleritt3r), [@fabriciocarraro](https://x.com/fabriciocarraro), [@startracker](https://x.com/startracker), [@mattwatkajtys](https://x.com/mattwatkajtys), [@AIsaOneHQ](https://x.com/AIsaOneHQ), [@MiaAI_lab](https://x.com/MiaAI_lab), [@hqmank](https://x.com/hqmank), [@prasenx](https://x.com/prasenx), [@stas_sorokin_](https://x.com/stas_sorokin_), [@RoundtableSpace](https://x.com/RoundtableSpace), [@karankendre](https://x.com/karankendre), [@0xzynex](https://x.com/0xzynex), [@ashen_one](https://x.com/ashen_one), [@MAXdeg0](https://x.com/MAXdeg0), [@ice_bearcute](https://x.com/ice_bearcute), [@mnmn94253156337](https://x.com/mnmn94253156337), [@morganlinton](https://x.com/morganlinton), [@vikktorrrre](https://x.com/vikktorrrre), [@kirillk_web3](https://x.com/kirillk_web3), [@_guillecasaus](https://x.com/_guillecasaus), [@demian_ai](https://x.com/demian_ai), [@aidenybai](https://x.com/aidenybai), [@LexnLin](https://x.com/LexnLin), [@boxmining](https://x.com/boxmining), [@Nekt_0](https://x.com/Nekt_0), [@RetroChainer](https://x.com/RetroChainer), [@tamsi_besson](https://x.com/tamsi_besson), [@thehypedotnews](https://x.com/thehypedotnews), [@AiHubMix](https://x.com/AiHubMix), [@sairahul1](https://x.com/sairahul1), [@echen](https://x.com/echen), [@Oluwaphilemon1](https://x.com/Oluwaphilemon1), [@diegocabezas01](https://x.com/diegocabezas01), [@lanyon_ai](https://x.com/lanyon_ai), [@mkurman88](https://x.com/mkurman88), [@ShenSeanChen](https://x.com/ShenSeanChen), [@michaelrbock](https://x.com/michaelrbock), [@Kirratr](https://x.com/Kirratr), [@jadeferrara_](https://x.com/jadeferrara_), [@biscuitweb3](https://x.com/biscuitweb3)

*Для исправления атрибуции или текста откройте issue и приложите публичный источник*
