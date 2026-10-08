# -*- coding: utf-8 -*-
# Measured token-ratio facts per language page (o200k vs cl100k, relative to English).
# One 34-token English customer-support prompt, translated into 41 languages.

FACT = {
    "en": dict(
        callout="The same text can use from 3% (Chinese) to 144% (Punjabi) more tokens than English — see how we measured 41 languages.",
        q4="Do non-English prompts use more tokens?",
        a4="Yes: across 41 languages, the same prompt uses from 3% (Simplified Chinese) to 144% (Punjabi) more tokens than English on GPT's o200k tokenizer. The gap used to be much larger — Hindi, for example, dropped from 359% more on the old GPT-4 tokenizer to 50% more today.",
        more="How we measured",
    ),
    "ko": dict(
        callout="같은 내용이라도 한국어는 영어보다 토큰을 약 44% 더 씁니다 (GPT o200k 토크나이저 기준 실측).",
        q4="한국어는 영어보다 토큰이 몇 % 더 나오나요?",
        a4="GPT 토크나이저(o200k)에서 한국어는 같은 내용의 영어보다 토큰을 약 44% 더 씁니다. 그래서 프롬프트를 영어로 바꿔 보내면 토큰이 약 31% 줄어듭니다. 💸 토큰 절약 버튼을 누르면 PC용 Chrome·Edge의 기기 내 번역으로 영어로 바꾸고, 답은 한국어로 받도록 한 줄을 붙여 줍니다.",
        more="측정 방법 보기",
    ),
    "ja": dict(
        callout="同じ内容でも、日本語は英語より約79%多くトークンを使います（GPTのo200kトークナイザーで実測）。",
        q4="日本語は英語より何%多くトークンを使いますか？",
        a4="GPTのトークナイザー（o200k）では、日本語は同じ内容の英語より約79%多くトークンを使います。そのためプロンプトを英語にして送ると、トークンが約44%減ります。💸 トークン節約ボタンを押すと、デスクトップ版Chrome・Edgeの端末内翻訳で英語に変換し、回答は日本語で返すよう一行を添えます。",
        more="測定方法",
    ),
    "zh-CN": dict(
        callout="同样的内容，简体中文的 Token 数约比英文多 3%（基于 GPT 的 o200k 分词器实测）。",
        q4="中文比英文多用多少 Token？",
        a4="在 GPT 的 o200k 分词器上，简体中文的 Token 数约比同等英文内容多 3%。旧版 GPT-4 分词器要多 53%，因此中文的使用成本已大幅下降；在 41 种语言中，比英文多出的比例从 3%（简体中文）到 144%（旁遮普语）不等。",
        more="测量方法",
    ),
    "zh-TW": dict(
        callout="同樣的內容，繁體中文的 Token 數約比英文多 35%（以 GPT 的 o200k 分詞器實測）。",
        q4="繁體中文比英文多用多少 Token？",
        a4="在 GPT 的 o200k 分詞器上，繁體中文的 Token 數約比同等英文內容多 35%。舊版 GPT-4 分詞器要多 112%，因此繁體中文的使用成本已大幅下降；在 41 種語言中，比英文多出的比例從 3%（簡體中文）到 144%（旁遮普語）不等。",
        more="測量方法",
    ),
    "es": dict(
        callout="El español usa un 18 % más de tokens que el inglés para el mismo texto (medido con el tokenizador o200k de GPT).",
        q4="¿Cuántos tokens más usa el español que el inglés?",
        a4="Con el tokenizador o200k de GPT, el español usa un 18 % más de tokens que el mismo texto en inglés. El antiguo tokenizador de GPT-4 necesitaba un 29 % más, así que el coste para el español ha bajado bastante; entre 41 idiomas, la diferencia va de un 3 % (chino simplificado) a un 144 % más (panyabí).",
        more="Cómo lo medimos",
    ),
    "pt": dict(
        callout="O português usa cerca de 21% mais tokens que o inglês para o mesmo texto (medido no tokenizador o200k do GPT).",
        q4="Quantos tokens a mais o português usa em relação ao inglês?",
        a4="No tokenizador o200k do GPT, o português usa cerca de 21% mais tokens que o mesmo texto em inglês. O antigo tokenizador do GPT-4 precisava de 41% mais, então o custo para o português caiu bastante; entre 41 idiomas, a diferença vai de 3% (chinês simplificado) a 144% a mais (punjabi).",
        more="Como medimos",
    ),
    "fr": dict(
        callout="Le français utilise environ 29 % de tokens de plus que l’anglais pour le même texte (mesuré avec le tokenizer o200k de GPT).",
        q4="Combien de tokens en plus le français utilise-t-il par rapport à l’anglais ?",
        a4="Avec le tokenizer o200k de GPT, le français utilise environ 29 % de tokens de plus que le même texte en anglais. L’ancien tokenizer de GPT-4 en demandait 44 % de plus, donc le coût pour le français a nettement baissé ; sur 41 langues, l’écart va de 3 % (chinois simplifié) à 144 % de plus (pendjabi).",
        more="Notre méthode",
    ),
    "de": dict(
        callout="Deutsch braucht für denselben Text etwa 26 % mehr Tokens als Englisch (gemessen mit GPTs o200k-Tokenizer).",
        q4="Wie viel mehr Tokens braucht Deutsch als Englisch?",
        a4="Mit GPTs o200k-Tokenizer braucht Deutsch etwa 26 % mehr Tokens als derselbe Text auf Englisch. Der alte GPT-4-Tokenizer brauchte noch 50 % mehr, die Kosten für Deutsch sind also deutlich gesunken; über 41 Sprachen reicht der Mehrbedarf von 3 % (vereinfachtes Chinesisch) bis 144 % (Punjabi).",
        more="So haben wir gemessen",
    ),
    "it": dict(
        callout="L’italiano usa circa il 38% di token in più dell’inglese per lo stesso testo (misurato con il tokenizer o200k di GPT).",
        q4="Quanti token in più usa l’italiano rispetto all’inglese?",
        a4="Con il tokenizer o200k di GPT, l’italiano usa circa il 38% di token in più rispetto allo stesso testo in inglese. Il vecchio tokenizer di GPT-4 ne richiedeva il 59% in più, quindi il costo per l’italiano è sceso parecchio; su 41 lingue, la differenza va dal 3% (cinese semplificato) al 144% in più (punjabi).",
        more="Come abbiamo misurato",
    ),
    "ru": dict(
        callout="Русский текст занимает примерно на 32% больше токенов, чем тот же текст на английском (замер на токенизаторе o200k от GPT).",
        q4="На сколько процентов больше токенов тратит русский язык по сравнению с английским?",
        a4="На токенизаторе o200k от GPT русский текст занимает примерно на 32% больше токенов, чем тот же текст на английском. Старому токенизатору GPT-4 требовалось на 115% больше, так что стоимость для русского языка заметно снизилась; среди 41 языка разница варьируется от 3% (упрощённый китайский) до 144% (панджаби).",
        more="Как мы измеряли",
    ),
    "uk": dict(
        callout="Український текст займає приблизно на 88% більше токенів, ніж той самий текст англійською (виміряно на токенізаторі o200k від GPT).",
        q4="На скільки відсотків більше токенів використовує українська порівняно з англійською?",
        a4="На токенізаторі o200k від GPT український текст займає приблизно на 88% більше токенів, ніж той самий текст англійською. Старому токенізатору GPT-4 потрібно було на 215% більше, тож вартість для української суттєво знизилася; серед 41 мови різниця коливається від 3% (спрощена китайська) до 144% (панджабі).",
        more="Як ми вимірювали",
    ),
    "tr": dict(
        callout="Türkçe aynı metin için İngilizceden yaklaşık %47 daha fazla token kullanır (GPT'nin o200k tokenizer'ıyla ölçüldü).",
        q4="Türkçe İngilizceye göre yüzde kaç daha fazla token kullanır?",
        a4="GPT'nin o200k tokenizer'ında Türkçe, aynı İngilizce metinden yaklaşık %47 daha fazla token kullanır. Eski GPT-4 tokenizer'ında bu fark %106 idi, yani Türkçe için maliyet belirgin şekilde düştü; 41 dil genelinde fark %3 (Basitleştirilmiş Çince) ile %144 (Pencapça) arasında değişir.",
        more="Nasıl ölçtük",
    ),
    "ar": dict(
        callout="تستهلك العربية رموزًا أكثر من الإنجليزية بنحو 26% للنص نفسه (قياس فعلي على مُجزّئ o200k الخاص بـ GPT).",
        q4="بكم في المئة تستهلك العربية رموزًا أكثر من الإنجليزية؟",
        a4="على مُجزّئ o200k الخاص بـ GPT، تستهلك العربية رموزًا أكثر بنحو 26% من النص نفسه بالإنجليزية. كان مُجزّئ GPT-4 القديم يحتاج إلى 203% أكثر، لذا انخفضت تكلفة العربية كثيرًا؛ وعبر 41 لغة تتراوح الزيادة من 3% (الصينية المبسطة) إلى 144% (البنجابية).",
        more="كيف قسنا ذلك",
    ),
    "fa": dict(
        callout="فارسی برای همان متن حدود 24% توکن بیشتری از انگلیسی مصرف می‌کند (اندازه‌گیری‌شده با توکنایزر o200k در GPT).",
        q4="فارسی چند درصد بیشتر از انگلیسی توکن مصرف می‌کند؟",
        a4="در توکنایزر o200k در GPT، فارسی حدود 24% توکن بیشتری از همان متن انگلیسی مصرف می‌کند. توکنایزر قدیمی GPT-4 به 179% بیشتر نیاز داشت، پس هزینه برای فارسی بسیار کاهش یافته است؛ در میان 41 زبان این افزایش از 3% (چینی ساده‌شده) تا 144% (پنجابی) متغیر است.",
        more="روش اندازه‌گیری ما",
    ),
    "hi": dict(
        callout="एक ही टेक्स्ट के लिए हिंदी, अंग्रेज़ी के मुकाबले लगभग 50% ज़्यादा टोकन लेती है (GPT के o200k टोकनाइज़र पर मापा गया)।",
        q4="हिंदी में अंग्रेज़ी से कितने प्रतिशत ज़्यादा टोकन लगते हैं?",
        a4="GPT के o200k टोकनाइज़र पर हिंदी, उसी अंग्रेज़ी टेक्स्ट के मुकाबले लगभग 50% ज़्यादा टोकन लेती है। पुराने GPT-4 टोकनाइज़र में 359% ज़्यादा लगते थे, इसलिए हिंदी की लागत काफ़ी घट गई है; 41 भाषाओं में यह अंतर 3% (सरलीकृत चीनी) से 144% (पंजाबी) तक है।",
        more="हमने कैसे मापा",
    ),
    "id": dict(
        callout="Bahasa Indonesia memakai sekitar 15% lebih banyak token daripada bahasa Inggris untuk teks yang sama (diukur dengan tokenizer o200k GPT).",
        q4="Berapa persen lebih banyak token yang dipakai bahasa Indonesia dibanding bahasa Inggris?",
        a4="Pada tokenizer o200k GPT, bahasa Indonesia memakai sekitar 15% lebih banyak token daripada teks yang sama dalam bahasa Inggris. Tokenizer GPT-4 lama membutuhkan 38% lebih banyak, jadi biaya untuk bahasa Indonesia turun cukup banyak; di 41 bahasa, selisihnya berkisar dari 3% (Tionghoa Sederhana) hingga 144% (Punjabi).",
        more="Cara kami mengukur",
    ),
    "vi": dict(
        callout="Tiếng Việt dùng nhiều hơn khoảng 35% số token so với tiếng Anh cho cùng một nội dung (đo trên tokenizer o200k của GPT).",
        q4="Tiếng Việt tốn nhiều hơn bao nhiêu phần trăm token so với tiếng Anh?",
        a4="Trên tokenizer o200k của GPT, tiếng Việt dùng nhiều hơn khoảng 35% số token so với cùng nội dung bằng tiếng Anh. Tokenizer GPT-4 cũ cần nhiều hơn tới 132%, nên chi phí cho tiếng Việt đã giảm đáng kể; trên 41 ngôn ngữ, mức chênh lệch dao động từ 3% (tiếng Trung giản thể) đến 144% (tiếng Punjab).",
        more="Cách chúng tôi đo",
    ),
    "th": dict(
        callout="ข้อความเดียวกัน ภาษาไทยใช้โทเค็นมากกว่าภาษาอังกฤษประมาณ 74% (วัดจริงด้วยตัวแบ่งโทเค็น o200k ของ GPT)",
        q4="ภาษาไทยใช้โทเค็นมากกว่าภาษาอังกฤษกี่เปอร์เซ็นต์?",
        a4="บนตัวแบ่งโทเค็น o200k ของ GPT ภาษาไทยใช้โทเค็นมากกว่าข้อความเดียวกันในภาษาอังกฤษประมาณ 74% ตัวแบ่งโทเค็น GPT-4 รุ่นเก่าต้องใช้มากกว่าถึง 271% ค่าใช้จ่ายสำหรับภาษาไทยจึงลดลงมาก และใน 41 ภาษา ส่วนที่มากกว่าอยู่ระหว่าง 3% (จีนตัวย่อ) ถึง 144% (ปัญจาบี)",
        more="วิธีที่เราวัด",
    ),
    "pl": dict(
        callout="Polski zużywa ok. 88% więcej tokenów niż angielski dla tego samego tekstu (zmierzone na tokenizerze o200k w GPT).",
        q4="O ile procent więcej tokenów zużywa polski niż angielski?",
        a4="Na tokenizerze o200k w GPT polski tekst zużywa ok. 88% więcej tokenów niż ten sam tekst po angielsku. Stary tokenizer GPT-4 potrzebował 112% więcej, więc koszt dla języka polskiego wyraźnie spadł; w 41 językach różnica wynosi od 3% (chiński uproszczony) do 144% (pendżabski).",
        more="Jak mierzyliśmy",
    ),
    "nl": dict(
        callout="Nederlands gebruikt ongeveer 29% meer tokens dan Engels voor dezelfde tekst (gemeten met de o200k-tokenizer van GPT).",
        q4="Hoeveel meer tokens gebruikt Nederlands dan Engels?",
        a4="Met de o200k-tokenizer van GPT gebruikt Nederlands ongeveer 29% meer tokens dan dezelfde tekst in het Engels. De oude GPT-4-tokenizer had 74% meer nodig, dus de kosten voor Nederlands zijn flink gedaald; over 41 talen loopt het verschil van 3% (vereenvoudigd Chinees) tot 144% (Punjabi).",
        more="Hoe we meten",
    ),
    "bn": dict(
        callout="একই লেখার জন্য বাংলা ইংরেজির চেয়ে প্রায় 68% বেশি টোকেন ব্যবহার করে (GPT-এর o200k টোকেনাইজারে মাপা)।",
        q4="বাংলায় ইংরেজির চেয়ে কত শতাংশ বেশি টোকেন লাগে?",
        a4="GPT-এর o200k টোকেনাইজারে বাংলা একই ইংরেজি লেখার চেয়ে প্রায় 68% বেশি টোকেন ব্যবহার করে। পুরোনো GPT-4 টোকেনাইজারে 509% বেশি লাগত, তাই বাংলার খরচ অনেক কমেছে; 41টি ভাষায় এই বাড়তি অংশ 3% (সরলীকৃত চীনা) থেকে 144% (পাঞ্জাবি) পর্যন্ত।",
        more="আমরা কীভাবে মেপেছি",
    ),
    "ur": dict(
        callout="ایک ہی متن کے لیے اردو انگریزی کے مقابلے میں تقریباً 59% زیادہ ٹوکن استعمال کرتی ہے (GPT کے o200k ٹوکنائزر پر ناپا گیا)۔",
        q4="اردو میں انگریزی سے کتنے فیصد زیادہ ٹوکن لگتے ہیں؟",
        a4="GPT کے o200k ٹوکنائزر پر اردو اسی انگریزی متن کے مقابلے میں تقریباً 59% زیادہ ٹوکن استعمال کرتی ہے۔ پرانے GPT-4 ٹوکنائزر میں 324% زیادہ لگتے تھے، اس لیے اردو کی لاگت کافی کم ہو گئی ہے؛ 41 زبانوں میں یہ فرق 3% (سادہ چینی) سے 144% (پنجابی) تک ہے۔",
        more="ہم نے کیسے ناپا",
    ),
    "fil": dict(
        callout="Gumagamit ang Filipino ng mga 53% na mas maraming token kumpara sa Ingles para sa parehong teksto (sinukat sa o200k tokenizer ng GPT).",
        q4="Ilang porsiyento na mas maraming token ang ginagamit ng Filipino kaysa Ingles?",
        a4="Sa o200k tokenizer ng GPT, gumagamit ang Filipino ng mga 53% na mas maraming token kumpara sa parehong teksto sa Ingles. Ang lumang GPT-4 tokenizer ay nangangailangan ng 76% na mas marami, kaya bumaba ang gastos para sa Filipino; sa 41 wika, ang dagdag ay mula 3% (Simplified Chinese) hanggang 144% (Punjabi).",
        more="Paano namin sinukat",
    ),
    "cs": dict(
        callout="Čeština spotřebuje pro stejný text zhruba o 100 % více tokenů než angličtina (měřeno na tokenizéru o200k od GPT).",
        q4="O kolik procent více tokenů spotřebuje čeština než angličtina?",
        a4="Na tokenizéru o200k od GPT spotřebuje čeština zhruba o 100 % více tokenů než stejný text v angličtině, což ji řadí mezi nejdražší ze 41 měřených jazyků (rozsah od 3 % u zjednodušené čínštiny až po 144 % u pandžábštiny). Starý tokenizér GPT-4 potřeboval o 159 % více, takže náklady pro češtinu přesto znatelně klesly.",
        more="Jak jsme měřili",
    ),
    "sv": dict(
        callout="Svenska använder cirka 32 % fler tokens än engelska för samma text (uppmätt med GPT:s o200k-tokenizer).",
        q4="Hur många fler tokens använder svenska jämfört med engelska?",
        a4="Med GPT:s o200k-tokenizer använder svenska cirka 32 % fler tokens än samma text på engelska. Den gamla GPT-4-tokenizern krävde 50 % fler, så kostnaden för svenska har sjunkit tydligt; över 41 språk sträcker sig skillnaden från 3 % (förenklad kinesiska) till 144 % (punjabi).",
        more="Så mätte vi",
    ),
    "he": dict(
        callout="עברית צורכת בערך 56% יותר טוקנים מאנגלית עבור אותו טקסט (נמדד במפרק הטוקנים o200k של GPT).",
        q4="בכמה אחוזים יותר טוקנים צורכת עברית לעומת אנגלית?",
        a4="במפרק הטוקנים o200k של GPT, עברית צורכת בערך 56% יותר טוקנים מאותו טקסט באנגלית. מפרק הטוקנים הישן של GPT-4 דרש 276% יותר, כך שהעלות לעברית ירדה מאוד; בקרב 41 שפות התוספת נעה בין 3% (סינית מפושטת) ל-144% (פנג'אבית).",
        more="איך מדדנו",
    ),
}

from i18n_eu7 import F7 as _F7
FACT.update(_F7)
from i18n_in7 import F_IN as _FI
FACT.update(_FI)
