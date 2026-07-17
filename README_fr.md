<div align="center">

<a href="https://evolink.ai/kimi-k3?utm_source=github&utm_medium=banner&utm_campaign=awesome-kimi-k3-usecases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/images/fr-v2.png" alt="Bannière Kimi K3 localisée avec paysage lunaire et appel à l’action EvoLink" width="760"></a>

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

# Cas d’usage remarquables de Kimi K3

## 🍌 Introduction

Bienvenue dans la sélection de cas d’usage Kimi K3 à forte valeur informative

**Nous rassemblons des jeux, scènes 3D, créations animées, intégrations, évaluations et limites pratiques étayés par des sources publiques**

Les 70 cas à forte confiance proviennent de l’artefact source fourni; les 31 cas à confiance moyenne sont exclus. Les titres et auteurs renvoient aux sources originales

[EvoLink](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=introduction_cta)

## 📊 Vue d’ensemble

- 70 cas à forte confiance sélectionnés auprès de créateurs et de praticiens
- Jeux, 3D, frontend, motion design, développement, intégrations, benchmarks et limites pratiques
- Chaque cas conserve la source, l’auteur, le type, la date et les limites factuelles
- Les cas à confiance moyenne sont exclus et les observations individuelles ne deviennent pas des conclusions générales

> [!NOTE]
> La collection privilégie les preuves concrètes et ne reconstitue ni prompts ni étapes absentes

## ⚡ Démarrage rapide

L’ID documenté par EvoLink est `kimi-k3`; la page du modèle et la documentation Chat Completions sont disponibles

1. [Voir les détails et tarifs de Kimi K3 sur EvoLink](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-kimi-k3-usecases&utm_content=model_link)
2. [Créer ou gérer une clé API EvoLink](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-kimi-k3-usecases&utm_content=api_key)
3. [Ouvrir la documentation API Kimi K3 d’EvoLink](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=first_run)

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
> La page du modèle et la documentation EvoLink vérifient la route publique et l’ID. Ce dépôt ne revendique pas de test API payant indépendant

## 📑 Menu

| Section | Cases |
|---|---|
| [Jeux interactifs et 3D](#games-3d) | 22 |
| [Frontend et motion design](#frontend-motion) | 15 |
| [Code et intégrations](#coding-integrations) | 8 |
| [Évaluation et limites](#evaluation-limits) | 25 |
| [Remerciements](#acknowledge) | Crédits et corrections |

<a id="games-3d"></a>
## 🎮 Jeux interactifs et 3D

| Case | What it shows | Type |
|---|---|---|
| [Créer un pod racer voxel avec un prompt](#case-1) | Partir d’une idée courte pour prototyper une course voxel puis cadrer l’itération suivante | Demo |
| [Comparer Frogger avec le même prompt](#case-2) | Garder le prompt constant pour examiner les différences entre modèles | Evaluation |
| [Générer Frogger et son enregistrement](#case-3) | Tester en un passage le jeu et le flux d’enregistrement | Demo |
| [Prototyper un porte-avions en Three.js](#case-4) | Tester la 3D interactive avec une scène précise de lancement et récupération | Demo |
| [Créez un jeu inspiré de Paper Mario avec des outils d'agent](#case-9) | Combinez Kimi K3 avec un harnais d'agent et des outils d'actifs pour produire des éléments de jeu 2D et 3D. | Demo |
| [Générer un jeu de tir à la première personne dans le métro](#case-11) | Utilisez un paramètre de métro concret pour inspecter un résultat de jeu de tir à la première personne généré. | Demo |
| [Modéliser un moteur V8 avec Blender MCP](#case-19) | Utilisez Blender MCP et une seule requête pour générer un modèle 3D mécanique détaillé. | Integration |
| [Créer une arène de combat jouable à partir d’une référence](#case-23) | Utilisez une seule référence pour tester la génération one-shot d'une arène jouable complète. | Demo |
| [Construire trois jeux rétro autonomes sous forme de fichiers HTML](#case-24) | Exiger des graphiques, des ennemis, des règles et un jeu autonome dans des fichiers de jeu HTML autonomes. | Benchmark |
| [Créer en une passe un jeu de cache-cache avec un caméléon](#case-27) | Générez un jeu à fichier unique avec correspondance des couleurs, zones procédurales, son et score à plusieurs tours. | Benchmark |
| [Créer un jeu 2,5D à la Paper Mario avec une chaîne d’outils agentiques](#case-36) | Utilisez Kimi K3 avec Grok Build ou Claude Code et Spriterrific pour assembler un flux de travail de jeu 2.5D. | Tutorial |
| [Créer un RPG wuxia 3D dans le navigateur](#case-43) | Combinez le combat au corps à corps, les quêtes, l'inventaire, la météo, les intérieurs, le travail sur l'environnement Blender et les ressources adaptées. | Demo |
| [Créer un jeu multijoueur par navigateur de type Minecraft](#case-44) | Utiliser un temps et un coût limités pour produire un jeu par navigateur multijoueur en ligne jouable. | Demo |
| [Recréez un jeu sur navigateur coopératif en écran partagé](#case-48) | Utilisez une requête pour générer une coopération en écran partagé basée sur un navigateur et une interaction avec l'environnement en temps réel. | Demo |
| [Générer un jeu jouable avec le mode Design de Command Code](#case-49) | Utilisez la commande de conception du code de commande pour créer un jeu unique et enregistrez si le résultat est jouable. | Demo |
| [Assembler un RPG de navigateur Wuxia cohérent](#case-51) | Intégrer la traversée, le combat, les quêtes, l'inventaire, la météo, l'exploration et l'environnement 3D dans un seul jeu. | Demo |
| [Construire un crossover jouable de Hollow Knight](#case-54) | Utiliser les ressources de jeu existantes pour créer une bataille jouable entre le Chevalier et Kimi. | Demo |
| [Créer en une passe un jeu 3D pour navigateur à la Fall Guys](#case-60) | Utilisez une requête unique pour générer un jeu d'obstacles 3D jouable et exposez le projet pour inspection. | Demo |
| [Construire et auto-tester un FPS apocalyptique de Lisbonne](#case-61) | Utiliser une exécution à effort maximal fondée sur une seule invite, qui teste, prend des captures d’écran et itère avant de livrer un FPS jouable. | Demo |
| [Générer un jeu de style Animal Crossing à partir d'une simple requête](#case-63) | Utilisez un résumé de jeu minimal pour inspecter la jouabilité, la boucle de jeu et les effets de parallaxe. | Demo |
| [Générer un jeu de type Mario à partir d'un brief d'une phrase](#case-65) | Utiliser une requête unique minimale pour inspecter la jouabilité, la conception de la scène, le pixel art et la parallaxe. | Demo |
| [Construisez un jeu de tir à la première personne zombie fonctionnel](#case-67) | Utilisez une cible de tir zombie en béton pour inspecter un artefact FPS jouable complet. | Demo |

<a id="case-1"></a>
### Case 1: [Créer un pod racer voxel avec un prompt](https://x.com/ivanfioravanti/status/2077763009657627055) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Partir d’une idée courte pour prototyper une course voxel puis cadrer l’itération suivante**

L’auteur indique que Kimi K3 a produit la première version avec un prompt public et prévoit plus de concurrents, une arrivée et une revue des détails

**Prompt:**

```text
Voxel star wars pod-racers run
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01-poster.jpg" alt="Case 1 video poster" height="360"></a>

[Play case 1 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-2"></a>
### Case 2: [Comparer Frogger avec le même prompt](https://x.com/ivanfioravanti/status/2077754781964054825) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Garder le prompt constant pour examiner les différences entre modèles**

L’auteur partage une version Kimi K3 comme comparaison. La source ne publie ni le prompt ni la grille d’évaluation

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02-poster.jpg" alt="Case 2 video poster" height="360"></a>

[Play case 2 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-3"></a>
### Case 3: [Générer Frogger et son enregistrement](https://x.com/TheAhmadOsman/status/2077776567292338285) (by [@TheAhmadOsman](https://x.com/TheAhmadOsman))

**Tester en un passage le jeu et le flux d’enregistrement**

L’auteur rapporte un passage pour le jeu et un autre pour l’enregistrement. Les prompts exacts ne sont pas publiés

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03-poster.jpg" alt="Case 3 video poster" height="360"></a>

[Play case 3 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-4"></a>
### Case 4: [Prototyper un porte-avions en Three.js](https://x.com/HarshithLucky3/status/2077753222018814360) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**Tester la 3D interactive avec une scène précise de lancement et récupération**

L’auteur montre des avions sur un porte-avions de classe Nimitz et juge positivement la génération 3D

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04-poster.jpg" alt="Case 4 video poster" height="360"></a>

[Play case 4 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-9"></a>
### Case 9: [Créez un jeu inspiré de Paper Mario avec des outils d'agent](https://x.com/chongdashu/status/2077886028866531655) (by [@chongdashu](https://x.com/chongdashu))

**Combinez Kimi K3 avec un harnais d'agent et des outils d'actifs pour produire des éléments de jeu 2D et 3D.**

Le créateur rapporte avoir utilisé Kimi K3 avec Grok Build, Spriterrific pour les ressources 2D et la géométrie pour les ressources 3D dans un jeu inspiré de Paper Mario. La source démontre l'utilisation des outils et des compétences, mais ne publie pas d'invite réutilisable exacte.

Type: Demo | Date: 2026-07-16

---

<a id="case-11"></a>
### Case 11: [Générer un jeu de tir à la première personne dans le métro](https://x.com/bijanbowen/status/2077881805751873997) (by [@bijanbowen](https://x.com/bijanbowen))

**Utilisez un paramètre de métro concret pour inspecter un résultat de jeu de tir à la première personne généré.**

Le créateur montre un FPS dans le métro attribué à Kimi K3 et note explicitement l'incertitude quant à savoir si le statut d'influenceur a affecté le résultat. Aucun flux de travail rapide ou reproductible n'est fourni.

Type: Demo | Date: 2026-07-16

---

<a id="case-19"></a>
### Case 19: [Modéliser un moteur V8 avec Blender MCP](https://x.com/aisearchio/status/2077962156147146925) (by [@aisearchio](https://x.com/aisearchio))

**Utilisez Blender MCP et une seule requête pour générer un modèle 3D mécanique détaillé.**

Le critique rapporte que Kimi K3 a généré un moteur V8 complet avec Blender MCP à partir d'une seule invite. Le message relie une critique plus complète mais n'expose pas l'invite exacte dans l'enregistrement fourni.

Type: Integration | Date: 2026-07-17

---

<a id="case-23"></a>
### Case 23: [Créer une arène de combat jouable à partir d’une référence](https://x.com/VORTEX_Promos/status/2077879705378730074) (by [@VORTEX_Promos](https://x.com/VORTEX_Promos))

**Utilisez une seule référence pour tester la génération one-shot d'une arène jouable complète.**

Le créateur rapporte que Kimi K3 a produit une arène de combat jouable en un seul coup à partir d'une seule référence. Une revendication distincte du classement apparaît dans l'article, mais le cas d'utilisation concret est l'artefact d'arène démontré.

Type: Demo | Date: 2026-07-16

---

<a id="case-24"></a>
### Case 24: [Construire trois jeux rétro autonomes sous forme de fichiers HTML](https://x.com/rohanpaul_ai/status/2077889084761206860) (by [@rohanpaul_ai](https://x.com/rohanpaul_ai))

**Exiger des graphiques, des ennemis, des règles et un jeu autonome dans des fichiers de jeu HTML autonomes.**

La source rapporte une comparaison Atomic Chat dans laquelle les modèles ont construit Road Fighter, Battle City et Q*bert sous forme de fichiers HTML autonomes. Sa comparaison de coût et de qualité est rapportée par l'éditeur et n'est pas reproduite indépendamment ici.

Type: Benchmark | Date: 2026-07-16

---

<a id="case-27"></a>
### Case 27: [Créer en une passe un jeu de cache-cache avec un caméléon](https://x.com/aimlapi/status/2077898742179459274) (by [@aimlapi](https://x.com/aimlapi))

**Générez un jeu à fichier unique avec correspondance des couleurs, zones procédurales, son et score à plusieurs tours.**

AIMLAPI rapporte une comparaison unique pour un jeu de cache-cache et répertorie les coûts de 3,11 $ pour Kimi K3 et de 12,23 $ pour Fable 5. Les réclamations en matière de fonctionnalités et de coûts sont résultats rapportés par le fournisseur.

Type: Benchmark | Date: 2026-07-16

---

<a id="case-36"></a>
### Case 36: [Créer un jeu 2,5D à la Paper Mario avec une chaîne d’outils agentiques](https://x.com/chongdashu/status/2077981621223837739) (by [@chongdashu](https://x.com/chongdashu))

**Utilisez Kimi K3 avec Grok Build ou Claude Code et Spriterrific pour assembler un flux de travail de jeu 2.5D.**

Le créateur fournit une procédure complète en utilisant Grok Build et Kimi K3 et montre la génération de sprites avec Spriterrific. La source identifie les outils mais ne fournit pas d'invites réutilisables exactes.

Type: Tutorial | Date: 2026-07-17

---

<a id="case-43"></a>
### Case 43: [Créer un RPG wuxia 3D dans le navigateur](https://x.com/AngryTomtweets/status/2077868163136450619) (by [@AngryTomtweets](https://x.com/AngryTomtweets))

**Combinez le combat au corps à corps, les quêtes, l'inventaire, la météo, les intérieurs, le travail sur l'environnement Blender et les ressources adaptées.**

La source rapporte un RPG sur navigateur Kimi K3 avec combat au corps à corps, quêtes, inventaire, météo dynamique et intérieurs explorables, plus Modélisation de Blender, améliorations des collisions, retexturation PBR et actifs ouverts adaptés.

Type: Demo | Date: 2026-07-16

---

<a id="case-44"></a>
### Case 44: [Créer un jeu multijoueur par navigateur de type Minecraft](https://x.com/Alezander907/status/2077926014710407407) (by [@Alezander907](https://x.com/Alezander907))

**Utiliser un temps et un coût limités pour produire un jeu par navigateur multijoueur en ligne jouable.**

Le créateur rapporte que Kimi K3 a construit un jeu multijoueur de type Minecraft jouable par navigateur en une heure au coût de 6,57 $. Il s'agit de chiffres d'exécution autodéclarés à partir d'un artefact.

Type: Demo | Date: 2026-07-17

---

<a id="case-48"></a>
### Case 48: [Recréez un jeu sur navigateur coopératif en écran partagé](https://x.com/ridark_eth/status/2077882889803378969) (by [@ridark_eth](https://x.com/ridark_eth))

**Utilisez une requête pour générer une coopération en écran partagé basée sur un navigateur et une interaction avec l'environnement en temps réel.**

Le créateur rapporte que Kimi K3 a produit un jeu par navigateur inspiré de It Takes Two en une seule invite, avec Mario et Luigi interagissant en écran partagé et avec l'environnement en temps réel. time.

Type: Demo | Date: 2026-07-16

---

<a id="case-49"></a>
### Case 49: [Générer un jeu jouable avec le mode Design de Command Code](https://x.com/naymur_dev/status/2077873562661335207) (by [@naymur_dev](https://x.com/naymur_dev))

**Utilisez la commande de conception du code de commande pour créer un jeu unique et enregistrez si le résultat est jouable.**

Le créateur rapporte une comparaison unique en utilisant le mode de conception du code de commande et indique que l'exécution de Kimi K3 a produit un jeu jouable pour 0,038 $. Ce résultat de coût et de qualité est auto-déclaré.

Type: Demo | Date: 2026-07-16

---

<a id="case-51"></a>
### Case 51: [Assembler un RPG de navigateur Wuxia cohérent](https://x.com/TokenGremlin/status/2077855657068310620) (by [@TokenGremlin](https://x.com/TokenGremlin))

**Intégrer la traversée, le combat, les quêtes, l'inventaire, la météo, l'exploration et l'environnement 3D dans un seul jeu.**

La source rapporte un RPG de navigateur de style Kimi K3 wuxia qui combine combat au corps à corps, quêtes, inventaire, météo dynamique, intérieurs explorables et un Structure de jeu 3D.

Type: Demo | Date: 2026-07-16

---

<a id="case-54"></a>
### Case 54: [Construire un crossover jouable de Hollow Knight](https://x.com/wangfeng0315/status/2077933531200991583) (by [@wangfeng0315](https://x.com/wangfeng0315))

**Utiliser les ressources de jeu existantes pour créer une bataille jouable entre le Chevalier et Kimi.**

Le créateur, qui déclare travailler chez Kimi, rapporte avoir construit un jeu à partir des ressources de Hollow Knight dans lequel le Chevalier combat Kimi et fournit un lien de jeu public. L'attribution et l'évaluation doivent tenir compte de cette affiliation.

Type: Demo | Date: 2026-07-17

---

<a id="case-60"></a>
### Case 60: [Créer en une passe un jeu 3D pour navigateur à la Fall Guys](https://x.com/aayushman2703/status/2077857886441783526) (by [@aayushman2703](https://x.com/aayushman2703))

**Utilisez une requête unique pour générer un jeu d'obstacles 3D jouable et exposez le projet pour inspection.**

Le créateur rapporte une version unique de Kimi K3 d'un jeu par navigateur de style Fall Guys et indique que l'invite et le projet GitHub sont liés à partir de la source. Cet enregistrement ne reproduit pas cette invite.

Type: Demo | Date: 2026-07-16

---

<a id="case-61"></a>
### Case 61: [Construire et auto-tester un FPS apocalyptique de Lisbonne](https://x.com/goncalo_canhoto/status/2077863166655037668) (by [@goncalo_canhoto](https://x.com/goncalo_canhoto))

**Utiliser une exécution à effort maximal fondée sur une seule invite, qui teste, prend des captures d’écran et itère avant de livrer un FPS jouable.**

Le créateur rapporte que Kimi K3 a produit un FPS de navigateur apocalyptique de Lisbonne jouable après environ une heure, avec des tests, des captures d'écran et des itérations répétés. Ces détails sur le calendrier et le processus sont auto-déclarés.

Type: Demo | Date: 2026-07-16

---

<a id="case-63"></a>
### Case 63: [Générer un jeu de style Animal Crossing à partir d'une simple requête](https://x.com/gagarot200/status/2077949230287896830) (by [@gagarot200](https://x.com/gagarot200))

**Utilisez un résumé de jeu minimal pour inspecter la jouabilité, la boucle de jeu et les effets de parallaxe.**

Le créateur rapporte que Kimi K3 a généré un jeu de style Animal Crossing entièrement jouable avec une boucle de jeu et des effets de parallaxe à partir d'une invite très simple. Le libellé exact n'est pas présent dans l'enregistrement fourni.

Type: Demo | Date: 2026-07-17

---

<a id="case-65"></a>
### Case 65: [Générer un jeu de type Mario à partir d'un brief d'une phrase](https://x.com/izutorishima/status/2077939370154475992) (by [@izutorishima](https://x.com/izutorishima))

**Utiliser une requête unique minimale pour inspecter la jouabilité, la conception de la scène, le pixel art et la parallaxe.**

Le créateur rapporte que Kimi K3 a produit un jeu de type Mario fonctionnel sans bugs évidents, y compris la structure de la scène et la parallaxe, à partir d'un seul brief. Le même rapport critique la qualité de la musique et des graphiques.

Type: Demo | Date: 2026-07-17

---

<a id="case-67"></a>
### Case 67: [Construisez un jeu de tir à la première personne zombie fonctionnel](https://x.com/X2worldtech/status/2077902793449296203) (by [@X2worldtech](https://x.com/X2worldtech))

**Utilisez une cible de tir zombie en béton pour inspecter un artefact FPS jouable complet.**

La source montre un FPS zombie entièrement fonctionnel attribué à Kimi K3. Il ne fournit pas d'invite, de détails de mise en œuvre ou d'évaluation externe du gameplay.

> [!WARNING]
> The original source permalink returned HTTP 404 during the 2026-07-17 audit. Attribution and evidence are preserved from the supplied high-confidence source package.

Type: Demo | Date: 2026-07-16

---


<a id="frontend-motion"></a>
## 🎨 Frontend et motion design

| Case | What it shows | Type |
|---|---|---|
| [Créer un frontend de motion design interactif](#case-5) | Construire des graphismes qui restent interactifs une fois l’animation en pause | Demo |
| [Produire une publicité animée synchronisée](#case-6) | Vérifier la synchronisation de la musique, des effets et du mouvement | Demo |
| [Créer une conception de mouvement entièrement dans le code](#case-14) | Testez si un flux de travail de codage unique peut produire une conception de mouvement sans outils de génération auxiliaires. | Demo |
| [Recherchez une personne et créez un site personnel animé](#case-15) | Donnez un aperçu général du site personnel, puis inspectez la recherche, la planification, l'itération et la validation du navigateur du modèle. | Tutorial |
| [Générer une simulation de trou noir](#case-17) | Utilisez une tâche de visualisation scientifique pour inspecter une simulation de trou noir générée. | Demo |
| [Testez la modélisation frontale complexe, les particules et les shaders](#case-22) | Utilisez une invite frontale publique pour inspecter la précision de la modélisation, les effets de particules et la génération de shaders en ligne en un seul passage. | Demo |
| [Générer un outil de musique procédurale en une seule tentative](#case-26) | Testez la génération unique d'un générateur de musique procédurale interactif et comparez le résultat visible avec prudence. | Demo |
| [Créer une page produit Three.js à partir de deux images](#case-33) | Utiliser deux images de référence et une exigence Three.js explicite pour générer une présentation de produit. | Demo |
| [Inventez un coupe-pain de luxe et sa page produit](#case-39) | Combinez l'idéation du produit, une vue éclatée, une démonstration et une page de destination dans un seul artefact de conception. | Demo |
| [Générer un GIF de pélican récursif de dix secondes](#case-45) | Utilisez un bref d'animation en boucle entièrement spécifié pour inspecter la continuité narrative et la récursion dans un GIF. | Demo |
| [Générer un SVG de profil d’une BMW M4 CS](#case-55) | Utiliser un véhicule et un point de vue spécifiques pour inspecter la sortie de l'illustration vectorielle. | Demo |
| [Recréer Gargantua grâce aux retours de captures d’écran](#case-58) | Utiliser des captures d'écran répétées comme observations pour diagnostiquer et affiner une visualisation scientifique. | Tutorial |
| [Affiner une visualisation de trou noir avec 62 captures d'écran](#case-66) | Utiliser une boucle de retours par captures d’écran pour lire, diagnostiquer et corriger une simulation visuelle sur de nombreuses itérations. | Tutorial |
| [Créer un PDF marketing post-formation](#case-68) | Utiliser un produit nommé et un format de livrable pour générer un document marketing. | Demo |
| [Créer une interface utilisateur à partir d'une seule invite](#case-70) | Utilisez une seule requête pour générer et inspecter une conception d'interface utilisateur complète. | Demo |

<a id="case-5"></a>
### Case 5: [Créer un frontend de motion design interactif](https://x.com/chetaslua/status/2077749371144442022) (by [@chetaslua](https://x.com/chetaslua))

**Construire des graphismes qui restent interactifs une fois l’animation en pause**

L’auteur rapporte 42 minutes, un passage, du code simple, sans harness, MCP ni skills

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05-poster.jpg" alt="Case 5 video poster" height="360"></a>

[Play case 5 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-6"></a>
### Case 6: [Produire une publicité animée synchronisée](https://x.com/abhinavflac/status/2077760297918484667) (by [@abhinavflac](https://x.com/abhinavflac))

**Vérifier la synchronisation de la musique, des effets et du mouvement**

L’auteur rapporte une publicité de style Spotify produite en un prompt. Le prompt exact n’est pas publié

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06-poster.jpg" alt="Case 6 video poster" height="360"></a>

[Play case 6 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-14"></a>
### Case 14: [Créer une conception de mouvement entièrement dans le code](https://x.com/chetaslua/status/2077952938564354503) (by [@chetaslua](https://x.com/chetaslua))

**Testez si un flux de travail de codage unique peut produire une conception de mouvement sans outils de génération auxiliaires.**

Le créateur rapporte un résultat de conception de mouvement unique Kimi K3 entièrement réalisé en code sans MCP, compétences, outils, génération de vidéo ou invites spéciales. L'invite exacte n'est pas fournie.

Type: Demo | Date: 2026-07-17

---

<a id="case-15"></a>
### Case 15: [Recherchez une personne et créez un site personnel animé](https://x.com/nicky_sap/status/2077857190707429411) (by [@nicky_sap](https://x.com/nicky_sap))

**Donnez un aperçu général du site personnel, puis inspectez la recherche, la planification, l'itération et la validation du navigateur du modèle.**

Le créateur rapporte que Kimi K3 a fait des recherches sur Nick Saponaro et a produit un site Web personnel animé à partir d'une large demande, y compris la planification, les tests, l'itération et les vérifications du navigateur. Le résultat est une démonstration de flux de travail auto-déclarée.

Type: Tutorial | Date: 2026-07-16

---

<a id="case-17"></a>
### Case 17: [Générer une simulation de trou noir](https://x.com/chetaslua/status/2077961850352971796) (by [@chetaslua](https://x.com/chetaslua))

**Utilisez une tâche de visualisation scientifique pour inspecter une simulation de trou noir générée.**

Le créateur montre une simulation de trou noir attribuée à Kimi K3 et l'appelle la meilleure qu'il ait vue. La source fournit un résultat visible mais aucune invite, rubrique ou validation indépendante.

Type: Demo | Date: 2026-07-17

---

<a id="case-22"></a>
### Case 22: [Testez la modélisation frontale complexe, les particules et les shaders](https://x.com/karminski3/status/2077889959223337099) (by [@karminski3](https://x.com/karminski3))

**Utilisez une invite frontale publique pour inspecter la précision de la modélisation, les effets de particules et la génération de shaders en ligne en un seul passage.**

Le créateur rapporte un résultat frontal Kimi K3 en un seul passage couvrant la modélisation précise, les effets de particules et le code de shader en ligne complexe, et déclare que l'invite de test est publique sur la source liée.

Type: Demo | Date: 2026-07-16

---

<a id="case-26"></a>
### Case 26: [Générer un outil de musique procédurale en une seule tentative](https://x.com/mirochill/status/2077723551331758478) (by [@mirochill](https://x.com/mirochill))

**Testez la génération unique d'un générateur de musique procédurale interactif et comparez le résultat visible avec prudence.**

Le créateur rapporte que Kimi K3 a généré un outil de musique procédurale en une seule tentative et le compare favorablement aux résultats de Fable 5 et GPT-5.6 Sol. Il s'agit de l'ensemble de tests du créateur, et non d'une référence standardisée.

Type: Demo | Date: 2026-07-16

---

<a id="case-33"></a>
### Case 33: [Créer une page produit Three.js à partir de deux images](https://x.com/1littlecoder/status/2077890296806031665) (by [@1littlecoder](https://x.com/1littlecoder))

**Utiliser deux images de référence et une exigence Three.js explicite pour générer une présentation de produit.**

Le créateur rapporte que Kimi K3 a conçu une page produit à partir de deux images et a produit la version Three.js explicitement demandée. Aucune autre invite ni aucun détail de mise en œuvre n'est fourni.

Type: Demo | Date: 2026-07-16

---

<a id="case-39"></a>
### Case 39: [Inventez un coupe-pain de luxe et sa page produit](https://x.com/filicroval/status/2077871090731221438) (by [@filicroval](https://x.com/filicroval))

**Combinez l'idéation du produit, une vue éclatée, une démonstration et une page de destination dans un seul artefact de conception.**

Le créateur rapporte que Kimi K3 a inventé un coupe-pain de style guillotine, l'a présenté comme un produit de luxe et a produit une page de destination avec une vue éclatée et démonstration.

Type: Demo | Date: 2026-07-16

---

<a id="case-45"></a>
### Case 45: [Générer un GIF de pélican récursif de dix secondes](https://x.com/1littlecoder/status/2077880380900937865) (by [@1littlecoder](https://x.com/1littlecoder))

**Utilisez un bref d'animation en boucle entièrement spécifié pour inspecter la continuité narrative et la récursion dans un GIF.**

La source inclut une invite pour un GIF en boucle de dix secondes d'un pélican faisant du vélo et recevant la même vidéo par texte lorsque la caméra zoome. Le créateur montre celui de Kimi K3. animation résultante.

Type: Demo | Date: 2026-07-16

---

<a id="case-55"></a>
### Case 55: [Générer un SVG de profil d’une BMW M4 CS](https://x.com/HarshithLucky3/status/2077765821380886942) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**Utiliser un véhicule et un point de vue spécifiques pour inspecter la sortie de l'illustration vectorielle.**

Le créateur montre une vue latérale BMW M4 CS SVG attribuée à Kimi K3 Max. La source fournie contient l'artefact mais aucune invite ni étape de production.

Type: Demo | Date: 2026-07-16

---

<a id="case-58"></a>
### Case 58: [Recréer Gargantua grâce aux retours de captures d’écran](https://x.com/AngryTomtweets/status/2077868981659324444) (by [@AngryTomtweets](https://x.com/AngryTomtweets))

**Utiliser des captures d'écran répétées comme observations pour diagnostiquer et affiner une visualisation scientifique.**

La source rapporte que Kimi K3 a recréé Gargantua d’Interstellar au fil de 62 auto-captures d’écran, en lisant chaque résultat, en diagnostiquant les problèmes puis en agissant de manière itérative.

Type: Tutorial | Date: 2026-07-16

---

<a id="case-66"></a>
### Case 66: [Affiner une visualisation de trou noir avec 62 captures d'écran](https://x.com/TokenGremlin/status/2077855959201042645) (by [@TokenGremlin](https://x.com/TokenGremlin))

**Utiliser une boucle de retours par captures d’écran pour lire, diagnostiquer et corriger une simulation visuelle sur de nombreuses itérations.**

La source rapporte que Kimi K3 a reconstruit le Gargantua d'Interstellar en observant et en affinant sa sortie sur 62 captures d'écran. Cela démontre la boucle de rétroaction signalée plutôt qu'une précision physique indépendante.

Type: Tutorial | Date: 2026-07-16

---

<a id="case-68"></a>
### Case 68: [Créer un PDF marketing post-formation](https://x.com/Satvik_Pen/status/2077859673517023313) (by [@Satvik_Pen](https://x.com/Satvik_Pen))

**Utiliser un produit nommé et un format de livrable pour générer un document marketing.**

Le créateur rapporte avoir demandé à Kimi K3 un PDF marketing sur la post-formation Inkling de Thinking Machines et partage le résultat, tout en louant également le processus en coulisses. Aucune invite ou critère d'évaluation n'est fourni.

Type: Demo | Date: 2026-07-16

---

<a id="case-70"></a>
### Case 70: [Créer une interface utilisateur à partir d'une seule invite](https://x.com/BrianMRey/status/2077891942088671689) (by [@BrianMRey](https://x.com/BrianMRey))

**Utilisez une seule requête pour générer et inspecter une conception d'interface utilisateur complète.**

Le créateur montre une conception d'interface utilisateur attribuée à une exécution en une seule invite de Kimi K3 et donne une évaluation subjective fortement positive. L'invite et la rubrique exactes ne sont pas incluses.

Type: Demo | Date: 2026-07-16

---


<a id="coding-integrations"></a>
## 💻 Code et intégrations

| Case | What it shows | Type |
|---|---|---|
| [Créez un MacBook virtuel avec macOS fonctionnel](#case-18) | Combinez le rendu matériel Three.js avec une simulation interactive du système d'exploitation de navigateur. | Demo |
| [Construire un compilateur GPU de DSL à PTX](#case-25) | Utiliser une tâche de compilateur de bout en bout couvrant un DSL, les passes du compilateur, la génération PTX et un chemin Tensor Core. | Demo |
| [Créer un traceur de rayons de trou noir en temps réel dans WebGL2](#case-32) | Tester la génération en une seule fois d'un traceur de rayons géodésique WebGL2 natif dans un fichier HTML. | Benchmark |
| [Construire un émulateur Game Boy Advance autour de mGBA WASM](#case-46) | Intégrer un modèle 3D sous licence et un véritable noyau d'émulateur, puis améliorer de manière récursive l'interface et le gameplay. | Integration |
| [Rechercher plusieurs sujets à partir de sources en langue chinoise](#case-50) | Utiliser des tâches de recherche de longue durée pour comparer l'exhaustivité et la latence entre les générations de modèles. | Evaluation |
| [Cloner macOS dans le navigateur avec des applications fonctionnelles](#case-56) | Créer une simulation de système d'exploitation de navigateur qui inclut de la musique, un navigateur et des applications de messagerie. | Demo |
| [Créer une simulation macOS avec FaceTime fonctionnel](#case-62) | Utiliser une tâche de système d'exploitation virtuel pour tester si une interaction d'application générée fonctionne. | Demo |
| [Ajouter un comparateur d’effets frontend entre deux tâches](#case-64) | Créez un outil qui sélectionne deux tâches terminées, les affiche côte à côte et synchronise les vues et les interactions. | Tutorial |

<a id="case-18"></a>
### Case 18: [Créez un MacBook virtuel avec macOS fonctionnel](https://x.com/scottstts/status/2077890054299541890) (by [@scottstts](https://x.com/scottstts))

**Combinez le rendu matériel Three.js avec une simulation interactive du système d'exploitation de navigateur.**

La source rapporte que Kimi K3 a créé un MacBook virtuel dans Three.js avec un environnement fonctionnel de style macOS. Il démontre l'artefact mais ne fournit pas les étapes de mise en œuvre.

Type: Demo | Date: 2026-07-16

---

<a id="case-25"></a>
### Case 25: [Construire un compilateur GPU de DSL à PTX](https://x.com/rohanpaul_ai/status/2077886618657231220) (by [@rohanpaul_ai](https://x.com/rohanpaul_ai))

**Utiliser une tâche de compilateur de bout en bout couvrant un DSL, les passes du compilateur, la génération PTX et un chemin Tensor Core.**

La source rapporte que Kimi K3 a construit un compilateur GPU à partir de zéro, à partir de son DSL et passe par la génération PTX, et compare son Chemin Tensor Core avec Triton. Aucun détail de référence indépendant n'est inclus dans l'enregistrement fourni.

Type: Demo | Date: 2026-07-16

---

<a id="case-32"></a>
### Case 32: [Créer un traceur de rayons de trou noir en temps réel dans WebGL2](https://x.com/AlicanKiraz0/status/2077885419744612597) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**Tester la génération en une seule fois d'un traceur de rayons géodésique WebGL2 natif dans un fichier HTML.**

L'auteur décrit un test de codage nécessitant un traceur de rayons de courbure de lumière de trou noir à fichier unique fonctionnel dans WebGL2 natif. L'enregistrement fourni établit la tâche et les modèles participants, mais pas un audit de résultat entièrement indépendant.

Type: Benchmark | Date: 2026-07-16

---

<a id="case-46"></a>
### Case 46: [Construire un émulateur Game Boy Advance autour de mGBA WASM](https://x.com/teortaxesTex/status/2077925090168062272) (by [@teortaxesTex](https://x.com/teortaxesTex))

**Intégrer un modèle 3D sous licence et un véritable noyau d'émulateur, puis améliorer de manière récursive l'interface et le gameplay.**

Le projet Kimi K3 cité adapte un modèle sous licence AGB-001, intègre un noyau mGBA WASM et améliore l'interface et le gameplay grâce à une auto-amélioration récursive. Le message cite une description du projet plutôt qu'une reproduction indépendante.

Type: Integration | Date: 2026-07-17

---

<a id="case-50"></a>
### Case 50: [Rechercher plusieurs sujets à partir de sources en langue chinoise](https://x.com/tphuang/status/2077911994607239400) (by [@tphuang](https://x.com/tphuang))

**Utiliser des tâches de recherche de longue durée pour comparer l'exhaustivité et la latence entre les générations de modèles.**

L'auteur rapporte avoir testé Kimi K3 sur de nombreux sujets de recherche en utilisant des sources en langue chinoise, le trouvant plus approfondi que K2.6 mais plus lent. Le message note également une forte demande de service à l'époque.

Type: Evaluation | Date: 2026-07-17

---

<a id="case-56"></a>
### Case 56: [Cloner macOS dans le navigateur avec des applications fonctionnelles](https://x.com/twid/status/2077924755357974989) (by [@twid](https://x.com/twid))

**Créer une simulation de système d'exploitation de navigateur qui inclut de la musique, un navigateur et des applications de messagerie.**

La source rapporte que Kimi K3 a été utilisé pour créer un clone macOS basé sur un navigateur avec de la musique, un navigateur, une messagerie électronique et d'autres fonctions. Il ne fournit pas de détails de mise en œuvre.

Type: Demo | Date: 2026-07-17

---

<a id="case-62"></a>
### Case 62: [Créer une simulation macOS avec FaceTime fonctionnel](https://x.com/LinearUncle/status/2077919552239997078) (by [@LinearUncle](https://x.com/LinearUncle))

**Utiliser une tâche de système d'exploitation virtuel pour tester si une interaction d'application générée fonctionne.**

Le créateur montre un environnement de style macOS attribué à Kimi K3 et signale que sa fonctionnalité FaceTime fonctionne. La source ne fournit aucune étape de configuration ou de validation.

Type: Demo | Date: 2026-07-17

---

<a id="case-64"></a>
### Case 64: [Ajouter un comparateur d’effets frontend entre deux tâches](https://x.com/MinLiBuilds/status/2077939461510615376) (by [@MinLiBuilds](https://x.com/MinLiBuilds))

**Créez un outil qui sélectionne deux tâches terminées, les affiche côte à côte et synchronise les vues et les interactions.**

Le créateur rapporte avoir demandé à Kimi K3 d'ajouter un flux de travail de comparaison frontale avec sélection de tâches, deux volets de navigateur, modes objet et itinérance, points de vue synchronisés et tests d'interaction. L'article note également des limitations plus larges du modèle.

Type: Tutorial | Date: 2026-07-17

---


<a id="evaluation-limits"></a>
## 🧪 Évaluation et limites

| Case | What it shows | Type |
|---|---|---|
| [Comparer le design frontend sur la tâche de lampe à lave BridgeBench](#case-7) | Utilisez la tâche de lampe à lave BridgeBench comme une comparaison limitée de conception frontale plutôt qu'un classement universel. | Benchmark |
| [Évaluer l’écriture de scripts dans une voix éditoriale](#case-8) | Mesurez l'adéquation de la voix éditoriale, le classement relatif et le coût par script au sein d'un benchmark interne clairement identifié. | Benchmark |
| [Comparez la conception, le coût et la difficulté du jeu Flappy](#case-10) | Enregistrez les paramètres de difficulté, le coût, la conception et les fonctionnalités de jeu lors de la comparaison des jeux générés. | Benchmark |
| [Comparez la conception du jeu avec la même invite de conception](#case-12) | Maintenez l'invite de conception constante et inspectez séparément le rythme, le sens de la conception et la sensation du gameplay. | Benchmark |
| [Exiger un examen indépendant pour l'audit statistique](#case-13) | Associer les audits statistiques générés par un modèle avec un expert indépendant ou un examen du modèle avant de s'appuyer sur les résultats. | Limit |
| [Évaluer une exécution frontale lente mais forte](#case-16) | Enregistrer le temps d'achèvement ainsi que la qualité de sortie lors du test d'une tâche frontale. | Evaluation |
| [Tester les défauts de préfiguration dans l’écriture d’un roman policier](#case-20) | Évaluer si un mystère généré équilibre les indices, l'obscurité et la préfiguration. | Limit |
| [Comparez la modélisation et l'animation du Millennium Falcon](#case-21) | Utilisez des demandes de style et des paramètres d'effort correspondants pour comparer la modélisation 3D, l'animation, le temps et le coût. | Benchmark |
| [Examiner une collection de dix projets Kimi K3](#case-28) | Utiliser un récapitulatif de projets liés pour découvrir des artefacts concrets pour une vérification séparée. | Evaluation |
| [Comparez une page de destination avancée sur quatre modèles](#case-29) | Maintenez une demande de page de destination constante et inspectez la profondeur et l'achèvement de l'animation dans les sorties du modèle. | Evaluation |
| [Évaluer les mécaniques et le coût de jeux rétro](#case-30) | Comparez le gameplay, la physique, la mécanique, le comportement autonome, l'utilisation des jetons et le coût sur les mêmes tâches de rétro-jeu. | Benchmark |
| [Comparez la génération de jeux avec Fable 5](#case-31) | Utilisez un exemple de jeu généré côte à côte comme une évaluation étroite plutôt qu'un verdict de modèle large. | Evaluation |
| [Comparer des tâches complexes de frontend et de développement avec Opus 4.8](#case-34) | Utilisez plusieurs tâches de codage complexes pour identifier les victoires et les pertes au lieu de déclarer un modèle universellement supérieur. | Evaluation |
| [Examiner des benchmarks et un test de landing page](#case-35) | Combinez le contexte de référence avec un test concret de génération de page de destination tout en gardant les deux types de preuves séparés. | Evaluation |
| [Évaluer le raisonnement inductif avec des tâches graphe-vers-formule](#case-37) | Mesurer l'exactitude, le comportement de rétention et la complexité des formules sur les tâches d'induction de premier ordre. | Benchmark |
| [Examiner les jeux, landing pages, travaux 3D et contextes étendus rapportés](#case-38) | Utilisez un résumé multi-sources pour comparer les artefacts concrets et notez les limitations de vitesse ainsi que les réclamations de coûts. | Evaluation |
| [Auditer un plan complexe et contester ses remèdes](#case-40) | Utiliser un deuxième modèle pour identifier les résultats sous-estimés, les remèdes incorrects et les conclusions qui devraient être rejetées. | Evaluation |
| [Comparez les diagrammes ASCII d'apprentissage par renforcement de style PPO](#case-41) | Maintenez une invite de diagramme ASCII constante et comparez la façon dont les modèles représentent la boucle d'apprentissage par renforcement. | Evaluation |
| [Modéliser dans Blender tout en suivant les erreurs de capacité](#case-42) | Évaluez la progression partielle de Blender ainsi que la fiabilité du service plutôt que de juger uniquement l'artefact. | Limit |
| [Comparer la génération Flappy Bird dans une arène](#case-47) | Utilisez une tâche d'arène pour comparer deux résultats Flappy Bird générés tout en gardant la tâche de jugement spécifique. | Evaluation |
| [Résoudre un problème d'induction visuelle Bongard avec un outil](#case-52) | Tester si l'utilisation d'un outil aide à dériver la règle visuelle dans une tâche de raisonnement Bongard. | Evaluation |
| [Comparer la qualité visuelle du frontend et le design 3D avec GPT-5.6 Sol](#case-53) | Inspectez les fonctionnalités, le goût visuel, l'élégance et l'exécution 3D dans une comparaison frontale limitée. | Evaluation |
| [Comparez la génération de sites Web sur trois modèles](#case-57) | Utilisez les sorties de sites Web visibles pour comparer Kimi K3, Fable 5 et GPT-5.6 Sol sur un seul test. | Evaluation |
| [Comparez la génération et le coût des jeux 3D procéduraux](#case-59) | Maintenez une invite constante entre les modèles et inspectez les systèmes de roulette, de machine à sous et de flipper générés avec le coût par exécution. | Benchmark |
| [Comparez les détails et l'éclairage de la scène d'arsenal 3D](#case-69) | Inspectez la densité des objets, l'éclairage et les détails de la scène dans une comparaison limitée entre Kimi K3 et Opus 4.8. | Evaluation |

<a id="case-7"></a>
### Case 7: [Comparer le design frontend sur la tâche de lampe à lave BridgeBench](https://x.com/bridgemindai/status/2077868061953007908) (by [@bridgemindai](https://x.com/bridgemindai))

**Utilisez la tâche de lampe à lave BridgeBench comme une comparaison limitée de conception frontale plutôt qu'un classement universel.**

BridgeMind AI rapporte que Kimi K3 a surpassé Fable 5 sur sa tâche de lampe à lave BridgeBench et s'est classé premier dans l'arène citée. Voici les résultats de comparaison rapportés par l'éditeur.

Type: Benchmark | Date: 2026-07-16

---

<a id="case-8"></a>
### Case 8: [Évaluer l’écriture de scripts dans une voix éditoriale](https://x.com/Whats_AI/status/2077860441380798908) (by [@Whats_AI](https://x.com/Whats_AI))

**Mesurez l'adéquation de la voix éditoriale, le classement relatif et le coût par script au sein d'un benchmark interne clairement identifié.**

Whats_AI rapporte des résultats internes préliminaires de 2 840 Elo, la première place de son propre classement et un coût d’environ 0,25 $ par script. Il s’agit du benchmark préliminaire d’une organisation, et non d’une garantie générale de performance ou de prix.

Type: Benchmark | Date: 2026-07-16

---

<a id="case-10"></a>
### Case 10: [Comparez la conception, le coût et la difficulté du jeu Flappy](https://x.com/MrAhmadAwais/status/2077915347974557862) (by [@MrAhmadAwais](https://x.com/MrAhmadAwais))

**Enregistrez les paramètres de difficulté, le coût, la conception et les fonctionnalités de jeu lors de la comparaison des jeux générés.**

Le benchmark Flappy interne de Command Code rapporte différents paramètres de difficulté entre les modèles et répertorie Kimi K3 à 0,024 $, Fable 5 à 0,42 $ et GPT-5.6 Sol à 0,15 $. Les paramètres inégaux en font une comparaison interne limitée.

Type: Benchmark | Date: 2026-07-17

---

<a id="case-12"></a>
### Case 12: [Comparez la conception du jeu avec la même invite de conception](https://x.com/CommandCodeAI/status/2077921526213746948) (by [@CommandCodeAI](https://x.com/CommandCodeAI))

**Maintenez l'invite de conception constante et inspectez séparément le rythme, le sens de la conception et la sensation du gameplay.**

Le code de commande rapporte une comparaison de la même invite de Kimi K3, GPT-5.6 Sol et Fable 5. Son message indique que Kimi K3 a bien performé en termes de sens du design tandis que les deux autres ont joué trop vite ; cela reste l'évaluation de l'éditeur.

Type: Benchmark | Date: 2026-07-17

---

<a id="case-13"></a>
### Case 13: [Exiger un examen indépendant pour l'audit statistique](https://x.com/emollick/status/2077869293031624793) (by [@emollick](https://x.com/emollick))

**Associer les audits statistiques générés par un modèle avec un expert indépendant ou un examen du modèle avant de s'appuyer sur les résultats.**

Ethan Mollick rapporte que Kimi K3 Max a mal appliqué les statistiques lors de l'audit de travaux universitaires antérieurs et est d'accord avec une critique distincte. Cet exemple négatif prend en charge une vérification indépendante plutôt qu'une acceptation non vérifiée.

Type: Limit | Date: 2026-07-16

---

<a id="case-16"></a>
### Case 16: [Évaluer une exécution frontale lente mais forte](https://x.com/Lentils80/status/2077387333154857151) (by [@Lentils80](https://x.com/Lentils80))

**Enregistrer le temps d'achèvement ainsi que la qualité de sortie lors du test d'une tâche frontale.**

Le créateur rapporte qu'une exécution frontale Kimi K3 a pris 35 minutes et décrit la sortie comme l'une des meilleures vues pour cette invite. Les jugements de vitesse et de qualité sont l'observation d'un seul utilisateur.

Type: Evaluation | Date: 2026-07-15

---

<a id="case-20"></a>
### Case 20: [Tester les défauts de préfiguration dans l’écriture d’un roman policier](https://x.com/emollick/status/2077951790868238616) (by [@emollick](https://x.com/emollick))

**Évaluer si un mystère généré équilibre les indices, l'obscurité et la préfiguration.**

Ethan Mollick rapporte que Kimi K3 n'a pas écrit un bon meurtre mystère, rendant les indices à la fois trop évidents et trop obscurs et échouant à préfiguration. Il note également que d'autres modèles partagent cette limitation.

Type: Limit | Date: 2026-07-17

---

<a id="case-21"></a>
### Case 21: [Comparez la modélisation et l'animation du Millennium Falcon](https://x.com/gmi_cloud/status/2077903360263676090) (by [@gmi_cloud](https://x.com/gmi_cloud))

**Utilisez des demandes de style et des paramètres d'effort correspondants pour comparer la modélisation 3D, l'animation, le temps et le coût.**

GMI Cloud rapporte avoir comparé Kimi K3 et Fable 5 sur des recréations du Millennium Falcon en style pixel et en style original, avec un effort maximal. Le fournisseur indique que Kimi K3 a pris plus de temps, mais a coûté environ un tiers du prix lors du premier test et moins de la moitié lors d’un autre.

Type: Benchmark | Date: 2026-07-16

---

<a id="case-28"></a>
### Case 28: [Examiner une collection de dix projets Kimi K3](https://x.com/minchoi/status/2077957907857994006) (by [@minchoi](https://x.com/minchoi))

**Utiliser un récapitulatif de projets liés pour découvrir des artefacts concrets pour une vérification séparée.**

L'auteur organise dix exemples de Kimi K3 avec des médias, y compris un émulateur Game Boy Advance. Cet enregistrement est une collection plutôt qu'un seul flux de travail reproductible, donc chaque exemple lié doit être vérifié indépendamment.

Type: Evaluation | Date: 2026-07-17

---

<a id="case-29"></a>
### Case 29: [Comparez une page de destination avancée sur quatre modèles](https://x.com/doutorcaleb/status/2077904020471947773) (by [@doutorcaleb](https://x.com/doutorcaleb))

**Maintenez une demande de page de destination constante et inspectez la profondeur et l'achèvement de l'animation dans les sorties du modèle.**

Le créateur rapporte avoir donné la même invite de page de destination avancée à Kimi K3, Fable, Grok et GPT Terra, et juge Kimi K3 le plus puissant. résultat. Il s'agit d'une comparaison autodéclarée à partir d'une tâche.

Type: Evaluation | Date: 2026-07-16

---

<a id="case-30"></a>
### Case 30: [Évaluer les mécaniques et le coût de jeux rétro](https://x.com/adxtyahq/status/2077860500462055570) (by [@adxtyahq](https://x.com/adxtyahq))

**Comparez le gameplay, la physique, la mécanique, le comportement autonome, l'utilisation des jetons et le coût sur les mêmes tâches de rétro-jeu.**

La source rapporte des tests identiques pour Road Fighter, Battle City et Q*bert et indique 0,28 $ pour Kimi K3, 0,28 $ pour GPT-5.6 et 0,54 $ pour Opus 4.8. Ce sont les chiffres de référence de l'éditeur.

Type: Benchmark | Date: 2026-07-16

---

<a id="case-31"></a>
### Case 31: [Comparez la génération de jeux avec Fable 5](https://x.com/higgsfield_ai/status/2077943629633712490) (by [@higgsfield_ai](https://x.com/higgsfield_ai))

**Utilisez un exemple de jeu généré côte à côte comme une évaluation étroite plutôt qu'un verdict de modèle large.**

Higgsfield présente une comparaison de la génération de jeux Kimi K3 par rapport à Fable 5. Le dossier fourni comprend le support de comparaison mais aucune invite, rubrique de notation ou conditions détaillées.

Type: Evaluation | Date: 2026-07-17

---

<a id="case-34"></a>
### Case 34: [Comparer des tâches complexes de frontend et de développement avec Opus 4.8](https://x.com/op7418/status/2077969583018066116) (by [@op7418](https://x.com/op7418))

**Utilisez plusieurs tâches de codage complexes pour identifier les victoires et les pertes au lieu de déclarer un modèle universellement supérieur.**

Le critique rapporte les tests directs de Kimi K3 par rapport à l'Opus 4.8 et les juge à peu près comparables sur des travaux d'interface et de développement complexes, avec des résultats mitigés. Cela reste l'évaluation d'un évaluateur.

Type: Evaluation | Date: 2026-07-17

---

<a id="case-35"></a>
### Case 35: [Examiner des benchmarks et un test de landing page](https://x.com/adamuchigabriel/status/2077880433925120471) (by [@adamuchigabriel](https://x.com/adamuchigabriel))

**Combinez le contexte de référence avec un test concret de génération de page de destination tout en gardant les deux types de preuves séparés.**

La vidéo présente une discussion de référence, un test de page de destination et des observations de conception frontale pour Kimi K3. L'enregistrement fourni ne fournit pas l'invite de test complète ni la rubrique de notation.

Type: Evaluation | Date: 2026-07-16

---

<a id="case-37"></a>
### Case 37: [Évaluer le raisonnement inductif avec des tâches graphe-vers-formule](https://x.com/s_batzoglou/status/2077884096307454119) (by [@s_batzoglou](https://x.com/s_batzoglou))

**Mesurer l'exactitude, le comportement de rétention et la complexité des formules sur les tâches d'induction de premier ordre.**

L'auteur rapporte une analyse comparative de Kimi K3 et d'autres modèles sur la tâche ICML INDUCTION en utilisant 6 à 10 petits graphiques de 8 à 10 éléments chacun pour déduire une formule de premier ordre. Le message indique que les résultats ont été mis à jour à partir de travaux antérieurs ; aucune nouvelle reproduction indépendante n'est revendiquée ici.

Type: Benchmark | Date: 2026-07-16

---

<a id="case-38"></a>
### Case 38: [Examiner les jeux, landing pages, travaux 3D et contextes étendus rapportés](https://x.com/servasyy_ai/status/2077903775113834689) (by [@servasyy_ai](https://x.com/servasyy_ai))

**Utilisez un résumé multi-sources pour comparer les artefacts concrets et notez les limitations de vitesse ainsi que les réclamations de coûts.**

L'auteur résume les tests rapportés de Kimi K3 sur les jeux, les pages de destination, la génération 3D et le travail en contexte long, tout en concluant que cela vaut la peine d'essayer mais pas encore un remplacement pour Fable 5. Toutes les figures sont des rapports secondaires dans ce résumé.

Type: Evaluation | Date: 2026-07-16

---

<a id="case-40"></a>
### Case 40: [Auditer un plan complexe et contester ses remèdes](https://x.com/doodlestein/status/2077901883637665958) (by [@doodlestein](https://x.com/doodlestein))

**Utiliser un deuxième modèle pour identifier les résultats sous-estimés, les remèdes incorrects et les conclusions qui devraient être rejetées.**

Le créateur rapporte que Kimi K3 a examiné un plan fortement affiné et a constaté que les problèmes graves étaient sous-estimés, environ un tiers des remèdes proposés devaient être corrigés et une conclusion a été réfutée. Ce sont les résultats de cet audit spécifique.

Type: Evaluation | Date: 2026-07-16

---

<a id="case-41"></a>
### Case 41: [Comparez les diagrammes ASCII d'apprentissage par renforcement de style PPO](https://x.com/dejavucoder/status/2077872015856615541) (by [@dejavucoder](https://x.com/dejavucoder))

**Maintenez une invite de diagramme ASCII constante et comparez la façon dont les modèles représentent la boucle d'apprentissage par renforcement.**

La source fournit l'invite pour dessiner une boucle d'apprentissage par renforcement de style PPO en ASCII et montre Kimi K3 Max à côté de Fable 5 High. Le jugement reste une comparaison visuelle d'une tâche.

Type: Evaluation | Date: 2026-07-16

---

<a id="case-42"></a>
### Case 42: [Modéliser dans Blender tout en suivant les erreurs de capacité](https://x.com/Angaisb_/status/2077910845523214668) (by [@Angaisb_](https://x.com/Angaisb_))

**Évaluez la progression partielle de Blender ainsi que la fiabilité du service plutôt que de juger uniquement l'artefact.**

Le créateur montre la progression de la modélisation de Blender à partir de Kimi K3 et signale également des erreurs de capacité répétées. Le travail est incomplet dans la source fournie, donc le résultat partiel et la limitation de fiabilité doivent être considérés ensemble.

Type: Limit | Date: 2026-07-17

---

<a id="case-47"></a>
### Case 47: [Comparer la génération Flappy Bird dans une arène](https://x.com/jun_song/status/2077396996865003739) (by [@jun_song](https://x.com/jun_song))

**Utilisez une tâche d'arène pour comparer deux résultats Flappy Bird générés tout en gardant la tâche de jugement spécifique.**

Le créateur rapporte une comparaison d'arène entre Kimi K3 et Opus 4.8 sur une tâche Flappy Bird et juge Kimi K3 nettement mieux. Aucune invite ou rubrique complète n'est fournie dans le dossier.

Type: Evaluation | Date: 2026-07-15

---

<a id="case-52"></a>
### Case 52: [Résoudre un problème d'induction visuelle Bongard avec un outil](https://x.com/IntuitMachine/status/2077885406528311561) (by [@IntuitMachine](https://x.com/IntuitMachine))

**Tester si l'utilisation d'un outil aide à dériver la règle visuelle dans une tâche de raisonnement Bongard.**

Le créateur rapporte que Kimi K3 a utilisé un outil pour résoudre un problème Bongard que Grok 4.5 et Muse Spark 1.1 n'ont pas résolu dans la même comparaison. Il s'agit du résultat d'une tâche d'un utilisateur, et non d'une référence de raisonnement général.

Type: Evaluation | Date: 2026-07-16

---

<a id="case-53"></a>
### Case 53: [Comparer la qualité visuelle du frontend et le design 3D avec GPT-5.6 Sol](https://x.com/filicroval/status/2077736407506751952) (by [@filicroval](https://x.com/filicroval))

**Inspectez les fonctionnalités, le goût visuel, l'élégance et l'exécution 3D dans une comparaison frontale limitée.**

Le créateur compare Kimi K3 et GPT-5.6 Sol sur la conception du frontend et juge Kimi K3 plus fort en termes de goût visuel, d'élégance et Capacité 3D. L'évaluation est subjective et spécifique à la tâche.

Type: Evaluation | Date: 2026-07-16

---

<a id="case-57"></a>
### Case 57: [Comparez la génération de sites Web sur trois modèles](https://x.com/pengchujin/status/2077962916226298340) (by [@pengchujin](https://x.com/pengchujin))

**Utilisez les sorties de sites Web visibles pour comparer Kimi K3, Fable 5 et GPT-5.6 Sol sur un seul test.**

Le créateur présente une comparaison de génération de sites Web entre Kimi K3, Fable 5 et GPT-5.6 Sol. L'enregistrement fourni n'expose pas l'invite complète ni une grille de notation.

Type: Evaluation | Date: 2026-07-17

---

<a id="case-59"></a>
### Case 59: [Comparez la génération et le coût des jeux 3D procéduraux](https://x.com/adxtyahq/status/2077958193511362856) (by [@adxtyahq](https://x.com/adxtyahq))

**Maintenez une invite constante entre les modèles et inspectez les systèmes de roulette, de machine à sous et de flipper générés avec le coût par exécution.**

L'éditeur rapporte une comparaison de jeux 3D procéduraux multimodèles et répertorie les coûts, y compris 0,71 $ pour Kimi K3 et 0,30 $ pour Grok 4.5. Traitez tous les classements et les coûts comme les résultats de l'exécution de cet éditeur.

Type: Benchmark | Date: 2026-07-17

---

<a id="case-69"></a>
### Case 69: [Comparez les détails et l'éclairage de la scène d'arsenal 3D](https://x.com/hakki_alkan/status/2077887013332636032) (by [@hakki_alkan](https://x.com/hakki_alkan))

**Inspectez la densité des objets, l'éclairage et les détails de la scène dans une comparaison limitée entre Kimi K3 et Opus 4.8.**

La source rapporte que Kimi K3 a produit une scène d’arsenal détaillée avec des étagères remplies, des boîtes et un éclairage réaliste, tandis qu’Opus 4.8 a produit une pièce peu meublée. Il s’agit d’un rapport de comparaison tiers, et non d’un benchmark indépendant.

Type: Evaluation | Date: 2026-07-16

---

## Ressources associées

- [Voir les détails et tarifs de Kimi K3 sur EvoLink](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_model)
- [Ouvrir la documentation API Kimi K3 d’EvoLink](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_api_docs)
- [En savoir plus sur Kimi K3 sur EvoLink](https://evolink.ai/blog/is-kimi-k3-available-on-evolink?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_article)
- La page du modèle et la documentation API EvoLink sont vérifiées; aucune skill Kimi K3 installable n’a été vérifiée

<a id="acknowledge"></a>
## 🙏 Remerciements

Merci aux personnes qui ont partagé publiquement leurs travaux avec Kimi K3

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

*Pour corriger une attribution ou un texte, ouvrez une issue avec une source publique*
