<div align="center">

<a href="https://evolink.ai/kimi-k3?utm_source=github&utm_medium=banner&utm_campaign=awesome-kimi-k3-usecases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/images/es-v2.png" alt="Banner localizado de Kimi K3 con paisaje lunar y llamada a la acción de EvoLink" width="760"></a>

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

# Casos de uso increíbles de Kimi K3

## 🍌 Introducción

Bienvenido al repositorio de casos de uso de alta señal de Kimi K3

**Recopilamos juegos, escenas 3D, diseños en movimiento, integraciones, evaluaciones y límites prácticos de Kimi K3 respaldados por fuentes públicas**

Los 70 casos de esta edición incluyen todos y únicamente los elementos de alta confianza del paquete de fuentes proporcionado; se excluyen los 31 casos de confianza media. Los títulos enlazan a las publicaciones originales y los autores a sus perfiles

[EvoLink](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=introduction_cta)

## 📊 Resumen

- Los 70 casos de alta confianza están incluidos y los 31 casos de confianza media están excluidos
- Incluye juegos interactivos, 3D, frontend, motion graphics, programación, integraciones, investigación, evaluaciones y límites prácticos
- Cada caso conserva fuente, autor, tipo, fecha y límite del prompt
- Las experiencias individuales no se presentan como benchmarks

> [!NOTE]
> La colección prioriza evidencia concreta. No reconstruye prompts ausentes ni inventa pasos de configuración

## ⚡ Inicio rápido

El ID documentado por EvoLink es `kimi-k3`; la página del modelo y la documentación de Chat Completions están disponibles

1. [Ver detalles y precios de Kimi K3 en EvoLink](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-kimi-k3-usecases&utm_content=model_link)
2. [Crear o administrar una clave API de EvoLink](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-kimi-k3-usecases&utm_content=api_key)
3. [Abrir la documentación API de Kimi K3 en EvoLink](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=first_run)

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
> La página del modelo y la documentación de EvoLink verifican la ruta pública y el ID. Este repositorio no afirma una prueba API de pago independiente

## 📑 Menú

| Section | Cases |
|---|---|
| [Juegos interactivos y 3D](#games-3d) | 22 |
| [Frontend y diseño en movimiento](#frontend-motion) | 15 |
| [Programación e integraciones](#coding-integrations) | 8 |
| [Evaluación y límites](#evaluation-limits) | 25 |
| [Agradecimientos](#acknowledge) | Créditos y correcciones |

<a id="games-3d"></a>
## 🎮 Juegos interactivos y 3D

| Case | What it shows | Type |
|---|---|---|
| [Crear un pod racer voxel con un prompt](#case-1) | Usa una idea breve para prototipar una carrera voxel y define una segunda iteración | Demo |
| [Comparar Frogger con el mismo prompt](#case-2) | Mantén constante el prompt para inspeccionar diferencias entre modelos | Evaluation |
| [Generar Frogger y su grabación](#case-3) | Prueba en una sola ejecución tanto el juego como el flujo de grabación | Demo |
| [Prototipar un portaaviones en Three.js](#case-4) | Usa una escena concreta para probar un prototipo 3D interactivo | Demo |
| [Crear un juego inspirado en Paper Mario con herramientas de agente](#case-9) | Combina Kimi K3 con un harness de agente y herramientas de recursos para producir elementos de juego tanto 2D como 3D | Demo |
| [Generar un shooter en primera persona ambientado en el metro](#case-11) | Usa un escenario concreto de metro para examinar el resultado de un shooter en primera persona generado | Demo |
| [Modelar un motor V8 con Blender MCP](#case-19) | Usa Blender MCP y una sola petición para generar un modelo mecánico 3D detallado | Integration |
| [Crear una arena de combate jugable a partir de una referencia](#case-23) | Usa una sola referencia para probar la generación de una arena jugable completa en una ejecución | Demo |
| [Crear tres juegos retro autónomos como archivos HTML](#case-24) | Exige gráficos, enemigos, reglas y juego autónomo dentro de archivos HTML independientes | Benchmark |
| [Crear en una ejecución un juego de escondite con camaleones](#case-27) | Genera un juego en un solo archivo con combinación de colores, zonas procedimentales, sonido y puntuación en varias rondas | Benchmark |
| [Crear un juego 2.5D al estilo Paper Mario con herramientas de agente](#case-36) | Usa Kimi K3 con Grok Build o Claude Code y Spriterrific para montar un flujo de trabajo de juego 2.5D | Tutorial |
| [Crear un RPG wuxia 3D para navegador](#case-43) | Combina combate cuerpo a cuerpo, misiones, inventario, clima, interiores, trabajo de entornos en Blender y recursos adaptados | Demo |
| [Crear un juego multijugador de navegador al estilo Minecraft](#case-44) | Usa una ejecución acotada por tiempo y coste para producir un juego multijugador online jugable en el navegador | Demo |
| [Recrear un juego cooperativo de navegador con pantalla dividida](#case-48) | Usa una petición para generar cooperación en pantalla dividida dentro del navegador e interacción con el entorno en tiempo real | Demo |
| [Generar un juego jugable con el modo de diseño de Command Code](#case-49) | Usa el comando de diseño de Command Code para crear un juego en una sola ejecución y registra si el resultado es jugable | Demo |
| [Montar un RPG wuxia de navegador cohesionado](#case-51) | Integra desplazamiento, combate, misiones, inventario, clima, exploración y trabajo de entornos 3D en un solo juego | Demo |
| [Crear un crossover jugable de Hollow Knight](#case-54) | Usa recursos de un juego existente para crear una batalla jugable entre el Caballero y Kimi | Demo |
| [Crear en una ejecución un juego 3D de navegador al estilo Fall Guys](#case-60) | Usa una petición de una sola ejecución para generar un juego de obstáculos 3D jugable y expón el proyecto para su inspección | Demo |
| [Crear y autoprobar un FPS apocalíptico ambientado en Lisboa](#case-61) | Usa una ejecución de esfuerzo máximo y un solo prompt que pruebe, capture pantallas e itere antes de entregar un FPS jugable | Demo |
| [Generar un juego al estilo Animal Crossing a partir de una petición simple](#case-63) | Usa una instrucción mínima de juego para examinar la jugabilidad, el bucle de juego y los efectos de paralaje | Demo |
| [Generar un juego al estilo Mario a partir de una frase](#case-65) | Usa una petición mínima de una sola ejecución para examinar jugabilidad, diseño de niveles, pixel art y paralaje | Demo |
| [Crear un shooter de zombis en primera persona funcional](#case-67) | Usa un objetivo concreto de shooter de zombis para examinar un artefacto FPS completo y jugable | Demo |

<a id="case-1"></a>
### Case 1: [Crear un pod racer voxel con un prompt](https://x.com/ivanfioravanti/status/2077763009657627055) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Usa una idea breve para prototipar una carrera voxel y define una segunda iteración**

El creador informa que Kimi K3 produjo la primera versión con un único prompt público y planea añadir corredores, meta y revisión de detalles

**Prompt:**

```text
Voxel star wars pod-racers run
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01-poster.jpg" alt="Case 1 video poster" height="360"></a>

[Play case 1 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-2"></a>
### Case 2: [Comparar Frogger con el mismo prompt](https://x.com/ivanfioravanti/status/2077754781964054825) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Mantén constante el prompt para inspeccionar diferencias entre modelos**

El creador comparte una versión Frogger de Kimi K3 como comparación. La fuente no publica el prompt ni una rúbrica

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02-poster.jpg" alt="Case 2 video poster" height="360"></a>

[Play case 2 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-3"></a>
### Case 3: [Generar Frogger y su grabación](https://x.com/TheAhmadOsman/status/2077776567292338285) (by [@TheAhmadOsman](https://x.com/TheAhmadOsman))

**Prueba en una sola ejecución tanto el juego como el flujo de grabación**

El creador afirma que Kimi K3 produjo el juego y el flujo de grabación en una ejecución cada uno. No incluye los prompts

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03-poster.jpg" alt="Case 3 video poster" height="360"></a>

[Play case 3 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-4"></a>
### Case 4: [Prototipar un portaaviones en Three.js](https://x.com/HarshithLucky3/status/2077753222018814360) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**Usa una escena concreta para probar un prototipo 3D interactivo**

El creador muestra despegue y recuperación de aviones en un portaaviones clase Nimitz y valora positivamente la generación 3D

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04-poster.jpg" alt="Case 4 video poster" height="360"></a>

[Play case 4 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-9"></a>
### Case 9: [Crear un juego inspirado en Paper Mario con herramientas de agente](https://x.com/chongdashu/status/2077886028866531655) (by [@chongdashu](https://x.com/chongdashu))

**Combina Kimi K3 con un harness de agente y herramientas de recursos para producir elementos de juego tanto 2D como 3D**

El creador informa que usó Kimi K3 con Grok Build, Spriterrific para los recursos 2D y geometría para los recursos 3D en un juego inspirado en Paper Mario. La fuente demuestra el uso de herramientas y skills, pero no publica un prompt reutilizable exacto

Type: Demo | Date: 2026-07-16

---

<a id="case-11"></a>
### Case 11: [Generar un shooter en primera persona ambientado en el metro](https://x.com/bijanbowen/status/2077881805751873997) (by [@bijanbowen](https://x.com/bijanbowen))

**Usa un escenario concreto de metro para examinar el resultado de un shooter en primera persona generado**

El creador muestra un FPS de metro atribuido a Kimi K3 y señala explícitamente la incertidumbre sobre si su condición de influencer afectó al resultado. No se aporta un prompt ni un flujo reproducible

Type: Demo | Date: 2026-07-16

---

<a id="case-19"></a>
### Case 19: [Modelar un motor V8 con Blender MCP](https://x.com/aisearchio/status/2077962156147146925) (by [@aisearchio](https://x.com/aisearchio))

**Usa Blender MCP y una sola petición para generar un modelo mecánico 3D detallado**

El evaluador informa que Kimi K3 generó un motor V8 completo con Blender MCP a partir de un prompt. La publicación enlaza una reseña más amplia, pero no expone el prompt exacto en el registro proporcionado

Type: Integration | Date: 2026-07-17

---

<a id="case-23"></a>
### Case 23: [Crear una arena de combate jugable a partir de una referencia](https://x.com/VORTEX_Promos/status/2077879705378730074) (by [@VORTEX_Promos](https://x.com/VORTEX_Promos))

**Usa una sola referencia para probar la generación de una arena jugable completa en una ejecución**

El creador informa que Kimi K3 produjo una arena de combate jugable en una sola ejecución a partir de una referencia. La publicación incluye otra afirmación de clasificación, pero el caso de uso concreto es el artefacto de arena demostrado

Type: Demo | Date: 2026-07-16

---

<a id="case-24"></a>
### Case 24: [Crear tres juegos retro autónomos como archivos HTML](https://x.com/rohanpaul_ai/status/2077889084761206860) (by [@rohanpaul_ai](https://x.com/rohanpaul_ai))

**Exige gráficos, enemigos, reglas y juego autónomo dentro de archivos HTML independientes**

La fuente informa de una comparación de Atomic Chat en la que los modelos crearon Road Fighter, Battle City y Q*bert como archivos HTML que juegan solos. La comparación de coste y calidad procede del editor y no se reproduce de forma independiente aquí

Type: Benchmark | Date: 2026-07-16

---

<a id="case-27"></a>
### Case 27: [Crear en una ejecución un juego de escondite con camaleones](https://x.com/aimlapi/status/2077898742179459274) (by [@aimlapi](https://x.com/aimlapi))

**Genera un juego en un solo archivo con combinación de colores, zonas procedimentales, sonido y puntuación en varias rondas**

AIMLAPI informa de una comparación en una sola ejecución y con el mismo prompt para un juego de escondite, y enumera costes de 3,11 USD para Kimi K3 y 12,23 USD para Fable 5. Las funciones y los costes son resultados comunicados por el proveedor

Type: Benchmark | Date: 2026-07-16

---

<a id="case-36"></a>
### Case 36: [Crear un juego 2.5D al estilo Paper Mario con herramientas de agente](https://x.com/chongdashu/status/2077981621223837739) (by [@chongdashu](https://x.com/chongdashu))

**Usa Kimi K3 con Grok Build o Claude Code y Spriterrific para montar un flujo de trabajo de juego 2.5D**

El creador ofrece un tutorial completo con Grok Build y Kimi K3 y muestra la generación de sprites con Spriterrific. La fuente identifica las herramientas, pero no aporta prompts reutilizables exactos

Type: Tutorial | Date: 2026-07-17

---

<a id="case-43"></a>
### Case 43: [Crear un RPG wuxia 3D para navegador](https://x.com/AngryTomtweets/status/2077868163136450619) (by [@AngryTomtweets](https://x.com/AngryTomtweets))

**Combina combate cuerpo a cuerpo, misiones, inventario, clima, interiores, trabajo de entornos en Blender y recursos adaptados**

La fuente informa de un RPG de navegador con Kimi K3 que incluye combate cuerpo a cuerpo, misiones, inventario, clima dinámico e interiores explorables, además de modelado en Blender, mejoras de colisiones, retexturizado PBR y adaptación de recursos abiertos

Type: Demo | Date: 2026-07-16

---

<a id="case-44"></a>
### Case 44: [Crear un juego multijugador de navegador al estilo Minecraft](https://x.com/Alezander907/status/2077926014710407407) (by [@Alezander907](https://x.com/Alezander907))

**Usa una ejecución acotada por tiempo y coste para producir un juego multijugador online jugable en el navegador**

El creador informa que Kimi K3 creó en una hora y por 6,57 USD un juego multijugador al estilo Minecraft jugable en el navegador. Son cifras autodeclaradas de una sola ejecución y un solo artefacto

Type: Demo | Date: 2026-07-17

---

<a id="case-48"></a>
### Case 48: [Recrear un juego cooperativo de navegador con pantalla dividida](https://x.com/ridark_eth/status/2077882889803378969) (by [@ridark_eth](https://x.com/ridark_eth))

**Usa una petición para generar cooperación en pantalla dividida dentro del navegador e interacción con el entorno en tiempo real**

El creador informa que Kimi K3 produjo en un prompt un juego de navegador inspirado en It Takes Two, con Mario y Luigi interactuando en pantalla dividida y con el entorno en tiempo real

Type: Demo | Date: 2026-07-16

---

<a id="case-49"></a>
### Case 49: [Generar un juego jugable con el modo de diseño de Command Code](https://x.com/naymur_dev/status/2077873562661335207) (by [@naymur_dev](https://x.com/naymur_dev))

**Usa el comando de diseño de Command Code para crear un juego en una sola ejecución y registra si el resultado es jugable**

El creador informa de una comparación en una sola ejecución mediante el modo de diseño de Command Code y afirma que la ejecución con Kimi K3 produjo un juego jugable por 0,038 USD. Este resultado de coste y calidad es autodeclarado

Type: Demo | Date: 2026-07-16

---

<a id="case-51"></a>
### Case 51: [Montar un RPG wuxia de navegador cohesionado](https://x.com/TokenGremlin/status/2077855657068310620) (by [@TokenGremlin](https://x.com/TokenGremlin))

**Integra desplazamiento, combate, misiones, inventario, clima, exploración y trabajo de entornos 3D en un solo juego**

La fuente informa de un RPG de navegador estilo wuxia con Kimi K3 que combina combate cuerpo a cuerpo, misiones, inventario, clima dinámico, interiores explorables y una estructura de juego 3D cohesionada

Type: Demo | Date: 2026-07-16

---

<a id="case-54"></a>
### Case 54: [Crear un crossover jugable de Hollow Knight](https://x.com/wangfeng0315/status/2077933531200991583) (by [@wangfeng0315](https://x.com/wangfeng0315))

**Usa recursos de un juego existente para crear una batalla jugable entre el Caballero y Kimi**

El creador, que declara trabajar en Kimi, informa que creó con recursos de Hollow Knight un juego en el que el Caballero lucha contra Kimi y proporciona un enlace público para jugar. La atribución y la evaluación deben tener en cuenta esa afiliación

Type: Demo | Date: 2026-07-17

---

<a id="case-60"></a>
### Case 60: [Crear en una ejecución un juego 3D de navegador al estilo Fall Guys](https://x.com/aayushman2703/status/2077857886441783526) (by [@aayushman2703](https://x.com/aayushman2703))

**Usa una petición de una sola ejecución para generar un juego de obstáculos 3D jugable y expón el proyecto para su inspección**

El creador informa de una creación en una sola ejecución con Kimi K3 de un juego de navegador al estilo Fall Guys y afirma que el prompt y el proyecto de GitHub están enlazados desde la fuente. Este registro no reproduce ese prompt

Type: Demo | Date: 2026-07-16

---

<a id="case-61"></a>
### Case 61: [Crear y autoprobar un FPS apocalíptico ambientado en Lisboa](https://x.com/goncalo_canhoto/status/2077863166655037668) (by [@goncalo_canhoto](https://x.com/goncalo_canhoto))

**Usa una ejecución de esfuerzo máximo y un solo prompt que pruebe, capture pantallas e itere antes de entregar un FPS jugable**

El creador informa que Kimi K3 produjo un FPS de navegador jugable ambientado en una Lisboa apocalíptica tras aproximadamente una hora, con pruebas, capturas e iteraciones repetidas. Estos detalles de tiempo y proceso son autodeclarados

Type: Demo | Date: 2026-07-16

---

<a id="case-63"></a>
### Case 63: [Generar un juego al estilo Animal Crossing a partir de una petición simple](https://x.com/gagarot200/status/2077949230287896830) (by [@gagarot200](https://x.com/gagarot200))

**Usa una instrucción mínima de juego para examinar la jugabilidad, el bucle de juego y los efectos de paralaje**

El creador informa que Kimi K3 generó a partir de un prompt muy simple un juego al estilo Animal Crossing completamente jugable, con bucle de juego y efectos de paralaje. La redacción exacta no aparece en el registro proporcionado

Type: Demo | Date: 2026-07-17

---

<a id="case-65"></a>
### Case 65: [Generar un juego al estilo Mario a partir de una frase](https://x.com/izutorishima/status/2077939370154475992) (by [@izutorishima](https://x.com/izutorishima))

**Usa una petición mínima de una sola ejecución para examinar jugabilidad, diseño de niveles, pixel art y paralaje**

El creador informa que Kimi K3 produjo a partir de una sola instrucción un juego funcional al estilo Mario sin errores evidentes, con estructura de niveles y paralaje. El mismo informe critica la calidad de la música y los gráficos

Type: Demo | Date: 2026-07-17

---

<a id="case-67"></a>
### Case 67: [Crear un shooter de zombis en primera persona funcional](https://x.com/X2worldtech/status/2077902793449296203) (by [@X2worldtech](https://x.com/X2worldtech))

**Usa un objetivo concreto de shooter de zombis para examinar un artefacto FPS completo y jugable**

La fuente muestra un FPS de zombis completamente funcional atribuido a Kimi K3. No proporciona el prompt, detalles de implementación ni una evaluación externa de la jugabilidad

> [!WARNING]
> The original source permalink returned HTTP 404 during the 2026-07-17 audit. Attribution and evidence are preserved from the supplied high-confidence source package.

Type: Demo | Date: 2026-07-16

---


<a id="frontend-motion"></a>
## 🎨 Frontend y diseño en movimiento

| Case | What it shows | Type |
|---|---|---|
| [Crear un frontend de motion graphics interactivo](#case-5) | Construye gráficos que sigan siendo interactivos al pausar la animación | Demo |
| [Producir un anuncio animado sincronizado](#case-6) | Comprueba la sincronía entre música, efectos y movimiento | Demo |
| [Crear motion design íntegramente con código](#case-14) | Comprueba si un flujo de programación de una sola ejecución puede producir motion design sin herramientas auxiliares de generación | Demo |
| [Investigar a una persona y crear su sitio personal animado](#case-15) | Da una instrucción amplia para un sitio personal y examina la investigación, planificación, iteración y validación en el navegador del modelo | Tutorial |
| [Generar una simulación de un agujero negro](#case-17) | Usa una tarea de visualización científica para examinar una simulación generada de un agujero negro | Demo |
| [Probar modelado frontend complejo, partículas y shaders](#case-22) | Usa un prompt frontend público para examinar en una sola pasada la precisión del modelado, los efectos de partículas y la generación de shaders inline | Demo |
| [Generar una herramienta de música procedimental en un intento](#case-26) | Prueba la generación en un intento de un generador interactivo de música procedimental y compara con cautela el resultado visible | Demo |
| [Crear una página de producto en Three.js a partir de dos imágenes](#case-33) | Usa dos imágenes de referencia y un requisito explícito de Three.js para generar una presentación de producto | Demo |
| [Inventar una cortadora de pan de lujo y su página de producto](#case-39) | Combina la ideación de producto, una vista explotada, una demostración y una landing page en un solo artefacto de diseño | Demo |
| [Generar un GIF recursivo de diez segundos con un pelícano](#case-45) | Usa una instrucción completamente especificada de animación en bucle para examinar la continuidad narrativa y la recursión en un GIF | Demo |
| [Generar un SVG lateral de un BMW M4 CS](#case-55) | Usa un vehículo y un punto de vista específicos para examinar el resultado de una ilustración vectorial | Demo |
| [Recrear Gargantúa mediante feedback de capturas de pantalla](#case-58) | Usa capturas repetidas como observaciones para diagnosticar y perfeccionar una visualización científica | Tutorial |
| [Perfeccionar una visualización de agujero negro con 62 capturas](#case-66) | Usa un bucle de feedback de capturas para leer, diagnosticar y corregir una simulación visual durante muchas iteraciones | Tutorial |
| [Crear un PDF de marketing sobre post-training](#case-68) | Usa un producto y un formato de entrega concretos para generar un documento de marketing | Demo |
| [Crear una interfaz de usuario a partir de un prompt](#case-70) | Usa una sola petición para generar y examinar un diseño completo de interfaz de usuario | Demo |

<a id="case-5"></a>
### Case 5: [Crear un frontend de motion graphics interactivo](https://x.com/chetaslua/status/2077749371144442022) (by [@chetaslua](https://x.com/chetaslua))

**Construye gráficos que sigan siendo interactivos al pausar la animación**

El creador informa de una construcción de 42 minutos, en una ejecución, con código simple y sin harness, MCP ni skills

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05-poster.jpg" alt="Case 5 video poster" height="360"></a>

[Play case 5 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-6"></a>
### Case 6: [Producir un anuncio animado sincronizado](https://x.com/abhinavflac/status/2077760297918484667) (by [@abhinavflac](https://x.com/abhinavflac))

**Comprueba la sincronía entre música, efectos y movimiento**

El creador dice que un prompt produjo en una ejecución un anuncio de estilo Spotify. El prompt exacto no está publicado

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06-poster.jpg" alt="Case 6 video poster" height="360"></a>

[Play case 6 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-14"></a>
### Case 14: [Crear motion design íntegramente con código](https://x.com/chetaslua/status/2077952938564354503) (by [@chetaslua](https://x.com/chetaslua))

**Comprueba si un flujo de programación de una sola ejecución puede producir motion design sin herramientas auxiliares de generación**

El creador informa de un resultado de motion design con Kimi K3 en una sola ejecución, realizado por completo con código y sin MCP, skills, herramientas, generación de vídeo ni prompts especiales. No se proporciona el prompt exacto

Type: Demo | Date: 2026-07-17

---

<a id="case-15"></a>
### Case 15: [Investigar a una persona y crear su sitio personal animado](https://x.com/nicky_sap/status/2077857190707429411) (by [@nicky_sap](https://x.com/nicky_sap))

**Da una instrucción amplia para un sitio personal y examina la investigación, planificación, iteración y validación en el navegador del modelo**

El creador informa que Kimi K3 investigó a Nick Saponaro y produjo un sitio web personal animado a partir de una petición amplia, con planificación, pruebas, iteración y comprobaciones en el navegador. El resultado es una demostración de flujo autodeclarada

Type: Tutorial | Date: 2026-07-16

---

<a id="case-17"></a>
### Case 17: [Generar una simulación de un agujero negro](https://x.com/chetaslua/status/2077961850352971796) (by [@chetaslua](https://x.com/chetaslua))

**Usa una tarea de visualización científica para examinar una simulación generada de un agujero negro**

El creador muestra una simulación de agujero negro atribuida a Kimi K3 y la califica como la mejor que ha visto. La fuente aporta un resultado visible, pero no un prompt, una rúbrica ni validación independiente

Type: Demo | Date: 2026-07-17

---

<a id="case-22"></a>
### Case 22: [Probar modelado frontend complejo, partículas y shaders](https://x.com/karminski3/status/2077889959223337099) (by [@karminski3](https://x.com/karminski3))

**Usa un prompt frontend público para examinar en una sola pasada la precisión del modelado, los efectos de partículas y la generación de shaders inline**

El creador informa de un resultado frontend de Kimi K3 en una sola pasada que cubre modelado preciso, efectos de partículas y código shader inline complejo, y afirma que el prompt de prueba es público en la fuente enlazada

Type: Demo | Date: 2026-07-16

---

<a id="case-26"></a>
### Case 26: [Generar una herramienta de música procedimental en un intento](https://x.com/mirochill/status/2077723551331758478) (by [@mirochill](https://x.com/mirochill))

**Prueba la generación en un intento de un generador interactivo de música procedimental y compara con cautela el resultado visible**

El creador informa que Kimi K3 generó una herramienta de música procedimental en un intento y la compara favorablemente con resultados de Fable 5 y GPT-5.6 Sol. Se trata del conjunto de pruebas del propio creador, no de un benchmark estandarizado

Type: Demo | Date: 2026-07-16

---

<a id="case-33"></a>
### Case 33: [Crear una página de producto en Three.js a partir de dos imágenes](https://x.com/1littlecoder/status/2077890296806031665) (by [@1littlecoder](https://x.com/1littlecoder))

**Usa dos imágenes de referencia y un requisito explícito de Three.js para generar una presentación de producto**

El creador informa que Kimi K3 diseñó una página de producto a partir de dos imágenes y produjo la versión solicitada explícitamente en Three.js. No se facilitan más detalles del prompt ni de la implementación

Type: Demo | Date: 2026-07-16

---

<a id="case-39"></a>
### Case 39: [Inventar una cortadora de pan de lujo y su página de producto](https://x.com/filicroval/status/2077871090731221438) (by [@filicroval](https://x.com/filicroval))

**Combina la ideación de producto, una vista explotada, una demostración y una landing page en un solo artefacto de diseño**

El creador informa que Kimi K3 inventó una cortadora de pan estilo guillotina, la presentó como producto de lujo y produjo una landing page con vista explotada y demostración

Type: Demo | Date: 2026-07-16

---

<a id="case-45"></a>
### Case 45: [Generar un GIF recursivo de diez segundos con un pelícano](https://x.com/1littlecoder/status/2077880380900937865) (by [@1littlecoder](https://x.com/1littlecoder))

**Usa una instrucción completamente especificada de animación en bucle para examinar la continuidad narrativa y la recursión en un GIF**

La fuente incluye un prompt para un GIF en bucle de diez segundos en el que un pelícano monta en bicicleta y recibe por mensaje el mismo vídeo mientras la cámara se acerca. El creador muestra la animación resultante de Kimi K3

Type: Demo | Date: 2026-07-16

---

<a id="case-55"></a>
### Case 55: [Generar un SVG lateral de un BMW M4 CS](https://x.com/HarshithLucky3/status/2077765821380886942) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**Usa un vehículo y un punto de vista específicos para examinar el resultado de una ilustración vectorial**

El creador muestra un SVG lateral de un BMW M4 CS atribuido a Kimi K3 Max. La fuente proporcionada contiene el artefacto, pero no el prompt ni los pasos de producción

Type: Demo | Date: 2026-07-16

---

<a id="case-58"></a>
### Case 58: [Recrear Gargantúa mediante feedback de capturas de pantalla](https://x.com/AngryTomtweets/status/2077868981659324444) (by [@AngryTomtweets](https://x.com/AngryTomtweets))

**Usa capturas repetidas como observaciones para diagnosticar y perfeccionar una visualización científica**

La fuente informa que Kimi K3 recreó Gargantúa de Interstellar mediante 62 capturas de pantalla propias, leyendo cada resultado, diagnosticando problemas y actuando sobre ellos de forma iterativa

Type: Tutorial | Date: 2026-07-16

---

<a id="case-66"></a>
### Case 66: [Perfeccionar una visualización de agujero negro con 62 capturas](https://x.com/TokenGremlin/status/2077855959201042645) (by [@TokenGremlin](https://x.com/TokenGremlin))

**Usa un bucle de feedback de capturas para leer, diagnosticar y corregir una simulación visual durante muchas iteraciones**

La fuente informa que Kimi K3 reconstruyó Gargantúa de Interstellar observando y perfeccionando su resultado a lo largo de 62 capturas. Esto demuestra el bucle de feedback comunicado, no una verificación independiente de la precisión física

Type: Tutorial | Date: 2026-07-16

---

<a id="case-68"></a>
### Case 68: [Crear un PDF de marketing sobre post-training](https://x.com/Satvik_Pen/status/2077859673517023313) (by [@Satvik_Pen](https://x.com/Satvik_Pen))

**Usa un producto y un formato de entrega concretos para generar un documento de marketing**

El creador informa que pidió a Kimi K3 un PDF de marketing sobre Inkling, el producto de post-training de Thinking Machines, y comparte el resultado, además de elogiar el proceso interno. No se facilitan el prompt ni criterios de evaluación

Type: Demo | Date: 2026-07-16

---

<a id="case-70"></a>
### Case 70: [Crear una interfaz de usuario a partir de un prompt](https://x.com/BrianMRey/status/2077891942088671689) (by [@BrianMRey](https://x.com/BrianMRey))

**Usa una sola petición para generar y examinar un diseño completo de interfaz de usuario**

El creador muestra un diseño de interfaz atribuido a una ejecución de Kimi K3 con un prompt y ofrece una valoración subjetiva muy positiva. No se incluyen el prompt exacto ni una rúbrica

Type: Demo | Date: 2026-07-16

---


<a id="coding-integrations"></a>
## 💻 Programación e integraciones

| Case | What it shows | Type |
|---|---|---|
| [Crear un MacBook virtual con macOS funcional](#case-18) | Combina el renderizado de hardware con Three.js y una simulación interactiva de un sistema operativo en el navegador | Demo |
| [Crear un compilador GPU desde un DSL hasta PTX](#case-25) | Usa una tarea de compilador de extremo a extremo que abarque un DSL, las pasadas del compilador, la generación de PTX y una ruta para Tensor Cores | Demo |
| [Crear un raytracer de agujero negro en tiempo real con WebGL2](#case-32) | Prueba la generación con un prompt de un raytracer geodésico nativo de WebGL2 dentro de un solo archivo HTML | Benchmark |
| [Crear un emulador de Game Boy Advance basado en mGBA WASM](#case-46) | Integra un modelo 3D con licencia y un núcleo de emulación real, y mejora recursivamente la interfaz y la experiencia de juego | Integration |
| [Investigar varios temas con fuentes en chino](#case-50) | Usa tareas de investigación prolongadas para comparar exhaustividad y latencia entre generaciones de modelos | Evaluation |
| [Clonar macOS en el navegador con aplicaciones funcionales](#case-56) | Crea una simulación de sistema operativo en el navegador que incluya aplicaciones de música, navegador y correo electrónico | Demo |
| [Crear una simulación de macOS con FaceTime funcional](#case-62) | Usa una tarea de sistema operativo virtual para comprobar si funciona la interacción de una aplicación generada | Demo |
| [Añadir un comparador frontend de dos tareas](#case-64) | Crea una herramienta que seleccione dos tareas completadas, las muestre lado a lado y sincronice vistas e interacciones | Tutorial |

<a id="case-18"></a>
### Case 18: [Crear un MacBook virtual con macOS funcional](https://x.com/scottstts/status/2077890054299541890) (by [@scottstts](https://x.com/scottstts))

**Combina el renderizado de hardware con Three.js y una simulación interactiva de un sistema operativo en el navegador**

La fuente informa que Kimi K3 creó un MacBook virtual en Three.js con un entorno funcional al estilo de macOS. Demuestra el artefacto, pero no aporta los pasos de implementación

Type: Demo | Date: 2026-07-16

---

<a id="case-25"></a>
### Case 25: [Crear un compilador GPU desde un DSL hasta PTX](https://x.com/rohanpaul_ai/status/2077886618657231220) (by [@rohanpaul_ai](https://x.com/rohanpaul_ai))

**Usa una tarea de compilador de extremo a extremo que abarque un DSL, las pasadas del compilador, la generación de PTX y una ruta para Tensor Cores**

La fuente informa que Kimi K3 creó desde cero un compilador GPU, desde su DSL y sus pasadas hasta la generación de PTX, y compara su ruta de Tensor Cores con Triton. El registro proporcionado no incluye detalles de un benchmark independiente

Type: Demo | Date: 2026-07-16

---

<a id="case-32"></a>
### Case 32: [Crear un raytracer de agujero negro en tiempo real con WebGL2](https://x.com/AlicanKiraz0/status/2077885419744612597) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**Prueba la generación con un prompt de un raytracer geodésico nativo de WebGL2 dentro de un solo archivo HTML**

El autor describe un benchmark de programación que exige un raytracer funcional de desviación de luz por un agujero negro, en un solo archivo y con WebGL2 nativo. El registro proporcionado establece la tarea y los modelos participantes, pero no una auditoría independiente completa del resultado

Type: Benchmark | Date: 2026-07-16

---

<a id="case-46"></a>
### Case 46: [Crear un emulador de Game Boy Advance basado en mGBA WASM](https://x.com/teortaxesTex/status/2077925090168062272) (by [@teortaxesTex](https://x.com/teortaxesTex))

**Integra un modelo 3D con licencia y un núcleo de emulación real, y mejora recursivamente la interfaz y la experiencia de juego**

El proyecto citado de Kimi K3 adapta un modelo AGB-001 con licencia, integra un núcleo mGBA WASM y mejora la interfaz y el juego mediante autooptimización recursiva. La publicación cita la descripción del proyecto, no una reproducción independiente

Type: Integration | Date: 2026-07-17

---

<a id="case-50"></a>
### Case 50: [Investigar varios temas con fuentes en chino](https://x.com/tphuang/status/2077911994607239400) (by [@tphuang](https://x.com/tphuang))

**Usa tareas de investigación prolongadas para comparar exhaustividad y latencia entre generaciones de modelos**

El autor informa que probó Kimi K3 en numerosos temas de investigación con fuentes en chino, y lo encontró más exhaustivo que K2.6, aunque más lento. La publicación también señala una fuerte demanda del servicio en ese momento

Type: Evaluation | Date: 2026-07-17

---

<a id="case-56"></a>
### Case 56: [Clonar macOS en el navegador con aplicaciones funcionales](https://x.com/twid/status/2077924755357974989) (by [@twid](https://x.com/twid))

**Crea una simulación de sistema operativo en el navegador que incluya aplicaciones de música, navegador y correo electrónico**

La fuente informa que se usó Kimi K3 para crear un clon de macOS en el navegador con música, navegador, correo electrónico y otras funciones. No proporciona detalles de implementación

Type: Demo | Date: 2026-07-17

---

<a id="case-62"></a>
### Case 62: [Crear una simulación de macOS con FaceTime funcional](https://x.com/LinearUncle/status/2077919552239997078) (by [@LinearUncle](https://x.com/LinearUncle))

**Usa una tarea de sistema operativo virtual para comprobar si funciona la interacción de una aplicación generada**

El creador muestra un entorno al estilo de macOS atribuido a Kimi K3 e informa que su función FaceTime funciona. La fuente no proporciona pasos de configuración ni validación

Type: Demo | Date: 2026-07-17

---

<a id="case-64"></a>
### Case 64: [Añadir un comparador frontend de dos tareas](https://x.com/MinLiBuilds/status/2077939461510615376) (by [@MinLiBuilds](https://x.com/MinLiBuilds))

**Crea una herramienta que seleccione dos tareas completadas, las muestre lado a lado y sincronice vistas e interacciones**

El creador informa que pidió a Kimi K3 añadir un flujo de comparación frontend con selección de tareas, dos paneles de navegador, modos de objetos y recorrido, puntos de vista sincronizados y pruebas de interacción. La publicación también señala limitaciones más amplias del modelo

Type: Tutorial | Date: 2026-07-17

---


<a id="evaluation-limits"></a>
## 🧪 Evaluación y límites

| Case | What it shows | Type |
|---|---|---|
| [Comparar el diseño frontend en la tarea de lámpara de lava de BridgeBench](#case-7) | Usa la tarea de lámpara de lava de BridgeBench como una comparación acotada de diseño frontend, no como una clasificación universal | Benchmark |
| [Evaluar la escritura de guiones con voz editorial](#case-8) | Mide el ajuste a la voz editorial, la posición relativa y el coste por guion dentro de un benchmark interno claramente identificado | Benchmark |
| [Comparar diseño, coste y dificultad en un juego tipo Flappy](#case-10) | Registra los ajustes de dificultad, el coste, el diseño y las funciones de juego al comparar juegos generados | Benchmark |
| [Comparar el diseño de juegos con el mismo prompt](#case-12) | Mantén constante el prompt de diseño y examina por separado el ritmo, el criterio de diseño y las sensaciones de juego | Benchmark |
| [Exigir una revisión independiente en auditorías estadísticas](#case-13) | Complementa las auditorías estadísticas generadas por el modelo con una revisión independiente de expertos u otros modelos antes de confiar en sus hallazgos | Limit |
| [Evaluar una ejecución frontend lenta pero sólida](#case-16) | Registra el tiempo de finalización junto con la calidad del resultado al probar una tarea frontend | Evaluation |
| [Probar la escritura de misterio para detectar fallos de presagio](#case-20) | Evalúa si un misterio generado equilibra las pistas, la sutileza y el presagio narrativo | Limit |
| [Comparar el modelado y la animación del Halcón Milenario](#case-21) | Usa peticiones de estilo y ajustes de esfuerzo equivalentes para comparar modelado 3D, animación, tiempo y coste | Benchmark |
| [Revisar una colección de diez proyectos de Kimi K3](#case-28) | Usa una recopilación enlazada de proyectos para descubrir artefactos concretos que deban verificarse por separado | Evaluation |
| [Comparar una landing page avanzada entre cuatro modelos](#case-29) | Mantén constante la petición de la landing page y examina la profundidad de las animaciones y el grado de finalización de los resultados | Evaluation |
| [Evaluar mecánicas y costes de juegos retro](#case-30) | Compara jugabilidad, físicas, mecánicas, comportamiento autónomo, uso de tokens y coste en las mismas tareas de juegos retro | Benchmark |
| [Comparar la generación de juegos con Fable 5](#case-31) | Usa un ejemplo de juegos generados lado a lado como evaluación acotada, no como veredicto general sobre los modelos | Evaluation |
| [Comparar tareas complejas de frontend y desarrollo con Opus 4.8](#case-34) | Usa varias tareas complejas de programación para identificar victorias y derrotas en lugar de declarar que un modelo es universalmente superior | Evaluation |
| [Revisar benchmarks y una prueba de landing page](#case-35) | Combina el contexto de benchmarks con una prueba concreta de generación de landing pages, manteniendo separados ambos tipos de evidencia | Evaluation |
| [Evaluar el razonamiento inductivo con tareas de grafos a fórmulas](#case-37) | Mide la corrección, el comportamiento en holdout y la complejidad de las fórmulas en tareas de inducción de primer orden | Benchmark |
| [Revisar informes sobre juegos, landing pages, trabajo 3D y contexto largo](#case-38) | Usa una recopilación de múltiples fuentes para comparar artefactos concretos y señalar las limitaciones de velocidad junto con las afirmaciones de coste | Evaluation |
| [Auditar un plan complejo y cuestionar sus soluciones](#case-40) | Usa un segundo modelo para identificar hallazgos minimizados, soluciones incorrectas y conclusiones que deberían rechazarse | Evaluation |
| [Comparar diagramas ASCII de aprendizaje por refuerzo al estilo PPO](#case-41) | Mantén constante el prompt del diagrama ASCII y compara cómo representan los modelos el ciclo de aprendizaje por refuerzo | Evaluation |
| [Modelar en Blender mientras se registran errores de capacidad](#case-42) | Evalúa el progreso parcial en Blender junto con la fiabilidad del servicio, no solo el artefacto | Limit |
| [Comparar la generación de Flappy Bird en una arena](#case-47) | Usa una tarea de arena para comparar dos resultados generados de Flappy Bird, manteniendo el juicio limitado a esa tarea | Evaluation |
| [Resolver con una herramienta un problema de inducción visual de Bongard](#case-52) | Comprueba si el uso de herramientas ayuda a deducir la regla visual en una tarea de razonamiento de Bongard | Evaluation |
| [Comparar el gusto frontend y el diseño 3D con GPT-5.6 Sol](#case-53) | Examina funciones, gusto visual, elegancia y ejecución 3D en una comparación frontend acotada | Evaluation |
| [Comparar la generación de sitios web entre tres modelos](#case-57) | Usa resultados visibles de sitios web para comparar Kimi K3, Fable 5 y GPT-5.6 Sol en una prueba | Evaluation |
| [Comparar la generación y el coste de juegos 3D procedimentales](#case-59) | Mantén constante el prompt entre modelos y examina sistemas generados de ruleta, tragaperras y pinball junto con el coste por ejecución | Benchmark |
| [Comparar el detalle y la iluminación de una escena 3D de arsenal](#case-69) | Examina la densidad de objetos, la iluminación y el detalle de la escena en una comparación acotada entre Kimi K3 y Opus 4.8 | Evaluation |

<a id="case-7"></a>
### Case 7: [Comparar el diseño frontend en la tarea de lámpara de lava de BridgeBench](https://x.com/bridgemindai/status/2077868061953007908) (by [@bridgemindai](https://x.com/bridgemindai))

**Usa la tarea de lámpara de lava de BridgeBench como una comparación acotada de diseño frontend, no como una clasificación universal**

BridgeMind AI informa que Kimi K3 superó a Fable 5 en su tarea de lámpara de lava de BridgeBench y quedó primero en la arena citada. Estos son los resultados comparativos comunicados por el editor

Type: Benchmark | Date: 2026-07-16

---

<a id="case-8"></a>
### Case 8: [Evaluar la escritura de guiones con voz editorial](https://x.com/Whats_AI/status/2077860441380798908) (by [@Whats_AI](https://x.com/Whats_AI))

**Mide el ajuste a la voz editorial, la posición relativa y el coste por guion dentro de un benchmark interno claramente identificado**

Whats_AI comunica resultados internos preliminares de 2.840 Elo, primer puesto en su tabla y unos 0,25 USD por guion. Deben tratarse como el benchmark preliminar de una organización, no como garantía general de rendimiento o precio

Type: Benchmark | Date: 2026-07-16

---

<a id="case-10"></a>
### Case 10: [Comparar diseño, coste y dificultad en un juego tipo Flappy](https://x.com/MrAhmadAwais/status/2077915347974557862) (by [@MrAhmadAwais](https://x.com/MrAhmadAwais))

**Registra los ajustes de dificultad, el coste, el diseño y las funciones de juego al comparar juegos generados**

El benchmark interno de Flappy de Command Code informa de distintos ajustes de dificultad entre modelos y asigna 0,024 USD a Kimi K3, 0,42 USD a Fable 5 y 0,15 USD a GPT-5.6 Sol. La desigualdad de ajustes limita el alcance de esta comparación interna

Type: Benchmark | Date: 2026-07-17

---

<a id="case-12"></a>
### Case 12: [Comparar el diseño de juegos con el mismo prompt](https://x.com/CommandCodeAI/status/2077921526213746948) (by [@CommandCodeAI](https://x.com/CommandCodeAI))

**Mantén constante el prompt de diseño y examina por separado el ritmo, el criterio de diseño y las sensaciones de juego**

Command Code informa de una comparación con el mismo prompt entre Kimi K3, GPT-5.6 Sol y Fable 5. Su publicación afirma que Kimi K3 rindió bien en criterio de diseño mientras que los otros dos jugaban demasiado rápido; sigue siendo la evaluación del editor

Type: Benchmark | Date: 2026-07-17

---

<a id="case-13"></a>
### Case 13: [Exigir una revisión independiente en auditorías estadísticas](https://x.com/emollick/status/2077869293031624793) (by [@emollick](https://x.com/emollick))

**Complementa las auditorías estadísticas generadas por el modelo con una revisión independiente de expertos u otros modelos antes de confiar en sus hallazgos**

Ethan Mollick informa que Kimi K3 Max aplicó incorrectamente la estadística al auditar trabajos académicos previos y coincide con una crítica separada. Este ejemplo negativo respalda la comprobación independiente en lugar de la aceptación sin revisión

Type: Limit | Date: 2026-07-16

---

<a id="case-16"></a>
### Case 16: [Evaluar una ejecución frontend lenta pero sólida](https://x.com/Lentils80/status/2077387333154857151) (by [@Lentils80](https://x.com/Lentils80))

**Registra el tiempo de finalización junto con la calidad del resultado al probar una tarea frontend**

El creador informa que una ejecución frontend de Kimi K3 tardó 35 minutos y describe el resultado como uno de los mejores que ha visto para ese prompt. Tanto la velocidad como la calidad son observaciones de un solo usuario

Type: Evaluation | Date: 2026-07-15

---

<a id="case-20"></a>
### Case 20: [Probar la escritura de misterio para detectar fallos de presagio](https://x.com/emollick/status/2077951790868238616) (by [@emollick](https://x.com/emollick))

**Evalúa si un misterio generado equilibra las pistas, la sutileza y el presagio narrativo**

Ethan Mollick informa que Kimi K3 no escribió un buen misterio de asesinato, pues hizo las pistas a la vez demasiado obvias y demasiado oscuras y falló en el presagio. También señala que otros modelos comparten esta limitación

Type: Limit | Date: 2026-07-17

---

<a id="case-21"></a>
### Case 21: [Comparar el modelado y la animación del Halcón Milenario](https://x.com/gmi_cloud/status/2077903360263676090) (by [@gmi_cloud](https://x.com/gmi_cloud))

**Usa peticiones de estilo y ajustes de esfuerzo equivalentes para comparar modelado 3D, animación, tiempo y coste**

GMI Cloud informa de una comparación entre Kimi K3 y Fable 5 al recrear el Halcón Milenario en estilo pixelado y original con esfuerzo máximo. Afirma que Kimi K3 tardó más, pero costó alrededor de un tercio en la primera prueba y menos de la mitad en otra; son resultados comunicados por el proveedor

Type: Benchmark | Date: 2026-07-16

---

<a id="case-28"></a>
### Case 28: [Revisar una colección de diez proyectos de Kimi K3](https://x.com/minchoi/status/2077957907857994006) (by [@minchoi](https://x.com/minchoi))

**Usa una recopilación enlazada de proyectos para descubrir artefactos concretos que deban verificarse por separado**

El autor selecciona diez ejemplos de Kimi K3 con material multimedia, incluido un emulador de Game Boy Advance. Este registro es una colección y no un único flujo reproducible, por lo que cada ejemplo enlazado debe comprobarse de forma independiente

Type: Evaluation | Date: 2026-07-17

---

<a id="case-29"></a>
### Case 29: [Comparar una landing page avanzada entre cuatro modelos](https://x.com/doutorcaleb/status/2077904020471947773) (by [@doutorcaleb](https://x.com/doutorcaleb))

**Mantén constante la petición de la landing page y examina la profundidad de las animaciones y el grado de finalización de los resultados**

El creador informa que dio el mismo prompt de landing page avanzada a Kimi K3, Fable, Grok y GPT Terra, y considera que Kimi K3 produjo el resultado más sólido. Es una comparación autodeclarada de una sola tarea

Type: Evaluation | Date: 2026-07-16

---

<a id="case-30"></a>
### Case 30: [Evaluar mecánicas y costes de juegos retro](https://x.com/adxtyahq/status/2077860500462055570) (by [@adxtyahq](https://x.com/adxtyahq))

**Compara jugabilidad, físicas, mecánicas, comportamiento autónomo, uso de tokens y coste en las mismas tareas de juegos retro**

La fuente informa de pruebas con el mismo prompt para Road Fighter, Battle City y Q*bert y enumera 0,28 USD para Kimi K3, 0,28 USD para GPT-5.6 y 0,54 USD para Opus 4.8. Estas cifras pertenecen al benchmark del editor

Type: Benchmark | Date: 2026-07-16

---

<a id="case-31"></a>
### Case 31: [Comparar la generación de juegos con Fable 5](https://x.com/higgsfield_ai/status/2077943629633712490) (by [@higgsfield_ai](https://x.com/higgsfield_ai))

**Usa un ejemplo de juegos generados lado a lado como evaluación acotada, no como veredicto general sobre los modelos**

Higgsfield presenta una comparación de generación de juegos entre Kimi K3 y Fable 5. El registro proporcionado incluye el material comparativo, pero no el prompt, una rúbrica de puntuación ni las condiciones detalladas

Type: Evaluation | Date: 2026-07-17

---

<a id="case-34"></a>
### Case 34: [Comparar tareas complejas de frontend y desarrollo con Opus 4.8](https://x.com/op7418/status/2077969583018066116) (by [@op7418](https://x.com/op7418))

**Usa varias tareas complejas de programación para identificar victorias y derrotas en lugar de declarar que un modelo es universalmente superior**

El evaluador informa de pruebas directas entre Kimi K3 y Opus 4.8 y considera que son aproximadamente comparables en tareas complejas de frontend y desarrollo, con resultados mixtos. Sigue siendo la valoración de un solo evaluador

Type: Evaluation | Date: 2026-07-17

---

<a id="case-35"></a>
### Case 35: [Revisar benchmarks y una prueba de landing page](https://x.com/adamuchigabriel/status/2077880433925120471) (by [@adamuchigabriel](https://x.com/adamuchigabriel))

**Combina el contexto de benchmarks con una prueba concreta de generación de landing pages, manteniendo separados ambos tipos de evidencia**

El vídeo presenta una discusión de benchmarks, una prueba de landing page y observaciones sobre diseño frontend con Kimi K3. El registro proporcionado no incluye el prompt de prueba completo ni una rúbrica de puntuación

Type: Evaluation | Date: 2026-07-16

---

<a id="case-37"></a>
### Case 37: [Evaluar el razonamiento inductivo con tareas de grafos a fórmulas](https://x.com/s_batzoglou/status/2077884096307454119) (by [@s_batzoglou](https://x.com/s_batzoglou))

**Mide la corrección, el comportamiento en holdout y la complejidad de las fórmulas en tareas de inducción de primer orden**

El autor informa de un benchmark de Kimi K3 y otros modelos en la tarea INDUCTION de ICML, usando entre 6 y 10 grafos pequeños de entre 8 y 10 elementos cada uno para inferir una fórmula de primer orden. La publicación afirma que los resultados se actualizaron respecto a trabajos anteriores; aquí no se alega una nueva reproducción independiente

Type: Benchmark | Date: 2026-07-16

---

<a id="case-38"></a>
### Case 38: [Revisar informes sobre juegos, landing pages, trabajo 3D y contexto largo](https://x.com/servasyy_ai/status/2077903775113834689) (by [@servasyy_ai](https://x.com/servasyy_ai))

**Usa una recopilación de múltiples fuentes para comparar artefactos concretos y señalar las limitaciones de velocidad junto con las afirmaciones de coste**

El autor resume pruebas comunicadas de Kimi K3 en juegos, landing pages, generación 3D y trabajo con contexto largo, y concluye que merece la pena probarlo, pero todavía no sustituye a Fable 5. Todas las cifras son informes secundarios dentro de esta recopilación

Type: Evaluation | Date: 2026-07-16

---

<a id="case-40"></a>
### Case 40: [Auditar un plan complejo y cuestionar sus soluciones](https://x.com/doodlestein/status/2077901883637665958) (by [@doodlestein](https://x.com/doodlestein))

**Usa un segundo modelo para identificar hallazgos minimizados, soluciones incorrectas y conclusiones que deberían rechazarse**

El creador informa que Kimi K3 revisó un plan muy refinado y detectó que se habían minimizado problemas graves, que cerca de un tercio de las soluciones propuestas requería corrección y que un hallazgo fue refutado. Son resultados de esa auditoría concreta

Type: Evaluation | Date: 2026-07-16

---

<a id="case-41"></a>
### Case 41: [Comparar diagramas ASCII de aprendizaje por refuerzo al estilo PPO](https://x.com/dejavucoder/status/2077872015856615541) (by [@dejavucoder](https://x.com/dejavucoder))

**Mantén constante el prompt del diagrama ASCII y compara cómo representan los modelos el ciclo de aprendizaje por refuerzo**

La fuente proporciona el prompt para dibujar en ASCII un ciclo de aprendizaje por refuerzo al estilo PPO y muestra Kimi K3 Max junto a Fable 5 High. La valoración sigue siendo una comparación visual de una sola tarea

Type: Evaluation | Date: 2026-07-16

---

<a id="case-42"></a>
### Case 42: [Modelar en Blender mientras se registran errores de capacidad](https://x.com/Angaisb_/status/2077910845523214668) (by [@Angaisb_](https://x.com/Angaisb_))

**Evalúa el progreso parcial en Blender junto con la fiabilidad del servicio, no solo el artefacto**

El creador muestra avances de modelado en Blender con Kimi K3 y también informa de errores de capacidad repetidos. El trabajo está incompleto en la fuente proporcionada, por lo que deben considerarse conjuntamente el resultado parcial y la limitación de fiabilidad

Type: Limit | Date: 2026-07-17

---

<a id="case-47"></a>
### Case 47: [Comparar la generación de Flappy Bird en una arena](https://x.com/jun_song/status/2077396996865003739) (by [@jun_song](https://x.com/jun_song))

**Usa una tarea de arena para comparar dos resultados generados de Flappy Bird, manteniendo el juicio limitado a esa tarea**

El creador informa de una comparación en Arena entre Kimi K3 y Opus 4.8 con una tarea de Flappy Bird y considera que Kimi K3 fue significativamente mejor. El registro no aporta el prompt completo ni una rúbrica

Type: Evaluation | Date: 2026-07-15

---

<a id="case-52"></a>
### Case 52: [Resolver con una herramienta un problema de inducción visual de Bongard](https://x.com/IntuitMachine/status/2077885406528311561) (by [@IntuitMachine](https://x.com/IntuitMachine))

**Comprueba si el uso de herramientas ayuda a deducir la regla visual en una tarea de razonamiento de Bongard**

El creador informa que Kimi K3 usó una herramienta para resolver un problema de Bongard que Grok 4.5 y Muse Spark 1.1 no resolvieron en la misma comparación. Es el resultado de la tarea de un usuario, no un benchmark general de razonamiento

Type: Evaluation | Date: 2026-07-16

---

<a id="case-53"></a>
### Case 53: [Comparar el gusto frontend y el diseño 3D con GPT-5.6 Sol](https://x.com/filicroval/status/2077736407506751952) (by [@filicroval](https://x.com/filicroval))

**Examina funciones, gusto visual, elegancia y ejecución 3D en una comparación frontend acotada**

El creador compara Kimi K3 y GPT-5.6 Sol en diseño frontend y considera a Kimi K3 más sólido en gusto visual, elegancia y capacidad 3D. La valoración es subjetiva y específica de la tarea

Type: Evaluation | Date: 2026-07-16

---

<a id="case-57"></a>
### Case 57: [Comparar la generación de sitios web entre tres modelos](https://x.com/pengchujin/status/2077962916226298340) (by [@pengchujin](https://x.com/pengchujin))

**Usa resultados visibles de sitios web para comparar Kimi K3, Fable 5 y GPT-5.6 Sol en una prueba**

El creador presenta una comparación de generación de sitios web entre Kimi K3, Fable 5 y GPT-5.6 Sol. El registro proporcionado no expone el prompt completo ni una rúbrica de puntuación

Type: Evaluation | Date: 2026-07-17

---

<a id="case-59"></a>
### Case 59: [Comparar la generación y el coste de juegos 3D procedimentales](https://x.com/adxtyahq/status/2077958193511362856) (by [@adxtyahq](https://x.com/adxtyahq))

**Mantén constante el prompt entre modelos y examina sistemas generados de ruleta, tragaperras y pinball junto con el coste por ejecución**

El editor informa de una comparación multimodelo de juegos 3D procedimentales y enumera costes que incluyen 0,71 USD para Kimi K3 y 0,30 USD para Grok 4.5. Todas las clasificaciones y costes deben tratarse como resultados de la ejecución de ese editor

Type: Benchmark | Date: 2026-07-17

---

<a id="case-69"></a>
### Case 69: [Comparar el detalle y la iluminación de una escena 3D de arsenal](https://x.com/hakki_alkan/status/2077887013332636032) (by [@hakki_alkan](https://x.com/hakki_alkan))

**Examina la densidad de objetos, la iluminación y el detalle de la escena en una comparación acotada entre Kimi K3 y Opus 4.8**

La fuente informa que Kimi K3 produjo una escena de arsenal detallada con estantes abastecidos, cajas e iluminación realista, mientras que Opus 4.8 produjo una habitación vacía. Es un informe comparativo de terceros, no un benchmark independiente

Type: Evaluation | Date: 2026-07-16

---

## Recursos relacionados

- [Ver detalles y precios de Kimi K3 en EvoLink](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_model)
- [Abrir la documentación API de Kimi K3 en EvoLink](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_api_docs)
- [Más información sobre Kimi K3 en EvoLink](https://evolink.ai/blog/is-kimi-k3-available-on-evolink?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_article)
- La página del modelo y la documentación API de EvoLink están verificadas; no se verificó una skill instalable de Kimi K3

<a id="acknowledge"></a>
## 🙏 Agradecimientos

Este repositorio existe gracias a quienes compartieron públicamente su trabajo con Kimi K3

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

*Si la atribución o el texto necesitan una corrección, abre una issue con una fuente pública*
