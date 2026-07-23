<div align="center">

<a href="https://evolink.ai/kimi-k3?utm_source=github&utm_medium=banner&utm_campaign=awesome-kimi-k3-usecases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/images/es-v2.png" alt="Banner localizado de Kimi K3 con paisaje lunar y llamada a la acción de EvoLink" width="760"></a>

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

# Casos de uso increíbles de Kimi K3

## 🍌 Introducción

Bienvenido al repositorio de casos de uso de alta señal de Kimi K3

**Recopilamos juegos, escenas 3D, diseños en movimiento, integraciones, evaluaciones y límites prácticos de Kimi K3 respaldados por fuentes públicas**

Los 129 casos proceden de fuentes públicas de alta confianza. Los títulos y autores enlazan a los originales; se excluyen candidatos débiles, duplicados o insuficientemente documentados

## 📊 Resumen

- 129 casos de alta confianza de creadores y profesionales
- Incluye juegos interactivos, 3D, frontend, motion graphics, programación, integraciones, investigación, evaluaciones y límites prácticos
- Cada caso conserva fuente, autor, tipo, fecha y límite del prompt
- Las experiencias individuales no se presentan como benchmarks

> [!NOTE]
> La colección prioriza evidencia concreta. No reconstruye prompts ausentes ni inventa pasos de configuración

<a id="quick-api-access"></a>
## ⚡ Inicio rápido

El ID documentado por EvoLink es `kimi-k3`; la página del modelo y la documentación de Chat Completions están disponibles

1. [Ver detalles y precios de Kimi K3 en EvoLink](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=landing_overview)
2. [Crear o administrar una clave API de EvoLink](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-kimi-k3-usecases&utm_content=api_key)

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

[Abrir la documentación API de Kimi K3 en EvoLink](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=first_run)

> [!IMPORTANT]
> La página del modelo y la documentación de EvoLink verifican la ruta pública y el ID. No se verificó una superficie independiente de navegador o sin código para Kimi K3, y este repositorio no afirma una prueba API de pago independiente

## 📑 Menú

| Section | Cases |
|---|---|
| [Juegos interactivos y 3D](#games-3d) | 39 |
| [Frontend y diseño en movimiento](#frontend-motion) | 27 |
| [Programación e integraciones](#coding-integrations) | 16 |
| [Evaluación y límites](#evaluation-limits) | 47 |
| [Recursos relacionados](#related-resources) | Recursos relacionados |
| [Inicio rápido](#quick-api-access) | Inicio rápido |
| [Agradecimientos](#acknowledge) | Créditos y correcciones |

| Case | Category | What it shows | Type |
|---|---|---|---|
| [Crear un pod racer voxel con un prompt](#case-1) | Juegos interactivos y 3D | Usa una idea breve para prototipar una carrera voxel y define una segunda iteración | Demo |
| [Comparar Frogger con el mismo prompt](#case-2) | Juegos interactivos y 3D | Mantén constante el prompt para inspeccionar diferencias entre modelos | Evaluation |
| [Generar Frogger y su grabación](#case-3) | Juegos interactivos y 3D | Prueba en una sola ejecución tanto el juego como el flujo de grabación | Demo |
| [Prototipar un portaaviones en Three.js](#case-4) | Juegos interactivos y 3D | Usa una escena concreta para probar un prototipo 3D interactivo | Demo |
| [Crear un frontend de motion graphics interactivo](#case-5) | Frontend y diseño en movimiento | Construye gráficos que sigan siendo interactivos al pausar la animación | Demo |
| [Producir un anuncio animado sincronizado](#case-6) | Frontend y diseño en movimiento | Comprueba la sincronía entre música, efectos y movimiento | Demo |
| [Comparar el diseño frontend en la tarea de lámpara de lava de BridgeBench](#case-7) | Evaluación y límites | Usa la tarea de lámpara de lava de BridgeBench como una comparación acotada de diseño frontend, no como una clasificación universal | Benchmark |
| [Evaluar la escritura de guiones con voz editorial](#case-8) | Evaluación y límites | Mide el ajuste a la voz editorial, la posición relativa y el coste por guion dentro de un benchmark interno claramente identificado | Benchmark |
| [Crear un juego inspirado en Paper Mario con herramientas de agente](#case-9) | Juegos interactivos y 3D | Combina Kimi K3 con un harness de agente y herramientas de recursos para producir elementos de juego tanto 2D como 3D | Demo |
| [Comparar diseño, coste y dificultad en un juego tipo Flappy](#case-10) | Evaluación y límites | Registra los ajustes de dificultad, el coste, el diseño y las funciones de juego al comparar juegos generados | Benchmark |
| [Generar un shooter en primera persona ambientado en el metro](#case-11) | Juegos interactivos y 3D | Usa un escenario concreto de metro para examinar el resultado de un shooter en primera persona generado | Demo |
| [Comparar el diseño de juegos con el mismo prompt](#case-12) | Evaluación y límites | Mantén constante el prompt de diseño y examina por separado el ritmo, el criterio de diseño y las sensaciones de juego | Benchmark |
| [Exigir una revisión independiente en auditorías estadísticas](#case-13) | Evaluación y límites | Complementa las auditorías estadísticas generadas por el modelo con una revisión independiente de expertos u otros modelos antes de confiar en sus hallazgos | Limit |
| [Crear motion design íntegramente con código](#case-14) | Frontend y diseño en movimiento | Comprueba si un flujo de programación de una sola ejecución puede producir motion design sin herramientas auxiliares de generación | Demo |
| [Investigar a una persona y crear su sitio personal animado](#case-15) | Frontend y diseño en movimiento | Da una instrucción amplia para un sitio personal y examina la investigación, planificación, iteración y validación en el navegador del modelo | Tutorial |
| [Evaluar una ejecución frontend lenta pero sólida](#case-16) | Evaluación y límites | Registra el tiempo de finalización junto con la calidad del resultado al probar una tarea frontend | Evaluation |
| [Generar una simulación de un agujero negro](#case-17) | Frontend y diseño en movimiento | Usa una tarea de visualización científica para examinar una simulación generada de un agujero negro | Demo |
| [Crear un MacBook virtual con macOS funcional](#case-18) | Programación e integraciones | Combina el renderizado de hardware con Three.js y una simulación interactiva de un sistema operativo en el navegador | Demo |
| [Modelar un motor V8 con Blender MCP](#case-19) | Juegos interactivos y 3D | Usa Blender MCP y una sola petición para generar un modelo mecánico 3D detallado | Integration |
| [Probar la escritura de misterio para detectar fallos de presagio](#case-20) | Evaluación y límites | Evalúa si un misterio generado equilibra las pistas, la sutileza y el presagio narrativo | Limit |
| [Comparar el modelado y la animación del Halcón Milenario](#case-21) | Evaluación y límites | Usa peticiones de estilo y ajustes de esfuerzo equivalentes para comparar modelado 3D, animación, tiempo y coste | Benchmark |
| [Probar modelado frontend complejo, partículas y shaders](#case-22) | Frontend y diseño en movimiento | Usa un prompt frontend público para examinar en una sola pasada la precisión del modelado, los efectos de partículas y la generación de shaders inline | Demo |
| [Crear una arena de combate jugable a partir de una referencia](#case-23) | Juegos interactivos y 3D | Usa una sola referencia para probar la generación de una arena jugable completa en una ejecución | Demo |
| [Crear tres juegos retro autónomos como archivos HTML](#case-24) | Juegos interactivos y 3D | Exige gráficos, enemigos, reglas y juego autónomo dentro de archivos HTML independientes | Benchmark |
| [Crear un compilador GPU desde un DSL hasta PTX](#case-25) | Programación e integraciones | Usa una tarea de compilador de extremo a extremo que abarque un DSL, las pasadas del compilador, la generación de PTX y una ruta para Tensor Cores | Demo |
| [Generar una herramienta de música procedimental en un intento](#case-26) | Frontend y diseño en movimiento | Prueba la generación en un intento de un generador interactivo de música procedimental y compara con cautela el resultado visible | Demo |
| [Crear en una ejecución un juego de escondite con camaleones](#case-27) | Juegos interactivos y 3D | Genera un juego en un solo archivo con combinación de colores, zonas procedimentales, sonido y puntuación en varias rondas | Benchmark |
| [Revisar una colección de diez proyectos de Kimi K3](#case-28) | Evaluación y límites | Usa una recopilación enlazada de proyectos para descubrir artefactos concretos que deban verificarse por separado | Evaluation |
| [Comparar una landing page avanzada entre cuatro modelos](#case-29) | Evaluación y límites | Mantén constante la petición de la landing page y examina la profundidad de las animaciones y el grado de finalización de los resultados | Evaluation |
| [Evaluar mecánicas y costes de juegos retro](#case-30) | Evaluación y límites | Compara jugabilidad, físicas, mecánicas, comportamiento autónomo, uso de tokens y coste en las mismas tareas de juegos retro | Benchmark |
| [Comparar la generación de juegos con Fable 5](#case-31) | Evaluación y límites | Usa un ejemplo de juegos generados lado a lado como evaluación acotada, no como veredicto general sobre los modelos | Evaluation |
| [Crear un raytracer de agujero negro en tiempo real con WebGL2](#case-32) | Programación e integraciones | Prueba la generación con un prompt de un raytracer geodésico nativo de WebGL2 dentro de un solo archivo HTML | Benchmark |
| [Crear una página de producto en Three.js a partir de dos imágenes](#case-33) | Frontend y diseño en movimiento | Usa dos imágenes de referencia y un requisito explícito de Three.js para generar una presentación de producto | Demo |
| [Comparar tareas complejas de frontend y desarrollo con Opus 4.8](#case-34) | Evaluación y límites | Usa varias tareas complejas de programación para identificar victorias y derrotas en lugar de declarar que un modelo es universalmente superior | Evaluation |
| [Revisar benchmarks y una prueba de landing page](#case-35) | Evaluación y límites | Combina el contexto de benchmarks con una prueba concreta de generación de landing pages, manteniendo separados ambos tipos de evidencia | Evaluation |
| [Crear un juego 2.5D al estilo Paper Mario con herramientas de agente](#case-36) | Juegos interactivos y 3D | Usa Kimi K3 con Grok Build o Claude Code y Spriterrific para montar un flujo de trabajo de juego 2.5D | Tutorial |
| [Evaluar el razonamiento inductivo con tareas de grafos a fórmulas](#case-37) | Evaluación y límites | Mide la corrección, el comportamiento en holdout y la complejidad de las fórmulas en tareas de inducción de primer orden | Benchmark |
| [Revisar informes sobre juegos, landing pages, trabajo 3D y contexto largo](#case-38) | Evaluación y límites | Usa una recopilación de múltiples fuentes para comparar artefactos concretos y señalar las limitaciones de velocidad junto con las afirmaciones de coste | Evaluation |
| [Inventar una cortadora de pan de lujo y su página de producto](#case-39) | Frontend y diseño en movimiento | Combina la ideación de producto, una vista explotada, una demostración y una landing page en un solo artefacto de diseño | Demo |
| [Auditar un plan complejo y cuestionar sus soluciones](#case-40) | Evaluación y límites | Usa un segundo modelo para identificar hallazgos minimizados, soluciones incorrectas y conclusiones que deberían rechazarse | Evaluation |
| [Comparar diagramas ASCII de aprendizaje por refuerzo al estilo PPO](#case-41) | Evaluación y límites | Mantén constante el prompt del diagrama ASCII y compara cómo representan los modelos el ciclo de aprendizaje por refuerzo | Evaluation |
| [Modelar en Blender mientras se registran errores de capacidad](#case-42) | Evaluación y límites | Evalúa el progreso parcial en Blender junto con la fiabilidad del servicio, no solo el artefacto | Limit |
| [Crear un RPG wuxia 3D para navegador](#case-43) | Juegos interactivos y 3D | Combina combate cuerpo a cuerpo, misiones, inventario, clima, interiores, trabajo de entornos en Blender y recursos adaptados | Demo |
| [Crear un juego multijugador de navegador al estilo Minecraft](#case-44) | Juegos interactivos y 3D | Usa una ejecución acotada por tiempo y coste para producir un juego multijugador online jugable en el navegador | Demo |
| [Generar un GIF recursivo de diez segundos con un pelícano](#case-45) | Frontend y diseño en movimiento | Usa una instrucción completamente especificada de animación en bucle para examinar la continuidad narrativa y la recursión en un GIF | Demo |
| [Crear un emulador de Game Boy Advance basado en mGBA WASM](#case-46) | Programación e integraciones | Integra un modelo 3D con licencia y un núcleo de emulación real, y mejora recursivamente la interfaz y la experiencia de juego | Integration |
| [Comparar la generación de Flappy Bird en una arena](#case-47) | Evaluación y límites | Usa una tarea de arena para comparar dos resultados generados de Flappy Bird, manteniendo el juicio limitado a esa tarea | Evaluation |
| [Recrear un juego cooperativo de navegador con pantalla dividida](#case-48) | Juegos interactivos y 3D | Usa una petición para generar cooperación en pantalla dividida dentro del navegador e interacción con el entorno en tiempo real | Demo |
| [Generar un juego jugable con el modo de diseño de Command Code](#case-49) | Juegos interactivos y 3D | Usa el comando de diseño de Command Code para crear un juego en una sola ejecución y registra si el resultado es jugable | Demo |
| [Investigar varios temas con fuentes en chino](#case-50) | Programación e integraciones | Usa tareas de investigación prolongadas para comparar exhaustividad y latencia entre generaciones de modelos | Evaluation |
| [Montar un RPG wuxia de navegador cohesionado](#case-51) | Juegos interactivos y 3D | Integra desplazamiento, combate, misiones, inventario, clima, exploración y trabajo de entornos 3D en un solo juego | Demo |
| [Resolver con una herramienta un problema de inducción visual de Bongard](#case-52) | Evaluación y límites | Comprueba si el uso de herramientas ayuda a deducir la regla visual en una tarea de razonamiento de Bongard | Evaluation |
| [Comparar el gusto frontend y el diseño 3D con GPT-5.6 Sol](#case-53) | Evaluación y límites | Examina funciones, gusto visual, elegancia y ejecución 3D en una comparación frontend acotada | Evaluation |
| [Crear un crossover jugable de Hollow Knight](#case-54) | Juegos interactivos y 3D | Usa recursos de un juego existente para crear una batalla jugable entre el Caballero y Kimi | Demo |
| [Generar un SVG lateral de un BMW M4 CS](#case-55) | Frontend y diseño en movimiento | Usa un vehículo y un punto de vista específicos para examinar el resultado de una ilustración vectorial | Demo |
| [Clonar macOS en el navegador con aplicaciones funcionales](#case-56) | Programación e integraciones | Crea una simulación de sistema operativo en el navegador que incluya aplicaciones de música, navegador y correo electrónico | Demo |
| [Comparar la generación de sitios web entre tres modelos](#case-57) | Evaluación y límites | Usa resultados visibles de sitios web para comparar Kimi K3, Fable 5 y GPT-5.6 Sol en una prueba | Evaluation |
| [Recrear Gargantúa mediante feedback de capturas de pantalla](#case-58) | Frontend y diseño en movimiento | Usa capturas repetidas como observaciones para diagnosticar y perfeccionar una visualización científica | Tutorial |
| [Comparar la generación y el coste de juegos 3D procedimentales](#case-59) | Evaluación y límites | Mantén constante el prompt entre modelos y examina sistemas generados de ruleta, tragaperras y pinball junto con el coste por ejecución | Benchmark |
| [Crear en una ejecución un juego 3D de navegador al estilo Fall Guys](#case-60) | Juegos interactivos y 3D | Usa una petición de una sola ejecución para generar un juego de obstáculos 3D jugable y expón el proyecto para su inspección | Demo |
| [Crear y autoprobar un FPS apocalíptico ambientado en Lisboa](#case-61) | Juegos interactivos y 3D | Usa una ejecución de esfuerzo máximo y un solo prompt que pruebe, capture pantallas e itere antes de entregar un FPS jugable | Demo |
| [Crear una simulación de macOS con FaceTime funcional](#case-62) | Programación e integraciones | Usa una tarea de sistema operativo virtual para comprobar si funciona la interacción de una aplicación generada | Demo |
| [Generar un juego al estilo Animal Crossing a partir de una petición simple](#case-63) | Juegos interactivos y 3D | Usa una instrucción mínima de juego para examinar la jugabilidad, el bucle de juego y los efectos de paralaje | Demo |
| [Añadir un comparador frontend de dos tareas](#case-64) | Programación e integraciones | Crea una herramienta que seleccione dos tareas completadas, las muestre lado a lado y sincronice vistas e interacciones | Tutorial |
| [Generar un juego al estilo Mario a partir de una frase](#case-65) | Juegos interactivos y 3D | Usa una petición mínima de una sola ejecución para examinar jugabilidad, diseño de niveles, pixel art y paralaje | Demo |
| [Perfeccionar una visualización de agujero negro con 62 capturas](#case-66) | Frontend y diseño en movimiento | Usa un bucle de feedback de capturas para leer, diagnosticar y corregir una simulación visual durante muchas iteraciones | Tutorial |
| [Crear un shooter de zombis en primera persona funcional](#case-67) | Juegos interactivos y 3D | Usa un objetivo concreto de shooter de zombis para examinar un artefacto FPS completo y jugable | Demo |
| [Crear un PDF de marketing sobre post-training](#case-68) | Frontend y diseño en movimiento | Usa un producto y un formato de entrega concretos para generar un documento de marketing | Demo |
| [Comparar el detalle y la iluminación de una escena 3D de arsenal](#case-69) | Evaluación y límites | Examina la densidad de objetos, la iluminación y el detalle de la escena en una comparación acotada entre Kimi K3 y Opus 4.8 | Evaluation |
| [Crear una interfaz de usuario a partir de un prompt](#case-70) | Frontend y diseño en movimiento | Usa una sola petición para generar y examinar un diseño completo de interfaz de usuario | Demo |
| [Crear un juego indie de naves](#case-71) | Juegos interactivos y 3D | Usa Kimi K3 Standard para una primera versión y compara coherencia, fallos, calidad visual y coste de tokens | Demo |
| [Comparar frontends con prompts Arena idénticos](#case-72) | Evaluación y límites | Usa prompts idénticos y resultados paralelos en lugar de depender de una sola posición en el ranking | Benchmark |
| [Autoprobar un juego en Summer Engine](#case-73) | Juegos interactivos y 3D | Haz que Kimi K3 ejecute el juego, revise capturas y registros y corrija fallos visibles en la misma sesión | Demo |
| [Evaluar Kimi Code con agentes de código](#case-74) | Evaluación y límites | Evalúa Kimi K3 con varias pruebas y coste por tarea sin generalizar un único ranking frontend | Benchmark |
| [Configurar Kimi como subagente de Codex](#case-75) | Programación e integraciones | Mantén la orquestación en Codex y delega el frontend a un subagente Kimi K3 OpenCode con un límite claro para secretos | Tutorial |
| [Comparar Arena y el arnés de reparación](#case-76) | Evaluación y límites | Mira tanto preferencia frontend como reparación de repositorios porque Kimi K3 puede quedar primero en una y séptimo en otra | Benchmark |
| [Iterar un battle royale en el navegador](#case-77) | Juegos interactivos y 3D | Prevé iteraciones autónomas largas y prompts posteriores específicos para juegos de navegador con muchas funciones | Demo |
| [Crear un sitio web de estilo premiado](#case-78) | Frontend y diseño en movimiento | Evalúa la sesión grabada completa y no solo la captura final | Tutorial |
| [Enrutar código simple mediante ChatLLM](#case-79) | Programación e integraciones | Envía código simple a Kimi K3 y reserva el código difícil y el diseño para otros modelos | Integration |
| [Evaluar Kimi K3 en Prinzbench](#case-80) | Evaluación y límites | Usa una actualización independiente de benchmark para comparar Kimi K3 con modelos abiertos y frontera en búsqueda, razonamiento y consistencia. | Benchmark |
| [Crear un frontend con metaballs al desplazarse](#case-81) | Frontend y diseño en movimiento | Pide a Kimi K3 una página estilo Awwwards con desplazamiento y revisa si los efectos matemáticos pueden reemplazar mallas o texturas pesadas. | Demo |
| [Rediseñar un sitio personal entre modelos](#case-82) | Frontend y diseño en movimiento | Ejecuta el mismo brief de rediseño con varios harnesses de código y compara tiempo, dirección visual y ajuste a la identidad existente. | Evaluation |
| [Ampliar el paisaje de un juego espacial](#case-83) | Juegos interactivos y 3D | Usa Kimi K3 como una pasada larga para sustituir terreno provisional por un entorno de juego más grande inspirado en datos reales. | Demo |
| [Desbloquear un renderizador físico en Three.js](#case-84) | Juegos interactivos y 3D | Introduce Kimi K3 en un proyecto de física Three.js estancado cuando la matemática funciona pero el render necesita avanzar. | Demo |
| [Comparar generación de un gemelo digital ISS](#case-85) | Evaluación y límites | Usa un reto 3D con el mismo prompt para comparar Kimi K3 y GPT-5.6 Sol en reconstrucción, controles, etiquetas y detalle visual. | Benchmark |
| [Crear un explorador interactivo de cuero cabelludo](#case-86) | Frontend y diseño en movimiento | Usa Kimi K3 para una escena educativa 3D de una sola pasada con capas anatómicas, cabello responsivo y puntos interactivos. | Demo |
| [Compartir un prompt de dashboard globo 3D](#case-87) | Frontend y diseño en movimiento | Estudia un setup con prompt e imagen de referencia para un dashboard globo 3D de Kimi K3 en vez de inferir el flujo solo por la imagen final. | Tutorial |
| [Crear Counter-Strike en navegador en un archivo](#case-88) | Juegos interactivos y 3D | Usa Kimi K3 para generar un FPS de navegador en un solo archivo y verifica mapa, bots, armas, reglas de ronda y audio procedural. | Demo |
| [Revisar un mundo forestal WebGPU](#case-89) | Evaluación y límites | Evalúa Kimi K3 como cerebro de agente de código en una construcción larga con Three.js y WebGPU, incluyendo calidad, velocidad, consistencia y tasa de edición. | Evaluation |
| [Comparar prompts de casa de cristal](#case-90) | Evaluación y límites | Usa una escena arquitectónica con el mismo prompt para comparar Kimi K3 y Opus 4.8 en atmósfera, iluminación y completitud espacial. | Evaluation |
| [Crear CS con recursos generados](#case-91) | Programación e integraciones | Combina Kimi K3 para el código del juego con GPT Image 2 para los recursos al prototipar un pequeño juego estilo Counter-Strike en navegador. | Integration |
| [Evaluar un gol de fútbol vóxel](#case-92) | Evaluación y límites | Ejecuta el mismo prompt de animación de fútbol en HTML/CSS/JS puro en dos modelos para comparar calidad de movimiento y coste. | Benchmark |
| [Revisar una prueba Minecraft](#case-93) | Evaluación y límites | Mira una revisión estructurada de Minecraft antes de tratar la publicidad de lanzamiento o el precio como evidencia suficiente. | Benchmark |
| [Ejecutar cinco pruebas UI UX](#case-94) | Frontend y diseño en movimiento | Evalúa Kimi K3 con varias tareas de UI, logotipo y Figma MCP en lugar de confiar en una sola captura frontend. | Evaluation |
| [Usar la skill Design de Command Code](#case-95) | Programación e integraciones | Combina Kimi K3 con una skill de diseño dedicada en Command Code al crear un prototipo visual de juego con presupuesto de tokens. | Integration |
| [Construir un juego de pirámide](#case-96) | Juegos interactivos y 3D | Usa Kimi K3 para una pasada de un día en un juego 3D de exploración, luego inspecciona misiones, interiores y alcance antes de juzgar la calidad. | Demo |
| [Crear landings desde referencias](#case-97) | Frontend y diseño en movimiento | Usa tableros de referencia, Figma AI y Motion Sites con Kimi K3 para convertir dirección visual en secciones de landing reutilizables. | Tutorial |
| [Medir límites de nivel API](#case-98) | Evaluación y límites | Planifica ejecuciones de agente con Kimi K3 según tokens, nivel, TPM y TPD, no solo por el precio principal del modelo. | Limit |
| [Comparar un demo estilo Limbo](#case-99) | Evaluación y límites | Compara alcance jugable, pulido, coste y fallos al probar Kimi K3 frente a Fable 5 en el mismo prototipo de juego. | Benchmark |
| [Revisar costes de VulcanBench](#case-100) | Evaluación y límites | Usa los resultados de VulcanBench para comparar precisión, coste y evidencia abierta de Kimi K3 antes de elegir un modelo de producción. | Benchmark |
| [Comparar profundidad en Minecraft](#case-101) | Juegos interactivos y 3D | Compara profundidad, gráficos, velocidad y valor de suscripción en un juego Minecraft one-shot de Kimi K3 frente a Fable 5. | Evaluation |
| [Construir un FPS de Fallout](#case-102) | Juegos interactivos y 3D | Usa un FPS estilo Fallout hecho en tres intentos para estimar alcance jugable y coste de tokens con Kimi K3. | Demo |
| [Seguir un tutorial web premium](#case-103) | Frontend y diseño en movimiento | Sigue un tutorial corto en español para usar Kimi K3 en la generación de sitios web con acabado visual premium. | Tutorial |
| [Evaluar física de doble péndulo](#case-104) | Evaluación y límites | Evalúa Kimi K3 con una simulación de doble péndulo usando coste por iteración, puntuaciones de juez y criterios físicos. | Benchmark |
| [Lanzar un RPG de data center](#case-105) | Juegos interactivos y 3D | Estudia cómo un flujo con lead agent convirtió con Kimi K3 un brief de dos frases en un RPG completo de navegador. | Demo |
| [Comparar costes de frontend humanoide](#case-106) | Frontend y diseño en movimiento | Compara Kimi K3 y GPT-5.6 en un prompt general de frontend de robot humanoide usando líneas, tokens y coste. | Benchmark |
| [Revisar preparación en ReactBench](#case-107) | Evaluación y límites | Usa ReactBench para juzgar dónde Kimi K3 es más barato y fuerte que Opus 4.8, pero aún detrás de los modelos frontera en frontend de producción. | Benchmark |
| [Construir un juego 3D de coches](#case-108) | Juegos interactivos y 3D | Usa Kimi K3 para prototipar un juego 3D de coches con assets externos, agua, clima, carreteras y ciclo día-noche. | Demo |
| [Ejecutar Kimi K3 en Claude Code](#case-109) | Programación e integraciones | Conecta Kimi K3 a Claude Code con un VPS para mantener el flujo de coding y cambiar el backend del modelo. | Integration |
| [Evaluar Kimi K3 en AA-Briefcase](#case-110) | Evaluación y límites | Usa los resultados de AA-Briefcase para juzgar Kimi K3 en tareas agentic de trabajo del conocimiento antes de confiar en afirmaciones de leaderboard. | Benchmark |
| [Comparar clones de Geometry Dash](#case-111) | Juegos interactivos y 3D | Compara builds de juegos con el mismo brief para decidir si Kimi K3 basta para prototipos jugables de estilo móvil. | Evaluation |
| [Probar un juego retro en Command Code](#case-112) | Juegos interactivos y 3D | Usa una prueba de diseño multi-modelo en Command Code para comparar funciones de gameplay de Kimi K3 y coste por modelo. | Evaluation |
| [Auditar salvedades del leaderboard frontend](#case-113) | Evaluación y límites | Usa esta nota de limitación para separar las victorias de Kimi K3 en leaderboards de afirmaciones más amplias sobre coding y coste. | Limit |
| [Comparar resultados de arquitectura StackPerf](#case-114) | Evaluación y límites | Usa StackPerf para comparar Kimi K3 y Qwen 3.8 en calidad de arquitectura, velocidad y comportamiento de tool calls. | Benchmark |
| [Comparar builds Three.js Kimi-vs-GLM](#case-115) | Frontend y diseño en movimiento | Ejecuta los mismos prompts procedurales de Three.js con Kimi K3 y GLM 5.2 para comparar comportamiento frontend y 3D. | Benchmark |
| [Evaluar el juego Space Discoverer](#case-116) | Juegos interactivos y 3D | Usa el mini-benchmark Space Discoverer para comparar salidas de modelos en un brief genérico de juego 3D de navegador. | Benchmark |
| [Construir juego de conducción con ruta real](#case-117) | Juegos interactivos y 3D | Prototipa un juego de conducción combinando Kimi K3 con Blender y Godot alrededor de un mapa de una carretera local real. | Demo |
| [Comparar costes con prompt Monument Valley](#case-118) | Evaluación y límites | Usa un único prompt estilo Monument Valley para comparar calidad visual, tiempo de ejecución y coste entre Kimi K3 y otros modelos. | Benchmark |
| [Enrutar Kimi con claude-code-router](#case-119) | Programación e integraciones | Prueba Kimi K3 en un flujo existente de Claude Code mediante claude-code-router evitando el modo proxy innecesario. | Integration |
| [Evaluar Kimi K3 en el índice Surge](#case-120) | Evaluación y límites | Usa los resultados divididos de SurgeAI para separar la fortaleza de Kimi K3 en chat cotidiano de su rendimiento más débil en agentes empresariales y ciencia. | Benchmark |
| [Crear landing pages con referencia](#case-121) | Frontend y diseño en movimiento | Da a Kimi K3 referencias visuales sólidas y guía iterativa al probar generación de landing pages. | Demo |
| [Crear un juego vertical de plataformas](#case-122) | Juegos interactivos y 3D | Usa un brief de juego conciso para probar si Kimi K3 devuelve un prototipo web de un solo archivo. | Demo |
| [Evaluar errores en PDE](#case-123) | Evaluación y límites | Usa fallos en benchmarks de PDE para decidir dónde las tareas simbólicas o numéricas requieren verificación alrededor de Kimi K3. | Benchmark |
| [Revisar casos EHR de ClinicalBench](#case-124) | Evaluación y límites | Usa los casos EHR de ClinicalBench para inspeccionar dónde Kimi K3 acierta y dónde falla el razonamiento diagnóstico. | Benchmark |
| [Ejecutar un harness de agentes abierto](#case-125) | Programación e integraciones | Usa un harness de agentes compartido para comparar Kimi K3 con otros modelos frontera en tareas con herramientas. | Benchmark |
| [Evaluar cálculos de impuestos](#case-126) | Evaluación y límites | Prueba Kimi K3 por separado en cargas fiscales en vez de asumir que su fortaleza frontend se transfiere. | Limit |
| [Verificar un Geometry Dash generado](#case-127) | Juegos interactivos y 3D | Combina un juego de Kimi K3 con solver y pruebas en navegador antes de tratarlo como prototipo terminado. | Benchmark |
| [Simular un sistema de partículas 3D](#case-128) | Frontend y diseño en movimiento | Usa prompts de simulación de partículas para comparar la calidad de movimiento de Kimi K3 con modelos cerrados. | Evaluation |
| [Ejecutar Kimi en Codex OAuth](#case-129) | Programación e integraciones | Usa la ruta OAuth de Codex cuando un flujo de programación con Kimi K3 deba evitar configurar una clave API manual. | Integration |

<a id="games-3d"></a>
## 🎮 Juegos interactivos y 3D

<a id="case-1"></a>
### Case 1: [Crear un pod racer voxel con un prompt](https://x.com/ivanfioravanti/status/2077763009657627055) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Usa una idea breve para prototipar una carrera voxel y define una segunda iteración**

El creador informa que Kimi K3 produjo la primera versión con un único prompt público y planea añadir corredores, meta y revisión de detalles

**Prompt:**

```text
Voxel star wars pod-racers run
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01-poster.jpg" alt="Case 1 source video poster" height="360"></a>

[Play case 1 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-2"></a>
### Case 2: [Comparar Frogger con el mismo prompt](https://x.com/ivanfioravanti/status/2077754781964054825) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Mantén constante el prompt para inspeccionar diferencias entre modelos**

El creador comparte una versión Frogger de Kimi K3 como comparación. La fuente no publica el prompt ni una rúbrica

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02-poster.jpg" alt="Case 2 source video poster" height="360"></a>

[Play case 2 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-3"></a>
### Case 3: [Generar Frogger y su grabación](https://x.com/TheAhmadOsman/status/2077776567292338285) (by [@TheAhmadOsman](https://x.com/TheAhmadOsman))

**Prueba en una sola ejecución tanto el juego como el flujo de grabación**

El creador afirma que Kimi K3 produjo el juego y el flujo de grabación en una ejecución cada uno. No incluye los prompts

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03-poster.jpg" alt="Case 3 source video poster" height="360"></a>

[Play case 3 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-4"></a>
### Case 4: [Prototipar un portaaviones en Three.js](https://x.com/HarshithLucky3/status/2077753222018814360) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**Usa una escena concreta para probar un prototipo 3D interactivo**

El creador muestra despegue y recuperación de aviones en un portaaviones clase Nimitz y valora positivamente la generación 3D

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04-poster.jpg" alt="Case 4 source video poster" height="360"></a>

[Play case 4 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-9"></a>
### Case 9: [Crear un juego inspirado en Paper Mario con herramientas de agente](https://x.com/chongdashu/status/2077886028866531655) (by [@chongdashu](https://x.com/chongdashu))

**Combina Kimi K3 con un harness de agente y herramientas de recursos para producir elementos de juego tanto 2D como 3D**

El creador informa que usó Kimi K3 con Grok Build, Spriterrific para los recursos 2D y geometría para los recursos 3D en un juego inspirado en Paper Mario. La fuente demuestra el uso de herramientas y skills, pero no publica un prompt reutilizable exacto

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-09.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-09-poster.jpg" alt="Case 9 source video poster" height="360"></a>

[Play case 9 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-09.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-11"></a>
### Case 11: [Generar un shooter en primera persona ambientado en el metro](https://x.com/bijanbowen/status/2077881805751873997) (by [@bijanbowen](https://x.com/bijanbowen))

**Usa un escenario concreto de metro para examinar el resultado de un shooter en primera persona generado**

El creador muestra un FPS de metro atribuido a Kimi K3 y señala explícitamente la incertidumbre sobre si su condición de influencer afectó al resultado. No se aporta un prompt ni un flujo reproducible

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-11.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-11-poster.jpg" alt="Case 11 source video poster" height="360"></a>

[Play case 11 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-11.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-19"></a>
### Case 19: [Modelar un motor V8 con Blender MCP](https://x.com/aisearchio/status/2077962156147146925) (by [@aisearchio](https://x.com/aisearchio))

**Usa Blender MCP y una sola petición para generar un modelo mecánico 3D detallado**

El evaluador informa que Kimi K3 generó un motor V8 completo con Blender MCP a partir de un prompt. La publicación enlaza una reseña más amplia, pero no expone el prompt exacto en el registro proporcionado

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-19.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-19-poster.jpg" alt="Case 19 source video poster" height="360"></a>

[Play case 19 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-19.mp4)

Type: Integration | Date: 2026-07-17

---

<a id="case-23"></a>
### Case 23: [Crear una arena de combate jugable a partir de una referencia](https://x.com/VORTEX_Promos/status/2077879705378730074) (by [@VORTEX_Promos](https://x.com/VORTEX_Promos))

**Usa una sola referencia para probar la generación de una arena jugable completa en una ejecución**

El creador informa que Kimi K3 produjo una arena de combate jugable en una sola ejecución a partir de una referencia. La publicación incluye otra afirmación de clasificación, pero el caso de uso concreto es el artefacto de arena demostrado

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23-poster.jpg" alt="Case 23 source video poster" height="360"></a>

[Play case 23 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23-01.jpg" alt="Case 23 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-24"></a>
### Case 24: [Crear tres juegos retro autónomos como archivos HTML](https://x.com/rohanpaul_ai/status/2077889084761206860) (by [@rohanpaul_ai](https://x.com/rohanpaul_ai))

**Exige gráficos, enemigos, reglas y juego autónomo dentro de archivos HTML independientes**

La fuente informa de una comparación de Atomic Chat en la que los modelos crearon Road Fighter, Battle City y Q*bert como archivos HTML que juegan solos. La comparación de coste y calidad procede del editor y no se reproduce de forma independiente aquí

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-24.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-24-poster.jpg" alt="Case 24 source video poster" height="360"></a>

[Play case 24 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-24.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-27"></a>
### Case 27: [Crear en una ejecución un juego de escondite con camaleones](https://x.com/aimlapi/status/2077898742179459274) (by [@aimlapi](https://x.com/aimlapi))

**Genera un juego en un solo archivo con combinación de colores, zonas procedimentales, sonido y puntuación en varias rondas**

AIMLAPI informa de una comparación en una sola ejecución y con el mismo prompt para un juego de escondite, y enumera costes de 3,11 USD para Kimi K3 y 12,23 USD para Fable 5. Las funciones y los costes son resultados comunicados por el proveedor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-27.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-27-poster.jpg" alt="Case 27 source video poster" height="360"></a>

[Play case 27 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-27.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-36"></a>
### Case 36: [Crear un juego 2.5D al estilo Paper Mario con herramientas de agente](https://x.com/chongdashu/status/2077981621223837739) (by [@chongdashu](https://x.com/chongdashu))

**Usa Kimi K3 con Grok Build o Claude Code y Spriterrific para montar un flujo de trabajo de juego 2.5D**

El creador ofrece un tutorial completo con Grok Build y Kimi K3 y muestra la generación de sprites con Spriterrific. La fuente identifica las herramientas, pero no aporta prompts reutilizables exactos

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-36.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-36-poster.jpg" alt="Case 36 source video poster" height="360"></a>

[Play case 36 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-36.mp4)

Type: Tutorial | Date: 2026-07-17

---

<a id="case-43"></a>
### Case 43: [Crear un RPG wuxia 3D para navegador](https://x.com/AngryTomtweets/status/2077868163136450619) (by [@AngryTomtweets](https://x.com/AngryTomtweets))

**Combina combate cuerpo a cuerpo, misiones, inventario, clima, interiores, trabajo de entornos en Blender y recursos adaptados**

La fuente informa de un RPG de navegador con Kimi K3 que incluye combate cuerpo a cuerpo, misiones, inventario, clima dinámico e interiores explorables, además de modelado en Blender, mejoras de colisiones, retexturizado PBR y adaptación de recursos abiertos

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-43.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-43-poster.jpg" alt="Case 43 source video poster" height="360"></a>

[Play case 43 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-43.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-44"></a>
### Case 44: [Crear un juego multijugador de navegador al estilo Minecraft](https://x.com/Alezander907/status/2077926014710407407) (by [@Alezander907](https://x.com/Alezander907))

**Usa una ejecución acotada por tiempo y coste para producir un juego multijugador online jugable en el navegador**

El creador informa que Kimi K3 creó en una hora y por 6,57 USD un juego multijugador al estilo Minecraft jugable en el navegador. Son cifras autodeclaradas de una sola ejecución y un solo artefacto

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-44.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-44-poster.jpg" alt="Case 44 source video poster" height="360"></a>

[Play case 44 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-44.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-48"></a>
### Case 48: [Recrear un juego cooperativo de navegador con pantalla dividida](https://x.com/ridark_eth/status/2077882889803378969) (by [@ridark_eth](https://x.com/ridark_eth))

**Usa una petición para generar cooperación en pantalla dividida dentro del navegador e interacción con el entorno en tiempo real**

El creador informa que Kimi K3 produjo en un prompt un juego de navegador inspirado en It Takes Two, con Mario y Luigi interactuando en pantalla dividida y con el entorno en tiempo real

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-48.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-48-poster.jpg" alt="Case 48 source video poster" height="360"></a>

[Play case 48 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-48.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-49"></a>
### Case 49: [Generar un juego jugable con el modo de diseño de Command Code](https://x.com/naymur_dev/status/2077873562661335207) (by [@naymur_dev](https://x.com/naymur_dev))

**Usa el comando de diseño de Command Code para crear un juego en una sola ejecución y registra si el resultado es jugable**

El creador informa de una comparación en una sola ejecución mediante el modo de diseño de Command Code y afirma que la ejecución con Kimi K3 produjo un juego jugable por 0,038 USD. Este resultado de coste y calidad es autodeclarado

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-49.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-49-poster.jpg" alt="Case 49 source video poster" height="360"></a>

[Play case 49 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-49.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-51"></a>
### Case 51: [Montar un RPG wuxia de navegador cohesionado](https://x.com/TokenGremlin/status/2077855657068310620) (by [@TokenGremlin](https://x.com/TokenGremlin))

**Integra desplazamiento, combate, misiones, inventario, clima, exploración y trabajo de entornos 3D en un solo juego**

La fuente informa de un RPG de navegador estilo wuxia con Kimi K3 que combina combate cuerpo a cuerpo, misiones, inventario, clima dinámico, interiores explorables y una estructura de juego 3D cohesionada

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-51.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-51-poster.jpg" alt="Case 51 source video poster" height="360"></a>

[Play case 51 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-51.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-54"></a>
### Case 54: [Crear un crossover jugable de Hollow Knight](https://x.com/wangfeng0315/status/2077933531200991583) (by [@wangfeng0315](https://x.com/wangfeng0315))

**Usa recursos de un juego existente para crear una batalla jugable entre el Caballero y Kimi**

El creador, que declara trabajar en Kimi, informa que creó con recursos de Hollow Knight un juego en el que el Caballero lucha contra Kimi y proporciona un enlace público para jugar. La atribución y la evaluación deben tener en cuenta esa afiliación

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54-poster.jpg" alt="Case 54 source video poster" height="360"></a>

[Play case 54 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54-01.jpg" alt="Case 54 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-17

---

<a id="case-60"></a>
### Case 60: [Crear en una ejecución un juego 3D de navegador al estilo Fall Guys](https://x.com/aayushman2703/status/2077857886441783526) (by [@aayushman2703](https://x.com/aayushman2703))

**Usa una petición de una sola ejecución para generar un juego de obstáculos 3D jugable y expón el proyecto para su inspección**

El creador informa de una creación en una sola ejecución con Kimi K3 de un juego de navegador al estilo Fall Guys y afirma que el prompt y el proyecto de GitHub están enlazados desde la fuente. Este registro no reproduce ese prompt

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-60.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-60-poster.jpg" alt="Case 60 source video poster" height="360"></a>

[Play case 60 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-60.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-61"></a>
### Case 61: [Crear y autoprobar un FPS apocalíptico ambientado en Lisboa](https://x.com/goncalo_canhoto/status/2077863166655037668) (by [@goncalo_canhoto](https://x.com/goncalo_canhoto))

**Usa una ejecución de esfuerzo máximo y un solo prompt que pruebe, capture pantallas e itere antes de entregar un FPS jugable**

El creador informa que Kimi K3 produjo un FPS de navegador jugable ambientado en una Lisboa apocalíptica tras aproximadamente una hora, con pruebas, capturas e iteraciones repetidas. Estos detalles de tiempo y proceso son autodeclarados

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-61-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-61-01.jpg" alt="Case 61 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-63"></a>
### Case 63: [Generar un juego al estilo Animal Crossing a partir de una petición simple](https://x.com/gagarot200/status/2077949230287896830) (by [@gagarot200](https://x.com/gagarot200))

**Usa una instrucción mínima de juego para examinar la jugabilidad, el bucle de juego y los efectos de paralaje**

El creador informa que Kimi K3 generó a partir de un prompt muy simple un juego al estilo Animal Crossing completamente jugable, con bucle de juego y efectos de paralaje. La redacción exacta no aparece en el registro proporcionado

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-63.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-63-poster.jpg" alt="Case 63 source video poster" height="360"></a>

[Play case 63 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-63.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-65"></a>
### Case 65: [Generar un juego al estilo Mario a partir de una frase](https://x.com/izutorishima/status/2077939370154475992) (by [@izutorishima](https://x.com/izutorishima))

**Usa una petición mínima de una sola ejecución para examinar jugabilidad, diseño de niveles, pixel art y paralaje**

El creador informa que Kimi K3 produjo a partir de una sola instrucción un juego funcional al estilo Mario sin errores evidentes, con estructura de niveles y paralaje. El mismo informe critica la calidad de la música y los gráficos

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-01.jpg" alt="Case 65 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-02.jpg" alt="Case 65 source image 2" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-03.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-03.jpg" alt="Case 65 source image 3" height="360"></a>

Type: Demo | Date: 2026-07-17

---

<a id="case-67"></a>
### Case 67: [Crear un shooter de zombis en primera persona funcional](https://x.com/X2worldtech/status/2077902793449296203) (by [@X2worldtech](https://x.com/X2worldtech))

**Usa un objetivo concreto de shooter de zombis para examinar un artefacto FPS completo y jugable**

La fuente muestra un FPS de zombis completamente funcional atribuido a Kimi K3. No proporciona el prompt, detalles de implementación ni una evaluación externa de la jugabilidad

> [!WARNING]
> The original source permalink returned HTTP 404 during the 2026-07-17 audit. Attribution and evidence are preserved from the supplied high-confidence source package.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-67.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-67-poster.jpg" alt="Case 67 source video poster" height="360"></a>

[Play case 67 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-67.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-71"></a>
### Case 71: [Crear un juego indie de naves](https://x.com/ChrisGPT/status/2078261217924087999) (by [@ChrisGPT](https://x.com/ChrisGPT))

**Usa Kimi K3 Standard para una primera versión y compara coherencia, fallos, calidad visual y coste de tokens**

ChrisGPT informa de una primera versión de un juego de naves por unos 2,50 dólares en tokens API. La consideró más coherente y con menos errores que GPT-5.5, aunque Fable 5 seguía siendo más pulido visualmente

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-71.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-71-poster.jpg" alt="Case 71 source video poster" height="360"></a>

[Play case 71 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-71.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-73"></a>
### Case 73: [Autoprobar un juego en Summer Engine](https://x.com/MathiasHeide/status/2078231589436465199) (by [@MathiasHeide](https://x.com/MathiasHeide))

**Haz que Kimi K3 ejecute el juego, revise capturas y registros y corrija fallos visibles en la misma sesión**

Mathias Heide informa de que Kimi K3 creó un juego de aviones de papel en una sesión de 27 minutos, lo ejecutó, revisó capturas y logs, corrigió errores y cambió el avión negro a blanco

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-73.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-73-poster.jpg" alt="Case 73 source video poster" height="360"></a>

[Play case 73 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-73.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-77"></a>
### Case 77: [Iterar un battle royale en el navegador](https://x.com/Ananth7e/status/2078158089929601203) (by [@Ananth7e](https://x.com/Ananth7e))

**Prevé iteraciones autónomas largas y prompts posteriores específicos para juegos de navegador con muchas funciones**

Ananth informa de más de 130 minutos y 40 rondas de capturas de Chrome para un juego estilo PUBG, seguidas de dos prompts adicionales para corregir errores restantes

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-77.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-77-poster.jpg" alt="Case 77 source video poster" height="360"></a>

[Play case 77 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-77.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-83"></a>
### Case 83: [Ampliar el paisaje de un juego espacial](https://x.com/startracker/status/2078543423167160342) (by [@startracker](https://x.com/startracker))

**Usa Kimi K3 como una pasada larga para sustituir terreno provisional por un entorno de juego más grande inspirado en datos reales.**

El creador describe el segundo día de un juego espacial: Kimi K3 reemplazó una costa provisional por un paisaje de 8 x 8 km inspirado en Islandia, añadió océano animado sensible a la costa, reconstruyó la nave y generó recursos ambientales para una pasada posterior. También señala ejecución lenta y problemas pendientes de captura de fotogramas.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-83.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-83-poster.jpg" alt="Case 83 source video poster" height="360"></a>

[Play case 83 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-83.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-84"></a>
### Case 84: [Desbloquear un renderizador físico en Three.js](https://x.com/mattwatkajtys/status/2078523373861339475) (by [@mattwatkajtys](https://x.com/mattwatkajtys))

**Introduce Kimi K3 en un proyecto de física Three.js estancado cuando la matemática funciona pero el render necesita avanzar.**

El creador indica que su constructor de mundos físicos llevaba meses bloqueado porque el pipeline de render no progresaba, aunque la matemática y la física funcionaban. La pasada con Kimi K3 movió el proyecto y el video muestra el resultado interactivo actual.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-84.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-84-poster.jpg" alt="Case 84 source video poster" height="360"></a>

[Play case 84 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-84.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-88"></a>
### Case 88: [Crear Counter-Strike en navegador en un archivo](https://x.com/prasenx/status/2078453069021659477) (by [@prasenx](https://x.com/prasenx))

**Usa Kimi K3 para generar un FPS de navegador en un solo archivo y verifica mapa, bots, armas, reglas de ronda y audio procedural.**

El creador reporta un juego tipo Counter-Strike con Kimi K3 en un único HTML de más de 3.700 líneas y sin build step. El artefacto incluye mapa inspirado en Dust2, varias armas, recargas, bots que patrullan y empujan, headshots, kill feed, ronda de dos minutos, audio procedural, Three.js, PBR y coste API inferior a 5 dólares.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-88.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-88-poster.jpg" alt="Case 88 source video poster" height="360"></a>

[Play case 88 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-88.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-96"></a>
### Case 96: [Construir un juego de pirámide](https://x.com/ice_bearcute/status/2078828887468056763) (by [@ice_bearcute](https://x.com/ice_bearcute))

**Usa Kimi K3 para una pasada de un día en un juego 3D de exploración, luego inspecciona misiones, interiores y alcance antes de juzgar la calidad.**

ice_bearcute informa haber construido en un día un juego 3D Pyramid Expedition con Kimi K3. La fuente dice que el resultado no es solo una escena exterior: los jugadores pueden explorar una tumba antigua y completar misiones, mientras que el medio adjunto aporta evidencia visible de jugabilidad.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-96.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-96-poster.jpg" alt="Case 96 source video poster" height="360"></a>

[Play case 96 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-96.mp4)

Type: Demo | Date: 2026-07-19

---

<a id="case-101"></a>
### Case 101: [Comparar profundidad en Minecraft](https://x.com/vikktorrrre/status/2079294696459804762) (by [@vikktorrrre](https://x.com/vikktorrrre))

**Compara profundidad, gráficos, velocidad y valor de suscripción en un juego Minecraft one-shot de Kimi K3 frente a Fable 5.**

Vikktorrrre probó el mismo prompt en Kimi K3 y Fable 5 sin ajustes. Kimi tardó 1 hora y 20 minutos, razonó primero la lógica y mecánicas, y según el post produjo mejores gráficos y un resultado más jugable; Fable 5 fue más rápido pero más superficial.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-101.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-101-poster.jpg" alt="Case 101 source video poster" height="360"></a>

[Play case 101 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-101.mp4)

Type: Evaluation | Date: 2026-07-20

---

<a id="case-102"></a>
### Case 102: [Construir un FPS de Fallout](https://x.com/kirillk_web3/status/2079290747585437781) (by [@kirillk_web3](https://x.com/kirillk_web3))

**Usa un FPS estilo Fallout hecho en tres intentos para estimar alcance jugable y coste de tokens con Kimi K3.**

Kirill cuenta que Kimi K3 creó un clon FPS Vault-Tec de Fallout en tres intentos por unos 2,48 dólares de API. El post compara el mismo conteo de tokens con 5,34 dólares en GPT-5.6 Sol y presenta el resultado como un prototipo FPS jugable de bajo coste.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-102.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-102-poster.jpg" alt="Case 102 source video poster" height="360"></a>

[Play case 102 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-102.mp4)

Type: Demo | Date: 2026-07-20

---

<a id="case-105"></a>
### Case 105: [Lanzar un RPG de data center](https://x.com/demian_ai/status/2079239035596218578) (by [@demian_ai](https://x.com/demian_ai))

**Estudia cómo un flujo con lead agent convirtió con Kimi K3 un brief de dos frases en un RPG completo de navegador.**

Demian describe Charlie & the Token Factory a partir de un prompt breve sobre un mundo tipo Pokemon de centros de datos. El post menciona combates, captura, progreso, jefes, guardado, música y postgame, además de agentes especialistas, gates de build y verificadores que encontraron bugs reales.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-105.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-105-poster.jpg" alt="Case 105 source video poster" height="360"></a>

[Play case 105 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-105.mp4)

Type: Demo | Date: 2026-07-20

---

<a id="case-108"></a>
### Case 108: [Construir un juego 3D de coches](https://x.com/LexnLin/status/2079233761242235081) (by [@LexnLin](https://x.com/LexnLin))

**Usa Kimi K3 para prototipar un juego 3D de coches con assets externos, agua, clima, carreteras y ciclo día-noche.**

LexnLin dice que Kimi K3 construyó un juego 3D de coches con assets externos. El post destaca agua realista, paisajes, carreteras, clima, ciclo día-noche y varios medios de evidencia.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-poster.jpg" alt="Case 108 source video poster" height="360"></a>

[Play case 108 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-01.jpg" alt="Case 108 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-02.jpg" alt="Case 108 source image 2" height="360"></a>

Type: Demo | Date: 2026-07-20

---

<a id="case-111"></a>
### Case 111: [Comparar clones de Geometry Dash](https://x.com/Nekt_0/status/2079629004483465473) (by [@Nekt_0](https://x.com/Nekt_0))

**Compara builds de juegos con el mismo brief para decidir si Kimi K3 basta para prototipos jugables de estilo móvil.**

Nekt dice que Kimi K3 dedicó unos 30 minutos y 200.000 tokens a construir un clon tipo Geometry Dash con saltos, obstáculos, niveles, música y efectos visuales, y lo compara con una build de Claude Fable 5 en el video adjunto.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-111.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-111-poster.jpg" alt="Case 111 source video poster" height="360"></a>

[Play case 111 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-111.mp4)

Type: Evaluation | Date: 2026-07-21

---

<a id="case-112"></a>
### Case 112: [Probar un juego retro en Command Code](https://x.com/naymur_dev/status/2079627963000398334) (by [@naymur_dev](https://x.com/naymur_dev))

**Usa una prueba de diseño multi-modelo en Command Code para comparar funciones de gameplay de Kimi K3 y coste por modelo.**

Naymur reporta el mismo prompt /design en Command Code con Fable 5, GPT-5.6 Sol, Grok 4.5 y Kimi K3. El post dice que Kimi K3 produjo un juego retro ASCII con gameplay, niveles, balas y jefes, con coste reportado de $0.15.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-112.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-112-poster.jpg" alt="Case 112 source video poster" height="360"></a>

[Play case 112 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-112.mp4)

Type: Evaluation | Date: 2026-07-21

---

<a id="case-116"></a>
### Case 116: [Evaluar el juego Space Discoverer](https://x.com/fabriciocarraro/status/2079548607393382528) (by [@fabriciocarraro](https://x.com/fabriciocarraro))

**Usa el mini-benchmark Space Discoverer para comparar salidas de modelos en un brief genérico de juego 3D de navegador.**

Fabricio Carraro reporta un mini-benchmark con Claude Fable 5, GPT-5.6 Sol y Kimi K3 en máximos niveles de razonamiento. La tarea fue un juego 3D de navegador llamado Space Discoverer, y el post dice que los tres convergieron en Three.js sobre WebGL 2.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-116.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-116-poster.jpg" alt="Case 116 source video poster" height="360"></a>

[Play case 116 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-116.mp4)

Type: Benchmark | Date: 2026-07-21

---

<a id="case-117"></a>
### Case 117: [Construir juego de conducción con ruta real](https://x.com/bijanbowen/status/2079526003643179102) (by [@bijanbowen](https://x.com/bijanbowen))

**Prototipa un juego de conducción combinando Kimi K3 con Blender y Godot alrededor de un mapa de una carretera local real.**

Bijan Bowen muestra a Kimi K3 creando un juego de conducción con Blender y Godot, usando como mapa un tramo real de carretera cercano al creador. El video adjunto es la evidencia pública del estado de la build.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-117.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-117-poster.jpg" alt="Case 117 source video poster" height="360"></a>

[Play case 117 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-117.mp4)

Type: Demo | Date: 2026-07-21

---

<a id="case-122"></a>
### Case 122: [Crear un juego vertical de plataformas](https://x.com/diegocabezas01/status/2079946676270219488) (by [@diegocabezas01](https://x.com/diegocabezas01))

**Usa un brief de juego conciso para probar si Kimi K3 devuelve un prototipo web de un solo archivo.**

Diego Cabezas muestra una ejecución de Kimi K3 Max para un juego vertical donde el jugador salta cada vez más alto mientras las plataformas se mueven. La publicación registra un resultado de una sola toma en HTML.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-122.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-122-poster.jpg" alt="Case 122 source video poster" height="360"></a>

[Play case 122 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-122.mp4)

Type: Demo | Date: 2026-07-22

---

<a id="case-127"></a>
### Case 127: [Verificar un Geometry Dash generado](https://x.com/Kirratr/status/2079902410042909108) (by [@Kirratr](https://x.com/Kirratr))

**Combina un juego de Kimi K3 con solver y pruebas en navegador antes de tratarlo como prototipo terminado.**

Kirratr informa que Kimi K3 tardó 36:53 en el mismo brief de Geometry Dash. La fuente dice que un solver encontró una ruta ganadora de 64 saltos y la reprodujo en el navegador sin errores de consola.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-127.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-127-poster.jpg" alt="Case 127 source video poster" height="360"></a>

[Play case 127 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-127.mp4)

Type: Benchmark | Date: 2026-07-22

---


<a id="frontend-motion"></a>
## 🎨 Frontend y diseño en movimiento

<a id="case-5"></a>
### Case 5: [Crear un frontend de motion graphics interactivo](https://x.com/chetaslua/status/2077749371144442022) (by [@chetaslua](https://x.com/chetaslua))

**Construye gráficos que sigan siendo interactivos al pausar la animación**

El creador informa de una construcción de 42 minutos, en una ejecución, con código simple y sin harness, MCP ni skills

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05-poster.jpg" alt="Case 5 source video poster" height="360"></a>

[Play case 5 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-6"></a>
### Case 6: [Producir un anuncio animado sincronizado](https://x.com/abhinavflac/status/2077760297918484667) (by [@abhinavflac](https://x.com/abhinavflac))

**Comprueba la sincronía entre música, efectos y movimiento**

El creador dice que un prompt produjo en una ejecución un anuncio de estilo Spotify. El prompt exacto no está publicado

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06-poster.jpg" alt="Case 6 source video poster" height="360"></a>

[Play case 6 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-14"></a>
### Case 14: [Crear motion design íntegramente con código](https://x.com/chetaslua/status/2077952938564354503) (by [@chetaslua](https://x.com/chetaslua))

**Comprueba si un flujo de programación de una sola ejecución puede producir motion design sin herramientas auxiliares de generación**

El creador informa de un resultado de motion design con Kimi K3 en una sola ejecución, realizado por completo con código y sin MCP, skills, herramientas, generación de vídeo ni prompts especiales. No se proporciona el prompt exacto

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-14.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-14-poster.jpg" alt="Case 14 source video poster" height="360"></a>

[Play case 14 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-14.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-15"></a>
### Case 15: [Investigar a una persona y crear su sitio personal animado](https://x.com/nicky_sap/status/2077857190707429411) (by [@nicky_sap](https://x.com/nicky_sap))

**Da una instrucción amplia para un sitio personal y examina la investigación, planificación, iteración y validación en el navegador del modelo**

El creador informa que Kimi K3 investigó a Nick Saponaro y produjo un sitio web personal animado a partir de una petición amplia, con planificación, pruebas, iteración y comprobaciones en el navegador. El resultado es una demostración de flujo autodeclarada

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-15.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-15-poster.jpg" alt="Case 15 source video poster" height="360"></a>

[Play case 15 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-15.mp4)

Type: Tutorial | Date: 2026-07-16

---

<a id="case-17"></a>
### Case 17: [Generar una simulación de un agujero negro](https://x.com/chetaslua/status/2077961850352971796) (by [@chetaslua](https://x.com/chetaslua))

**Usa una tarea de visualización científica para examinar una simulación generada de un agujero negro**

El creador muestra una simulación de agujero negro atribuida a Kimi K3 y la califica como la mejor que ha visto. La fuente aporta un resultado visible, pero no un prompt, una rúbrica ni validación independiente

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-17.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-17-poster.jpg" alt="Case 17 source video poster" height="360"></a>

[Play case 17 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-17.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-22"></a>
### Case 22: [Probar modelado frontend complejo, partículas y shaders](https://x.com/karminski3/status/2077889959223337099) (by [@karminski3](https://x.com/karminski3))

**Usa un prompt frontend público para examinar en una sola pasada la precisión del modelado, los efectos de partículas y la generación de shaders inline**

El creador informa de un resultado frontend de Kimi K3 en una sola pasada que cubre modelado preciso, efectos de partículas y código shader inline complejo, y afirma que el prompt de prueba es público en la fuente enlazada

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-22.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-22-poster.jpg" alt="Case 22 source video poster" height="360"></a>

[Play case 22 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-22.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-26"></a>
### Case 26: [Generar una herramienta de música procedimental en un intento](https://x.com/mirochill/status/2077723551331758478) (by [@mirochill](https://x.com/mirochill))

**Prueba la generación en un intento de un generador interactivo de música procedimental y compara con cautela el resultado visible**

El creador informa que Kimi K3 generó una herramienta de música procedimental en un intento y la compara favorablemente con resultados de Fable 5 y GPT-5.6 Sol. Se trata del conjunto de pruebas del propio creador, no de un benchmark estandarizado

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-26-poster.jpg" alt="Case 26 source video poster" height="360"></a>

[Play case 26 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-26.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-33"></a>
### Case 33: [Crear una página de producto en Three.js a partir de dos imágenes](https://x.com/1littlecoder/status/2077890296806031665) (by [@1littlecoder](https://x.com/1littlecoder))

**Usa dos imágenes de referencia y un requisito explícito de Three.js para generar una presentación de producto**

El creador informa que Kimi K3 diseñó una página de producto a partir de dos imágenes y produjo la versión solicitada explícitamente en Three.js. No se facilitan más detalles del prompt ni de la implementación

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-33.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-33-poster.jpg" alt="Case 33 source video poster" height="360"></a>

[Play case 33 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-33.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-39"></a>
### Case 39: [Inventar una cortadora de pan de lujo y su página de producto](https://x.com/filicroval/status/2077871090731221438) (by [@filicroval](https://x.com/filicroval))

**Combina la ideación de producto, una vista explotada, una demostración y una landing page en un solo artefacto de diseño**

El creador informa que Kimi K3 inventó una cortadora de pan estilo guillotina, la presentó como producto de lujo y produjo una landing page con vista explotada y demostración

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-39.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-39-poster.jpg" alt="Case 39 source video poster" height="360"></a>

[Play case 39 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-39.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-45"></a>
### Case 45: [Generar un GIF recursivo de diez segundos con un pelícano](https://x.com/1littlecoder/status/2077880380900937865) (by [@1littlecoder](https://x.com/1littlecoder))

**Usa una instrucción completamente especificada de animación en bucle para examinar la continuidad narrativa y la recursión en un GIF**

La fuente incluye un prompt para un GIF en bucle de diez segundos en el que un pelícano monta en bicicleta y recibe por mensaje el mismo vídeo mientras la cámara se acerca. El creador muestra la animación resultante de Kimi K3

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-45.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-45-poster.jpg" alt="Case 45 source video poster" height="360"></a>

[Play case 45 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-45.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-55"></a>
### Case 55: [Generar un SVG lateral de un BMW M4 CS](https://x.com/HarshithLucky3/status/2077765821380886942) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**Usa un vehículo y un punto de vista específicos para examinar el resultado de una ilustración vectorial**

El creador muestra un SVG lateral de un BMW M4 CS atribuido a Kimi K3 Max. La fuente proporcionada contiene el artefacto, pero no el prompt ni los pasos de producción

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-55-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-55-01.jpg" alt="Case 55 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-58"></a>
### Case 58: [Recrear Gargantúa mediante feedback de capturas de pantalla](https://x.com/AngryTomtweets/status/2077868981659324444) (by [@AngryTomtweets](https://x.com/AngryTomtweets))

**Usa capturas repetidas como observaciones para diagnosticar y perfeccionar una visualización científica**

La fuente informa que Kimi K3 recreó Gargantúa de Interstellar mediante 62 capturas de pantalla propias, leyendo cada resultado, diagnosticando problemas y actuando sobre ellos de forma iterativa

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-58.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-58-poster.jpg" alt="Case 58 source video poster" height="360"></a>

[Play case 58 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-58.mp4)

Type: Tutorial | Date: 2026-07-16

---

<a id="case-66"></a>
### Case 66: [Perfeccionar una visualización de agujero negro con 62 capturas](https://x.com/TokenGremlin/status/2077855959201042645) (by [@TokenGremlin](https://x.com/TokenGremlin))

**Usa un bucle de feedback de capturas para leer, diagnosticar y corregir una simulación visual durante muchas iteraciones**

La fuente informa que Kimi K3 reconstruyó Gargantúa de Interstellar observando y perfeccionando su resultado a lo largo de 62 capturas. Esto demuestra el bucle de feedback comunicado, no una verificación independiente de la precisión física

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-66.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-66-poster.jpg" alt="Case 66 source video poster" height="360"></a>

[Play case 66 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-66.mp4)

Type: Tutorial | Date: 2026-07-16

---

<a id="case-68"></a>
### Case 68: [Crear un PDF de marketing sobre post-training](https://x.com/Satvik_Pen/status/2077859673517023313) (by [@Satvik_Pen](https://x.com/Satvik_Pen))

**Usa un producto y un formato de entrega concretos para generar un documento de marketing**

El creador informa que pidió a Kimi K3 un PDF de marketing sobre Inkling, el producto de post-training de Thinking Machines, y comparte el resultado, además de elogiar el proceso interno. No se facilitan el prompt ni criterios de evaluación

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-01.png" alt="Case 68 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-02.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-02.png" alt="Case 68 source image 2" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-03.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-03.png" alt="Case 68 source image 3" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-04.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-04.png" alt="Case 68 source image 4" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-70"></a>
### Case 70: [Crear una interfaz de usuario a partir de un prompt](https://x.com/BrianMRey/status/2077891942088671689) (by [@BrianMRey](https://x.com/BrianMRey))

**Usa una sola petición para generar y examinar un diseño completo de interfaz de usuario**

El creador muestra un diseño de interfaz atribuido a una ejecución de Kimi K3 con un prompt y ofrece una valoración subjetiva muy positiva. No se incluyen el prompt exacto ni una rúbrica

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-70.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-70-poster.jpg" alt="Case 70 source video poster" height="360"></a>

[Play case 70 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-70.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-78"></a>
### Case 78: [Crear un sitio web de estilo premiado](https://x.com/viktoroddy/status/2078140696910037002) (by [@viktoroddy](https://x.com/viktoroddy))

**Evalúa la sesión grabada completa y no solo la captura final**

Viktor Oddy publica un tutorial de 13 minutos para crear con Kimi K3 un sitio web de estilo premiado, aportando evidencia del proceso completo

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-78.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-78-poster.jpg" alt="Case 78 source video poster" height="360"></a>

[Play case 78 tutorial video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-78.mp4)

Type: Tutorial | Date: 2026-07-17

---

<a id="case-81"></a>
### Case 81: [Crear un frontend con metaballs al desplazarse](https://x.com/abhinavflac/status/2078603131055993130) (by [@abhinavflac](https://x.com/abhinavflac))

**Pide a Kimi K3 una página estilo Awwwards con desplazamiento y revisa si los efectos matemáticos pueden reemplazar mallas o texturas pesadas.**

El creador informa una sesión frontend de Kimi K3 que produjo un sitio con metaballs al hacer scroll usando comportamiento visual basado en matemáticas, sin mallas ni texturas. El video adjunto es el artefacto visible; no se publica prompt reutilizable ni pasos de implementación.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-81.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-81-poster.jpg" alt="Case 81 source video poster" height="360"></a>

[Play case 81 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-81.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-82"></a>
### Case 82: [Rediseñar un sitio personal entre modelos](https://x.com/fabriciocarraro/status/2078574831466078265) (by [@fabriciocarraro](https://x.com/fabriciocarraro))

**Ejecuta el mismo brief de rediseño con varios harnesses de código y compara tiempo, dirección visual y ajuste a la identidad existente.**

El creador probó Fable 5, GPT-5.6 Sol y Kimi K3 en el rediseño de su sitio personal con el harness oficial y modo de máximo esfuerzo de cada modelo. Kimi K3 tardó unos 50 minutos, Fable 35 y Sol unos 70; la publicación lo presenta como un mini benchmark específico de la tarea.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-82.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-82-poster.jpg" alt="Case 82 source video poster" height="360"></a>

[Play case 82 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-82.mp4)

Type: Evaluation | Date: 2026-07-18

---

<a id="case-86"></a>
### Case 86: [Crear un explorador interactivo de cuero cabelludo](https://x.com/MiaAI_lab/status/2078508824752017757) (by [@MiaAI_lab](https://x.com/MiaAI_lab))

**Usa Kimi K3 para una escena educativa 3D de una sola pasada con capas anatómicas, cabello responsivo y puntos interactivos.**

El creador reporta que Kimi K3 single-shot un explorador realista de cuero cabelludo usando unas 105k tokens, con iluminación cinematográfica, anatomía por capas, hebras de pelo responsivas, cortes transversales y hotspots educativos. La fuente dice que el resultado fue impresionante pero no barato y enlaza una versión para probar.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-86.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-86-poster.jpg" alt="Case 86 source video poster" height="360"></a>

[Play case 86 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-86.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-87"></a>
### Case 87: [Compartir un prompt de dashboard globo 3D](https://x.com/hqmank/status/2078465403349840144) (by [@hqmank](https://x.com/hqmank))

**Estudia un setup con prompt e imagen de referencia para un dashboard globo 3D de Kimi K3 en vez de inferir el flujo solo por la imagen final.**

El creador responde a solicitudes del prompt y la imagen de referencia detrás de una demo de dashboard globo 3D con Kimi K3 y comparte ambos en imágenes adjuntas. El repositorio registra la fuente como límite de prompt tutorial, pero no transcribe texto desde imágenes.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-87.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-87-poster.jpg" alt="Case 87 source video poster" height="360"></a>

[Play case 87 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-87.mp4)

Type: Tutorial | Date: 2026-07-18

---

<a id="case-94"></a>
### Case 94: [Ejecutar cinco pruebas UI UX](https://x.com/MAXdeg0/status/2078855257686196399) (by [@MAXdeg0](https://x.com/MAXdeg0))

**Evalúa Kimi K3 con varias tareas de UI, logotipo y Figma MCP en lugar de confiar en una sola captura frontend.**

MAXdeg0 informa cinco pruebas de UI/UX y diseño de logotipos con Kimi K3 usando Claude Code y el servidor Figma MCP. La fuente enumera tareas como reconstrucción de landing page, reconstrucción de hero section y trabajo de marca, e incluye tiempo y coste concretos para al menos la landing.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-94.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-94-poster.jpg" alt="Case 94 source video poster" height="360"></a>

[Play case 94 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-94.mp4)

Type: Evaluation | Date: 2026-07-19

---

<a id="case-97"></a>
### Case 97: [Crear landings desde referencias](https://x.com/MAXdeg0/status/2078776969072877715) (by [@MAXdeg0](https://x.com/MAXdeg0))

**Usa tableros de referencia, Figma AI y Motion Sites con Kimi K3 para convertir dirección visual en secciones de landing reutilizables.**

MAXdeg0 describe un flujo para landing pages: obtener referencias de estilo en Pinterest, remezclar el look con Figma AI o pegar una referencia de UI más prompt en Motion Sites para que Kimi K3 construya la página. El post añade que la técnica se reutiliza en más secciones y enlaza una guía de prompts.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-97.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-97-poster.jpg" alt="Case 97 source video poster" height="360"></a>

[Play case 97 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-97.mp4)

Type: Tutorial | Date: 2026-07-19

---

<a id="case-103"></a>
### Case 103: [Seguir un tutorial web premium](https://x.com/_guillecasaus/status/2079258261014908980) (by [@_guillecasaus](https://x.com/_guillecasaus))

**Sigue un tutorial corto en español para usar Kimi K3 en la generación de sitios web con acabado visual premium.**

Guille Casaus comparte un tutorial de 13 minutos para crear páginas web con Kimi K3. El post dice que explica paso a paso cómo usar el modelo para lograr un acabado visual mucho más premium.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-103.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-103-poster.jpg" alt="Case 103 source video poster" height="360"></a>

[Play case 103 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-103.mp4)

Type: Tutorial | Date: 2026-07-20

---

<a id="case-106"></a>
### Case 106: [Comparar costes de frontend humanoide](https://x.com/ChrisGPT/status/2079236298464796958) (by [@ChrisGPT](https://x.com/ChrisGPT))

**Compara Kimi K3 y GPT-5.6 en un prompt general de frontend de robot humanoide usando líneas, tokens y coste.**

ChrisGPT compara GPT-5.6 y Kimi K3 en una web frontend de robot humanoide con un prompt amplio. El post reporta 2.100 LOC y 21K tokens por 0,63 dólares para GPT-5.6, frente a 2.400 LOC y 24K tokens por 0,36 dólares para Kimi K3.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-106.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-106-poster.jpg" alt="Case 106 source video poster" height="360"></a>

[Play case 106 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-106.mp4)

Type: Benchmark | Date: 2026-07-20

---

<a id="case-115"></a>
### Case 115: [Comparar builds Three.js Kimi-vs-GLM](https://x.com/thehypedotnews/status/2079553731218325840) (by [@thehypedotnews](https://x.com/thehypedotnews))

**Ejecuta los mismos prompts procedurales de Three.js con Kimi K3 y GLM 5.2 para comparar comportamiento frontend y 3D.**

The Hype dice que probó Kimi K3 y GLM 5.2 con tres prompts de HTML de un solo archivo y Three.js: una sala ochentera con textura de canvas en un CRT, una bici de ruta con cinemática de transmisión y una escena de acuario de vidrio.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-115.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-115-poster.jpg" alt="Case 115 source video poster" height="360"></a>

[Play case 115 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-115.mp4)

Type: Benchmark | Date: 2026-07-21

---

<a id="case-121"></a>
### Case 121: [Crear landing pages con referencia](https://x.com/Oluwaphilemon1/status/2079951300108697683) (by [@Oluwaphilemon1](https://x.com/Oluwaphilemon1))

**Da a Kimi K3 referencias visuales sólidas y guía iterativa al probar generación de landing pages.**

Oluwaphilemon describe una imagen de referencia y un prompt detallado para una landing page. La fuente señala que Kimi primero intentó crear la bicicleta como modelo 3D y luego mejoró tras varias iteraciones guiadas.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-121.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-121-poster.jpg" alt="Case 121 source video poster" height="360"></a>

[Play case 121 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-121.mp4)

Type: Demo | Date: 2026-07-22

---

<a id="case-128"></a>
### Case 128: [Simular un sistema de partículas 3D](https://x.com/jadeferrara_/status/2079884161251262540) (by [@jadeferrara_](https://x.com/jadeferrara_))

**Usa prompts de simulación de partículas para comparar la calidad de movimiento de Kimi K3 con modelos cerrados.**

Jade Ferrara informa que dio el mismo prompt de sistema de partículas 3D a Kimi K3 y Opus 4.8. La fuente dice que Kimi produjo movimiento más orgánico y menor coste API.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-128.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-128-poster.jpg" alt="Case 128 source video poster" height="360"></a>

[Play case 128 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-128.mp4)

Type: Evaluation | Date: 2026-07-22

---


<a id="coding-integrations"></a>
## 💻 Programación e integraciones

<a id="case-18"></a>
### Case 18: [Crear un MacBook virtual con macOS funcional](https://x.com/scottstts/status/2077890054299541890) (by [@scottstts](https://x.com/scottstts))

**Combina el renderizado de hardware con Three.js y una simulación interactiva de un sistema operativo en el navegador**

La fuente informa que Kimi K3 creó un MacBook virtual en Three.js con un entorno funcional al estilo de macOS. Demuestra el artefacto, pero no aporta los pasos de implementación

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-18.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-18-poster.jpg" alt="Case 18 source video poster" height="360"></a>

[Play case 18 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-18.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-25"></a>
### Case 25: [Crear un compilador GPU desde un DSL hasta PTX](https://x.com/rohanpaul_ai/status/2077886618657231220) (by [@rohanpaul_ai](https://x.com/rohanpaul_ai))

**Usa una tarea de compilador de extremo a extremo que abarque un DSL, las pasadas del compilador, la generación de PTX y una ruta para Tensor Cores**

La fuente informa que Kimi K3 creó desde cero un compilador GPU, desde su DSL y sus pasadas hasta la generación de PTX, y compara su ruta de Tensor Cores con Triton. El registro proporcionado no incluye detalles de un benchmark independiente

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-25-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-25-01.png" alt="Case 25 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-32"></a>
### Case 32: [Crear un raytracer de agujero negro en tiempo real con WebGL2](https://x.com/AlicanKiraz0/status/2077885419744612597) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**Prueba la generación con un prompt de un raytracer geodésico nativo de WebGL2 dentro de un solo archivo HTML**

El autor describe un benchmark de programación que exige un raytracer funcional de desviación de luz por un agujero negro, en un solo archivo y con WebGL2 nativo. El registro proporcionado establece la tarea y los modelos participantes, pero no una auditoría independiente completa del resultado

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-32.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-32-poster.jpg" alt="Case 32 source video poster" height="360"></a>

[Play case 32 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-32.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-46"></a>
### Case 46: [Crear un emulador de Game Boy Advance basado en mGBA WASM](https://x.com/teortaxesTex/status/2077925090168062272) (by [@teortaxesTex](https://x.com/teortaxesTex))

**Integra un modelo 3D con licencia y un núcleo de emulación real, y mejora recursivamente la interfaz y la experiencia de juego**

El proyecto citado de Kimi K3 adapta un modelo AGB-001 con licencia, integra un núcleo mGBA WASM y mejora la interfaz y el juego mediante autooptimización recursiva. La publicación cita la descripción del proyecto, no una reproducción independiente

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-46-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-46-01.jpg" alt="Case 46 source image 1" height="360"></a>

Type: Integration | Date: 2026-07-17

---

<a id="case-50"></a>
### Case 50: [Investigar varios temas con fuentes en chino](https://x.com/tphuang/status/2077911994607239400) (by [@tphuang](https://x.com/tphuang))

**Usa tareas de investigación prolongadas para comparar exhaustividad y latencia entre generaciones de modelos**

El autor informa que probó Kimi K3 en numerosos temas de investigación con fuentes en chino, y lo encontró más exhaustivo que K2.6, aunque más lento. La publicación también señala una fuerte demanda del servicio en ese momento

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-50-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-50-01.png" alt="Case 50 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-17

---

<a id="case-56"></a>
### Case 56: [Clonar macOS en el navegador con aplicaciones funcionales](https://x.com/twid/status/2077924755357974989) (by [@twid](https://x.com/twid))

**Crea una simulación de sistema operativo en el navegador que incluya aplicaciones de música, navegador y correo electrónico**

La fuente informa que se usó Kimi K3 para crear un clon de macOS en el navegador con música, navegador, correo electrónico y otras funciones. No proporciona detalles de implementación

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-56.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-56-poster.jpg" alt="Case 56 source video poster" height="360"></a>

[Play case 56 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-56.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-62"></a>
### Case 62: [Crear una simulación de macOS con FaceTime funcional](https://x.com/LinearUncle/status/2077919552239997078) (by [@LinearUncle](https://x.com/LinearUncle))

**Usa una tarea de sistema operativo virtual para comprobar si funciona la interacción de una aplicación generada**

El creador muestra un entorno al estilo de macOS atribuido a Kimi K3 e informa que su función FaceTime funciona. La fuente no proporciona pasos de configuración ni validación

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-62-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-62-01.jpg" alt="Case 62 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-17

---

<a id="case-64"></a>
### Case 64: [Añadir un comparador frontend de dos tareas](https://x.com/MinLiBuilds/status/2077939461510615376) (by [@MinLiBuilds](https://x.com/MinLiBuilds))

**Crea una herramienta que seleccione dos tareas completadas, las muestre lado a lado y sincronice vistas e interacciones**

El creador informa que pidió a Kimi K3 añadir un flujo de comparación frontend con selección de tareas, dos paneles de navegador, modos de objetos y recorrido, puntos de vista sincronizados y pruebas de interacción. La publicación también señala limitaciones más amplias del modelo

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-64.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-64-poster.jpg" alt="Case 64 source video poster" height="360"></a>

[Play case 64 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-64.mp4)

Type: Tutorial | Date: 2026-07-17

---

<a id="case-75"></a>
### Case 75: [Configurar Kimi como subagente de Codex](https://x.com/nauczymycieAI/status/2078181182701736132) (by [@nauczymycieAI](https://x.com/nauczymycieAI))

**Mantén la orquestación en Codex y delega el frontend a un subagente Kimi K3 OpenCode con un límite claro para secretos**

nauczymycieAI explica cómo instalar y verificar OpenCode, crear manualmente una clave Kimi sin pegarla en Codex, conectar Kimi K3 y crear un skill global de Codex para enrutar tareas frontend

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-75.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-75.jpg" alt="Case 75 source image 1" height="360"></a>

Type: Tutorial | Date: 2026-07-17

---

<a id="case-79"></a>
### Case 79: [Enrutar código simple mediante ChatLLM](https://x.com/abacusai/status/2078022418661257411) (by [@abacusai](https://x.com/abacusai))

**Envía código simple a Kimi K3 y reserva el código difícil y el diseño para otros modelos**

Abacus AI anuncia Kimi K3 en ChatLLM: código simple con Kimi K3, código difícil con Fable 5 y diseño con GPT-5.6 Sol. El router sirve en ChatLLM, Abacus AI Agent y Claude Code

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-79.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-79.jpg" alt="Case 79 source image 1" height="360"></a>

Type: Integration | Date: 2026-07-17

---

<a id="case-91"></a>
### Case 91: [Crear CS con recursos generados](https://x.com/karankendre/status/2078938615900688728) (by [@karankendre](https://x.com/karankendre))

**Combina Kimi K3 para el código del juego con GPT Image 2 para los recursos al prototipar un pequeño juego estilo Counter-Strike en navegador.**

Karan Kendre informa que usó Kimi K3 para construir el juego y GPT Image 2 para crear los recursos de un proyecto estilo Counter-Strike, con un coste total aproximado de 10 dólares. El video fuente es el artefacto visible, por lo que el registro sirve como flujo de combinación de herramientas más que como benchmark exclusivo de Kimi.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-91.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-91-poster.jpg" alt="Case 91 source video poster" height="360"></a>

[Play case 91 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-91.mp4)

Type: Integration | Date: 2026-07-19

---

<a id="case-95"></a>
### Case 95: [Usar la skill Design de Command Code](https://x.com/MrAhmadAwais/status/2078841789205934547) (by [@MrAhmadAwais](https://x.com/MrAhmadAwais))

**Combina Kimi K3 con una skill de diseño dedicada en Command Code al crear un prototipo visual de juego con presupuesto de tokens.**

Ahmad Awais informa usar Kimi K3 con Command Code y su skill /design para un juego con cámara de persecución estilo Forza. El post dice que la sesión costó 0,97 dólares e incluyó correcciones de escala de carretera y coche, fondo, animación y niebla, por lo que es un flujo concreto de harness de agente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-95.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-95-poster.jpg" alt="Case 95 source video poster" height="360"></a>

[Play case 95 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-95.mp4)

Type: Integration | Date: 2026-07-19

---

<a id="case-109"></a>
### Case 109: [Ejecutar Kimi K3 en Claude Code](https://x.com/boxmining/status/2079115758618239337) (by [@boxmining](https://x.com/boxmining))

**Conecta Kimi K3 a Claude Code con un VPS para mantener el flujo de coding y cambiar el backend del modelo.**

Boxmining comparte una guía de setup para ejecutar Kimi K3 dentro de Claude Code. El post describe Claude Code como harness de programación y Kimi K3 en un VPS 24/7 para loops, subagents y workflows de coding de mayor rendimiento.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-109.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-109-poster.jpg" alt="Case 109 source video poster" height="360"></a>

[Play case 109 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-109.mp4)

Type: Integration | Date: 2026-07-20

---

<a id="case-119"></a>
### Case 119: [Enrutar Kimi con claude-code-router](https://x.com/sairahul1/status/2079393675885588855) (by [@sairahul1](https://x.com/sairahul1))

**Prueba Kimi K3 en un flujo existente de Claude Code mediante claude-code-router evitando el modo proxy innecesario.**

Sai Rahul describe soporte patrocinado por Moonshot para Kimi K3 en claude-code-router, con presets integrados, importación de API key o suscripción, enrutamiento nativo de suscripción, balance y uso en dashboard, failover, precios de caché y una advertencia para dejar el modo proxy apagado salvo que haga falta.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-119.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-119-poster.jpg" alt="Case 119 source video poster" height="360"></a>

[Play case 119 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-119.mp4)

Type: Integration | Date: 2026-07-21

---

<a id="case-125"></a>
### Case 125: [Ejecutar un harness de agentes abierto](https://x.com/ShenSeanChen/status/2079914609222221976) (by [@ShenSeanChen](https://x.com/ShenSeanChen))

**Usa un harness de agentes compartido para comparar Kimi K3 con otros modelos frontera en tareas con herramientas.**

Sean Chen describe una carrera de Kimi K3 contra varios modelos en un harness abierto con bucle de agente, recuperación de memoria, llamadas a herramientas, evaluación, trazas y panel de coste.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-125.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-125-poster.jpg" alt="Case 125 source video poster" height="360"></a>

[Play case 125 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-125.mp4)

Type: Benchmark | Date: 2026-07-22

---

<a id="case-129"></a>
### Case 129: [Ejecutar Kimi en Codex OAuth](https://x.com/biscuitweb3/status/2079844959843197342) (by [@biscuitweb3](https://x.com/biscuitweb3))

**Usa la ruta OAuth de Codex cuando un flujo de programación con Kimi K3 deba evitar configurar una clave API manual.**

biscuitweb3 informa que Kimi K3 funciona dentro de Codex mediante OAuth sin configuración adicional de API key. La captura adjunta aporta evidencia de la integración.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-129-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-129-01.jpg" alt="Case 129 source image 1" height="360"></a>

Type: Integration | Date: 2026-07-22

---


<a id="evaluation-limits"></a>
## 🧪 Evaluación y límites

<a id="case-7"></a>
### Case 7: [Comparar el diseño frontend en la tarea de lámpara de lava de BridgeBench](https://x.com/bridgemindai/status/2077868061953007908) (by [@bridgemindai](https://x.com/bridgemindai))

**Usa la tarea de lámpara de lava de BridgeBench como una comparación acotada de diseño frontend, no como una clasificación universal**

BridgeMind AI informa que Kimi K3 superó a Fable 5 en su tarea de lámpara de lava de BridgeBench y quedó primero en la arena citada. Estos son los resultados comparativos comunicados por el editor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-07.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-07-poster.jpg" alt="Case 7 source video poster" height="360"></a>

[Play case 7 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-07.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-8"></a>
### Case 8: [Evaluar la escritura de guiones con voz editorial](https://x.com/Whats_AI/status/2077860441380798908) (by [@Whats_AI](https://x.com/Whats_AI))

**Mide el ajuste a la voz editorial, la posición relativa y el coste por guion dentro de un benchmark interno claramente identificado**

Whats_AI comunica resultados internos preliminares de 2.840 Elo, primer puesto en su tabla y unos 0,25 USD por guion. Deben tratarse como el benchmark preliminar de una organización, no como garantía general de rendimiento o precio

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-08-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-08-01.jpg" alt="Case 8 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-16

---

<a id="case-10"></a>
### Case 10: [Comparar diseño, coste y dificultad en un juego tipo Flappy](https://x.com/MrAhmadAwais/status/2077915347974557862) (by [@MrAhmadAwais](https://x.com/MrAhmadAwais))

**Registra los ajustes de dificultad, el coste, el diseño y las funciones de juego al comparar juegos generados**

El benchmark interno de Flappy de Command Code informa de distintos ajustes de dificultad entre modelos y asigna 0,024 USD a Kimi K3, 0,42 USD a Fable 5 y 0,15 USD a GPT-5.6 Sol. La desigualdad de ajustes limita el alcance de esta comparación interna

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-10.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-10-poster.jpg" alt="Case 10 source video poster" height="360"></a>

[Play case 10 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-10.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-12"></a>
### Case 12: [Comparar el diseño de juegos con el mismo prompt](https://x.com/CommandCodeAI/status/2077921526213746948) (by [@CommandCodeAI](https://x.com/CommandCodeAI))

**Mantén constante el prompt de diseño y examina por separado el ritmo, el criterio de diseño y las sensaciones de juego**

Command Code informa de una comparación con el mismo prompt entre Kimi K3, GPT-5.6 Sol y Fable 5. Su publicación afirma que Kimi K3 rindió bien en criterio de diseño mientras que los otros dos jugaban demasiado rápido; sigue siendo la evaluación del editor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-12.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-12-poster.jpg" alt="Case 12 source video poster" height="360"></a>

[Play case 12 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-12.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-13"></a>
### Case 13: [Exigir una revisión independiente en auditorías estadísticas](https://x.com/emollick/status/2077869293031624793) (by [@emollick](https://x.com/emollick))

**Complementa las auditorías estadísticas generadas por el modelo con una revisión independiente de expertos u otros modelos antes de confiar en sus hallazgos**

Ethan Mollick informa que Kimi K3 Max aplicó incorrectamente la estadística al auditar trabajos académicos previos y coincide con una crítica separada. Este ejemplo negativo respalda la comprobación independiente en lugar de la aceptación sin revisión

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-13-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-13-01.jpg" alt="Case 13 source image 1" height="360"></a>

Type: Limit | Date: 2026-07-16

---

<a id="case-16"></a>
### Case 16: [Evaluar una ejecución frontend lenta pero sólida](https://x.com/Lentils80/status/2077387333154857151) (by [@Lentils80](https://x.com/Lentils80))

**Registra el tiempo de finalización junto con la calidad del resultado al probar una tarea frontend**

El creador informa que una ejecución frontend de Kimi K3 tardó 35 minutos y describe el resultado como uno de los mejores que ha visto para ese prompt. Tanto la velocidad como la calidad son observaciones de un solo usuario

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-16.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-16-poster.jpg" alt="Case 16 source video poster" height="360"></a>

[Play case 16 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-16.mp4)

Type: Evaluation | Date: 2026-07-15

---

<a id="case-20"></a>
### Case 20: [Probar la escritura de misterio para detectar fallos de presagio](https://x.com/emollick/status/2077951790868238616) (by [@emollick](https://x.com/emollick))

**Evalúa si un misterio generado equilibra las pistas, la sutileza y el presagio narrativo**

Ethan Mollick informa que Kimi K3 no escribió un buen misterio de asesinato, pues hizo las pistas a la vez demasiado obvias y demasiado oscuras y falló en el presagio. También señala que otros modelos comparten esta limitación

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-01.jpg" alt="Case 20 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-02.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-02.png" alt="Case 20 source image 2" height="360"></a>

Type: Limit | Date: 2026-07-17

---

<a id="case-21"></a>
### Case 21: [Comparar el modelado y la animación del Halcón Milenario](https://x.com/gmi_cloud/status/2077903360263676090) (by [@gmi_cloud](https://x.com/gmi_cloud))

**Usa peticiones de estilo y ajustes de esfuerzo equivalentes para comparar modelado 3D, animación, tiempo y coste**

GMI Cloud informa de una comparación entre Kimi K3 y Fable 5 al recrear el Halcón Milenario en estilo pixelado y original con esfuerzo máximo. Afirma que Kimi K3 tardó más, pero costó alrededor de un tercio en la primera prueba y menos de la mitad en otra; son resultados comunicados por el proveedor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-21.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-21-poster.jpg" alt="Case 21 source video poster" height="360"></a>

[Play case 21 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-21.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-28"></a>
### Case 28: [Revisar una colección de diez proyectos de Kimi K3](https://x.com/minchoi/status/2077957907857994006) (by [@minchoi](https://x.com/minchoi))

**Usa una recopilación enlazada de proyectos para descubrir artefactos concretos que deban verificarse por separado**

El autor selecciona diez ejemplos de Kimi K3 con material multimedia, incluido un emulador de Game Boy Advance. Este registro es una colección y no un único flujo reproducible, por lo que cada ejemplo enlazado debe comprobarse de forma independiente

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-28.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-28-poster.jpg" alt="Case 28 source video poster" height="360"></a>

[Play case 28 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-28.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-29"></a>
### Case 29: [Comparar una landing page avanzada entre cuatro modelos](https://x.com/doutorcaleb/status/2077904020471947773) (by [@doutorcaleb](https://x.com/doutorcaleb))

**Mantén constante la petición de la landing page y examina la profundidad de las animaciones y el grado de finalización de los resultados**

El creador informa que dio el mismo prompt de landing page avanzada a Kimi K3, Fable, Grok y GPT Terra, y considera que Kimi K3 produjo el resultado más sólido. Es una comparación autodeclarada de una sola tarea

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-29.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-29-poster.jpg" alt="Case 29 source video poster" height="360"></a>

[Play case 29 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-29.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-30"></a>
### Case 30: [Evaluar mecánicas y costes de juegos retro](https://x.com/adxtyahq/status/2077860500462055570) (by [@adxtyahq](https://x.com/adxtyahq))

**Compara jugabilidad, físicas, mecánicas, comportamiento autónomo, uso de tokens y coste en las mismas tareas de juegos retro**

La fuente informa de pruebas con el mismo prompt para Road Fighter, Battle City y Q*bert y enumera 0,28 USD para Kimi K3, 0,28 USD para GPT-5.6 y 0,54 USD para Opus 4.8. Estas cifras pertenecen al benchmark del editor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-30.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-30-poster.jpg" alt="Case 30 source video poster" height="360"></a>

[Play case 30 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-30.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-31"></a>
### Case 31: [Comparar la generación de juegos con Fable 5](https://x.com/higgsfield_ai/status/2077943629633712490) (by [@higgsfield_ai](https://x.com/higgsfield_ai))

**Usa un ejemplo de juegos generados lado a lado como evaluación acotada, no como veredicto general sobre los modelos**

Higgsfield presenta una comparación de generación de juegos entre Kimi K3 y Fable 5. El registro proporcionado incluye el material comparativo, pero no el prompt, una rúbrica de puntuación ni las condiciones detalladas

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-31.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-31-poster.jpg" alt="Case 31 source video poster" height="360"></a>

[Play case 31 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-31.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-34"></a>
### Case 34: [Comparar tareas complejas de frontend y desarrollo con Opus 4.8](https://x.com/op7418/status/2077969583018066116) (by [@op7418](https://x.com/op7418))

**Usa varias tareas complejas de programación para identificar victorias y derrotas en lugar de declarar que un modelo es universalmente superior**

El evaluador informa de pruebas directas entre Kimi K3 y Opus 4.8 y considera que son aproximadamente comparables en tareas complejas de frontend y desarrollo, con resultados mixtos. Sigue siendo la valoración de un solo evaluador

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-34.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-34-poster.jpg" alt="Case 34 source video poster" height="360"></a>

[Play case 34 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-34.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-35"></a>
### Case 35: [Revisar benchmarks y una prueba de landing page](https://x.com/adamuchigabriel/status/2077880433925120471) (by [@adamuchigabriel](https://x.com/adamuchigabriel))

**Combina el contexto de benchmarks con una prueba concreta de generación de landing pages, manteniendo separados ambos tipos de evidencia**

El vídeo presenta una discusión de benchmarks, una prueba de landing page y observaciones sobre diseño frontend con Kimi K3. El registro proporcionado no incluye el prompt de prueba completo ni una rúbrica de puntuación

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-35.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-35-poster.jpg" alt="Case 35 source video poster" height="360"></a>

[Play case 35 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-35.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-37"></a>
### Case 37: [Evaluar el razonamiento inductivo con tareas de grafos a fórmulas](https://x.com/s_batzoglou/status/2077884096307454119) (by [@s_batzoglou](https://x.com/s_batzoglou))

**Mide la corrección, el comportamiento en holdout y la complejidad de las fórmulas en tareas de inducción de primer orden**

El autor informa de un benchmark de Kimi K3 y otros modelos en la tarea INDUCTION de ICML, usando entre 6 y 10 grafos pequeños de entre 8 y 10 elementos cada uno para inferir una fórmula de primer orden. La publicación afirma que los resultados se actualizaron respecto a trabajos anteriores; aquí no se alega una nueva reproducción independiente

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-37-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-37-01.png" alt="Case 37 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-16

---

<a id="case-38"></a>
### Case 38: [Revisar informes sobre juegos, landing pages, trabajo 3D y contexto largo](https://x.com/servasyy_ai/status/2077903775113834689) (by [@servasyy_ai](https://x.com/servasyy_ai))

**Usa una recopilación de múltiples fuentes para comparar artefactos concretos y señalar las limitaciones de velocidad junto con las afirmaciones de coste**

El autor resume pruebas comunicadas de Kimi K3 en juegos, landing pages, generación 3D y trabajo con contexto largo, y concluye que merece la pena probarlo, pero todavía no sustituye a Fable 5. Todas las cifras son informes secundarios dentro de esta recopilación

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-38-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-38-01.jpg" alt="Case 38 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-40"></a>
### Case 40: [Auditar un plan complejo y cuestionar sus soluciones](https://x.com/doodlestein/status/2077901883637665958) (by [@doodlestein](https://x.com/doodlestein))

**Usa un segundo modelo para identificar hallazgos minimizados, soluciones incorrectas y conclusiones que deberían rechazarse**

El creador informa que Kimi K3 revisó un plan muy refinado y detectó que se habían minimizado problemas graves, que cerca de un tercio de las soluciones propuestas requería corrección y que un hallazgo fue refutado. Son resultados de esa auditoría concreta

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-40-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-40-01.jpg" alt="Case 40 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-41"></a>
### Case 41: [Comparar diagramas ASCII de aprendizaje por refuerzo al estilo PPO](https://x.com/dejavucoder/status/2077872015856615541) (by [@dejavucoder](https://x.com/dejavucoder))

**Mantén constante el prompt del diagrama ASCII y compara cómo representan los modelos el ciclo de aprendizaje por refuerzo**

La fuente proporciona el prompt para dibujar en ASCII un ciclo de aprendizaje por refuerzo al estilo PPO y muestra Kimi K3 Max junto a Fable 5 High. La valoración sigue siendo una comparación visual de una sola tarea

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-01.png" alt="Case 41 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-02.jpg" alt="Case 41 source image 2" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-42"></a>
### Case 42: [Modelar en Blender mientras se registran errores de capacidad](https://x.com/Angaisb_/status/2077910845523214668) (by [@Angaisb_](https://x.com/Angaisb_))

**Evalúa el progreso parcial en Blender junto con la fiabilidad del servicio, no solo el artefacto**

El creador muestra avances de modelado en Blender con Kimi K3 y también informa de errores de capacidad repetidos. El trabajo está incompleto en la fuente proporcionada, por lo que deben considerarse conjuntamente el resultado parcial y la limitación de fiabilidad

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-42-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-42-01.jpg" alt="Case 42 source image 1" height="360"></a>

Type: Limit | Date: 2026-07-17

---

<a id="case-47"></a>
### Case 47: [Comparar la generación de Flappy Bird en una arena](https://x.com/jun_song/status/2077396996865003739) (by [@jun_song](https://x.com/jun_song))

**Usa una tarea de arena para comparar dos resultados generados de Flappy Bird, manteniendo el juicio limitado a esa tarea**

El creador informa de una comparación en Arena entre Kimi K3 y Opus 4.8 con una tarea de Flappy Bird y considera que Kimi K3 fue significativamente mejor. El registro no aporta el prompt completo ni una rúbrica

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-47.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-47-poster.jpg" alt="Case 47 source video poster" height="360"></a>

[Play case 47 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-47.mp4)

Type: Evaluation | Date: 2026-07-15

---

<a id="case-52"></a>
### Case 52: [Resolver con una herramienta un problema de inducción visual de Bongard](https://x.com/IntuitMachine/status/2077885406528311561) (by [@IntuitMachine](https://x.com/IntuitMachine))

**Comprueba si el uso de herramientas ayuda a deducir la regla visual en una tarea de razonamiento de Bongard**

El creador informa que Kimi K3 usó una herramienta para resolver un problema de Bongard que Grok 4.5 y Muse Spark 1.1 no resolvieron en la misma comparación. Es el resultado de la tarea de un usuario, no un benchmark general de razonamiento

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-52-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-52-01.jpg" alt="Case 52 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-53"></a>
### Case 53: [Comparar el gusto frontend y el diseño 3D con GPT-5.6 Sol](https://x.com/filicroval/status/2077736407506751952) (by [@filicroval](https://x.com/filicroval))

**Examina funciones, gusto visual, elegancia y ejecución 3D en una comparación frontend acotada**

El creador compara Kimi K3 y GPT-5.6 Sol en diseño frontend y considera a Kimi K3 más sólido en gusto visual, elegancia y capacidad 3D. La valoración es subjetiva y específica de la tarea

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-53.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-53-poster.jpg" alt="Case 53 source video poster" height="360"></a>

[Play case 53 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-53.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-57"></a>
### Case 57: [Comparar la generación de sitios web entre tres modelos](https://x.com/pengchujin/status/2077962916226298340) (by [@pengchujin](https://x.com/pengchujin))

**Usa resultados visibles de sitios web para comparar Kimi K3, Fable 5 y GPT-5.6 Sol en una prueba**

El creador presenta una comparación de generación de sitios web entre Kimi K3, Fable 5 y GPT-5.6 Sol. El registro proporcionado no expone el prompt completo ni una rúbrica de puntuación

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-57.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-57-poster.jpg" alt="Case 57 source video poster" height="360"></a>

[Play case 57 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-57.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-59"></a>
### Case 59: [Comparar la generación y el coste de juegos 3D procedimentales](https://x.com/adxtyahq/status/2077958193511362856) (by [@adxtyahq](https://x.com/adxtyahq))

**Mantén constante el prompt entre modelos y examina sistemas generados de ruleta, tragaperras y pinball junto con el coste por ejecución**

El editor informa de una comparación multimodelo de juegos 3D procedimentales y enumera costes que incluyen 0,71 USD para Kimi K3 y 0,30 USD para Grok 4.5. Todas las clasificaciones y costes deben tratarse como resultados de la ejecución de ese editor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-59.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-59-poster.jpg" alt="Case 59 source video poster" height="360"></a>

[Play case 59 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-59.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-69"></a>
### Case 69: [Comparar el detalle y la iluminación de una escena 3D de arsenal](https://x.com/hakki_alkan/status/2077887013332636032) (by [@hakki_alkan](https://x.com/hakki_alkan))

**Examina la densidad de objetos, la iluminación y el detalle de la escena en una comparación acotada entre Kimi K3 y Opus 4.8**

La fuente informa que Kimi K3 produjo una escena de arsenal detallada con estantes abastecidos, cajas e iluminación realista, mientras que Opus 4.8 produjo una habitación vacía. Es un informe comparativo de terceros, no un benchmark independiente

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-69-poster.jpg" alt="Case 69 source video poster" height="360"></a>

[Play case 69 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-69.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-72"></a>
### Case 72: [Comparar frontends con prompts Arena idénticos](https://x.com/arena/status/2078240399517524365) (by [@arena](https://x.com/arena))

**Usa prompts idénticos y resultados paralelos en lugar de depender de una sola posición en el ranking**

Arena.ai publica una comparación de Kimi K3 y Fable 5 en Frontend Code Arena con prompts idénticos. El video conserva ambos resultados bajo la misma condición

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-72.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-72-poster.jpg" alt="Case 72 source video poster" height="360"></a>

[Play case 72 comparison video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-72.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-74"></a>
### Case 74: [Evaluar Kimi Code con agentes de código](https://x.com/ArtificialAnlys/status/2078230240766345330) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Evalúa Kimi K3 con varias pruebas y coste por tarea sin generalizar un único ranking frontend**

Artificial Analysis informa de 57 puntos y quinto puesto conjunto: 84 % en Terminal-Bench v2, 64 % en DeepSWE, 23 % en SWE-Atlas-QnA y 3,18 dólares de coste medio por tarea

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-74.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-74.jpg" alt="Case 74 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-17

---

<a id="case-76"></a>
### Case 76: [Comparar Arena y el arnés de reparación](https://x.com/AlphaSignalAI/status/2078172629496746183) (by [@AlphaSignalAI](https://x.com/AlphaSignalAI))

**Mira tanto preferencia frontend como reparación de repositorios porque Kimi K3 puede quedar primero en una y séptimo en otra**

AlphaSignal informa del primer puesto con 1679 puntos en Frontend Code Arena, pero de 53 aciertos en 67 intentos, 79 %, y séptimo puesto en un arnés de reparación de agentes

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-76.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-76.jpg" alt="Case 76 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-17

---

<a id="case-80"></a>
### Case 80: [Evaluar Kimi K3 en Prinzbench](https://x.com/deredleritt3r/status/2078606700496773166) (by [@deredleritt3r](https://x.com/deredleritt3r))

**Usa una actualización independiente de benchmark para comparar Kimi K3 con modelos abiertos y frontera en búsqueda, razonamiento y consistencia.**

El autor agrega Kimi K3 a Prinzbench y reporta 47/99, por encima de GLM-5.2 con 30/99 y cerca de un resultado antiguo de Gemini 3.1 Pro con 50/99. La publicación destaca buena búsqueda, razonamiento lógico más débil y más inconsistencia que modelos frontera comparables.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-80-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-80-01.png" alt="Case 80 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-18

---

<a id="case-85"></a>
### Case 85: [Comparar generación de un gemelo digital ISS](https://x.com/AIsaOneHQ/status/2078519527588200536) (by [@AIsaOneHQ](https://x.com/AIsaOneHQ))

**Usa un reto 3D con el mismo prompt para comparar Kimi K3 y GPT-5.6 Sol en reconstrucción, controles, etiquetas y detalle visual.**

AIsaOneHQ reporta un benchmark one-shot donde ambos modelos debían reconstruir un gemelo digital interactivo de la Estación Espacial Internacional sin modelo preconstruido, con Tierra, luz orbital, controles, etiquetas, visitas guiadas, vista explotada, pruebas y refinamiento. La publicación dice que Kimi K3 terminó más rápido, costó menos y logró mejor render en esa ejecución.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-85.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-85-poster.jpg" alt="Case 85 source video poster" height="360"></a>

[Play case 85 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-85.mp4)

Type: Benchmark | Date: 2026-07-18

---

<a id="case-89"></a>
### Case 89: [Revisar un mundo forestal WebGPU](https://x.com/stas_sorokin_/status/2078435840728908093) (by [@stas_sorokin_](https://x.com/stas_sorokin_))

**Evalúa Kimi K3 como cerebro de agente de código en una construcción larga con Three.js y WebGPU, incluyendo calidad, velocidad, consistencia y tasa de edición.**

El creador reporta una revisión profunda de Kimi K3 con un mundo de lago y bosque en Three.js y WebGPU, con agua viva, clima, fauna, ciclos día-noche y cámaras cinematográficas. La publicación dice que Kimi K3 produjo alta calidad, fue más lento que una generación comparable con GPT-5.6 Sol, mantuvo consistencia y solo necesitó un ajuste manual de luminosidad.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-89.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-89-poster.jpg" alt="Case 89 source video poster" height="360"></a>

[Play case 89 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-89.mp4)

Type: Evaluation | Date: 2026-07-18

---

<a id="case-90"></a>
### Case 90: [Comparar prompts de casa de cristal](https://x.com/RoundtableSpace/status/2079004612070416755) (by [@RoundtableSpace](https://x.com/RoundtableSpace))

**Usa una escena arquitectónica con el mismo prompt para comparar Kimi K3 y Opus 4.8 en atmósfera, iluminación y completitud espacial.**

Roundtable Space informa una comparación con el mismo prompt entre Kimi K3 y Claude Opus 4.8 a un precio parecido. El resultado de Kimi se describe como una casa de cristal en hora azul con luz interior cálida, piscina reflectante y detalles de planos, mientras que Opus queda como una salida más tipográfica y menos espacial.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-90.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-90-poster.jpg" alt="Case 90 source video poster" height="360"></a>

[Play case 90 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-90.mp4)

Type: Evaluation | Date: 2026-07-20

---

<a id="case-92"></a>
### Case 92: [Evaluar un gol de fútbol vóxel](https://x.com/0xzynex/status/2078920667542487230) (by [@0xzynex](https://x.com/0xzynex))

**Ejecuta el mismo prompt de animación de fútbol en HTML/CSS/JS puro en dos modelos para comparar calidad de movimiento y coste.**

0xzynex informa una comparación de una sola ejecución, sin reintentos, donde Kimi K3 y GPT-5.6 Sol High debían crear una jugada de fútbol en bloques con regate, gol, cámara dinámica y celebración en código de navegador. El post dice que Kimi produjo un movimiento más fluido y menor coste, y el video conserva el artefacto comparativo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-92.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-92-poster.jpg" alt="Case 92 source video poster" height="360"></a>

[Play case 92 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-92.mp4)

Type: Benchmark | Date: 2026-07-19

---

<a id="case-93"></a>
### Case 93: [Revisar una prueba Minecraft](https://x.com/ashen_one/status/2078892418976666071) (by [@ashen_one](https://x.com/ashen_one))

**Mira una revisión estructurada de Minecraft antes de tratar la publicidad de lanzamiento o el precio como evidencia suficiente.**

ashen_one publica una revisión grabada de Kimi K3 con capítulos sobre expectativa frente a realidad, benchmarks, precios, una prueba de Minecraft, errores de primera ejecución y veredicto final. La fuente es útil porque combina benchmark y notas tempranas de fiabilidad en un video inspeccionable.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-93.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-93-poster.jpg" alt="Case 93 source video poster" height="360"></a>

[Play case 93 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-93.mp4)

Type: Benchmark | Date: 2026-07-19

---

<a id="case-98"></a>
### Case 98: [Medir límites de nivel API](https://x.com/mnmn94253156337/status/2078739859154620497) (by [@mnmn94253156337](https://x.com/mnmn94253156337))

**Planifica ejecuciones de agente con Kimi K3 según tokens, nivel, TPM y TPD, no solo por el precio principal del modelo.**

La fuente en chino informa una prueba personal de la API de Kimi K3 tras cargar 5 dólares, con alrededor de 1,1 dólares consumidos durante la preparación y posterior límite Tier0. Enumera precios de entrada, entrada cacheada y salida, además de conceptos de límite como TPM y TPD, por lo que funciona como reporte temprano de limitación.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-98.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-98-poster.jpg" alt="Case 98 source video poster" height="360"></a>

[Play case 98 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-98.mp4)

Type: Limit | Date: 2026-07-19

---

<a id="case-99"></a>
### Case 99: [Comparar un demo estilo Limbo](https://x.com/ChrisGPT/status/2078679211116835017) (by [@ChrisGPT](https://x.com/ChrisGPT))

**Compara alcance jugable, pulido, coste y fallos al probar Kimi K3 frente a Fable 5 en el mismo prototipo de juego.**

ChrisGPT compara Fable 5 y Kimi K3 en un demo tipo Limbo. El post reporta 2.400 líneas y 24K tokens de salida por 1,20 dólares para Fable, frente a 3.000 líneas y 30K tokens por 0,12 dólares para Kimi, con más gameplay añadido pero también más errores.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-99.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-99-poster.jpg" alt="Case 99 source video poster" height="360"></a>

[Play case 99 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-99.mp4)

Type: Benchmark | Date: 2026-07-19

---

<a id="case-100"></a>
### Case 100: [Revisar costes de VulcanBench](https://x.com/morganlinton/status/2079358902194569357) (by [@morganlinton](https://x.com/morganlinton))

**Usa los resultados de VulcanBench para comparar precisión, coste y evidencia abierta de Kimi K3 antes de elegir un modelo de producción.**

Morgan Linton comparte una tabla de VulcanBench y dice que el desglose, la suite de evaluación y el código del benchmark están disponibles públicamente. El post informa que Grok 4.5 ganó en precisión y coste, mientras Kimi K3 resultó caro en este benchmark pese a sus menores precios por token.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-100-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-100-01.jpg" alt="Case 100 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-21

---

<a id="case-104"></a>
### Case 104: [Evaluar física de doble péndulo](https://x.com/AlicanKiraz0/status/2079241239736504768) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**Evalúa Kimi K3 con una simulación de doble péndulo usando coste por iteración, puntuaciones de juez y criterios físicos.**

Alican Kiraz compara Qwen3.6-35B y Kimi-K3 en una tarea de doble péndulo con OpenCode juzgada por ChatGPT 5.6 Pro. El post reporta 3 iteraciones y 0,59 dólares para Kimi, 90,6/100 puntos y ventaja en arquitectura física, caos, trails, rendimiento largo y riesgo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-104.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-104-poster.jpg" alt="Case 104 source video poster" height="360"></a>

[Play case 104 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-104.mp4)

Type: Benchmark | Date: 2026-07-20

---

<a id="case-107"></a>
### Case 107: [Revisar preparación en ReactBench](https://x.com/aidenybai/status/2079233934693650567) (by [@aidenybai](https://x.com/aidenybai))

**Usa ReactBench para juzgar dónde Kimi K3 es más barato y fuerte que Opus 4.8, pero aún detrás de los modelos frontera en frontend de producción.**

Aiden Bai informa que Kimi K3 ocupa el puesto 6 en ReactBench, supera a Opus 4.8 con más de 2x de ahorro y sube 10 puntos frente a K2.7. El mismo post aclara que sigue por detrás de Fable y Sol en preparación de frontend de producción.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-107.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-107-poster.jpg" alt="Case 107 source video poster" height="360"></a>

[Play case 107 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-107.mp4)

Type: Benchmark | Date: 2026-07-20

---

<a id="case-110"></a>
### Case 110: [Evaluar Kimi K3 en AA-Briefcase](https://x.com/ArtificialAnlys/status/2079715807983210572) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Usa los resultados de AA-Briefcase para juzgar Kimi K3 en tareas agentic de trabajo del conocimiento antes de confiar en afirmaciones de leaderboard.**

Artificial Analysis informa que Kimi K3 obtuvo 1543 Elo en AA-Briefcase, segundo detrás de Claude Fable 5, y señala que el modelo promedió casi una hora por tarea y costó más que Opus 4.8 en este benchmark.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-110-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-110-01.jpg" alt="Case 110 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-21

---

<a id="case-113"></a>
### Case 113: [Auditar salvedades del leaderboard frontend](https://x.com/RetroChainer/status/2079622227796885850) (by [@RetroChainer](https://x.com/RetroChainer))

**Usa esta nota de limitación para separar las victorias de Kimi K3 en leaderboards de afirmaciones más amplias sobre coding y coste.**

RetroChainer verifica el liderazgo en Frontend Code Arena y los precios listados, y luego marca salvedades: el rango es específico de ese tablero, los pesos aún no eran públicos al publicarse, los ahorros por trabajo venían de una sola tarea y el razonamiento máximo puede gastar muchos tokens en trabajos pequeños.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-113.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-113-poster.jpg" alt="Case 113 source video poster" height="360"></a>

[Play case 113 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-113.mp4)

Type: Limit | Date: 2026-07-21

---

<a id="case-114"></a>
### Case 114: [Comparar resultados de arquitectura StackPerf](https://x.com/tamsi_besson/status/2079573266855834071) (by [@tamsi_besson](https://x.com/tamsi_besson))

**Usa StackPerf para comparar Kimi K3 y Qwen 3.8 en calidad de arquitectura, velocidad y comportamiento de tool calls.**

Tamsi Besson comparte una instantánea de StackPerf donde Kimi K3 supera ligeramente a Qwen 3.8 Max Preview en calidad y corre más rápido en total, mientras Qwen registra cero tool calls fallidos frente a dos de Kimi pese a que Kimi hizo más llamadas.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-114-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-114-01.jpg" alt="Case 114 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-21

---

<a id="case-118"></a>
### Case 118: [Comparar costes con prompt Monument Valley](https://x.com/AiHubMix/status/2079507420083294557) (by [@AiHubMix](https://x.com/AiHubMix))

**Usa un único prompt estilo Monument Valley para comparar calidad visual, tiempo de ejecución y coste entre Kimi K3 y otros modelos.**

AiHubMix compara Claude Fable 5, Kimi K3 y GPT-5.6 Sol con un prompt estilo Monument Valley. El post reporta Fable como el más coherente, Kimi como el más lento con 52m30s y $1.50, y GPT-5.6 Sol como el más rápido y barato pero más débil en lógica espacial.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-118.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-118-poster.jpg" alt="Case 118 source video poster" height="360"></a>

[Play case 118 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-118.mp4)

Type: Benchmark | Date: 2026-07-21

---

<a id="case-120"></a>
### Case 120: [Evaluar Kimi K3 en el índice Surge](https://x.com/echen/status/2080021575190110523) (by [@echen](https://x.com/echen))

**Usa los resultados divididos de SurgeAI para separar la fortaleza de Kimi K3 en chat cotidiano de su rendimiento más débil en agentes empresariales y ciencia.**

Eric Chen informa que SurgeAI probó Kimi K3 en un índice que cubre chatbots cotidianos, agentes empresariales, razonamiento profundo y ciencia de frontera. La publicación dice que Kimi K3 compite bien en chat diario, mientras Fable sigue por delante y Kimi queda detrás de Fable y Sol en agentes empresariales y ciencia.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-120-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-120-01.jpg" alt="Case 120 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-22

---

<a id="case-123"></a>
### Case 123: [Evaluar errores en PDE](https://x.com/lanyon_ai/status/2079931884511887740) (by [@lanyon_ai](https://x.com/lanyon_ai))

**Usa fallos en benchmarks de PDE para decidir dónde las tareas simbólicas o numéricas requieren verificación alrededor de Kimi K3.**

Lanyon AI compara su arquitectura neurosimbólica con modelos frontera, incluido Kimi K3, en PDE lineales simples. La fuente informa errores matemáticos, algorítmicos y computacionales incluso con prompts detallados.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-123-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-123-01.jpg" alt="Case 123 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-22

---

<a id="case-124"></a>
### Case 124: [Revisar casos EHR de ClinicalBench](https://x.com/mkurman88/status/2079918374977413534) (by [@mkurman88](https://x.com/mkurman88))

**Usa los casos EHR de ClinicalBench para inspeccionar dónde Kimi K3 acierta y dónde falla el razonamiento diagnóstico.**

Michael Kurman informa resultados de ClinicalBench v0.0.4 para Kimi K3 en un sandbox EHR virtual con 10 casos de urgencias. La fuente dice que Kimi K3 resolvió 7 de 10 y tuvo problemas con el caso 6.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-124-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-124-01.jpg" alt="Case 124 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-124-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-124-02.jpg" alt="Case 124 source image 2" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-124-03.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-124-03.jpg" alt="Case 124 source image 3" height="360"></a>

Type: Benchmark | Date: 2026-07-22

---

<a id="case-126"></a>
### Case 126: [Evaluar cálculos de impuestos](https://x.com/michaelrbock/status/2079913117698666964) (by [@michaelrbock](https://x.com/michaelrbock))

**Prueba Kimi K3 por separado en cargas fiscales en vez de asumir que su fortaleza frontend se transfiere.**

Michael Bock informa una prueba de Kimi K3 en 50 declaraciones federales y estatales hiperrealistas. La fuente dice que Kimi K3 logró 6% en TaxCalcBench, frente a 58% de GPT-5.6 Sol y 4% de Fable 5.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-126-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-126-01.jpg" alt="Case 126 source image 1" height="360"></a>

Type: Limit | Date: 2026-07-22

---

<a id="related-resources"></a>
## Recursos relacionados

- [Ver detalles y precios de Kimi K3 en EvoLink](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=landing_overview)
- [Abrir la documentación API de Kimi K3 en EvoLink](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=docs_link)
- [Más información sobre Kimi K3 en EvoLink](https://evolink.ai/blog/is-kimi-k3-available-on-evolink?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_article)
- [KimiK3.io](https://kimik3.io/)
- La página del modelo y la documentación API de EvoLink están verificadas; no se verificó una skill instalable de Kimi K3

<a id="acknowledge"></a>
## 🙏 Agradecimientos

Este repositorio existe gracias a quienes compartieron públicamente su trabajo con Kimi K3

[@ivanfioravanti](https://x.com/ivanfioravanti), [@TheAhmadOsman](https://x.com/TheAhmadOsman), [@HarshithLucky3](https://x.com/HarshithLucky3), [@chetaslua](https://x.com/chetaslua), [@abhinavflac](https://x.com/abhinavflac), [@bridgemindai](https://x.com/bridgemindai), [@Whats_AI](https://x.com/Whats_AI), [@chongdashu](https://x.com/chongdashu), [@MrAhmadAwais](https://x.com/MrAhmadAwais), [@bijanbowen](https://x.com/bijanbowen), [@CommandCodeAI](https://x.com/CommandCodeAI), [@emollick](https://x.com/emollick), [@nicky_sap](https://x.com/nicky_sap), [@Lentils80](https://x.com/Lentils80), [@scottstts](https://x.com/scottstts), [@aisearchio](https://x.com/aisearchio), [@gmi_cloud](https://x.com/gmi_cloud), [@karminski3](https://x.com/karminski3), [@VORTEX_Promos](https://x.com/VORTEX_Promos), [@rohanpaul_ai](https://x.com/rohanpaul_ai), [@mirochill](https://x.com/mirochill), [@aimlapi](https://x.com/aimlapi), [@minchoi](https://x.com/minchoi), [@doutorcaleb](https://x.com/doutorcaleb), [@adxtyahq](https://x.com/adxtyahq), [@higgsfield_ai](https://x.com/higgsfield_ai), [@AlicanKiraz0](https://x.com/AlicanKiraz0), [@1littlecoder](https://x.com/1littlecoder), [@op7418](https://x.com/op7418), [@adamuchigabriel](https://x.com/adamuchigabriel), [@s_batzoglou](https://x.com/s_batzoglou), [@servasyy_ai](https://x.com/servasyy_ai), [@filicroval](https://x.com/filicroval), [@doodlestein](https://x.com/doodlestein), [@dejavucoder](https://x.com/dejavucoder), [@Angaisb_](https://x.com/Angaisb_), [@AngryTomtweets](https://x.com/AngryTomtweets), [@Alezander907](https://x.com/Alezander907), [@teortaxesTex](https://x.com/teortaxesTex), [@jun_song](https://x.com/jun_song), [@ridark_eth](https://x.com/ridark_eth), [@naymur_dev](https://x.com/naymur_dev), [@tphuang](https://x.com/tphuang), [@TokenGremlin](https://x.com/TokenGremlin), [@IntuitMachine](https://x.com/IntuitMachine), [@wangfeng0315](https://x.com/wangfeng0315), [@twid](https://x.com/twid), [@pengchujin](https://x.com/pengchujin), [@aayushman2703](https://x.com/aayushman2703), [@goncalo_canhoto](https://x.com/goncalo_canhoto), [@LinearUncle](https://x.com/LinearUncle), [@gagarot200](https://x.com/gagarot200), [@MinLiBuilds](https://x.com/MinLiBuilds), [@izutorishima](https://x.com/izutorishima), [@X2worldtech](https://x.com/X2worldtech), [@Satvik_Pen](https://x.com/Satvik_Pen), [@hakki_alkan](https://x.com/hakki_alkan), [@BrianMRey](https://x.com/BrianMRey), [@ChrisGPT](https://x.com/ChrisGPT), [@arena](https://x.com/arena), [@MathiasHeide](https://x.com/MathiasHeide), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@nauczymycieAI](https://x.com/nauczymycieAI), [@AlphaSignalAI](https://x.com/AlphaSignalAI), [@Ananth7e](https://x.com/Ananth7e), [@viktoroddy](https://x.com/viktoroddy), [@abacusai](https://x.com/abacusai), [@deredleritt3r](https://x.com/deredleritt3r), [@fabriciocarraro](https://x.com/fabriciocarraro), [@startracker](https://x.com/startracker), [@mattwatkajtys](https://x.com/mattwatkajtys), [@AIsaOneHQ](https://x.com/AIsaOneHQ), [@MiaAI_lab](https://x.com/MiaAI_lab), [@hqmank](https://x.com/hqmank), [@prasenx](https://x.com/prasenx), [@stas_sorokin_](https://x.com/stas_sorokin_), [@RoundtableSpace](https://x.com/RoundtableSpace), [@karankendre](https://x.com/karankendre), [@0xzynex](https://x.com/0xzynex), [@ashen_one](https://x.com/ashen_one), [@MAXdeg0](https://x.com/MAXdeg0), [@ice_bearcute](https://x.com/ice_bearcute), [@mnmn94253156337](https://x.com/mnmn94253156337), [@morganlinton](https://x.com/morganlinton), [@vikktorrrre](https://x.com/vikktorrrre), [@kirillk_web3](https://x.com/kirillk_web3), [@_guillecasaus](https://x.com/_guillecasaus), [@demian_ai](https://x.com/demian_ai), [@aidenybai](https://x.com/aidenybai), [@LexnLin](https://x.com/LexnLin), [@boxmining](https://x.com/boxmining), [@Nekt_0](https://x.com/Nekt_0), [@RetroChainer](https://x.com/RetroChainer), [@tamsi_besson](https://x.com/tamsi_besson), [@thehypedotnews](https://x.com/thehypedotnews), [@AiHubMix](https://x.com/AiHubMix), [@sairahul1](https://x.com/sairahul1), [@echen](https://x.com/echen), [@Oluwaphilemon1](https://x.com/Oluwaphilemon1), [@diegocabezas01](https://x.com/diegocabezas01), [@lanyon_ai](https://x.com/lanyon_ai), [@mkurman88](https://x.com/mkurman88), [@ShenSeanChen](https://x.com/ShenSeanChen), [@michaelrbock](https://x.com/michaelrbock), [@Kirratr](https://x.com/Kirratr), [@jadeferrara_](https://x.com/jadeferrara_), [@biscuitweb3](https://x.com/biscuitweb3)

*Si la atribución o el texto necesitan una corrección, abre una issue con una fuente pública*
