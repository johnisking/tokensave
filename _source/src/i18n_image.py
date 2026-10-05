# Strings for the AI image cost calculator page (tokensave.app/image).
# Shared labels (badge, res, model, total, na, cheapest, srcOfficial, srcRunway, f2) are reused from V in i18n_video.py.

I = {}

I["en"] = dict(
  navImage="Image Cost",
  title="AI Image Cost Calculator – Nano Banana, GPT Image, FLUX, Grok Prices | TokenSave",
  desc="Compare the API cost per image of Nano Banana 2, Nano Banana Pro, GPT Image 2.5, FLUX.2, Grok Imagine, Seedream and Runway. Pick a resolution and count to see the total instantly.",
  h1="AI Image Cost Calculator",
  sub="See what the same images cost on every major AI image model.",
  count="Number of images", perImg="Per image",
  notes="Prices are per generated image. Reference-image fees, taxes and volume discounts are not included.",
  q1="How is AI image generation priced?", a1="Most image APIs charge a fixed price per image that rises with resolution. OpenAI models also charge more for higher quality settings, and FLUX bills by megapixel.",
  q2="What is the cheapest AI image model?", a2="Small models such as FLUX.2 [klein], Grok Imagine and GPT Image at low quality cost around $0.01–0.02 per image. Premium models at 4K can cost $0.15–0.40 per image.",
  q3="What is Nano Banana?", a3="Nano Banana is the nickname for Google's Gemini image models. Nano Banana 2 is Gemini 3.1 Flash Image and Nano Banana Pro is Gemini 3 Pro Image.",
  f1="Official list prices from each provider's API pricing page, checked October 5, 2026. OpenAI and Nano Banana Pro are shown at Runway API rates.",
)

I["ko"] = dict(
  navImage="이미지 비용",
  title="AI 이미지 생성 비용 계산기 – 나노바나나, GPT Image, FLUX, Grok 가격 비교 | TokenSave",
  desc="나노바나나 2, 나노바나나 프로, GPT Image 2.5, FLUX.2, Grok Imagine, Seedream, Runway의 이미지 1장당 API 비용을 비교하세요. 해상도와 장수를 정하면 합계가 바로 나옵니다.",
  h1="AI 이미지 생성 비용 계산기",
  sub="같은 이미지를 모델별로 만들면 얼마인지 한눈에 비교하세요.",
  count="이미지 수", perImg="장당",
  notes="가격은 생성된 이미지 1장 기준입니다. 참조 이미지 요금, 세금, 대량 할인은 포함되지 않습니다.",
  q1="AI 이미지는 어떻게 과금되나요?", a1="대부분의 이미지 API는 장당 고정 가격을 받고, 해상도가 높을수록 비싸집니다. OpenAI 모델은 품질 설정이 높을수록 더 비싸고, FLUX는 메가픽셀 단위로 과금합니다.",
  q2="가장 싼 AI 이미지 모델은?", a2="FLUX.2 [klein], Grok Imagine, 낮은 품질의 GPT Image 같은 모델은 장당 약 $0.01–0.02입니다. 고급 모델로 4K를 만들면 장당 $0.15–0.40까지 들 수 있습니다.",
  q3="나노바나나가 뭔가요?", a3="나노바나나는 구글 Gemini 이미지 모델의 별명입니다. 나노바나나 2는 Gemini 3.1 Flash Image, 나노바나나 프로는 Gemini 3 Pro Image입니다.",
  f1="각 회사 API 요금 페이지의 공식 가격이며 2026년 10월 5일에 확인했습니다. OpenAI와 나노바나나 프로는 Runway API 가격으로 표시합니다.",
)

I["ja"] = dict(
  navImage="画像コスト",
  title="AI画像生成コスト計算ツール – Nano Banana・GPT Image・FLUX・Grokの料金比較 | TokenSave",
  desc="Nano Banana 2、Nano Banana Pro、GPT Image 2.5、FLUX.2、Grok Imagine、Seedream、Runwayの1枚あたりのAPI料金を比較。解像度と枚数を選ぶと合計がすぐにわかります。",
  h1="AI画像生成コスト計算ツール",
  sub="同じ画像を各モデルで作るといくらかかるか一目で比較。",
  count="画像の枚数", perImg="1枚あたり",
  notes="料金は生成画像1枚あたりです。参照画像の料金、税金、ボリュームディスカウントは含まれません。",
  q1="AI画像生成の料金体系は？", a1="多くの画像APIは1枚ごとの固定料金で、解像度が上がるほど高くなります。OpenAIのモデルは品質設定が高いほど高く、FLUXはメガピクセル単位で課金されます。",
  q2="いちばん安いAI画像モデルは？", a2="FLUX.2 [klein]、Grok Imagine、低品質のGPT Imageなどは1枚あたり約$0.01〜0.02です。上位モデルで4Kを作ると1枚$0.15〜0.40かかることもあります。",
  q3="Nano Bananaとは？", a3="Nano BananaはGoogleのGemini画像モデルの愛称です。Nano Banana 2はGemini 3.1 Flash Image、Nano Banana ProはGemini 3 Pro Imageです。",
  f1="各社API料金ページの公式価格（2026年10月5日確認）。OpenAIとNano Banana ProはRunway APIの料金で表示しています。",
)

I["zh-CN"] = dict(
  navImage="图片费用",
  title="AI 图片生成费用计算器 – Nano Banana、GPT Image、FLUX、Grok 价格对比 | TokenSave",
  desc="对比 Nano Banana 2、Nano Banana Pro、GPT Image 2.5、FLUX.2、Grok Imagine、Seedream 和 Runway 每张图片的 API 费用。选择分辨率和数量，立即看到总价。",
  h1="AI 图片生成费用计算器",
  sub="一眼看清同样的图片在各大 AI 图片模型上要花多少钱。",
  count="图片数量", perImg="每张",
  notes="价格按每张生成图片计算，不含参考图费用、税费和批量折扣。",
  q1="AI 图片生成如何计费？", a1="多数图片 API 按张收取固定费用，分辨率越高越贵。OpenAI 模型的质量设置越高越贵，FLUX 则按百万像素计费。",
  q2="最便宜的 AI 图片模型是哪个？", a2="FLUX.2 [klein]、Grok Imagine 和低质量档的 GPT Image 每张约 $0.01–0.02。高端模型生成 4K 图片每张可能要 $0.15–0.40。",
  q3="Nano Banana 是什么？", a3="Nano Banana 是 Google Gemini 图片模型的昵称。Nano Banana 2 即 Gemini 3.1 Flash Image，Nano Banana Pro 即 Gemini 3 Pro Image。",
  f1="价格来自各家 API 定价页的官方标价，于 2026 年 10 月 5 日核对。OpenAI 和 Nano Banana Pro 按 Runway API 价格显示。",
)

I["zh-TW"] = dict(
  navImage="圖片費用",
  title="AI 圖片生成費用計算器 – Nano Banana、GPT Image、FLUX、Grok 價格比較 | TokenSave",
  desc="比較 Nano Banana 2、Nano Banana Pro、GPT Image 2.5、FLUX.2、Grok Imagine、Seedream 與 Runway 每張圖片的 API 費用。選擇解析度與數量，立即看到總價。",
  h1="AI 圖片生成費用計算器",
  sub="一眼看清同樣的圖片在各大 AI 圖片模型上要花多少錢。",
  count="圖片數量", perImg="每張",
  notes="價格以每張生成圖片計算，不含參考圖費用、稅金與大量折扣。",
  q1="AI 圖片生成如何計費？", a1="多數圖片 API 按張收取固定費用，解析度越高越貴。OpenAI 模型的品質設定越高越貴，FLUX 則以百萬像素計費。",
  q2="最便宜的 AI 圖片模型是哪個？", a2="FLUX.2 [klein]、Grok Imagine 與低品質檔的 GPT Image 每張約 $0.01–0.02。高階模型生成 4K 圖片每張可能要 $0.15–0.40。",
  q3="Nano Banana 是什麼？", a3="Nano Banana 是 Google Gemini 圖片模型的暱稱。Nano Banana 2 即 Gemini 3.1 Flash Image，Nano Banana Pro 即 Gemini 3 Pro Image。",
  f1="價格來自各家 API 定價頁的官方牌價，於 2026 年 10 月 5 日核對。OpenAI 與 Nano Banana Pro 以 Runway API 價格顯示。",
)

I["es"] = dict(
  navImage="Coste de imagen",
  title="Calculadora de coste de imágenes IA – Precios de Nano Banana, GPT Image, FLUX y Grok | TokenSave",
  desc="Compara el coste por imagen en la API de Nano Banana 2, Nano Banana Pro, GPT Image 2.5, FLUX.2, Grok Imagine, Seedream y Runway. Elige resolución y cantidad y ve el total al instante.",
  h1="Calculadora de coste de imágenes IA",
  sub="Mira cuánto cuestan las mismas imágenes en cada gran modelo de imagen IA.",
  count="Número de imágenes", perImg="Por imagen",
  notes="Precios por imagen generada. No incluyen tarifas de imágenes de referencia, impuestos ni descuentos por volumen.",
  q1="¿Cómo se cobra la generación de imágenes con IA?", a1="La mayoría de las API cobran un precio fijo por imagen que sube con la resolución. Los modelos de OpenAI cobran más en calidades altas y FLUX factura por megapíxel.",
  q2="¿Cuál es el modelo de imagen IA más barato?", a2="Modelos pequeños como FLUX.2 [klein], Grok Imagine o GPT Image en calidad baja cuestan unos $0,01–0,02 por imagen. Los modelos premium en 4K pueden costar $0,15–0,40 por imagen.",
  q3="¿Qué es Nano Banana?", a3="Nano Banana es el apodo de los modelos de imagen Gemini de Google. Nano Banana 2 es Gemini 3.1 Flash Image y Nano Banana Pro es Gemini 3 Pro Image.",
  f1="Precios oficiales de la página de precios de la API de cada proveedor, revisados el 5 de octubre de 2026. OpenAI y Nano Banana Pro se muestran con tarifas de la API de Runway.",
)

I["pt"] = dict(
  navImage="Custo de imagem",
  title="Calculadora de custo de imagens com IA – Preços de Nano Banana, GPT Image, FLUX e Grok | TokenSave",
  desc="Compare o custo por imagem na API do Nano Banana 2, Nano Banana Pro, GPT Image 2.5, FLUX.2, Grok Imagine, Seedream e Runway. Escolha a resolução e a quantidade e veja o total na hora.",
  h1="Calculadora de custo de imagens com IA",
  sub="Veja quanto as mesmas imagens custam em cada grande modelo de imagem com IA.",
  count="Número de imagens", perImg="Por imagem",
  notes="Preços por imagem gerada. Não incluem taxas de imagens de referência, impostos nem descontos por volume.",
  q1="Como é cobrada a geração de imagens com IA?", a1="A maioria das APIs cobra um preço fixo por imagem que aumenta com a resolução. Os modelos da OpenAI cobram mais em qualidades altas, e o FLUX cobra por megapixel.",
  q2="Qual é o modelo de imagem com IA mais barato?", a2="Modelos pequenos como FLUX.2 [klein], Grok Imagine e GPT Image em qualidade baixa custam cerca de $0,01–0,02 por imagem. Modelos premium em 4K podem custar $0,15–0,40 por imagem.",
  q3="O que é Nano Banana?", a3="Nano Banana é o apelido dos modelos de imagem Gemini do Google. Nano Banana 2 é o Gemini 3.1 Flash Image e Nano Banana Pro é o Gemini 3 Pro Image.",
  f1="Preços oficiais da página de preços da API de cada fornecedor, verificados em 5 de outubro de 2026. OpenAI e Nano Banana Pro aparecem com tarifas da API da Runway.",
)

I["fr"] = dict(
  navImage="Coût image",
  title="Calculateur de coût d'images IA – Prix Nano Banana, GPT Image, FLUX, Grok | TokenSave",
  desc="Comparez le coût par image via API de Nano Banana 2, Nano Banana Pro, GPT Image 2.5, FLUX.2, Grok Imagine, Seedream et Runway. Choisissez la résolution et le nombre pour voir le total instantanément.",
  h1="Calculateur de coût d'images IA",
  sub="Voyez ce que coûtent les mêmes images sur chaque grand modèle d'image IA.",
  count="Nombre d'images", perImg="Par image",
  notes="Prix par image générée. Frais d'images de référence, taxes et remises sur volume non inclus.",
  q1="Comment la génération d'images IA est-elle facturée ?", a1="La plupart des API facturent un prix fixe par image qui augmente avec la résolution. Les modèles OpenAI coûtent plus cher en qualité élevée, et FLUX facture au mégapixel.",
  q2="Quel est le modèle d'image IA le moins cher ?", a2="Les petits modèles comme FLUX.2 [klein], Grok Imagine ou GPT Image en qualité basse coûtent environ 0,01–0,02 $ par image. Les modèles premium en 4K peuvent coûter 0,15–0,40 $ par image.",
  q3="Qu'est-ce que Nano Banana ?", a3="Nano Banana est le surnom des modèles d'image Gemini de Google. Nano Banana 2 correspond à Gemini 3.1 Flash Image et Nano Banana Pro à Gemini 3 Pro Image.",
  f1="Prix officiels issus de la page tarifaire API de chaque fournisseur, vérifiés le 5 octobre 2026. OpenAI et Nano Banana Pro sont affichés aux tarifs de l'API Runway.",
)

I["de"] = dict(
  navImage="Bildkosten",
  title="KI-Bildkostenrechner – Preise für Nano Banana, GPT Image, FLUX, Grok | TokenSave",
  desc="Vergleiche die API-Kosten pro Bild von Nano Banana 2, Nano Banana Pro, GPT Image 2.5, FLUX.2, Grok Imagine, Seedream und Runway. Auflösung und Anzahl wählen und sofort die Summe sehen.",
  h1="KI-Bildkostenrechner",
  sub="Sieh auf einen Blick, was dieselben Bilder bei jedem großen KI-Bildmodell kosten.",
  count="Anzahl der Bilder", perImg="Pro Bild",
  notes="Preise pro erzeugtem Bild. Gebühren für Referenzbilder, Steuern und Mengenrabatte sind nicht enthalten.",
  q1="Wie wird KI-Bildgenerierung abgerechnet?", a1="Die meisten Bild-APIs berechnen einen festen Preis pro Bild, der mit der Auflösung steigt. OpenAI-Modelle kosten bei höherer Qualität mehr, FLUX rechnet pro Megapixel ab.",
  q2="Welches KI-Bildmodell ist am günstigsten?", a2="Kleine Modelle wie FLUX.2 [klein], Grok Imagine oder GPT Image in niedriger Qualität kosten etwa 0,01–0,02 $ pro Bild. Premium-Modelle in 4K können 0,15–0,40 $ pro Bild kosten.",
  q3="Was ist Nano Banana?", a3="Nano Banana ist der Spitzname für Googles Gemini-Bildmodelle. Nano Banana 2 ist Gemini 3.1 Flash Image, Nano Banana Pro ist Gemini 3 Pro Image.",
  f1="Offizielle Listenpreise von der API-Preisseite des jeweiligen Anbieters, geprüft am 5. Oktober 2026. OpenAI und Nano Banana Pro werden mit Runway-API-Preisen angezeigt.",
)

I["it"] = dict(
  navImage="Costo immagini",
  title="Calcolatore costo immagini IA – Prezzi Nano Banana, GPT Image, FLUX, Grok | TokenSave",
  desc="Confronta il costo per immagine via API di Nano Banana 2, Nano Banana Pro, GPT Image 2.5, FLUX.2, Grok Imagine, Seedream e Runway. Scegli risoluzione e quantità e vedi subito il totale.",
  h1="Calcolatore costo immagini IA",
  sub="Scopri quanto costano le stesse immagini su ogni grande modello di immagini IA.",
  count="Numero di immagini", perImg="Per immagine",
  notes="Prezzi per immagine generata. Costi delle immagini di riferimento, tasse e sconti di volume esclusi.",
  q1="Come viene fatturata la generazione di immagini IA?", a1="La maggior parte delle API applica un prezzo fisso per immagine che cresce con la risoluzione. I modelli OpenAI costano di più con qualità alta, e FLUX fattura per megapixel.",
  q2="Qual è il modello di immagini IA più economico?", a2="Modelli piccoli come FLUX.2 [klein], Grok Imagine o GPT Image a bassa qualità costano circa $0,01–0,02 per immagine. I modelli premium in 4K possono costare $0,15–0,40 per immagine.",
  q3="Cos'è Nano Banana?", a3="Nano Banana è il soprannome dei modelli di immagini Gemini di Google. Nano Banana 2 è Gemini 3.1 Flash Image e Nano Banana Pro è Gemini 3 Pro Image.",
  f1="Prezzi di listino ufficiali dalla pagina prezzi API di ciascun fornitore, verificati il 5 ottobre 2026. OpenAI e Nano Banana Pro sono mostrati con le tariffe dell'API Runway.",
)

I["ru"] = dict(
  navImage="Стоимость изображений",
  title="Калькулятор стоимости ИИ-изображений – цены Nano Banana, GPT Image, FLUX, Grok | TokenSave",
  desc="Сравните стоимость одного изображения через API у Nano Banana 2, Nano Banana Pro, GPT Image 2.5, FLUX.2, Grok Imagine, Seedream и Runway. Выберите разрешение и количество — итог появится сразу.",
  h1="Калькулятор стоимости ИИ-изображений",
  sub="Узнайте, сколько стоят одни и те же изображения в каждой крупной ИИ-модели.",
  count="Количество изображений", perImg="За изображение",
  notes="Цены указаны за одно сгенерированное изображение. Плата за референсы, налоги и скидки за объём не учтены.",
  q1="Как тарифицируется генерация изображений ИИ?", a1="Большинство API берут фиксированную цену за изображение, которая растёт с разрешением. У моделей OpenAI высокое качество стоит дороже, а FLUX тарифицирует по мегапикселям.",
  q2="Какая ИИ-модель для изображений самая дешёвая?", a2="Небольшие модели — FLUX.2 [klein], Grok Imagine и GPT Image на низком качестве — стоят около $0,01–0,02 за изображение. Премиальные модели в 4K могут стоить $0,15–0,40 за изображение.",
  q3="Что такое Nano Banana?", a3="Nano Banana — прозвище моделей изображений Google Gemini. Nano Banana 2 — это Gemini 3.1 Flash Image, а Nano Banana Pro — Gemini 3 Pro Image.",
  f1="Официальные цены со страниц тарифов API каждого провайдера, проверено 5 октября 2026 г. OpenAI и Nano Banana Pro показаны по тарифам Runway API.",
)

I["uk"] = dict(
  navImage="Вартість зображень",
  title="Калькулятор вартості ШІ-зображень – ціни Nano Banana, GPT Image, FLUX, Grok | TokenSave",
  desc="Порівняйте вартість одного зображення через API у Nano Banana 2, Nano Banana Pro, GPT Image 2.5, FLUX.2, Grok Imagine, Seedream і Runway. Оберіть роздільність і кількість — підсумок з'явиться одразу.",
  h1="Калькулятор вартості ШІ-зображень",
  sub="Дізнайтеся, скільки коштують ті самі зображення в кожній великій ШІ-моделі.",
  count="Кількість зображень", perImg="За зображення",
  notes="Ціни вказано за одне згенероване зображення. Плату за референси, податки та знижки за обсяг не враховано.",
  q1="Як тарифікується генерація зображень ШІ?", a1="Більшість API беруть фіксовану ціну за зображення, яка зростає з роздільністю. У моделей OpenAI висока якість коштує дорожче, а FLUX тарифікує за мегапікселі.",
  q2="Яка ШІ-модель для зображень найдешевша?", a2="Невеликі моделі — FLUX.2 [klein], Grok Imagine і GPT Image на низькій якості — коштують близько $0,01–0,02 за зображення. Преміальні моделі в 4K можуть коштувати $0,15–0,40 за зображення.",
  q3="Що таке Nano Banana?", a3="Nano Banana — прізвисько моделей зображень Google Gemini. Nano Banana 2 — це Gemini 3.1 Flash Image, а Nano Banana Pro — Gemini 3 Pro Image.",
  f1="Офіційні ціни зі сторінок тарифів API кожного постачальника, перевірено 5 жовтня 2026 р. OpenAI і Nano Banana Pro показано за тарифами Runway API.",
)

I["tr"] = dict(
  navImage="Görsel maliyeti",
  title="Yapay Zekâ Görsel Maliyet Hesaplayıcı – Nano Banana, GPT Image, FLUX, Grok Fiyatları | TokenSave",
  desc="Nano Banana 2, Nano Banana Pro, GPT Image 2.5, FLUX.2, Grok Imagine, Seedream ve Runway'in görsel başına API maliyetini karşılaştırın. Çözünürlüğü ve adedi seçin, toplamı anında görün.",
  h1="Yapay Zekâ Görsel Maliyet Hesaplayıcı",
  sub="Aynı görsellerin her büyük yapay zekâ görsel modelinde ne kadar tuttuğunu görün.",
  count="Görsel sayısı", perImg="Görsel başına",
  notes="Fiyatlar üretilen görsel başınadır. Referans görsel ücretleri, vergiler ve hacim indirimleri dahil değildir.",
  q1="Yapay zekâ görsel üretimi nasıl ücretlendirilir?", a1="Çoğu görsel API'si görsel başına sabit bir fiyat alır ve bu fiyat çözünürlükle artar. OpenAI modelleri yüksek kalitede daha pahalıdır, FLUX ise megapiksel başına ücretlendirir.",
  q2="En ucuz yapay zekâ görsel modeli hangisi?", a2="FLUX.2 [klein], Grok Imagine ve düşük kalitede GPT Image gibi küçük modeller görsel başına yaklaşık $0,01–0,02 tutar. Premium modellerle 4K görsel başına $0,15–0,40 olabilir.",
  q3="Nano Banana nedir?", a3="Nano Banana, Google'ın Gemini görsel modellerinin takma adıdır. Nano Banana 2, Gemini 3.1 Flash Image; Nano Banana Pro ise Gemini 3 Pro Image'dır.",
  f1="Her sağlayıcının API fiyat sayfasındaki resmi liste fiyatları, 5 Ekim 2026'da kontrol edildi. OpenAI ve Nano Banana Pro, Runway API fiyatlarıyla gösterilir.",
)

I["ar"] = dict(
  navImage="تكلفة الصور",
  title="حاسبة تكلفة صور الذكاء الاصطناعي – أسعار Nano Banana وGPT Image وFLUX وGrok | TokenSave",
  desc="قارن تكلفة الصورة الواحدة عبر API لنماذج Nano Banana 2 وNano Banana Pro وGPT Image 2.5 وFLUX.2 وGrok Imagine وSeedream وRunway. اختر الدقة والعدد لترى الإجمالي فورًا.",
  h1="حاسبة تكلفة صور الذكاء الاصطناعي",
  sub="اعرف كم تكلّف الصور نفسها على كل نموذج صور رئيسي بالذكاء الاصطناعي.",
  count="عدد الصور", perImg="لكل صورة",
  notes="الأسعار لكل صورة مُولَّدة، ولا تشمل رسوم الصور المرجعية أو الضرائب أو خصومات الكميات.",
  q1="كيف تُسعَّر صور الذكاء الاصطناعي؟", a1="تفرض معظم واجهات الصور سعرًا ثابتًا لكل صورة يرتفع مع الدقة. نماذج OpenAI أغلى في إعدادات الجودة العالية، وFLUX يحاسب لكل ميغابكسل.",
  q2="ما أرخص نموذج صور بالذكاء الاصطناعي؟", a2="النماذج الصغيرة مثل FLUX.2 [klein] وGrok Imagine وGPT Image بجودة منخفضة تكلّف نحو 0.01–0.02 دولار للصورة. أما النماذج المتقدمة بدقة 4K فقد تكلّف 0.15–0.40 دولار للصورة.",
  q3="ما هو Nano Banana؟", a3="Nano Banana هو اللقب الشائع لنماذج الصور Gemini من Google. ‏Nano Banana 2 هو Gemini 3.1 Flash Image، وNano Banana Pro هو Gemini 3 Pro Image.",
  f1="أسعار رسمية من صفحة أسعار API لدى كل مزوّد، تم التحقق منها في 5 أكتوبر 2026. تُعرض OpenAI وNano Banana Pro بأسعار Runway API.",
)

I["fa"] = dict(
  navImage="هزینه تصویر",
  title="ماشین‌حساب هزینه تصویر هوش مصنوعی – قیمت Nano Banana، GPT Image، FLUX و Grok | TokenSave",
  desc="هزینه هر تصویر از طریق API را در Nano Banana 2، Nano Banana Pro، GPT Image 2.5، FLUX.2، Grok Imagine، Seedream و Runway مقایسه کنید. وضوح و تعداد را انتخاب کنید تا جمع کل فوراً نمایش داده شود.",
  h1="ماشین‌حساب هزینه تصویر هوش مصنوعی",
  sub="ببینید همان تصاویر در هر مدل بزرگ تصویرساز هوش مصنوعی چقدر هزینه دارد.",
  count="تعداد تصاویر", perImg="هر تصویر",
  notes="قیمت‌ها برای هر تصویر تولیدشده است. هزینه تصاویر مرجع، مالیات و تخفیف حجمی لحاظ نشده است.",
  q1="تولید تصویر با هوش مصنوعی چطور قیمت‌گذاری می‌شود؟", a1="بیشتر APIهای تصویر برای هر تصویر قیمت ثابتی می‌گیرند که با وضوح بالاتر می‌رود. مدل‌های OpenAI در کیفیت بالاتر گران‌ترند و FLUX بر اساس مگاپیکسل حساب می‌کند.",
  q2="ارزان‌ترین مدل تصویر هوش مصنوعی کدام است؟", a2="مدل‌های کوچک مانند FLUX.2 [klein]، Grok Imagine و GPT Image با کیفیت پایین حدود ۰٫۰۱ تا ۰٫۰۲ دلار برای هر تصویر هزینه دارند. مدل‌های پیشرفته با وضوح 4K ممکن است ۰٫۱۵ تا ۰٫۴۰ دلار برای هر تصویر باشند.",
  q3="Nano Banana چیست؟", a3="Nano Banana لقب مدل‌های تصویر Gemini گوگل است. Nano Banana 2 همان Gemini 3.1 Flash Image و Nano Banana Pro همان Gemini 3 Pro Image است.",
  f1="قیمت‌های رسمی از صفحه قیمت API هر ارائه‌دهنده، بررسی‌شده در ۵ اکتبر ۲۰۲۶. OpenAI و Nano Banana Pro با نرخ Runway API نمایش داده می‌شوند.",
)

I["hi"] = dict(
  navImage="इमेज लागत",
  title="AI इमेज लागत कैलकुलेटर – Nano Banana, GPT Image, FLUX, Grok की कीमतें | TokenSave",
  desc="Nano Banana 2, Nano Banana Pro, GPT Image 2.5, FLUX.2, Grok Imagine, Seedream और Runway की प्रति इमेज API लागत की तुलना करें। रेज़ोल्यूशन और संख्या चुनें और कुल तुरंत देखें।",
  h1="AI इमेज लागत कैलकुलेटर",
  sub="देखें कि वही इमेज हर बड़े AI इमेज मॉडल पर कितने की पड़ती हैं।",
  count="इमेज की संख्या", perImg="प्रति इमेज",
  notes="कीमतें प्रति बनाई गई इमेज हैं। रेफ़रेंस इमेज शुल्क, टैक्स और वॉल्यूम छूट शामिल नहीं हैं।",
  q1="AI इमेज बनाने की कीमत कैसे तय होती है?", a1="ज़्यादातर इमेज API प्रति इमेज तय कीमत लेते हैं, जो रेज़ोल्यूशन के साथ बढ़ती है। OpenAI मॉडल ऊँची क्वालिटी पर महँगे हैं और FLUX प्रति मेगापिक्सल चार्ज करता है।",
  q2="सबसे सस्ता AI इमेज मॉडल कौन-सा है?", a2="FLUX.2 [klein], Grok Imagine और कम क्वालिटी वाला GPT Image जैसे छोटे मॉडल प्रति इमेज लगभग $0.01–0.02 के हैं। प्रीमियम मॉडल पर 4K इमेज $0.15–0.40 तक की पड़ सकती है।",
  q3="Nano Banana क्या है?", a3="Nano Banana, Google के Gemini इमेज मॉडल का उपनाम है। Nano Banana 2 यानी Gemini 3.1 Flash Image और Nano Banana Pro यानी Gemini 3 Pro Image।",
  f1="हर प्रदाता के API मूल्य पेज की आधिकारिक कीमतें, 5 अक्टूबर 2026 को जाँची गईं। OpenAI और Nano Banana Pro को Runway API दरों पर दिखाया गया है।",
)

I["id"] = dict(
  navImage="Biaya gambar",
  title="Kalkulator Biaya Gambar AI – Harga Nano Banana, GPT Image, FLUX, Grok | TokenSave",
  desc="Bandingkan biaya API per gambar untuk Nano Banana 2, Nano Banana Pro, GPT Image 2.5, FLUX.2, Grok Imagine, Seedream, dan Runway. Pilih resolusi dan jumlah, totalnya langsung muncul.",
  h1="Kalkulator Biaya Gambar AI",
  sub="Lihat berapa biaya gambar yang sama di setiap model gambar AI utama.",
  count="Jumlah gambar", perImg="Per gambar",
  notes="Harga per gambar yang dihasilkan. Biaya gambar referensi, pajak, dan diskon volume tidak termasuk.",
  q1="Bagaimana pembuatan gambar AI ditagih?", a1="Sebagian besar API gambar mengenakan harga tetap per gambar yang naik seiring resolusi. Model OpenAI lebih mahal pada kualitas tinggi, dan FLUX menagih per megapiksel.",
  q2="Model gambar AI apa yang paling murah?", a2="Model kecil seperti FLUX.2 [klein], Grok Imagine, dan GPT Image kualitas rendah sekitar $0,01–0,02 per gambar. Model premium pada 4K bisa $0,15–0,40 per gambar.",
  q3="Apa itu Nano Banana?", a3="Nano Banana adalah julukan model gambar Gemini dari Google. Nano Banana 2 adalah Gemini 3.1 Flash Image dan Nano Banana Pro adalah Gemini 3 Pro Image.",
  f1="Harga resmi dari halaman harga API setiap penyedia, dicek 5 Oktober 2026. OpenAI dan Nano Banana Pro ditampilkan dengan tarif Runway API.",
)

I["vi"] = dict(
  navImage="Chi phí ảnh",
  title="Công cụ tính chi phí ảnh AI – Giá Nano Banana, GPT Image, FLUX, Grok | TokenSave",
  desc="So sánh chi phí API cho mỗi ảnh của Nano Banana 2, Nano Banana Pro, GPT Image 2.5, FLUX.2, Grok Imagine, Seedream và Runway. Chọn độ phân giải và số lượng để xem tổng ngay.",
  h1="Công cụ tính chi phí ảnh AI",
  sub="Xem cùng những bức ảnh đó tốn bao nhiêu trên từng mô hình ảnh AI lớn.",
  count="Số lượng ảnh", perImg="Mỗi ảnh",
  notes="Giá tính cho mỗi ảnh được tạo. Chưa gồm phí ảnh tham chiếu, thuế và chiết khấu số lượng lớn.",
  q1="Tạo ảnh AI được tính phí thế nào?", a1="Hầu hết API ảnh thu giá cố định cho mỗi ảnh và tăng theo độ phân giải. Mô hình OpenAI đắt hơn ở mức chất lượng cao, còn FLUX tính theo megapixel.",
  q2="Mô hình ảnh AI nào rẻ nhất?", a2="Các mô hình nhỏ như FLUX.2 [klein], Grok Imagine và GPT Image chất lượng thấp khoảng $0,01–0,02 mỗi ảnh. Mô hình cao cấp ở 4K có thể $0,15–0,40 mỗi ảnh.",
  q3="Nano Banana là gì?", a3="Nano Banana là biệt danh của các mô hình ảnh Gemini của Google. Nano Banana 2 là Gemini 3.1 Flash Image, còn Nano Banana Pro là Gemini 3 Pro Image.",
  f1="Giá niêm yết chính thức từ trang giá API của từng nhà cung cấp, kiểm tra ngày 5/10/2026. OpenAI và Nano Banana Pro hiển thị theo giá Runway API.",
)

I["th"] = dict(
  navImage="ค่ารูปภาพ",
  title="เครื่องคำนวณค่าสร้างภาพ AI – ราคา Nano Banana, GPT Image, FLUX, Grok | TokenSave",
  desc="เปรียบเทียบค่า API ต่อภาพของ Nano Banana 2, Nano Banana Pro, GPT Image 2.5, FLUX.2, Grok Imagine, Seedream และ Runway เลือกความละเอียดและจำนวน แล้วดูยอดรวมได้ทันที",
  h1="เครื่องคำนวณค่าสร้างภาพ AI",
  sub="ดูว่าภาพเดียวกันมีค่าใช้จ่ายเท่าไรบนโมเดลภาพ AI หลักแต่ละตัว",
  count="จำนวนภาพ", perImg="ต่อภาพ",
  notes="ราคาต่อภาพที่สร้าง ไม่รวมค่าภาพอ้างอิง ภาษี และส่วนลดตามปริมาณ",
  q1="การสร้างภาพ AI คิดเงินอย่างไร?", a1="API ภาพส่วนใหญ่คิดราคาคงที่ต่อภาพและแพงขึ้นตามความละเอียด โมเดลของ OpenAI แพงขึ้นเมื่อตั้งคุณภาพสูง ส่วน FLUX คิดตามเมกะพิกเซล",
  q2="โมเดลภาพ AI ตัวไหนถูกที่สุด?", a2="โมเดลเล็กอย่าง FLUX.2 [klein], Grok Imagine และ GPT Image คุณภาพต่ำ ราคาประมาณ $0.01–0.02 ต่อภาพ ส่วนโมเดลระดับสูงที่ 4K อาจถึง $0.15–0.40 ต่อภาพ",
  q3="Nano Banana คืออะไร?", a3="Nano Banana เป็นชื่อเล่นของโมเดลภาพ Gemini ของ Google โดย Nano Banana 2 คือ Gemini 3.1 Flash Image และ Nano Banana Pro คือ Gemini 3 Pro Image",
  f1="ราคาทางการจากหน้าราคา API ของผู้ให้บริการแต่ละราย ตรวจสอบเมื่อ 5 ตุลาคม 2026 OpenAI และ Nano Banana Pro แสดงตามราคา Runway API",
)

I["pl"] = dict(
  navImage="Koszt obrazów",
  title="Kalkulator kosztu obrazów AI – ceny Nano Banana, GPT Image, FLUX, Grok | TokenSave",
  desc="Porównaj koszt API za obraz w Nano Banana 2, Nano Banana Pro, GPT Image 2.5, FLUX.2, Grok Imagine, Seedream i Runway. Wybierz rozdzielczość i liczbę, a suma pojawi się od razu.",
  h1="Kalkulator kosztu obrazów AI",
  sub="Zobacz, ile kosztują te same obrazy w każdym dużym modelu obrazów AI.",
  count="Liczba obrazów", perImg="Za obraz",
  notes="Ceny za wygenerowany obraz. Nie obejmują opłat za obrazy referencyjne, podatków ani rabatów ilościowych.",
  q1="Jak rozliczane jest generowanie obrazów AI?", a1="Większość API pobiera stałą cenę za obraz, która rośnie z rozdzielczością. Modele OpenAI są droższe przy wyższej jakości, a FLUX rozlicza za megapiksel.",
  q2="Który model obrazów AI jest najtańszy?", a2="Małe modele, takie jak FLUX.2 [klein], Grok Imagine czy GPT Image w niskiej jakości, kosztują ok. 0,01–0,02 USD za obraz. Modele premium w 4K mogą kosztować 0,15–0,40 USD za obraz.",
  q3="Co to jest Nano Banana?", a3="Nano Banana to przydomek modeli obrazów Gemini od Google. Nano Banana 2 to Gemini 3.1 Flash Image, a Nano Banana Pro to Gemini 3 Pro Image.",
  f1="Oficjalne ceny z cenników API poszczególnych dostawców, sprawdzone 5 października 2026 r. OpenAI i Nano Banana Pro pokazano według stawek Runway API.",
)

I["nl"] = dict(
  navImage="Beeldkosten",
  title="AI-beeldkostencalculator – Prijzen van Nano Banana, GPT Image, FLUX en Grok | TokenSave",
  desc="Vergelijk de API-kosten per afbeelding van Nano Banana 2, Nano Banana Pro, GPT Image 2.5, FLUX.2, Grok Imagine, Seedream en Runway. Kies resolutie en aantal en zie direct het totaal.",
  h1="AI-beeldkostencalculator",
  sub="Zie wat dezelfde afbeeldingen kosten bij elk groot AI-beeldmodel.",
  count="Aantal afbeeldingen", perImg="Per afbeelding",
  notes="Prijzen per gegenereerde afbeelding. Kosten voor referentiebeelden, belastingen en volumekortingen zijn niet inbegrepen.",
  q1="Hoe wordt AI-beeldgeneratie afgerekend?", a1="De meeste beeld-API's rekenen een vaste prijs per afbeelding die stijgt met de resolutie. OpenAI-modellen kosten meer bij hogere kwaliteit en FLUX rekent per megapixel.",
  q2="Wat is het goedkoopste AI-beeldmodel?", a2="Kleine modellen zoals FLUX.2 [klein], Grok Imagine en GPT Image op lage kwaliteit kosten ongeveer $0,01–0,02 per afbeelding. Premiummodellen in 4K kunnen $0,15–0,40 per afbeelding kosten.",
  q3="Wat is Nano Banana?", a3="Nano Banana is de bijnaam voor de Gemini-beeldmodellen van Google. Nano Banana 2 is Gemini 3.1 Flash Image en Nano Banana Pro is Gemini 3 Pro Image.",
  f1="Officiële prijzen van de API-prijspagina van elke aanbieder, gecontroleerd op 5 oktober 2026. OpenAI en Nano Banana Pro worden getoond tegen Runway API-tarieven.",
)

# Extra languages (i18n_extra/*.py)
from extra_langs import EXTRA as _EXTRA
for _e in _EXTRA:
    I[_e.TAG] = dict(_e.I, navImage=_e.NAV["navImage"])
