![Claude Code, Codex ve Cursor kullanımı ve maliyeti nasıl görülür?](/claude-code-kullanim-takibi-tr.jpg)

Claude Code, abonelik sınırınıza ne kadar yaklaştığınızı gösterir ama tokenlerin nereye gittiğini pek söylemez. Oturumda `/usage` yazdığınızda 5 saatlik ve haftalık sınır için yüzde çubukları görürsünüz; API kullanıyorsanız mevcut oturumun tahmini tutarını da görürsünüz. Ancak "geçen salı ne kadar harcadım", "bu ay en çok hangi proje kullandı", "Max aboneliği token başına ödemeden gerçekten daha mı ucuzdu" gibi bir geçmişi göstermez.

Aslında bu bilgi zaten bilgisayarınızda duruyor. Claude Code her konuşmayı bir kayıt dosyasına yazar ve her yanıtta model adını ve token sayılarını tam olarak not eder. ccusage ve CodeBurn gibi komut satırı araçları bu dosyaları okuyup toplar. Ben aynı cevabı hiçbir şey kurmadan görmek istedim ve kayıtları tarayıcının içinde okuyan bir [Claude Code kullanım analizi](/tr/claude-code-usage) aracı yaptım. Codex kayıtlarını ve Cursor kullanım CSV'sini de okuyor.

Bu yazıda kullanım verilerinin nerede durduğunu, nasıl kontrol edilebileceğini ve kendi gerçek kayıtlarımı araca yüklediğimde ne çıktığını anlatıyorum. Aşağıdaki tüm rakamlar bu kayıtlardan ve 15 Ekim 2026'da kontrol ettiğim resmî fiyat listelerinden geliyor. TL tutarları yaklaşık olarak 1 dolar = 49,28 TL ile hesaplandı.

## Claude Code kullanımı nerede tutulur?

Claude Code her oturumun konuşma kaydını `~/.claude/projects/` altına kaydeder. Her proje için bir klasör oluşur ve her oturum bir `.jsonl` dosyasıdır (her satırda bir JSON). Alt ajan konuşmaları, ait oldukları oturumun yanındaki `subagents/` klasöründe durur.

| İşletim sistemi | Klasör |
|---|---|
| Windows | `%USERPROFILE%\.claude\projects` |
| Mac | `~/.claude/projects` |
| Linux | `~/.claude/projects` (CLAUDE_CONFIG_DIR ayarladıysanız içindeki `projects/`) |

Modelin her yanıtında bir `usage` bölümü vardır ve maliyeti etkileyen beş değer bulunur:

- **giriş tokenleri**: önbelleğe alınmamış yeni giriş
- **önbellek yazma tokenleri**: istem önbelleğine yeni yazılan giriş (5 dakikalık ve 1 saatlik olarak ayrılır)
- **önbellek okuma tokenleri**: önbellekten yeniden okunan giriş
- **çıkış tokenleri**: modelin yazdığı yanıt (düşünme dahil)
- **model**: örneğin `claude-opus-5-5`

İki nokta sık karıştırılır. Birincisi, aynı yanıt akış sırasında birkaç satıra yazılır ve oturumu sürdürdüğünüzde yeniden kopyalanabilir; düz toplarsanız aynı yanıtı birden fazla sayarsınız. Araç her yanıtı mesaj ve istek kimliğiyle yalnızca bir kez sayar. İkincisi, kayıtlar sonsuza kadar kalmaz. Claude Code belgelerine göre `cleanupPeriodDays` değerinden eski kayıtlar silinir ve **varsayılan değer 30 gündür**. Daha uzun bir geçmiş istiyorsanız, eski dosyalar silinmeden önce `~/.claude/settings.json` içinde bu değeri artırın.

## Claude Code kullanımını kontrol etmenin 4 yolu

![Claude Code kullanımını kontrol etmenin 4 yolu: Yöntem, Ne görürsünüz, Kurulum, Gün ve projeye göre geçmiş, Abonelik vs API, Codex ve Cursor](/claude-code-kullanim-takibi-claude-code-kullanimini-kontrol-etmenin-tr.jpg)

![Claude Code kullanımını kontrol etmenin 4 yolu: Yöntem, Ne görürsünüz, Kurulum, Gün ve projeye göre geçmiş, Abonelik vs API, Codex ve Cursor](/claude-code-kullanim-takibi-claude-code-kullanimini-kontrol-etmenin-tr.jpg)

| Yöntem | Ne görürsünüz | Kurulum | Gün ve projeye göre geçmiş | Abonelik vs API | Codex ve Cursor |
|---|---|---|---|---|---|
| Claude Code içinde `/usage` | Sınır çubukları, mevcut oturum, sınırı kullanan öğeler | Gerekmez | Yok | Yok | Yok |
| ccusage (`npx ccusage`) | Terminalde günlük, aylık ve oturum raporları | Node.js | Var | Yok | Claude Code odaklı |
| CodeBurn (`npx codeburn`) | Terminal paneli, birçok araç | Node.js | Var | Yok | Var (Cursor tahmini) |
| [TokenSave kullanım analizi](/tr/claude-code-usage) | Gün, proje, model ve araca göre maliyet, CSV | Gerekmez (tarayıcı) | Var | Var | Var |

Sınıra takılıp takılmayacağınızı görmek için doğru yer `/usage`'dır; Pro ve Max'te alt ajanlar, MCP sunucuları veya önbellek kaçırmaları gibi sınırı en çok kullanan öğeleri de gösterir. Ancak haftalar boyunca geriye bakmak için tasarlanmamıştır. Terminali seviyorsanız ccusage ve CodeBurn iyi seçeneklerdir; ikisi de aynı `.jsonl` dosyalarını okur. Tarayıcıdaki araç, Node.js kurmak istemeyenler veya abonelik ile API karşılaştırmasını tek ekranda görmek isteyenler içindir.

## Araç nasıl kullanılır?

![Dosya seçme ekranı ve Claude Code, Codex, Cursor kayıtlarının yeri](/claude-code-usage-analyzer-pick-tr.jpg)

1. [tokensave.app/tr/claude-code-usage](/tr/claude-code-usage) sayfasını açın.
2. **Klasör seç** düğmesine basıp `projects` klasörünü seçin. Windows'ta klasör seçme penceresinin adres çubuğuna `%USERPROFILE%\.claude\projects` yapıştırıp Enter'a basın. Mac'te ⌘ + Shift + G'ye basıp `~/.claude/projects` yapıştırın.
3. İsterseniz Codex için `~/.codex/sessions` klasörünü ve Cursor kullanım CSV'sini (Cursor paneli → Usage → Export CSV) de ekleyin.
4. Sonuçlara bakın. Dönemi tümü, 7 gün, 30 gün ve bu ay arasında değiştirebilir, aboneliğinizi seçerek karşılaştırma görebilirsiniz.

Klasör seçerken Chrome "Dosyalar bu siteye yüklensin mi?" diye sorabilir. Bu, klasör erişiminde tarayıcının kullandığı sabit ifadedir. Sayfa dosyaları tarayıcının dosya özelliğiyle okur ve yalnızca sayıları toplar; istemleriniz ve kodunuz sekmeden çıkmaz, hiçbir sunucuya gönderilmez.

## Kendi kayıtlarımda ne çıktı?

![Analiz sonuçları: API karşılığı maliyet, tokenler, önbellek tasarrufu ve araca göre maliyet](/claude-code-usage-analyzer-result-tr.jpg)

Üç tür kayıt yükledim: bu siteyi kurmak ve yönetmek için kullandığım Claude ajan oturumları (Claude Code ile aynı biçimde kaydedilir), bilgisayarımdaki Codex oturumları ve hesabımın Cursor kullanım CSV'si.

| Araç | Yanıt | Token | API karşılığı maliyet | Kullandığım plan |
|---|---|---|---|---|
| Claude Code (Opus 5.5) | 1.636 | 277,5 milyon | 145,90 $ (yaklaşık 7.190 TL) | Max 5× |
| Codex (GPT-5.6 Terra, GPT-6 Luna) | 108 | 6,5 milyon | 1,98 $ | Ücretsiz |
| Cursor (Grok 4.6) | 2 | 379 bin | 0,29 $ | Ücretsiz |

Claude Code kayıtları 29 Eylül ile 15 Ekim arasını kapsıyor ve aracı gerçekten kullandığım gün sayısı 10. En yoğun gün olan 8 Ekim, API fiyatlarıyla yaklaşık 39 $ tuttu.

Asıl şaşırtıcı olan tokenlerin dağılımıydı. 277,5 milyon tokenin yalnızca yaklaşık 3 bini yeni girişti. Yaklaşık 264 milyonu önbellek okuması, 10,8 milyonu önbellek yazması ve 1,8 milyonu çıkıştı. Yani **Claude Code'un "kullandığı" tokenlerin %95'ten fazlası, aynı bağlamın önbellekten yeniden okunmasıydı.** Ajan her adımda konuşmayı, açtığı dosyaları ve araç sonuçlarını yeniden gönderir; önbellek bunu ucuzlatır.

Ucuz ama bedava değil. Opus 5.5 fiyatlarıyla 145,90 $'ın dağılımı şöyle:

| Kalem | 1M token başına | Maliyetteki payı |
|---|---|---|
| Önbellek okuma | 0,20 $ | yaklaşık %36 |
| 5 dakikalık önbellek yazma | 5,00 $ | yaklaşık %34 |
| Çıkış | 20,00 $ | yaklaşık %25 |
| 1 saatlik önbellek yazma | 8,00 $ | yaklaşık %4 |
| Yeni giriş | 4,00 $ | %1'den az |

Opus 5.5'te önbellek okuma normal girişten %95 daha ucuz, ama miktar o kadar büyük ki maliyetin en büyük payı yine ona ait. Önbellek yazma da neredeyse aynı büyüklükte, çünkü her yeni dosya, araç sonucu veya uzun yanıt ucuza okunmadan önce önbelleğe yazılmak zorunda. Çıkış yalnızca 1,8 milyon token olmasına rağmen milyon başına 20 $ olduğu için faturanın dörtte birini oluşturdu.

Önbellek olmasaydı aynı önbellek okumaları normal giriş fiyatıyla yaklaşık 1.017 $ daha pahalıya gelirdi. Ekrandaki "Önbellekle tasarruf" bu tutardır.

## Claude Max değer mi? Abonelik ve API karşılaştırması

![Abonelik karşılaştırması: Claude Max 5× ile 17 gün ve aynı kullanımın API maliyeti](/claude-code-usage-analyzer-plan-tr.jpg)

Araç, seçtiğiniz aboneliği aynı dönemde aynı aracın API maliyetiyle karşılaştırır. Claude kayıtlarım 17 güne yayılıyor. Max 5× KDV hariç ayda 100 $, yani 17 günü yaklaşık 56,67 $. Aynı tokenler API'de 145,90 $ tutacaktı; yani **ödediğim ücretin yaklaşık %257'si kadar API değeri kullandım.** Yoğun ajan çalışması için abonelik, token başına ödemeden açıkça daha ucuzdu.

Kendi sonucunuza bakarken iki şeye dikkat edin:

- **Aboneliklerin sınırı var.** Pro ve Max her 5 saatte bir sıfırlanır ve haftalık bir üst sınırı da vardır. API karşılığı ücretin kat kat üstündeyse muhtemelen sınırlara sık takılıyorsunuzdur; o zaman seçenekler beklemek, üst plana geçmek veya ek kullanım satın almaktır.
- **Az kullananlar için abonelik zarar olabilir.** Codex ve Cursor kullanımım ücretsiz planlardaydı ve sırasıyla 1,98 $ ile 0,29 $ tuttu. Bu kadar Codex kullanımı için ChatGPT Plus'a (ayda 20 $) ödeseydim, ücretin altında kullanmış olurdum. Araç bu durumu turuncu gösterir.

Claude Code'u henüz kullanmadıysanız ve geçmiş yerine tahmin görmek istiyorsanız, görev büyüklüğü ve günlük görev sayısından aylık maliyeti hesaplayan [Claude Code aylık maliyet hesaplayıcı](/tr/agents) işinizi görür.

## Codex ve Cursor kullanımı

**Codex**, `~/.codex/sessions/YIL/AY/GÜN/` altında her oturum için bir `rollout-….jsonl` dosyası bırakır. Her yanıt için ayrı kullanım yazmak yerine, her adımda tüm oturumun toplamını yazar. Araç adımlar arasındaki artışı OpenAI API fiyatlarıyla, önbellekli girişi önbellek fiyatıyla hesaplar. Kayıtlarımdaki GPT-5.6 Terra milyon token başına giriş 2 $, önbellekli giriş 0,20 $ ve çıkış 12 $; GPT-6 Luna ise sırasıyla 0,10 $, 0,01 $ ve 0,50 $. Arşivlenen oturumlar aynı adla `archived_sessions/` klasörüne taşındığı için aynı dosya adı yalnızca bir kez sayılır.

**Cursor** farklı. Bilgisayarımdaki Cursor yerel veritabanını açtığımda her konuşmanın token sayısı sıfır olarak kayıtlıydı. Güncel Cursor sürümleri token sayılarını bilgisayarda tutmuyor; bu yüzden komut satırı araçları da Cursor kullanımını yalnızca metin uzunluğundan tahmin edebiliyor. Doğru kaynak Cursor panelindeki kullanım dışa aktarımı: Usage ekranında **Export CSV**'ye basınca her istek için tarih, model, önbellek yazmalı ve yazmasız giriş, önbellek okuma, çıkış ve Cursor'un aldığı ücret gelir. Araç bu ücreti olduğu gibi kullanır.

## Maliyeti düşürmek için

Maliyetin çoğunun önbellek trafiği ve çıkış olduğunu bilmek, birkaç alışkanlığı öne çıkarıyor:

- **Yeni iş için yeni oturum açın.** `/clear` eski bağlamı temizler; sonraki adımlar onu yeniden okumaz. Uzun oturumlar önceki her şey için önbellek okuma ödemeye devam eder.
- **Rutin işlerde Sonnet kullanın.** Sonnet 5.5 milyon token başına 2 $/10 $, Opus 5.5 ise 4 $/20 $; aynı oturum API fiyatlarıyla yaklaşık %50 daha ucuzdur.
- **Pahalı günlere bakın.** Günlük grafik, maliyeti hangi gün ve hangi tür işin artırdığını hemen gösterir.
- **Kullanmadığınız araçları kaldırın.** Abonelikte `/usage`, hangi MCP sunucularının ve alt ajanların sınırınızdan pay aldığını gösterir.

Sınırların kendisini [Claude Code kullanım sınırları](/tr/blog/claude-code-limit) yazısında anlattım.

## Sık sorulan sorular

**Claude Code kullanım geçmişimi nasıl görürüm?**
[Kullanım analizi](/tr/claude-code-usage) aracında `~/.claude/projects` klasörünü açın veya terminalde `npx ccusage` çalıştırın. Claude Code içindeki `/usage` geçmişi değil, mevcut sınırları gösterir.

**Araç kodumu yüklüyor mu?**
Hayır. Dosyaları tarayıcı sekmesinde okur ve yalnızca token sayılarını toplar. Hiçbir yere gönderilmez.

**API karşılığı neden aboneliğimden çok daha yüksek?**
Ajanlar her adımda tüm bağlamı yeniden okur, bu da çok büyük önbellek trafiği yaratır. Abonelikte sabit ücret ödersiniz; bu rakam aynı tokenler için token başına ödeseydiniz ödeyeceğiniz tutardır.

**Neden yalnızca son bir ay görünüyor?**
Claude Code varsayılan olarak 30 günden eski kayıtları siler. Daha uzun saklamak için `settings.json` içinde `cleanupPeriodDays` değerini artırın.

**Gemini CLI, Copilot veya Windsurf'ü okuyabilir mi?**
Henüz değil. Şu an Claude Code, Codex ve Cursor CSV'sini okuyor.

## Özet

Claude Code harcadığınız her tokeni zaten kaydediyor; zor olan bunu okumak. `/usage` sınıra ne kadar yakın olduğunuzu, `~/.claude/projects` içindeki kayıtlar ise paranın nereye gittiğini gösterir. Benim 17 günlük ajan çalışmamda tokenlerin neredeyse tamamı önbellek okumasıydı, önbellek trafiği API karşılığı maliyetin yaklaşık dörtte üçünü oluşturdu ve Max 5× ücretinin yaklaşık %257'si kadar değer sağladı. Ücretsiz planlardaki Codex ve Cursor toplamda birkaç dolar tuttu. Kendi rakamlarınızı merak ediyorsanız klasörünüzü [kullanım analizi](/tr/claude-code-usage) aracına yükleyin ve sonucu aboneliğinizle karşılaştırın.

## Kaynaklar

- [Claude Code belgeleri: .claude dizini (kayıt yeri ve 30 günlük temizlik)](https://code.claude.com/docs/en/claude-directory)
- [Claude Code belgeleri: maliyet yönetimi (/usage)](https://code.claude.com/docs/en/costs)
- [Anthropic API fiyatları (istem önbelleği)](https://platform.claude.com/docs/en/about-claude/pricing)
- [OpenAI API fiyatları](https://developers.openai.com/api/docs/pricing)
- [Claude planları](https://claude.com/pricing) · [Cursor fiyatları](https://cursor.com/pricing)
- [ccusage](https://github.com/ryoppippi/ccusage) · [CodeBurn](https://github.com/getagentseal/codeburn)
<!-- autoimg -->
