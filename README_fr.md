<div align="center">

<a href="https://evolink.ai/kimi-k3?utm_source=github&utm_medium=banner&utm_campaign=awesome-kimi-k3-usecases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/images/fr-v2.png" alt="Bannière Kimi K3 localisée avec paysage lunaire et appel à l’action EvoLink" width="760"></a>

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

# Cas d’usage remarquables de Kimi K3

## 🍌 Introduction

Bienvenue dans la sélection de cas d’usage Kimi K3 à forte valeur informative

**Nous rassemblons des jeux, scènes 3D, créations animées, intégrations, évaluations et limites pratiques étayés par des sources publiques**

Les 129 cas proviennent de sources publiques à haute confiance. Les titres et auteurs pointent vers les originaux; les candidats faibles, doublons ou insuffisamment étayés sont exclus

## 📊 Vue d’ensemble

- 129 cas à haute confiance de créateurs et praticiens
- Jeux, 3D, frontend, motion design, développement, intégrations, benchmarks et limites pratiques
- Chaque cas conserve la source, l’auteur, le type, la date et les limites factuelles
- Les cas à confiance moyenne sont exclus et les observations individuelles ne deviennent pas des conclusions générales

> [!NOTE]
> La collection privilégie les preuves concrètes et ne reconstitue ni prompts ni étapes absentes

<a id="quick-api-access"></a>
## ⚡ Démarrage rapide

L’ID documenté par EvoLink est `kimi-k3`; la page du modèle et la documentation Chat Completions sont disponibles

1. [Voir les détails et tarifs de Kimi K3 sur EvoLink](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=landing_overview)
2. [Créer ou gérer une clé API EvoLink](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-kimi-k3-usecases&utm_content=api_key)

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

[Ouvrir la documentation API Kimi K3 d’EvoLink](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=first_run)

> [!IMPORTANT]
> La page du modèle et la documentation EvoLink vérifient la route publique et l’ID. Aucune interface Kimi K3 indépendante dans le navigateur ou sans code n’a été vérifiée, et ce dépôt ne revendique pas de test API payant indépendant

## 📑 Menu

| Section | Cases |
|---|---|
| [Jeux interactifs et 3D](#games-3d) | 39 |
| [Frontend et motion design](#frontend-motion) | 27 |
| [Code et intégrations](#coding-integrations) | 16 |
| [Évaluation et limites](#evaluation-limits) | 47 |
| [Ressources associées](#related-resources) | Ressources associées |
| [Démarrage rapide](#quick-api-access) | Démarrage rapide |
| [Remerciements](#acknowledge) | Crédits et corrections |

| Case | Category | What it shows | Type |
|---|---|---|---|
| [Créer un pod racer voxel avec un prompt](#case-1) | Jeux interactifs et 3D | Partir d’une idée courte pour prototyper une course voxel puis cadrer l’itération suivante | Demo |
| [Comparer Frogger avec le même prompt](#case-2) | Jeux interactifs et 3D | Garder le prompt constant pour examiner les différences entre modèles | Evaluation |
| [Générer Frogger et son enregistrement](#case-3) | Jeux interactifs et 3D | Tester en un passage le jeu et le flux d’enregistrement | Demo |
| [Prototyper un porte-avions en Three.js](#case-4) | Jeux interactifs et 3D | Tester la 3D interactive avec une scène précise de lancement et récupération | Demo |
| [Créer un frontend de motion design interactif](#case-5) | Frontend et motion design | Construire des graphismes qui restent interactifs une fois l’animation en pause | Demo |
| [Produire une publicité animée synchronisée](#case-6) | Frontend et motion design | Vérifier la synchronisation de la musique, des effets et du mouvement | Demo |
| [Comparer le design frontend sur la tâche de lampe à lave BridgeBench](#case-7) | Évaluation et limites | Utilisez la tâche de lampe à lave BridgeBench comme une comparaison limitée de conception frontale plutôt qu'un classement universel. | Benchmark |
| [Évaluer l’écriture de scripts dans une voix éditoriale](#case-8) | Évaluation et limites | Mesurez l'adéquation de la voix éditoriale, le classement relatif et le coût par script au sein d'un benchmark interne clairement identifié. | Benchmark |
| [Créez un jeu inspiré de Paper Mario avec des outils d'agent](#case-9) | Jeux interactifs et 3D | Combinez Kimi K3 avec un harnais d'agent et des outils d'actifs pour produire des éléments de jeu 2D et 3D. | Demo |
| [Comparez la conception, le coût et la difficulté du jeu Flappy](#case-10) | Évaluation et limites | Enregistrez les paramètres de difficulté, le coût, la conception et les fonctionnalités de jeu lors de la comparaison des jeux générés. | Benchmark |
| [Générer un jeu de tir à la première personne dans le métro](#case-11) | Jeux interactifs et 3D | Utilisez un paramètre de métro concret pour inspecter un résultat de jeu de tir à la première personne généré. | Demo |
| [Comparez la conception du jeu avec la même invite de conception](#case-12) | Évaluation et limites | Maintenez l'invite de conception constante et inspectez séparément le rythme, le sens de la conception et la sensation du gameplay. | Benchmark |
| [Exiger un examen indépendant pour l'audit statistique](#case-13) | Évaluation et limites | Associer les audits statistiques générés par un modèle avec un expert indépendant ou un examen du modèle avant de s'appuyer sur les résultats. | Limit |
| [Créer une conception de mouvement entièrement dans le code](#case-14) | Frontend et motion design | Testez si un flux de travail de codage unique peut produire une conception de mouvement sans outils de génération auxiliaires. | Demo |
| [Recherchez une personne et créez un site personnel animé](#case-15) | Frontend et motion design | Donnez un aperçu général du site personnel, puis inspectez la recherche, la planification, l'itération et la validation du navigateur du modèle. | Tutorial |
| [Évaluer une exécution frontale lente mais forte](#case-16) | Évaluation et limites | Enregistrer le temps d'achèvement ainsi que la qualité de sortie lors du test d'une tâche frontale. | Evaluation |
| [Générer une simulation de trou noir](#case-17) | Frontend et motion design | Utilisez une tâche de visualisation scientifique pour inspecter une simulation de trou noir générée. | Demo |
| [Créez un MacBook virtuel avec macOS fonctionnel](#case-18) | Code et intégrations | Combinez le rendu matériel Three.js avec une simulation interactive du système d'exploitation de navigateur. | Demo |
| [Modéliser un moteur V8 avec Blender MCP](#case-19) | Jeux interactifs et 3D | Utilisez Blender MCP et une seule requête pour générer un modèle 3D mécanique détaillé. | Integration |
| [Tester les défauts de préfiguration dans l’écriture d’un roman policier](#case-20) | Évaluation et limites | Évaluer si un mystère généré équilibre les indices, l'obscurité et la préfiguration. | Limit |
| [Comparez la modélisation et l'animation du Millennium Falcon](#case-21) | Évaluation et limites | Utilisez des demandes de style et des paramètres d'effort correspondants pour comparer la modélisation 3D, l'animation, le temps et le coût. | Benchmark |
| [Testez la modélisation frontale complexe, les particules et les shaders](#case-22) | Frontend et motion design | Utilisez une invite frontale publique pour inspecter la précision de la modélisation, les effets de particules et la génération de shaders en ligne en un seul passage. | Demo |
| [Créer une arène de combat jouable à partir d’une référence](#case-23) | Jeux interactifs et 3D | Utilisez une seule référence pour tester la génération one-shot d'une arène jouable complète. | Demo |
| [Construire trois jeux rétro autonomes sous forme de fichiers HTML](#case-24) | Jeux interactifs et 3D | Exiger des graphiques, des ennemis, des règles et un jeu autonome dans des fichiers de jeu HTML autonomes. | Benchmark |
| [Construire un compilateur GPU de DSL à PTX](#case-25) | Code et intégrations | Utiliser une tâche de compilateur de bout en bout couvrant un DSL, les passes du compilateur, la génération PTX et un chemin Tensor Core. | Demo |
| [Générer un outil de musique procédurale en une seule tentative](#case-26) | Frontend et motion design | Testez la génération unique d'un générateur de musique procédurale interactif et comparez le résultat visible avec prudence. | Demo |
| [Créer en une passe un jeu de cache-cache avec un caméléon](#case-27) | Jeux interactifs et 3D | Générez un jeu à fichier unique avec correspondance des couleurs, zones procédurales, son et score à plusieurs tours. | Benchmark |
| [Examiner une collection de dix projets Kimi K3](#case-28) | Évaluation et limites | Utiliser un récapitulatif de projets liés pour découvrir des artefacts concrets pour une vérification séparée. | Evaluation |
| [Comparez une page de destination avancée sur quatre modèles](#case-29) | Évaluation et limites | Maintenez une demande de page de destination constante et inspectez la profondeur et l'achèvement de l'animation dans les sorties du modèle. | Evaluation |
| [Évaluer les mécaniques et le coût de jeux rétro](#case-30) | Évaluation et limites | Comparez le gameplay, la physique, la mécanique, le comportement autonome, l'utilisation des jetons et le coût sur les mêmes tâches de rétro-jeu. | Benchmark |
| [Comparez la génération de jeux avec Fable 5](#case-31) | Évaluation et limites | Utilisez un exemple de jeu généré côte à côte comme une évaluation étroite plutôt qu'un verdict de modèle large. | Evaluation |
| [Créer un traceur de rayons de trou noir en temps réel dans WebGL2](#case-32) | Code et intégrations | Tester la génération en une seule fois d'un traceur de rayons géodésique WebGL2 natif dans un fichier HTML. | Benchmark |
| [Créer une page produit Three.js à partir de deux images](#case-33) | Frontend et motion design | Utiliser deux images de référence et une exigence Three.js explicite pour générer une présentation de produit. | Demo |
| [Comparer des tâches complexes de frontend et de développement avec Opus 4.8](#case-34) | Évaluation et limites | Utilisez plusieurs tâches de codage complexes pour identifier les victoires et les pertes au lieu de déclarer un modèle universellement supérieur. | Evaluation |
| [Examiner des benchmarks et un test de landing page](#case-35) | Évaluation et limites | Combinez le contexte de référence avec un test concret de génération de page de destination tout en gardant les deux types de preuves séparés. | Evaluation |
| [Créer un jeu 2,5D à la Paper Mario avec une chaîne d’outils agentiques](#case-36) | Jeux interactifs et 3D | Utilisez Kimi K3 avec Grok Build ou Claude Code et Spriterrific pour assembler un flux de travail de jeu 2.5D. | Tutorial |
| [Évaluer le raisonnement inductif avec des tâches graphe-vers-formule](#case-37) | Évaluation et limites | Mesurer l'exactitude, le comportement de rétention et la complexité des formules sur les tâches d'induction de premier ordre. | Benchmark |
| [Examiner les jeux, landing pages, travaux 3D et contextes étendus rapportés](#case-38) | Évaluation et limites | Utilisez un résumé multi-sources pour comparer les artefacts concrets et notez les limitations de vitesse ainsi que les réclamations de coûts. | Evaluation |
| [Inventez un coupe-pain de luxe et sa page produit](#case-39) | Frontend et motion design | Combinez l'idéation du produit, une vue éclatée, une démonstration et une page de destination dans un seul artefact de conception. | Demo |
| [Auditer un plan complexe et contester ses remèdes](#case-40) | Évaluation et limites | Utiliser un deuxième modèle pour identifier les résultats sous-estimés, les remèdes incorrects et les conclusions qui devraient être rejetées. | Evaluation |
| [Comparez les diagrammes ASCII d'apprentissage par renforcement de style PPO](#case-41) | Évaluation et limites | Maintenez une invite de diagramme ASCII constante et comparez la façon dont les modèles représentent la boucle d'apprentissage par renforcement. | Evaluation |
| [Modéliser dans Blender tout en suivant les erreurs de capacité](#case-42) | Évaluation et limites | Évaluez la progression partielle de Blender ainsi que la fiabilité du service plutôt que de juger uniquement l'artefact. | Limit |
| [Créer un RPG wuxia 3D dans le navigateur](#case-43) | Jeux interactifs et 3D | Combinez le combat au corps à corps, les quêtes, l'inventaire, la météo, les intérieurs, le travail sur l'environnement Blender et les ressources adaptées. | Demo |
| [Créer un jeu multijoueur par navigateur de type Minecraft](#case-44) | Jeux interactifs et 3D | Utiliser un temps et un coût limités pour produire un jeu par navigateur multijoueur en ligne jouable. | Demo |
| [Générer un GIF de pélican récursif de dix secondes](#case-45) | Frontend et motion design | Utilisez un bref d'animation en boucle entièrement spécifié pour inspecter la continuité narrative et la récursion dans un GIF. | Demo |
| [Construire un émulateur Game Boy Advance autour de mGBA WASM](#case-46) | Code et intégrations | Intégrer un modèle 3D sous licence et un véritable noyau d'émulateur, puis améliorer de manière récursive l'interface et le gameplay. | Integration |
| [Comparer la génération Flappy Bird dans une arène](#case-47) | Évaluation et limites | Utilisez une tâche d'arène pour comparer deux résultats Flappy Bird générés tout en gardant la tâche de jugement spécifique. | Evaluation |
| [Recréez un jeu sur navigateur coopératif en écran partagé](#case-48) | Jeux interactifs et 3D | Utilisez une requête pour générer une coopération en écran partagé basée sur un navigateur et une interaction avec l'environnement en temps réel. | Demo |
| [Générer un jeu jouable avec le mode Design de Command Code](#case-49) | Jeux interactifs et 3D | Utilisez la commande de conception du code de commande pour créer un jeu unique et enregistrez si le résultat est jouable. | Demo |
| [Rechercher plusieurs sujets à partir de sources en langue chinoise](#case-50) | Code et intégrations | Utiliser des tâches de recherche de longue durée pour comparer l'exhaustivité et la latence entre les générations de modèles. | Evaluation |
| [Assembler un RPG de navigateur Wuxia cohérent](#case-51) | Jeux interactifs et 3D | Intégrer la traversée, le combat, les quêtes, l'inventaire, la météo, l'exploration et l'environnement 3D dans un seul jeu. | Demo |
| [Résoudre un problème d'induction visuelle Bongard avec un outil](#case-52) | Évaluation et limites | Tester si l'utilisation d'un outil aide à dériver la règle visuelle dans une tâche de raisonnement Bongard. | Evaluation |
| [Comparer la qualité visuelle du frontend et le design 3D avec GPT-5.6 Sol](#case-53) | Évaluation et limites | Inspectez les fonctionnalités, le goût visuel, l'élégance et l'exécution 3D dans une comparaison frontale limitée. | Evaluation |
| [Construire un crossover jouable de Hollow Knight](#case-54) | Jeux interactifs et 3D | Utiliser les ressources de jeu existantes pour créer une bataille jouable entre le Chevalier et Kimi. | Demo |
| [Générer un SVG de profil d’une BMW M4 CS](#case-55) | Frontend et motion design | Utiliser un véhicule et un point de vue spécifiques pour inspecter la sortie de l'illustration vectorielle. | Demo |
| [Cloner macOS dans le navigateur avec des applications fonctionnelles](#case-56) | Code et intégrations | Créer une simulation de système d'exploitation de navigateur qui inclut de la musique, un navigateur et des applications de messagerie. | Demo |
| [Comparez la génération de sites Web sur trois modèles](#case-57) | Évaluation et limites | Utilisez les sorties de sites Web visibles pour comparer Kimi K3, Fable 5 et GPT-5.6 Sol sur un seul test. | Evaluation |
| [Recréer Gargantua grâce aux retours de captures d’écran](#case-58) | Frontend et motion design | Utiliser des captures d'écran répétées comme observations pour diagnostiquer et affiner une visualisation scientifique. | Tutorial |
| [Comparez la génération et le coût des jeux 3D procéduraux](#case-59) | Évaluation et limites | Maintenez une invite constante entre les modèles et inspectez les systèmes de roulette, de machine à sous et de flipper générés avec le coût par exécution. | Benchmark |
| [Créer en une passe un jeu 3D pour navigateur à la Fall Guys](#case-60) | Jeux interactifs et 3D | Utilisez une requête unique pour générer un jeu d'obstacles 3D jouable et exposez le projet pour inspection. | Demo |
| [Construire et auto-tester un FPS apocalyptique de Lisbonne](#case-61) | Jeux interactifs et 3D | Utiliser une exécution à effort maximal fondée sur une seule invite, qui teste, prend des captures d’écran et itère avant de livrer un FPS jouable. | Demo |
| [Créer une simulation macOS avec FaceTime fonctionnel](#case-62) | Code et intégrations | Utiliser une tâche de système d'exploitation virtuel pour tester si une interaction d'application générée fonctionne. | Demo |
| [Générer un jeu de style Animal Crossing à partir d'une simple requête](#case-63) | Jeux interactifs et 3D | Utilisez un résumé de jeu minimal pour inspecter la jouabilité, la boucle de jeu et les effets de parallaxe. | Demo |
| [Ajouter un comparateur d’effets frontend entre deux tâches](#case-64) | Code et intégrations | Créez un outil qui sélectionne deux tâches terminées, les affiche côte à côte et synchronise les vues et les interactions. | Tutorial |
| [Générer un jeu de type Mario à partir d'un brief d'une phrase](#case-65) | Jeux interactifs et 3D | Utiliser une requête unique minimale pour inspecter la jouabilité, la conception de la scène, le pixel art et la parallaxe. | Demo |
| [Affiner une visualisation de trou noir avec 62 captures d'écran](#case-66) | Frontend et motion design | Utiliser une boucle de retours par captures d’écran pour lire, diagnostiquer et corriger une simulation visuelle sur de nombreuses itérations. | Tutorial |
| [Construisez un jeu de tir à la première personne zombie fonctionnel](#case-67) | Jeux interactifs et 3D | Utilisez une cible de tir zombie en béton pour inspecter un artefact FPS jouable complet. | Demo |
| [Créer un PDF marketing post-formation](#case-68) | Frontend et motion design | Utiliser un produit nommé et un format de livrable pour générer un document marketing. | Demo |
| [Comparez les détails et l'éclairage de la scène d'arsenal 3D](#case-69) | Évaluation et limites | Inspectez la densité des objets, l'éclairage et les détails de la scène dans une comparaison limitée entre Kimi K3 et Opus 4.8. | Evaluation |
| [Créer une interface utilisateur à partir d'une seule invite](#case-70) | Frontend et motion design | Utilisez une seule requête pour générer et inspecter une conception d'interface utilisateur complète. | Demo |
| [Créer un jeu indépendant de vaisseau](#case-71) | Jeux interactifs et 3D | Produisez une première version avec Kimi K3 Standard puis comparez cohérence, défauts, qualité visuelle et coût en jetons | Demo |
| [Comparer des frontends avec des invites Arena identiques](#case-72) | Évaluation et limites | Utilisez des invites identiques et des sorties côte à côte plutôt qu'un seul rang | Benchmark |
| [Auto-tester un jeu Summer Engine](#case-73) | Jeux interactifs et 3D | Faites exécuter le jeu par Kimi K3, inspecter captures et journaux, puis corriger les défauts dans la même session | Demo |
| [Évaluer Kimi Code sur des agents de code](#case-74) | Évaluation et limites | Évaluez Kimi K3 sur plusieurs suites et le coût par tâche sans généraliser un classement frontend | Benchmark |
| [Configurer Kimi comme sous-agent Codex](#case-75) | Code et intégrations | Gardez l'orchestration dans Codex et déléguez le frontend à un sous-agent Kimi K3 OpenCode avec une limite claire pour les secrets | Tutorial |
| [Comparer Arena et le banc de réparation](#case-76) | Évaluation et limites | Examinez préférence frontend et réparation de dépôt car Kimi K3 peut être premier dans l'une et septième dans l'autre | Benchmark |
| [Itérer un battle royale dans le navigateur](#case-77) | Jeux interactifs et 3D | Prévoyez de longues itérations autonomes et des invites de suivi ciblées pour un jeu riche en fonctions | Demo |
| [Créer un site de style primé](#case-78) | Frontend et motion design | Évaluez la session enregistrée complète plutôt que la seule capture finale | Tutorial |
| [Router le code simple via ChatLLM](#case-79) | Code et intégrations | Envoyez le code simple à Kimi K3 et réservez le code difficile et le design à d'autres modèles | Integration |
| [Évaluer Kimi K3 avec Prinzbench](#case-80) | Évaluation et limites | Prinzbench compare Kimi K3 à OpenAI o3 et à d’autres modèles, avec un classement et des limites sur le même banc d’essai. | Benchmark |
| [Créer un frontend à métaballes synchronisé au défilement](#case-81) | Frontend et motion design | Kimi K3 assemble une interface web soignée avec des métaballes lumineuses et des animations liées au scroll. | Demo |
| [Comparer la refonte d’un site personnel entre modèles](#case-82) | Frontend et motion design | La même tâche de refonte est donnée à Kimi K3 et à d’autres modèles afin de comparer qualité visuelle et structure. | Evaluation |
| [Étendre un paysage de jeu spatial](#case-83) | Jeux interactifs et 3D | Kimi K3 transforme une scène de jeu spatial en environnement plus large avec terrain, vaisseaux et éclairage. | Demo |
| [Débloquer un rendu physique Three.js](#case-84) | Jeux interactifs et 3D | Kimi K3 sert d’aide d’implémentation pour faire avancer un problème de rendu physique Three.js. | Demo |
| [Comparer la génération d’un jumeau numérique de l’ISS](#case-85) | Évaluation et limites | Kimi K3 est comparé à d’autres modèles sur un jumeau numérique de l’ISS, révélant des écarts en visualisation 3D complexe. | Benchmark |
| [Créer un explorateur interactif du cuir chevelu](#case-86) | Frontend et motion design | Kimi K3 génère un visualiseur pédagogique du cuir chevelu, utile pour des interfaces explicatives. | Demo |
| [Partager un prompt de tableau de bord avec globe 3D](#case-87) | Frontend et motion design | Un prompt public montre comment produire avec Kimi K3 une interface de tableau de bord centrée sur un globe 3D. | Tutorial |
| [Créer un Counter-Strike navigateur en un seul fichier](#case-88) | Jeux interactifs et 3D | Kimi K3 produit un jeu FPS de style Counter-Strike dans un fichier HTML unique. | Demo |
| [Évaluer une forêt WebGPU](#case-89) | Évaluation et limites | Une scène de forêt WebGPU créée avec Kimi K3 est évaluée pour sa qualité immersive et ses limites 3D. | Evaluation |
| [Comparer des prompts de maison vitrée](#case-90) | Évaluation et limites | Utilise la même scène architecturale pour comparer Kimi K3 et Opus 4.8 sur l’atmosphère, la lumière et la complétude spatiale. | Evaluation |
| [Créer CS avec des assets générés](#case-91) | Code et intégrations | Associe Kimi K3 pour le code du jeu et GPT Image 2 pour les assets lors du prototypage d’un petit jeu navigateur façon Counter-Strike. | Integration |
| [Benchmarker un but de football voxel](#case-92) | Évaluation et limites | Lance le même prompt d’animation football en HTML/CSS/JS pur sur deux modèles pour comparer mouvement et coût. | Benchmark |
| [Examiner un benchmark Minecraft](#case-93) | Évaluation et limites | Regarde une revue Minecraft structurée avant de prendre le battage de lancement ou le prix comme preuve suffisante. | Benchmark |
| [Exécuter cinq tests UI UX](#case-94) | Frontend et motion design | Évalue Kimi K3 avec plusieurs tâches UI, logo et Figma MCP au lieu de te fier à une seule capture frontend. | Evaluation |
| [Utiliser la skill Design de Command Code](#case-95) | Code et intégrations | Combine Kimi K3 avec une skill design dédiée dans Command Code pour créer un prototype visuel de jeu sous budget tokens. | Integration |
| [Construire un jeu de pyramide](#case-96) | Jeux interactifs et 3D | Utilise Kimi K3 pour une passe d’une journée sur un jeu 3D d’exploration, puis inspecte quêtes, intérieurs et portée avant de juger la qualité. | Demo |
| [Créer des landings depuis des références](#case-97) | Frontend et motion design | Utilise des tableaux de référence, Figma AI et Motion Sites avec Kimi K3 pour transformer une direction visuelle en sections réutilisables. | Tutorial |
| [Mesurer les limites de niveau API](#case-98) | Évaluation et limites | Planifie les runs agents Kimi K3 selon tokens, niveau, TPM et TPD, pas seulement selon le prix affiché du modèle. | Limit |
| [Comparer une démo façon Limbo](#case-99) | Évaluation et limites | Compare portée jouable, finition, coût et bugs en testant Kimi K3 contre Fable 5 sur le même prototype de jeu. | Benchmark |
| [Examiner les coûts VulcanBench](#case-100) | Évaluation et limites | Utilisez ce cas pour évaluer le workflow réel, le coût ou les limites de Kimi K3 sur « Examiner les coûts VulcanBench ». | Benchmark |
| [Comparer la profondeur Minecraft](#case-101) | Jeux interactifs et 3D | Utilisez ce cas pour évaluer le workflow réel, le coût ou les limites de Kimi K3 sur « Comparer la profondeur Minecraft ». | Evaluation |
| [Créer un FPS Fallout](#case-102) | Jeux interactifs et 3D | Utilisez ce cas pour évaluer le workflow réel, le coût ou les limites de Kimi K3 sur « Créer un FPS Fallout ». | Demo |
| [Suivre un tutoriel web premium](#case-103) | Frontend et motion design | Utilisez ce cas pour évaluer le workflow réel, le coût ou les limites de Kimi K3 sur « Suivre un tutoriel web premium ». | Tutorial |
| [Évaluer la physique du double pendule](#case-104) | Évaluation et limites | Utilisez ce cas pour évaluer le workflow réel, le coût ou les limites de Kimi K3 sur « Évaluer la physique du double pendule ». | Benchmark |
| [Livrer un RPG de data center](#case-105) | Jeux interactifs et 3D | Utilisez ce cas pour évaluer le workflow réel, le coût ou les limites de Kimi K3 sur « Livrer un RPG de data center ». | Demo |
| [Comparer les coûts frontend humanoïde](#case-106) | Frontend et motion design | Utilisez ce cas pour évaluer le workflow réel, le coût ou les limites de Kimi K3 sur « Comparer les coûts frontend humanoïde ». | Benchmark |
| [Examiner la maturité ReactBench](#case-107) | Évaluation et limites | Utilisez ce cas pour évaluer le workflow réel, le coût ou les limites de Kimi K3 sur « Examiner la maturité ReactBench ». | Benchmark |
| [Créer un jeu de voiture 3D](#case-108) | Jeux interactifs et 3D | Utilisez ce cas pour évaluer le workflow réel, le coût ou les limites de Kimi K3 sur « Créer un jeu de voiture 3D ». | Demo |
| [Exécuter Kimi K3 dans Claude Code](#case-109) | Code et intégrations | Utilisez ce cas pour évaluer le workflow réel, le coût ou les limites de Kimi K3 sur « Exécuter Kimi K3 dans Claude Code ». | Integration |
| [Évaluer Kimi K3 sur AA-Briefcase](#case-110) | Évaluation et limites | Utilise les résultats AA-Briefcase pour juger Kimi K3 sur des tâches agentiques de knowledge work avant de croire un leaderboard. | Benchmark |
| [Comparer des clones Geometry Dash](#case-111) | Jeux interactifs et 3D | Compare des builds de jeu avec le même brief pour savoir si Kimi K3 suffit à des prototypes mobiles jouables. | Evaluation |
| [Tester un jeu rétro dans Command Code](#case-112) | Jeux interactifs et 3D | Utilise un run design multi-modèle dans Command Code pour comparer les fonctions gameplay de Kimi K3 et le coût par modèle. | Evaluation |
| [Auditer les limites du leaderboard frontend](#case-113) | Évaluation et limites | Utilise cette note de limite pour séparer les victoires leaderboard de Kimi K3 des affirmations générales sur le coding et le coût. | Limit |
| [Comparer les résultats StackPerf architecture](#case-114) | Évaluation et limites | Utilise StackPerf pour comparer Kimi K3 et Qwen 3.8 sur qualité d’architecture, vitesse et tool calls. | Benchmark |
| [Comparer des builds Three.js Kimi-vs-GLM](#case-115) | Frontend et motion design | Exécute les mêmes prompts procéduraux Three.js avec Kimi K3 et GLM 5.2 pour comparer frontend et 3D. | Benchmark |
| [Benchmarker le jeu Space Discoverer](#case-116) | Jeux interactifs et 3D | Utilise le mini-benchmark Space Discoverer pour comparer des sorties de modèles sur un brief de jeu 3D navigateur. | Benchmark |
| [Créer un jeu de conduite réel](#case-117) | Jeux interactifs et 3D | Prototype un jeu de conduite en associant Kimi K3 à Blender et Godot autour d’une vraie route locale. | Demo |
| [Comparer les coûts Monument Valley](#case-118) | Évaluation et limites | Utilise un seul prompt style Monument Valley pour comparer qualité visuelle, temps et coût entre Kimi K3 et ses pairs. | Benchmark |
| [Router Kimi via claude-code-router](#case-119) | Code et intégrations | Teste Kimi K3 dans un workflow Claude Code existant via claude-code-router en évitant le mode proxy inutile. | Integration |
| [Évaluer Kimi K3 avec l'indice Surge](#case-120) | Évaluation et limites | Utilise les résultats séparés de SurgeAI pour distinguer la force de Kimi K3 en chat quotidien de ses limites en agents d’entreprise et en science. | Benchmark |
| [Créer des landing pages avec référence](#case-121) | Frontend et motion design | Donne à Kimi K3 des références visuelles fortes et un guidage itératif pour tester la génération de landing pages. | Demo |
| [Créer un jeu de plateforme vertical](#case-122) | Jeux interactifs et 3D | Utilise un brief de jeu concis pour tester si Kimi K3 peut produire un prototype navigateur en un seul fichier. | Demo |
| [Comparer les erreurs de solveur PDE](#case-123) | Évaluation et limites | Utilise les échecs de benchmark PDE pour décider où les tâches symboliques ou numériques demandent une vérification avec Kimi K3. | Benchmark |
| [Examiner les cas EHR ClinicalBench](#case-124) | Évaluation et limites | Utilise les cas EHR de ClinicalBench pour voir où Kimi K3 réussit et où le raisonnement diagnostique échoue encore. | Benchmark |
| [Exécuter un harness d'agents ouvert](#case-125) | Code et intégrations | Utilise un harness partagé pour comparer Kimi K3 à d’autres modèles frontier sur des tâches avec outils. | Benchmark |
| [Évaluer les calculs fiscaux](#case-126) | Évaluation et limites | Teste Kimi K3 séparément sur les charges fiscales au lieu de supposer que la force frontend se transfère. | Limit |
| [Vérifier un Geometry Dash généré](#case-127) | Jeux interactifs et 3D | Associe un jeu Kimi K3 à un solveur et à des playtests navigateur avant de le traiter comme prototype terminé. | Benchmark |
| [Simuler un système de particules 3D](#case-128) | Frontend et motion design | Utilise des prompts de simulation de particules pour comparer la qualité de mouvement de Kimi K3 aux modèles fermés. | Evaluation |
| [Exécuter Kimi via Codex OAuth](#case-129) | Code et intégrations | Utilise la route OAuth de Codex quand un workflow de code Kimi K3 doit éviter la configuration manuelle d’une clé API. | Integration |

<a id="games-3d"></a>
## 🎮 Jeux interactifs et 3D

<a id="case-1"></a>
### Case 1: [Créer un pod racer voxel avec un prompt](https://x.com/ivanfioravanti/status/2077763009657627055) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Partir d’une idée courte pour prototyper une course voxel puis cadrer l’itération suivante**

L’auteur indique que Kimi K3 a produit la première version avec un prompt public et prévoit plus de concurrents, une arrivée et une revue des détails

**Prompt:**

```text
Voxel star wars pod-racers run
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01-poster.jpg" alt="Case 1 source video poster" height="360"></a>

[Play case 1 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-2"></a>
### Case 2: [Comparer Frogger avec le même prompt](https://x.com/ivanfioravanti/status/2077754781964054825) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Garder le prompt constant pour examiner les différences entre modèles**

L’auteur partage une version Kimi K3 comme comparaison. La source ne publie ni le prompt ni la grille d’évaluation

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02-poster.jpg" alt="Case 2 source video poster" height="360"></a>

[Play case 2 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-3"></a>
### Case 3: [Générer Frogger et son enregistrement](https://x.com/TheAhmadOsman/status/2077776567292338285) (by [@TheAhmadOsman](https://x.com/TheAhmadOsman))

**Tester en un passage le jeu et le flux d’enregistrement**

L’auteur rapporte un passage pour le jeu et un autre pour l’enregistrement. Les prompts exacts ne sont pas publiés

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03-poster.jpg" alt="Case 3 source video poster" height="360"></a>

[Play case 3 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-4"></a>
### Case 4: [Prototyper un porte-avions en Three.js](https://x.com/HarshithLucky3/status/2077753222018814360) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**Tester la 3D interactive avec une scène précise de lancement et récupération**

L’auteur montre des avions sur un porte-avions de classe Nimitz et juge positivement la génération 3D

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04-poster.jpg" alt="Case 4 source video poster" height="360"></a>

[Play case 4 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-9"></a>
### Case 9: [Créez un jeu inspiré de Paper Mario avec des outils d'agent](https://x.com/chongdashu/status/2077886028866531655) (by [@chongdashu](https://x.com/chongdashu))

**Combinez Kimi K3 avec un harnais d'agent et des outils d'actifs pour produire des éléments de jeu 2D et 3D.**

Le créateur rapporte avoir utilisé Kimi K3 avec Grok Build, Spriterrific pour les ressources 2D et la géométrie pour les ressources 3D dans un jeu inspiré de Paper Mario. La source démontre l'utilisation des outils et des compétences, mais ne publie pas d'invite réutilisable exacte.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-09.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-09-poster.jpg" alt="Case 9 source video poster" height="360"></a>

[Play case 9 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-09.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-11"></a>
### Case 11: [Générer un jeu de tir à la première personne dans le métro](https://x.com/bijanbowen/status/2077881805751873997) (by [@bijanbowen](https://x.com/bijanbowen))

**Utilisez un paramètre de métro concret pour inspecter un résultat de jeu de tir à la première personne généré.**

Le créateur montre un FPS dans le métro attribué à Kimi K3 et note explicitement l'incertitude quant à savoir si le statut d'influenceur a affecté le résultat. Aucun flux de travail rapide ou reproductible n'est fourni.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-11.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-11-poster.jpg" alt="Case 11 source video poster" height="360"></a>

[Play case 11 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-11.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-19"></a>
### Case 19: [Modéliser un moteur V8 avec Blender MCP](https://x.com/aisearchio/status/2077962156147146925) (by [@aisearchio](https://x.com/aisearchio))

**Utilisez Blender MCP et une seule requête pour générer un modèle 3D mécanique détaillé.**

Le critique rapporte que Kimi K3 a généré un moteur V8 complet avec Blender MCP à partir d'une seule invite. Le message relie une critique plus complète mais n'expose pas l'invite exacte dans l'enregistrement fourni.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-19.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-19-poster.jpg" alt="Case 19 source video poster" height="360"></a>

[Play case 19 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-19.mp4)

Type: Integration | Date: 2026-07-17

---

<a id="case-23"></a>
### Case 23: [Créer une arène de combat jouable à partir d’une référence](https://x.com/VORTEX_Promos/status/2077879705378730074) (by [@VORTEX_Promos](https://x.com/VORTEX_Promos))

**Utilisez une seule référence pour tester la génération one-shot d'une arène jouable complète.**

Le créateur rapporte que Kimi K3 a produit une arène de combat jouable en un seul coup à partir d'une seule référence. Une revendication distincte du classement apparaît dans l'article, mais le cas d'utilisation concret est l'artefact d'arène démontré.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23-poster.jpg" alt="Case 23 source video poster" height="360"></a>

[Play case 23 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23-01.jpg" alt="Case 23 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-24"></a>
### Case 24: [Construire trois jeux rétro autonomes sous forme de fichiers HTML](https://x.com/rohanpaul_ai/status/2077889084761206860) (by [@rohanpaul_ai](https://x.com/rohanpaul_ai))

**Exiger des graphiques, des ennemis, des règles et un jeu autonome dans des fichiers de jeu HTML autonomes.**

La source rapporte une comparaison Atomic Chat dans laquelle les modèles ont construit Road Fighter, Battle City et Q*bert sous forme de fichiers HTML autonomes. Sa comparaison de coût et de qualité est rapportée par l'éditeur et n'est pas reproduite indépendamment ici.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-24.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-24-poster.jpg" alt="Case 24 source video poster" height="360"></a>

[Play case 24 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-24.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-27"></a>
### Case 27: [Créer en une passe un jeu de cache-cache avec un caméléon](https://x.com/aimlapi/status/2077898742179459274) (by [@aimlapi](https://x.com/aimlapi))

**Générez un jeu à fichier unique avec correspondance des couleurs, zones procédurales, son et score à plusieurs tours.**

AIMLAPI rapporte une comparaison unique pour un jeu de cache-cache et répertorie les coûts de 3,11 $ pour Kimi K3 et de 12,23 $ pour Fable 5. Les réclamations en matière de fonctionnalités et de coûts sont résultats rapportés par le fournisseur.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-27.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-27-poster.jpg" alt="Case 27 source video poster" height="360"></a>

[Play case 27 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-27.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-36"></a>
### Case 36: [Créer un jeu 2,5D à la Paper Mario avec une chaîne d’outils agentiques](https://x.com/chongdashu/status/2077981621223837739) (by [@chongdashu](https://x.com/chongdashu))

**Utilisez Kimi K3 avec Grok Build ou Claude Code et Spriterrific pour assembler un flux de travail de jeu 2.5D.**

Le créateur fournit une procédure complète en utilisant Grok Build et Kimi K3 et montre la génération de sprites avec Spriterrific. La source identifie les outils mais ne fournit pas d'invites réutilisables exactes.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-36.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-36-poster.jpg" alt="Case 36 source video poster" height="360"></a>

[Play case 36 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-36.mp4)

Type: Tutorial | Date: 2026-07-17

---

<a id="case-43"></a>
### Case 43: [Créer un RPG wuxia 3D dans le navigateur](https://x.com/AngryTomtweets/status/2077868163136450619) (by [@AngryTomtweets](https://x.com/AngryTomtweets))

**Combinez le combat au corps à corps, les quêtes, l'inventaire, la météo, les intérieurs, le travail sur l'environnement Blender et les ressources adaptées.**

La source rapporte un RPG sur navigateur Kimi K3 avec combat au corps à corps, quêtes, inventaire, météo dynamique et intérieurs explorables, plus Modélisation de Blender, améliorations des collisions, retexturation PBR et actifs ouverts adaptés.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-43.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-43-poster.jpg" alt="Case 43 source video poster" height="360"></a>

[Play case 43 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-43.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-44"></a>
### Case 44: [Créer un jeu multijoueur par navigateur de type Minecraft](https://x.com/Alezander907/status/2077926014710407407) (by [@Alezander907](https://x.com/Alezander907))

**Utiliser un temps et un coût limités pour produire un jeu par navigateur multijoueur en ligne jouable.**

Le créateur rapporte que Kimi K3 a construit un jeu multijoueur de type Minecraft jouable par navigateur en une heure au coût de 6,57 $. Il s'agit de chiffres d'exécution autodéclarés à partir d'un artefact.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-44.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-44-poster.jpg" alt="Case 44 source video poster" height="360"></a>

[Play case 44 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-44.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-48"></a>
### Case 48: [Recréez un jeu sur navigateur coopératif en écran partagé](https://x.com/ridark_eth/status/2077882889803378969) (by [@ridark_eth](https://x.com/ridark_eth))

**Utilisez une requête pour générer une coopération en écran partagé basée sur un navigateur et une interaction avec l'environnement en temps réel.**

Le créateur rapporte que Kimi K3 a produit un jeu par navigateur inspiré de It Takes Two en une seule invite, avec Mario et Luigi interagissant en écran partagé et avec l'environnement en temps réel. time.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-48.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-48-poster.jpg" alt="Case 48 source video poster" height="360"></a>

[Play case 48 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-48.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-49"></a>
### Case 49: [Générer un jeu jouable avec le mode Design de Command Code](https://x.com/naymur_dev/status/2077873562661335207) (by [@naymur_dev](https://x.com/naymur_dev))

**Utilisez la commande de conception du code de commande pour créer un jeu unique et enregistrez si le résultat est jouable.**

Le créateur rapporte une comparaison unique en utilisant le mode de conception du code de commande et indique que l'exécution de Kimi K3 a produit un jeu jouable pour 0,038 $. Ce résultat de coût et de qualité est auto-déclaré.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-49.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-49-poster.jpg" alt="Case 49 source video poster" height="360"></a>

[Play case 49 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-49.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-51"></a>
### Case 51: [Assembler un RPG de navigateur Wuxia cohérent](https://x.com/TokenGremlin/status/2077855657068310620) (by [@TokenGremlin](https://x.com/TokenGremlin))

**Intégrer la traversée, le combat, les quêtes, l'inventaire, la météo, l'exploration et l'environnement 3D dans un seul jeu.**

La source rapporte un RPG de navigateur de style Kimi K3 wuxia qui combine combat au corps à corps, quêtes, inventaire, météo dynamique, intérieurs explorables et un Structure de jeu 3D.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-51.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-51-poster.jpg" alt="Case 51 source video poster" height="360"></a>

[Play case 51 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-51.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-54"></a>
### Case 54: [Construire un crossover jouable de Hollow Knight](https://x.com/wangfeng0315/status/2077933531200991583) (by [@wangfeng0315](https://x.com/wangfeng0315))

**Utiliser les ressources de jeu existantes pour créer une bataille jouable entre le Chevalier et Kimi.**

Le créateur, qui déclare travailler chez Kimi, rapporte avoir construit un jeu à partir des ressources de Hollow Knight dans lequel le Chevalier combat Kimi et fournit un lien de jeu public. L'attribution et l'évaluation doivent tenir compte de cette affiliation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54-poster.jpg" alt="Case 54 source video poster" height="360"></a>

[Play case 54 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54-01.jpg" alt="Case 54 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-17

---

<a id="case-60"></a>
### Case 60: [Créer en une passe un jeu 3D pour navigateur à la Fall Guys](https://x.com/aayushman2703/status/2077857886441783526) (by [@aayushman2703](https://x.com/aayushman2703))

**Utilisez une requête unique pour générer un jeu d'obstacles 3D jouable et exposez le projet pour inspection.**

Le créateur rapporte une version unique de Kimi K3 d'un jeu par navigateur de style Fall Guys et indique que l'invite et le projet GitHub sont liés à partir de la source. Cet enregistrement ne reproduit pas cette invite.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-60.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-60-poster.jpg" alt="Case 60 source video poster" height="360"></a>

[Play case 60 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-60.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-61"></a>
### Case 61: [Construire et auto-tester un FPS apocalyptique de Lisbonne](https://x.com/goncalo_canhoto/status/2077863166655037668) (by [@goncalo_canhoto](https://x.com/goncalo_canhoto))

**Utiliser une exécution à effort maximal fondée sur une seule invite, qui teste, prend des captures d’écran et itère avant de livrer un FPS jouable.**

Le créateur rapporte que Kimi K3 a produit un FPS de navigateur apocalyptique de Lisbonne jouable après environ une heure, avec des tests, des captures d'écran et des itérations répétés. Ces détails sur le calendrier et le processus sont auto-déclarés.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-61-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-61-01.jpg" alt="Case 61 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-63"></a>
### Case 63: [Générer un jeu de style Animal Crossing à partir d'une simple requête](https://x.com/gagarot200/status/2077949230287896830) (by [@gagarot200](https://x.com/gagarot200))

**Utilisez un résumé de jeu minimal pour inspecter la jouabilité, la boucle de jeu et les effets de parallaxe.**

Le créateur rapporte que Kimi K3 a généré un jeu de style Animal Crossing entièrement jouable avec une boucle de jeu et des effets de parallaxe à partir d'une invite très simple. Le libellé exact n'est pas présent dans l'enregistrement fourni.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-63.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-63-poster.jpg" alt="Case 63 source video poster" height="360"></a>

[Play case 63 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-63.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-65"></a>
### Case 65: [Générer un jeu de type Mario à partir d'un brief d'une phrase](https://x.com/izutorishima/status/2077939370154475992) (by [@izutorishima](https://x.com/izutorishima))

**Utiliser une requête unique minimale pour inspecter la jouabilité, la conception de la scène, le pixel art et la parallaxe.**

Le créateur rapporte que Kimi K3 a produit un jeu de type Mario fonctionnel sans bugs évidents, y compris la structure de la scène et la parallaxe, à partir d'un seul brief. Le même rapport critique la qualité de la musique et des graphiques.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-01.jpg" alt="Case 65 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-02.jpg" alt="Case 65 source image 2" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-03.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-03.jpg" alt="Case 65 source image 3" height="360"></a>

Type: Demo | Date: 2026-07-17

---

<a id="case-67"></a>
### Case 67: [Construisez un jeu de tir à la première personne zombie fonctionnel](https://x.com/X2worldtech/status/2077902793449296203) (by [@X2worldtech](https://x.com/X2worldtech))

**Utilisez une cible de tir zombie en béton pour inspecter un artefact FPS jouable complet.**

La source montre un FPS zombie entièrement fonctionnel attribué à Kimi K3. Il ne fournit pas d'invite, de détails de mise en œuvre ou d'évaluation externe du gameplay.

> [!WARNING]
> The original source permalink returned HTTP 404 during the 2026-07-17 audit. Attribution and evidence are preserved from the supplied high-confidence source package.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-67.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-67-poster.jpg" alt="Case 67 source video poster" height="360"></a>

[Play case 67 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-67.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-71"></a>
### Case 71: [Créer un jeu indépendant de vaisseau](https://x.com/ChrisGPT/status/2078261217924087999) (by [@ChrisGPT](https://x.com/ChrisGPT))

**Produisez une première version avec Kimi K3 Standard puis comparez cohérence, défauts, qualité visuelle et coût en jetons**

ChrisGPT rapporte une première version d'un jeu de vaisseau pour environ 2,50 dollars de jetons API. Elle était plus cohérente et moins boguée que celle de GPT-5.5, mais Fable 5 restait plus soigné visuellement

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-71.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-71-poster.jpg" alt="Case 71 source video poster" height="360"></a>

[Play case 71 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-71.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-73"></a>
### Case 73: [Auto-tester un jeu Summer Engine](https://x.com/MathiasHeide/status/2078231589436465199) (by [@MathiasHeide](https://x.com/MathiasHeide))

**Faites exécuter le jeu par Kimi K3, inspecter captures et journaux, puis corriger les défauts dans la même session**

Mathias Heide rapporte que Kimi K3 a créé un jeu d'avion en papier en une session de 27 minutes, l'a lancé, a lu captures et logs, corrigé des bogues et changé l'avion noir en blanc

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-73.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-73-poster.jpg" alt="Case 73 source video poster" height="360"></a>

[Play case 73 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-73.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-77"></a>
### Case 77: [Itérer un battle royale dans le navigateur](https://x.com/Ananth7e/status/2078158089929601203) (by [@Ananth7e](https://x.com/Ananth7e))

**Prévoyez de longues itérations autonomes et des invites de suivi ciblées pour un jeu riche en fonctions**

Ananth rapporte plus de 130 minutes et 40 cycles de captures Chrome pour un jeu de type PUBG, puis deux invites supplémentaires pour corriger les derniers bogues

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-77.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-77-poster.jpg" alt="Case 77 source video poster" height="360"></a>

[Play case 77 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-77.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-83"></a>
### Case 83: [Étendre un paysage de jeu spatial](https://x.com/startracker/status/2078543423167160342) (by [@startracker](https://x.com/startracker))

**Kimi K3 transforme une scène de jeu spatial en environnement plus large avec terrain, vaisseaux et éclairage.**

L’image publique montre une scène SF de type jeu et illustre la gestion de la profondeur, des objets multiples et de la palette par Kimi K3.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-83.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-83-poster.jpg" alt="Case 83 source video poster" height="360"></a>

[Play case 83 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-83.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-84"></a>
### Case 84: [Débloquer un rendu physique Three.js](https://x.com/mattwatkajtys/status/2078523373861339475) (by [@mattwatkajtys](https://x.com/mattwatkajtys))

**Kimi K3 sert d’aide d’implémentation pour faire avancer un problème de rendu physique Three.js.**

L’auteur indique avoir résolu un blocage de rendu 3D avec Kimi K3 et montre en vidéo une scène physique dans le navigateur.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-84.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-84-poster.jpg" alt="Case 84 source video poster" height="360"></a>

[Play case 84 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-84.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-88"></a>
### Case 88: [Créer un Counter-Strike navigateur en un seul fichier](https://x.com/prasenx/status/2078453069021659477) (by [@prasenx](https://x.com/prasenx))

**Kimi K3 produit un jeu FPS de style Counter-Strike dans un fichier HTML unique.**

L’auteur montre un jeu exécutable depuis un seul fichier, avec boucle de jeu, entrées, rendu et interface simple.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-88.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-88-poster.jpg" alt="Case 88 source video poster" height="360"></a>

[Play case 88 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-88.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-96"></a>
### Case 96: [Construire un jeu de pyramide](https://x.com/ice_bearcute/status/2078828887468056763) (by [@ice_bearcute](https://x.com/ice_bearcute))

**Utilise Kimi K3 pour une passe d’une journée sur un jeu 3D d’exploration, puis inspecte quêtes, intérieurs et portée avant de juger la qualité.**

ice_bearcute dit avoir construit en une journée un jeu 3D Pyramid Expedition avec Kimi K3. La source précise que ce n’est pas seulement une scène extérieure : on peut explorer une tombe ancienne et terminer des quêtes, avec média attaché comme preuve de gameplay.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-96.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-96-poster.jpg" alt="Case 96 source video poster" height="360"></a>

[Play case 96 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-96.mp4)

Type: Demo | Date: 2026-07-19

---

<a id="case-101"></a>
### Case 101: [Comparer la profondeur Minecraft](https://x.com/vikktorrrre/status/2079294696459804762) (by [@vikktorrrre](https://x.com/vikktorrrre))

**Utilisez ce cas pour évaluer le workflow réel, le coût ou les limites de Kimi K3 sur « Comparer la profondeur Minecraft ».**

Le post source fournit une preuve publique sur « Comparer la profondeur Minecraft », avec description de l’auteur, média du résultat ou informations de benchmark/tutoriel. Le dépôt conserve seulement les faits vérifiables et ne reconstruit pas les prompts ou étapes non publiés.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-101.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-101-poster.jpg" alt="Case 101 source video poster" height="360"></a>

[Play case 101 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-101.mp4)

Type: Evaluation | Date: 2026-07-20

---

<a id="case-102"></a>
### Case 102: [Créer un FPS Fallout](https://x.com/kirillk_web3/status/2079290747585437781) (by [@kirillk_web3](https://x.com/kirillk_web3))

**Utilisez ce cas pour évaluer le workflow réel, le coût ou les limites de Kimi K3 sur « Créer un FPS Fallout ».**

Le post source fournit une preuve publique sur « Créer un FPS Fallout », avec description de l’auteur, média du résultat ou informations de benchmark/tutoriel. Le dépôt conserve seulement les faits vérifiables et ne reconstruit pas les prompts ou étapes non publiés.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-102.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-102-poster.jpg" alt="Case 102 source video poster" height="360"></a>

[Play case 102 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-102.mp4)

Type: Demo | Date: 2026-07-20

---

<a id="case-105"></a>
### Case 105: [Livrer un RPG de data center](https://x.com/demian_ai/status/2079239035596218578) (by [@demian_ai](https://x.com/demian_ai))

**Utilisez ce cas pour évaluer le workflow réel, le coût ou les limites de Kimi K3 sur « Livrer un RPG de data center ».**

Le post source fournit une preuve publique sur « Livrer un RPG de data center », avec description de l’auteur, média du résultat ou informations de benchmark/tutoriel. Le dépôt conserve seulement les faits vérifiables et ne reconstruit pas les prompts ou étapes non publiés.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-105.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-105-poster.jpg" alt="Case 105 source video poster" height="360"></a>

[Play case 105 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-105.mp4)

Type: Demo | Date: 2026-07-20

---

<a id="case-108"></a>
### Case 108: [Créer un jeu de voiture 3D](https://x.com/LexnLin/status/2079233761242235081) (by [@LexnLin](https://x.com/LexnLin))

**Utilisez ce cas pour évaluer le workflow réel, le coût ou les limites de Kimi K3 sur « Créer un jeu de voiture 3D ».**

Le post source fournit une preuve publique sur « Créer un jeu de voiture 3D », avec description de l’auteur, média du résultat ou informations de benchmark/tutoriel. Le dépôt conserve seulement les faits vérifiables et ne reconstruit pas les prompts ou étapes non publiés.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-poster.jpg" alt="Case 108 source video poster" height="360"></a>

[Play case 108 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-01.jpg" alt="Case 108 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-108-02.jpg" alt="Case 108 source image 2" height="360"></a>

Type: Demo | Date: 2026-07-20

---

<a id="case-111"></a>
### Case 111: [Comparer des clones Geometry Dash](https://x.com/Nekt_0/status/2079629004483465473) (by [@Nekt_0](https://x.com/Nekt_0))

**Compare des builds de jeu avec le même brief pour savoir si Kimi K3 suffit à des prototypes mobiles jouables.**

Nekt dit que Kimi K3 a passé environ 30 minutes et 200 000 tokens à créer un clone type Geometry Dash avec sauts, obstacles, niveaux, musique et effets visuels, puis le compare à un build Claude Fable 5 dans la vidéo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-111.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-111-poster.jpg" alt="Case 111 source video poster" height="360"></a>

[Play case 111 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-111.mp4)

Type: Evaluation | Date: 2026-07-21

---

<a id="case-112"></a>
### Case 112: [Tester un jeu rétro dans Command Code](https://x.com/naymur_dev/status/2079627963000398334) (by [@naymur_dev](https://x.com/naymur_dev))

**Utilise un run design multi-modèle dans Command Code pour comparer les fonctions gameplay de Kimi K3 et le coût par modèle.**

Naymur rapporte le même prompt /design dans Command Code avec Fable 5, GPT-5.6 Sol, Grok 4.5 et Kimi K3. Le post dit que Kimi K3 a produit un jeu rétro ASCII avec gameplay, niveaux, tirs et boss, pour un coût annoncé de $0.15.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-112.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-112-poster.jpg" alt="Case 112 source video poster" height="360"></a>

[Play case 112 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-112.mp4)

Type: Evaluation | Date: 2026-07-21

---

<a id="case-116"></a>
### Case 116: [Benchmarker le jeu Space Discoverer](https://x.com/fabriciocarraro/status/2079548607393382528) (by [@fabriciocarraro](https://x.com/fabriciocarraro))

**Utilise le mini-benchmark Space Discoverer pour comparer des sorties de modèles sur un brief de jeu 3D navigateur.**

Fabricio Carraro rapporte un mini-benchmark avec Claude Fable 5, GPT-5.6 Sol et Kimi K3 au niveau de raisonnement maximal. La tâche était un jeu 3D navigateur nommé Space Discoverer, et les trois modèles ont convergé vers Three.js sur WebGL 2.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-116.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-116-poster.jpg" alt="Case 116 source video poster" height="360"></a>

[Play case 116 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-116.mp4)

Type: Benchmark | Date: 2026-07-21

---

<a id="case-117"></a>
### Case 117: [Créer un jeu de conduite réel](https://x.com/bijanbowen/status/2079526003643179102) (by [@bijanbowen](https://x.com/bijanbowen))

**Prototype un jeu de conduite en associant Kimi K3 à Blender et Godot autour d’une vraie route locale.**

Bijan Bowen montre Kimi K3 en train de créer un jeu de conduite avec Blender et Godot, en utilisant une vraie portion de route près de lui comme base de carte. La vidéo jointe est la preuve publique de l’état du build.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-117.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-117-poster.jpg" alt="Case 117 source video poster" height="360"></a>

[Play case 117 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-117.mp4)

Type: Demo | Date: 2026-07-21

---

<a id="case-122"></a>
### Case 122: [Créer un jeu de plateforme vertical](https://x.com/diegocabezas01/status/2079946676270219488) (by [@diegocabezas01](https://x.com/diegocabezas01))

**Utilise un brief de jeu concis pour tester si Kimi K3 peut produire un prototype navigateur en un seul fichier.**

Diego Cabezas montre un run Kimi K3 Max pour un jeu vertical où le joueur saute toujours plus haut pendant que les plateformes bougent. Le post indique un résultat one-shot en HTML unique.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-122.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-122-poster.jpg" alt="Case 122 source video poster" height="360"></a>

[Play case 122 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-122.mp4)

Type: Demo | Date: 2026-07-22

---

<a id="case-127"></a>
### Case 127: [Vérifier un Geometry Dash généré](https://x.com/Kirratr/status/2079902410042909108) (by [@Kirratr](https://x.com/Kirratr))

**Associe un jeu Kimi K3 à un solveur et à des playtests navigateur avant de le traiter comme prototype terminé.**

Kirratr rapporte que Kimi K3 a pris 36:53 sur le même brief Geometry Dash. Un solveur beam-search a trouvé une trajectoire gagnante de 64 sauts, rejouée dans le navigateur sans erreur console.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-127.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-127-poster.jpg" alt="Case 127 source video poster" height="360"></a>

[Play case 127 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-127.mp4)

Type: Benchmark | Date: 2026-07-22

---


<a id="frontend-motion"></a>
## 🎨 Frontend et motion design

<a id="case-5"></a>
### Case 5: [Créer un frontend de motion design interactif](https://x.com/chetaslua/status/2077749371144442022) (by [@chetaslua](https://x.com/chetaslua))

**Construire des graphismes qui restent interactifs une fois l’animation en pause**

L’auteur rapporte 42 minutes, un passage, du code simple, sans harness, MCP ni skills

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05-poster.jpg" alt="Case 5 source video poster" height="360"></a>

[Play case 5 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-6"></a>
### Case 6: [Produire une publicité animée synchronisée](https://x.com/abhinavflac/status/2077760297918484667) (by [@abhinavflac](https://x.com/abhinavflac))

**Vérifier la synchronisation de la musique, des effets et du mouvement**

L’auteur rapporte une publicité de style Spotify produite en un prompt. Le prompt exact n’est pas publié

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06-poster.jpg" alt="Case 6 source video poster" height="360"></a>

[Play case 6 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-14"></a>
### Case 14: [Créer une conception de mouvement entièrement dans le code](https://x.com/chetaslua/status/2077952938564354503) (by [@chetaslua](https://x.com/chetaslua))

**Testez si un flux de travail de codage unique peut produire une conception de mouvement sans outils de génération auxiliaires.**

Le créateur rapporte un résultat de conception de mouvement unique Kimi K3 entièrement réalisé en code sans MCP, compétences, outils, génération de vidéo ou invites spéciales. L'invite exacte n'est pas fournie.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-14.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-14-poster.jpg" alt="Case 14 source video poster" height="360"></a>

[Play case 14 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-14.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-15"></a>
### Case 15: [Recherchez une personne et créez un site personnel animé](https://x.com/nicky_sap/status/2077857190707429411) (by [@nicky_sap](https://x.com/nicky_sap))

**Donnez un aperçu général du site personnel, puis inspectez la recherche, la planification, l'itération et la validation du navigateur du modèle.**

Le créateur rapporte que Kimi K3 a fait des recherches sur Nick Saponaro et a produit un site Web personnel animé à partir d'une large demande, y compris la planification, les tests, l'itération et les vérifications du navigateur. Le résultat est une démonstration de flux de travail auto-déclarée.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-15.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-15-poster.jpg" alt="Case 15 source video poster" height="360"></a>

[Play case 15 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-15.mp4)

Type: Tutorial | Date: 2026-07-16

---

<a id="case-17"></a>
### Case 17: [Générer une simulation de trou noir](https://x.com/chetaslua/status/2077961850352971796) (by [@chetaslua](https://x.com/chetaslua))

**Utilisez une tâche de visualisation scientifique pour inspecter une simulation de trou noir générée.**

Le créateur montre une simulation de trou noir attribuée à Kimi K3 et l'appelle la meilleure qu'il ait vue. La source fournit un résultat visible mais aucune invite, rubrique ou validation indépendante.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-17.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-17-poster.jpg" alt="Case 17 source video poster" height="360"></a>

[Play case 17 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-17.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-22"></a>
### Case 22: [Testez la modélisation frontale complexe, les particules et les shaders](https://x.com/karminski3/status/2077889959223337099) (by [@karminski3](https://x.com/karminski3))

**Utilisez une invite frontale publique pour inspecter la précision de la modélisation, les effets de particules et la génération de shaders en ligne en un seul passage.**

Le créateur rapporte un résultat frontal Kimi K3 en un seul passage couvrant la modélisation précise, les effets de particules et le code de shader en ligne complexe, et déclare que l'invite de test est publique sur la source liée.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-22.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-22-poster.jpg" alt="Case 22 source video poster" height="360"></a>

[Play case 22 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-22.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-26"></a>
### Case 26: [Générer un outil de musique procédurale en une seule tentative](https://x.com/mirochill/status/2077723551331758478) (by [@mirochill](https://x.com/mirochill))

**Testez la génération unique d'un générateur de musique procédurale interactif et comparez le résultat visible avec prudence.**

Le créateur rapporte que Kimi K3 a généré un outil de musique procédurale en une seule tentative et le compare favorablement aux résultats de Fable 5 et GPT-5.6 Sol. Il s'agit de l'ensemble de tests du créateur, et non d'une référence standardisée.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-26-poster.jpg" alt="Case 26 source video poster" height="360"></a>

[Play case 26 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-26.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-33"></a>
### Case 33: [Créer une page produit Three.js à partir de deux images](https://x.com/1littlecoder/status/2077890296806031665) (by [@1littlecoder](https://x.com/1littlecoder))

**Utiliser deux images de référence et une exigence Three.js explicite pour générer une présentation de produit.**

Le créateur rapporte que Kimi K3 a conçu une page produit à partir de deux images et a produit la version Three.js explicitement demandée. Aucune autre invite ni aucun détail de mise en œuvre n'est fourni.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-33.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-33-poster.jpg" alt="Case 33 source video poster" height="360"></a>

[Play case 33 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-33.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-39"></a>
### Case 39: [Inventez un coupe-pain de luxe et sa page produit](https://x.com/filicroval/status/2077871090731221438) (by [@filicroval](https://x.com/filicroval))

**Combinez l'idéation du produit, une vue éclatée, une démonstration et une page de destination dans un seul artefact de conception.**

Le créateur rapporte que Kimi K3 a inventé un coupe-pain de style guillotine, l'a présenté comme un produit de luxe et a produit une page de destination avec une vue éclatée et démonstration.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-39.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-39-poster.jpg" alt="Case 39 source video poster" height="360"></a>

[Play case 39 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-39.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-45"></a>
### Case 45: [Générer un GIF de pélican récursif de dix secondes](https://x.com/1littlecoder/status/2077880380900937865) (by [@1littlecoder](https://x.com/1littlecoder))

**Utilisez un bref d'animation en boucle entièrement spécifié pour inspecter la continuité narrative et la récursion dans un GIF.**

La source inclut une invite pour un GIF en boucle de dix secondes d'un pélican faisant du vélo et recevant la même vidéo par texte lorsque la caméra zoome. Le créateur montre celui de Kimi K3. animation résultante.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-45.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-45-poster.jpg" alt="Case 45 source video poster" height="360"></a>

[Play case 45 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-45.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-55"></a>
### Case 55: [Générer un SVG de profil d’une BMW M4 CS](https://x.com/HarshithLucky3/status/2077765821380886942) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**Utiliser un véhicule et un point de vue spécifiques pour inspecter la sortie de l'illustration vectorielle.**

Le créateur montre une vue latérale BMW M4 CS SVG attribuée à Kimi K3 Max. La source fournie contient l'artefact mais aucune invite ni étape de production.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-55-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-55-01.jpg" alt="Case 55 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-58"></a>
### Case 58: [Recréer Gargantua grâce aux retours de captures d’écran](https://x.com/AngryTomtweets/status/2077868981659324444) (by [@AngryTomtweets](https://x.com/AngryTomtweets))

**Utiliser des captures d'écran répétées comme observations pour diagnostiquer et affiner une visualisation scientifique.**

La source rapporte que Kimi K3 a recréé Gargantua d’Interstellar au fil de 62 auto-captures d’écran, en lisant chaque résultat, en diagnostiquant les problèmes puis en agissant de manière itérative.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-58.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-58-poster.jpg" alt="Case 58 source video poster" height="360"></a>

[Play case 58 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-58.mp4)

Type: Tutorial | Date: 2026-07-16

---

<a id="case-66"></a>
### Case 66: [Affiner une visualisation de trou noir avec 62 captures d'écran](https://x.com/TokenGremlin/status/2077855959201042645) (by [@TokenGremlin](https://x.com/TokenGremlin))

**Utiliser une boucle de retours par captures d’écran pour lire, diagnostiquer et corriger une simulation visuelle sur de nombreuses itérations.**

La source rapporte que Kimi K3 a reconstruit le Gargantua d'Interstellar en observant et en affinant sa sortie sur 62 captures d'écran. Cela démontre la boucle de rétroaction signalée plutôt qu'une précision physique indépendante.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-66.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-66-poster.jpg" alt="Case 66 source video poster" height="360"></a>

[Play case 66 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-66.mp4)

Type: Tutorial | Date: 2026-07-16

---

<a id="case-68"></a>
### Case 68: [Créer un PDF marketing post-formation](https://x.com/Satvik_Pen/status/2077859673517023313) (by [@Satvik_Pen](https://x.com/Satvik_Pen))

**Utiliser un produit nommé et un format de livrable pour générer un document marketing.**

Le créateur rapporte avoir demandé à Kimi K3 un PDF marketing sur la post-formation Inkling de Thinking Machines et partage le résultat, tout en louant également le processus en coulisses. Aucune invite ou critère d'évaluation n'est fourni.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-01.png" alt="Case 68 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-02.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-02.png" alt="Case 68 source image 2" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-03.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-03.png" alt="Case 68 source image 3" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-04.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-04.png" alt="Case 68 source image 4" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-70"></a>
### Case 70: [Créer une interface utilisateur à partir d'une seule invite](https://x.com/BrianMRey/status/2077891942088671689) (by [@BrianMRey](https://x.com/BrianMRey))

**Utilisez une seule requête pour générer et inspecter une conception d'interface utilisateur complète.**

Le créateur montre une conception d'interface utilisateur attribuée à une exécution en une seule invite de Kimi K3 et donne une évaluation subjective fortement positive. L'invite et la rubrique exactes ne sont pas incluses.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-70.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-70-poster.jpg" alt="Case 70 source video poster" height="360"></a>

[Play case 70 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-70.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-78"></a>
### Case 78: [Créer un site de style primé](https://x.com/viktoroddy/status/2078140696910037002) (by [@viktoroddy](https://x.com/viktoroddy))

**Évaluez la session enregistrée complète plutôt que la seule capture finale**

Viktor Oddy publie un tutoriel de 13 minutes pour créer avec Kimi K3 un site au style primé et fournit une preuve du processus complet

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-78.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-78-poster.jpg" alt="Case 78 source video poster" height="360"></a>

[Play case 78 tutorial video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-78.mp4)

Type: Tutorial | Date: 2026-07-17

---

<a id="case-81"></a>
### Case 81: [Créer un frontend à métaballes synchronisé au défilement](https://x.com/abhinavflac/status/2078603131055993130) (by [@abhinavflac](https://x.com/abhinavflac))

**Kimi K3 assemble une interface web soignée avec des métaballes lumineuses et des animations liées au scroll.**

La vidéo montre un frontend dynamique terminé, reliant effets visuels, mise en page et mouvement à partir du prompt.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-81.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-81-poster.jpg" alt="Case 81 source video poster" height="360"></a>

[Play case 81 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-81.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-82"></a>
### Case 82: [Comparer la refonte d’un site personnel entre modèles](https://x.com/fabriciocarraro/status/2078574831466078265) (by [@fabriciocarraro](https://x.com/fabriciocarraro))

**La même tâche de refonte est donnée à Kimi K3 et à d’autres modèles afin de comparer qualité visuelle et structure.**

Le post met plusieurs sorties côte à côte et permet d’observer les choix de design, l’organisation des sections et le niveau de finition de Kimi K3.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-82.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-82-poster.jpg" alt="Case 82 source video poster" height="360"></a>

[Play case 82 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-82.mp4)

Type: Evaluation | Date: 2026-07-18

---

<a id="case-86"></a>
### Case 86: [Créer un explorateur interactif du cuir chevelu](https://x.com/MiaAI_lab/status/2078508824752017757) (by [@MiaAI_lab](https://x.com/MiaAI_lab))

**Kimi K3 génère un visualiseur pédagogique du cuir chevelu, utile pour des interfaces explicatives.**

La démo montre une exploration interactive des structures du cuir chevelu, avec un cas d’usage médical et éducatif plausible.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-86.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-86-poster.jpg" alt="Case 86 source video poster" height="360"></a>

[Play case 86 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-86.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-87"></a>
### Case 87: [Partager un prompt de tableau de bord avec globe 3D](https://x.com/hqmank/status/2078465403349840144) (by [@hqmank](https://x.com/hqmank))

**Un prompt public montre comment produire avec Kimi K3 une interface de tableau de bord centrée sur un globe 3D.**

Le post inclut le prompt et la vidéo finale, combinant globe, affichage de données et composition de dashboard.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-87.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-87-poster.jpg" alt="Case 87 source video poster" height="360"></a>

[Play case 87 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-87.mp4)

Type: Tutorial | Date: 2026-07-18

---

<a id="case-94"></a>
### Case 94: [Exécuter cinq tests UI UX](https://x.com/MAXdeg0/status/2078855257686196399) (by [@MAXdeg0](https://x.com/MAXdeg0))

**Évalue Kimi K3 avec plusieurs tâches UI, logo et Figma MCP au lieu de te fier à une seule capture frontend.**

MAXdeg0 rapporte cinq tests UI/UX et logo avec Kimi K3 via Claude Code et le serveur Figma MCP. La source liste des tâches comme reconstruction de landing page, hero section et travail de marque, avec temps et coût concrets pour au moins la landing.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-94.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-94-poster.jpg" alt="Case 94 source video poster" height="360"></a>

[Play case 94 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-94.mp4)

Type: Evaluation | Date: 2026-07-19

---

<a id="case-97"></a>
### Case 97: [Créer des landings depuis des références](https://x.com/MAXdeg0/status/2078776969072877715) (by [@MAXdeg0](https://x.com/MAXdeg0))

**Utilise des tableaux de référence, Figma AI et Motion Sites avec Kimi K3 pour transformer une direction visuelle en sections réutilisables.**

MAXdeg0 décrit un workflow de landing page : tirer des styles de Pinterest, remixer avec Figma AI, ou coller référence UI plus prompt dans Motion Sites pour que Kimi K3 construise la page. Le post indique que la technique se réutilise sur d’autres sections et renvoie à un guide.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-97.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-97-poster.jpg" alt="Case 97 source video poster" height="360"></a>

[Play case 97 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-97.mp4)

Type: Tutorial | Date: 2026-07-19

---

<a id="case-103"></a>
### Case 103: [Suivre un tutoriel web premium](https://x.com/_guillecasaus/status/2079258261014908980) (by [@_guillecasaus](https://x.com/_guillecasaus))

**Utilisez ce cas pour évaluer le workflow réel, le coût ou les limites de Kimi K3 sur « Suivre un tutoriel web premium ».**

Le post source fournit une preuve publique sur « Suivre un tutoriel web premium », avec description de l’auteur, média du résultat ou informations de benchmark/tutoriel. Le dépôt conserve seulement les faits vérifiables et ne reconstruit pas les prompts ou étapes non publiés.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-103.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-103-poster.jpg" alt="Case 103 source video poster" height="360"></a>

[Play case 103 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-103.mp4)

Type: Tutorial | Date: 2026-07-20

---

<a id="case-106"></a>
### Case 106: [Comparer les coûts frontend humanoïde](https://x.com/ChrisGPT/status/2079236298464796958) (by [@ChrisGPT](https://x.com/ChrisGPT))

**Utilisez ce cas pour évaluer le workflow réel, le coût ou les limites de Kimi K3 sur « Comparer les coûts frontend humanoïde ».**

Le post source fournit une preuve publique sur « Comparer les coûts frontend humanoïde », avec description de l’auteur, média du résultat ou informations de benchmark/tutoriel. Le dépôt conserve seulement les faits vérifiables et ne reconstruit pas les prompts ou étapes non publiés.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-106.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-106-poster.jpg" alt="Case 106 source video poster" height="360"></a>

[Play case 106 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-106.mp4)

Type: Benchmark | Date: 2026-07-20

---

<a id="case-115"></a>
### Case 115: [Comparer des builds Three.js Kimi-vs-GLM](https://x.com/thehypedotnews/status/2079553731218325840) (by [@thehypedotnews](https://x.com/thehypedotnews))

**Exécute les mêmes prompts procéduraux Three.js avec Kimi K3 et GLM 5.2 pour comparer frontend et 3D.**

The Hype dit avoir testé Kimi K3 et GLM 5.2 avec trois prompts HTML single-file et Three.js : salon fin années 80 avec texture canvas CRT, vélo de route avec cinématique de transmission et aquarium en verre.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-115.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-115-poster.jpg" alt="Case 115 source video poster" height="360"></a>

[Play case 115 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-115.mp4)

Type: Benchmark | Date: 2026-07-21

---

<a id="case-121"></a>
### Case 121: [Créer des landing pages avec référence](https://x.com/Oluwaphilemon1/status/2079951300108697683) (by [@Oluwaphilemon1](https://x.com/Oluwaphilemon1))

**Donne à Kimi K3 des références visuelles fortes et un guidage itératif pour tester la génération de landing pages.**

Oluwaphilemon décrit une image de référence et un prompt détaillé pour une landing page. La source note que Kimi a d’abord essayé de créer le vélo en 3D, puis a obtenu un résultat plus propre après quelques itérations guidées.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-121.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-121-poster.jpg" alt="Case 121 source video poster" height="360"></a>

[Play case 121 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-121.mp4)

Type: Demo | Date: 2026-07-22

---

<a id="case-128"></a>
### Case 128: [Simuler un système de particules 3D](https://x.com/jadeferrara_/status/2079884161251262540) (by [@jadeferrara_](https://x.com/jadeferrara_))

**Utilise des prompts de simulation de particules pour comparer la qualité de mouvement de Kimi K3 aux modèles fermés.**

Jade Ferrara rapporte avoir donné le même prompt de système de particules 3D à Kimi K3 et Opus 4.8. Kimi aurait produit une distribution plus organique, un mouvement plus fluide et un coût API plus bas.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-128.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-128-poster.jpg" alt="Case 128 source video poster" height="360"></a>

[Play case 128 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-128.mp4)

Type: Evaluation | Date: 2026-07-22

---


<a id="coding-integrations"></a>
## 💻 Code et intégrations

<a id="case-18"></a>
### Case 18: [Créez un MacBook virtuel avec macOS fonctionnel](https://x.com/scottstts/status/2077890054299541890) (by [@scottstts](https://x.com/scottstts))

**Combinez le rendu matériel Three.js avec une simulation interactive du système d'exploitation de navigateur.**

La source rapporte que Kimi K3 a créé un MacBook virtuel dans Three.js avec un environnement fonctionnel de style macOS. Il démontre l'artefact mais ne fournit pas les étapes de mise en œuvre.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-18.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-18-poster.jpg" alt="Case 18 source video poster" height="360"></a>

[Play case 18 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-18.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-25"></a>
### Case 25: [Construire un compilateur GPU de DSL à PTX](https://x.com/rohanpaul_ai/status/2077886618657231220) (by [@rohanpaul_ai](https://x.com/rohanpaul_ai))

**Utiliser une tâche de compilateur de bout en bout couvrant un DSL, les passes du compilateur, la génération PTX et un chemin Tensor Core.**

La source rapporte que Kimi K3 a construit un compilateur GPU à partir de zéro, à partir de son DSL et passe par la génération PTX, et compare son Chemin Tensor Core avec Triton. Aucun détail de référence indépendant n'est inclus dans l'enregistrement fourni.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-25-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-25-01.png" alt="Case 25 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-32"></a>
### Case 32: [Créer un traceur de rayons de trou noir en temps réel dans WebGL2](https://x.com/AlicanKiraz0/status/2077885419744612597) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**Tester la génération en une seule fois d'un traceur de rayons géodésique WebGL2 natif dans un fichier HTML.**

L'auteur décrit un test de codage nécessitant un traceur de rayons de courbure de lumière de trou noir à fichier unique fonctionnel dans WebGL2 natif. L'enregistrement fourni établit la tâche et les modèles participants, mais pas un audit de résultat entièrement indépendant.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-32.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-32-poster.jpg" alt="Case 32 source video poster" height="360"></a>

[Play case 32 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-32.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-46"></a>
### Case 46: [Construire un émulateur Game Boy Advance autour de mGBA WASM](https://x.com/teortaxesTex/status/2077925090168062272) (by [@teortaxesTex](https://x.com/teortaxesTex))

**Intégrer un modèle 3D sous licence et un véritable noyau d'émulateur, puis améliorer de manière récursive l'interface et le gameplay.**

Le projet Kimi K3 cité adapte un modèle sous licence AGB-001, intègre un noyau mGBA WASM et améliore l'interface et le gameplay grâce à une auto-amélioration récursive. Le message cite une description du projet plutôt qu'une reproduction indépendante.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-46-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-46-01.jpg" alt="Case 46 source image 1" height="360"></a>

Type: Integration | Date: 2026-07-17

---

<a id="case-50"></a>
### Case 50: [Rechercher plusieurs sujets à partir de sources en langue chinoise](https://x.com/tphuang/status/2077911994607239400) (by [@tphuang](https://x.com/tphuang))

**Utiliser des tâches de recherche de longue durée pour comparer l'exhaustivité et la latence entre les générations de modèles.**

L'auteur rapporte avoir testé Kimi K3 sur de nombreux sujets de recherche en utilisant des sources en langue chinoise, le trouvant plus approfondi que K2.6 mais plus lent. Le message note également une forte demande de service à l'époque.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-50-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-50-01.png" alt="Case 50 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-17

---

<a id="case-56"></a>
### Case 56: [Cloner macOS dans le navigateur avec des applications fonctionnelles](https://x.com/twid/status/2077924755357974989) (by [@twid](https://x.com/twid))

**Créer une simulation de système d'exploitation de navigateur qui inclut de la musique, un navigateur et des applications de messagerie.**

La source rapporte que Kimi K3 a été utilisé pour créer un clone macOS basé sur un navigateur avec de la musique, un navigateur, une messagerie électronique et d'autres fonctions. Il ne fournit pas de détails de mise en œuvre.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-56.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-56-poster.jpg" alt="Case 56 source video poster" height="360"></a>

[Play case 56 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-56.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-62"></a>
### Case 62: [Créer une simulation macOS avec FaceTime fonctionnel](https://x.com/LinearUncle/status/2077919552239997078) (by [@LinearUncle](https://x.com/LinearUncle))

**Utiliser une tâche de système d'exploitation virtuel pour tester si une interaction d'application générée fonctionne.**

Le créateur montre un environnement de style macOS attribué à Kimi K3 et signale que sa fonctionnalité FaceTime fonctionne. La source ne fournit aucune étape de configuration ou de validation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-62-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-62-01.jpg" alt="Case 62 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-17

---

<a id="case-64"></a>
### Case 64: [Ajouter un comparateur d’effets frontend entre deux tâches](https://x.com/MinLiBuilds/status/2077939461510615376) (by [@MinLiBuilds](https://x.com/MinLiBuilds))

**Créez un outil qui sélectionne deux tâches terminées, les affiche côte à côte et synchronise les vues et les interactions.**

Le créateur rapporte avoir demandé à Kimi K3 d'ajouter un flux de travail de comparaison frontale avec sélection de tâches, deux volets de navigateur, modes objet et itinérance, points de vue synchronisés et tests d'interaction. L'article note également des limitations plus larges du modèle.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-64.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-64-poster.jpg" alt="Case 64 source video poster" height="360"></a>

[Play case 64 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-64.mp4)

Type: Tutorial | Date: 2026-07-17

---

<a id="case-75"></a>
### Case 75: [Configurer Kimi comme sous-agent Codex](https://x.com/nauczymycieAI/status/2078181182701736132) (by [@nauczymycieAI](https://x.com/nauczymycieAI))

**Gardez l'orchestration dans Codex et déléguez le frontend à un sous-agent Kimi K3 OpenCode avec une limite claire pour les secrets**

nauczymycieAI décrit l'installation d'OpenCode, la création manuelle d'une clé Kimi sans la coller dans Codex, la connexion à Kimi K3 et un skill Codex global pour router les tâches frontend

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-75.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-75.jpg" alt="Case 75 source image 1" height="360"></a>

Type: Tutorial | Date: 2026-07-17

---

<a id="case-79"></a>
### Case 79: [Router le code simple via ChatLLM](https://x.com/abacusai/status/2078022418661257411) (by [@abacusai](https://x.com/abacusai))

**Envoyez le code simple à Kimi K3 et réservez le code difficile et le design à d'autres modèles**

Abacus AI annonce Kimi K3 dans ChatLLM : code simple avec Kimi K3, code difficile avec Fable 5, design avec GPT-5.6 Sol. Le routeur fonctionne dans ChatLLM, Abacus AI Agent et Claude Code

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-79.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-79.jpg" alt="Case 79 source image 1" height="360"></a>

Type: Integration | Date: 2026-07-17

---

<a id="case-91"></a>
### Case 91: [Créer CS avec des assets générés](https://x.com/karankendre/status/2078938615900688728) (by [@karankendre](https://x.com/karankendre))

**Associe Kimi K3 pour le code du jeu et GPT Image 2 pour les assets lors du prototypage d’un petit jeu navigateur façon Counter-Strike.**

Karan Kendre indique avoir utilisé Kimi K3 pour construire le jeu et GPT Image 2 pour produire les assets d’un projet façon Counter-Strike, pour environ 10 dollars au total. La vidéo source est l’artefact visible, donc ce cas documente surtout un workflow de combinaison d’outils.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-91.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-91-poster.jpg" alt="Case 91 source video poster" height="360"></a>

[Play case 91 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-91.mp4)

Type: Integration | Date: 2026-07-19

---

<a id="case-95"></a>
### Case 95: [Utiliser la skill Design de Command Code](https://x.com/MrAhmadAwais/status/2078841789205934547) (by [@MrAhmadAwais](https://x.com/MrAhmadAwais))

**Combine Kimi K3 avec une skill design dédiée dans Command Code pour créer un prototype visuel de jeu sous budget tokens.**

Ahmad Awais rapporte l’usage de Kimi K3 avec Command Code et la skill /design pour un jeu à caméra poursuite façon Forza. Le post cite un coût de session de 0,97 dollar et des corrections d’échelle route/voiture, fond, animation et brouillard, ce qui en fait un workflow agent concret.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-95.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-95-poster.jpg" alt="Case 95 source video poster" height="360"></a>

[Play case 95 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-95.mp4)

Type: Integration | Date: 2026-07-19

---

<a id="case-109"></a>
### Case 109: [Exécuter Kimi K3 dans Claude Code](https://x.com/boxmining/status/2079115758618239337) (by [@boxmining](https://x.com/boxmining))

**Utilisez ce cas pour évaluer le workflow réel, le coût ou les limites de Kimi K3 sur « Exécuter Kimi K3 dans Claude Code ».**

Le post source fournit une preuve publique sur « Exécuter Kimi K3 dans Claude Code », avec description de l’auteur, média du résultat ou informations de benchmark/tutoriel. Le dépôt conserve seulement les faits vérifiables et ne reconstruit pas les prompts ou étapes non publiés.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-109.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-109-poster.jpg" alt="Case 109 source video poster" height="360"></a>

[Play case 109 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-109.mp4)

Type: Integration | Date: 2026-07-20

---

<a id="case-119"></a>
### Case 119: [Router Kimi via claude-code-router](https://x.com/sairahul1/status/2079393675885588855) (by [@sairahul1](https://x.com/sairahul1))

**Teste Kimi K3 dans un workflow Claude Code existant via claude-code-router en évitant le mode proxy inutile.**

Sai Rahul décrit le support Kimi K3 sponsorisé par Moonshot dans claude-code-router, avec presets, import de clé API ou abonnement, routage natif, dashboard solde/usage, failover, prix cache et conseil de laisser le proxy mode désactivé sauf besoin.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-119.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-119-poster.jpg" alt="Case 119 source video poster" height="360"></a>

[Play case 119 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-119.mp4)

Type: Integration | Date: 2026-07-21

---

<a id="case-125"></a>
### Case 125: [Exécuter un harness d'agents ouvert](https://x.com/ShenSeanChen/status/2079914609222221976) (by [@ShenSeanChen](https://x.com/ShenSeanChen))

**Utilise un harness partagé pour comparer Kimi K3 à d’autres modèles frontier sur des tâches avec outils.**

Sean Chen décrit un harness open source avec boucle agent, récupération mémoire, appels d’outils, évaluation, traces et tableau de coûts pour faire concourir Kimi K3 avec plusieurs modèles.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-125.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-125-poster.jpg" alt="Case 125 source video poster" height="360"></a>

[Play case 125 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-125.mp4)

Type: Benchmark | Date: 2026-07-22

---

<a id="case-129"></a>
### Case 129: [Exécuter Kimi via Codex OAuth](https://x.com/biscuitweb3/status/2079844959843197342) (by [@biscuitweb3](https://x.com/biscuitweb3))

**Utilise la route OAuth de Codex quand un workflow de code Kimi K3 doit éviter la configuration manuelle d’une clé API.**

biscuitweb3 rapporte que Kimi K3 fonctionne dans Codex via OAuth sans configuration API key supplémentaire. La capture jointe fournit la preuve d’intégration.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-129-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-129-01.jpg" alt="Case 129 source image 1" height="360"></a>

Type: Integration | Date: 2026-07-22

---


<a id="evaluation-limits"></a>
## 🧪 Évaluation et limites

<a id="case-7"></a>
### Case 7: [Comparer le design frontend sur la tâche de lampe à lave BridgeBench](https://x.com/bridgemindai/status/2077868061953007908) (by [@bridgemindai](https://x.com/bridgemindai))

**Utilisez la tâche de lampe à lave BridgeBench comme une comparaison limitée de conception frontale plutôt qu'un classement universel.**

BridgeMind AI rapporte que Kimi K3 a surpassé Fable 5 sur sa tâche de lampe à lave BridgeBench et s'est classé premier dans l'arène citée. Voici les résultats de comparaison rapportés par l'éditeur.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-07.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-07-poster.jpg" alt="Case 7 source video poster" height="360"></a>

[Play case 7 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-07.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-8"></a>
### Case 8: [Évaluer l’écriture de scripts dans une voix éditoriale](https://x.com/Whats_AI/status/2077860441380798908) (by [@Whats_AI](https://x.com/Whats_AI))

**Mesurez l'adéquation de la voix éditoriale, le classement relatif et le coût par script au sein d'un benchmark interne clairement identifié.**

Whats_AI rapporte des résultats internes préliminaires de 2 840 Elo, la première place de son propre classement et un coût d’environ 0,25 $ par script. Il s’agit du benchmark préliminaire d’une organisation, et non d’une garantie générale de performance ou de prix.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-08-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-08-01.jpg" alt="Case 8 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-16

---

<a id="case-10"></a>
### Case 10: [Comparez la conception, le coût et la difficulté du jeu Flappy](https://x.com/MrAhmadAwais/status/2077915347974557862) (by [@MrAhmadAwais](https://x.com/MrAhmadAwais))

**Enregistrez les paramètres de difficulté, le coût, la conception et les fonctionnalités de jeu lors de la comparaison des jeux générés.**

Le benchmark Flappy interne de Command Code rapporte différents paramètres de difficulté entre les modèles et répertorie Kimi K3 à 0,024 $, Fable 5 à 0,42 $ et GPT-5.6 Sol à 0,15 $. Les paramètres inégaux en font une comparaison interne limitée.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-10.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-10-poster.jpg" alt="Case 10 source video poster" height="360"></a>

[Play case 10 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-10.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-12"></a>
### Case 12: [Comparez la conception du jeu avec la même invite de conception](https://x.com/CommandCodeAI/status/2077921526213746948) (by [@CommandCodeAI](https://x.com/CommandCodeAI))

**Maintenez l'invite de conception constante et inspectez séparément le rythme, le sens de la conception et la sensation du gameplay.**

Le code de commande rapporte une comparaison de la même invite de Kimi K3, GPT-5.6 Sol et Fable 5. Son message indique que Kimi K3 a bien performé en termes de sens du design tandis que les deux autres ont joué trop vite ; cela reste l'évaluation de l'éditeur.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-12.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-12-poster.jpg" alt="Case 12 source video poster" height="360"></a>

[Play case 12 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-12.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-13"></a>
### Case 13: [Exiger un examen indépendant pour l'audit statistique](https://x.com/emollick/status/2077869293031624793) (by [@emollick](https://x.com/emollick))

**Associer les audits statistiques générés par un modèle avec un expert indépendant ou un examen du modèle avant de s'appuyer sur les résultats.**

Ethan Mollick rapporte que Kimi K3 Max a mal appliqué les statistiques lors de l'audit de travaux universitaires antérieurs et est d'accord avec une critique distincte. Cet exemple négatif prend en charge une vérification indépendante plutôt qu'une acceptation non vérifiée.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-13-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-13-01.jpg" alt="Case 13 source image 1" height="360"></a>

Type: Limit | Date: 2026-07-16

---

<a id="case-16"></a>
### Case 16: [Évaluer une exécution frontale lente mais forte](https://x.com/Lentils80/status/2077387333154857151) (by [@Lentils80](https://x.com/Lentils80))

**Enregistrer le temps d'achèvement ainsi que la qualité de sortie lors du test d'une tâche frontale.**

Le créateur rapporte qu'une exécution frontale Kimi K3 a pris 35 minutes et décrit la sortie comme l'une des meilleures vues pour cette invite. Les jugements de vitesse et de qualité sont l'observation d'un seul utilisateur.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-16.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-16-poster.jpg" alt="Case 16 source video poster" height="360"></a>

[Play case 16 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-16.mp4)

Type: Evaluation | Date: 2026-07-15

---

<a id="case-20"></a>
### Case 20: [Tester les défauts de préfiguration dans l’écriture d’un roman policier](https://x.com/emollick/status/2077951790868238616) (by [@emollick](https://x.com/emollick))

**Évaluer si un mystère généré équilibre les indices, l'obscurité et la préfiguration.**

Ethan Mollick rapporte que Kimi K3 n'a pas écrit un bon meurtre mystère, rendant les indices à la fois trop évidents et trop obscurs et échouant à préfiguration. Il note également que d'autres modèles partagent cette limitation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-01.jpg" alt="Case 20 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-02.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-02.png" alt="Case 20 source image 2" height="360"></a>

Type: Limit | Date: 2026-07-17

---

<a id="case-21"></a>
### Case 21: [Comparez la modélisation et l'animation du Millennium Falcon](https://x.com/gmi_cloud/status/2077903360263676090) (by [@gmi_cloud](https://x.com/gmi_cloud))

**Utilisez des demandes de style et des paramètres d'effort correspondants pour comparer la modélisation 3D, l'animation, le temps et le coût.**

GMI Cloud rapporte avoir comparé Kimi K3 et Fable 5 sur des recréations du Millennium Falcon en style pixel et en style original, avec un effort maximal. Le fournisseur indique que Kimi K3 a pris plus de temps, mais a coûté environ un tiers du prix lors du premier test et moins de la moitié lors d’un autre.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-21.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-21-poster.jpg" alt="Case 21 source video poster" height="360"></a>

[Play case 21 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-21.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-28"></a>
### Case 28: [Examiner une collection de dix projets Kimi K3](https://x.com/minchoi/status/2077957907857994006) (by [@minchoi](https://x.com/minchoi))

**Utiliser un récapitulatif de projets liés pour découvrir des artefacts concrets pour une vérification séparée.**

L'auteur organise dix exemples de Kimi K3 avec des médias, y compris un émulateur Game Boy Advance. Cet enregistrement est une collection plutôt qu'un seul flux de travail reproductible, donc chaque exemple lié doit être vérifié indépendamment.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-28.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-28-poster.jpg" alt="Case 28 source video poster" height="360"></a>

[Play case 28 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-28.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-29"></a>
### Case 29: [Comparez une page de destination avancée sur quatre modèles](https://x.com/doutorcaleb/status/2077904020471947773) (by [@doutorcaleb](https://x.com/doutorcaleb))

**Maintenez une demande de page de destination constante et inspectez la profondeur et l'achèvement de l'animation dans les sorties du modèle.**

Le créateur rapporte avoir donné la même invite de page de destination avancée à Kimi K3, Fable, Grok et GPT Terra, et juge Kimi K3 le plus puissant. résultat. Il s'agit d'une comparaison autodéclarée à partir d'une tâche.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-29.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-29-poster.jpg" alt="Case 29 source video poster" height="360"></a>

[Play case 29 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-29.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-30"></a>
### Case 30: [Évaluer les mécaniques et le coût de jeux rétro](https://x.com/adxtyahq/status/2077860500462055570) (by [@adxtyahq](https://x.com/adxtyahq))

**Comparez le gameplay, la physique, la mécanique, le comportement autonome, l'utilisation des jetons et le coût sur les mêmes tâches de rétro-jeu.**

La source rapporte des tests identiques pour Road Fighter, Battle City et Q*bert et indique 0,28 $ pour Kimi K3, 0,28 $ pour GPT-5.6 et 0,54 $ pour Opus 4.8. Ce sont les chiffres de référence de l'éditeur.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-30.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-30-poster.jpg" alt="Case 30 source video poster" height="360"></a>

[Play case 30 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-30.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-31"></a>
### Case 31: [Comparez la génération de jeux avec Fable 5](https://x.com/higgsfield_ai/status/2077943629633712490) (by [@higgsfield_ai](https://x.com/higgsfield_ai))

**Utilisez un exemple de jeu généré côte à côte comme une évaluation étroite plutôt qu'un verdict de modèle large.**

Higgsfield présente une comparaison de la génération de jeux Kimi K3 par rapport à Fable 5. Le dossier fourni comprend le support de comparaison mais aucune invite, rubrique de notation ou conditions détaillées.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-31.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-31-poster.jpg" alt="Case 31 source video poster" height="360"></a>

[Play case 31 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-31.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-34"></a>
### Case 34: [Comparer des tâches complexes de frontend et de développement avec Opus 4.8](https://x.com/op7418/status/2077969583018066116) (by [@op7418](https://x.com/op7418))

**Utilisez plusieurs tâches de codage complexes pour identifier les victoires et les pertes au lieu de déclarer un modèle universellement supérieur.**

Le critique rapporte les tests directs de Kimi K3 par rapport à l'Opus 4.8 et les juge à peu près comparables sur des travaux d'interface et de développement complexes, avec des résultats mitigés. Cela reste l'évaluation d'un évaluateur.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-34.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-34-poster.jpg" alt="Case 34 source video poster" height="360"></a>

[Play case 34 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-34.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-35"></a>
### Case 35: [Examiner des benchmarks et un test de landing page](https://x.com/adamuchigabriel/status/2077880433925120471) (by [@adamuchigabriel](https://x.com/adamuchigabriel))

**Combinez le contexte de référence avec un test concret de génération de page de destination tout en gardant les deux types de preuves séparés.**

La vidéo présente une discussion de référence, un test de page de destination et des observations de conception frontale pour Kimi K3. L'enregistrement fourni ne fournit pas l'invite de test complète ni la rubrique de notation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-35.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-35-poster.jpg" alt="Case 35 source video poster" height="360"></a>

[Play case 35 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-35.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-37"></a>
### Case 37: [Évaluer le raisonnement inductif avec des tâches graphe-vers-formule](https://x.com/s_batzoglou/status/2077884096307454119) (by [@s_batzoglou](https://x.com/s_batzoglou))

**Mesurer l'exactitude, le comportement de rétention et la complexité des formules sur les tâches d'induction de premier ordre.**

L'auteur rapporte une analyse comparative de Kimi K3 et d'autres modèles sur la tâche ICML INDUCTION en utilisant 6 à 10 petits graphiques de 8 à 10 éléments chacun pour déduire une formule de premier ordre. Le message indique que les résultats ont été mis à jour à partir de travaux antérieurs ; aucune nouvelle reproduction indépendante n'est revendiquée ici.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-37-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-37-01.png" alt="Case 37 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-16

---

<a id="case-38"></a>
### Case 38: [Examiner les jeux, landing pages, travaux 3D et contextes étendus rapportés](https://x.com/servasyy_ai/status/2077903775113834689) (by [@servasyy_ai](https://x.com/servasyy_ai))

**Utilisez un résumé multi-sources pour comparer les artefacts concrets et notez les limitations de vitesse ainsi que les réclamations de coûts.**

L'auteur résume les tests rapportés de Kimi K3 sur les jeux, les pages de destination, la génération 3D et le travail en contexte long, tout en concluant que cela vaut la peine d'essayer mais pas encore un remplacement pour Fable 5. Toutes les figures sont des rapports secondaires dans ce résumé.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-38-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-38-01.jpg" alt="Case 38 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-40"></a>
### Case 40: [Auditer un plan complexe et contester ses remèdes](https://x.com/doodlestein/status/2077901883637665958) (by [@doodlestein](https://x.com/doodlestein))

**Utiliser un deuxième modèle pour identifier les résultats sous-estimés, les remèdes incorrects et les conclusions qui devraient être rejetées.**

Le créateur rapporte que Kimi K3 a examiné un plan fortement affiné et a constaté que les problèmes graves étaient sous-estimés, environ un tiers des remèdes proposés devaient être corrigés et une conclusion a été réfutée. Ce sont les résultats de cet audit spécifique.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-40-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-40-01.jpg" alt="Case 40 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-41"></a>
### Case 41: [Comparez les diagrammes ASCII d'apprentissage par renforcement de style PPO](https://x.com/dejavucoder/status/2077872015856615541) (by [@dejavucoder](https://x.com/dejavucoder))

**Maintenez une invite de diagramme ASCII constante et comparez la façon dont les modèles représentent la boucle d'apprentissage par renforcement.**

La source fournit l'invite pour dessiner une boucle d'apprentissage par renforcement de style PPO en ASCII et montre Kimi K3 Max à côté de Fable 5 High. Le jugement reste une comparaison visuelle d'une tâche.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-01.png" alt="Case 41 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-02.jpg" alt="Case 41 source image 2" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-42"></a>
### Case 42: [Modéliser dans Blender tout en suivant les erreurs de capacité](https://x.com/Angaisb_/status/2077910845523214668) (by [@Angaisb_](https://x.com/Angaisb_))

**Évaluez la progression partielle de Blender ainsi que la fiabilité du service plutôt que de juger uniquement l'artefact.**

Le créateur montre la progression de la modélisation de Blender à partir de Kimi K3 et signale également des erreurs de capacité répétées. Le travail est incomplet dans la source fournie, donc le résultat partiel et la limitation de fiabilité doivent être considérés ensemble.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-42-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-42-01.jpg" alt="Case 42 source image 1" height="360"></a>

Type: Limit | Date: 2026-07-17

---

<a id="case-47"></a>
### Case 47: [Comparer la génération Flappy Bird dans une arène](https://x.com/jun_song/status/2077396996865003739) (by [@jun_song](https://x.com/jun_song))

**Utilisez une tâche d'arène pour comparer deux résultats Flappy Bird générés tout en gardant la tâche de jugement spécifique.**

Le créateur rapporte une comparaison d'arène entre Kimi K3 et Opus 4.8 sur une tâche Flappy Bird et juge Kimi K3 nettement mieux. Aucune invite ou rubrique complète n'est fournie dans le dossier.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-47.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-47-poster.jpg" alt="Case 47 source video poster" height="360"></a>

[Play case 47 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-47.mp4)

Type: Evaluation | Date: 2026-07-15

---

<a id="case-52"></a>
### Case 52: [Résoudre un problème d'induction visuelle Bongard avec un outil](https://x.com/IntuitMachine/status/2077885406528311561) (by [@IntuitMachine](https://x.com/IntuitMachine))

**Tester si l'utilisation d'un outil aide à dériver la règle visuelle dans une tâche de raisonnement Bongard.**

Le créateur rapporte que Kimi K3 a utilisé un outil pour résoudre un problème Bongard que Grok 4.5 et Muse Spark 1.1 n'ont pas résolu dans la même comparaison. Il s'agit du résultat d'une tâche d'un utilisateur, et non d'une référence de raisonnement général.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-52-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-52-01.jpg" alt="Case 52 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-53"></a>
### Case 53: [Comparer la qualité visuelle du frontend et le design 3D avec GPT-5.6 Sol](https://x.com/filicroval/status/2077736407506751952) (by [@filicroval](https://x.com/filicroval))

**Inspectez les fonctionnalités, le goût visuel, l'élégance et l'exécution 3D dans une comparaison frontale limitée.**

Le créateur compare Kimi K3 et GPT-5.6 Sol sur la conception du frontend et juge Kimi K3 plus fort en termes de goût visuel, d'élégance et Capacité 3D. L'évaluation est subjective et spécifique à la tâche.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-53.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-53-poster.jpg" alt="Case 53 source video poster" height="360"></a>

[Play case 53 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-53.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-57"></a>
### Case 57: [Comparez la génération de sites Web sur trois modèles](https://x.com/pengchujin/status/2077962916226298340) (by [@pengchujin](https://x.com/pengchujin))

**Utilisez les sorties de sites Web visibles pour comparer Kimi K3, Fable 5 et GPT-5.6 Sol sur un seul test.**

Le créateur présente une comparaison de génération de sites Web entre Kimi K3, Fable 5 et GPT-5.6 Sol. L'enregistrement fourni n'expose pas l'invite complète ni une grille de notation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-57.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-57-poster.jpg" alt="Case 57 source video poster" height="360"></a>

[Play case 57 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-57.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-59"></a>
### Case 59: [Comparez la génération et le coût des jeux 3D procéduraux](https://x.com/adxtyahq/status/2077958193511362856) (by [@adxtyahq](https://x.com/adxtyahq))

**Maintenez une invite constante entre les modèles et inspectez les systèmes de roulette, de machine à sous et de flipper générés avec le coût par exécution.**

L'éditeur rapporte une comparaison de jeux 3D procéduraux multimodèles et répertorie les coûts, y compris 0,71 $ pour Kimi K3 et 0,30 $ pour Grok 4.5. Traitez tous les classements et les coûts comme les résultats de l'exécution de cet éditeur.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-59.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-59-poster.jpg" alt="Case 59 source video poster" height="360"></a>

[Play case 59 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-59.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-69"></a>
### Case 69: [Comparez les détails et l'éclairage de la scène d'arsenal 3D](https://x.com/hakki_alkan/status/2077887013332636032) (by [@hakki_alkan](https://x.com/hakki_alkan))

**Inspectez la densité des objets, l'éclairage et les détails de la scène dans une comparaison limitée entre Kimi K3 et Opus 4.8.**

La source rapporte que Kimi K3 a produit une scène d’arsenal détaillée avec des étagères remplies, des boîtes et un éclairage réaliste, tandis qu’Opus 4.8 a produit une pièce peu meublée. Il s’agit d’un rapport de comparaison tiers, et non d’un benchmark indépendant.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-69-poster.jpg" alt="Case 69 source video poster" height="360"></a>

[Play case 69 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-69.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-72"></a>
### Case 72: [Comparer des frontends avec des invites Arena identiques](https://x.com/arena/status/2078240399517524365) (by [@arena](https://x.com/arena))

**Utilisez des invites identiques et des sorties côte à côte plutôt qu'un seul rang**

Arena.ai publie une comparaison Frontend Code Arena de Kimi K3 et Fable 5 avec des invites identiques. La vidéo conserve les deux sorties dans les mêmes conditions

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-72.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-72-poster.jpg" alt="Case 72 source video poster" height="360"></a>

[Play case 72 comparison video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-72.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-74"></a>
### Case 74: [Évaluer Kimi Code sur des agents de code](https://x.com/ArtificialAnlys/status/2078230240766345330) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Évaluez Kimi K3 sur plusieurs suites et le coût par tâche sans généraliser un classement frontend**

Artificial Analysis rapporte 57 points et une cinquième place ex aequo : 84 % sur Terminal-Bench v2, 64 % sur DeepSWE, 23 % sur SWE-Atlas-QnA et 3,18 dollars en moyenne par tâche

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-74.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-74.jpg" alt="Case 74 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-17

---

<a id="case-76"></a>
### Case 76: [Comparer Arena et le banc de réparation](https://x.com/AlphaSignalAI/status/2078172629496746183) (by [@AlphaSignalAI](https://x.com/AlphaSignalAI))

**Examinez préférence frontend et réparation de dépôt car Kimi K3 peut être premier dans l'une et septième dans l'autre**

AlphaSignal rapporte la première place avec 1 679 points dans Frontend Code Arena, mais 53 réussites sur 67, soit 79 %, et la septième place dans un banc de réparation d'agents

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-76.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-76.jpg" alt="Case 76 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-17

---

<a id="case-80"></a>
### Case 80: [Évaluer Kimi K3 avec Prinzbench](https://x.com/deredleritt3r/status/2078606700496773166) (by [@deredleritt3r](https://x.com/deredleritt3r))

**Prinzbench compare Kimi K3 à OpenAI o3 et à d’autres modèles, avec un classement et des limites sur le même banc d’essai.**

Le post place Kimi K3 dans un tableau Prinzbench et rend visibles son écart avec les meilleurs modèles ainsi que ses forces relatives sur des tâches d’évaluation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-80-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-80-01.png" alt="Case 80 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-18

---

<a id="case-85"></a>
### Case 85: [Comparer la génération d’un jumeau numérique de l’ISS](https://x.com/AIsaOneHQ/status/2078519527588200536) (by [@AIsaOneHQ](https://x.com/AIsaOneHQ))

**Kimi K3 est comparé à d’autres modèles sur un jumeau numérique de l’ISS, révélant des écarts en visualisation 3D complexe.**

Le post compare plusieurs sorties sur la même tâche ISS et aide à juger la compréhension structurelle et les limites visuelles de Kimi K3.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-85.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-85-poster.jpg" alt="Case 85 source video poster" height="360"></a>

[Play case 85 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-85.mp4)

Type: Benchmark | Date: 2026-07-18

---

<a id="case-89"></a>
### Case 89: [Évaluer une forêt WebGPU](https://x.com/stas_sorokin_/status/2078435840728908093) (by [@stas_sorokin_](https://x.com/stas_sorokin_))

**Une scène de forêt WebGPU créée avec Kimi K3 est évaluée pour sa qualité immersive et ses limites 3D.**

La vidéo présente un environnement forestier dans le navigateur et sert d’évidence pour les capacités WebGPU/3D de Kimi K3.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-89.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-89-poster.jpg" alt="Case 89 source video poster" height="360"></a>

[Play case 89 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-89.mp4)

Type: Evaluation | Date: 2026-07-18

---

<a id="case-90"></a>
### Case 90: [Comparer des prompts de maison vitrée](https://x.com/RoundtableSpace/status/2079004612070416755) (by [@RoundtableSpace](https://x.com/RoundtableSpace))

**Utilise la même scène architecturale pour comparer Kimi K3 et Opus 4.8 sur l’atmosphère, la lumière et la complétude spatiale.**

Roundtable Space rapporte une comparaison à prompt identique entre Kimi K3 et Claude Opus 4.8 à prix proche. Le rendu de Kimi est décrit comme une maison vitrée à l’heure bleue avec lumière intérieure chaude, bassin réfléchissant et plans visibles, tandis qu’Opus paraît plus typographique et moins spatialement complet.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-90.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-90-poster.jpg" alt="Case 90 source video poster" height="360"></a>

[Play case 90 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-90.mp4)

Type: Evaluation | Date: 2026-07-20

---

<a id="case-92"></a>
### Case 92: [Benchmarker un but de football voxel](https://x.com/0xzynex/status/2078920667542487230) (by [@0xzynex](https://x.com/0xzynex))

**Lance le même prompt d’animation football en HTML/CSS/JS pur sur deux modèles pour comparer mouvement et coût.**

0xzynex rapporte une comparaison en une seule passe, sans retry, où Kimi K3 et GPT-5.6 Sol High devaient créer une action de football en blocs avec dribble, but, caméra dynamique et célébration en code navigateur. Le post dit que Kimi a produit un mouvement plus fluide et un coût inférieur, avec vidéo comparative.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-92.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-92-poster.jpg" alt="Case 92 source video poster" height="360"></a>

[Play case 92 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-92.mp4)

Type: Benchmark | Date: 2026-07-19

---

<a id="case-93"></a>
### Case 93: [Examiner un benchmark Minecraft](https://x.com/ashen_one/status/2078892418976666071) (by [@ashen_one](https://x.com/ashen_one))

**Regarde une revue Minecraft structurée avant de prendre le battage de lancement ou le prix comme preuve suffisante.**

ashen_one publie une revue vidéo de Kimi K3 avec chapitres sur hype contre réalité, benchmarks, prix, test Minecraft, bugs de première exécution et verdict final. La source est utile car elle combine cadrage benchmark et premières notes de fiabilité dans une vidéo inspectable.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-93.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-93-poster.jpg" alt="Case 93 source video poster" height="360"></a>

[Play case 93 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-93.mp4)

Type: Benchmark | Date: 2026-07-19

---

<a id="case-98"></a>
### Case 98: [Mesurer les limites de niveau API](https://x.com/mnmn94253156337/status/2078739859154620497) (by [@mnmn94253156337](https://x.com/mnmn94253156337))

**Planifie les runs agents Kimi K3 selon tokens, niveau, TPM et TPD, pas seulement selon le prix affiché du modèle.**

La source en chinois relate un essai personnel de l’API Kimi K3 après 5 dollars de crédit, environ 1,1 dollar consommé pendant la configuration, puis des limites Tier0. Elle liste prix d’entrée, entrée cachée et sortie ainsi que TPM/TPD, utile comme rapport de limitation précoce.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-98.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-98-poster.jpg" alt="Case 98 source video poster" height="360"></a>

[Play case 98 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-98.mp4)

Type: Limit | Date: 2026-07-19

---

<a id="case-99"></a>
### Case 99: [Comparer une démo façon Limbo](https://x.com/ChrisGPT/status/2078679211116835017) (by [@ChrisGPT](https://x.com/ChrisGPT))

**Compare portée jouable, finition, coût et bugs en testant Kimi K3 contre Fable 5 sur le même prototype de jeu.**

ChrisGPT compare Fable 5 et Kimi K3 sur une démo clone de Limbo. Le post donne 2 400 lignes et 24K tokens de sortie pour 1,20 dollar côté Fable, contre 3 000 lignes et 30K tokens pour 0,12 dollar côté Kimi, avec plus de gameplay mais aussi plus de bugs.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-99.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-99-poster.jpg" alt="Case 99 source video poster" height="360"></a>

[Play case 99 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-99.mp4)

Type: Benchmark | Date: 2026-07-19

---

<a id="case-100"></a>
### Case 100: [Examiner les coûts VulcanBench](https://x.com/morganlinton/status/2079358902194569357) (by [@morganlinton](https://x.com/morganlinton))

**Utilisez ce cas pour évaluer le workflow réel, le coût ou les limites de Kimi K3 sur « Examiner les coûts VulcanBench ».**

Le post source fournit une preuve publique sur « Examiner les coûts VulcanBench », avec description de l’auteur, média du résultat ou informations de benchmark/tutoriel. Le dépôt conserve seulement les faits vérifiables et ne reconstruit pas les prompts ou étapes non publiés.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-100-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-100-01.jpg" alt="Case 100 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-21

---

<a id="case-104"></a>
### Case 104: [Évaluer la physique du double pendule](https://x.com/AlicanKiraz0/status/2079241239736504768) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**Utilisez ce cas pour évaluer le workflow réel, le coût ou les limites de Kimi K3 sur « Évaluer la physique du double pendule ».**

Le post source fournit une preuve publique sur « Évaluer la physique du double pendule », avec description de l’auteur, média du résultat ou informations de benchmark/tutoriel. Le dépôt conserve seulement les faits vérifiables et ne reconstruit pas les prompts ou étapes non publiés.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-104.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-104-poster.jpg" alt="Case 104 source video poster" height="360"></a>

[Play case 104 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-104.mp4)

Type: Benchmark | Date: 2026-07-20

---

<a id="case-107"></a>
### Case 107: [Examiner la maturité ReactBench](https://x.com/aidenybai/status/2079233934693650567) (by [@aidenybai](https://x.com/aidenybai))

**Utilisez ce cas pour évaluer le workflow réel, le coût ou les limites de Kimi K3 sur « Examiner la maturité ReactBench ».**

Le post source fournit une preuve publique sur « Examiner la maturité ReactBench », avec description de l’auteur, média du résultat ou informations de benchmark/tutoriel. Le dépôt conserve seulement les faits vérifiables et ne reconstruit pas les prompts ou étapes non publiés.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-107.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-107-poster.jpg" alt="Case 107 source video poster" height="360"></a>

[Play case 107 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-107.mp4)

Type: Benchmark | Date: 2026-07-20

---

<a id="case-110"></a>
### Case 110: [Évaluer Kimi K3 sur AA-Briefcase](https://x.com/ArtificialAnlys/status/2079715807983210572) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Utilise les résultats AA-Briefcase pour juger Kimi K3 sur des tâches agentiques de knowledge work avant de croire un leaderboard.**

Artificial Analysis indique que Kimi K3 atteint 1543 Elo sur AA-Briefcase, deuxième derrière Claude Fable 5, tout en signalant presque une heure par tâche et un coût supérieur à Opus 4.8 dans ce benchmark.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-110-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-110-01.jpg" alt="Case 110 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-21

---

<a id="case-113"></a>
### Case 113: [Auditer les limites du leaderboard frontend](https://x.com/RetroChainer/status/2079622227796885850) (by [@RetroChainer](https://x.com/RetroChainer))

**Utilise cette note de limite pour séparer les victoires leaderboard de Kimi K3 des affirmations générales sur le coding et le coût.**

RetroChainer vérifie la première place Frontend Code Arena et les prix listés, puis note que le rang est propre à ce tableau, que les poids n’étaient pas encore publics, que les économies par tâche viennent d’un seul test et que le raisonnement max peut brûler des tokens sur de petites tâches.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-113.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-113-poster.jpg" alt="Case 113 source video poster" height="360"></a>

[Play case 113 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-113.mp4)

Type: Limit | Date: 2026-07-21

---

<a id="case-114"></a>
### Case 114: [Comparer les résultats StackPerf architecture](https://x.com/tamsi_besson/status/2079573266855834071) (by [@tamsi_besson](https://x.com/tamsi_besson))

**Utilise StackPerf pour comparer Kimi K3 et Qwen 3.8 sur qualité d’architecture, vitesse et tool calls.**

Tamsi Besson partage un snapshot StackPerf où Kimi K3 devance légèrement Qwen 3.8 Max Preview en qualité et va plus vite au total, tandis que Qwen affiche zéro tool call échoué contre deux pour Kimi malgré plus d’appels.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-114-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-114-01.jpg" alt="Case 114 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-21

---

<a id="case-118"></a>
### Case 118: [Comparer les coûts Monument Valley](https://x.com/AiHubMix/status/2079507420083294557) (by [@AiHubMix](https://x.com/AiHubMix))

**Utilise un seul prompt style Monument Valley pour comparer qualité visuelle, temps et coût entre Kimi K3 et ses pairs.**

AiHubMix compare Claude Fable 5, Kimi K3 et GPT-5.6 Sol sur un prompt style Monument Valley. Le post décrit Fable comme le plus cohérent, Kimi comme le plus lent à 52m30s et $1.50, et GPT-5.6 Sol comme le plus rapide et moins cher mais moins bon en logique spatiale.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-118.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-118-poster.jpg" alt="Case 118 source video poster" height="360"></a>

[Play case 118 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-118.mp4)

Type: Benchmark | Date: 2026-07-21

---

<a id="case-120"></a>
### Case 120: [Évaluer Kimi K3 avec l'indice Surge](https://x.com/echen/status/2080021575190110523) (by [@echen](https://x.com/echen))

**Utilise les résultats séparés de SurgeAI pour distinguer la force de Kimi K3 en chat quotidien de ses limites en agents d’entreprise et en science.**

Eric Chen rapporte que SurgeAI a testé Kimi K3 sur un indice couvrant chatbots quotidiens, agents d’entreprise, raisonnement profond et science de pointe. Le post dit que Kimi K3 est compétitif en chat quotidien mais derrière Fable et Sol pour agents et science.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-120-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-120-01.jpg" alt="Case 120 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-22

---

<a id="case-123"></a>
### Case 123: [Comparer les erreurs de solveur PDE](https://x.com/lanyon_ai/status/2079931884511887740) (by [@lanyon_ai](https://x.com/lanyon_ai))

**Utilise les échecs de benchmark PDE pour décider où les tâches symboliques ou numériques demandent une vérification avec Kimi K3.**

Lanyon AI compare son architecture neurosymbolique à des modèles frontier, dont Kimi K3, sur des PDE linéaires simples. La source signale des erreurs mathématiques, algorithmiques et computationnelles même avec des prompts détaillés.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-123-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-123-01.jpg" alt="Case 123 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-22

---

<a id="case-124"></a>
### Case 124: [Examiner les cas EHR ClinicalBench](https://x.com/mkurman88/status/2079918374977413534) (by [@mkurman88](https://x.com/mkurman88))

**Utilise les cas EHR de ClinicalBench pour voir où Kimi K3 réussit et où le raisonnement diagnostique échoue encore.**

Michael Kurman rapporte les résultats ClinicalBench v0.0.4 de Kimi K3 dans un sandbox EHR virtuel avec 10 cas d’urgence. Kimi K3 en résout 7 sur 10 et bloque sur le sixième cas.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-124-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-124-01.jpg" alt="Case 124 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-124-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-124-02.jpg" alt="Case 124 source image 2" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-124-03.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-124-03.jpg" alt="Case 124 source image 3" height="360"></a>

Type: Benchmark | Date: 2026-07-22

---

<a id="case-126"></a>
### Case 126: [Évaluer les calculs fiscaux](https://x.com/michaelrbock/status/2079913117698666964) (by [@michaelrbock](https://x.com/michaelrbock))

**Teste Kimi K3 séparément sur les charges fiscales au lieu de supposer que la force frontend se transfère.**

Michael Bock rapporte un test sur 50 déclarations fiscales fédérales et d’État hyperréalistes. La source donne 6% à Kimi K3 sur TaxCalcBench, contre 58% pour GPT-5.6 Sol et 4% pour Fable 5.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-126-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-126-01.jpg" alt="Case 126 source image 1" height="360"></a>

Type: Limit | Date: 2026-07-22

---

<a id="related-resources"></a>
## Ressources associées

- [Voir les détails et tarifs de Kimi K3 sur EvoLink](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=landing_overview)
- [Ouvrir la documentation API Kimi K3 d’EvoLink](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=docs_link)
- [En savoir plus sur Kimi K3 sur EvoLink](https://evolink.ai/blog/is-kimi-k3-available-on-evolink?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_article)
- [KimiK3.io](https://kimik3.io/)
- La page du modèle et la documentation API EvoLink sont vérifiées; aucune skill Kimi K3 installable n’a été vérifiée

<a id="acknowledge"></a>
## 🙏 Remerciements

Merci aux personnes qui ont partagé publiquement leurs travaux avec Kimi K3

[@ivanfioravanti](https://x.com/ivanfioravanti), [@TheAhmadOsman](https://x.com/TheAhmadOsman), [@HarshithLucky3](https://x.com/HarshithLucky3), [@chetaslua](https://x.com/chetaslua), [@abhinavflac](https://x.com/abhinavflac), [@bridgemindai](https://x.com/bridgemindai), [@Whats_AI](https://x.com/Whats_AI), [@chongdashu](https://x.com/chongdashu), [@MrAhmadAwais](https://x.com/MrAhmadAwais), [@bijanbowen](https://x.com/bijanbowen), [@CommandCodeAI](https://x.com/CommandCodeAI), [@emollick](https://x.com/emollick), [@nicky_sap](https://x.com/nicky_sap), [@Lentils80](https://x.com/Lentils80), [@scottstts](https://x.com/scottstts), [@aisearchio](https://x.com/aisearchio), [@gmi_cloud](https://x.com/gmi_cloud), [@karminski3](https://x.com/karminski3), [@VORTEX_Promos](https://x.com/VORTEX_Promos), [@rohanpaul_ai](https://x.com/rohanpaul_ai), [@mirochill](https://x.com/mirochill), [@aimlapi](https://x.com/aimlapi), [@minchoi](https://x.com/minchoi), [@doutorcaleb](https://x.com/doutorcaleb), [@adxtyahq](https://x.com/adxtyahq), [@higgsfield_ai](https://x.com/higgsfield_ai), [@AlicanKiraz0](https://x.com/AlicanKiraz0), [@1littlecoder](https://x.com/1littlecoder), [@op7418](https://x.com/op7418), [@adamuchigabriel](https://x.com/adamuchigabriel), [@s_batzoglou](https://x.com/s_batzoglou), [@servasyy_ai](https://x.com/servasyy_ai), [@filicroval](https://x.com/filicroval), [@doodlestein](https://x.com/doodlestein), [@dejavucoder](https://x.com/dejavucoder), [@Angaisb_](https://x.com/Angaisb_), [@AngryTomtweets](https://x.com/AngryTomtweets), [@Alezander907](https://x.com/Alezander907), [@teortaxesTex](https://x.com/teortaxesTex), [@jun_song](https://x.com/jun_song), [@ridark_eth](https://x.com/ridark_eth), [@naymur_dev](https://x.com/naymur_dev), [@tphuang](https://x.com/tphuang), [@TokenGremlin](https://x.com/TokenGremlin), [@IntuitMachine](https://x.com/IntuitMachine), [@wangfeng0315](https://x.com/wangfeng0315), [@twid](https://x.com/twid), [@pengchujin](https://x.com/pengchujin), [@aayushman2703](https://x.com/aayushman2703), [@goncalo_canhoto](https://x.com/goncalo_canhoto), [@LinearUncle](https://x.com/LinearUncle), [@gagarot200](https://x.com/gagarot200), [@MinLiBuilds](https://x.com/MinLiBuilds), [@izutorishima](https://x.com/izutorishima), [@X2worldtech](https://x.com/X2worldtech), [@Satvik_Pen](https://x.com/Satvik_Pen), [@hakki_alkan](https://x.com/hakki_alkan), [@BrianMRey](https://x.com/BrianMRey), [@ChrisGPT](https://x.com/ChrisGPT), [@arena](https://x.com/arena), [@MathiasHeide](https://x.com/MathiasHeide), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@nauczymycieAI](https://x.com/nauczymycieAI), [@AlphaSignalAI](https://x.com/AlphaSignalAI), [@Ananth7e](https://x.com/Ananth7e), [@viktoroddy](https://x.com/viktoroddy), [@abacusai](https://x.com/abacusai), [@deredleritt3r](https://x.com/deredleritt3r), [@fabriciocarraro](https://x.com/fabriciocarraro), [@startracker](https://x.com/startracker), [@mattwatkajtys](https://x.com/mattwatkajtys), [@AIsaOneHQ](https://x.com/AIsaOneHQ), [@MiaAI_lab](https://x.com/MiaAI_lab), [@hqmank](https://x.com/hqmank), [@prasenx](https://x.com/prasenx), [@stas_sorokin_](https://x.com/stas_sorokin_), [@RoundtableSpace](https://x.com/RoundtableSpace), [@karankendre](https://x.com/karankendre), [@0xzynex](https://x.com/0xzynex), [@ashen_one](https://x.com/ashen_one), [@MAXdeg0](https://x.com/MAXdeg0), [@ice_bearcute](https://x.com/ice_bearcute), [@mnmn94253156337](https://x.com/mnmn94253156337), [@morganlinton](https://x.com/morganlinton), [@vikktorrrre](https://x.com/vikktorrrre), [@kirillk_web3](https://x.com/kirillk_web3), [@_guillecasaus](https://x.com/_guillecasaus), [@demian_ai](https://x.com/demian_ai), [@aidenybai](https://x.com/aidenybai), [@LexnLin](https://x.com/LexnLin), [@boxmining](https://x.com/boxmining), [@Nekt_0](https://x.com/Nekt_0), [@RetroChainer](https://x.com/RetroChainer), [@tamsi_besson](https://x.com/tamsi_besson), [@thehypedotnews](https://x.com/thehypedotnews), [@AiHubMix](https://x.com/AiHubMix), [@sairahul1](https://x.com/sairahul1), [@echen](https://x.com/echen), [@Oluwaphilemon1](https://x.com/Oluwaphilemon1), [@diegocabezas01](https://x.com/diegocabezas01), [@lanyon_ai](https://x.com/lanyon_ai), [@mkurman88](https://x.com/mkurman88), [@ShenSeanChen](https://x.com/ShenSeanChen), [@michaelrbock](https://x.com/michaelrbock), [@Kirratr](https://x.com/Kirratr), [@jadeferrara_](https://x.com/jadeferrara_), [@biscuitweb3](https://x.com/biscuitweb3)

*Pour corriger une attribution ou un texte, ouvrez une issue avec une source publique*
