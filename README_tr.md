<div align="center">

<a href="https://evolink.ai/kimi-k3?utm_source=github&utm_medium=banner&utm_campaign=awesome-kimi-k3-usecases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/images/tr-v2.png" alt="Ay manzarası ve EvoLink çağrısı içeren Türkçe Kimi K3 bannerı" width="760"></a>

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

# Harika Kimi K3 Kullanım Örnekleri

## 🍌 Giriş

Kimi K3 için yüksek sinyalli kullanım örnekleri deposuna hoş geldiniz

**Kamuya açık kaynaklara dayanan oyunları, 3D sahneleri, hareketli tasarımları, entegrasyonları, değerlendirmeleri ve pratik sınırları topluyoruz**

89 örneğin tamamı yüksek güvenli açık kaynaklara dayanır. Başlıklar ve yazarlar özgün kaynaklara bağlanır; zayıf, yinelenen ve yetersiz kanıtlı adaylar dışarıda bırakılır

## 📊 Genel bakış

- Geniş görev kapsamına sahip yüksek güvenli 89 örnek
- Oyunlar, 3D, frontend, hareketli grafikler, kodlama, araştırma, tasarım ve sınır değerlendirmesi
- Her örnek kaynak, yazar, tür, tarih ve prompt sınırını korur
- Orta güvenli 31 örnek dışarıda bırakıldı; tekil gözlemler benchmark olarak sunulmaz

> [!NOTE]
> Somut kanıt önceliklidir; eksik prompt veya kurulum adımları yeniden oluşturulmaz

<a id="quick-api-access"></a>
## ⚡ Hızlı başlangıç

EvoLink tarafından belgelenen model kimliği `kimi-k3`; model sayfası ve Chat Completions API belgeleri kullanılabilir

1. [EvoLink’te Kimi K3 ayrıntılarını ve fiyatlarını gör](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=landing_overview)
2. [EvoLink API anahtarı oluştur veya yönet](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-kimi-k3-usecases&utm_content=api_key)

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

[EvoLink Kimi K3 API belgelerini aç](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=first_run)

> [!IMPORTANT]
> EvoLink model sayfası ve API belgeleri genel rotayı ve kimliği doğrular. Bağımsız Kimi K3 tarayıcı veya kodsuz yüzeyi doğrulanmadı ve bu depo bağımsız ücretli API testi yaptığını iddia etmez

## 📑 Menü

| Section | Cases |
|---|---|
| [Etkileşimli oyunlar ve 3D](#games-3d) | 29 |
| [Frontend ve hareketli tasarım](#frontend-motion) | 22 |
| [Kodlama ve entegrasyonlar](#coding-integrations) | 12 |
| [Değerlendirme ve sınırlar](#evaluation-limits) | 36 |
| [İlgili kaynaklar](#related-resources) | İlgili kaynaklar |
| [Hızlı başlangıç](#quick-api-access) | Hızlı başlangıç |
| [Teşekkürler](#acknowledge) | Katkılar ve düzeltmeler |

| Case | Category | What it shows | Type |
|---|---|---|---|
| [Tek prompt ile voxel pod racer oluştur](#case-1) | Etkileşimli oyunlar ve 3D | Kısa bir fikirle yarış prototipi kur ve sonraki sürümü sınırla | Demo |
| [Frogger'ı aynı prompt ile karşılaştır](#case-2) | Etkileşimli oyunlar ve 3D | Model farklarını görmek için promptu sabit tut | Evaluation |
| [Frogger ve oynanış kaydını üret](#case-3) | Etkileşimli oyunlar ve 3D | Oyunu ve kayıt akışını ayrı tek geçişlerle dene | Demo |
| [Three.js ile uçak gemisi prototiple](#case-4) | Etkileşimli oyunlar ve 3D | Belirli bir kalkış ve dönüş sahnesiyle etkileşimli 3D'yi dene | Demo |
| [Etkileşimli motion frontend oluştur](#case-5) | Frontend ve hareketli tasarım | Duraklatıldığında da etkileşimli kalan grafikler üret | Demo |
| [Senkron hareketli reklam üret](#case-6) | Frontend ve hareketli tasarım | Müzik, efekt ve hareket senkronunu kontrol et | Demo |
| [BridgeBench lav lambası görevinde frontend tasarımını karşılaştır](#case-7) | Değerlendirme ve sınırlar | BridgeBench lav lambası görevini evrensel sıralama yerine sınırları belli tek bir frontend tasarım karşılaştırması olarak kullan | Benchmark |
| [Editoryal sesle senaryo yazımını ölç](#case-8) | Değerlendirme ve sınırlar | Açıkça tanımlanmış bir iç benchmark içinde editoryal sese uyumu, göreli sıralamayı ve senaryo başına maliyeti ölç | Benchmark |
| [Ajan araçlarıyla Paper Mario esintili bir oyun kur](#case-9) | Etkileşimli oyunlar ve 3D | Hem 2D hem de 3D oyun öğeleri üretmek için Kimi K3'ü bir ajan harness'ı ve varlık araçlarıyla birleştir | Demo |
| [Flappy türü oyunların tasarımını, maliyetini ve zorluğunu karşılaştır](#case-10) | Değerlendirme ve sınırlar | Üretilen oyunları karşılaştırırken zorluk ayarlarını, maliyeti, tasarımı ve oynanış özelliklerini kaydet | Benchmark |
| [Metroda geçen bir birinci şahıs nişancı oyunu üret](#case-11) | Etkileşimli oyunlar ve 3D | Üretilen birinci şahıs nişancı sonucunu incelemek için somut bir metro ortamı kullan | Demo |
| [Oyun tasarımını aynı tasarım promptuyla karşılaştır](#case-12) | Değerlendirme ve sınırlar | Tasarım promptunu sabit tut; tempo, tasarım anlayışı ve oynanış hissini ayrı ayrı incele | Benchmark |
| [İstatistiksel denetimde bağımsız inceleme şartı koy](#case-13) | Değerlendirme ve sınırlar | Bulgulara güvenmeden önce modelin istatistiksel denetimini bağımsız uzman veya başka bir model incelemesiyle eşleştir | Limit |
| [Hareketli tasarımı bütünüyle kodla oluştur](#case-14) | Frontend ve hareketli tasarım | Tek geçişli kodlama workflow'unun yardımcı üretim araçları olmadan hareketli tasarım üretip üretemediğini dene | Demo |
| [Bir kişiyi araştırıp animasyonlu kişisel site kur](#case-15) | Frontend ve hareketli tasarım | Geniş bir kişisel site brief'i ver; ardından modelin araştırma, planlama, yineleme ve tarayıcı doğrulamasını incele | Tutorial |
| [Yavaş ama güçlü bir frontend çalışmasını değerlendir](#case-16) | Değerlendirme ve sınırlar | Bir frontend görevini test ederken çıktı kalitesiyle birlikte tamamlanma süresini de kaydet | Evaluation |
| [Kara delik simülasyonu oluştur](#case-17) | Frontend ve hareketli tasarım | Üretilmiş bir kara delik simülasyonunu incelemek için bilimsel görselleştirme görevi kullan | Demo |
| [İşlevsel macOS içeren sanal MacBook kur](#case-18) | Kodlama ve entegrasyonlar | Three.js donanım render'ını etkileşimli bir tarayıcı işletim sistemi simülasyonuyla birleştir | Demo |
| [Blender MCP ile V8 motoru modelle](#case-19) | Etkileşimli oyunlar ve 3D | Ayrıntılı mekanik 3D model üretmek için Blender MCP ve tek bir istek kullan | Integration |
| [Polisiye yazımını önceden sezdirme hataları açısından dene](#case-20) | Değerlendirme ve sınırlar | Üretilen bir gizemin ipuçları, kapalılık ve önceden sezdirme arasında denge kurup kurmadığını değerlendir | Limit |
| [Millennium Falcon modelleme ve animasyonunu karşılaştır](#case-21) | Değerlendirme ve sınırlar | 3D modelleme, animasyon, süre ve maliyeti karşılaştırmak için eşleşen stil istekleri ve efor ayarları kullan | Benchmark |
| [Karmaşık frontend modelleme, parçacıklar ve shader'ları dene](#case-22) | Frontend ve hareketli tasarım | Tek geçişte modelleme hassasiyetini, parçacık efektlerini ve inline shader üretimini incelemek için açık bir frontend promptu kullan | Demo |
| [Tek referanstan oynanabilir savaş arenası kur](#case-23) | Etkileşimli oyunlar ve 3D | Eksiksiz oynanabilir bir arenanın tek geçişte üretimini denemek için tek referans kullan | Demo |
| [Üç kendi kendine oynayan retro oyunu HTML dosyaları olarak kur](#case-24) | Etkileşimli oyunlar ve 3D | Bağımsız HTML oyun dosyalarında grafik, düşman, kural ve özerk oynanış şartı koy | Benchmark |
| [DSL'den PTX'e GPU derleyicisi geliştir](#case-25) | Kodlama ve entegrasyonlar | DSL, compiler pass'leri, PTX üretimi ve Tensor Core yolunu kapsayan uçtan uca derleyici görevi kullan | Demo |
| [Tek denemede prosedürel müzik aracı üret](#case-26) | Frontend ve hareketli tasarım | Etkileşimli prosedürel müzik üretecinin tek geçişli üretimini dene ve görünür sonucu temkinli karşılaştır | Demo |
| [Tek geçişte bukalemun saklambaç oyunu kur](#case-27) | Etkileşimli oyunlar ve 3D | Renk eşleme, prosedürel bölgeler, ses ve çok turlu skor içeren tek dosyalı oyun üret | Benchmark |
| [On Kimi K3 projesinden oluşan koleksiyonu incele](#case-28) | Değerlendirme ve sınırlar | Ayrı ayrı doğrulanacak somut eserleri keşfetmek için bağlantılı proje derlemesini kullan | Evaluation |
| [Gelişmiş bir landing page'i dört modelde karşılaştır](#case-29) | Değerlendirme ve sınırlar | Landing page isteğini sabit tut; model çıktılarında animasyon derinliğini ve tamamlanmayı incele | Evaluation |
| [Retro oyun mekaniklerini ve maliyetini ölç](#case-30) | Değerlendirme ve sınırlar | Aynı retro oyun görevlerinde oynanış, fizik, mekanik, özerk davranış, token kullanımı ve maliyeti karşılaştır | Benchmark |
| [Oyun üretimini Fable 5 ile karşılaştır](#case-31) | Değerlendirme ve sınırlar | Yan yana üretilmiş oyun örneğini geniş model hükmü değil dar bir değerlendirme olarak kullan | Evaluation |
| [WebGL2'de gerçek zamanlı kara delik raytracer'ı kur](#case-32) | Kodlama ve entegrasyonlar | Tek HTML dosyasında yerel WebGL2 geodesic raytracer'ın tek promptla üretimini dene | Benchmark |
| [İki görselden Three.js ürün sayfası oluştur](#case-33) | Frontend ve hareketli tasarım | Ürün sunumu üretmek için iki referans görseli ve açık bir Three.js şartı kullan | Demo |
| [Karmaşık frontend ve geliştirme görevlerini Opus 4.8 ile karşılaştır](#case-34) | Değerlendirme ve sınırlar | Bir modeli evrensel olarak üstün ilan etmek yerine kazanım ve kayıpları görmek için birden çok karmaşık kodlama görevi kullan | Evaluation |
| [Benchmark'ları ve landing page testini incele](#case-35) | Değerlendirme ve sınırlar | İki kanıt türünü ayrı tutarak benchmark bağlamını somut landing page üretim testiyle birleştir | Evaluation |
| [Ajan araç zinciriyle Paper Mario benzeri 2.5D oyun kur](#case-36) | Etkileşimli oyunlar ve 3D | 2.5D oyun workflow'u oluşturmak için Kimi K3'ü Grok Build veya Claude Code ve Spriterrific ile kullan | Tutorial |
| [Grafikten formüle görevlerle tümevarım muhakemesini ölç](#case-37) | Değerlendirme ve sınırlar | Birinci dereceden tümevarım görevlerinde doğruluk, holdout davranışı ve formül karmaşıklığını ölç | Benchmark |
| [Bildirilen oyunları, landing page'leri, 3D işleri ve uzun bağlamı incele](#case-38) | Değerlendirme ve sınırlar | Somut eserleri karşılaştırmak ve hız sınırlarını maliyet iddialarıyla birlikte belirtmek için çok kaynaklı derleme kullan | Evaluation |
| [Lüks bir ekmek kesici ve ürün sayfası tasarla](#case-39) | Frontend ve hareketli tasarım | Ürün fikri, patlatılmış görünüm, gösterim ve landing page'i tek tasarım eserinde birleştir | Demo |
| [Karmaşık bir planı denetle ve çözümlerine itiraz et](#case-40) | Değerlendirme ve sınırlar | Hafife alınmış bulguları, yanlış çözümleri ve reddedilmesi gereken sonuçları bulmak için ikinci model kullan | Evaluation |
| [PPO tarzı reinforcement-learning ASCII diyagramlarını karşılaştır](#case-41) | Değerlendirme ve sınırlar | ASCII diyagram promptunu sabit tut ve modellerin reinforcement-learning döngüsünü nasıl temsil ettiğini karşılaştır | Evaluation |
| [Kapasite hatalarını izleyerek Blender'da modelle](#case-42) | Değerlendirme ve sınırlar | Yalnız eseri değil hizmet güvenilirliğini de değerlendirerek kısmi Blender ilerlemesini incele | Limit |
| [Tarayıcı tabanlı 3D wuxia RPG kur](#case-43) | Etkileşimli oyunlar ve 3D | Yakın dövüş, görevler, envanter, hava durumu, iç mekânlar, Blender ortam işi ve uyarlanmış varlıkları birleştir | Demo |
| [Tarayıcıda çok oyunculu Minecraft benzeri oyun kur](#case-44) | Etkileşimli oyunlar ve 3D | Süre ve maliyeti sınırlandırılmış bir çalışmada oynanabilir çevrimiçi çok oyunculu tarayıcı oyunu üret | Demo |
| [On saniyelik özyinelemeli pelikan GIF'i üret](#case-45) | Frontend ve hareketli tasarım | GIF'te anlatı sürekliliği ve özyinelemeyi incelemek için tamamen belirtilmiş döngülü animasyon brief'i kullan | Demo |
| [mGBA WASM çevresinde Game Boy Advance emülatörü kur](#case-46) | Kodlama ve entegrasyonlar | Lisanslı 3D model ve gerçek emülatör çekirdeğini birleştir; ardından arayüz ve oynanışı özyinelemeli olarak geliştir | Integration |
| [Bir arenada Flappy Bird üretimini karşılaştır](#case-47) | Değerlendirme ve sınırlar | İki Flappy Bird sonucunu karşılaştırmak için arena görevi kullan ve yargıyı göreve özgü tut | Evaluation |
| [Bölünmüş ekranlı işbirlikçi tarayıcı oyununu yeniden kur](#case-48) | Etkileşimli oyunlar ve 3D | Tek istekle tarayıcı tabanlı bölünmüş ekran işbirliği ve gerçek zamanlı çevre etkileşimi üret | Demo |
| [Command Code Design Mode ile oynanabilir oyun üret](#case-49) | Etkileşimli oyunlar ve 3D | Tek geçişli oyun yapımı için Command Code'un design komutunu kullan ve sonucun oynanabilir olup olmadığını kaydet | Demo |
| [Çince kaynaklardan birden çok konuyu araştır](#case-50) | Kodlama ve entegrasyonlar | Model kuşakları arasında kapsamlılık ve gecikmeyi karşılaştırmak için uzun süren araştırma görevleri kullan | Evaluation |
| [Bütünlüklü bir wuxia tarayıcı RPG'si oluştur](#case-51) | Etkileşimli oyunlar ve 3D | Hareket, savaş, görevler, envanter, hava, keşif ve 3D ortam işini tek oyunda birleştir | Demo |
| [Bir araçla Bongard görsel tümevarım problemini çöz](#case-52) | Değerlendirme ve sınırlar | Bongard muhakeme görevinde araç kullanımının görsel kuralı çıkarmaya yardım edip etmediğini dene | Evaluation |
| [Frontend zevkini ve 3D tasarımı GPT-5.6 Sol ile karşılaştır](#case-53) | Değerlendirme ve sınırlar | Sınırları belli frontend karşılaştırmasında özellikleri, görsel zevki, zarafeti ve 3D uygulamayı incele | Evaluation |
| [Oynanabilir Hollow Knight crossover'ı oluştur](#case-54) | Etkileşimli oyunlar ve 3D | Knight ile Kimi arasında oynanabilir savaş oluşturmak için mevcut oyun varlıklarını kullan | Demo |
| [BMW M4 CS'nin yandan görünüş SVG'sini üret](#case-55) | Frontend ve hareketli tasarım | Vektör illüstrasyon çıktısını incelemek için belirli araç ve bakış açısı kullan | Demo |
| [Çalışan uygulamalarla macOS'u tarayıcıda klonla](#case-56) | Kodlama ve entegrasyonlar | Müzik, tarayıcı ve email uygulamalarını içeren tarayıcı işletim sistemi simülasyonu kur | Demo |
| [Web sitesi üretimini üç model arasında karşılaştır](#case-57) | Değerlendirme ve sınırlar | Tek testte Kimi K3, Fable 5 ve GPT-5.6 Sol'u karşılaştırmak için görünür web sitesi çıktılarını kullan | Evaluation |
| [Ekran görüntüsü geri bildirimiyle Gargantua'yı yeniden oluştur](#case-58) | Frontend ve hareketli tasarım | Bilimsel görselleştirmeyi teşhis edip geliştirmek için art arda ekran görüntülerini gözlem olarak kullan | Tutorial |
| [Prosedürel 3D oyun üretimini ve maliyeti karşılaştır](#case-59) | Değerlendirme ve sınırlar | Promptu modeller arasında sabit tut; üretilen rulet, slot makinesi ve pinball sistemlerini çalışma başına maliyetle incele | Benchmark |
| [Tek geçişte Fall Guys tarzı 3D tarayıcı oyunu kur](#case-60) | Etkileşimli oyunlar ve 3D | Oynanabilir 3D engel oyunu üretmek ve projeyi incelemeye açmak için tek geçişli istek kullan | Demo |
| [Kıyamet sonrası Lizbon FPS'si kurup kendi kendine test ettir](#case-61) | Etkileşimli oyunlar ve 3D | Oynanabilir FPS sunmadan önce test eden, ekran görüntüsü alan ve yineleyen tek promptlu maksimum efor çalışması kullan | Demo |
| [Çalışan FaceTime içeren macOS simülasyonu kur](#case-62) | Kodlama ve entegrasyonlar | Üretilmiş bir uygulama etkileşiminin çalışıp çalışmadığını sınamak için sanal işletim sistemi görevi kullan | Demo |
| [Basit istekten Animal Crossing tarzı oyun üret](#case-63) | Etkileşimli oyunlar ve 3D | Oynanabilirlik, gameplay loop ve parallax efektlerini incelemek için minimal oyun brief'i kullan | Demo |
| [Çift görevli frontend efekt karşılaştırıcısı ekle](#case-64) | Kodlama ve entegrasyonlar | Tamamlanmış iki görevi seçen, yan yana gösteren, görünümleri ve etkileşimleri senkronlayan araç kur | Tutorial |
| [Tek cümlelik brief'ten Mario tarzı oyun üret](#case-65) | Etkileşimli oyunlar ve 3D | Oynanabilirlik, bölüm tasarımı, pixel art ve parallax'ı incelemek için minimal tek geçişli istek kullan | Demo |
| [Kara delik görselleştirmesini 62 ekran görüntüsüyle iyileştir](#case-66) | Frontend ve hareketli tasarım | Çok sayıda yinelemede görsel simülasyonu okumak, teşhis etmek ve düzeltmek için ekran görüntüsü feedback loop'u kullan | Tutorial |
| [Çalışan bir zombi birinci şahıs nişancı oyunu kur](#case-67) | Etkileşimli oyunlar ve 3D | Eksiksiz oynanabilir FPS eserini incelemek için somut bir zombi nişancı hedefi kullan | Demo |
| [Post-training için pazarlama PDF'i oluştur](#case-68) | Frontend ve hareketli tasarım | Pazarlama belgesi üretmek için adı belirtilmiş ürün ve teslim formatı kullan | Demo |
| [3D cephanelik sahnesinin ayrıntı ve ışığını karşılaştır](#case-69) | Değerlendirme ve sınırlar | Sınırları belli Kimi K3 ve Opus 4.8 karşılaştırmasında nesne yoğunluğu, aydınlatma ve sahne ayrıntısını incele | Evaluation |
| [Tek promptla kullanıcı arayüzü oluştur](#case-70) | Frontend ve hareketli tasarım | Eksiksiz UI tasarımı üretmek ve incelemek için tek istek kullan | Demo |
| [Bağımsız bir uzay gemisi oyunu oluştur](#case-71) | Etkileşimli oyunlar ve 3D | Kimi K3 Standard ile ilk sürümü üretip tutarlılık, hata, görsel kalite ve token maliyetini karşılaştır | Demo |
| [Aynı Arena promptlarıyla frontendleri karşılaştır](#case-72) | Değerlendirme ve sınırlar | Tek bir sıralama puanı yerine aynı promptları ve yan yana çıktıları kullan | Benchmark |
| [Summer Engine oyununu kendi kendine test et](#case-73) | Etkileşimli oyunlar ve 3D | Kimi K3'ün oyunu çalıştırmasını, ekran görüntülerini ve logları inceleyip aynı oturumda hataları düzeltmesini sağla | Demo |
| [Kimi Code'u kodlama ajanlarında değerlendir](#case-74) | Değerlendirme ve sınırlar | Kimi K3'ü birden fazla test ve görev maliyetiyle değerlendir; tek frontend sıralamasını genelleme | Benchmark |
| [Kimi'yi Codex alt ajanı olarak yapılandır](#case-75) | Kodlama ve entegrasyonlar | Orkestrasyonu Codex'te tut, frontend uygulamasını gizli bilgi sınırıyla Kimi K3 OpenCode alt ajanına devret | Tutorial |
| [Arena ve onarım testini karşılaştır](#case-76) | Değerlendirme ve sınırlar | Kimi K3 birinde birinci, diğerinde yedinci olabildiği için frontend tercihi ve depo onarımını birlikte incele | Benchmark |
| [Tarayıcı battle royale oyununu yinele](#case-77) | Etkileşimli oyunlar ve 3D | Özellikli tarayıcı oyunlarında uzun otonom yinelemeler ve hedefli ek promptlar bekle | Demo |
| [Ödüllü stilde web sitesi oluştur](#case-78) | Frontend ve hareketli tasarım | Sadece son ekran görüntüsü yerine tam kayıtlı oturumu değerlendir | Tutorial |
| [Basit kodlamayı ChatLLM ile yönlendir](#case-79) | Kodlama ve entegrasyonlar | Basit kodlamayı Kimi K3'e gönder, zor kodlama ve tasarımı diğer modellere ayır | Integration |
| [Kimi K3ü Prinzbench ile ölçmek](#case-80) | Değerlendirme ve sınırlar | Prinzbench, Kimi K3ü OpenAI o3 ve diğer modellerle aynı değerlendirme tablosunda karşılaştırarak sırasını ve sınırlarını gösteriyor. | Benchmark |
| [Metaball kaydırma ön yüzü oluşturmak](#case-81) | Frontend ve hareketli tasarım | Kimi K3, parlayan metaball öğeleri ve kaydırmaya bağlı animasyonlarla rafine bir web arayüzü kuruyor. | Demo |
| [Kişisel siteyi modeller arasında yeniden tasarlamak](#case-82) | Frontend ve hareketli tasarım | Aynı kişisel site yeniden tasarım görevi Kimi K3 ve diğer modellerle karşılaştırılarak görsel kalite ve yapı farkları gösteriliyor. | Evaluation |
| [Bir uzay oyunu manzarasını genişletmek](#case-83) | Etkileşimli oyunlar ve 3D | Kimi K3, uzay oyunu sahnesini arazi, gemiler ve ışıklandırma içeren geniş bir görsele dönüştürüyor. | Demo |
| [Three.js fizik rendererını açmak](#case-84) | Etkileşimli oyunlar ve 3D | Kimi K3, Three.js fizik render sorununu ilerletmek için uygulama yardımcısı olarak kullanıldı. | Demo |
| [ISS dijital ikiz üretimini karşılaştırmak](#case-85) | Değerlendirme ve sınırlar | Kimi K3, ISS dijital ikiz görevi üzerinde diğer modellerle karşılaştırılarak karmaşık 3D görselleştirmedeki farkları gösteriyor. | Benchmark |
| [Etkileşimli saç derisi keşif aracı yapmak](#case-86) | Frontend ve hareketli tasarım | Kimi K3, eğitim amaçlı insan saç derisi görselleştiricisi üreterek açıklayıcı UI kullanımını gösteriyor. | Demo |
| [3D küre panosu promptu paylaşmak](#case-87) | Frontend ve hareketli tasarım | Açık bir prompt, Kimi K3 ile 3D küre tabanlı pano arayüzü üretme akışını gösteriyor. | Tutorial |
| [Tarayıcıda tek dosyalık Counter-Strike yapmak](#case-88) | Etkileşimli oyunlar ve 3D | Kimi K3, tek HTML dosyasında çalışan FPS tarzı bir tarayıcı oyunu oluşturuyor. | Demo |
| [WebGPU orman dünyasını değerlendirmek](#case-89) | Değerlendirme ve sınırlar | Kimi K3 ile oluşturulan WebGPU orman dünyası, etkileyici 3D sahne kalitesi ve sınırları açısından değerlendiriliyor. | Evaluation |
| [Cam ev promptlarını karşılaştır](#case-90) | Değerlendirme ve sınırlar | Aynı mimari sahne promptuyla Kimi K3 ve Opus 4.8’i atmosfer, ışık ve mekansal bütünlük açısından karşılaştır. | Evaluation |
| [Üretilmiş assetlerle CS kur](#case-91) | Kodlama ve entegrasyonlar | Küçük bir Counter-Strike tarzı tarayıcı oyunu prototiplerken oyun kodu için Kimi K3, assetler için GPT Image 2 kullan. | Integration |
| [Voxel futbol golünü ölç](#case-92) | Değerlendirme ve sınırlar | Aynı saf HTML/CSS/JS futbol animasyonu promptunu iki modelde çalıştırarak hareket kalitesini ve maliyeti karşılaştır. | Benchmark |
| [Minecraft benchmark incele](#case-93) | Değerlendirme ve sınırlar | Lansman hype’ını veya fiyatı yeterli kanıt saymadan önce yapılandırılmış bir Minecraft incelemesi izle. | Benchmark |
| [Beş UI UX testi çalıştır](#case-94) | Frontend ve hareketli tasarım | Kimi K3’ü tek bir frontend ekran görüntüsü yerine UI, logo ve Figma MCP görevleriyle değerlendir. | Evaluation |
| [Command Code Design skill kullan](#case-95) | Kodlama ve entegrasyonlar | Token bütçesi altında görsel oyun prototipi kurarken Kimi K3’ü Command Code’daki özel design skill ile birleştir. | Integration |
| [Piramit keşif oyunu kur](#case-96) | Etkileşimli oyunlar ve 3D | Kimi K3 ile bir günlük 3D keşif oyunu geçişi yap, sonra görev, iç mekan ve keşif kapsamına bakarak kaliteyi değerlendir. | Demo |
| [Referanslardan landing üret](#case-97) | Frontend ve hareketli tasarım | Referans panoları, Figma AI ve Motion Sites ile Kimi K3 kullanarak görsel yönü tekrar kullanılabilir landing page bölümlerine çevir. | Tutorial |
| [API tier limitlerini ölç](#case-98) | Değerlendirme ve sınırlar | Kimi K3 agent run planını yalnızca model fiyatına değil token, tier, TPM ve TPD sınırlarına göre yap. | Limit |
| [Limbo tarzı demo karşılaştır](#case-99) | Değerlendirme ve sınırlar | Aynı oyun prototipinde Kimi K3 ile Fable 5’i oynanabilir kapsam, görsel polish, maliyet ve bug açısından karşılaştır. | Benchmark |

<a id="games-3d"></a>
## 🎮 Etkileşimli oyunlar ve 3D

<a id="case-1"></a>
### Case 1: [Tek prompt ile voxel pod racer oluştur](https://x.com/ivanfioravanti/status/2077763009657627055) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Kısa bir fikirle yarış prototipi kur ve sonraki sürümü sınırla**

Üretici Kimi K3'ün ilk sürümü tek bir açık prompt ile yaptığını ve daha fazla yarışçı, bitiş çizgisi ve ayrıntı incelemesi planladığını bildiriyor

**Prompt:**

```text
Voxel star wars pod-racers run
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01-poster.jpg" alt="Case 1 source video poster" height="360"></a>

[Play case 1 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-01.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-2"></a>
### Case 2: [Frogger'ı aynı prompt ile karşılaştır](https://x.com/ivanfioravanti/status/2077754781964054825) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Model farklarını görmek için promptu sabit tut**

Üretici Kimi K3 sürümünü karşılaştırma olarak paylaşıyor. Kaynak prompt metnini veya değerlendirme ölçütünü vermiyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02-poster.jpg" alt="Case 2 source video poster" height="360"></a>

[Play case 2 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-02.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-3"></a>
### Case 3: [Frogger ve oynanış kaydını üret](https://x.com/TheAhmadOsman/status/2077776567292338285) (by [@TheAhmadOsman](https://x.com/TheAhmadOsman))

**Oyunu ve kayıt akışını ayrı tek geçişlerle dene**

Üretici oyunun ve kayıt akışının birer geçişte üretildiğini söylüyor. Tam promptlar yayımlanmamış

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03-poster.jpg" alt="Case 3 source video poster" height="360"></a>

[Play case 3 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-03.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-4"></a>
### Case 4: [Three.js ile uçak gemisi prototiple](https://x.com/HarshithLucky3/status/2077753222018814360) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**Belirli bir kalkış ve dönüş sahnesiyle etkileşimli 3D'yi dene**

Üretici Nimitz sınıfı gemide savaş uçağı kalkış ve dönüşünü gösteriyor ve 3D üretimini olumlu değerlendiriyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04-poster.jpg" alt="Case 4 source video poster" height="360"></a>

[Play case 4 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-04.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-9"></a>
### Case 9: [Ajan araçlarıyla Paper Mario esintili bir oyun kur](https://x.com/chongdashu/status/2077886028866531655) (by [@chongdashu](https://x.com/chongdashu))

**Hem 2D hem de 3D oyun öğeleri üretmek için Kimi K3'ü bir ajan harness'ı ve varlık araçlarıyla birleştir**

Üretici Paper Mario esintili oyunda Kimi K3 ile Grok Build'i, 2D varlıklar için Spriterrific'i ve 3D varlıklar için geometriyi kullandığını bildiriyor. Kaynak araç ve skill kullanımını gösteriyor ancak yeniden kullanılabilir tam prompt yayımlamıyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-09.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-09-poster.jpg" alt="Case 9 source video poster" height="360"></a>

[Play case 9 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-09.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-11"></a>
### Case 11: [Metroda geçen bir birinci şahıs nişancı oyunu üret](https://x.com/bijanbowen/status/2077881805751873997) (by [@bijanbowen](https://x.com/bijanbowen))

**Üretilen birinci şahıs nişancı sonucunu incelemek için somut bir metro ortamı kullan**

Üretici Kimi K3'e atfedilen bir metro FPS gösteriyor ve influencer statüsünün sonucu etkileyip etkilemediğinden emin olmadığını açıkça belirtiyor. Prompt veya yeniden üretilebilir workflow sağlanmıyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-11.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-11-poster.jpg" alt="Case 11 source video poster" height="360"></a>

[Play case 11 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-11.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-19"></a>
### Case 19: [Blender MCP ile V8 motoru modelle](https://x.com/aisearchio/status/2077962156147146925) (by [@aisearchio](https://x.com/aisearchio))

**Ayrıntılı mekanik 3D model üretmek için Blender MCP ve tek bir istek kullan**

İncelemeci, Kimi K3'ün Blender MCP ile tek prompttan eksiksiz bir V8 motoru ürettiğini bildiriyor. Gönderi daha kapsamlı incelemeye bağlantı verse de sağlanan kayıtta tam prompt yok

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-19.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-19-poster.jpg" alt="Case 19 source video poster" height="360"></a>

[Play case 19 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-19.mp4)

Type: Integration | Date: 2026-07-17

---

<a id="case-23"></a>
### Case 23: [Tek referanstan oynanabilir savaş arenası kur](https://x.com/VORTEX_Promos/status/2077879705378730074) (by [@VORTEX_Promos](https://x.com/VORTEX_Promos))

**Eksiksiz oynanabilir bir arenanın tek geçişte üretimini denemek için tek referans kullan**

Üretici Kimi K3'ün tek referanstan tek geçişte oynanabilir savaş arenası ürettiğini bildiriyor. Gönderide ayrı bir leaderboard iddiası da var ancak somut kullanım örneği gösterilen arena eseridir

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23-poster.jpg" alt="Case 23 source video poster" height="360"></a>

[Play case 23 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-23-01.jpg" alt="Case 23 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-24"></a>
### Case 24: [Üç kendi kendine oynayan retro oyunu HTML dosyaları olarak kur](https://x.com/rohanpaul_ai/status/2077889084761206860) (by [@rohanpaul_ai](https://x.com/rohanpaul_ai))

**Bağımsız HTML oyun dosyalarında grafik, düşman, kural ve özerk oynanış şartı koy**

Kaynak, modellerin Road Fighter, Battle City ve Q*bert'i kendi kendine oynayan HTML dosyaları olarak kurduğu Atomic Chat karşılaştırmasını bildiriyor. Maliyet ve kalite karşılaştırması yayıncıya aittir ve burada bağımsız olarak yeniden üretilmemiştir

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-24.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-24-poster.jpg" alt="Case 24 source video poster" height="360"></a>

[Play case 24 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-24.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-27"></a>
### Case 27: [Tek geçişte bukalemun saklambaç oyunu kur](https://x.com/aimlapi/status/2077898742179459274) (by [@aimlapi](https://x.com/aimlapi))

**Renk eşleme, prosedürel bölgeler, ses ve çok turlu skor içeren tek dosyalı oyun üret**

AIMLAPI aynı promptla tek geçişli saklambaç karşılaştırması bildiriyor ve Kimi K3 için $3.11, Fable 5 için $12.23 maliyet listeliyor. Özellik ve maliyet iddiaları sağlayıcı sonuçlarıdır

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-27.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-27-poster.jpg" alt="Case 27 source video poster" height="360"></a>

[Play case 27 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-27.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-36"></a>
### Case 36: [Ajan araç zinciriyle Paper Mario benzeri 2.5D oyun kur](https://x.com/chongdashu/status/2077981621223837739) (by [@chongdashu](https://x.com/chongdashu))

**2.5D oyun workflow'u oluşturmak için Kimi K3'ü Grok Build veya Claude Code ve Spriterrific ile kullan**

Üretici Grok Build ve Kimi K3 ile tam walkthrough sağlıyor ve Spriterrific ile sprite üretimini gösteriyor. Kaynak araçları tanımlıyor ancak yeniden kullanılabilir tam promptlar sunmuyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-36.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-36-poster.jpg" alt="Case 36 source video poster" height="360"></a>

[Play case 36 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-36.mp4)

Type: Tutorial | Date: 2026-07-17

---

<a id="case-43"></a>
### Case 43: [Tarayıcı tabanlı 3D wuxia RPG kur](https://x.com/AngryTomtweets/status/2077868163136450619) (by [@AngryTomtweets](https://x.com/AngryTomtweets))

**Yakın dövüş, görevler, envanter, hava durumu, iç mekânlar, Blender ortam işi ve uyarlanmış varlıkları birleştir**

Kaynak yakın dövüş, görev, envanter, dinamik hava ve keşfedilebilir iç mekânlara sahip Kimi K3 tarayıcı RPG'si; ayrıca Blender modelleme, collision iyileştirme, PBR yeniden dokulama ve uyarlanmış açık varlıklar bildiriyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-43.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-43-poster.jpg" alt="Case 43 source video poster" height="360"></a>

[Play case 43 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-43.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-44"></a>
### Case 44: [Tarayıcıda çok oyunculu Minecraft benzeri oyun kur](https://x.com/Alezander907/status/2077926014710407407) (by [@Alezander907](https://x.com/Alezander907))

**Süre ve maliyeti sınırlandırılmış bir çalışmada oynanabilir çevrimiçi çok oyunculu tarayıcı oyunu üret**

Üretici Kimi K3'ün bir saatte $6.57 maliyetle tarayıcıda oynanabilir çok oyunculu Minecraft benzeri oyun yaptığını bildiriyor. Bunlar tek esere ait öz bildirime dayalı çalışma rakamlarıdır

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-44.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-44-poster.jpg" alt="Case 44 source video poster" height="360"></a>

[Play case 44 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-44.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-48"></a>
### Case 48: [Bölünmüş ekranlı işbirlikçi tarayıcı oyununu yeniden kur](https://x.com/ridark_eth/status/2077882889803378969) (by [@ridark_eth](https://x.com/ridark_eth))

**Tek istekle tarayıcı tabanlı bölünmüş ekran işbirliği ve gerçek zamanlı çevre etkileşimi üret**

Üretici Kimi K3'ün tek promptla It Takes Two esintili, Mario ve Luigi'nin bölünmüş ekranda ve çevreyle gerçek zamanlı etkileştiği tarayıcı oyunu ürettiğini bildiriyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-48.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-48-poster.jpg" alt="Case 48 source video poster" height="360"></a>

[Play case 48 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-48.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-49"></a>
### Case 49: [Command Code Design Mode ile oynanabilir oyun üret](https://x.com/naymur_dev/status/2077873562661335207) (by [@naymur_dev](https://x.com/naymur_dev))

**Tek geçişli oyun yapımı için Command Code'un design komutunu kullan ve sonucun oynanabilir olup olmadığını kaydet**

Üretici Command Code design mode ile tek geçişli karşılaştırma yaptığını ve Kimi K3 çalışmasının $0.038 karşılığında oynanabilir oyun ürettiğini bildiriyor. Bu maliyet ve kalite sonucu öz bildirime dayanır

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-49.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-49-poster.jpg" alt="Case 49 source video poster" height="360"></a>

[Play case 49 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-49.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-51"></a>
### Case 51: [Bütünlüklü bir wuxia tarayıcı RPG'si oluştur](https://x.com/TokenGremlin/status/2077855657068310620) (by [@TokenGremlin](https://x.com/TokenGremlin))

**Hareket, savaş, görevler, envanter, hava, keşif ve 3D ortam işini tek oyunda birleştir**

Kaynak yakın dövüş, görevler, envanter, dinamik hava, keşfedilebilir iç mekânlar ve bütünlüklü 3D oynanış yapısını birleştiren Kimi K3 wuxia tarzı tarayıcı RPG'si bildiriyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-51.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-51-poster.jpg" alt="Case 51 source video poster" height="360"></a>

[Play case 51 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-51.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-54"></a>
### Case 54: [Oynanabilir Hollow Knight crossover'ı oluştur](https://x.com/wangfeng0315/status/2077933531200991583) (by [@wangfeng0315](https://x.com/wangfeng0315))

**Knight ile Kimi arasında oynanabilir savaş oluşturmak için mevcut oyun varlıklarını kullan**

Kimi'de çalıştığını belirten üretici, Hollow Knight varlıklarından Knight'ın Kimi ile savaştığı bir oyun kurduğunu bildiriyor ve açık oynama bağlantısı sunuyor. Atıf ve değerlendirmede bu bağlantı dikkate alınmalıdır

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54-poster.jpg" alt="Case 54 source video poster" height="360"></a>

[Play case 54 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-54-01.jpg" alt="Case 54 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-17

---

<a id="case-60"></a>
### Case 60: [Tek geçişte Fall Guys tarzı 3D tarayıcı oyunu kur](https://x.com/aayushman2703/status/2077857886441783526) (by [@aayushman2703](https://x.com/aayushman2703))

**Oynanabilir 3D engel oyunu üretmek ve projeyi incelemeye açmak için tek geçişli istek kullan**

Üretici Kimi K3'ün tek geçişte Fall Guys tarzı tarayıcı oyunu yaptığını ve prompt ile GitHub projesinin kaynakta bağlantılı olduğunu bildiriyor. Bu kayıt promptu yeniden yayımlamıyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-60.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-60-poster.jpg" alt="Case 60 source video poster" height="360"></a>

[Play case 60 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-60.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-61"></a>
### Case 61: [Kıyamet sonrası Lizbon FPS'si kurup kendi kendine test ettir](https://x.com/goncalo_canhoto/status/2077863166655037668) (by [@goncalo_canhoto](https://x.com/goncalo_canhoto))

**Oynanabilir FPS sunmadan önce test eden, ekran görüntüsü alan ve yineleyen tek promptlu maksimum efor çalışması kullan**

Üretici Kimi K3'ün yaklaşık bir saatte, tekrarlanan testler, ekran görüntüleri ve yinelemelerle oynanabilir Apocalyptic Lisbon tarayıcı FPS'si ürettiğini bildiriyor. Süre ve süreç ayrıntıları öz bildirime dayanır

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-61-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-61-01.jpg" alt="Case 61 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-63"></a>
### Case 63: [Basit istekten Animal Crossing tarzı oyun üret](https://x.com/gagarot200/status/2077949230287896830) (by [@gagarot200](https://x.com/gagarot200))

**Oynanabilirlik, gameplay loop ve parallax efektlerini incelemek için minimal oyun brief'i kullan**

Üretici Kimi K3'ün çok basit prompttan gameplay loop ve parallax efektleri içeren tamamen oynanabilir Animal Crossing tarzı oyun ürettiğini bildiriyor. Tam ifade sağlanan kayıtta yok

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-63.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-63-poster.jpg" alt="Case 63 source video poster" height="360"></a>

[Play case 63 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-63.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-65"></a>
### Case 65: [Tek cümlelik brief'ten Mario tarzı oyun üret](https://x.com/izutorishima/status/2077939370154475992) (by [@izutorishima](https://x.com/izutorishima))

**Oynanabilirlik, bölüm tasarımı, pixel art ve parallax'ı incelemek için minimal tek geçişli istek kullan**

Üretici Kimi K3'ün tek brief'ten belirgin hatasız çalışan, bölüm yapısı ve parallax içeren Mario tarzı oyun ürettiğini bildiriyor. Aynı rapor müzik ve grafik kalitesini eleştiriyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-01.jpg" alt="Case 65 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-02.jpg" alt="Case 65 source image 2" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-03.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-65-03.jpg" alt="Case 65 source image 3" height="360"></a>

Type: Demo | Date: 2026-07-17

---

<a id="case-67"></a>
### Case 67: [Çalışan bir zombi birinci şahıs nişancı oyunu kur](https://x.com/X2worldtech/status/2077902793449296203) (by [@X2worldtech](https://x.com/X2worldtech))

**Eksiksiz oynanabilir FPS eserini incelemek için somut bir zombi nişancı hedefi kullan**

Kaynak Kimi K3'e atfedilen tam çalışan bir zombi FPS gösteriyor. Prompt, uygulama ayrıntıları veya dış oynanış değerlendirmesi sunulmuyor

> [!WARNING]
> The original source permalink returned HTTP 404 during the 2026-07-17 audit. Attribution and evidence are preserved from the supplied high-confidence source package.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-67.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-67-poster.jpg" alt="Case 67 source video poster" height="360"></a>

[Play case 67 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-67.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-71"></a>
### Case 71: [Bağımsız bir uzay gemisi oyunu oluştur](https://x.com/ChrisGPT/status/2078261217924087999) (by [@ChrisGPT](https://x.com/ChrisGPT))

**Kimi K3 Standard ile ilk sürümü üretip tutarlılık, hata, görsel kalite ve token maliyetini karşılaştır**

ChrisGPT yaklaşık 2,50 dolarlık API token maliyetiyle ilk uzay gemisi oyunu sürümünü bildirdi. GPT-5.5 sürümünden daha tutarlı ve az hatalıydı, ancak Fable 5 görsel olarak daha cilalı kaldı

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-71.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-71-poster.jpg" alt="Case 71 source video poster" height="360"></a>

[Play case 71 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-71.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-73"></a>
### Case 73: [Summer Engine oyununu kendi kendine test et](https://x.com/MathiasHeide/status/2078231589436465199) (by [@MathiasHeide](https://x.com/MathiasHeide))

**Kimi K3'ün oyunu çalıştırmasını, ekran görüntülerini ve logları inceleyip aynı oturumda hataları düzeltmesini sağla**

Mathias Heide, Kimi K3'ün 27 dakikalık tek oturumda kağıt uçak oyunu yaptığını, ekran görüntüsü ve logları okuyup hataları düzelttiğini ve siyah uçağı beyaza çevirdiğini bildiriyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-73.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-73-poster.jpg" alt="Case 73 source video poster" height="360"></a>

[Play case 73 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-73.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-77"></a>
### Case 77: [Tarayıcı battle royale oyununu yinele](https://x.com/Ananth7e/status/2078158089929601203) (by [@Ananth7e](https://x.com/Ananth7e))

**Özellikli tarayıcı oyunlarında uzun otonom yinelemeler ve hedefli ek promptlar bekle**

Ananth, PUBG tarzı oyun için 130 dakikadan fazla ve 40'tan fazla Chrome ekran görüntüsü döngüsü, ardından kalan hatalar için iki ek prompt bildiriyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-77.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-77-poster.jpg" alt="Case 77 source video poster" height="360"></a>

[Play case 77 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-77.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-83"></a>
### Case 83: [Bir uzay oyunu manzarasını genişletmek](https://x.com/startracker/status/2078543423167160342) (by [@startracker](https://x.com/startracker))

**Kimi K3, uzay oyunu sahnesini arazi, gemiler ve ışıklandırma içeren geniş bir görsele dönüştürüyor.**

Kamuya açık görsel, oyun tarzı bir bilim kurgu sahnesi sunuyor ve Kimi K3ün derinlik, nesne ve renk düzenini birlikte ele alışını gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-83.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-83-poster.jpg" alt="Case 83 source video poster" height="360"></a>

[Play case 83 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-83.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-84"></a>
### Case 84: [Three.js fizik rendererını açmak](https://x.com/mattwatkajtys/status/2078523373861339475) (by [@mattwatkajtys](https://x.com/mattwatkajtys))

**Kimi K3, Three.js fizik render sorununu ilerletmek için uygulama yardımcısı olarak kullanıldı.**

Yazar, takıldığı 3D render problemini Kimi K3 ile çözdüğünü belirtiyor ve tarayıcıdaki fizik sahnesini video ile gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-84.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-84-poster.jpg" alt="Case 84 source video poster" height="360"></a>

[Play case 84 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-84.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-88"></a>
### Case 88: [Tarayıcıda tek dosyalık Counter-Strike yapmak](https://x.com/prasenx/status/2078453069021659477) (by [@prasenx](https://x.com/prasenx))

**Kimi K3, tek HTML dosyasında çalışan FPS tarzı bir tarayıcı oyunu oluşturuyor.**

Yazar tek dosyada çalışan Counter-Strike benzeri oyunu gösteriyor; oyun döngüsü, giriş, render ve basit UI birlikte üretilmiş.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-88.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-88-poster.jpg" alt="Case 88 source video poster" height="360"></a>

[Play case 88 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-88.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-96"></a>
### Case 96: [Piramit keşif oyunu kur](https://x.com/ice_bearcute/status/2078828887468056763) (by [@ice_bearcute](https://x.com/ice_bearcute))

**Kimi K3 ile bir günlük 3D keşif oyunu geçişi yap, sonra görev, iç mekan ve keşif kapsamına bakarak kaliteyi değerlendir.**

ice_bearcute, Kimi K3 ile bir günde tam bir 3D Pyramid Expedition oyunu yaptığını bildiriyor. Kaynak bunun yalnızca dış mekan sahnesi olmadığını, oyuncunun antik mezarı gezip görevleri tamamlayabildiğini söylüyor; ekli medya gameplay kanıtı sağlıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-96.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-96-poster.jpg" alt="Case 96 source video poster" height="360"></a>

[Play case 96 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-96.mp4)

Type: Demo | Date: 2026-07-19

---


<a id="frontend-motion"></a>
## 🎨 Frontend ve hareketli tasarım

<a id="case-5"></a>
### Case 5: [Etkileşimli motion frontend oluştur](https://x.com/chetaslua/status/2077749371144442022) (by [@chetaslua](https://x.com/chetaslua))

**Duraklatıldığında da etkileşimli kalan grafikler üret**

Üretici 42 dakika, tek geçiş, basit kod ve harness, MCP ya da skill kullanılmadığını bildiriyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05-poster.jpg" alt="Case 5 source video poster" height="360"></a>

[Play case 5 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-05.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-6"></a>
### Case 6: [Senkron hareketli reklam üret](https://x.com/abhinavflac/status/2077760297918484667) (by [@abhinavflac](https://x.com/abhinavflac))

**Müzik, efekt ve hareket senkronunu kontrol et**

Üretici Spotify tarzı reklamın yalnızca prompt ile tek geçişte çıktığını söylüyor. Tam prompt yayımlanmamış

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06-poster.jpg" alt="Case 6 source video poster" height="360"></a>

[Play case 6 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-06.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-14"></a>
### Case 14: [Hareketli tasarımı bütünüyle kodla oluştur](https://x.com/chetaslua/status/2077952938564354503) (by [@chetaslua](https://x.com/chetaslua))

**Tek geçişli kodlama workflow'unun yardımcı üretim araçları olmadan hareketli tasarım üretip üretemediğini dene**

Üretici MCP, skill, araç, video üretimi veya özel prompt olmadan tamamen kodla yapılmış tek geçişli bir Kimi K3 hareketli tasarım sonucu bildiriyor. Tam prompt verilmemiş

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-14.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-14-poster.jpg" alt="Case 14 source video poster" height="360"></a>

[Play case 14 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-14.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-15"></a>
### Case 15: [Bir kişiyi araştırıp animasyonlu kişisel site kur](https://x.com/nicky_sap/status/2077857190707429411) (by [@nicky_sap](https://x.com/nicky_sap))

**Geniş bir kişisel site brief'i ver; ardından modelin araştırma, planlama, yineleme ve tarayıcı doğrulamasını incele**

Üretici Kimi K3'ün Nick Saponaro'yu araştırdığını ve geniş bir istekten planlama, test, yineleme ve tarayıcı kontrolleri içeren animasyonlu kişisel site ürettiğini bildiriyor. Sonuç, üreticinin kendi workflow gösterimidir

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-15.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-15-poster.jpg" alt="Case 15 source video poster" height="360"></a>

[Play case 15 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-15.mp4)

Type: Tutorial | Date: 2026-07-16

---

<a id="case-17"></a>
### Case 17: [Kara delik simülasyonu oluştur](https://x.com/chetaslua/status/2077961850352971796) (by [@chetaslua](https://x.com/chetaslua))

**Üretilmiş bir kara delik simülasyonunu incelemek için bilimsel görselleştirme görevi kullan**

Üretici Kimi K3'e atfedilen bir kara delik simülasyonu gösteriyor ve gördüklerinin en iyisi olduğunu söylüyor. Görünür sonuç var; prompt, rubric veya bağımsız doğrulama yok

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-17.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-17-poster.jpg" alt="Case 17 source video poster" height="360"></a>

[Play case 17 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-17.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-22"></a>
### Case 22: [Karmaşık frontend modelleme, parçacıklar ve shader'ları dene](https://x.com/karminski3/status/2077889959223337099) (by [@karminski3](https://x.com/karminski3))

**Tek geçişte modelleme hassasiyetini, parçacık efektlerini ve inline shader üretimini incelemek için açık bir frontend promptu kullan**

Üretici hassas modelleme, parçacık efektleri ve karmaşık inline shader kodunu kapsayan tek geçişli Kimi K3 frontend sonucu bildiriyor ve test promptunun bağlantılı kaynakta açık olduğunu söylüyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-22.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-22-poster.jpg" alt="Case 22 source video poster" height="360"></a>

[Play case 22 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-22.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-26"></a>
### Case 26: [Tek denemede prosedürel müzik aracı üret](https://x.com/mirochill/status/2077723551331758478) (by [@mirochill](https://x.com/mirochill))

**Etkileşimli prosedürel müzik üretecinin tek geçişli üretimini dene ve görünür sonucu temkinli karşılaştır**

Üretici Kimi K3'ün tek denemede prosedürel müzik aracı ürettiğini ve bunu Fable 5 ile GPT-5.6 Sol sonuçlarından daha iyi bulduğunu bildiriyor. Bu, standart bir benchmark değil, üreticinin kendi test setidir

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-26-poster.jpg" alt="Case 26 source video poster" height="360"></a>

[Play case 26 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-26.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-33"></a>
### Case 33: [İki görselden Three.js ürün sayfası oluştur](https://x.com/1littlecoder/status/2077890296806031665) (by [@1littlecoder](https://x.com/1littlecoder))

**Ürün sunumu üretmek için iki referans görseli ve açık bir Three.js şartı kullan**

Üretici Kimi K3'ün iki görselden ürün sayfası tasarladığını ve özellikle istenen Three.js sürümünü ürettiğini bildiriyor. Ek prompt veya uygulama ayrıntısı yok

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-33.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-33-poster.jpg" alt="Case 33 source video poster" height="360"></a>

[Play case 33 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-33.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-39"></a>
### Case 39: [Lüks bir ekmek kesici ve ürün sayfası tasarla](https://x.com/filicroval/status/2077871090731221438) (by [@filicroval](https://x.com/filicroval))

**Ürün fikri, patlatılmış görünüm, gösterim ve landing page'i tek tasarım eserinde birleştir**

Üretici Kimi K3'ün giyotin tarzı ekmek kesici icat ettiğini, lüks ürün olarak sunduğunu ve patlatılmış görünüm ile gösterim içeren landing page hazırladığını bildiriyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-39.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-39-poster.jpg" alt="Case 39 source video poster" height="360"></a>

[Play case 39 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-39.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-45"></a>
### Case 45: [On saniyelik özyinelemeli pelikan GIF'i üret](https://x.com/1littlecoder/status/2077880380900937865) (by [@1littlecoder](https://x.com/1littlecoder))

**GIF'te anlatı sürekliliği ve özyinelemeyi incelemek için tamamen belirtilmiş döngülü animasyon brief'i kullan**

Kaynak bisiklete binen ve kamera yaklaşırken mesajla aynı videoyu alan pelikanı anlatan on saniyelik döngülü GIF promptunu içeriyor. Üretici Kimi K3 animasyonunu gösteriyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-45.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-45-poster.jpg" alt="Case 45 source video poster" height="360"></a>

[Play case 45 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-45.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-55"></a>
### Case 55: [BMW M4 CS'nin yandan görünüş SVG'sini üret](https://x.com/HarshithLucky3/status/2077765821380886942) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**Vektör illüstrasyon çıktısını incelemek için belirli araç ve bakış açısı kullan**

Üretici Kimi K3 Max'e atfedilen yandan görünüş BMW M4 CS SVG'si gösteriyor. Sağlanan kaynakta eser var ancak prompt veya üretim adımları yok

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-55-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-55-01.jpg" alt="Case 55 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-58"></a>
### Case 58: [Ekran görüntüsü geri bildirimiyle Gargantua'yı yeniden oluştur](https://x.com/AngryTomtweets/status/2077868981659324444) (by [@AngryTomtweets](https://x.com/AngryTomtweets))

**Bilimsel görselleştirmeyi teşhis edip geliştirmek için art arda ekran görüntülerini gözlem olarak kullan**

Kaynak Kimi K3'ün Interstellar'daki Gargantua'yı kendi çektiği 62 ekran görüntüsüyle; her sonucu okuyup sorunları teşhis ederek ve yinelemeli davranarak yeniden oluşturduğunu bildiriyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-58.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-58-poster.jpg" alt="Case 58 source video poster" height="360"></a>

[Play case 58 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-58.mp4)

Type: Tutorial | Date: 2026-07-16

---

<a id="case-66"></a>
### Case 66: [Kara delik görselleştirmesini 62 ekran görüntüsüyle iyileştir](https://x.com/TokenGremlin/status/2077855959201042645) (by [@TokenGremlin](https://x.com/TokenGremlin))

**Çok sayıda yinelemede görsel simülasyonu okumak, teşhis etmek ve düzeltmek için ekran görüntüsü feedback loop'u kullan**

Kaynak Kimi K3'ün Interstellar'daki Gargantua'yı 62 ekran görüntüsü boyunca çıktısını gözlemleyip geliştirerek yeniden kurduğunu bildiriyor. Bu, bağımsız fiziksel doğruluk değil bildirilen feedback loop'u gösterir

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-66.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-66-poster.jpg" alt="Case 66 source video poster" height="360"></a>

[Play case 66 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-66.mp4)

Type: Tutorial | Date: 2026-07-16

---

<a id="case-68"></a>
### Case 68: [Post-training için pazarlama PDF'i oluştur](https://x.com/Satvik_Pen/status/2077859673517023313) (by [@Satvik_Pen](https://x.com/Satvik_Pen))

**Pazarlama belgesi üretmek için adı belirtilmiş ürün ve teslim formatı kullan**

Üretici Kimi K3'ten Thinking Machines'in Inkling post-training ürünü hakkında pazarlama PDF'i istediğini, sonucu paylaştığını ve perde arkası süreci övdüğünü bildiriyor. Prompt veya değerlendirme ölçütleri sunulmuyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-01.png" alt="Case 68 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-02.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-02.png" alt="Case 68 source image 2" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-03.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-03.png" alt="Case 68 source image 3" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-04.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-68-04.png" alt="Case 68 source image 4" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-70"></a>
### Case 70: [Tek promptla kullanıcı arayüzü oluştur](https://x.com/BrianMRey/status/2077891942088671689) (by [@BrianMRey](https://x.com/BrianMRey))

**Eksiksiz UI tasarımı üretmek ve incelemek için tek istek kullan**

Üretici tek promptlu Kimi K3 çalışmasına atfedilen UI tasarımını gösteriyor ve son derece olumlu öznel değerlendirme yapıyor. Tam prompt ve rubric sunulmuyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-70.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-70-poster.jpg" alt="Case 70 source video poster" height="360"></a>

[Play case 70 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-70.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-78"></a>
### Case 78: [Ödüllü stilde web sitesi oluştur](https://x.com/viktoroddy/status/2078140696910037002) (by [@viktoroddy](https://x.com/viktoroddy))

**Sadece son ekran görüntüsü yerine tam kayıtlı oturumu değerlendir**

Viktor Oddy, Kimi K3 ile ödüllü stilde web sitesi oluşturmaya yönelik 13 dakikalık tutorial yayımlayarak sürecin tamamını gösteriyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-78.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-78-poster.jpg" alt="Case 78 source video poster" height="360"></a>

[Play case 78 tutorial video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-78.mp4)

Type: Tutorial | Date: 2026-07-17

---

<a id="case-81"></a>
### Case 81: [Metaball kaydırma ön yüzü oluşturmak](https://x.com/abhinavflac/status/2078603131055993130) (by [@abhinavflac](https://x.com/abhinavflac))

**Kimi K3, parlayan metaball öğeleri ve kaydırmaya bağlı animasyonlarla rafine bir web arayüzü kuruyor.**

Yayınlanan video, görsel efekt, yerleşim ve hareketin tek bir çıktıda birleştiği tamamlanmış dinamik ön yüzü gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-81.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-81-poster.jpg" alt="Case 81 source video poster" height="360"></a>

[Play case 81 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-81.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-82"></a>
### Case 82: [Kişisel siteyi modeller arasında yeniden tasarlamak](https://x.com/fabriciocarraro/status/2078574831466078265) (by [@fabriciocarraro](https://x.com/fabriciocarraro))

**Aynı kişisel site yeniden tasarım görevi Kimi K3 ve diğer modellerle karşılaştırılarak görsel kalite ve yapı farkları gösteriliyor.**

Gönderi birden fazla model çıktısını yan yana veriyor; Kimi K3ün tasarım kararları, bölüm yapısı ve bitiş kalitesi izlenebiliyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-82.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-82-poster.jpg" alt="Case 82 source video poster" height="360"></a>

[Play case 82 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-82.mp4)

Type: Evaluation | Date: 2026-07-18

---

<a id="case-86"></a>
### Case 86: [Etkileşimli saç derisi keşif aracı yapmak](https://x.com/MiaAI_lab/status/2078508824752017757) (by [@MiaAI_lab](https://x.com/MiaAI_lab))

**Kimi K3, eğitim amaçlı insan saç derisi görselleştiricisi üreterek açıklayıcı UI kullanımını gösteriyor.**

Demo, saç derisi yapılarını keşfetmeye yönelik etkileşimli bir ekran sunuyor; tıbbi ve eğitim odaklı anlatım arayüzleri için kanıt sağlıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-86.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-86-poster.jpg" alt="Case 86 source video poster" height="360"></a>

[Play case 86 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-86.mp4)

Type: Demo | Date: 2026-07-18

---

<a id="case-87"></a>
### Case 87: [3D küre panosu promptu paylaşmak](https://x.com/hqmank/status/2078465403349840144) (by [@hqmank](https://x.com/hqmank))

**Açık bir prompt, Kimi K3 ile 3D küre tabanlı pano arayüzü üretme akışını gösteriyor.**

Gönderide referans prompt ve sonuç videosu var; küre, veri gösterimi ve pano yerleşiminin birleşimi izlenebiliyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-87.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-87-poster.jpg" alt="Case 87 source video poster" height="360"></a>

[Play case 87 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-87.mp4)

Type: Tutorial | Date: 2026-07-18

---

<a id="case-94"></a>
### Case 94: [Beş UI UX testi çalıştır](https://x.com/MAXdeg0/status/2078855257686196399) (by [@MAXdeg0](https://x.com/MAXdeg0))

**Kimi K3’ü tek bir frontend ekran görüntüsü yerine UI, logo ve Figma MCP görevleriyle değerlendir.**

MAXdeg0, Claude Code ve Figma MCP server ile Kimi K3 üzerinde beş UI/UX ve logo tasarım testi bildirdi. Kaynak landing page rebuild, hero section rebuild ve marka çalışması gibi görevleri listeliyor; en az landing için somut süre ve maliyet veriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-94.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-94-poster.jpg" alt="Case 94 source video poster" height="360"></a>

[Play case 94 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-94.mp4)

Type: Evaluation | Date: 2026-07-19

---

<a id="case-97"></a>
### Case 97: [Referanslardan landing üret](https://x.com/MAXdeg0/status/2078776969072877715) (by [@MAXdeg0](https://x.com/MAXdeg0))

**Referans panoları, Figma AI ve Motion Sites ile Kimi K3 kullanarak görsel yönü tekrar kullanılabilir landing page bölümlerine çevir.**

MAXdeg0 bir landing page workflow anlatıyor: Pinterest’ten stil referansları almak, görünümü Figma AI ile remix etmek veya UI referansı ve promptu Motion Sites’a vererek Kimi K3’e sayfayı kurdurmak. Gönderi tekniğin başka bölümlerde tekrar kullanılabileceğini ve tam prompting guide bağlantısını belirtiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-97.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-97-poster.jpg" alt="Case 97 source video poster" height="360"></a>

[Play case 97 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-97.mp4)

Type: Tutorial | Date: 2026-07-19

---


<a id="coding-integrations"></a>
## 💻 Kodlama ve entegrasyonlar

<a id="case-18"></a>
### Case 18: [İşlevsel macOS içeren sanal MacBook kur](https://x.com/scottstts/status/2077890054299541890) (by [@scottstts](https://x.com/scottstts))

**Three.js donanım render'ını etkileşimli bir tarayıcı işletim sistemi simülasyonuyla birleştir**

Kaynak, Kimi K3'ün Three.js içinde işlevsel macOS tarzı ortama sahip sanal bir MacBook oluşturduğunu bildiriyor. Eser gösteriliyor ancak uygulama adımları sunulmuyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-18.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-18-poster.jpg" alt="Case 18 source video poster" height="360"></a>

[Play case 18 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-18.mp4)

Type: Demo | Date: 2026-07-16

---

<a id="case-25"></a>
### Case 25: [DSL'den PTX'e GPU derleyicisi geliştir](https://x.com/rohanpaul_ai/status/2077886618657231220) (by [@rohanpaul_ai](https://x.com/rohanpaul_ai))

**DSL, compiler pass'leri, PTX üretimi ve Tensor Core yolunu kapsayan uçtan uca derleyici görevi kullan**

Kaynak, Kimi K3'ün DSL ve pass'lerinden PTX üretimine kadar sıfırdan GPU derleyicisi yaptığını ve Tensor Core yolunu Triton ile karşılaştırdığını bildiriyor. Sağlanan kayıtta bağımsız benchmark ayrıntıları yok

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-25-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-25-01.png" alt="Case 25 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-16

---

<a id="case-32"></a>
### Case 32: [WebGL2'de gerçek zamanlı kara delik raytracer'ı kur](https://x.com/AlicanKiraz0/status/2077885419744612597) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**Tek HTML dosyasında yerel WebGL2 geodesic raytracer'ın tek promptla üretimini dene**

Yazar, yerel WebGL2'de çalışan tek dosyalı kara delik ışık bükülmesi raytracer'ı gerektiren bir coding benchmark tanımlıyor. Kayıt görevi ve katılan modelleri gösteriyor ancak tam bağımsız sonuç denetimi sunmuyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-32.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-32-poster.jpg" alt="Case 32 source video poster" height="360"></a>

[Play case 32 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-32.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-46"></a>
### Case 46: [mGBA WASM çevresinde Game Boy Advance emülatörü kur](https://x.com/teortaxesTex/status/2077925090168062272) (by [@teortaxesTex](https://x.com/teortaxesTex))

**Lisanslı 3D model ve gerçek emülatör çekirdeğini birleştir; ardından arayüz ve oynanışı özyinelemeli olarak geliştir**

Belirtilen Kimi K3 projesi lisanslı AGB-001 modelini uyarlar, mGBA WASM çekirdeğini entegre eder ve arayüz ile oynanışı recursive self-improvement yoluyla geliştirir. Gönderi bağımsız yeniden üretim değil proje açıklaması aktarıyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-46-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-46-01.jpg" alt="Case 46 source image 1" height="360"></a>

Type: Integration | Date: 2026-07-17

---

<a id="case-50"></a>
### Case 50: [Çince kaynaklardan birden çok konuyu araştır](https://x.com/tphuang/status/2077911994607239400) (by [@tphuang](https://x.com/tphuang))

**Model kuşakları arasında kapsamlılık ve gecikmeyi karşılaştırmak için uzun süren araştırma görevleri kullan**

Yazar Kimi K3'ü Çince kaynaklarla birçok araştırma konusunda test ettiğini, K2.6'dan daha kapsamlı ancak daha yavaş bulduğunu bildiriyor. Gönderi o sıradaki yoğun hizmet talebini de belirtiyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-50-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-50-01.png" alt="Case 50 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-17

---

<a id="case-56"></a>
### Case 56: [Çalışan uygulamalarla macOS'u tarayıcıda klonla](https://x.com/twid/status/2077924755357974989) (by [@twid](https://x.com/twid))

**Müzik, tarayıcı ve email uygulamalarını içeren tarayıcı işletim sistemi simülasyonu kur**

Kaynak Kimi K3 ile müzik, tarayıcı, email ve diğer işlevlere sahip tarayıcı tabanlı macOS klonu yapıldığını bildiriyor. Uygulama ayrıntıları sağlanmıyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-56.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-56-poster.jpg" alt="Case 56 source video poster" height="360"></a>

[Play case 56 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-56.mp4)

Type: Demo | Date: 2026-07-17

---

<a id="case-62"></a>
### Case 62: [Çalışan FaceTime içeren macOS simülasyonu kur](https://x.com/LinearUncle/status/2077919552239997078) (by [@LinearUncle](https://x.com/LinearUncle))

**Üretilmiş bir uygulama etkileşiminin çalışıp çalışmadığını sınamak için sanal işletim sistemi görevi kullan**

Üretici Kimi K3'e atfedilen macOS tarzı ortamı gösteriyor ve FaceTime özelliğinin çalıştığını bildiriyor. Kurulum veya doğrulama adımları sunulmuyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-62-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-62-01.jpg" alt="Case 62 source image 1" height="360"></a>

Type: Demo | Date: 2026-07-17

---

<a id="case-64"></a>
### Case 64: [Çift görevli frontend efekt karşılaştırıcısı ekle](https://x.com/MinLiBuilds/status/2077939461510615376) (by [@MinLiBuilds](https://x.com/MinLiBuilds))

**Tamamlanmış iki görevi seçen, yan yana gösteren, görünümleri ve etkileşimleri senkronlayan araç kur**

Üretici Kimi K3'ten görev seçimi, çift tarayıcı paneli, object ve roaming modları, senkron bakış açıları ve etkileşim testleri içeren frontend karşılaştırma workflow'u istediğini bildiriyor. Gönderi daha geniş model sınırlarını da belirtiyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-64.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-64-poster.jpg" alt="Case 64 source video poster" height="360"></a>

[Play case 64 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-64.mp4)

Type: Tutorial | Date: 2026-07-17

---

<a id="case-75"></a>
### Case 75: [Kimi'yi Codex alt ajanı olarak yapılandır](https://x.com/nauczymycieAI/status/2078181182701736132) (by [@nauczymycieAI](https://x.com/nauczymycieAI))

**Orkestrasyonu Codex'te tut, frontend uygulamasını gizli bilgi sınırıyla Kimi K3 OpenCode alt ajanına devret**

nauczymycieAI, OpenCode kurulumu, Kimi API anahtarının Codex'e yapıştırılmadan elle oluşturulması, Kimi K3 bağlantısı ve frontend işleri için global Codex skill adımlarını yayımlıyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-75.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-75.jpg" alt="Case 75 source image 1" height="360"></a>

Type: Tutorial | Date: 2026-07-17

---

<a id="case-79"></a>
### Case 79: [Basit kodlamayı ChatLLM ile yönlendir](https://x.com/abacusai/status/2078022418661257411) (by [@abacusai](https://x.com/abacusai))

**Basit kodlamayı Kimi K3'e gönder, zor kodlama ve tasarımı diğer modellere ayır**

Abacus AI, ChatLLM'de Kimi K3'ü duyuruyor: basit kodlama Kimi K3, zor kodlama Fable 5, tasarım GPT-5.6 Sol. Router ChatLLM, Abacus AI Agent ve Claude Code'da çalışıyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-79.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-79.jpg" alt="Case 79 source image 1" height="360"></a>

Type: Integration | Date: 2026-07-17

---

<a id="case-91"></a>
### Case 91: [Üretilmiş assetlerle CS kur](https://x.com/karankendre/status/2078938615900688728) (by [@karankendre](https://x.com/karankendre))

**Küçük bir Counter-Strike tarzı tarayıcı oyunu prototiplerken oyun kodu için Kimi K3, assetler için GPT Image 2 kullan.**

Karan Kendre, Counter-Strike tarzı bir projede oyunu Kimi K3’ün, assetleri GPT Image 2’nin oluşturduğunu ve toplam maliyetin yaklaşık 10 dolar olduğunu bildiriyor. Kaynak video görünen çıktıdır; bu kayıt Kimi’ye özel benchmark değil, araç birleşimi workflow olarak değerlidir.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-91.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-91-poster.jpg" alt="Case 91 source video poster" height="360"></a>

[Play case 91 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-91.mp4)

Type: Integration | Date: 2026-07-19

---

<a id="case-95"></a>
### Case 95: [Command Code Design skill kullan](https://x.com/MrAhmadAwais/status/2078841789205934547) (by [@MrAhmadAwais](https://x.com/MrAhmadAwais))

**Token bütçesi altında görsel oyun prototipi kurarken Kimi K3’ü Command Code’daki özel design skill ile birleştir.**

Ahmad Awais, Command Code ve /design skill ile Kimi K3 kullanarak Forza tarzı chase-camera oyunu yaptığını bildiriyor. Gönderi oturum maliyetini 0,97 dolar olarak verir ve yol/araba ölçeği, arka plan, animasyon ve sis düzeltmelerini içerir; bu somut bir agent harness workflow’dur.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-95.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-95-poster.jpg" alt="Case 95 source video poster" height="360"></a>

[Play case 95 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-95.mp4)

Type: Integration | Date: 2026-07-19

---


<a id="evaluation-limits"></a>
## 🧪 Değerlendirme ve sınırlar

<a id="case-7"></a>
### Case 7: [BridgeBench lav lambası görevinde frontend tasarımını karşılaştır](https://x.com/bridgemindai/status/2077868061953007908) (by [@bridgemindai](https://x.com/bridgemindai))

**BridgeBench lav lambası görevini evrensel sıralama yerine sınırları belli tek bir frontend tasarım karşılaştırması olarak kullan**

BridgeMind AI, Kimi K3'ün BridgeBench lav lambası görevinde Fable 5'i geçtiğini ve belirtilen arenada birinci olduğunu bildiriyor. Bunlar yayıncının bildirdiği karşılaştırma sonuçlarıdır

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-07.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-07-poster.jpg" alt="Case 7 source video poster" height="360"></a>

[Play case 7 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-07.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-8"></a>
### Case 8: [Editoryal sesle senaryo yazımını ölç](https://x.com/Whats_AI/status/2077860441380798908) (by [@Whats_AI](https://x.com/Whats_AI))

**Açıkça tanımlanmış bir iç benchmark içinde editoryal sese uyumu, göreli sıralamayı ve senaryo başına maliyeti ölç**

Whats_AI ilk iç sonuçlarında 2,840 Elo, kendi tablosunda birincilik ve senaryo başına yaklaşık $0.25 bildiriyor. Bunlar tek bir kuruluşun ön sonuçlarıdır; genel performans veya fiyat garantisi değildir

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-08-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-08-01.jpg" alt="Case 8 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-16

---

<a id="case-10"></a>
### Case 10: [Flappy türü oyunların tasarımını, maliyetini ve zorluğunu karşılaştır](https://x.com/MrAhmadAwais/status/2077915347974557862) (by [@MrAhmadAwais](https://x.com/MrAhmadAwais))

**Üretilen oyunları karşılaştırırken zorluk ayarlarını, maliyeti, tasarımı ve oynanış özelliklerini kaydet**

Command Code'un iç Flappy benchmark'ı modeller arasında farklı zorluk ayarları bildiriyor ve Kimi K3 için $0.024, Fable 5 için $0.42, GPT-5.6 Sol için $0.15 listeliyor. Eşit olmayan ayarlar bu iç karşılaştırmayı sınırlar

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-10.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-10-poster.jpg" alt="Case 10 source video poster" height="360"></a>

[Play case 10 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-10.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-12"></a>
### Case 12: [Oyun tasarımını aynı tasarım promptuyla karşılaştır](https://x.com/CommandCodeAI/status/2077921526213746948) (by [@CommandCodeAI](https://x.com/CommandCodeAI))

**Tasarım promptunu sabit tut; tempo, tasarım anlayışı ve oynanış hissini ayrı ayrı incele**

Command Code, Kimi K3, GPT-5.6 Sol ve Fable 5'i aynı promptla karşılaştırdığını bildiriyor. Gönderiye göre Kimi K3 tasarım anlayışında iyi performans gösterirken diğer ikisi fazla hızlı oynadı; bu yayıncının değerlendirmesidir

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-12.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-12-poster.jpg" alt="Case 12 source video poster" height="360"></a>

[Play case 12 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-12.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-13"></a>
### Case 13: [İstatistiksel denetimde bağımsız inceleme şartı koy](https://x.com/emollick/status/2077869293031624793) (by [@emollick](https://x.com/emollick))

**Bulgulara güvenmeden önce modelin istatistiksel denetimini bağımsız uzman veya başka bir model incelemesiyle eşleştir**

Ethan Mollick, Kimi K3 Max'in önceki akademik çalışmayı denetlerken istatistiği yanlış uyguladığını bildiriyor ve ayrı bir eleştiriye katılıyor. Bu olumsuz örnek, denetlenmemiş kabul yerine bağımsız kontrolü destekliyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-13-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-13-01.jpg" alt="Case 13 source image 1" height="360"></a>

Type: Limit | Date: 2026-07-16

---

<a id="case-16"></a>
### Case 16: [Yavaş ama güçlü bir frontend çalışmasını değerlendir](https://x.com/Lentils80/status/2077387333154857151) (by [@Lentils80](https://x.com/Lentils80))

**Bir frontend görevini test ederken çıktı kalitesiyle birlikte tamamlanma süresini de kaydet**

Üretici bir Kimi K3 frontend çalışmasının 35 dakika sürdüğünü ve çıktının bu prompt için gördüklerinin en iyilerinden biri olduğunu bildiriyor. Hız ve kalite yargıları tek bir kullanıcının gözlemidir

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-16.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-16-poster.jpg" alt="Case 16 source video poster" height="360"></a>

[Play case 16 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-16.mp4)

Type: Evaluation | Date: 2026-07-15

---

<a id="case-20"></a>
### Case 20: [Polisiye yazımını önceden sezdirme hataları açısından dene](https://x.com/emollick/status/2077951790868238616) (by [@emollick](https://x.com/emollick))

**Üretilen bir gizemin ipuçları, kapalılık ve önceden sezdirme arasında denge kurup kurmadığını değerlendir**

Ethan Mollick, Kimi K3'ün iyi bir cinayet gizemi yazamadığını; ipuçlarını hem fazla açık hem fazla kapalı yaptığını ve önceden sezdirmenin başarısız olduğunu bildiriyor. Diğer modellerin de bu sınıra sahip olduğunu ekliyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-01.jpg" alt="Case 20 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-02.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-20-02.png" alt="Case 20 source image 2" height="360"></a>

Type: Limit | Date: 2026-07-17

---

<a id="case-21"></a>
### Case 21: [Millennium Falcon modelleme ve animasyonunu karşılaştır](https://x.com/gmi_cloud/status/2077903360263676090) (by [@gmi_cloud](https://x.com/gmi_cloud))

**3D modelleme, animasyon, süre ve maliyeti karşılaştırmak için eşleşen stil istekleri ve efor ayarları kullan**

GMI Cloud, Kimi K3 ve Fable 5'i maksimum eforla piksel ve özgün tarz Millennium Falcon üretimlerinde karşılaştırdığını bildiriyor. Kimi K3'ün daha uzun sürdüğünü ancak ilk testte yaklaşık üçte bir, diğerinde yarıdan az maliyetli olduğunu söylüyor; bunlar sağlayıcı sonuçlarıdır

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-21.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-21-poster.jpg" alt="Case 21 source video poster" height="360"></a>

[Play case 21 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-21.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-28"></a>
### Case 28: [On Kimi K3 projesinden oluşan koleksiyonu incele](https://x.com/minchoi/status/2077957907857994006) (by [@minchoi](https://x.com/minchoi))

**Ayrı ayrı doğrulanacak somut eserleri keşfetmek için bağlantılı proje derlemesini kullan**

Yazar Game Boy Advance emülatörü dahil medyalı on Kimi K3 örneği derliyor. Bu tek yeniden üretilebilir workflow değil bir koleksiyondur; her bağlantılı örnek bağımsız kontrol edilmelidir

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-28.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-28-poster.jpg" alt="Case 28 source video poster" height="360"></a>

[Play case 28 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-28.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-29"></a>
### Case 29: [Gelişmiş bir landing page'i dört modelde karşılaştır](https://x.com/doutorcaleb/status/2077904020471947773) (by [@doutorcaleb](https://x.com/doutorcaleb))

**Landing page isteğini sabit tut; model çıktılarında animasyon derinliğini ve tamamlanmayı incele**

Üretici aynı gelişmiş landing page promptunu Kimi K3, Fable, Grok ve GPT Terra'ya verdiğini ve Kimi K3'ü en güçlü bulduğunu bildiriyor. Bu, tek görevden öz bildirime dayalı bir karşılaştırmadır

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-29.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-29-poster.jpg" alt="Case 29 source video poster" height="360"></a>

[Play case 29 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-29.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-30"></a>
### Case 30: [Retro oyun mekaniklerini ve maliyetini ölç](https://x.com/adxtyahq/status/2077860500462055570) (by [@adxtyahq](https://x.com/adxtyahq))

**Aynı retro oyun görevlerinde oynanış, fizik, mekanik, özerk davranış, token kullanımı ve maliyeti karşılaştır**

Kaynak Road Fighter, Battle City ve Q*bert için aynı prompt testleri bildiriyor; Kimi K3 için $0.28, GPT-5.6 için $0.28 ve Opus 4.8 için $0.54 listeliyor. Bunlar yayıncının benchmark rakamlarıdır

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-30.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-30-poster.jpg" alt="Case 30 source video poster" height="360"></a>

[Play case 30 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-30.mp4)

Type: Benchmark | Date: 2026-07-16

---

<a id="case-31"></a>
### Case 31: [Oyun üretimini Fable 5 ile karşılaştır](https://x.com/higgsfield_ai/status/2077943629633712490) (by [@higgsfield_ai](https://x.com/higgsfield_ai))

**Yan yana üretilmiş oyun örneğini geniş model hükmü değil dar bir değerlendirme olarak kullan**

Higgsfield, Kimi K3 ile Fable 5 oyun üretimi karşılaştırması sunuyor. Sağlanan kayıt karşılaştırma medyası içeriyor ancak prompt, puanlama rubric'i veya ayrıntılı koşullar içermiyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-31.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-31-poster.jpg" alt="Case 31 source video poster" height="360"></a>

[Play case 31 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-31.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-34"></a>
### Case 34: [Karmaşık frontend ve geliştirme görevlerini Opus 4.8 ile karşılaştır](https://x.com/op7418/status/2077969583018066116) (by [@op7418](https://x.com/op7418))

**Bir modeli evrensel olarak üstün ilan etmek yerine kazanım ve kayıpları görmek için birden çok karmaşık kodlama görevi kullan**

İncelemeci doğrudan Kimi K3 ve Opus 4.8 testleri yaptığını, karmaşık frontend ve geliştirmede karışık sonuçlarla kabaca denk olduklarını bildiriyor. Bu tek bir incelemecinin değerlendirmesidir

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-34.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-34-poster.jpg" alt="Case 34 source video poster" height="360"></a>

[Play case 34 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-34.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-35"></a>
### Case 35: [Benchmark'ları ve landing page testini incele](https://x.com/adamuchigabriel/status/2077880433925120471) (by [@adamuchigabriel](https://x.com/adamuchigabriel))

**İki kanıt türünü ayrı tutarak benchmark bağlamını somut landing page üretim testiyle birleştir**

Video Kimi K3 için benchmark tartışması, landing page testi ve frontend tasarım gözlemleri sunuyor. Sağlanan kayıtta tam test promptu veya puanlama rubric'i yok

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-35.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-35-poster.jpg" alt="Case 35 source video poster" height="360"></a>

[Play case 35 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-35.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-37"></a>
### Case 37: [Grafikten formüle görevlerle tümevarım muhakemesini ölç](https://x.com/s_batzoglou/status/2077884096307454119) (by [@s_batzoglou](https://x.com/s_batzoglou))

**Birinci dereceden tümevarım görevlerinde doğruluk, holdout davranışı ve formül karmaşıklığını ölç**

Yazar, birinci dereceden formül çıkarmak için her biri 8–10 öğeli 6–10 küçük grafik kullanılan ICML INDUCTION görevinde Kimi K3 ve diğer modelleri benchmark ettiğini bildiriyor. Gönderi önceki çalışmanın sonuçlarını güncelliyor; burada yeni bağımsız yeniden üretim iddia edilmiyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-37-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-37-01.png" alt="Case 37 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-16

---

<a id="case-38"></a>
### Case 38: [Bildirilen oyunları, landing page'leri, 3D işleri ve uzun bağlamı incele](https://x.com/servasyy_ai/status/2077903775113834689) (by [@servasyy_ai](https://x.com/servasyy_ai))

**Somut eserleri karşılaştırmak ve hız sınırlarını maliyet iddialarıyla birlikte belirtmek için çok kaynaklı derleme kullan**

Yazar oyunlar, landing page'ler, 3D üretim ve uzun bağlam çalışmalarına ilişkin Kimi K3 testlerini özetliyor ve denemeye değer olduğunu ancak henüz Fable 5'in yerini tutmadığını söylüyor. Tüm rakamlar bu derlemedeki ikincil bildirimlerdir

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-38-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-38-01.jpg" alt="Case 38 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-40"></a>
### Case 40: [Karmaşık bir planı denetle ve çözümlerine itiraz et](https://x.com/doodlestein/status/2077901883637665958) (by [@doodlestein](https://x.com/doodlestein))

**Hafife alınmış bulguları, yanlış çözümleri ve reddedilmesi gereken sonuçları bulmak için ikinci model kullan**

Üretici Kimi K3'ün yoğun biçimde iyileştirilmiş bir planı incelediğini; ağır sorunların hafife alındığını, önerilen çözümlerin yaklaşık üçte birinin düzeltilmesi gerektiğini ve bir bulgunun çürütüldüğünü bildiriyor. Bunlar o denetime özgü sonuçlardır

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-40-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-40-01.jpg" alt="Case 40 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-41"></a>
### Case 41: [PPO tarzı reinforcement-learning ASCII diyagramlarını karşılaştır](https://x.com/dejavucoder/status/2077872015856615541) (by [@dejavucoder](https://x.com/dejavucoder))

**ASCII diyagram promptunu sabit tut ve modellerin reinforcement-learning döngüsünü nasıl temsil ettiğini karşılaştır**

Kaynak PPO tarzı reinforcement-learning döngüsünü ASCII olarak çizme promptunu veriyor ve Kimi K3 Max'i Fable 5 High yanında gösteriyor. Yargı, tek görevin görsel karşılaştırması olarak kalır

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-01.png" alt="Case 41 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-41-02.jpg" alt="Case 41 source image 2" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-42"></a>
### Case 42: [Kapasite hatalarını izleyerek Blender'da modelle](https://x.com/Angaisb_/status/2077910845523214668) (by [@Angaisb_](https://x.com/Angaisb_))

**Yalnız eseri değil hizmet güvenilirliğini de değerlendirerek kısmi Blender ilerlemesini incele**

Üretici Kimi K3'ün Blender modelleme ilerlemesini gösteriyor ve tekrarlanan kapasite hataları bildiriyor. Sağlanan kaynakta iş tamamlanmamış; kısmi sonuç ve güvenilirlik sınırı birlikte ele alınmalıdır

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-42-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-42-01.jpg" alt="Case 42 source image 1" height="360"></a>

Type: Limit | Date: 2026-07-17

---

<a id="case-47"></a>
### Case 47: [Bir arenada Flappy Bird üretimini karşılaştır](https://x.com/jun_song/status/2077396996865003739) (by [@jun_song](https://x.com/jun_song))

**İki Flappy Bird sonucunu karşılaştırmak için arena görevi kullan ve yargıyı göreve özgü tut**

Üretici bir Flappy Bird görevinde Kimi K3 ve Opus 4.8 Arena karşılaştırması bildiriyor ve Kimi K3'ü belirgin biçimde daha iyi buluyor. Kayıtta tam prompt veya rubric yok

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-47.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-47-poster.jpg" alt="Case 47 source video poster" height="360"></a>

[Play case 47 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-47.mp4)

Type: Evaluation | Date: 2026-07-15

---

<a id="case-52"></a>
### Case 52: [Bir araçla Bongard görsel tümevarım problemini çöz](https://x.com/IntuitMachine/status/2077885406528311561) (by [@IntuitMachine](https://x.com/IntuitMachine))

**Bongard muhakeme görevinde araç kullanımının görsel kuralı çıkarmaya yardım edip etmediğini dene**

Üretici Kimi K3'ün aynı karşılaştırmada Grok 4.5 ve Muse Spark 1.1'in çözemediği Bongard problemini araç kullanarak çözdüğünü bildiriyor. Bu tek kullanıcı görevi sonucudur, genel muhakeme benchmark'ı değildir

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-52-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-52-01.jpg" alt="Case 52 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-07-16

---

<a id="case-53"></a>
### Case 53: [Frontend zevkini ve 3D tasarımı GPT-5.6 Sol ile karşılaştır](https://x.com/filicroval/status/2077736407506751952) (by [@filicroval](https://x.com/filicroval))

**Sınırları belli frontend karşılaştırmasında özellikleri, görsel zevki, zarafeti ve 3D uygulamayı incele**

Üretici Kimi K3 ve GPT-5.6 Sol'u frontend tasarımında karşılaştırıyor; Kimi K3'ü görsel zevk, zarafet ve 3D yeteneğinde daha güçlü buluyor. Değerlendirme öznel ve göreve özgüdür

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-53.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-53-poster.jpg" alt="Case 53 source video poster" height="360"></a>

[Play case 53 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-53.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-57"></a>
### Case 57: [Web sitesi üretimini üç model arasında karşılaştır](https://x.com/pengchujin/status/2077962916226298340) (by [@pengchujin](https://x.com/pengchujin))

**Tek testte Kimi K3, Fable 5 ve GPT-5.6 Sol'u karşılaştırmak için görünür web sitesi çıktılarını kullan**

Üretici Kimi K3, Fable 5 ve GPT-5.6 Sol arasında web sitesi üretimi karşılaştırması sunuyor. Sağlanan kayıt eksiksiz promptu veya puanlama rubric'ini göstermiyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-57.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-57-poster.jpg" alt="Case 57 source video poster" height="360"></a>

[Play case 57 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-57.mp4)

Type: Evaluation | Date: 2026-07-17

---

<a id="case-59"></a>
### Case 59: [Prosedürel 3D oyun üretimini ve maliyeti karşılaştır](https://x.com/adxtyahq/status/2077958193511362856) (by [@adxtyahq](https://x.com/adxtyahq))

**Promptu modeller arasında sabit tut; üretilen rulet, slot makinesi ve pinball sistemlerini çalışma başına maliyetle incele**

Yayıncı çok modelli prosedürel 3D oyun karşılaştırması bildiriyor ve Kimi K3 için $0.71, Grok 4.5 için $0.30 dahil maliyetler listeliyor. Tüm sıralama ve maliyetler o yayıncının çalışmasına aittir

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-59.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-59-poster.jpg" alt="Case 59 source video poster" height="360"></a>

[Play case 59 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-59.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-69"></a>
### Case 69: [3D cephanelik sahnesinin ayrıntı ve ışığını karşılaştır](https://x.com/hakki_alkan/status/2077887013332636032) (by [@hakki_alkan](https://x.com/hakki_alkan))

**Sınırları belli Kimi K3 ve Opus 4.8 karşılaştırmasında nesne yoğunluğu, aydınlatma ve sahne ayrıntısını incele**

Kaynak Kimi K3'ün dolu raflar, kutular ve gerçekçi aydınlatmayla ayrıntılı cephanelik sahnesi; Opus 4.8'in ise seyrek bir oda ürettiğini bildiriyor. Bu üçüncü taraf karşılaştırma raporudur, bağımsız benchmark değildir

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-69-poster.jpg" alt="Case 69 source video poster" height="360"></a>

[Play case 69 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-69.mp4)

Type: Evaluation | Date: 2026-07-16

---

<a id="case-72"></a>
### Case 72: [Aynı Arena promptlarıyla frontendleri karşılaştır](https://x.com/arena/status/2078240399517524365) (by [@arena](https://x.com/arena))

**Tek bir sıralama puanı yerine aynı promptları ve yan yana çıktıları kullan**

Arena.ai, Kimi K3 ile Fable 5'i aynı promptlarla karşılaştıran Frontend Code Arena videosu yayımladı. Video iki çıktıyı aynı koşulda koruyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-72.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-72-poster.jpg" alt="Case 72 source video poster" height="360"></a>

[Play case 72 comparison video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-72.mp4)

Type: Benchmark | Date: 2026-07-17

---

<a id="case-74"></a>
### Case 74: [Kimi Code'u kodlama ajanlarında değerlendir](https://x.com/ArtificialAnlys/status/2078230240766345330) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Kimi K3'ü birden fazla test ve görev maliyetiyle değerlendir; tek frontend sıralamasını genelleme**

Artificial Analysis 57 puan ve ortak beşincilik; Terminal-Bench v2'de %84, DeepSWE'de %64, SWE-Atlas-QnA'da %23 ve görev başına 3,18 dolar bildiriyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-74.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-74.jpg" alt="Case 74 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-17

---

<a id="case-76"></a>
### Case 76: [Arena ve onarım testini karşılaştır](https://x.com/AlphaSignalAI/status/2078172629496746183) (by [@AlphaSignalAI](https://x.com/AlphaSignalAI))

**Kimi K3 birinde birinci, diğerinde yedinci olabildiği için frontend tercihi ve depo onarımını birlikte incele**

AlphaSignal Frontend Code Arena'da 1679 puanla birincilik, ancak kodlama ajanı onarım testinde 67 denemede 53 başarı, %79 ve yedincilik bildiriyor

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-76.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/cases/case-76.jpg" alt="Case 76 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-17

---

<a id="case-80"></a>
### Case 80: [Kimi K3ü Prinzbench ile ölçmek](https://x.com/deredleritt3r/status/2078606700496773166) (by [@deredleritt3r](https://x.com/deredleritt3r))

**Prinzbench, Kimi K3ü OpenAI o3 ve diğer modellerle aynı değerlendirme tablosunda karşılaştırarak sırasını ve sınırlarını gösteriyor.**

Gönderi Kimi K3ü Prinzbench tablosuna ekliyor; üst modellerle farkı ve değerlendirme görevlerindeki göreli güçlü yanları görünür kılıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-80-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-80-01.png" alt="Case 80 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-07-18

---

<a id="case-85"></a>
### Case 85: [ISS dijital ikiz üretimini karşılaştırmak](https://x.com/AIsaOneHQ/status/2078519527588200536) (by [@AIsaOneHQ](https://x.com/AIsaOneHQ))

**Kimi K3, ISS dijital ikiz görevi üzerinde diğer modellerle karşılaştırılarak karmaşık 3D görselleştirmedeki farkları gösteriyor.**

Gönderi aynı ISS görevi için birden fazla sonucu kıyaslıyor; Kimi K3ün yapısal anlayışı ve görsel sınırları değerlendirilebiliyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-85.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-85-poster.jpg" alt="Case 85 source video poster" height="360"></a>

[Play case 85 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-85.mp4)

Type: Benchmark | Date: 2026-07-18

---

<a id="case-89"></a>
### Case 89: [WebGPU orman dünyasını değerlendirmek](https://x.com/stas_sorokin_/status/2078435840728908093) (by [@stas_sorokin_](https://x.com/stas_sorokin_))

**Kimi K3 ile oluşturulan WebGPU orman dünyası, etkileyici 3D sahne kalitesi ve sınırları açısından değerlendiriliyor.**

Video tarayıcıda çalışan bir orman ortamını gösteriyor ve Kimi K3ün WebGPU/3D sahne üretimini değerlendirmek için kanıt sağlıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-89.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-89-poster.jpg" alt="Case 89 source video poster" height="360"></a>

[Play case 89 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-89.mp4)

Type: Evaluation | Date: 2026-07-18

---

<a id="case-90"></a>
### Case 90: [Cam ev promptlarını karşılaştır](https://x.com/RoundtableSpace/status/2079004612070416755) (by [@RoundtableSpace](https://x.com/RoundtableSpace))

**Aynı mimari sahne promptuyla Kimi K3 ve Opus 4.8’i atmosfer, ışık ve mekansal bütünlük açısından karşılaştır.**

Roundtable Space, benzer fiyatla Kimi K3 ve Claude Opus 4.8 arasında aynı prompt karşılaştırması bildiriyor. Kimi sonucu mavi saat cam ev, sıcak iç ışık, yansıtıcı havuz ve plan detaylarıyla anlatılırken Opus daha tipografik ve mekansal olarak daha eksik görülüyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-90.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-90-poster.jpg" alt="Case 90 source video poster" height="360"></a>

[Play case 90 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-90.mp4)

Type: Evaluation | Date: 2026-07-20

---

<a id="case-92"></a>
### Case 92: [Voxel futbol golünü ölç](https://x.com/0xzynex/status/2078920667542487230) (by [@0xzynex](https://x.com/0xzynex))

**Aynı saf HTML/CSS/JS futbol animasyonu promptunu iki modelde çalıştırarak hareket kalitesini ve maliyeti karşılaştır.**

0xzynex, Kimi K3 ve GPT-5.6 Sol High’ın blok tarzı futbol driblingi, gol, dinamik kamera ve kutlamayı tarayıcı koduyla üretmesini isteyen tek denemelik bir karşılaştırma bildiriyor. Gönderi Kimi’nin daha akıcı hareket ve daha düşük maliyet verdiğini, videonun da çıktıyı koruduğunu söylüyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-92.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-92-poster.jpg" alt="Case 92 source video poster" height="360"></a>

[Play case 92 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-92.mp4)

Type: Benchmark | Date: 2026-07-19

---

<a id="case-93"></a>
### Case 93: [Minecraft benchmark incele](https://x.com/ashen_one/status/2078892418976666071) (by [@ashen_one](https://x.com/ashen_one))

**Lansman hype’ını veya fiyatı yeterli kanıt saymadan önce yapılandırılmış bir Minecraft incelemesi izle.**

ashen_one, Kimi K3 için hype-gerçeklik, benchmarklar, fiyatlandırma, Minecraft testi, ilk çalıştırma hataları ve son karar bölümleri olan kayıtlı bir inceleme yayımlıyor. Kaynak, benchmark çerçevesi ve erken güvenilirlik notlarını tek denetlenebilir videoda topluyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-93.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-93-poster.jpg" alt="Case 93 source video poster" height="360"></a>

[Play case 93 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-93.mp4)

Type: Benchmark | Date: 2026-07-19

---

<a id="case-98"></a>
### Case 98: [API tier limitlerini ölç](https://x.com/mnmn94253156337/status/2078739859154620497) (by [@mnmn94253156337](https://x.com/mnmn94253156337))

**Kimi K3 agent run planını yalnızca model fiyatına değil token, tier, TPM ve TPD sınırlarına göre yap.**

Çince kaynak, Kimi K3 API’ye 5 dolar yükledikten sonra kurulumda yaklaşık 1,1 dolar harcandığını ve ardından Tier0 limitine takıldığını anlatan kişisel bir deneme raporu sunuyor. Input, cached input, output fiyatları ve TPM/TPD kavramlarıyla erken bir limit vakasıdır.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-98.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-98-poster.jpg" alt="Case 98 source video poster" height="360"></a>

[Play case 98 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-98.mp4)

Type: Limit | Date: 2026-07-19

---

<a id="case-99"></a>
### Case 99: [Limbo tarzı demo karşılaştır](https://x.com/ChrisGPT/status/2078679211116835017) (by [@ChrisGPT](https://x.com/ChrisGPT))

**Aynı oyun prototipinde Kimi K3 ile Fable 5’i oynanabilir kapsam, görsel polish, maliyet ve bug açısından karşılaştır.**

ChrisGPT, Limbo clone demo üzerinde Fable 5 ve Kimi K3’ü karşılaştırıyor. Gönderi Fable için 2.400 satır, 24K output token ve 1,20 dolar; Kimi için 3.000 satır, 30K token ve 0,12 dolar bildiriyor. Kimi daha fazla gameplay ekliyor ama daha fazla bug da taşıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-99.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-99-poster.jpg" alt="Case 99 source video poster" height="360"></a>

[Play case 99 demo video](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-kimi-k3-usecases/media/source-cases/case-99.mp4)

Type: Benchmark | Date: 2026-07-19

---

<a id="related-resources"></a>
## İlgili kaynaklar

- [EvoLink’te Kimi K3 ayrıntılarını ve fiyatlarını gör](https://evolink.ai/kimi-k3?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=landing_overview)
- [EvoLink Kimi K3 API belgelerini aç](https://docs.evolink.ai/en/api-manual/language-series/kimi-k3/kimi-k3-chat?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-usecases&utm_content=docs_link)
- [EvoLink’te Kimi K3 hakkında daha fazla bilgi](https://evolink.ai/blog/is-kimi-k3-available-on-evolink?utm_source=github&utm_medium=readme&utm_campaign=awesome-kimi-k3-usecases&utm_content=related_article)
- [KimiK3.io](https://kimik3.io/)
- EvoLink model sayfası ve API belgeleri doğrulandı; kurulabilir Kimi K3 skill doğrulanmadı

<a id="acknowledge"></a>
## 🙏 Teşekkürler

Kimi K3 çalışmalarını kamuya açık paylaşan herkese teşekkür ederiz

[@ivanfioravanti](https://x.com/ivanfioravanti), [@TheAhmadOsman](https://x.com/TheAhmadOsman), [@HarshithLucky3](https://x.com/HarshithLucky3), [@chetaslua](https://x.com/chetaslua), [@abhinavflac](https://x.com/abhinavflac), [@bridgemindai](https://x.com/bridgemindai), [@Whats_AI](https://x.com/Whats_AI), [@chongdashu](https://x.com/chongdashu), [@MrAhmadAwais](https://x.com/MrAhmadAwais), [@bijanbowen](https://x.com/bijanbowen), [@CommandCodeAI](https://x.com/CommandCodeAI), [@emollick](https://x.com/emollick), [@nicky_sap](https://x.com/nicky_sap), [@Lentils80](https://x.com/Lentils80), [@scottstts](https://x.com/scottstts), [@aisearchio](https://x.com/aisearchio), [@gmi_cloud](https://x.com/gmi_cloud), [@karminski3](https://x.com/karminski3), [@VORTEX_Promos](https://x.com/VORTEX_Promos), [@rohanpaul_ai](https://x.com/rohanpaul_ai), [@mirochill](https://x.com/mirochill), [@aimlapi](https://x.com/aimlapi), [@minchoi](https://x.com/minchoi), [@doutorcaleb](https://x.com/doutorcaleb), [@adxtyahq](https://x.com/adxtyahq), [@higgsfield_ai](https://x.com/higgsfield_ai), [@AlicanKiraz0](https://x.com/AlicanKiraz0), [@1littlecoder](https://x.com/1littlecoder), [@op7418](https://x.com/op7418), [@adamuchigabriel](https://x.com/adamuchigabriel), [@s_batzoglou](https://x.com/s_batzoglou), [@servasyy_ai](https://x.com/servasyy_ai), [@filicroval](https://x.com/filicroval), [@doodlestein](https://x.com/doodlestein), [@dejavucoder](https://x.com/dejavucoder), [@Angaisb_](https://x.com/Angaisb_), [@AngryTomtweets](https://x.com/AngryTomtweets), [@Alezander907](https://x.com/Alezander907), [@teortaxesTex](https://x.com/teortaxesTex), [@jun_song](https://x.com/jun_song), [@ridark_eth](https://x.com/ridark_eth), [@naymur_dev](https://x.com/naymur_dev), [@tphuang](https://x.com/tphuang), [@TokenGremlin](https://x.com/TokenGremlin), [@IntuitMachine](https://x.com/IntuitMachine), [@wangfeng0315](https://x.com/wangfeng0315), [@twid](https://x.com/twid), [@pengchujin](https://x.com/pengchujin), [@aayushman2703](https://x.com/aayushman2703), [@goncalo_canhoto](https://x.com/goncalo_canhoto), [@LinearUncle](https://x.com/LinearUncle), [@gagarot200](https://x.com/gagarot200), [@MinLiBuilds](https://x.com/MinLiBuilds), [@izutorishima](https://x.com/izutorishima), [@X2worldtech](https://x.com/X2worldtech), [@Satvik_Pen](https://x.com/Satvik_Pen), [@hakki_alkan](https://x.com/hakki_alkan), [@BrianMRey](https://x.com/BrianMRey), [@ChrisGPT](https://x.com/ChrisGPT), [@arena](https://x.com/arena), [@MathiasHeide](https://x.com/MathiasHeide), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@nauczymycieAI](https://x.com/nauczymycieAI), [@AlphaSignalAI](https://x.com/AlphaSignalAI), [@Ananth7e](https://x.com/Ananth7e), [@viktoroddy](https://x.com/viktoroddy), [@abacusai](https://x.com/abacusai), [@deredleritt3r](https://x.com/deredleritt3r), [@fabriciocarraro](https://x.com/fabriciocarraro), [@startracker](https://x.com/startracker), [@mattwatkajtys](https://x.com/mattwatkajtys), [@AIsaOneHQ](https://x.com/AIsaOneHQ), [@MiaAI_lab](https://x.com/MiaAI_lab), [@hqmank](https://x.com/hqmank), [@prasenx](https://x.com/prasenx), [@stas_sorokin_](https://x.com/stas_sorokin_), [@RoundtableSpace](https://x.com/RoundtableSpace), [@karankendre](https://x.com/karankendre), [@0xzynex](https://x.com/0xzynex), [@ashen_one](https://x.com/ashen_one), [@MAXdeg0](https://x.com/MAXdeg0), [@ice_bearcute](https://x.com/ice_bearcute), [@mnmn94253156337](https://x.com/mnmn94253156337)

*Atıf veya metin düzeltmesi için kamuya açık kaynakla bir issue açın*
