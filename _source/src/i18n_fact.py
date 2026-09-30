# -*- coding: utf-8 -*-
# Measured token-ratio facts per language page (o200k vs cl100k, relative to English).
# One 34-token English customer-support prompt, translated into 27 languages.

FACT = {
    "en": dict(
        callout="The same text can cost from 1.03× (Chinese) to 2.00× (Czech) the tokens of English — see how we measured 27 languages.",
        q4="Do non-English prompts use more tokens?",
        a4="Yes: across 27 languages, the same prompt uses from 1.03× (Simplified Chinese) to 2.00× (Czech) the tokens of English on GPT's o200k tokenizer. The gap used to be much larger — Hindi, for example, dropped from 4.59× on the old GPT-4 tokenizer to 1.50× today.",
        more="How we measured",
    ),
    "ko": dict(
        callout="같은 내용이라도 한국어는 영어보다 토큰을 약 1.44× 더 씁니다 (GPT o200k 토크나이저 기준 실측).",
        q4="한국어는 영어보다 토큰이 몇 배 더 나오나요?",
        a4="GPT의 o200k 토크나이저에서 한국어는 같은 내용의 영어보다 약 1.44×의 토큰을 씁니다. 예전 GPT-4 토크나이저에서는 2.50×가 필요했으므로 한국어 사용 비용이 크게 줄었으며, 27개 언어 전체로는 1.03×(중국어 간체)부터 2.00×(체코어)까지 차이가 납니다.",
        more="측정 방법 보기",
    ),
    "ja": dict(
        callout="同じ内容でも、日本語は英語の約1.79×のトークンを使います（GPTのo200kトークナイザーで実測）。",
        q4="日本語は英語の何倍のトークンを使いますか？",
        a4="GPTのo200kトークナイザーでは、日本語は同じ内容の英語の約1.79×のトークンを使います。旧GPT-4トークナイザーでは2.21×必要だったため日本語のコストは大きく下がっており、27言語全体では1.03×（簡体字中国語）から2.00×（チェコ語）までの幅があります。",
        more="測定方法",
    ),
    "zh-CN": dict(
        callout="同样的内容，简体中文的 Token 数约为英文的 1.03×（基于 GPT 的 o200k 分词器实测）。",
        q4="中文比英文多用多少 Token？",
        a4="在 GPT 的 o200k 分词器上，简体中文的 Token 数约为同等英文内容的 1.03×。旧版 GPT-4 分词器需要 1.53×，因此中文的使用成本已大幅下降；在 27 种语言中，比例从 1.03×（简体中文）到 2.00×（捷克语）不等。",
        more="测量方法",
    ),
    "zh-TW": dict(
        callout="同樣的內容，繁體中文的 Token 數約為英文的 1.35×（以 GPT 的 o200k 分詞器實測）。",
        q4="繁體中文比英文多用多少 Token？",
        a4="在 GPT 的 o200k 分詞器上，繁體中文的 Token 數約為同等英文內容的 1.35×。舊版 GPT-4 分詞器需要 2.12×，因此繁體中文的使用成本已大幅下降；在 27 種語言中，比例從 1.03×（簡體中文）到 2.00×（捷克語）不等。",
        more="測量方法",
    ),
    "es": dict(
        callout="El español usa unas 1.18× los tokens del inglés para el mismo texto (medido con el tokenizador o200k de GPT).",
        q4="¿Cuántos tokens más usa el español que el inglés?",
        a4="Con el tokenizador o200k de GPT, el español usa unas 1.18× los tokens del mismo texto en inglés. El antiguo tokenizador de GPT-4 necesitaba 1.29×, así que el coste para el español ha bajado bastante; entre 27 idiomas, la proporción va de 1.03× (chino simplificado) a 2.00× (checo).",
        more="Cómo lo medimos",
    ),
    "pt": dict(
        callout="O português usa cerca de 1.21× os tokens do inglês para o mesmo texto (medido no tokenizador o200k do GPT).",
        q4="Quantos tokens a mais o português usa em relação ao inglês?",
        a4="No tokenizador o200k do GPT, o português usa cerca de 1.21× os tokens do mesmo texto em inglês. O antigo tokenizador do GPT-4 precisava de 1.41×, então o custo para o português caiu bastante; entre 27 idiomas, a proporção vai de 1.03× (chinês simplificado) a 2.00× (tcheco).",
        more="Como medimos",
    ),
    "fr": dict(
        callout="Le français utilise environ 1.29× les tokens de l’anglais pour le même texte (mesuré avec le tokenizer o200k de GPT).",
        q4="Combien de tokens en plus le français utilise-t-il par rapport à l’anglais ?",
        a4="Avec le tokenizer o200k de GPT, le français utilise environ 1.29× les tokens du même texte en anglais. L’ancien tokenizer de GPT-4 en demandait 1.44×, donc le coût pour le français a nettement baissé ; sur 27 langues, le rapport va de 1.03× (chinois simplifié) à 2.00× (tchèque).",
        more="Notre méthode",
    ),
    "de": dict(
        callout="Deutsch braucht für denselben Text etwa 1.26× so viele Tokens wie Englisch (gemessen mit GPTs o200k-Tokenizer).",
        q4="Wie viel mehr Tokens braucht Deutsch als Englisch?",
        a4="Mit GPTs o200k-Tokenizer braucht Deutsch etwa 1.26× so viele Tokens wie derselbe Text auf Englisch. Der alte GPT-4-Tokenizer brauchte noch 1.50×, die Kosten für Deutsch sind also deutlich gesunken; über 27 Sprachen reicht das Verhältnis von 1.03× (vereinfachtes Chinesisch) bis 2.00× (Tschechisch).",
        more="So haben wir gemessen",
    ),
    "it": dict(
        callout="L’italiano usa circa 1.38× i token dell’inglese per lo stesso testo (misurato con il tokenizer o200k di GPT).",
        q4="Quanti token in più usa l’italiano rispetto all’inglese?",
        a4="Con il tokenizer o200k di GPT, l’italiano usa circa 1.38× i token dello stesso testo in inglese. Il vecchio tokenizer di GPT-4 ne richiedeva 1.59×, quindi il costo per l’italiano è sceso parecchio; su 27 lingue, il rapporto va da 1.03× (cinese semplificato) a 2.00× (ceco).",
        more="Come abbiamo misurato",
    ),
    "ru": dict(
        callout="Русский текст занимает примерно 1.32× токенов от того же текста на английском (замер на токенизаторе o200k от GPT).",
        q4="Во сколько раз больше токенов тратит русский язык по сравнению с английским?",
        a4="На токенизаторе o200k от GPT русский текст занимает примерно 1.32× токенов от того же текста на английском. Старому токенизатору GPT-4 требовалось 2.15×, так что стоимость для русского языка заметно снизилась; среди 27 языков соотношение варьируется от 1.03× (упрощённый китайский) до 2.00× (чешский).",
        more="Как мы измеряли",
    ),
    "uk": dict(
        callout="Український текст займає приблизно 1.88× токенів від того самого тексту англійською (виміряно на токенізаторі o200k від GPT).",
        q4="У скільки разів більше токенів використовує українська порівняно з англійською?",
        a4="На токенізаторі o200k від GPT український текст займає приблизно 1.88× токенів від того самого тексту англійською. Старому токенізатору GPT-4 потрібно було 3.15×, тож вартість для української суттєво знизилася; серед 27 мов співвідношення коливається від 1.03× (спрощена китайська) до 2.00× (чеська).",
        more="Як ми вимірювали",
    ),
    "tr": dict(
        callout="Türkçe aynı metin için İngilizcenin yaklaşık 1.47× katı token kullanır (GPT'nin o200k tokenizer'ıyla ölçüldü).",
        q4="Türkçe İngilizceye göre kaç kat daha fazla token kullanır?",
        a4="GPT'nin o200k tokenizer'ında Türkçe, aynı İngilizce metnin yaklaşık 1.47× katı token kullanır. Eski GPT-4 tokenizer'ında bu oran 2.06× idi, yani Türkçe için maliyet belirgin şekilde düştü; 27 dil genelinde oran 1.03× (Basitleştirilmiş Çince) ile 2.00× (Çekçe) arasında değişir.",
        more="Nasıl ölçtük",
    ),
    "ar": dict(
        callout="تستهلك العربية نحو 1.26× من رموز الإنجليزية للنص نفسه (قياس فعلي على مُجزّئ o200k الخاص بـ GPT).",
        q4="كم مرة تستهلك العربية رموزًا أكثر من الإنجليزية؟",
        a4="على مُجزّئ o200k الخاص بـ GPT، تستهلك العربية نحو 1.26× من رموز النص نفسه بالإنجليزية. كان مُجزّئ GPT-4 القديم يحتاج إلى 3.03×، لذا انخفضت تكلفة العربية كثيرًا؛ وعبر 27 لغة تتراوح النسبة من 1.03× (الصينية المبسطة) إلى 2.00× (التشيكية).",
        more="كيف قسنا ذلك",
    ),
    "fa": dict(
        callout="فارسی برای همان متن حدود 1.24× توکن‌های انگلیسی را مصرف می‌کند (اندازه‌گیری‌شده با توکنایزر o200k در GPT).",
        q4="فارسی چند برابر انگلیسی توکن مصرف می‌کند؟",
        a4="در توکنایزر o200k در GPT، فارسی حدود 1.24× توکن‌های همان متن انگلیسی را مصرف می‌کند. توکنایزر قدیمی GPT-4 به 2.79× نیاز داشت، پس هزینه برای فارسی بسیار کاهش یافته است؛ در میان 27 زبان این نسبت از 1.03× (چینی ساده‌شده) تا 2.00× (چکی) متغیر است.",
        more="روش اندازه‌گیری ما",
    ),
    "hi": dict(
        callout="एक ही टेक्स्ट के लिए हिंदी, अंग्रेज़ी के मुकाबले लगभग 1.50× टोकन लेती है (GPT के o200k टोकनाइज़र पर मापा गया)।",
        q4="हिंदी में अंग्रेज़ी से कितने गुना ज़्यादा टोकन लगते हैं?",
        a4="GPT के o200k टोकनाइज़र पर हिंदी, उसी अंग्रेज़ी टेक्स्ट के मुकाबले लगभग 1.50× टोकन लेती है। पुराने GPT-4 टोकनाइज़र में 4.59× लगते थे, इसलिए हिंदी की लागत काफ़ी घट गई है; 27 भाषाओं में यह अनुपात 1.03× (सरलीकृत चीनी) से 2.00× (चेक) तक है।",
        more="हमने कैसे मापा",
    ),
    "id": dict(
        callout="Bahasa Indonesia memakai sekitar 1.15× token bahasa Inggris untuk teks yang sama (diukur dengan tokenizer o200k GPT).",
        q4="Berapa kali lebih banyak token yang dipakai bahasa Indonesia dibanding bahasa Inggris?",
        a4="Pada tokenizer o200k GPT, bahasa Indonesia memakai sekitar 1.15× token dari teks yang sama dalam bahasa Inggris. Tokenizer GPT-4 lama membutuhkan 1.38×, jadi biaya untuk bahasa Indonesia turun cukup banyak; di 27 bahasa, rasionya berkisar dari 1.03× (Tionghoa Sederhana) hingga 2.00× (Ceko).",
        more="Cara kami mengukur",
    ),
    "vi": dict(
        callout="Tiếng Việt dùng khoảng 1.35× số token của tiếng Anh cho cùng một nội dung (đo trên tokenizer o200k của GPT).",
        q4="Tiếng Việt tốn gấp mấy lần token so với tiếng Anh?",
        a4="Trên tokenizer o200k của GPT, tiếng Việt dùng khoảng 1.35× số token so với cùng nội dung bằng tiếng Anh. Tokenizer GPT-4 cũ cần tới 2.32×, nên chi phí cho tiếng Việt đã giảm đáng kể; trên 27 ngôn ngữ, tỷ lệ dao động từ 1.03× (tiếng Trung giản thể) đến 2.00× (tiếng Séc).",
        more="Cách chúng tôi đo",
    ),
    "th": dict(
        callout="ข้อความเดียวกัน ภาษาไทยใช้โทเค็นประมาณ 1.74× ของภาษาอังกฤษ (วัดจริงด้วยตัวแบ่งโทเค็น o200k ของ GPT)",
        q4="ภาษาไทยใช้โทเค็นมากกว่าภาษาอังกฤษกี่เท่า?",
        a4="บนตัวแบ่งโทเค็น o200k ของ GPT ภาษาไทยใช้โทเค็นประมาณ 1.74× ของข้อความเดียวกันในภาษาอังกฤษ ตัวแบ่งโทเค็น GPT-4 รุ่นเก่าต้องใช้ถึง 3.71× ค่าใช้จ่ายสำหรับภาษาไทยจึงลดลงมาก และใน 27 ภาษา อัตราส่วนอยู่ระหว่าง 1.03× (จีนตัวย่อ) ถึง 2.00× (เช็ก)",
        more="วิธีที่เราวัด",
    ),
    "pl": dict(
        callout="Polski zużywa ok. 1.88× tokenów angielskiego dla tego samego tekstu (zmierzone na tokenizerze o200k w GPT).",
        q4="Ile razy więcej tokenów zużywa polski niż angielski?",
        a4="Na tokenizerze o200k w GPT polski tekst zużywa ok. 1.88× tokenów tego samego tekstu po angielsku. Stary tokenizer GPT-4 potrzebował 2.12×, więc koszt dla języka polskiego wyraźnie spadł; w 27 językach proporcja wynosi od 1.03× (chiński uproszczony) do 2.00× (czeski).",
        more="Jak mierzyliśmy",
    ),
    "nl": dict(
        callout="Nederlands gebruikt ongeveer 1.29× zoveel tokens als Engels voor dezelfde tekst (gemeten met de o200k-tokenizer van GPT).",
        q4="Hoeveel meer tokens gebruikt Nederlands dan Engels?",
        a4="Met de o200k-tokenizer van GPT gebruikt Nederlands ongeveer 1.29× zoveel tokens als dezelfde tekst in het Engels. De oude GPT-4-tokenizer had 1.74× nodig, dus de kosten voor Nederlands zijn flink gedaald; over 27 talen loopt de verhouding van 1.03× (vereenvoudigd Chinees) tot 2.00× (Tsjechisch).",
        more="Hoe we meten",
    ),
    "bn": dict(
        callout="একই লেখার জন্য বাংলা ইংরেজির প্রায় 1.68× টোকেন ব্যবহার করে (GPT-এর o200k টোকেনাইজারে মাপা)।",
        q4="বাংলায় ইংরেজির চেয়ে কত গুণ বেশি টোকেন লাগে?",
        a4="GPT-এর o200k টোকেনাইজারে বাংলা একই ইংরেজি লেখার প্রায় 1.68× টোকেন ব্যবহার করে। পুরোনো GPT-4 টোকেনাইজারে 6.09× লাগত, তাই বাংলার খরচ অনেক কমেছে; 27টি ভাষায় এই অনুপাত 1.03× (সরলীকৃত চীনা) থেকে 2.00× (চেক) পর্যন্ত।",
        more="আমরা কীভাবে মেপেছি",
    ),
    "ur": dict(
        callout="ایک ہی متن کے لیے اردو انگریزی کے مقابلے میں تقریباً 1.59× ٹوکن استعمال کرتی ہے (GPT کے o200k ٹوکنائزر پر ناپا گیا)۔",
        q4="اردو میں انگریزی سے کتنے گنا زیادہ ٹوکن لگتے ہیں؟",
        a4="GPT کے o200k ٹوکنائزر پر اردو اسی انگریزی متن کے مقابلے میں تقریباً 1.59× ٹوکن استعمال کرتی ہے۔ پرانے GPT-4 ٹوکنائزر میں 4.24× لگتے تھے، اس لیے اردو کی لاگت کافی کم ہو گئی ہے؛ 27 زبانوں میں یہ تناسب 1.03× (سادہ چینی) سے 2.00× (چیک) تک ہے۔",
        more="ہم نے کیسے ناپا",
    ),
    "fil": dict(
        callout="Gumagamit ang Filipino ng mga 1.53× na token kumpara sa Ingles para sa parehong teksto (sinukat sa o200k tokenizer ng GPT).",
        q4="Ilang beses na mas maraming token ang ginagamit ng Filipino kaysa Ingles?",
        a4="Sa o200k tokenizer ng GPT, gumagamit ang Filipino ng mga 1.53× na token kumpara sa parehong teksto sa Ingles. Ang lumang GPT-4 tokenizer ay nangangailangan ng 1.76×, kaya bumaba ang gastos para sa Filipino; sa 27 wika, ang ratio ay mula 1.03× (Simplified Chinese) hanggang 2.00× (Czech).",
        more="Paano namin sinukat",
    ),
    "cs": dict(
        callout="Čeština spotřebuje pro stejný text zhruba 2.00× tokenů oproti angličtině (měřeno na tokenizéru o200k od GPT).",
        q4="Kolikrát více tokenů spotřebuje čeština než angličtina?",
        a4="Na tokenizéru o200k od GPT spotřebuje čeština zhruba 2.00× tokenů oproti stejnému textu v angličtině, což je nejvíc z 27 měřených jazyků (rozsah 1.03× u zjednodušené čínštiny až 2.00× u češtiny). Starý tokenizér GPT-4 potřeboval 2.59×, takže náklady pro češtinu přesto znatelně klesly.",
        more="Jak jsme měřili",
    ),
    "sv": dict(
        callout="Svenska använder cirka 1.32× så många tokens som engelska för samma text (uppmätt med GPT:s o200k-tokenizer).",
        q4="Hur många fler tokens använder svenska jämfört med engelska?",
        a4="Med GPT:s o200k-tokenizer använder svenska cirka 1.32× så många tokens som samma text på engelska. Den gamla GPT-4-tokenizern krävde 1.50×, så kostnaden för svenska har sjunkit tydligt; över 27 språk sträcker sig förhållandet från 1.03× (förenklad kinesiska) till 2.00× (tjeckiska).",
        more="Så mätte vi",
    ),
    "he": dict(
        callout="עברית צורכת בערך פי 1.56× טוקנים מאנגלית עבור אותו טקסט (נמדד במפרק הטוקנים o200k של GPT).",
        q4="פי כמה יותר טוקנים צורכת עברית לעומת אנגלית?",
        a4="במפרק הטוקנים o200k של GPT, עברית צורכת בערך פי 1.56× טוקנים מאותו טקסט באנגלית. מפרק הטוקנים הישן של GPT-4 דרש פי 3.76×, כך שהעלות לעברית ירדה מאוד; בקרב 27 שפות היחס נע בין 1.03× (סינית מפושטת) ל-2.00× (צ'כית).",
        more="איך מדדנו",
    ),
}
