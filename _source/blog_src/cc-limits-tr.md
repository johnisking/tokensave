![Claude Code Limiti: 5 Saatlik ve Haftalık Limit Rehberi 2026](/claude-code-limit-tr.jpg)

"Claude usage limit reached" mesajı, Claude Code kullanıcılarının en sık gördüğü ve en çok kafa karıştıran uyarıdır. Çünkü **Claude Code limiti** tek bir sınır değil: aynı anda çalışan iki ayrı limit var. Bu yazıda 5 saatlik limit ile haftalık limitin nasıl işlediğini, hangi planın ne kadar kullanım verdiğini, limitinizi nasıl kontrol edeceğinizi ve limit dolunca neler yapabileceğinizi anlatıyoruz. Fiyatları dolar olarak ve Türkiye'den ödeme açısından da veriyoruz. Bilgiler 13 Ekim 2026'da Anthropic'in resmi sayfalarından kontrol edildi.

## Claude Code limiti nedir? İki ayrı limit

**1. 5 saatlik oturum limiti.** Kullanımınız 5 saatlik bir zaman penceresi içinde ölçülür. O pencere için verilen kullanım hakkını bitirirseniz, pencere sıfırlanana kadar beklemeniz gerekir.

**2. Haftalık limit.** Oturum limitine ek olarak, bir haftalık toplam kullanıma da bir üst sınır var. 5 saatlik pencereniz yeni açılmış olsa bile haftalık limite ulaştıysanız haftalık sıfırlamayı beklersiniz.

Max planlarında bunlara ek olarak **Claude Fable için ayrı bir haftalık limit** vardır. /usage ekranında bu, tüm modelleri kapsayan haftalık limitten ayrı bir satır olarak görünür.

En önemli nokta: bu limitler **Claude Code ile Claude uygulaması arasında ortaktır**. Web, masaüstü ve mobil uygulamadaki uzun bir sohbet, kodlama oturumunuzla aynı kullanım hakkından düşer. IDE içinden yapılan kullanım da aynı havuza dahildir.

## Planlara göre kullanım ve fiyat

![Planlara göre kullanım ve fiyat: Plan, Aylık fiyat (web), Kullanım, Claude Code](/claude-code-limit-planlara-gore-kullanim-ve-fiyat-tr.jpg)

Anthropic, plan limitlerini kesin token sayısıyla değil, birbirine göre oranla açıklıyor. Resmi bir mesaj veya token sayısı yayımlanmıyor.

| Plan | Aylık fiyat (web) | Kullanım | Claude Code |
|---|---|---|---|
| Free | 0 $ | Temel | Dahil değil |
| Pro | 20 $ (yıllık ödemede ayda 17 $) | Temel seviye | Dahil |
| Max 5x | 100 $ | Pro'nun %500'ü | Dahil |
| Max 20x | 200 $ | Pro'nun %2.000'i | Dahil |

Max planları yalnızca aylık ödenir, yıllık indirim yoktur. Kullanım hakkının ne kadar yeteceği tamamen ne yaptığınıza bağlıdır. Büyük dosyalar, uzun oturumlar ve Opus, Sonnet ile yapılan kısa işlere göre limiti çok daha hızlı tüketir.

### Türkiye'den ödeme: dolar, KDV ve uygulama fiyatı

- **Web üzerinden:** Anthropic dolarla ücret alır ve vergiyi fatura adresine göre hesaplar. Türkiye fatura adresiyle %20 KDV eklenir; Pro yaklaşık 24 $ tutar. Son tutar ödeme ekranında görünür ve bankanız doları kendi kuruyla TL'ye çevirir. Kur için referans: 1 USD ≈ 49 TL (1 Ekim 2026).
- **App Store ve Google Play üzerinden:** Anthropic, fiyatların web aboneliği için olduğunu ve mobil fiyatların platforma göre değişebileceğini belirtiyor. [Webtekno'nun haberine göre](https://www.webtekno.com/claude-app-store-paket-fiyatlari-zamlandi-h219478.html) App Store'da Pro 999,99 TL, Max 5x 6.999,99 TL, Max 20x 12.999,99 TL. Satın almadan önce mağazadaki güncel fiyatı kontrol edin.

Tüm yapay zeka aboneliklerinin TL karşılaştırması için [Türkiye'de yapay zeka abonelik fiyatları](/tr/blog/yapay-zeka-abonelik-fiyatlari) yazımıza bakın.

## 2026'da limitlerde neler değişti?

Anthropic 2026'da Claude Code limitlerini birkaç kez değiştirdi. Haberlere göre Mayıs 2026'da Pro, Max, Team ve koltuk bazlı Enterprise planlarında 5 saatlik limitler artırıldı ve Pro ile Max'te yoğun saatlerdeki ek kısıtlama kaldırıldı. Yaz boyunca haftalık limitlerde geçici bir artış uygulandı. Eylül 2026'da ise standart haftalık limitler kalıcı olarak %25 artırıldı; bu artış geçici yaz artışının yerini aldığı için, Eylül ortasından beri haftalık limite yazdan daha erken ulaşıyorsanız bu beklenen bir durum. Haberlere göre bu, orijinal seviyeye göre %25 fazla ama yaz dönemindeki geçici seviyeye göre yaklaşık %17 daha az kullanım demek. Bu tarihler Anthropic'in yardım sayfalarında ayrıca yer almıyor.

Limitler sık değiştiği için güncel kuralları her zaman Anthropic'in [Claude Code plan yardım sayfasından](https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan) kontrol edin.

## Limitinizi nasıl kontrol edersiniz? /usage komutu

![Limitinizi nasıl kontrol edersiniz? /usage komutu: Satır, Ne demek, Bizim değerimiz, Sıfırlanma](/claude-code-limit-limitinizi-nasil-kontrol-edersiniz-usage-tr.jpg)

Claude Code içinde **/usage** yazın. Kendi Max 5x hesabımızda 13 Ekim 2026'da gördüğümüz rapor şöyleydi:

| Satır | Ne demek | Bizim değerimiz | Sıfırlanma |
|---|---|---|---|
| session | 5 saatlik oturum limiti | %10 kullanıldı | Aynı gün 15:10 UTC |
| weekly_all | Tüm modeller için haftalık limit | %59 kullanıldı | 15 Ekim 10:00 UTC |
| weekly_scoped | Modele özel haftalık limit (Max'te ayrı tutulan) | %0 kullanıldı | 15 Ekim 10:00 UTC |

Rapor ayrıca o oturumdaki token dağılımını da gösteriyor. Opus 5.5 ile çalıştığımız oturumda doğrudan yazdığımız giriş yalnızca **138 token**, modelin çıktısı **4,7 bin token**, önbellekten okunan bağlam ise **20,7 milyon token** idi. Yani limiti tüketen şey yazdığınız istem değil, Claude Code'un her adımda yeniden okuduğu bağlam. Bu yüzden aşağıdaki "bağlamı küçük tutma" önerileri limiti en çok uzatan şeyler.

**/status** ile karıştırmayın: /status hesabınızı, planınızı (ör. Max 5x), kullanılan modeli ve bağlı MCP sunucularının sayısını gösterir, ama kullanım yüzdesini göstermez. Limit için doğru komut /usage.

Claude Code ayrıca bir limite yaklaştığınızda sizi uyarır. Uzun bir işe başlamadan önce /usage'a bakın, işin ortasında değil.

## Limit ne zaman sıfırlanır?

- **5 saatlik limit:** pencere, o pencerede gönderdiğiniz ilk istemle başlar ve 5 saat sonra kapanır. Saat başına veya gün başına hizalanmaz; /usage tam sıfırlanma saatini gösterir.
- **Haftalık limit:** bizim hesabımızda her iki haftalık limit de aynı sabit zamanda (perşembe 10:00 UTC, Türkiye saatiyle 13:00) sıfırlanıyor. Bu zaman hesaba göre değişebilir; kendi hesabınızınkini /usage'da görürsünüz. Pazartesi sıfırlandığını varsaymayın.
- **/clear limiti sıfırlamaz.** /clear yalnızca konuşma bağlamını temizler. Sonraki adımlar daha az token harcar, ama harcanmış kullanım geri gelmez.

## Hangi limite takıldınız?

![Hangi limite takıldınız?: Dolan limit, Model değiştirmek işe yarar mı?, En hızlı çözüm](/claude-code-limit-hangi-limite-takildiniz-tr.jpg)

Ne yapacağınız, hangi limitin dolduğuna bağlı. Önce /usage'a bakın:

| Dolan limit | Model değiştirmek işe yarar mı? | En hızlı çözüm |
|---|---|---|
| 5 saatlik oturum | Hayır, tüm modeller aynı limitten düşer | Sıfırlanmayı bekleyin veya kullanım kredisini açın |
| Haftalık (tüm modeller) | Hayır | Kullanım kredisi, API veya plan yükseltme |
| Modele özel haftalık | Evet, aynı bağlamla devam edersiniz | /model ile Sonnet'e geçin |

### "Usage limit reached" ile 429 hatası aynı şey değil

- **"Claude usage limit reached"** ve sıfırlanma saati: aboneliğinizin (Pro/Max) 5 saatlik veya haftalık limiti doldu. Beklemek veya yukarıdaki çözümler gerekir.
- **429 / rate_limit_error:** Claude Code'u API anahtarıyla kullanıyorsanız, hesabınızın dakika başına istek veya token sınırına takıldınız demektir. Bu genellikle kısa bir beklemeyle geçer; plan limitinizle ilgili değildir.

## Limit dolduğunda ne yapmalı?

1. **Sıfırlanmayı bekleyin.** 5 saatlik limitte bu genellikle birkaç saat demektir.
2. **Kullanım kredisini açın.** Pro ve Max planlarında kullanım kredilerini açarsanız, limite ulaştığınızda durmak yerine ayrıca ücretlendirilerek devam edebilirsiniz. Max'te bu; 5 saatlik, haftalık ve Fable haftalık limitlerinin hepsi için geçerlidir.
3. **API'ye geçin.** Claude Code, kullandıkça öde API faturalandırmasıyla da çalışabilir.
4. **Planınızı yükseltin.** Pro'dan Max 5x'e veya Max 5x'ten Max 20x'e.
5. **Görev başına daha az token kullanın.** Çoğu zaman en ucuz çözüm budur. Aşağıya bakın.

## Limit neden beklediğinizden hızlı doluyor?

- **Uzun oturumlar.** Claude Code her adımda o ana kadar olan her şeyi modele yeniden gönderir. İki saatlik bir oturum, her yeni adıma çok büyük bir bağlam taşır.
- **Opus.** Kullanım hakkını Sonnet'ten daha hızlı tüketir.
- **Görünmeyen bağlam.** CLAUDE.md, kurallar ve özellikle bağlı MCP sunucularının araç tanımları her istekle birlikte gönderilir. Kullanmadığınız bir MCP sunucusu bile her adımda token harcatır. Bağlamın neyle dolduğunu **/context** komutuyla görebilirsiniz.
- **Büyük dosyalar ve loglar.** 3.000 satırlık bir dosya veya tam bir test logu okumak on binlerce token ekler.
- **Belirsiz görevler.** "Projeyi temizle" onlarca adım sürebilir; "auth.py'deki başarısız testi düzelt" birkaç adım sürer.
- **Uygulamayı aynı anda kullanmak.** İkisi de aynı havuzdan düşer.
- **Türkçe istemler.** Türkçe metinler genellikle İngilizceden daha fazla token harcar; GPT'nin tokenizer'ında aynı metin %47 daha fazla token tutuyor. Ayrıntılar [Türkçe metinler neden daha fazla token harcar](/tr/blog/token-turkce-gpt) yazımızda.

## Limiti uzatmanın yolları

- Birbiriyle ilgisiz işler arasında yeni bir oturum başlatın (**/clear**), uzun bir oturumu **/compact** ile özetleyin.
- Claude'un dosya aramasına izin vermek yerine doğru dosyaları siz gösterin.
- CLAUDE.md talimatlarınızı kısa tutun: her adımda yeniden gönderilirler.
- Kullanmadığınız MCP sunucularını kapatın. Kaç sunucunun bağlı olduğunu /status, bağlamı neyin doldurduğunu /context gösterir.
- **/model opusplan** ayarı planlamayı Opus'a, uygulamayı Sonnet'e yaptırır. Opus'un kalitesini planlamada alırken kullanım hakkını daha yavaş tüketirsiniz.
- Rutin işler için Sonnet kullanın, Opus'u zor problemlere saklayın. Effort ayarının token kullanımına etkisini [Opus 5.5 effort seviyeleri](/tr/blog/claude-opus-5-5-effort) yazımızda test ettik.

## Team ve Enterprise planlarında limit

Şirket hesaplarında da Claude Code limitleri koltuk (seat) başına işler:

- **Team ve koltuk bazlı Enterprise:** Premium koltuklar Standard koltuklardan daha yüksek kullanım verir. Limit dolduğunda, hesap sahibi **ek kullanımı** açabilir; ek kullanım API fiyatlarıyla ücretlendirilir ve sahip, kuruluş, koltuk türü veya kişi bazında aylık harcama sınırı koyabilir.
- **Kullanım bazlı Enterprise:** dahil kullanım yoktur; ilk tokendan itibaren API fiyatlarıyla ücretlendirilir.

Ekip için plan seçiyorsanız, yoğun Claude Code kullanan geliştiricilere Premium koltuk vermek, herkese ek kullanım açmaktan genellikle daha öngörülebilirdir.

## Abonelik mi, API mi?

![Abonelik mi, API mi?: Model, Giriş, Çıkış, Önbellekten okunan giriş](/claude-code-limit-abonelik-mi-api-mi-tr.jpg)

Claude Code'u API ile kullanırsanız plan limiti yoktur, ama her token ücretlendirilir. API fiyatları (1 milyon token başına, 13 Ekim 2026):

| Model | Giriş | Çıkış | Önbellekten okunan giriş |
|---|---|---|---|
| Claude Haiku 4.5 | 1 $ | 5 $ | 0,10 $ |
| Claude Sonnet 5.5 | 2 $ | 10 $ | 0,10 $ |
| Claude Opus 5.5 | 4 $ | 20 $ | 0,20 $ |

Claude Code her adımda bağlamın büyük kısmını önbellekten okuduğu için gerçek maliyet, liste fiyatından çok daha düşüktür.

**Gerçek bir oturumun API karşılığı.** Yukarıdaki /usage raporundaki Opus 5.5 oturumunu resmi API fiyatlarıyla hesapladık:

| Kalem | Token | Fiyat (1M token) | Tutar |
|---|---|---|---|
| Önbellekten okunan bağlam | 20,7 milyon | 0,20 $ | 4,14 $ |
| Önbelleğe yazma (5 dakikalık) | 374,2 bin | 5 $ | 1,87 $ |
| Çıkış | 4,7 bin | 20 $ | 0,09 $ |
| Doğrudan giriş | 138 | 4 $ | 0,00 $ |
| **Toplam** | | | **yaklaşık 6,1 $** |

Raporu aldığımız anda Max 5x'in 5 saatlik limitinin yalnızca %10'u kullanılmıştı. Aynı işi API ile her gün yapsaydık ayda 22 iş gününde yaklaşık 134 $ öderdik; Max 5x ise 100 $. Günde bir kez bile böyle bir oturum açıyorsanız abonelik API'den ucuza geliyor. Ekim 2026'da çıkan Claude Haiku 5.5 çok daha ucuz (1 milyon giriş tokenı 0,10 $), ancak Claude Code'da kullanılabildiği resmi olarak belirtilmemiş.

[Kodlama ajanı maliyet modelimize](/tr/agents) göre, önbellek açıkken bir görevin API maliyeti:

| Görev | Adım | Haiku 4.5 | Sonnet 5.5 | Opus 5.5 |
|---|---|---|---|---|
| Küçük düzeltme | ~8 | 0,08 $ | 0,14 $ | 0,27 $ |
| Yeni özellik | ~25 | 0,36 $ | 0,57 $ | 1,14 $ |
| Büyük refaktör | ~60 | 1,33 $ | 1,91 $ | 3,82 $ |

Ayda 22 iş günü varsayımıyla:

| Kullanım | Aylık görev | API (Sonnet) | API (Opus) | Genelde yeten en ucuz plan |
|---|---|---|---|---|
| Hafif: günde 3 küçük düzeltme | 66 | ~9 $ | ~18 $ | API veya Pro (20 $) |
| Düzenli: günde 5 özellik | 110 | ~63 $ | ~125 $ | Pro veya Max 5x |
| Yoğun: günde 15 özellik | 330 | ~188 $ | ~375 $ | Max 5x veya Max 20x |

Nasıl karar verilir:

1. **Haftada birkaç kez kod yazıyorsanız Pro ile başlayın.**
2. **Limite ne sıklıkla takıldığınızı izleyin.** Çoğu hafta takılıyorsanız Max 5x, ek işi API fiyatıyla ödemekten muhtemelen daha ucuzdur.
3. **Otomasyon, CI veya çok düzensiz kullanım için API kullanın.**
4. **Modeli göreve göre seçin.** Sonnet çoğu kodlama işini halleder; Opus token başına %100 daha pahalı.

Kendi kullanımınızı [kodlama ajanı maliyet hesaplayıcısına](/tr/agents) girin; API maliyetini Pro ve Max ile yan yana görün. Sohbet kullanımı için [abonelik mi API mi hesaplayıcısı](/tr/plans) da var.

## Sık Sorulan Sorular

**Claude Code ücretsiz mi?**
Hayır. Claude'un ücretsiz planında Claude Code yok. En ucuz seçenek Pro planı (aylık 20 $) veya kullandıkça öde API.

**5 saatlik limit nedir, ne zaman sıfırlanır?**
Pencere, ilk isteminizle başlar ve 5 saat sonra kapanır. Tam sıfırlanma saatini /usage gösterir.

**Haftalık limit ne zaman sıfırlanır?**
Hesabınıza ait sabit bir zamanda; bizim hesabımızda perşembe 10:00 UTC. Kendi zamanınızı /usage'da görürsünüz.

**Model değiştirmek limiti sıfırlar mı?**
Yalnızca modele özel haftalık limit dolduysa işe yarar; /model ile başka bir modele geçip devam edersiniz. 5 saatlik limit ve tüm modeller için haftalık limit, modelden bağımsızdır.

**API anahtarıyla kullanırsam limit var mı?**
Pro/Max plan limitleri yoktur; her token ücretlendirilir. Yalnızca API hesabınızın dakika başına istek ve token sınırları geçerlidir.

**Türkçe istem yazmak limiti daha hızlı mı bitirir?**
Çok az. Türkçe metin İngilizceden daha fazla token tutar, ama bizim oturumumuzda doğrudan yazılan giriş 138 token, önbellekten okunan bağlam ise 20,7 milyon tokendı. Limiti asıl tüketen, Claude Code'un okuduğu dosyalar ve biriken bağlam; istemin dili değil.

**/clear limiti sıfırlar mı?**
Hayır. Yalnızca bağlamı temizler; sonraki adımlar daha az token harcar ama kullanılan hak geri gelmez.

**Claude Code ve Claude uygulaması aynı limiti mi kullanıyor?**
Evet. Web, masaüstü, mobil uygulama, Claude Code ve IDE kullanımı aynı limitten düşer.

**Limite takılınca ne yapmalıyım?**
Bekleyebilir, kullanım kredisini açabilir, API'ye geçebilir veya planınızı yükseltebilirsiniz. Uzun vadede en ucuz çözüm genellikle görev başına daha az token kullanmaktır.

**Pro mu Max mı almalıyım?**
Haftada birkaç kez kullanıyorsanız Pro yeterli. Çoğu hafta limite takılıyorsanız Max 5x'e, tüm gün ajan çalıştırıyorsanız Max 20x'e bakın.

**Türkiye'de Claude Pro kaç TL?**
Web'de 20 $ + %20 KDV, yani yaklaşık 24 $; TL tutarı bankanızın kuruna göre değişir. Haberlere göre App Store'da 999,99 TL.

## Kaynaklar

- [Claude planları ve fiyatlandırma (Anthropic)](https://claude.com/pricing)
- [Max planı nedir? (Claude Yardım Merkezi)](https://support.claude.com/en/articles/11049741-what-is-the-max-plan)
- [Claude Code'u Pro veya Max planıyla kullanma (Claude Yardım Merkezi)](https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan)
- [Claude API fiyatlandırması (Anthropic belgeleri)](https://platform.claude.com/docs/en/about-claude/pricing)
- [Claude Haiku 5.5 (Anthropic)](https://anthropic.com/claude-haiku-5-5)
- [Faturalandırma adresi ve vergi (Claude Yardım Merkezi)](https://support.claude.com/en/articles/12997130)
- [Claude Code'da modeller ve kullanım limitleri (Claude Yardım Merkezi)](https://support.claude.com/en/articles/14552983-models-usage-limits-in-claude-code)
- [Team ve Enterprise planlarında ek kullanım (Claude Yardım Merkezi)](https://support.claude.com/en/articles/12005970-extra-usage-for-team-and-seat-based-enterprise-plans)
- [Claude Code'u Team veya Enterprise planıyla kullanma (Claude Yardım Merkezi)](https://support.claude.com/en/articles/11845131-using-claude-code-with-your-team-or-enterprise-plan)
<!-- autoimg -->
