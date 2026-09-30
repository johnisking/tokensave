Aynı müşteri hizmetleri istemini 27 dile çevirdim ve tokenleri OpenAI'nin güncel tokenizer'ı o200k_base ile saydım (GPT-4o ve sonrası). İngilizce 34 token, Türkçe **50 token: İngilizcenin 1,47× katı**; 27 dil içinde en ucuzdan 17. sırada.

Türkçe sürümü:

> Aşağıdaki müşteri e-postasını üç madde halinde özetleyin ve kibar bir yanıt önerin. Müşteri, siparişin iki gün geç geldiğini ve kutuda bir ürünün eksik olduğunu söylüyor.

## Sonuçlar

| Dil | Token | İngilizceye göre | Eski GPT-4 tokenizer |
|---|---:|---:|---:|
| English | 34 | 1,00× | 1,00× |
| 简体中文 | 35 | 1,03× | 1,53× |
| Español | 40 | 1,18× | 1,29× |
| Deutsch | 43 | 1,26× | 1,50× |
| 한국어 | 49 | 1,44× | 2,50× |
| **Türkçe** | **50** | **1,47×** | **2,06×** |
| 日本語 | 61 | 1,79× | 2,21× |
| Čeština | 68 | 2,00× | 2,59× |

![Sonuçlar](/blog-language-tax-chart-v2.png)

## Neden

Tokenizer çoğunlukla İngilizce metinle eğitilir: " polite" veya " customer" gibi kelimeler tek token iken eklerle uzayan Türkçe kelimeler parçalara bölünür:

- Aşağıdaki → `A | şa | ğı | daki` · 4
- özetleyin → `ö | zet | ley | in` · 4
- e-postasını → `e | -post | asını` · 3

## Eski tokenizer'a göre

GPT-4 dönemi tokenizer'ında (cl100k) aynı istem **2,06×** tutuyordu; bugün **1,47×**.

## Parayla

Girdi için 1 milyon token başına 2 $ ücret alan bir modelde bu istemi 1 milyon kez göndermek İngilizcede 68 $, Türkçede 100 $ tutar. Yanıt da Türkçe olursa aynı çarpan, genellikle 4–5× daha pahalı olan çıktı tokenlerine de uygulanır.

## Nasıl tasarruf edilir

- Sistem istemini ve sabit talimatları İngilizce yazın; yalnızca kullanıcı girdisi Türkçe kalsın.
- Ara adımları (sınıflandırma, çıkarma, araç çağrıları) İngilizce ya da JSON olarak alın, yalnızca son yanıt Türkçe olsun.
- İstemin sabit kısmı için prompt caching kullanın.

## Sınırlamalar

- Tek bir istem ölçüldü; başka metinlerde oran ±0,1–0,2 değişebilir.
- Claude ve Gemini farklı tokenizer kullanır; bu sayılar yalnızca OpenAI modelleri için geçerlidir.
- Çeviri, kontrol edilmiş makine çevirisine dayanır.

27 dilin tüm sonuçları (İngilizce): [27 dil karşılaştırması](/blog/token-cost-27-languages)
