![Türkçe, GPT'de İngilizceden %47 daha fazla token harcıyor](/token-turkce-gpt-tr.jpg)

Aynı müşteri hizmetleri istemini 41 dile çevirdim ve tokenleri OpenAI'nin güncel tokenizer'ı o200k_base ile saydım (GPT-4o ve sonrası). İngilizce 34 token, Türkçe **50 token: İngilizceden %47 fazla**; 41 dil içinde en ucuzdan 20. sırada.

*Ölçüm: Ekim 2026, OpenAI'nin o200k_base tokenizer'ı (GPT-4o ve sonraki modeller).*

Türkçe sürümü:

> Aşağıdaki müşteri e-postasını üç madde halinde özetleyin ve kibar bir yanıt önerin. Müşteri, siparişin iki gün geç geldiğini ve kutuda bir ürünün eksik olduğunu söylüyor.

## Sonuçlar

| Dil | Token | İngilizceye göre | İngilizce gönderilirse tasarruf |
|---|---:|---:|---:|
| English | 34 | ±0% | – |
| 简体中文 | 35 | +3% | 3% |
| Español | 40 | +18% | 15% |
| Deutsch | 43 | +26% | 21% |
| 한국어 | 49 | +44% | 31% |
| **Türkçe** | **50** | **+47%** | **32%** |
| हिन्दी | 51 | +50% | 33% |
| 日本語 | 61 | +79% | 44% |
| Čeština | 68 | +100% | 50% |
| Ελληνικά | 70 | +106% | 51% |
| ਪੰਜਾਬੀ | 83 | +144% | 59% |

![Grafik: GPT'de her dilin İngilizceye göre fazladan harcadığı tokenler (41 dil)](/blog-language-tax-chart-v5.png)

## Diğer dillerle karşılaştırınca

Türkçe bu listede ortalarda yer alıyor. Aynı istem İspanyolcada İngilizceden %18, Almancada %26 fazla token tutarken Türkçede fark %47'ye çıkıyor. Korece (%44) ve Hintçe (%50) Türkçeye yakın. Japonca (%79), Çekçe (%100), Yunanca (%106) ve Pencapça (%144) ise çok daha pahalı. Yani Türkçe, Latin alfabesi kullanan diller arasında pahalı tarafta, ama Asya ve Hint dillerinin çoğundan daha ucuz. Fark büyük ölçüde dilin yapısından geliyor: kelimeye çok sayıda ek alan diller, tokenizer'ın sözlüğünde daha az hazır parça buluyor.

## Neden

![Neden: Aşağıdaki → A | şa | ğı | daki · 4; özetleyin → ö | zet | ley | in · 4; e-postasını → e | -post | asını · 3](/token-turkce-gpt-tr-2.jpg)

Tokenizer çoğunlukla İngilizce metinle eğitilir: " polite" veya " customer" gibi kelimeler tek token iken eklerle uzayan Türkçe kelimeler parçalara bölünür:

- Aşağıdaki → `A | şa | ğı | daki` · 4
- özetleyin → `ö | zet | ley | in` · 4
- e-postasını → `e | -post | asını` · 3

## Tek düğmeyle İngilizceye geçin

En büyük tasarruf, isteminizi İngilizce göndermektir: Türkçeye göre yaklaşık %32 daha az token. Güncel modeller İngilizce talimatları çok iyi anlar ve isterseniz Türkçe yanıt verir. [TokenSave token sayacında](/tr/) isteminizi yapıştırıp **💸 Token tasarrufu** düğmesine basın: boşlukları temizler, İngilizceye çevirir, gereksiz ifadeleri kırpar ve yanıt kendi dilinizde kalsın diye "Reply in Turkish." ekler. Masaüstü Chrome 138+ / Edge 148+ tarayıcılarına yerleşik çevirmeni kullanır; çeviri kendi cihazınızda yapılır ve metniniz asla yüklenmez. Orijinale dönmek için **↩ Orijinal** düğmesine basın.

## Parayla

Girdi için 1 milyon token başına 2 $ ücret alan bir modelde bu istemi 1 milyon kez göndermek İngilizcede 68 $, Türkçede 100 $ tutar. Yanıt da Türkçe olursa aynı fark, genellikle %300–400 daha pahalı olan çıktı tokenlerine de uygulanır.

## Bu ne anlama geliyor?

%47 fark küçük bir istemde birkaç token gibi görünür, ama sabit bir sistem istemi her mesajda yeniden gönderildiği için birikir. İngilizcede 2.000 token tutan bir sistem istemi, Türkçeye çevrildiğinde aynı ölçüyle yaklaşık 2.940 token olur. Günde binlerce istek alan bir sohbet botunda bu, girdi faturasının neredeyse yarısı kadar ek maliyet demek.

Fark yalnızca para değil. Bağlam penceresi token ile ölçüldüğü için, aynı pencereye Türkçe metinden yaklaşık %32 daha az içerik sığar. Uzun bir belgeyi özetletirken ya da uzun bir sohbeti sürdürürken Türkçe metin pencerenin sınırına daha erken ulaşır.

ChatGPT veya Claude aboneliği kullanıyorsanız token başına ödeme yapmazsınız; bu fark asıl olarak API ile uygulama geliştirenlerin faturasında görünür. Abonelik ile API arasında karar vermek için [yapay zeka abonelik fiyatları](/tr/blog/yapay-zeka-abonelik-fiyatlari) yazısına bakabilirsiniz.

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

41 dilin tamamını yan yana [dil tablosunda](/languages) görebilirsiniz.

## Sık sorulan sorular

**Türkçe neden daha fazla token harcıyor?**
Tokenizer'lar çoğunlukla İngilizce metinle eğitilir. Türkçe kelimeler eklerle uzadığı için ("özetleyin", "e-postasını") birkaç parçaya bölünür. İngilizcede aynı anlam çoğu zaman tek token olan kısa kelimelerle yazılır.

**İsteği İngilizce yazıp cevabı Türkçe alabilir miyim?**
Evet. İsteğin sonuna "Reply in Turkish." eklemeniz yeterli. Güncel modeller İngilizce talimatı anlayıp Türkçe yanıt verir. Bu ölçümde istemi İngilizce göndermek yaklaşık %32 daha az token kullanıyor.

**Bu sonuç Claude ve Gemini için de geçerli mi?**
Hayır, bu sayılar yalnızca OpenAI'nin o200k_base tokenizer'ı için geçerli. Claude ve Gemini farklı tokenizer kullanır. Kendi metninizi [token hesaplayıcısına](/tr/) yapıştırarak modelleri karşılaştırabilirsiniz.

**ChatGPT aboneliğim etkilenir mi?**
Abonelikte token başına ödeme olmadığı için faturanız değişmez. Fark, API'yi kullanarak kendi uygulamasını geliştirenlerin ödediği tutarda ortaya çıkar.

## Kaynaklar

- [tiktoken: OpenAI tokenizer’ı (o200k_base), GitHub](https://github.com/openai/tiktoken)
- [OpenAI API fiyatları](https://developers.openai.com/api/docs/pricing)

<!-- autoimg -->
