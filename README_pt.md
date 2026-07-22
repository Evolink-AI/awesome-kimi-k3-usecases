<div align="center">

<a href="https://evolink.ai/kimi-k3?utm_source=github&utm_medium=banner&utm_campaign=awesome-kimi-k3-usecases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/images/en-v2.png" alt="Banner em inglês de casos de uso do Kimi K3 com chamada da EvoLink" width="760"></a>

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

# Casos de uso incríveis do Kimi K3

## 🍌 Introdução

Bem-vindo ao repositório de casos de uso de alto sinal do Kimi K3

**Reunimos jogos, cenas 3D, motion design, integrações, avaliações e limites práticos do Kimi K3 apoiados por fontes públicas**

Os 89 casos vêm de fontes públicas de alta confiança. Títulos e autores levam aos originais; candidatos fracos, duplicados ou sem evidência suficiente são excluídos

## 📊 Visão geral

- 109 casos de alta confiança de criadores e profissionais
- Abrange amplamente jogos, Three.js, motion graphics, frontend, pesquisa, ferramentas de agentes, benchmarks, raciocínio e limites práticos
- Cada caso preserva fonte, autor, tipo, data e limite do prompt
- Relatos individuais não viram benchmarks

> [!NOTE]
> A coleção prioriza evidência concreta e não reconstrói prompts ou etapas ausentes

<a id="quick-api-access"></a>
## ⚡ Início rápido

O ID documentado pela EvoLink é `kimi-k3`; a página do modelo e a documentação de Chat Completions estão disponíveis

1. [Ver detalhes e preços do Kimi K3 na EvoLink](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=landing_overview)
2. [Criar ou gerenciar uma chave API da EvoLink](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-kimi-k3-usecases&utm_content=api_key)

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

[Abrir a documentação da API Kimi K3 na EvoLink](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=first_run)

> [!IMPORTANT]
> A página do modelo e a documentação da EvoLink verificam a rota pública e o ID. Nenhuma superfície independente de navegador ou sem código para Kimi K3 foi verificada, e este repositório não afirma ter feito um teste pago independente

## 📑 Menu

| Section | Cases |
|---|---|
| [Jogos interativos e 3D](#games-3d) | 37 |
| [Frontend e motion design](#frontend-motion) | 25 |
| [Código e integrações](#coding-integrations) | 14 |
| [Avaliação e limites](#evaluation-limits) | 43 |
| [Recursos relacionados](#related-resources) | Recursos relacionados |
| [Início rápido](#quick-api-access) | Início rápido |
| [Agradecimentos](#acknowledge) | Créditos e correções |

| Case | Category | What it shows | Type |
|---|---|---|---|
| [Criar um pod racer voxel com um prompt](#case-1) | Jogos interativos e 3D | Use uma ideia curta para prototipar uma corrida voxel e planejar a próxima versão | Demo |
| [Comparar Frogger com o mesmo prompt](#case-2) | Jogos interativos e 3D | Mantenha o prompt constante para inspecionar diferenças entre modelos | Evaluation |
| [Gerar Frogger e sua gravação](#case-3) | Jogos interativos e 3D | Teste em uma execução o jogo e o fluxo de gravação | Demo |
| [Prototipar um porta-aviões em Three.js](#case-4) | Jogos interativos e 3D | Use uma cena concreta para testar um protótipo 3D interativo | Demo |
| [Criar um frontend de motion graphics interativo](#case-5) | Frontend e motion design | Crie gráficos que continuem interativos quando pausados | Demo |
| [Produzir um anúncio animado sincronizado](#case-6) | Frontend e motion design | Verifique a sincronia entre música, efeitos e movimento | Demo |
| [Comparar design de frontend na tarefa de lava lamp do BridgeBench](#case-7) | Avaliação e limites | Use a tarefa de lava lamp do BridgeBench como uma comparação delimitada de design de frontend, não como ranking universal | Benchmark |
| [Avaliar roteiros com voz editorial](#case-8) | Avaliação e limites | Meça adequação à voz editorial, posição relativa e custo por roteiro dentro de um benchmark interno claramente identificado | Benchmark |
| [Criar um jogo inspirado em Paper Mario com ferramentas de agente](#case-9) | Jogos interativos e 3D | Combine Kimi K3 com um harness de agente e ferramentas de assets para produzir elementos de jogo 2D e 3D | Demo |
| [Comparar design, custo e dificuldade de jogos no estilo Flappy](#case-10) | Avaliação e limites | Registre configurações de dificuldade, custo, design e recursos de jogabilidade ao comparar jogos gerados | Benchmark |
| [Gerar um jogo de tiro em primeira pessoa no metrô](#case-11) | Jogos interativos e 3D | Use um cenário concreto de metrô para examinar o resultado de um FPS gerado | Demo |
| [Comparar design de jogos com o mesmo prompt de design](#case-12) | Avaliação e limites | Mantenha o prompt de design constante e examine ritmo, senso de design e sensação de jogabilidade separadamente | Benchmark |
| [Exigir revisão independente em auditorias estatísticas](#case-13) | Avaliação e limites | Combine auditorias estatísticas geradas por modelo com revisão independente de especialista ou de outro modelo antes de confiar nos achados | Limit |
| [Criar motion design inteiramente em código](#case-14) | Frontend e motion design | Teste se um fluxo de programação em uma execução consegue produzir motion design sem ferramentas auxiliares de geração | Demo |
| [Pesquisar uma pessoa e criar um site pessoal animado](#case-15) | Frontend e motion design | Forneça um briefing amplo de site pessoal e examine pesquisa, planejamento, iteração e validação no navegador pelo modelo | Tutorial |
| [Avaliar uma execução de frontend lenta, mas forte](#case-16) | Avaliação e limites | Registre o tempo de conclusão junto com a qualidade da saída ao testar uma tarefa de frontend | Evaluation |
| [Gerar uma simulação de buraco negro](#case-17) | Frontend e motion design | Use uma tarefa de visualização científica para examinar uma simulação gerada de buraco negro | Demo |
| [Criar um MacBook virtual com macOS funcional](#case-18) | Código e integrações | Combine renderização de hardware em Three.js com uma simulação interativa de sistema operacional no navegador | Demo |
| [Modelar um motor V8 com Blender MCP](#case-19) | Jogos interativos e 3D | Use Blender MCP e um único pedido para gerar um modelo mecânico 3D detalhado | Integration |
| [Testar falhas de prenúncio em narrativas de mistério](#case-20) | Avaliação e limites | Avalie se um mistério gerado equilibra pistas, obscuridade e prenúncio | Limit |
| [Comparar modelagem e animação da Millennium Falcon](#case-21) | Avaliação e limites | Use pedidos de estilo e configurações de esforço equivalentes para comparar modelagem 3D, animação, tempo e custo | Benchmark |
| [Testar modelagem complexa, partículas e shaders no frontend](#case-22) | Frontend e motion design | Use um prompt público de frontend para examinar precisão de modelagem, efeitos de partículas e geração de shaders inline em uma passagem | Demo |
| [Criar uma arena de batalha jogável a partir de uma referência](#case-23) | Jogos interativos e 3D | Use uma única referência para testar a geração em uma execução de uma arena jogável completa | Demo |
| [Criar três jogos retrô autônomos como arquivos HTML](#case-24) | Jogos interativos e 3D | Exija gráficos, inimigos, regras e jogo autônomo em arquivos HTML independentes | Benchmark |
| [Criar um compilador de GPU de DSL a PTX](#case-25) | Código e integrações | Use uma tarefa completa de compilador que abranja DSL, passes, geração de PTX e um caminho de Tensor Core | Demo |
| [Gerar uma ferramenta de música procedural em uma tentativa](#case-26) | Frontend e motion design | Teste a geração em uma execução de um gerador interativo de música procedural e compare o resultado visível com cautela | Demo |
| [Criar um jogo de esconde-esconde com camaleão em uma execução](#case-27) | Jogos interativos e 3D | Gere um jogo em arquivo único com combinação de cores, áreas procedurais, som e pontuação por várias rodadas | Benchmark |
| [Analisar uma coleção de dez projetos com Kimi K3](#case-28) | Avaliação e limites | Use uma coletânea de projetos vinculada para descobrir artefatos concretos que devem ser verificados separadamente | Evaluation |
| [Comparar uma landing page avançada entre quatro modelos](#case-29) | Avaliação e limites | Mantenha constante o pedido de landing page e examine profundidade de animação e conclusão nas saídas dos modelos | Evaluation |
| [Avaliar mecânicas e custos de jogos retrô](#case-30) | Avaliação e limites | Compare jogabilidade, física, mecânicas, comportamento autônomo, uso de tokens e custo nas mesmas tarefas de jogos retrô | Benchmark |
| [Comparar geração de jogos com Fable 5](#case-31) | Avaliação e limites | Use um exemplo lado a lado de jogos gerados como avaliação estreita, não como veredito amplo sobre os modelos | Evaluation |
| [Criar um raytracer de buraco negro em tempo real no WebGL2](#case-32) | Código e integrações | Teste a geração, com um prompt, de um raytracer geodésico nativo em WebGL2 dentro de um arquivo HTML | Benchmark |
| [Criar uma página de produto em Three.js a partir de duas imagens](#case-33) | Frontend e motion design | Use duas imagens de referência e uma exigência explícita de Three.js para gerar uma apresentação de produto | Demo |
| [Comparar tarefas complexas de frontend e desenvolvimento com Opus 4.8](#case-34) | Avaliação e limites | Use várias tarefas complexas de programação para identificar vitórias e derrotas, sem declarar um modelo universalmente superior | Evaluation |
| [Analisar benchmarks e um teste de landing page](#case-35) | Avaliação e limites | Combine contexto de benchmark com um teste concreto de geração de landing page, mantendo separados os dois tipos de evidência | Evaluation |
| [Criar um jogo 2.5D no estilo Paper Mario com uma cadeia de agentes](#case-36) | Jogos interativos e 3D | Use Kimi K3 com Grok Build ou Claude Code e Spriterrific para montar um fluxo de jogo 2.5D | Tutorial |
| [Avaliar raciocínio indutivo com tarefas de grafo para fórmula](#case-37) | Avaliação e limites | Meça correção, comportamento em holdout e complexidade de fórmula em tarefas de indução de primeira ordem | Benchmark |
| [Analisar relatos sobre jogos, landing pages, 3D e contexto longo](#case-38) | Avaliação e limites | Use uma coletânea de várias fontes para comparar artefatos concretos e observar limites de velocidade junto a alegações de custo | Evaluation |
| [Inventar um cortador de pão de luxo e sua página de produto](#case-39) | Frontend e motion design | Combine ideação de produto, vista explodida, demonstração e landing page em um artefato de design | Demo |
| [Auditar um plano complexo e contestar suas soluções](#case-40) | Avaliação e limites | Use um segundo modelo para identificar achados subestimados, soluções incorretas e conclusões que devem ser rejeitadas | Evaluation |
| [Comparar diagramas ASCII de aprendizado por reforço no estilo PPO](#case-41) | Avaliação e limites | Mantenha constante um prompt de diagrama ASCII e compare como os modelos representam o ciclo de aprendizado por reforço | Evaluation |
| [Modelar no Blender enquanto se monitoram erros de capacidade](#case-42) | Avaliação e limites | Avalie o progresso parcial no Blender junto com a confiabilidade do serviço, em vez de julgar apenas o artefato | Limit |
| [Criar um RPG wuxia 3D no navegador](#case-43) | Jogos interativos e 3D | Combine combate corpo a corpo, missões, inventário, clima, interiores, trabalho de ambiente no Blender e assets adaptados | Demo |
| [Criar um jogo multiplayer de navegador no estilo Minecraft](#case-44) | Jogos interativos e 3D | Use uma execução delimitada por tempo e custo para produzir um jogo multiplayer online jogável no navegador | Demo |
| [Gerar um GIF recursivo de pelicano com dez segundos](#case-45) | Frontend e motion design | Use um briefing completo de animação em loop para examinar continuidade narrativa e recursão em um GIF | Demo |
| [Criar um emulador de Game Boy Advance com mGBA WASM](#case-46) | Código e integrações | Integre um modelo 3D licenciado e um núcleo real de emulador e depois melhore recursivamente interface e jogabilidade | Integration |
| [Comparar geração de Flappy Bird em uma arena](#case-47) | Avaliação e limites | Use uma tarefa de arena para comparar dois resultados gerados de Flappy Bird, mantendo o julgamento específico à tarefa | Evaluation |
| [Recriar um jogo cooperativo de tela dividida no navegador](#case-48) | Jogos interativos e 3D | Use um pedido para gerar cooperação em tela dividida no navegador e interação com o ambiente em tempo real | Demo |
| [Gerar um jogo jogável com o modo de design da Command Code](#case-49) | Jogos interativos e 3D | Use o comando de design da Command Code para criar um jogo em uma execução e registre se o resultado é jogável | Demo |
| [Pesquisar vários temas em fontes de língua chinesa](#case-50) | Código e integrações | Use tarefas de pesquisa longas para comparar profundidade e latência entre gerações de modelos | Evaluation |
| [Montar um RPG wuxia coeso no navegador](#case-51) | Jogos interativos e 3D | Integre travessia, combate, missões, inventário, clima, exploração e trabalho de ambiente 3D em um jogo | Demo |
| [Resolver um problema de indução visual de Bongard com uma ferramenta](#case-52) | Avaliação e limites | Teste se o uso de ferramentas ajuda a derivar a regra visual em uma tarefa de raciocínio de Bongard | Evaluation |
| [Comparar bom gosto em frontend e design 3D com GPT-5.6 Sol](#case-53) | Avaliação e limites | Examine recursos, gosto visual, elegância e execução 3D em uma comparação delimitada de frontend | Evaluation |
| [Criar um crossover jogável de Hollow Knight](#case-54) | Jogos interativos e 3D | Use assets existentes do jogo para criar uma batalha jogável entre o Cavaleiro e Kimi | Demo |
| [Gerar um SVG lateral de um BMW M4 CS](#case-55) | Frontend e motion design | Use um veículo e ponto de vista específicos para examinar a saída de ilustração vetorial | Demo |
| [Clonar o macOS no navegador com aplicativos funcionais](#case-56) | Código e integrações | Crie uma simulação de sistema operacional no navegador que inclua aplicativos de música, navegador e e-mail | Demo |
| [Comparar geração de sites entre três modelos](#case-57) | Avaliação e limites | Use saídas visíveis de sites para comparar Kimi K3, Fable 5 e GPT-5.6 Sol em um teste | Evaluation |
| [Recriar Gargantua por feedback de capturas de tela](#case-58) | Frontend e motion design | Use capturas de tela repetidas como observações para diagnosticar e refinar uma visualização científica | Tutorial |
| [Comparar geração procedural de jogos 3D e custo](#case-59) | Avaliação e limites | Mantenha um prompt constante entre modelos e examine roleta, caça-níquel e pinball gerados com o custo por execução | Benchmark |
| [Criar em uma execução um jogo 3D no estilo Fall Guys para navegador](#case-60) | Jogos interativos e 3D | Use um pedido em uma execução para gerar um jogo 3D de obstáculos jogável e disponibilize o projeto para inspeção | Demo |
| [Criar e testar automaticamente um FPS apocalíptico em Lisboa](#case-61) | Jogos interativos e 3D | Use uma execução de esforço máximo com um prompt que teste, capture telas e itere antes de entregar um FPS jogável | Demo |
| [Criar uma simulação de macOS com FaceTime funcional](#case-62) | Código e integrações | Use uma tarefa de sistema operacional virtual para testar se uma interação de aplicativo gerada funciona | Demo |
| [Gerar um jogo no estilo Animal Crossing a partir de um pedido simples](#case-63) | Jogos interativos e 3D | Use um briefing mínimo de jogo para examinar jogabilidade, ciclo de jogo e efeitos de paralaxe | Demo |
| [Adicionar um comparador de efeitos de frontend com duas tarefas](#case-64) | Código e integrações | Crie uma ferramenta que selecione duas tarefas concluídas, exiba-as lado a lado e sincronize visualizações e interações | Tutorial |
| [Gerar um jogo no estilo Mario a partir de uma frase](#case-65) | Jogos interativos e 3D | Use um pedido mínimo em uma execução para examinar jogabilidade, design de fases, pixel art e paralaxe | Demo |
| [Refinar uma visualização de buraco negro com 62 capturas de tela](#case-66) | Frontend e motion design | Use um ciclo de feedback por capturas de tela para ler, diagnosticar e corrigir uma simulação visual ao longo de muitas iterações | Tutorial |
| [Criar um jogo de tiro em primeira pessoa com zumbis funcional](#case-67) | Jogos interativos e 3D | Use um alvo concreto de jogo de tiro com zumbis para examinar um artefato FPS completo e jogável | Demo |
| [Criar um PDF de marketing sobre pós-treinamento](#case-68) | Frontend e motion design | Use um produto nomeado e um formato de entrega para gerar um documento de marketing | Demo |
| [Comparar detalhes e iluminação de uma cena 3D de arsenal](#case-69) | Avaliação e limites | Examine densidade de objetos, iluminação e detalhes da cena em uma comparação delimitada entre Kimi K3 e Opus 4.8 | Evaluation |
| [Criar uma interface de usuário a partir de um prompt](#case-70) | Frontend e motion design | Use um único pedido para gerar e examinar um design completo de interface | Demo |
| [Criar um jogo indie de nave](#case-71) | Jogos interativos e 3D | Use Kimi K3 Standard para uma primeira versão e compare coerência, falhas, qualidade visual e custo de tokens | Demo |
| [Comparar frontends com prompts Arena idênticos](#case-72) | Avaliação e limites | Use prompts idênticos e resultados lado a lado em vez de depender de uma única posição no ranking | Benchmark |
| [Autotestar um jogo no Summer Engine](#case-73) | Jogos interativos e 3D | Faça Kimi K3 executar o jogo, verificar capturas e logs e corrigir defeitos visíveis na mesma sessão | Demo |
| [Avaliar Kimi Code em agentes de código](#case-74) | Avaliação e limites | Avalie Kimi K3 em vários testes e no custo por tarefa sem generalizar um ranking de frontend | Benchmark |
| [Configurar Kimi como subagente do Codex](#case-75) | Código e integrações | Mantenha a orquestração no Codex e delegue o frontend a um subagente Kimi K3 OpenCode com limite claro para segredos | Tutorial |
| [Comparar Arena e o teste de reparo](#case-76) | Avaliação e limites | Veja preferência de frontend e reparo de repositório porque Kimi K3 pode ficar em primeiro em um e sétimo em outro | Benchmark |
| [Iterar um battle royale no navegador](#case-77) | Jogos interativos e 3D | Espere iterações autônomas longas e prompts posteriores específicos em jogos de navegador ricos em recursos | Demo |
| [Criar um site com estilo premiado](#case-78) | Frontend e motion design | Avalie a sessão gravada completa, não apenas a captura final | Tutorial |
| [Rotear código simples pelo ChatLLM](#case-79) | Código e integrações | Envie código simples ao Kimi K3 e reserve código difícil e design para outros modelos | Integration |
| [Avaliar Kimi K3 no Prinzbench](#case-80) | Avaliação e limites | Use uma atualização independente de benchmark para comparar Kimi K3 com modelos abertos e de fronteira em busca, raciocínio e consistência. | Benchmark |
| [Criar frontend com metaballs no scroll](#case-81) | Frontend e motion design | Peça a Kimi K3 uma página estilo Awwwards com scroll e verifique se efeitos matemáticos substituem malhas ou texturas pesadas. | Demo |
| [Redesenhar um site pessoal entre modelos](#case-82) | Frontend e motion design | Rode o mesmo brief de redesign em vários harnesses de código e compare tempo, direção visual e aderência à identidade existente. | Evaluation |
| [Expandir a paisagem de um jogo espacial](#case-83) | Jogos interativos e 3D | Use Kimi K3 como uma passada longa para trocar terreno provisório por um ambiente maior inspirado em dados reais. | Demo |
| [Desbloquear renderização física em Three.js](#case-84) | Jogos interativos e 3D | Traga Kimi K3 para um projeto físico em Three.js quando a matemática funciona, mas o pipeline de renderização precisa avançar. | Demo |
| [Comparar geração de gêmeo digital da ISS](#case-85) | Avaliação e limites | Use um desafio 3D com o mesmo prompt para comparar Kimi K3 e GPT-5.6 Sol em reconstrução, controles, rótulos e detalhe visual. | Benchmark |
| [Criar explorador interativo de couro cabeludo](#case-86) | Frontend e motion design | Use Kimi K3 para uma cena educacional 3D de uma passada com camadas anatômicas, fios responsivos e hotspots interativos. | Demo |
| [Compartilhar prompt de dashboard globo 3D](#case-87) | Frontend e motion design | Estude um prompt e uma imagem de referência para um dashboard globo 3D em Kimi K3 em vez de inferir o fluxo apenas pelo resultado final. | Tutorial |
| [Criar Counter-Strike no navegador em um arquivo](#case-88) | Jogos interativos e 3D | Use Kimi K3 para gerar um FPS de navegador em arquivo único e conferir mapa, bots, armas, regras de rodada e áudio procedural. | Demo |
| [Revisar um mundo florestal WebGPU](#case-89) | Avaliação e limites | Avalie Kimi K3 como cérebro de agente de código em uma construção longa com Three.js e WebGPU, incluindo qualidade, velocidade, consistência e taxa de edição. | Evaluation |
| [Comparar prompts de casa de vidro](#case-90) | Avaliação e limites | Use uma cena arquitetônica com o mesmo prompt para comparar Kimi K3 e Opus 4.8 em atmosfera, iluminação e completude espacial. | Evaluation |
| [Criar CS com assets gerados](#case-91) | Código e integrações | Combine Kimi K3 para o código do jogo com GPT Image 2 para os assets ao prototipar um pequeno jogo estilo Counter-Strike no navegador. | Integration |
| [Avaliar um gol de futebol voxel](#case-92) | Avaliação e limites | Execute o mesmo prompt de animação de futebol em HTML/CSS/JS puro em dois modelos para comparar movimento e custo. | Benchmark |
| [Revisar uma prova Minecraft](#case-93) | Avaliação e limites | Assista a uma revisão estruturada de Minecraft antes de aceitar hype de lançamento ou preço como evidência suficiente. | Benchmark |
| [Executar cinco testes UI UX](#case-94) | Frontend e motion design | Avalie Kimi K3 em várias tarefas de UI, logo e Figma MCP em vez de confiar em um único screenshot frontend. | Evaluation |
| [Usar a skill Design do Command Code](#case-95) | Código e integrações | Combine Kimi K3 com uma skill dedicada de design no Command Code ao criar um protótipo visual de jogo dentro de orçamento de tokens. | Integration |
| [Construir um jogo de pirâmide](#case-96) | Jogos interativos e 3D | Use Kimi K3 em uma passada de um dia para um jogo 3D de exploração, depois inspecione missões, interiores e escopo antes de julgar qualidade. | Demo |
| [Criar landings a partir de referências](#case-97) | Frontend e motion design | Use boards de referência, Figma AI e Motion Sites com Kimi K3 para transformar direção visual em seções reutilizáveis de landing page. | Tutorial |
| [Medir limites de nível da API](#case-98) | Avaliação e limites | Planeje execuções de agente com Kimi K3 por tokens, nível, TPM e TPD, não só pelo preço de manchete do modelo. | Limit |
| [Comparar um demo estilo Limbo](#case-99) | Avaliação e limites | Compare escopo jogável, polimento, custo e bugs ao testar Kimi K3 contra Fable 5 no mesmo protótipo de jogo. | Benchmark |
| [Revisar custos do VulcanBench](#case-100) | Avaliação e limites | Use este caso para avaliar o fluxo real, o custo ou os limites do Kimi K3 em “Revisar custos do VulcanBench”. | Benchmark |
| [Comparar profundidade no Minecraft](#case-101) | Jogos interativos e 3D | Use este caso para avaliar o fluxo real, o custo ou os limites do Kimi K3 em “Comparar profundidade no Minecraft”. | Evaluation |
| [Criar um FPS de Fallout](#case-102) | Jogos interativos e 3D | Use este caso para avaliar o fluxo real, o custo ou os limites do Kimi K3 em “Criar um FPS de Fallout”. | Demo |
| [Seguir tutorial de site premium](#case-103) | Frontend e motion design | Use este caso para avaliar o fluxo real, o custo ou os limites do Kimi K3 em “Seguir tutorial de site premium”. | Tutorial |
| [Avaliar física de pêndulo duplo](#case-104) | Avaliação e limites | Use este caso para avaliar o fluxo real, o custo ou os limites do Kimi K3 em “Avaliar física de pêndulo duplo”. | Benchmark |
| [Lançar RPG de data center](#case-105) | Jogos interativos e 3D | Use este caso para avaliar o fluxo real, o custo ou os limites do Kimi K3 em “Lançar RPG de data center”. | Demo |
| [Comparar custos de frontend humanoide](#case-106) | Frontend e motion design | Use este caso para avaliar o fluxo real, o custo ou os limites do Kimi K3 em “Comparar custos de frontend humanoide”. | Benchmark |
| [Revisar prontidão no ReactBench](#case-107) | Avaliação e limites | Use este caso para avaliar o fluxo real, o custo ou os limites do Kimi K3 em “Revisar prontidão no ReactBench”. | Benchmark |
| [Criar jogo 3D de carros](#case-108) | Jogos interativos e 3D | Use este caso para avaliar o fluxo real, o custo ou os limites do Kimi K3 em “Criar jogo 3D de carros”. | Demo |
| [Rodar Kimi K3 no Claude Code](#case-109) | Código e integrações | Use este caso para avaliar o fluxo real, o custo ou os limites do Kimi K3 em “Rodar Kimi K3 no Claude Code”. | Integration |
| [Avaliar Kimi K3 no AA-Briefcase](#case-110) | Avaliação e limites | Use os resultados do AA-Briefcase para julgar Kimi K3 em tarefas agentic de trabalho do conhecimento antes de confiar em rankings. | Benchmark |
| [Comparar clones de Geometry Dash](#case-111) | Jogos interativos e 3D | Compare builds com o mesmo briefing para decidir se Kimi K3 serve para protótipos jogáveis de estilo mobile. | Evaluation |
| [Testar jogo retrô no Command Code](#case-112) | Jogos interativos e 3D | Use uma rodada multi-modelo no Command Code para comparar recursos de gameplay do Kimi K3 e custo por modelo. | Evaluation |
| [Auditar ressalvas do leaderboard frontend](#case-113) | Avaliação e limites | Use esta nota de limite para separar vitórias de Kimi K3 em leaderboard de afirmações gerais sobre coding e custo. | Limit |
| [Comparar resultados StackPerf de arquitetura](#case-114) | Avaliação e limites | Use StackPerf para comparar Kimi K3 e Qwen 3.8 em qualidade arquitetural, velocidade e chamadas de ferramenta. | Benchmark |
| [Comparar builds Three.js Kimi-vs-GLM](#case-115) | Frontend e motion design | Rode os mesmos prompts procedurais de Three.js com Kimi K3 e GLM 5.2 para comparar comportamento frontend e 3D. | Benchmark |
| [Avaliar o jogo Space Discoverer](#case-116) | Jogos interativos e 3D | Use o mini-benchmark Space Discoverer para comparar saídas em um briefing genérico de jogo 3D no navegador. | Benchmark |
| [Criar jogo de direção com estrada real](#case-117) | Jogos interativos e 3D | Prototipe um jogo de direção combinando Kimi K3 com Blender e Godot em torno de um mapa de estrada local real. | Demo |
| [Comparar custos com prompt Monument Valley](#case-118) | Avaliação e limites | Use um único prompt estilo Monument Valley para comparar qualidade visual, tempo e custo entre Kimi K3 e pares. | Benchmark |
| [Roteiar Kimi via claude-code-router](#case-119) | Código e integrações | Teste Kimi K3 em um fluxo Claude Code existente via claude-code-router evitando modo proxy desnecessário. | Integration |

<a id="games-3d"></a>
## 🎮 Jogos interativos e 3D

<a id="case-1"></a>
### Case 1: [Criar um pod racer voxel com um prompt](https://x.com/ivanfioravanti/status/2077763009657627055) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Use uma ideia curta para prototipar uma corrida voxel e planejar a próxima versão**

O criador relata que Kimi K3 fez a primeira versão com um prompt público e planeja mais corredores, linha de chegada e revisão

**Prompt:**

```text
Voxel star wars pod-racers run
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01-poster.jpg" alt="Case 1 source video poster" height="360"></a>

[Play case 1 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-2"></a>
### Case 2: [Comparar Frogger com o mesmo prompt](https://x.com/ivanfioravanti/status/2077754781964054825) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Mantenha o prompt constante para inspecionar diferenças entre modelos**

O criador compartilha Frogger no Kimi K3 como comparação. A fonte não publica o prompt nem uma rubrica

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02-poster.jpg" alt="Case 2 source video poster" height="360"></a>

[Play case 2 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-3"></a>
### Case 3: [Gerar Frogger e sua gravação](https://x.com/TheAhmadOsman/status/2077776567292338285) (by [@TheAhmadOsman](https://x.com/TheAhmadOsman))

**Teste em uma execução o jogo e o fluxo de gravação**

O criador diz que Kimi K3 produziu jogo e gravação em uma execução cada. Os prompts não foram publicados

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03-poster.jpg" alt="Case 3 source video poster" height="360"></a>

[Play case 3 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-4"></a>
### Case 4: [Prototipar um porta-aviões em Three.js](https://x.com/HarshithLucky3/status/2077753222018814360) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**Use uma cena concreta para testar um protótipo 3D interativo**

O criador mostra lançamento e recuperação de caças em um porta-aviões classe Nimitz e elogia a geração 3D

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04-poster.jpg" alt="Case 4 source video poster" height="360"></a>

[Play case 4 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-9"></a>
### Case 9: [Criar um jogo inspirado em Paper Mario com ferramentas de agente](https://x.com/chongdashu/status/2077886028866531655) (by [@chongdashu](https://x.com/chongdashu))

**Combine Kimi K3 com um harness de agente e ferramentas de assets para produzir elementos de jogo 2D e 3D**

O criador relata usar Kimi K3 com Grok Build, Spriterrific para assets 2D e geometria para assets 3D em um jogo inspirado em Paper Mario. A fonte demonstra uso de ferramentas e skills, mas não publica um prompt reutilizável exato

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-09.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-09-poster.jpg" alt="Case 9 source video poster" height="360"></a>

[Play case 9 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-09.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-11"></a>
### Case 11: [Gerar um jogo de tiro em primeira pessoa no metrô](https://x.com/bijanbowen/status/2077881805751873997) (by [@bijanbowen](https://x.com/bijanbowen))

**Use um cenário concreto de metrô para examinar o resultado de um FPS gerado**

O criador mostra um FPS no metrô atribuído ao Kimi K3 e observa explicitamente a incerteza sobre se o status de influenciador afetou o resultado. Nenhum prompt ou fluxo reproduzível é fornecido

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-11.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-11-poster.jpg" alt="Case 11 source video poster" height="360"></a>

[Play case 11 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-11.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-19"></a>
### Case 19: [Modelar um motor V8 com Blender MCP](https://x.com/aisearchio/status/2077962156147146925) (by [@aisearchio](https://x.com/aisearchio))

**Use Blender MCP e um único pedido para gerar um modelo mecânico 3D detalhado**

O avaliador relata que Kimi K3 gerou um motor V8 completo com Blender MCP a partir de um prompt. A publicação leva a uma análise mais completa, mas não expõe o prompt exato no registro fornecido

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-19.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-19-poster.jpg" alt="Case 19 source video poster" height="360"></a>

[Play case 19 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-19.mp4)

Type: Integration | Date: 2026-07-17

---

<a id="case-23"></a>
### Case 23: [Criar uma arena de batalha jogável a partir de uma referência](https://x.com/VORTEX_Promos/status/2077879705378730074) (by [@VORTEX_Promos](https://x.com/VORTEX_Promos))

**Use uma única referência para testar a geração em uma execução de uma arena jogável completa**

O criador relata que Kimi K3 produziu uma arena de batalha jogável em uma execução a partir de uma referência. Uma afirmação separada de leaderboard aparece na publicação, mas o caso concreto é o artefato demonstrado

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23-poster.jpg" alt="Case 23 source video poster" height="360"></a>

[Play case 23 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23-01.jpg" alt="Case 23 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-24"></a>
### Case 24: [Criar três jogos retrô autônomos como arquivos HTML](https://x.com/rohanpaul_ai/status/2077889084761206860) (by [@rohanpaul_ai](https://x.com/rohanpaul_ai))

**Exija gráficos, inimigos, regras e jogo autônomo em arquivos HTML independentes**

A fonte relata uma comparação do Atomic Chat em que modelos criaram Road Fighter, Battle City e Q*bert como arquivos HTML autônomos. Sua comparação de custo e qualidade é relatada pela editora e não foi reproduzida de forma independente aqui

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-24.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-24-poster.jpg" alt="Case 24 source video poster" height="360"></a>

[Play case 24 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-24.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-27"></a>
### Case 27: [Criar um jogo de esconde-esconde com camaleão em uma execução](https://x.com/aimlapi/status/2077898742179459274) (by [@aimlapi](https://x.com/aimlapi))

**Gere um jogo em arquivo único com combinação de cores, áreas procedurais, som e pontuação por várias rodadas**

A AIMLAPI relata uma comparação em uma execução com o mesmo prompt para um jogo de esconde-esconde e lista custos de US$ 3,11 para Kimi K3 e US$ 12,23 para Fable 5. As alegações de recursos e custos são resultados relatados pelo provedor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-27.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-27-poster.jpg" alt="Case 27 source video poster" height="360"></a>

[Play case 27 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-27.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-36"></a>
### Case 36: [Criar um jogo 2.5D no estilo Paper Mario com uma cadeia de agentes](https://x.com/chongdashu/status/2077981621223837739) (by [@chongdashu](https://x.com/chongdashu))

**Use Kimi K3 com Grok Build ou Claude Code e Spriterrific para montar um fluxo de jogo 2.5D**

O criador fornece um tutorial completo usando Grok Build e Kimi K3 e mostra a geração de sprites com Spriterrific. A fonte identifica as ferramentas, mas não fornece prompts reutilizáveis exatos

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-36.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-36-poster.jpg" alt="Case 36 source video poster" height="360"></a>

[Play case 36 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-36.mp4)

Type: Tutorial | Date: 2026-07-17

---

<a id="case-43"></a>
### Case 43: [Criar um RPG wuxia 3D no navegador](https://x.com/AngryTomtweets/status/2077868163136450619) (by [@AngryTomtweets](https://x.com/AngryTomtweets))

**Combine combate corpo a corpo, missões, inventário, clima, interiores, trabalho de ambiente no Blender e assets adaptados**

A fonte relata um RPG de navegador com Kimi K3 que inclui combate corpo a corpo, missões, inventário, clima dinâmico e interiores exploráveis, além de modelagem no Blender, melhorias de colisão, novas texturas PBR e assets abertos adaptados

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-43.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-43-poster.jpg" alt="Case 43 source video poster" height="360"></a>

[Play case 43 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-43.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-44"></a>
### Case 44: [Criar um jogo multiplayer de navegador no estilo Minecraft](https://x.com/Alezander907/status/2077926014710407407) (by [@Alezander907](https://x.com/Alezander907))

**Use uma execução delimitada por tempo e custo para produzir um jogo multiplayer online jogável no navegador**

O criador relata que Kimi K3 criou um jogo multiplayer no estilo Minecraft, jogável no navegador, em uma hora e por US$ 6,57. São números autorrelatados de uma execução e um artefato

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-44.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-44-poster.jpg" alt="Case 44 source video poster" height="360"></a>

[Play case 44 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-44.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-48"></a>
### Case 48: [Recriar um jogo cooperativo de tela dividida no navegador](https://x.com/ridark_eth/status/2077882889803378969) (by [@ridark_eth](https://x.com/ridark_eth))

**Use um pedido para gerar cooperação em tela dividida no navegador e interação com o ambiente em tempo real**

O criador relata que Kimi K3 produziu, com um prompt, um jogo de navegador inspirado em It Takes Two, com Mario e Luigi interagindo em tela dividida e com o ambiente em tempo real

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-48.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-48-poster.jpg" alt="Case 48 source video poster" height="360"></a>

[Play case 48 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-48.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-49"></a>
### Case 49: [Gerar um jogo jogável com o modo de design da Command Code](https://x.com/naymur_dev/status/2077873562661335207) (by [@naymur_dev](https://x.com/naymur_dev))

**Use o comando de design da Command Code para criar um jogo em uma execução e registre se o resultado é jogável**

O criador relata uma comparação em uma execução usando o modo de design da Command Code e diz que a execução com Kimi K3 produziu um jogo jogável por US$ 0,038. Esse resultado de custo e qualidade é autorrelatado

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-49.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-49-poster.jpg" alt="Case 49 source video poster" height="360"></a>

[Play case 49 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-49.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-51"></a>
### Case 51: [Montar um RPG wuxia coeso no navegador](https://x.com/TokenGremlin/status/2077855657068310620) (by [@TokenGremlin](https://x.com/TokenGremlin))

**Integre travessia, combate, missões, inventário, clima, exploração e trabalho de ambiente 3D em um jogo**

A fonte relata um RPG de navegador no estilo wuxia com Kimi K3 que combina combate corpo a corpo, missões, inventário, clima dinâmico, interiores exploráveis e uma estrutura coesa de jogabilidade 3D

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-51.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-51-poster.jpg" alt="Case 51 source video poster" height="360"></a>

[Play case 51 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-51.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-54"></a>
### Case 54: [Criar um crossover jogável de Hollow Knight](https://x.com/wangfeng0315/status/2077933531200991583) (by [@wangfeng0315](https://x.com/wangfeng0315))

**Use assets existentes do jogo para criar uma batalha jogável entre o Cavaleiro e Kimi**

O criador, que afirma trabalhar na Kimi, relata ter criado um jogo com assets de Hollow Knight em que o Cavaleiro enfrenta Kimi e fornece um link público para jogar. A atribuição e a avaliação devem considerar essa afiliação

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54-poster.jpg" alt="Case 54 source video poster" height="360"></a>

[Play case 54 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54-01.jpg" alt="Case 54 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-17

---

<a id="case-60"></a>
### Case 60: [Criar em uma execução um jogo 3D no estilo Fall Guys para navegador](https://x.com/aayushman2703/status/2077857886441783526) (by [@aayushman2703](https://x.com/aayushman2703))

**Use um pedido em uma execução para gerar um jogo 3D de obstáculos jogável e disponibilize o projeto para inspeção**

O criador relata uma criação em uma execução com Kimi K3 de um jogo de navegador no estilo Fall Guys e diz que o prompt e o projeto no GitHub estão vinculados na fonte. Este registro não reproduz esse prompt

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-60.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-60-poster.jpg" alt="Case 60 source video poster" height="360"></a>

[Play case 60 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-60.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-61"></a>
### Case 61: [Criar e testar automaticamente um FPS apocalíptico em Lisboa](https://x.com/goncalo_canhoto/status/2077863166655037668) (by [@goncalo_canhoto](https://x.com/goncalo_canhoto))

**Use uma execução de esforço máximo com um prompt que teste, capture telas e itere antes de entregar um FPS jogável**

O criador relata que Kimi K3 produziu um FPS de navegador jogável ambientado em uma Lisboa apocalíptica após cerca de uma hora, com testes, capturas de tela e iterações repetidos. Esses detalhes de tempo e processo são autorrelatados

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-61-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-61-01.jpg" alt="Case 61 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-63"></a>
### Case 63: [Gerar um jogo no estilo Animal Crossing a partir de um pedido simples](https://x.com/gagarot200/status/2077949230287896830) (by [@gagarot200](https://x.com/gagarot200))

**Use um briefing mínimo de jogo para examinar jogabilidade, ciclo de jogo e efeitos de paralaxe**

O criador relata que Kimi K3 gerou um jogo totalmente jogável no estilo Animal Crossing, com ciclo de jogo e efeitos de paralaxe, a partir de um prompt muito simples. A formulação exata não consta no registro fornecido

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-63.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-63-poster.jpg" alt="Case 63 source video poster" height="360"></a>

[Play case 63 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-63.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-65"></a>
### Case 65: [Gerar um jogo no estilo Mario a partir de uma frase](https://x.com/izutorishima/status/2077939370154475992) (by [@izutorishima](https://x.com/izutorishima))

**Use um pedido mínimo em uma execução para examinar jogabilidade, design de fases, pixel art e paralaxe**

O criador relata que Kimi K3 produziu um jogo funcional no estilo Mario, sem bugs óbvios, com estrutura de fases e paralaxe, a partir de um único briefing. O mesmo relato critica a qualidade da música e dos gráficos

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-01.jpg" alt="Case 65 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-02.jpg" alt="Case 65 source image 2" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-03.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-03.jpg" alt="Case 65 source image 3" height="360"></a>

Type: Demo | Date: 2026-07-17

---

<a id="case-67"></a>
### Case 67: [Criar um jogo de tiro em primeira pessoa com zumbis funcional](https://x.com/X2worldtech/status/2077902793449296203) (by [@X2worldtech](https://x.com/X2worldtech))

**Use um alvo concreto de jogo de tiro com zumbis para examinar um artefato FPS completo e jogável**

A fonte mostra um FPS de zumbis totalmente funcional atribuído ao Kimi K3. Não fornece prompt, detalhes de implementação ou avaliação externa da jogabilidade

> [!WARNING]
> The original source permalink returned HTTP 404 during the 2026-07-17 audit. Attribution and evidence are preserved from the supplied high-confidence source package.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-67.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-67-poster.jpg" alt="Case 67 source video poster" height="360"></a>

[Play case 67 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-67.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-71"></a>
### Case 71: [Criar um jogo indie de nave](https://x.com/ChrisGPT/status/2078261217924087999) (by [@ChrisGPT](https://x.com/ChrisGPT))

**Use Kimi K3 Standard para uma primeira versão e compare coerência, falhas, qualidade visual e custo de tokens**

ChrisGPT relata uma primeira versão de um jogo de nave por cerca de US$ 2,50 em tokens de API. Ela foi mais coerente e teve menos bugs que a versão GPT-5.5, mas Fable 5 continuou mais polido visualmente

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-71.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-71-poster.jpg" alt="Case 71 source video poster" height="360"></a>

[Play case 71 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-71.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-73"></a>
### Case 73: [Autotestar um jogo no Summer Engine](https://x.com/MathiasHeide/status/2078231589436465199) (by [@MathiasHeide](https://x.com/MathiasHeide))

**Faça Kimi K3 executar o jogo, verificar capturas e logs e corrigir defeitos visíveis na mesma sessão**

Mathias Heide relata que Kimi K3 criou um jogo de avião de papel em uma sessão de 27 minutos, executou, examinou capturas e logs, corrigiu bugs e mudou o avião preto para branco

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-73.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-73-poster.jpg" alt="Case 73 source video poster" height="360"></a>

[Play case 73 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-73.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-77"></a>
### Case 77: [Iterar um battle royale no navegador](https://x.com/Ananth7e/status/2078158089929601203) (by [@Ananth7e](https://x.com/Ananth7e))

**Espere iterações autônomas longas e prompts posteriores específicos em jogos de navegador ricos em recursos**

Ananth relata mais de 130 minutos e 40 ciclos de capturas do Chrome para um jogo estilo PUBG, seguidos de dois prompts extras para corrigir bugs restantes

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-77.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-77-poster.jpg" alt="Case 77 source video poster" height="360"></a>

[Play case 77 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-77.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-83"></a>
### Case 83: [Expandir a paisagem de um jogo espacial](https://x.com/startracker/status/2078543423167160342) (by [@startracker](https://x.com/startracker))

**Use Kimi K3 como uma passada longa para trocar terreno provisório por um ambiente maior inspirado em dados reais.**

O criador descreve o segundo dia de um jogo espacial: Kimi K3 substituiu uma costa provisória por uma paisagem de 8 x 8 km inspirada na Islândia, adicionou oceano animado sensível à costa, refez a nave e gerou recursos ambientais para uma etapa futura. A fonte também nota execução lenta e problemas de captura de quadros.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-83.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-83-poster.jpg" alt="Case 83 source video poster" height="360"></a>

[Play case 83 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-83.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-84"></a>
### Case 84: [Desbloquear renderização física em Three.js](https://x.com/mattwatkajtys/status/2078523373861339475) (by [@mattwatkajtys](https://x.com/mattwatkajtys))

**Traga Kimi K3 para um projeto físico em Three.js quando a matemática funciona, mas o pipeline de renderização precisa avançar.**

O criador relata que um construtor de mundos físicos estava parado havia meses porque o pipeline de renderização não evoluía, embora matemática e física funcionassem. A passada com Kimi K3 fez o projeto avançar e o vídeo mostra o resultado interativo atual.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-84.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-84-poster.jpg" alt="Case 84 source video poster" height="360"></a>

[Play case 84 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-84.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-88"></a>
### Case 88: [Criar Counter-Strike no navegador em um arquivo](https://x.com/prasenx/status/2078453069021659477) (by [@prasenx](https://x.com/prasenx))

**Use Kimi K3 para gerar um FPS de navegador em arquivo único e conferir mapa, bots, armas, regras de rodada e áudio procedural.**

O criador relata um jogo tipo Counter-Strike feito com Kimi K3 em um único HTML com mais de 3.700 linhas e sem etapa de build. O artefato inclui mapa inspirado em Dust2, várias armas, recargas, bots, headshots, kill feed, rodada de dois minutos, áudio procedural, Three.js, PBR e custo de API abaixo de 5 dólares.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-88.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-88-poster.jpg" alt="Case 88 source video poster" height="360"></a>

[Play case 88 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-88.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-96"></a>
### Case 96: [Construir um jogo de pirâmide](https://x.com/ice_bearcute/status/2078828887468056763) (by [@ice_bearcute](https://x.com/ice_bearcute))

**Use Kimi K3 em uma passada de um dia para um jogo 3D de exploração, depois inspecione missões, interiores e escopo antes de julgar qualidade.**

ice_bearcute relata ter construído em um dia um jogo 3D Pyramid Expedition com Kimi K3. A fonte diz que o resultado não é só uma cena externa: jogadores podem explorar uma tumba antiga e completar missões, enquanto a mídia anexada fornece evidência visível de gameplay.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-96.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-96-poster.jpg" alt="Case 96 source video poster" height="360"></a>

[Play case 96 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-96.mp4)

Type: Demo | Date: 2026-07-19

---

<a id="case-101"></a>
### Case 101: [Comparar profundidade no Minecraft](https://x.com/vikktorrrre/status/2079294696459804762) (by [@vikktorrrre](https://x.com/vikktorrrre))

**Use este caso para avaliar o fluxo real, o custo ou os limites do Kimi K3 em “Comparar profundidade no Minecraft”.**

O post original traz evidência pública sobre “Comparar profundidade no Minecraft”, incluindo descrição do autor, mídia do resultado ou dados de benchmark/tutorial. O repositório preserva apenas fatos verificáveis e não reconstrói prompts ou etapas não publicados.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-101.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-101-poster.jpg" alt="Case 101 source video poster" height="360"></a>

[Play case 101 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-101.mp4)

Type: Evaluation | Date: 2026-07-20

---

<a id="case-102"></a>
### Case 102: [Criar um FPS de Fallout](https://x.com/kirillk_web3/status/2079290747585437781) (by [@kirillk_web3](https://x.com/kirillk_web3))

**Use este caso para avaliar o fluxo real, o custo ou os limites do Kimi K3 em “Criar um FPS de Fallout”.**

O post original traz evidência pública sobre “Criar um FPS de Fallout”, incluindo descrição do autor, mídia do resultado ou dados de benchmark/tutorial. O repositório preserva apenas fatos verificáveis e não reconstrói prompts ou etapas não publicados.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-102.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-102-poster.jpg" alt="Case 102 source video poster" height="360"></a>

[Play case 102 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-102.mp4)

Type: Demo | Date: 2026-07-20

---

<a id="case-105"></a>
### Case 105: [Lançar RPG de data center](https://x.com/demian_ai/status/2079239035596218578) (by [@demian_ai](https://x.com/demian_ai))

**Use este caso para avaliar o fluxo real, o custo ou os limites do Kimi K3 em “Lançar RPG de data center”.**

O post original traz evidência pública sobre “Lançar RPG de data center”, incluindo descrição do autor, mídia do resultado ou dados de benchmark/tutorial. O repositório preserva apenas fatos verificáveis e não reconstrói prompts ou etapas não publicados.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-105.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-105-poster.jpg" alt="Case 105 source video poster" height="360"></a>

[Play case 105 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-105.mp4)

Type: Demo | Date: 2026-07-20

---

<a id="case-108"></a>
### Case 108: [Criar jogo 3D de carros](https://x.com/LexnLin/status/2079233761242235081) (by [@LexnLin](https://x.com/LexnLin))

**Use este caso para avaliar o fluxo real, o custo ou os limites do Kimi K3 em “Criar jogo 3D de carros”.**

O post original traz evidência pública sobre “Criar jogo 3D de carros”, incluindo descrição do autor, mídia do resultado ou dados de benchmark/tutorial. O repositório preserva apenas fatos verificáveis e não reconstrói prompts ou etapas não publicados.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-poster.jpg" alt="Case 108 source video poster" height="360"></a>

[Play case 108 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-01.jpg" alt="Case 108 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-02.jpg" alt="Case 108 source image 2" height="360"></a>

Type: Demo | Date: 2026-07-20

---

<a id="case-111"></a>
### Case 111: [Comparar clones de Geometry Dash](https://x.com/Nekt_0/status/2079629004483465473) (by [@Nekt_0](https://x.com/Nekt_0))

**Compare builds com o mesmo briefing para decidir se Kimi K3 serve para protótipos jogáveis de estilo mobile.**

Nekt diz que Kimi K3 gastou cerca de 30 minutos e 200.000 tokens criando um clone de Geometry Dash com saltos, obstáculos, níveis, música e efeitos visuais, comparando com uma build do Claude Fable 5 no vídeo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-111.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-111-poster.jpg" alt="Case 111 source video poster" height="360"></a>

[Play case 111 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-111.mp4)

Type: Evaluation | Date: 2026-07-21

---

<a id="case-112"></a>
### Case 112: [Testar jogo retrô no Command Code](https://x.com/naymur_dev/status/2079627963000398334) (by [@naymur_dev](https://x.com/naymur_dev))

**Use uma rodada multi-modelo no Command Code para comparar recursos de gameplay do Kimi K3 e custo por modelo.**

Naymur relata o mesmo prompt /design no Command Code com Fable 5, GPT-5.6 Sol, Grok 4.5 e Kimi K3. O post diz que Kimi K3 gerou um jogo retrô ASCII com gameplay, níveis, balas e chefes, custando $0.15.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-112.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-112-poster.jpg" alt="Case 112 source video poster" height="360"></a>

[Play case 112 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-112.mp4)

Type: Evaluation | Date: 2026-07-21

---

<a id="case-116"></a>
### Case 116: [Avaliar o jogo Space Discoverer](https://x.com/fabriciocarraro/status/2079548607393382528) (by [@fabriciocarraro](https://x.com/fabriciocarraro))

**Use o mini-benchmark Space Discoverer para comparar saídas em um briefing genérico de jogo 3D no navegador.**

Fabricio Carraro relata um mini-benchmark com Claude Fable 5, GPT-5.6 Sol e Kimi K3 no máximo raciocínio. A tarefa foi um jogo 3D de navegador chamado Space Discoverer, e os três convergiram para Three.js sobre WebGL 2.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-116.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-116-poster.jpg" alt="Case 116 source video poster" height="360"></a>

[Play case 116 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-116.mp4)

Type: Benchmark | Date: 2026-07-21

---

<a id="case-117"></a>
### Case 117: [Criar jogo de direção com estrada real](https://x.com/bijanbowen/status/2079526003643179102) (by [@bijanbowen](https://x.com/bijanbowen))

**Prototipe um jogo de direção combinando Kimi K3 com Blender e Godot em torno de um mapa de estrada local real.**

Bijan Bowen mostra Kimi K3 criando um jogo de direção com Blender e Godot, usando como mapa um trecho real de estrada perto do criador. O vídeo anexado é a evidência pública da build.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-117.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-117-poster.jpg" alt="Case 117 source video poster" height="360"></a>

[Play case 117 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-117.mp4)

Type: Demo | Date: 2026-07-21

---


<a id="frontend-motion"></a>
## 🎨 Frontend e motion design

<a id="case-5"></a>
### Case 5: [Criar um frontend de motion graphics interativo](https://x.com/chetaslua/status/2077749371144442022) (by [@chetaslua](https://x.com/chetaslua))

**Crie gráficos que continuem interativos quando pausados**

O criador relata 42 minutos, uma execução, código simples e nenhum harness, MCP ou skill

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05-poster.jpg" alt="Case 5 source video poster" height="360"></a>

[Play case 5 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-6"></a>
### Case 6: [Produzir um anúncio animado sincronizado](https://x.com/abhinavflac/status/2077760297918484667) (by [@abhinavflac](https://x.com/abhinavflac))

**Verifique a sincronia entre música, efeitos e movimento**

O criador relata um anúncio estilo Spotify em uma execução por prompt. O prompt exato não foi publicado

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06-poster.jpg" alt="Case 6 source video poster" height="360"></a>

[Play case 6 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-14"></a>
### Case 14: [Criar motion design inteiramente em código](https://x.com/chetaslua/status/2077952938564354503) (by [@chetaslua](https://x.com/chetaslua))

**Teste se um fluxo de programação em uma execução consegue produzir motion design sem ferramentas auxiliares de geração**

O criador relata um resultado de motion design em uma execução com Kimi K3, feito totalmente em código, sem MCP, skills, ferramentas, geração de vídeo ou prompts especiais. O prompt exato não é fornecido

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-14.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-14-poster.jpg" alt="Case 14 source video poster" height="360"></a>

[Play case 14 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-14.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-15"></a>
### Case 15: [Pesquisar uma pessoa e criar um site pessoal animado](https://x.com/nicky_sap/status/2077857190707429411) (by [@nicky_sap](https://x.com/nicky_sap))

**Forneça um briefing amplo de site pessoal e examine pesquisa, planejamento, iteração e validação no navegador pelo modelo**

O criador relata que Kimi K3 pesquisou Nick Saponaro e produziu um site pessoal animado a partir de um pedido amplo, incluindo planejamento, testes, iteração e verificações no navegador. O resultado é uma demonstração de fluxo autorrelatada

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-15.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-15-poster.jpg" alt="Case 15 source video poster" height="360"></a>

[Play case 15 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-15.mp4)

Type: Tutorial | Date: 2026-07-16

---

<a id="case-17"></a>
### Case 17: [Gerar uma simulação de buraco negro](https://x.com/chetaslua/status/2077961850352971796) (by [@chetaslua](https://x.com/chetaslua))

**Use uma tarefa de visualização científica para examinar uma simulação gerada de buraco negro**

O criador mostra uma simulação de buraco negro atribuída ao Kimi K3 e a chama de melhor que já viu. A fonte traz um resultado visível, mas não prompt, rubrica ou validação independente

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-17.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-17-poster.jpg" alt="Case 17 source video poster" height="360"></a>

[Play case 17 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-17.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-22"></a>
### Case 22: [Testar modelagem complexa, partículas e shaders no frontend](https://x.com/karminski3/status/2077889959223337099) (by [@karminski3](https://x.com/karminski3))

**Use um prompt público de frontend para examinar precisão de modelagem, efeitos de partículas e geração de shaders inline em uma passagem**

O criador relata um resultado de frontend em uma passagem com Kimi K3, abrangendo modelagem precisa, efeitos de partículas e código complexo de shader inline, e afirma que o prompt de teste é público na fonte vinculada

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-22.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-22-poster.jpg" alt="Case 22 source video poster" height="360"></a>

[Play case 22 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-22.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-26"></a>
### Case 26: [Gerar uma ferramenta de música procedural em uma tentativa](https://x.com/mirochill/status/2077723551331758478) (by [@mirochill](https://x.com/mirochill))

**Teste a geração em uma execução de um gerador interativo de música procedural e compare o resultado visível com cautela**

O criador relata que Kimi K3 gerou uma ferramenta de música procedural em uma tentativa e a compara favoravelmente com resultados de Fable 5 e GPT-5.6 Sol. É o conjunto de testes do próprio criador, não um benchmark padronizado

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-26-poster.jpg" alt="Case 26 source video poster" height="360"></a>

[Play case 26 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-26.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-33"></a>
### Case 33: [Criar uma página de produto em Three.js a partir de duas imagens](https://x.com/1littlecoder/status/2077890296806031665) (by [@1littlecoder](https://x.com/1littlecoder))

**Use duas imagens de referência e uma exigência explícita de Three.js para gerar uma apresentação de produto**

O criador relata que Kimi K3 projetou uma página de produto a partir de duas imagens e produziu a versão em Three.js explicitamente solicitada. Nenhum outro detalhe de prompt ou implementação é fornecido

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-33.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-33-poster.jpg" alt="Case 33 source video poster" height="360"></a>

[Play case 33 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-33.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-39"></a>
### Case 39: [Inventar um cortador de pão de luxo e sua página de produto](https://x.com/filicroval/status/2077871090731221438) (by [@filicroval](https://x.com/filicroval))

**Combine ideação de produto, vista explodida, demonstração e landing page em um artefato de design**

O criador relata que Kimi K3 inventou um cortador de pão em estilo guilhotina, apresentou-o como produto de luxo e produziu uma landing page com vista explodida e demonstração

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-39.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-39-poster.jpg" alt="Case 39 source video poster" height="360"></a>

[Play case 39 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-39.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-45"></a>
### Case 45: [Gerar um GIF recursivo de pelicano com dez segundos](https://x.com/1littlecoder/status/2077880380900937865) (by [@1littlecoder](https://x.com/1littlecoder))

**Use um briefing completo de animação em loop para examinar continuidade narrativa e recursão em um GIF**

A fonte inclui um prompt para um GIF em loop de dez segundos, com um pelicano andando de bicicleta e recebendo o mesmo vídeo por mensagem enquanto a câmera aproxima. O criador mostra a animação resultante do Kimi K3

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-45.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-45-poster.jpg" alt="Case 45 source video poster" height="360"></a>

[Play case 45 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-45.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-55"></a>
### Case 55: [Gerar um SVG lateral de um BMW M4 CS](https://x.com/HarshithLucky3/status/2077765821380886942) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**Use um veículo e ponto de vista específicos para examinar a saída de ilustração vetorial**

O criador mostra um SVG lateral de um BMW M4 CS atribuído ao Kimi K3 Max. A fonte fornecida contém o artefato, mas não prompt ou etapas de produção

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-55-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-55-01.jpg" alt="Case 55 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-58"></a>
### Case 58: [Recriar Gargantua por feedback de capturas de tela](https://x.com/AngryTomtweets/status/2077868981659324444) (by [@AngryTomtweets](https://x.com/AngryTomtweets))

**Use capturas de tela repetidas como observações para diagnosticar e refinar uma visualização científica**

A fonte relata que Kimi K3 recriou Gargantua, de Interstellar, por meio de 62 capturas de tela próprias, lendo cada resultado, diagnosticando problemas e agindo de forma iterativa

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-58.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-58-poster.jpg" alt="Case 58 source video poster" height="360"></a>

[Play case 58 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-58.mp4)

Type: Tutorial | Date: 2026-07-16

---

<a id="case-66"></a>
### Case 66: [Refinar uma visualização de buraco negro com 62 capturas de tela](https://x.com/TokenGremlin/status/2077855959201042645) (by [@TokenGremlin](https://x.com/TokenGremlin))

**Use um ciclo de feedback por capturas de tela para ler, diagnosticar e corrigir uma simulação visual ao longo de muitas iterações**

A fonte relata que Kimi K3 reconstruiu Gargantua, de Interstellar, observando e refinando sua saída ao longo de 62 capturas de tela. Isso demonstra o ciclo de feedback relatado, não precisão física independente

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-66.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-66-poster.jpg" alt="Case 66 source video poster" height="360"></a>

[Play case 66 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-66.mp4)

Type: Tutorial | Date: 2026-07-16

---

<a id="case-68"></a>
### Case 68: [Criar um PDF de marketing sobre pós-treinamento](https://x.com/Satvik_Pen/status/2077859673517023313) (by [@Satvik_Pen](https://x.com/Satvik_Pen))

**Use um produto nomeado e um formato de entrega para gerar um documento de marketing**

O criador relata pedir ao Kimi K3 um PDF de marketing sobre o pós-treinamento Inkling da Thinking Machines e compartilha o resultado, elogiando também o processo nos bastidores. Nenhum prompt ou critério de avaliação é fornecido

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-01.png" alt="Case 68 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-02.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-02.png" alt="Case 68 source image 2" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-03.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-03.png" alt="Case 68 source image 3" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-04.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-04.png" alt="Case 68 source image 4" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-70"></a>
### Case 70: [Criar uma interface de usuário a partir de um prompt](https://x.com/BrianMRey/status/2077891942088671689) (by [@BrianMRey](https://x.com/BrianMRey))

**Use um único pedido para gerar e examinar um design completo de interface**

O criador mostra um design de interface atribuído a uma execução com um prompt no Kimi K3 e faz uma avaliação subjetiva muito positiva. O prompt exato e a rubrica não foram incluídos

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-70.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-70-poster.jpg" alt="Case 70 source video poster" height="360"></a>

[Play case 70 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-70.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-78"></a>
### Case 78: [Criar um site com estilo premiado](https://x.com/viktoroddy/status/2078140696910037002) (by [@viktoroddy](https://x.com/viktoroddy))

**Avalie a sessão gravada completa, não apenas a captura final**

Viktor Oddy publica um tutorial de 13 minutos para criar com Kimi K3 um site de estilo premiado e fornece evidência do processo completo

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-78.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-78-poster.jpg" alt="Case 78 source video poster" height="360"></a>

[Play case 78 tutorial video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-78.mp4)

Type: Tutorial | Date: 2026-07-17

---

<a id="case-81"></a>
### Case 81: [Criar frontend com metaballs no scroll](https://x.com/abhinavflac/status/2078603131055993130) (by [@abhinavflac](https://x.com/abhinavflac))

**Peça a Kimi K3 uma página estilo Awwwards com scroll e verifique se efeitos matemáticos substituem malhas ou texturas pesadas.**

O criador relata uma sessão frontend com Kimi K3 que produziu um site com metaballs reativos ao scroll usando comportamento visual matemático, sem malhas nem texturas. O vídeo anexado é o artefato visível; não há prompt reutilizável nem passos de implementação publicados.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-81.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-81-poster.jpg" alt="Case 81 source video poster" height="360"></a>

[Play case 81 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-81.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-82"></a>
### Case 82: [Redesenhar um site pessoal entre modelos](https://x.com/fabriciocarraro/status/2078574831466078265) (by [@fabriciocarraro](https://x.com/fabriciocarraro))

**Rode o mesmo brief de redesign em vários harnesses de código e compare tempo, direção visual e aderência à identidade existente.**

O criador testou Fable 5, GPT-5.6 Sol e Kimi K3 no redesign de seu site pessoal usando o harness oficial e esforço máximo de cada modelo. Kimi K3 levou cerca de 50 minutos, Fable 35 e Sol cerca de 70; a postagem trata o resultado como mini benchmark específico da tarefa.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-82.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-82-poster.jpg" alt="Case 82 source video poster" height="360"></a>

[Play case 82 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-82.mp4)

Type: Evaluation | Date: 2026-07-18

---

<a id="case-86"></a>
### Case 86: [Criar explorador interativo de couro cabeludo](https://x.com/MiaAI_lab/status/2078508824752017757) (by [@MiaAI_lab](https://x.com/MiaAI_lab))

**Use Kimi K3 para uma cena educacional 3D de uma passada com camadas anatômicas, fios responsivos e hotspots interativos.**

O criador relata que Kimi K3 gerou em uma passada um explorador realista de couro cabeludo com cerca de 105k tokens, iluminação cinematográfica, anatomia em camadas, fios de cabelo responsivos, cortes e hotspots educacionais. A fonte diz que o resultado impressiona, mas não é barato, e traz um link para testar.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-86.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-86-poster.jpg" alt="Case 86 source video poster" height="360"></a>

[Play case 86 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-86.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-87"></a>
### Case 87: [Compartilhar prompt de dashboard globo 3D](https://x.com/hqmank/status/2078465403349840144) (by [@hqmank](https://x.com/hqmank))

**Estude um prompt e uma imagem de referência para um dashboard globo 3D em Kimi K3 em vez de inferir o fluxo apenas pelo resultado final.**

O criador responde a pedidos pelo prompt e pela imagem de referência da demo de dashboard globo 3D feita com Kimi K3 e compartilha ambos nas imagens anexas. O repositório registra a fonte como fronteira tutorial de prompt, mas não transcreve texto a partir das imagens.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-87.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-87-poster.jpg" alt="Case 87 source video poster" height="360"></a>

[Play case 87 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-87.mp4)

Type: Tutorial | Date: 2026-07-18

---

<a id="case-94"></a>
### Case 94: [Executar cinco testes UI UX](https://x.com/MAXdeg0/status/2078855257686196399) (by [@MAXdeg0](https://x.com/MAXdeg0))

**Avalie Kimi K3 em várias tarefas de UI, logo e Figma MCP em vez de confiar em um único screenshot frontend.**

MAXdeg0 relata cinco testes de UI/UX e design de logo com Kimi K3 usando Claude Code e o servidor Figma MCP. A fonte lista tipos de tarefa como reconstrução de landing page, hero section e design visual, com tempo e custo concretos para pelo menos a landing.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-94.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-94-poster.jpg" alt="Case 94 source video poster" height="360"></a>

[Play case 94 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-94.mp4)

Type: Evaluation | Date: 2026-07-19

---

<a id="case-97"></a>
### Case 97: [Criar landings a partir de referências](https://x.com/MAXdeg0/status/2078776969072877715) (by [@MAXdeg0](https://x.com/MAXdeg0))

**Use boards de referência, Figma AI e Motion Sites com Kimi K3 para transformar direção visual em seções reutilizáveis de landing page.**

MAXdeg0 descreve um fluxo para landing pages: buscar estilos no Pinterest, remixar o visual com Figma AI ou colar referência de UI mais prompt no Motion Sites para Kimi K3 construir a página. O post diz que a técnica se reutiliza em mais seções e aponta para um guia completo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-97.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-97-poster.jpg" alt="Case 97 source video poster" height="360"></a>

[Play case 97 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-97.mp4)

Type: Tutorial | Date: 2026-07-19

---

<a id="case-103"></a>
### Case 103: [Seguir tutorial de site premium](https://x.com/_guillecasaus/status/2079258261014908980) (by [@_guillecasaus](https://x.com/_guillecasaus))

**Use este caso para avaliar o fluxo real, o custo ou os limites do Kimi K3 em “Seguir tutorial de site premium”.**

O post original traz evidência pública sobre “Seguir tutorial de site premium”, incluindo descrição do autor, mídia do resultado ou dados de benchmark/tutorial. O repositório preserva apenas fatos verificáveis e não reconstrói prompts ou etapas não publicados.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-103.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-103-poster.jpg" alt="Case 103 source video poster" height="360"></a>

[Play case 103 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-103.mp4)

Type: Tutorial | Date: 2026-07-20

---

<a id="case-106"></a>
### Case 106: [Comparar custos de frontend humanoide](https://x.com/ChrisGPT/status/2079236298464796958) (by [@ChrisGPT](https://x.com/ChrisGPT))

**Use este caso para avaliar o fluxo real, o custo ou os limites do Kimi K3 em “Comparar custos de frontend humanoide”.**

O post original traz evidência pública sobre “Comparar custos de frontend humanoide”, incluindo descrição do autor, mídia do resultado ou dados de benchmark/tutorial. O repositório preserva apenas fatos verificáveis e não reconstrói prompts ou etapas não publicados.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-106.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-106-poster.jpg" alt="Case 106 source video poster" height="360"></a>

[Play case 106 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-106.mp4)

Type: Benchmark | Date: 2026-07-20

---

<a id="case-115"></a>
### Case 115: [Comparar builds Three.js Kimi-vs-GLM](https://x.com/thehypedotnews/status/2079553731218325840) (by [@thehypedotnews](https://x.com/thehypedotnews))

**Rode os mesmos prompts procedurais de Three.js com Kimi K3 e GLM 5.2 para comparar comportamento frontend e 3D.**

The Hype diz que testou Kimi K3 e GLM 5.2 com três prompts de HTML único e Three.js: sala anos 80 com textura canvas em CRT, bicicleta com cinemática de transmissão e aquário de vidro.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-115.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-115-poster.jpg" alt="Case 115 source video poster" height="360"></a>

[Play case 115 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-115.mp4)

Type: Benchmark | Date: 2026-07-21

---


<a id="coding-integrations"></a>
## 💻 Código e integrações

<a id="case-18"></a>
### Case 18: [Criar um MacBook virtual com macOS funcional](https://x.com/scottstts/status/2077890054299541890) (by [@scottstts](https://x.com/scottstts))

**Combine renderização de hardware em Three.js com uma simulação interativa de sistema operacional no navegador**

A fonte relata que Kimi K3 criou um MacBook virtual em Three.js com um ambiente funcional no estilo macOS. Ela demonstra o artefato, mas não fornece etapas de implementação

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-18.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-18-poster.jpg" alt="Case 18 source video poster" height="360"></a>

[Play case 18 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-18.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-25"></a>
### Case 25: [Criar um compilador de GPU de DSL a PTX](https://x.com/rohanpaul_ai/status/2077886618657231220) (by [@rohanpaul_ai](https://x.com/rohanpaul_ai))

**Use uma tarefa completa de compilador que abranja DSL, passes, geração de PTX e um caminho de Tensor Core**

A fonte relata que Kimi K3 criou um compilador de GPU do zero, desde sua DSL e passes até a geração de PTX, e compara seu caminho de Tensor Core com Triton. Nenhum detalhe de benchmark independente consta no registro fornecido

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-25-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-25-01.png" alt="Case 25 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-32"></a>
### Case 32: [Criar um raytracer de buraco negro em tempo real no WebGL2](https://x.com/AlicanKiraz0/status/2077885419744612597) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**Teste a geração, com um prompt, de um raytracer geodésico nativo em WebGL2 dentro de um arquivo HTML**

O autor descreve um benchmark de programação que exige um raytracer funcional de curvatura da luz por buraco negro em arquivo único e WebGL2 nativo. O registro fornecido estabelece a tarefa e os modelos participantes, mas não uma auditoria independente completa dos resultados

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-32.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-32-poster.jpg" alt="Case 32 source video poster" height="360"></a>

[Play case 32 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-32.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-46"></a>
### Case 46: [Criar um emulador de Game Boy Advance com mGBA WASM](https://x.com/teortaxesTex/status/2077925090168062272) (by [@teortaxesTex](https://x.com/teortaxesTex))

**Integre um modelo 3D licenciado e um núcleo real de emulador e depois melhore recursivamente interface e jogabilidade**

O projeto Kimi K3 citado adapta um modelo AGB-001 licenciado, integra um núcleo mGBA WASM e melhora interface e jogabilidade por autoaperfeiçoamento recursivo. A publicação cita uma descrição do projeto, não uma reprodução independente

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-46-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-46-01.jpg" alt="Case 46 source image 1" height="360"></a>

Type: Integration | Date: 2026-07-17

---

<a id="case-50"></a>
### Case 50: [Pesquisar vários temas em fontes de língua chinesa](https://x.com/tphuang/status/2077911994607239400) (by [@tphuang](https://x.com/tphuang))

**Use tarefas de pesquisa longas para comparar profundidade e latência entre gerações de modelos**

O autor relata testar Kimi K3 em muitos temas de pesquisa usando fontes em chinês, considerando-o mais completo que K2.6, porém mais lento. A publicação também observa alta demanda pelo serviço naquele momento

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-50-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-50-01.png" alt="Case 50 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-17

---

<a id="case-56"></a>
### Case 56: [Clonar o macOS no navegador com aplicativos funcionais](https://x.com/twid/status/2077924755357974989) (by [@twid](https://x.com/twid))

**Crie uma simulação de sistema operacional no navegador que inclua aplicativos de música, navegador e e-mail**

A fonte relata que Kimi K3 foi usado para criar um clone do macOS no navegador com música, navegador, e-mail e outras funções. Ela não fornece detalhes de implementação

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-56.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-56-poster.jpg" alt="Case 56 source video poster" height="360"></a>

[Play case 56 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-56.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-62"></a>
### Case 62: [Criar uma simulação de macOS com FaceTime funcional](https://x.com/LinearUncle/status/2077919552239997078) (by [@LinearUncle](https://x.com/LinearUncle))

**Use uma tarefa de sistema operacional virtual para testar se uma interação de aplicativo gerada funciona**

O criador mostra um ambiente no estilo macOS atribuído ao Kimi K3 e relata que seu recurso FaceTime funciona. A fonte não fornece etapas de configuração ou validação

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-62-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-62-01.jpg" alt="Case 62 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-17

---

<a id="case-64"></a>
### Case 64: [Adicionar um comparador de efeitos de frontend com duas tarefas](https://x.com/MinLiBuilds/status/2077939461510615376) (by [@MinLiBuilds](https://x.com/MinLiBuilds))

**Crie uma ferramenta que selecione duas tarefas concluídas, exiba-as lado a lado e sincronize visualizações e interações**

O criador relata ter pedido ao Kimi K3 um fluxo de comparação de frontend com seleção de tarefas, dois painéis de navegador, modos de objeto e navegação, pontos de vista sincronizados e testes de interação. A publicação também observa limitações mais amplas do modelo

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-64.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-64-poster.jpg" alt="Case 64 source video poster" height="360"></a>

[Play case 64 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-64.mp4)

Type: Tutorial | Date: 2026-07-17

---

<a id="case-75"></a>
### Case 75: [Configurar Kimi como subagente do Codex](https://x.com/nauczymycieAI/status/2078181182701736132) (by [@nauczymycieAI](https://x.com/nauczymycieAI))

**Mantenha a orquestração no Codex e delegue o frontend a um subagente Kimi K3 OpenCode com limite claro para segredos**

nauczymycieAI explica a instalação do OpenCode, criação manual da chave Kimi sem colá-la no Codex, conexão com Kimi K3 e um skill global do Codex para rotear tarefas de frontend

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-75.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-75.jpg" alt="Case 75 source image 1" height="360"></a>

Type: Tutorial | Date: 2026-07-17

---

<a id="case-79"></a>
### Case 79: [Rotear código simples pelo ChatLLM](https://x.com/abacusai/status/2078022418661257411) (by [@abacusai](https://x.com/abacusai))

**Envie código simples ao Kimi K3 e reserve código difícil e design para outros modelos**

Abacus AI anuncia Kimi K3 no ChatLLM: código simples com Kimi K3, código difícil com Fable 5 e design com GPT-5.6 Sol. O roteador funciona no ChatLLM, Abacus AI Agent e Claude Code

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-79.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-79.jpg" alt="Case 79 source image 1" height="360"></a>

Type: Integration | Date: 2026-07-17

---

<a id="case-91"></a>
### Case 91: [Criar CS com assets gerados](https://x.com/karankendre/status/2078938615900688728) (by [@karankendre](https://x.com/karankendre))

**Combine Kimi K3 para o código do jogo com GPT Image 2 para os assets ao prototipar um pequeno jogo estilo Counter-Strike no navegador.**

Karan Kendre relata usar Kimi K3 para criar o jogo e GPT Image 2 para criar os assets de um projeto estilo Counter-Strike, com custo total perto de 10 dólares. O vídeo fonte é o artefato visível, então o registro vale como fluxo de combinação de ferramentas, não como benchmark só de Kimi.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-91.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-91-poster.jpg" alt="Case 91 source video poster" height="360"></a>

[Play case 91 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-91.mp4)

Type: Integration | Date: 2026-07-19

---

<a id="case-95"></a>
### Case 95: [Usar a skill Design do Command Code](https://x.com/MrAhmadAwais/status/2078841789205934547) (by [@MrAhmadAwais](https://x.com/MrAhmadAwais))

**Combine Kimi K3 com uma skill dedicada de design no Command Code ao criar um protótipo visual de jogo dentro de orçamento de tokens.**

Ahmad Awais relata usar Kimi K3 com Command Code e a skill /design para um jogo com câmera de perseguição estilo Forza. O post diz que a sessão custou 0,97 dólar e incluiu correções de escala da estrada e do carro, fundo, animação e neblina, formando um fluxo concreto de harness de agente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-95.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-95-poster.jpg" alt="Case 95 source video poster" height="360"></a>

[Play case 95 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-95.mp4)

Type: Integration | Date: 2026-07-19

---

<a id="case-109"></a>
### Case 109: [Rodar Kimi K3 no Claude Code](https://x.com/boxmining/status/2079115758618239337) (by [@boxmining](https://x.com/boxmining))

**Use este caso para avaliar o fluxo real, o custo ou os limites do Kimi K3 em “Rodar Kimi K3 no Claude Code”.**

O post original traz evidência pública sobre “Rodar Kimi K3 no Claude Code”, incluindo descrição do autor, mídia do resultado ou dados de benchmark/tutorial. O repositório preserva apenas fatos verificáveis e não reconstrói prompts ou etapas não publicados.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-109.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-109-poster.jpg" alt="Case 109 source video poster" height="360"></a>

[Play case 109 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-109.mp4)

Type: Integration | Date: 2026-07-20

---

<a id="case-119"></a>
### Case 119: [Roteiar Kimi via claude-code-router](https://x.com/sairahul1/status/2079393675885588855) (by [@sairahul1](https://x.com/sairahul1))

**Teste Kimi K3 em um fluxo Claude Code existente via claude-code-router evitando modo proxy desnecessário.**

Sai Rahul descreve suporte patrocinado pela Moonshot para Kimi K3 no claude-code-router, com presets, importação de chave ou assinatura, roteamento nativo, dashboard de saldo e uso, failover, preço de cache e alerta para deixar proxy desligado salvo necessidade.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-119.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-119-poster.jpg" alt="Case 119 source video poster" height="360"></a>

[Play case 119 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-119.mp4)

Type: Integration | Date: 2026-07-21

---


<a id="evaluation-limits"></a>
## 🧪 Avaliação e limites

<a id="case-7"></a>
### Case 7: [Comparar design de frontend na tarefa de lava lamp do BridgeBench](https://x.com/bridgemindai/status/2077868061953007908) (by [@bridgemindai](https://x.com/bridgemindai))

**Use a tarefa de lava lamp do BridgeBench como uma comparação delimitada de design de frontend, não como ranking universal**

A BridgeMind AI relata que Kimi K3 superou Fable 5 em sua tarefa de lava lamp do BridgeBench e ficou em primeiro na arena citada. São resultados comparativos relatados pela editora

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-07.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-07-poster.jpg" alt="Case 7 source video poster" height="360"></a>

[Play case 7 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-07.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-8"></a>
### Case 8: [Avaliar roteiros com voz editorial](https://x.com/Whats_AI/status/2077860441380798908) (by [@Whats_AI](https://x.com/Whats_AI))

**Meça adequação à voz editorial, posição relativa e custo por roteiro dentro de um benchmark interno claramente identificado**

Whats_AI relata resultados internos iniciais de 2.840 Elo, primeiro lugar em seu quadro e cerca de US$ 0,25 por roteiro. Trate-os como benchmark preliminar de uma organização, não como garantia geral de desempenho ou preço

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-08-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-08-01.jpg" alt="Case 8 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-16

---

<a id="case-10"></a>
### Case 10: [Comparar design, custo e dificuldade de jogos no estilo Flappy](https://x.com/MrAhmadAwais/status/2077915347974557862) (by [@MrAhmadAwais](https://x.com/MrAhmadAwais))

**Registre configurações de dificuldade, custo, design e recursos de jogabilidade ao comparar jogos gerados**

O benchmark interno Flappy da Command Code relata configurações de dificuldade diferentes entre modelos e lista Kimi K3 a US$ 0,024, Fable 5 a US$ 0,42 e GPT-5.6 Sol a US$ 0,15. As configurações desiguais tornam esta uma comparação interna delimitada

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-10.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-10-poster.jpg" alt="Case 10 source video poster" height="360"></a>

[Play case 10 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-10.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-12"></a>
### Case 12: [Comparar design de jogos com o mesmo prompt de design](https://x.com/CommandCodeAI/status/2077921526213746948) (by [@CommandCodeAI](https://x.com/CommandCodeAI))

**Mantenha o prompt de design constante e examine ritmo, senso de design e sensação de jogabilidade separadamente**

A Command Code relata uma comparação com o mesmo prompt entre Kimi K3, GPT-5.6 Sol e Fable 5. A publicação diz que Kimi K3 foi bem em senso de design, enquanto os outros dois jogavam rápido demais; essa continua sendo a avaliação da editora

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-12.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-12-poster.jpg" alt="Case 12 source video poster" height="360"></a>

[Play case 12 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-12.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-13"></a>
### Case 13: [Exigir revisão independente em auditorias estatísticas](https://x.com/emollick/status/2077869293031624793) (by [@emollick](https://x.com/emollick))

**Combine auditorias estatísticas geradas por modelo com revisão independente de especialista ou de outro modelo antes de confiar nos achados**

Ethan Mollick relata que Kimi K3 Max aplicou estatística incorretamente ao auditar trabalhos acadêmicos anteriores e concorda com uma crítica separada. Este exemplo negativo apoia verificação independente, não aceitação sem revisão

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-13-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-13-01.jpg" alt="Case 13 source image 1" height="360"></a>

Type: Limit | Date: 2026-07-16

---

<a id="case-16"></a>
### Case 16: [Avaliar uma execução de frontend lenta, mas forte](https://x.com/Lentils80/status/2077387333154857151) (by [@Lentils80](https://x.com/Lentils80))

**Registre o tempo de conclusão junto com a qualidade da saída ao testar uma tarefa de frontend**

O criador relata que uma execução de frontend com Kimi K3 levou 35 minutos e descreve a saída como uma das melhores vistas para aquele prompt. Tanto a velocidade quanto a qualidade são observações de um único usuário

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-16.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-16-poster.jpg" alt="Case 16 source video poster" height="360"></a>

[Play case 16 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-16.mp4)

Type: Evaluation | Date: 2026-07-15

---

<a id="case-20"></a>
### Case 20: [Testar falhas de prenúncio em narrativas de mistério](https://x.com/emollick/status/2077951790868238616) (by [@emollick](https://x.com/emollick))

**Avalie se um mistério gerado equilibra pistas, obscuridade e prenúncio**

Ethan Mollick relata que Kimi K3 não escreveu um bom mistério de assassinato, tornando as pistas óbvias e obscuras demais e falhando no prenúncio. Ele também observa que outros modelos compartilham essa limitação

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-01.jpg" alt="Case 20 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-02.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-02.png" alt="Case 20 source image 2" height="360"></a>

Type: Limit | Date: 2026-07-17

---

<a id="case-21"></a>
### Case 21: [Comparar modelagem e animação da Millennium Falcon](https://x.com/gmi_cloud/status/2077903360263676090) (by [@gmi_cloud](https://x.com/gmi_cloud))

**Use pedidos de estilo e configurações de esforço equivalentes para comparar modelagem 3D, animação, tempo e custo**

A GMI Cloud relata a comparação entre Kimi K3 e Fable 5 em recriações pixeladas e no estilo original da Millennium Falcon com esforço máximo. Diz que Kimi K3 levou mais tempo, mas custou cerca de um terço no primeiro teste e menos da metade em outro; são resultados relatados pelo provedor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-21.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-21-poster.jpg" alt="Case 21 source video poster" height="360"></a>

[Play case 21 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-21.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-28"></a>
### Case 28: [Analisar uma coleção de dez projetos com Kimi K3](https://x.com/minchoi/status/2077957907857994006) (by [@minchoi](https://x.com/minchoi))

**Use uma coletânea de projetos vinculada para descobrir artefatos concretos que devem ser verificados separadamente**

O autor seleciona dez exemplos de Kimi K3 com mídia, incluindo um emulador de Game Boy Advance. Este registro é uma coleção, não um único fluxo reproduzível, portanto cada exemplo vinculado deve ser verificado de forma independente

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-28.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-28-poster.jpg" alt="Case 28 source video poster" height="360"></a>

[Play case 28 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-28.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-29"></a>
### Case 29: [Comparar uma landing page avançada entre quatro modelos](https://x.com/doutorcaleb/status/2077904020471947773) (by [@doutorcaleb](https://x.com/doutorcaleb))

**Mantenha constante o pedido de landing page e examine profundidade de animação e conclusão nas saídas dos modelos**

O criador relata ter dado o mesmo prompt avançado de landing page a Kimi K3, Fable, Grok e GPT Terra, e considera Kimi K3 o resultado mais forte. É uma comparação autorrelatada de uma tarefa

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-29.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-29-poster.jpg" alt="Case 29 source video poster" height="360"></a>

[Play case 29 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-29.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-30"></a>
### Case 30: [Avaliar mecânicas e custos de jogos retrô](https://x.com/adxtyahq/status/2077860500462055570) (by [@adxtyahq](https://x.com/adxtyahq))

**Compare jogabilidade, física, mecânicas, comportamento autônomo, uso de tokens e custo nas mesmas tarefas de jogos retrô**

A fonte relata testes com o mesmo prompt para Road Fighter, Battle City e Q*bert e lista US$ 0,28 para Kimi K3, US$ 0,28 para GPT-5.6 e US$ 0,54 para Opus 4.8. Estes são números do benchmark da editora

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-30.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-30-poster.jpg" alt="Case 30 source video poster" height="360"></a>

[Play case 30 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-30.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-31"></a>
### Case 31: [Comparar geração de jogos com Fable 5](https://x.com/higgsfield_ai/status/2077943629633712490) (by [@higgsfield_ai](https://x.com/higgsfield_ai))

**Use um exemplo lado a lado de jogos gerados como avaliação estreita, não como veredito amplo sobre os modelos**

A Higgsfield apresenta uma comparação de geração de jogos entre Kimi K3 e Fable 5. O registro fornecido inclui a mídia comparativa, mas não prompt, rubrica de pontuação ou condições detalhadas

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-31.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-31-poster.jpg" alt="Case 31 source video poster" height="360"></a>

[Play case 31 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-31.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-34"></a>
### Case 34: [Comparar tarefas complexas de frontend e desenvolvimento com Opus 4.8](https://x.com/op7418/status/2077969583018066116) (by [@op7418](https://x.com/op7418))

**Use várias tarefas complexas de programação para identificar vitórias e derrotas, sem declarar um modelo universalmente superior**

O avaliador relata testes diretos entre Kimi K3 e Opus 4.8 e os considera aproximadamente comparáveis em frontend e desenvolvimento complexos, com resultados mistos. Essa continua sendo a avaliação de uma pessoa

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-34.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-34-poster.jpg" alt="Case 34 source video poster" height="360"></a>

[Play case 34 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-34.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-35"></a>
### Case 35: [Analisar benchmarks e um teste de landing page](https://x.com/adamuchigabriel/status/2077880433925120471) (by [@adamuchigabriel](https://x.com/adamuchigabriel))

**Combine contexto de benchmark com um teste concreto de geração de landing page, mantendo separados os dois tipos de evidência**

O vídeo apresenta discussão de benchmarks, um teste de landing page e observações de design de frontend para Kimi K3. O registro fornecido não traz o prompt completo nem a rubrica de pontuação

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-35.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-35-poster.jpg" alt="Case 35 source video poster" height="360"></a>

[Play case 35 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-35.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-37"></a>
### Case 37: [Avaliar raciocínio indutivo com tarefas de grafo para fórmula](https://x.com/s_batzoglou/status/2077884096307454119) (by [@s_batzoglou](https://x.com/s_batzoglou))

**Meça correção, comportamento em holdout e complexidade de fórmula em tarefas de indução de primeira ordem**

O autor relata um benchmark de Kimi K3 e outros modelos na tarefa INDUCTION da ICML, usando de 6 a 10 pequenos grafos com 8 a 10 elementos cada para inferir uma fórmula de primeira ordem. A publicação diz que os resultados foram atualizados em relação a trabalho anterior; não se alega nova reprodução independente aqui

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-37-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-37-01.png" alt="Case 37 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-16

---

<a id="case-38"></a>
### Case 38: [Analisar relatos sobre jogos, landing pages, 3D e contexto longo](https://x.com/servasyy_ai/status/2077903775113834689) (by [@servasyy_ai](https://x.com/servasyy_ai))

**Use uma coletânea de várias fontes para comparar artefatos concretos e observar limites de velocidade junto a alegações de custo**

O autor resume testes relatados de Kimi K3 em jogos, landing pages, geração 3D e contexto longo, concluindo que vale testar, mas ainda não substitui Fable 5. Todos os números são relatos secundários desta coletânea

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-38-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-38-01.jpg" alt="Case 38 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-40"></a>
### Case 40: [Auditar um plano complexo e contestar suas soluções](https://x.com/doodlestein/status/2077901883637665958) (by [@doodlestein](https://x.com/doodlestein))

**Use um segundo modelo para identificar achados subestimados, soluções incorretas e conclusões que devem ser rejeitadas**

O criador relata que Kimi K3 analisou um plano muito refinado e concluiu que problemas graves foram subestimados, cerca de um terço das soluções propostas precisava de correção e um achado foi refutado. São resultados dessa auditoria específica

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-40-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-40-01.jpg" alt="Case 40 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-41"></a>
### Case 41: [Comparar diagramas ASCII de aprendizado por reforço no estilo PPO](https://x.com/dejavucoder/status/2077872015856615541) (by [@dejavucoder](https://x.com/dejavucoder))

**Mantenha constante um prompt de diagrama ASCII e compare como os modelos representam o ciclo de aprendizado por reforço**

A fonte fornece o prompt para desenhar em ASCII um ciclo de aprendizado por reforço no estilo PPO e mostra Kimi K3 Max ao lado de Fable 5 High. O julgamento continua sendo uma comparação visual de uma tarefa

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-01.png" alt="Case 41 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-02.jpg" alt="Case 41 source image 2" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-42"></a>
### Case 42: [Modelar no Blender enquanto se monitoram erros de capacidade](https://x.com/Angaisb_/status/2077910845523214668) (by [@Angaisb_](https://x.com/Angaisb_))

**Avalie o progresso parcial no Blender junto com a confiabilidade do serviço, em vez de julgar apenas o artefato**

O criador mostra progresso de modelagem no Blender com Kimi K3 e também relata erros repetidos de capacidade. O trabalho está incompleto na fonte fornecida, portanto o resultado parcial e a limitação de confiabilidade devem ser considerados em conjunto

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-42-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-42-01.jpg" alt="Case 42 source image 1" height="360"></a>

Type: Limit | Date: 2026-07-17

---

<a id="case-47"></a>
### Case 47: [Comparar geração de Flappy Bird em uma arena](https://x.com/jun_song/status/2077396996865003739) (by [@jun_song](https://x.com/jun_song))

**Use uma tarefa de arena para comparar dois resultados gerados de Flappy Bird, mantendo o julgamento específico à tarefa**

O criador relata uma comparação de Arena entre Kimi K3 e Opus 4.8 em uma tarefa de Flappy Bird e considera Kimi K3 significativamente melhor. Nenhum prompt completo ou rubrica consta no registro

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-47.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-47-poster.jpg" alt="Case 47 source video poster" height="360"></a>

[Play case 47 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-47.mp4)

Type: Evaluation | Date: 2026-07-15

---

<a id="case-52"></a>
### Case 52: [Resolver um problema de indução visual de Bongard com uma ferramenta](https://x.com/IntuitMachine/status/2077885406528311561) (by [@IntuitMachine](https://x.com/IntuitMachine))

**Teste se o uso de ferramentas ajuda a derivar a regra visual em uma tarefa de raciocínio de Bongard**

O criador relata que Kimi K3 usou uma ferramenta para resolver um problema de Bongard que Grok 4.5 e Muse Spark 1.1 não resolveram na mesma comparação. É o resultado da tarefa de um usuário, não um benchmark geral de raciocínio

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-52-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-52-01.jpg" alt="Case 52 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-53"></a>
### Case 53: [Comparar bom gosto em frontend e design 3D com GPT-5.6 Sol](https://x.com/filicroval/status/2077736407506751952) (by [@filicroval](https://x.com/filicroval))

**Examine recursos, gosto visual, elegância e execução 3D em uma comparação delimitada de frontend**

O criador compara Kimi K3 e GPT-5.6 Sol em design de frontend e considera Kimi K3 mais forte em gosto visual, elegância e capacidade 3D. A avaliação é subjetiva e específica à tarefa

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-53.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-53-poster.jpg" alt="Case 53 source video poster" height="360"></a>

[Play case 53 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-53.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-57"></a>
### Case 57: [Comparar geração de sites entre três modelos](https://x.com/pengchujin/status/2077962916226298340) (by [@pengchujin](https://x.com/pengchujin))

**Use saídas visíveis de sites para comparar Kimi K3, Fable 5 e GPT-5.6 Sol em um teste**

O criador apresenta uma comparação de geração de sites entre Kimi K3, Fable 5 e GPT-5.6 Sol. O registro fornecido não expõe o prompt completo nem uma rubrica de pontuação

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-57.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-57-poster.jpg" alt="Case 57 source video poster" height="360"></a>

[Play case 57 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-57.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-59"></a>
### Case 59: [Comparar geração procedural de jogos 3D e custo](https://x.com/adxtyahq/status/2077958193511362856) (by [@adxtyahq](https://x.com/adxtyahq))

**Mantenha um prompt constante entre modelos e examine roleta, caça-níquel e pinball gerados com o custo por execução**

A editora relata uma comparação multimodelo de jogos 3D procedurais e lista custos como US$ 0,71 para Kimi K3 e US$ 0,30 para Grok 4.5. Trate todos os rankings e custos como resultados da execução da editora

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-59.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-59-poster.jpg" alt="Case 59 source video poster" height="360"></a>

[Play case 59 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-59.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-69"></a>
### Case 69: [Comparar detalhes e iluminação de uma cena 3D de arsenal](https://x.com/hakki_alkan/status/2077887013332636032) (by [@hakki_alkan](https://x.com/hakki_alkan))

**Examine densidade de objetos, iluminação e detalhes da cena em uma comparação delimitada entre Kimi K3 e Opus 4.8**

A fonte relata que Kimi K3 produziu uma cena detalhada de arsenal com prateleiras abastecidas, caixas e iluminação realista, enquanto Opus 4.8 produziu uma sala vazia. É um relato comparativo de terceiros, não um benchmark independente

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-69-poster.jpg" alt="Case 69 source video poster" height="360"></a>

[Play case 69 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-69.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-72"></a>
### Case 72: [Comparar frontends com prompts Arena idênticos](https://x.com/arena/status/2078240399517524365) (by [@arena](https://x.com/arena))

**Use prompts idênticos e resultados lado a lado em vez de depender de uma única posição no ranking**

Arena.ai publica uma comparação Frontend Code Arena entre Kimi K3 e Fable 5 com prompts idênticos. O vídeo preserva os dois resultados sob a mesma condição

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-72.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-72-poster.jpg" alt="Case 72 source video poster" height="360"></a>

[Play case 72 comparison video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-72.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-74"></a>
### Case 74: [Avaliar Kimi Code em agentes de código](https://x.com/ArtificialAnlys/status/2078230240766345330) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Avalie Kimi K3 em vários testes e no custo por tarefa sem generalizar um ranking de frontend**

Artificial Analysis relata 57 pontos e quinto lugar conjunto: 84% no Terminal-Bench v2, 64% no DeepSWE, 23% no SWE-Atlas-QnA e custo médio de US$ 3,18 por tarefa

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-74.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-74.jpg" alt="Case 74 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-17

---

<a id="case-76"></a>
### Case 76: [Comparar Arena e o teste de reparo](https://x.com/AlphaSignalAI/status/2078172629496746183) (by [@AlphaSignalAI](https://x.com/AlphaSignalAI))

**Veja preferência de frontend e reparo de repositório porque Kimi K3 pode ficar em primeiro em um e sétimo em outro**

AlphaSignal relata primeiro lugar com 1.679 pontos no Frontend Code Arena, mas 53 acertos em 67, ou 79%, e sétimo lugar em um teste de reparo de agentes

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-76.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-76.jpg" alt="Case 76 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-17

---

<a id="case-80"></a>
### Case 80: [Avaliar Kimi K3 no Prinzbench](https://x.com/deredleritt3r/status/2078606700496773166) (by [@deredleritt3r](https://x.com/deredleritt3r))

**Use uma atualização independente de benchmark para comparar Kimi K3 com modelos abertos e de fronteira em busca, raciocínio e consistência.**

O autor adiciona Kimi K3 ao Prinzbench e relata pontuação geral de 47/99, acima do GLM-5.2 com 30/99 e perto de um resultado antigo do Gemini 3.1 Pro com 50/99. A postagem destaca busca forte, raciocínio lógico mais fraco e maior inconsistência que modelos de fronteira comparáveis.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-80-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-80-01.png" alt="Case 80 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-18

---

<a id="case-85"></a>
### Case 85: [Comparar geração de gêmeo digital da ISS](https://x.com/AIsaOneHQ/status/2078519527588200536) (by [@AIsaOneHQ](https://x.com/AIsaOneHQ))

**Use um desafio 3D com o mesmo prompt para comparar Kimi K3 e GPT-5.6 Sol em reconstrução, controles, rótulos e detalhe visual.**

AIsaOneHQ relata um benchmark one-shot no qual ambos os modelos reconstruíram um gêmeo digital interativo da Estação Espacial Internacional sem modelo pronto, incluindo Terra, iluminação orbital, controles, rótulos, tours, vista explodida, testes e refinamento. A postagem diz que Kimi K3 terminou mais rápido, custou menos e renderizou melhor nessa rodada.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-85.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-85-poster.jpg" alt="Case 85 source video poster" height="360"></a>

[Play case 85 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-85.mp4)

Type: Benchmark | Date: 2026-07-18

---

<a id="case-89"></a>
### Case 89: [Revisar um mundo florestal WebGPU](https://x.com/stas_sorokin_/status/2078435840728908093) (by [@stas_sorokin_](https://x.com/stas_sorokin_))

**Avalie Kimi K3 como cérebro de agente de código em uma construção longa com Three.js e WebGPU, incluindo qualidade, velocidade, consistência e taxa de edição.**

O criador relata uma revisão profunda usando Kimi K3 em um mundo de floresta e lago com Three.js e WebGPU, água viva, clima, fauna, ciclo dia-noite e câmeras cinematográficas. A postagem diz que Kimi K3 entregou qualidade alta, foi mais lento que uma geração comparável com GPT-5.6 Sol, manteve consistência e exigiu só um ajuste manual de luminosidade.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-89.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-89-poster.jpg" alt="Case 89 source video poster" height="360"></a>

[Play case 89 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-89.mp4)

Type: Evaluation | Date: 2026-07-18

---

<a id="case-90"></a>
### Case 90: [Comparar prompts de casa de vidro](https://x.com/RoundtableSpace/status/2079004612070416755) (by [@RoundtableSpace](https://x.com/RoundtableSpace))

**Use uma cena arquitetônica com o mesmo prompt para comparar Kimi K3 e Opus 4.8 em atmosfera, iluminação e completude espacial.**

Roundtable Space relata uma comparação com o mesmo prompt entre Kimi K3 e Claude Opus 4.8 por preço parecido. O resultado do Kimi é descrito como uma casa de vidro na hora azul com luz interna quente, piscina refletiva e detalhes de plantas, enquanto o Opus aparece como uma saída mais tipográfica e menos espacial.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-90.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-90-poster.jpg" alt="Case 90 source video poster" height="360"></a>

[Play case 90 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-90.mp4)

Type: Evaluation | Date: 2026-07-20

---

<a id="case-92"></a>
### Case 92: [Avaliar um gol de futebol voxel](https://x.com/0xzynex/status/2078920667542487230) (by [@0xzynex](https://x.com/0xzynex))

**Execute o mesmo prompt de animação de futebol em HTML/CSS/JS puro em dois modelos para comparar movimento e custo.**

0xzynex relata uma comparação one-shot, sem tentativas extras, na qual Kimi K3 e GPT-5.6 Sol High criaram uma jogada de futebol em blocos com drible, gol, câmera dinâmica e comemoração em código de navegador. O post diz que Kimi gerou movimento mais fluido e custo menor, com o vídeo preservando o artefato.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-92.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-92-poster.jpg" alt="Case 92 source video poster" height="360"></a>

[Play case 92 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-92.mp4)

Type: Benchmark | Date: 2026-07-19

---

<a id="case-93"></a>
### Case 93: [Revisar uma prova Minecraft](https://x.com/ashen_one/status/2078892418976666071) (by [@ashen_one](https://x.com/ashen_one))

**Assista a uma revisão estruturada de Minecraft antes de aceitar hype de lançamento ou preço como evidência suficiente.**

ashen_one publica uma revisão gravada de Kimi K3 com capítulos sobre hype versus realidade, benchmarks, preço, teste Minecraft, bugs de primeira execução e veredito final. A fonte é útil por reunir enquadramento de benchmark e notas iniciais de confiabilidade em um vídeo inspecionável.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-93.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-93-poster.jpg" alt="Case 93 source video poster" height="360"></a>

[Play case 93 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-93.mp4)

Type: Benchmark | Date: 2026-07-19

---

<a id="case-98"></a>
### Case 98: [Medir limites de nível da API](https://x.com/mnmn94253156337/status/2078739859154620497) (by [@mnmn94253156337](https://x.com/mnmn94253156337))

**Planeje execuções de agente com Kimi K3 por tokens, nível, TPM e TPD, não só pelo preço de manchete do modelo.**

A fonte em chinês relata uma experiência pessoal com a API do Kimi K3 após carregar 5 dólares, vendo cerca de 1,1 dólar consumido na configuração e depois batendo limites Tier0. Ela lista preços de entrada, entrada em cache e saída, além de TPM e TPD, servindo como relatório inicial de limitação.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-98.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-98-poster.jpg" alt="Case 98 source video poster" height="360"></a>

[Play case 98 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-98.mp4)

Type: Limit | Date: 2026-07-19

---

<a id="case-99"></a>
### Case 99: [Comparar um demo estilo Limbo](https://x.com/ChrisGPT/status/2078679211116835017) (by [@ChrisGPT](https://x.com/ChrisGPT))

**Compare escopo jogável, polimento, custo e bugs ao testar Kimi K3 contra Fable 5 no mesmo protótipo de jogo.**

ChrisGPT compara Fable 5 e Kimi K3 em um demo tipo Limbo. O post informa 2.400 linhas e 24K tokens por 1,20 dólar para Fable, contra 3.000 linhas e 30K tokens por 0,12 dólar para Kimi, com mais gameplay, mas também mais bugs.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-99.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-99-poster.jpg" alt="Case 99 source video poster" height="360"></a>

[Play case 99 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-99.mp4)

Type: Benchmark | Date: 2026-07-19

---

<a id="case-100"></a>
### Case 100: [Revisar custos do VulcanBench](https://x.com/morganlinton/status/2079358902194569357) (by [@morganlinton](https://x.com/morganlinton))

**Use este caso para avaliar o fluxo real, o custo ou os limites do Kimi K3 em “Revisar custos do VulcanBench”.**

O post original traz evidência pública sobre “Revisar custos do VulcanBench”, incluindo descrição do autor, mídia do resultado ou dados de benchmark/tutorial. O repositório preserva apenas fatos verificáveis e não reconstrói prompts ou etapas não publicados.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-100-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-100-01.jpg" alt="Case 100 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-21

---

<a id="case-104"></a>
### Case 104: [Avaliar física de pêndulo duplo](https://x.com/AlicanKiraz0/status/2079241239736504768) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**Use este caso para avaliar o fluxo real, o custo ou os limites do Kimi K3 em “Avaliar física de pêndulo duplo”.**

O post original traz evidência pública sobre “Avaliar física de pêndulo duplo”, incluindo descrição do autor, mídia do resultado ou dados de benchmark/tutorial. O repositório preserva apenas fatos verificáveis e não reconstrói prompts ou etapas não publicados.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-104.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-104-poster.jpg" alt="Case 104 source video poster" height="360"></a>

[Play case 104 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-104.mp4)

Type: Benchmark | Date: 2026-07-20

---

<a id="case-107"></a>
### Case 107: [Revisar prontidão no ReactBench](https://x.com/aidenybai/status/2079233934693650567) (by [@aidenybai](https://x.com/aidenybai))

**Use este caso para avaliar o fluxo real, o custo ou os limites do Kimi K3 em “Revisar prontidão no ReactBench”.**

O post original traz evidência pública sobre “Revisar prontidão no ReactBench”, incluindo descrição do autor, mídia do resultado ou dados de benchmark/tutorial. O repositório preserva apenas fatos verificáveis e não reconstrói prompts ou etapas não publicados.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-107.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-107-poster.jpg" alt="Case 107 source video poster" height="360"></a>

[Play case 107 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-107.mp4)

Type: Benchmark | Date: 2026-07-20

---

<a id="case-110"></a>
### Case 110: [Avaliar Kimi K3 no AA-Briefcase](https://x.com/ArtificialAnlys/status/2079715807983210572) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Use os resultados do AA-Briefcase para julgar Kimi K3 em tarefas agentic de trabalho do conhecimento antes de confiar em rankings.**

A Artificial Analysis informa que Kimi K3 marcou 1543 Elo no AA-Briefcase, em segundo lugar atrás do Claude Fable 5, observando quase uma hora por tarefa e custo maior que Opus 4.8 neste benchmark.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-110-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-110-01.jpg" alt="Case 110 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-21

---

<a id="case-113"></a>
### Case 113: [Auditar ressalvas do leaderboard frontend](https://x.com/RetroChainer/status/2079622227796885850) (by [@RetroChainer](https://x.com/RetroChainer))

**Use esta nota de limite para separar vitórias de Kimi K3 em leaderboard de afirmações gerais sobre coding e custo.**

RetroChainer confirma a liderança no Frontend Code Arena e o preço listado, mas aponta ressalvas: o ranking é específico daquele quadro, os pesos ainda não eram públicos, a economia por tarefa veio de uma única tarefa e o raciocínio máximo pode gastar tokens demais em trabalhos pequenos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-113.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-113-poster.jpg" alt="Case 113 source video poster" height="360"></a>

[Play case 113 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-113.mp4)

Type: Limit | Date: 2026-07-21

---

<a id="case-114"></a>
### Case 114: [Comparar resultados StackPerf de arquitetura](https://x.com/tamsi_besson/status/2079573266855834071) (by [@tamsi_besson](https://x.com/tamsi_besson))

**Use StackPerf para comparar Kimi K3 e Qwen 3.8 em qualidade arquitetural, velocidade e chamadas de ferramenta.**

Tamsi Besson compartilha um snapshot do StackPerf em que Kimi K3 supera levemente Qwen 3.8 Max Preview em qualidade e roda mais rápido no total, enquanto Qwen tem zero chamadas de ferramenta falhas contra duas do Kimi.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-114-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-114-01.jpg" alt="Case 114 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-21

---

<a id="case-118"></a>
### Case 118: [Comparar custos com prompt Monument Valley](https://x.com/AiHubMix/status/2079507420083294557) (by [@AiHubMix](https://x.com/AiHubMix))

**Use um único prompt estilo Monument Valley para comparar qualidade visual, tempo e custo entre Kimi K3 e pares.**

AiHubMix compara Claude Fable 5, Kimi K3 e GPT-5.6 Sol em um prompt estilo Monument Valley. O post relata Fable como mais coerente, Kimi como mais lento com 52m30s e $1.50, e GPT-5.6 Sol como mais rápido e barato, mas mais fraco em lógica espacial.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-118.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-118-poster.jpg" alt="Case 118 source video poster" height="360"></a>

[Play case 118 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-118.mp4)

Type: Benchmark | Date: 2026-07-21

---

<a id="related-resources"></a>
## Recursos relacionados

- [Ver detalhes e preços do Kimi K3 na EvoLink](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=landing_overview)
- [Abrir a documentação da API Kimi K3 na EvoLink](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=docs_link)
- [Saiba mais sobre o Kimi K3 na EvoLink](https://evolink.ai/blog/is-kimi-k3-available-on-evolink?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_article)
- [KimiK3.io](https://kimik3.io/)
- A página do modelo e a documentação da API da EvoLink estão verificadas; nenhuma skill instalável de Kimi K3 foi verificada

<a id="acknowledge"></a>
## 🙏 Agradecimentos

Este repositório existe graças a quem compartilhou publicamente trabalhos com Kimi K3

[@ivanfioravanti](https://x.com/ivanfioravanti), [@TheAhmadOsman](https://x.com/TheAhmadOsman), [@HarshithLucky3](https://x.com/HarshithLucky3), [@chetaslua](https://x.com/chetaslua), [@abhinavflac](https://x.com/abhinavflac), [@bridgemindai](https://x.com/bridgemindai), [@Whats_AI](https://x.com/Whats_AI), [@chongdashu](https://x.com/chongdashu), [@MrAhmadAwais](https://x.com/MrAhmadAwais), [@bijanbowen](https://x.com/bijanbowen), [@CommandCodeAI](https://x.com/CommandCodeAI), [@emollick](https://x.com/emollick), [@nicky_sap](https://x.com/nicky_sap), [@Lentils80](https://x.com/Lentils80), [@scottstts](https://x.com/scottstts), [@aisearchio](https://x.com/aisearchio), [@gmi_cloud](https://x.com/gmi_cloud), [@karminski3](https://x.com/karminski3), [@VORTEX_Promos](https://x.com/VORTEX_Promos), [@rohanpaul_ai](https://x.com/rohanpaul_ai), [@mirochill](https://x.com/mirochill), [@aimlapi](https://x.com/aimlapi), [@minchoi](https://x.com/minchoi), [@doutorcaleb](https://x.com/doutorcaleb), [@adxtyahq](https://x.com/adxtyahq), [@higgsfield_ai](https://x.com/higgsfield_ai), [@AlicanKiraz0](https://x.com/AlicanKiraz0), [@1littlecoder](https://x.com/1littlecoder), [@op7418](https://x.com/op7418), [@adamuchigabriel](https://x.com/adamuchigabriel), [@s_batzoglou](https://x.com/s_batzoglou), [@servasyy_ai](https://x.com/servasyy_ai), [@filicroval](https://x.com/filicroval), [@doodlestein](https://x.com/doodlestein), [@dejavucoder](https://x.com/dejavucoder), [@Angaisb_](https://x.com/Angaisb_), [@AngryTomtweets](https://x.com/AngryTomtweets), [@Alezander907](https://x.com/Alezander907), [@teortaxesTex](https://x.com/teortaxesTex), [@jun_song](https://x.com/jun_song), [@ridark_eth](https://x.com/ridark_eth), [@naymur_dev](https://x.com/naymur_dev), [@tphuang](https://x.com/tphuang), [@TokenGremlin](https://x.com/TokenGremlin), [@IntuitMachine](https://x.com/IntuitMachine), [@wangfeng0315](https://x.com/wangfeng0315), [@twid](https://x.com/twid), [@pengchujin](https://x.com/pengchujin), [@aayushman2703](https://x.com/aayushman2703), [@goncalo_canhoto](https://x.com/goncalo_canhoto), [@LinearUncle](https://x.com/LinearUncle), [@gagarot200](https://x.com/gagarot200), [@MinLiBuilds](https://x.com/MinLiBuilds), [@izutorishima](https://x.com/izutorishima), [@X2worldtech](https://x.com/X2worldtech), [@Satvik_Pen](https://x.com/Satvik_Pen), [@hakki_alkan](https://x.com/hakki_alkan), [@BrianMRey](https://x.com/BrianMRey), [@ChrisGPT](https://x.com/ChrisGPT), [@arena](https://x.com/arena), [@MathiasHeide](https://x.com/MathiasHeide), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@nauczymycieAI](https://x.com/nauczymycieAI), [@AlphaSignalAI](https://x.com/AlphaSignalAI), [@Ananth7e](https://x.com/Ananth7e), [@viktoroddy](https://x.com/viktoroddy), [@abacusai](https://x.com/abacusai), [@deredleritt3r](https://x.com/deredleritt3r), [@fabriciocarraro](https://x.com/fabriciocarraro), [@startracker](https://x.com/startracker), [@mattwatkajtys](https://x.com/mattwatkajtys), [@AIsaOneHQ](https://x.com/AIsaOneHQ), [@MiaAI_lab](https://x.com/MiaAI_lab), [@hqmank](https://x.com/hqmank), [@prasenx](https://x.com/prasenx), [@stas_sorokin_](https://x.com/stas_sorokin_), [@RoundtableSpace](https://x.com/RoundtableSpace), [@karankendre](https://x.com/karankendre), [@0xzynex](https://x.com/0xzynex), [@ashen_one](https://x.com/ashen_one), [@MAXdeg0](https://x.com/MAXdeg0), [@ice_bearcute](https://x.com/ice_bearcute), [@mnmn94253156337](https://x.com/mnmn94253156337), [@morganlinton](https://x.com/morganlinton), [@vikktorrrre](https://x.com/vikktorrrre), [@kirillk_web3](https://x.com/kirillk_web3), [@_guillecasaus](https://x.com/_guillecasaus), [@demian_ai](https://x.com/demian_ai), [@aidenybai](https://x.com/aidenybai), [@LexnLin](https://x.com/LexnLin), [@boxmining](https://x.com/boxmining), [@Nekt_0](https://x.com/Nekt_0), [@RetroChainer](https://x.com/RetroChainer), [@tamsi_besson](https://x.com/tamsi_besson), [@thehypedotnews](https://x.com/thehypedotnews), [@AiHubMix](https://x.com/AiHubMix), [@sairahul1](https://x.com/sairahul1)

*Para corrigir atribuição ou texto, abra uma issue com uma fonte pública*
