# Short page titles (<= 40 chars) and descriptions (<= 80 chars) for search results and link previews.
# Naver Search Advisor recommends these limits; they also stay fully visible on Google.
# Format: META[tool][tag] = (title, description)

META = {"token": {}, "video": {}, "image": {}}

META["token"] = {
  "en":    ("AI Token Counter – GPT, Claude, Gemini", "Count tokens, characters and API cost for GPT, Claude and Gemini. Free, private."),
  "ko":    ("AI 토큰 계산기 – GPT·Claude·Gemini", "GPT·Claude·Gemini 토큰 수와 API 비용을 바로 계산하세요. 무료, 업로드 없음."),
  "ja":    ("AIトークン計算 – GPT・Claude・Gemini", "GPT・Claude・Geminiのトークン数とAPI料金をすぐ計算。無料・アップロード不要。"),
  "zh-CN": ("AI Token 计算器 – GPT、Claude、Gemini", "即时计算 GPT、Claude、Gemini 的 Token 数和 API 费用。免费，不上传。"),
  "zh-TW": ("AI Token 計算器 – GPT、Claude、Gemini", "即時計算 GPT、Claude、Gemini 的 Token 數與 API 費用。免費，不上傳。"),
  "es":    ("Contador de tokens IA – GPT, Claude", "Cuenta tokens y coste de API de GPT, Claude y Gemini. Gratis y sin subir nada."),
  "pt":    ("Contador de tokens de IA – GPT, Claude", "Conte tokens e o custo de API do GPT, Claude e Gemini. Grátis e sem upload."),
  "fr":    ("Compteur de tokens IA – GPT, Claude", "Comptez les tokens et le coût API de GPT, Claude et Gemini. Gratuit, sans envoi."),
  "de":    ("KI-Token-Zähler – GPT, Claude, Gemini", "Tokens und API-Kosten für GPT, Claude und Gemini sofort zählen. Gratis, lokal."),
  "it":    ("Contatore token IA – GPT, Claude", "Conta token e costo API di GPT, Claude e Gemini. Gratis, senza caricare nulla."),
  "ru":    ("Счётчик токенов ИИ – GPT, Claude", "Токены и стоимость API для GPT, Claude и Gemini. Бесплатно, без загрузки."),
  "uk":    ("Лічильник токенів ШІ – GPT, Claude", "Токени й вартість API для GPT, Claude і Gemini. Безкоштовно, без завантаження."),
  "tr":    ("Yapay Zekâ Token Sayacı – GPT, Claude", "GPT, Claude ve Gemini için token ve API maliyetini hesaplayın. Ücretsiz."),
  "ar":    ("عدّاد رموز الذكاء الاصطناعي – GPT", "احسب الرموز وتكلفة API لـ GPT وClaude وGemini فورًا. مجاني وبدون رفع."),
  "fa":    ("شمارنده توکن هوش مصنوعی – GPT و Claude", "توکن و هزینه API برای GPT، Claude و Gemini را فوراً حساب کنید. رایگان."),
  "hi":    ("AI टोकन काउंटर – GPT, Claude, Gemini", "GPT, Claude और Gemini के टोकन और API लागत तुरंत गिनें। मुफ़्त, कोई अपलोड नहीं।"),
  "id":    ("Penghitung Token AI – GPT, Claude", "Hitung token dan biaya API GPT, Claude, dan Gemini. Gratis, tanpa unggah."),
  "vi":    ("Đếm token AI – GPT, Claude, Gemini", "Đếm token và chi phí API của GPT, Claude, Gemini ngay. Miễn phí, không tải lên."),
  "th":    ("ตัวนับโทเค็น AI – GPT, Claude, Gemini", "นับโทเค็นและค่า API ของ GPT, Claude, Gemini ทันที ฟรี ไม่ต้องอัปโหลด"),
  "pl":    ("Licznik tokenów – kalkulator tokenów AI", "Licznik tokenów: ile tokenów ma polski tekst i ile to kosztuje w GPT i Claude."),
  "nl":    ("Tokenteller: tokens tellen voor GPT", "Gratis tokenteller: tokens en API-kosten van je tekst in GPT, Claude, Gemini."),
}

META["video"] = {
  "en":    ("AI Video Cost Calculator – Veo, Kling", "Compare API prices of Veo 3.1, Kling, Runway, Luma and more per second and clip."),
  "ko":    ("AI 영상 생성 비용 계산기 – Veo·Kling", "Veo 3.1, Kling, Runway, Luma 등 AI 영상 API 가격을 초당·클립당으로 비교하세요."),
  "ja":    ("AI動画生成コスト計算 – Veo・Kling", "Veo 3.1・Kling・Runway・LumaなどAI動画APIの料金を秒・クリップ単位で比較。"),
  "zh-CN": ("AI 视频生成费用计算器 – Veo、Kling", "按秒和按片段对比 Veo 3.1、Kling、Runway、Luma 等 AI 视频 API 价格。"),
  "zh-TW": ("AI 影片生成費用計算器 – Veo、Kling", "按秒與按片段比較 Veo 3.1、Kling、Runway、Luma 等 AI 影片 API 價格。"),
  "es":    ("Coste de vídeo con IA – Veo, Kling", "Compara precios de API de Veo 3.1, Kling, Runway, Luma y más por segundo."),
  "pt":    ("Custo de vídeo com IA – Veo, Kling", "Compare preços de API do Veo 3.1, Kling, Runway, Luma e outros por segundo."),
  "fr":    ("Coût vidéo IA – Veo, Kling, Runway", "Comparez les prix API de Veo 3.1, Kling, Runway, Luma et plus, à la seconde."),
  "de":    ("KI-Videokosten-Rechner – Veo, Kling", "API-Preise von Veo 3.1, Kling, Runway, Luma u. a. pro Sekunde vergleichen."),
  "it":    ("Costo video IA – Veo, Kling, Runway", "Confronta i prezzi API di Veo 3.1, Kling, Runway, Luma e altri al secondo."),
  "ru":    ("Стоимость ИИ-видео – Veo, Kling", "Сравните цены API Veo 3.1, Kling, Runway, Luma и других за секунду и клип."),
  "uk":    ("Вартість ШІ-відео – Veo, Kling", "Порівняйте ціни API Veo 3.1, Kling, Runway, Luma та інших за секунду й кліп."),
  "tr":    ("YZ Video Maliyeti – Veo, Kling, Runway", "Veo 3.1, Kling, Runway, Luma vb. API fiyatlarını saniye başına kıyaslayın."),
  "ar":    ("تكلفة فيديو الذكاء الاصطناعي – Veo", "قارن أسعار API لـ Veo 3.1 وKling وRunway وLuma وغيرها لكل ثانية ومقطع."),
  "fa":    ("هزینه ویدیوی هوش مصنوعی – Veo و Kling", "قیمت API مدل‌های Veo 3.1، Kling، Runway، Luma و دیگران را ثانیه‌ای مقایسه کنید."),
  "hi":    ("AI वीडियो लागत कैलकुलेटर – Veo, Kling", "Veo 3.1, Kling, Runway, Luma आदि की API कीमतें प्रति सेकंड और क्लिप तुलना करें।"),
  "id":    ("Biaya Video AI – Veo, Kling, Runway", "Bandingkan harga API Veo 3.1, Kling, Runway, Luma, dan lainnya per detik."),
  "vi":    ("Chi phí video AI – Veo, Kling, Runway", "So sánh giá API của Veo 3.1, Kling, Runway, Luma và khác theo giây, theo clip."),
  "th":    ("ค่าสร้างวิดีโอ AI – Veo, Kling, Runway", "เทียบราคา API ของ Veo 3.1, Kling, Runway, Luma และอื่น ๆ ต่อวินาทีและต่อคลิป"),
  "pl":    ("Koszt wideo AI – Veo, Kling, Runway", "Porównaj ceny API Veo 3.1, Kling, Runway, Luma i innych za sekundę i klip."),
  "nl":    ("Kosten AI-video per seconde: Veo, Kling", "Wat kost een AI-video? Prijs per seconde van Veo 3.1, Kling, Runway en Luma."),
}

META["image"] = {
  "en":    ("AI Image Cost – Nano Banana, GPT Image", "Compare per-image API prices of Nano Banana, GPT Image, FLUX, Grok and more."),
  "ko":    ("AI 이미지 생성 비용 – 나노바나나·GPT", "나노바나나, GPT Image, FLUX, Grok 등 AI 이미지 API 장당 가격을 비교하세요."),
  "ja":    ("AI画像生成コスト – Nano Banana・GPT", "Nano Banana・GPT Image・FLUX・GrokなどAI画像APIの1枚あたり料金を比較。"),
  "zh-CN": ("AI 图片生成费用 – Nano Banana、GPT", "对比 Nano Banana、GPT Image、FLUX、Grok 等 AI 图片 API 每张价格。"),
  "zh-TW": ("AI 圖片生成費用 – Nano Banana、GPT", "比較 Nano Banana、GPT Image、FLUX、Grok 等 AI 圖片 API 每張價格。"),
  "es":    ("Coste de imágenes IA – Nano Banana", "Compara el precio por imagen de Nano Banana, GPT Image, FLUX, Grok y más."),
  "pt":    ("Custo de imagens IA – Nano Banana", "Compare o preço por imagem de Nano Banana, GPT Image, FLUX, Grok e outros."),
  "fr":    ("Coût d'images IA – Nano Banana, GPT", "Comparez le prix par image de Nano Banana, GPT Image, FLUX, Grok et plus."),
  "de":    ("KI-Bildkosten – Nano Banana, GPT Image", "Preis pro Bild von Nano Banana, GPT Image, FLUX, Grok u. a. vergleichen."),
  "it":    ("Costo immagini IA – Nano Banana, GPT", "Confronta il prezzo per immagine di Nano Banana, GPT Image, FLUX, Grok e altri."),
  "ru":    ("Стоимость ИИ-изображений – Nano Banana", "Сравните цену за изображение Nano Banana, GPT Image, FLUX, Grok и других."),
  "uk":    ("Вартість ШІ-зображень – Nano Banana", "Порівняйте ціну за зображення Nano Banana, GPT Image, FLUX, Grok та інших."),
  "tr":    ("YZ Görsel Maliyeti – Nano Banana, GPT", "Nano Banana, GPT Image, FLUX, Grok ve diğerlerinin görsel başına fiyatları."),
  "ar":    ("تكلفة صور الذكاء الاصطناعي – Nano Banana", "قارن سعر الصورة في Nano Banana وGPT Image وFLUX وGrok وغيرها."),
  "fa":    ("هزینه تصویر هوش مصنوعی – Nano Banana", "قیمت هر تصویر در Nano Banana، GPT Image، FLUX، Grok و دیگران را مقایسه کنید."),
  "hi":    ("AI इमेज लागत – Nano Banana, GPT Image", "Nano Banana, GPT Image, FLUX, Grok आदि की प्रति इमेज API कीमत तुलना करें।"),
  "id":    ("Biaya Gambar AI – Nano Banana, GPT", "Bandingkan harga per gambar Nano Banana, GPT Image, FLUX, Grok, dan lainnya."),
  "vi":    ("Chi phí ảnh AI – Nano Banana, GPT Image", "So sánh giá mỗi ảnh của Nano Banana, GPT Image, FLUX, Grok và các mô hình khác."),
  "th":    ("ค่าสร้างภาพ AI – Nano Banana, GPT", "เทียบราคาต่อภาพของ Nano Banana, GPT Image, FLUX, Grok และอื่น ๆ"),
  "pl":    ("Koszt obrazów AI – Nano Banana, GPT", "Porównaj cenę za obraz w Nano Banana, GPT Image, FLUX, Grok i innych."),
  "nl":    ("Kosten AI-afbeelding: prijs per beeld", "Wat kost een AI-afbeelding? Prijs per beeld van Nano Banana, GPT Image en FLUX."),
}

# Extra languages (i18n_extra/*.py)
from extra_langs import EXTRA as _EXTRA
for _e in _EXTRA:
    for _tool in ("token", "video", "image"):
        META[_tool][_e.TAG] = _e.META[_tool]
