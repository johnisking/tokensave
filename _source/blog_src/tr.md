![Türkçe, GPT'de İngilizceden 1,47× daha fazla token harcıyor](/token-turkce-gpt-tr.jpg)

Aynı müşteri hizmetleri istemini 41 dile çevirdim ve tokenleri OpenAI'nin güncel tokenizer'ı o200k_base ile saydım (GPT-4o ve sonrası). İngilizce 34 token, Türkçe **50 token: İngilizcenin 1,47× katı**; 41 dil içinde en ucuzdan 20. sırada.

Türkçe sürümü:

> Aşağıdaki müşteri e-postasını üç madde halinde özetleyin ve kibar bir yanıt önerin. Müşteri, siparişin iki gün geç geldiğini ve kutuda bir ürünün eksik olduğunu söylüyor.

## Sonuçlar

| Dil | Token | İngilizceye göre | İngilizce gönderilirse tasarruf |
|---|---:|---:|---:|
| English | 34 | 1,00× | – |
| 简体中文 | 35 | 1,03× | 3% |
| Español | 40 | 1,18× | 15% |
| Deutsch | 43 | 1,26× | 21% |
| 한국어 | 49 | 1,44× | 31% |
| **Türkçe** | **50** | **1,47×** | **32%** |
| हिन्दी | 51 | 1,50× | 33% |
| 日本語 | 61 | 1,79× | 44% |
| Čeština | 68 | 2,00× | 50% |
| Ελληνικά | 70 | 2,06× | 51% |
| ਪੰਜਾਬੀ | 83 | 2,44× | 59% |

![Sonuçlar](/blog-language-tax-chart-v4.png)

## Neden

![Neden: Aşağıdaki → A | şa | ğı | daki · 4; özetleyin → ö | zet | ley | in · 4; e-postasını → e | -post | asını · 3](/token-turkce-gpt-tr-2.jpg)

Tokenizer çoğunlukla İngilizce metinle eğitilir: " polite" veya " customer" gibi kelimeler tek token iken eklerle uzayan Türkçe kelimeler parçalara bölünür:

- Aşağıdaki → `A | şa | ğı | daki` · 4
- özetleyin → `ö | zet | ley | in` · 4
- e-postasını → `e | -post | asını` · 3

## Tek düğmeyle İngilizceye geçin

En büyük tasarruf, isteminizi İngilizce göndermektir: Türkçeye göre yaklaşık %32 daha az token. Güncel modeller İngilizce talimatları çok iyi anlar ve isterseniz Türkçe yanıt verir. TokenSave token sayacında isteminizi yapıştırıp **💸 Token tasarrufu** düğmesine basın: boşlukları temizler, İngilizceye çevirir, gereksiz ifadeleri kırpar ve yanıt kendi dilinizde kalsın diye "Reply in Turkish." ekler. Masaüstü Chrome 138+ / Edge 148+ tarayıcılarına yerleşik çevirmeni kullanır; çeviri kendi cihazınızda yapılır ve metniniz asla yüklenmez. Orijinale dönmek için **↩ Orijinal** düğmesine basın.

## Parayla

Girdi için 1 milyon token başına 2 $ ücret alan bir modelde bu istemi 1 milyon kez göndermek İngilizcede 68 $, Türkçede 100 $ tutar. Yanıt da Türkçe olursa aynı çarpan, genellikle 4–5× daha pahalı olan çıktı tokenlerine de uygulanır.

## Nasıl tasarruf edilir

![Nasıl tasarruf edilir: Sistem istemini ve sabit talimatları İngilizce yazın; yalnızca kullanıcı girdisi Türkçe kalsın.; Ara adımları ](/token-turkce-gpt-nasl-tasarruf-edilir-tr.jpg)

- Sistem istemini ve sabit talimatları İngilizce yazın; yalnızca kullanıcı girdisi Türkçe kalsın.
- Ara adımları (sınıflandırma, çıkarma, araç çağrıları) İngilizce ya da JSON olarak alın, yalnızca son yanıt Türkçe olsun.
- İstemin sabit kısmı için prompt caching kullanın.

## Sınırlamalar

- Tek bir istem ölçüldü; başka metinlerde oran ±0,1–0,2 değişebilir.
- Claude ve Gemini farklı tokenizer kullanır; bu sayılar yalnızca OpenAI modelleri için geçerlidir.
- Çeviri, kontrol edilmiş makine çevirisine dayanır.

41 dilin tüm sonuçları (İngilizce): [41 dil karşılaştırması](/blog/token-cost-by-language)
<!-- autoimg -->
