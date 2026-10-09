![Claude Opus 5.5 effort seviyeleri test edildi: low'dan max'e](/claude-opus-5-5-effort-tr.jpg)

Claude **Opus 5.5**'te modelin ne kadar derin düşüneceğini belirleyen bir **effort** ayarı var ve beş seviyesi bulunuyor: low, medium, high, xhigh ve max. Seviye yükseldikçe sonucun iyileşmesi bekleniyor, ancak resmi belgeler her seviyenin ne kadar ek süre ve para getirdiğine dair rakam vermiyor. Bu yüzden 9 Ekim 2026'da aynı oyun yapma isteğini her seviyede birer kez çalıştırıp süreyi, token sayısını, maliyeti ve sonucu karşılaştırdık. En hızlı seviye 32 saniye, en yavaşı 22 dakika sürdü. Aşağıda her seviyede neyin değiştiğini, hangi iş için hangi seviyenin uygun olduğunu ve gerçek kullanım deneyimini bulacaksınız.

## Effort nedir

- **Modelin ne kadar düşüneceğini belirler.** Opus 5.5'te düşünme kapatılamaz; effort bu düşünmenin derinliğini ayarlar. Düşünme tokenları çıktı tokenı olarak ücretlendirilir.
- **Varsayılan medium.** Opus 5'te varsayılan high idi; Opus 5.5'te bir seviye aşağısı olan medium (Anthropic belgelerine göre).
- **Nasıl değiştirilir:** Claude Code'da `--effort` seçeneğiyle (low'dan max'e), API'de ise `effort` değeriyle.

## Nasıl ölçtük

- **Model:** Windows PC üzerinde Claude Code'da Claude Opus 5.5
- **İstem (aynen):** "Make a brick-breaker game that runs in the browser as a single file named index.html in the current folder. It needs 2 levels, a score display and 3 lives, and it must be playable with the keyboard and the mouse. Write the file and finish." Yani mevcut klasörde index.html adlı tek dosyada, tarayıcıda çalışan, 2 bölümlü, skor göstergeli, 3 canlı ve klavye ile fareyle oynanabilen bir tuğla kırma oyunu yazıp bitirmesini istiyor.
- **Yöntem:** aynı istem beş kez, yalnızca effort değiştirilerek. Çalıştırmalar birbirini etkilemesin diye her seviye ayrı bir klasörde çalıştı.
- **Ölçüm:** token ve maliyet için ücretsiz ccusage aracı, süre için başlangıç ve bitiş zaman damgaları. Maliyet API fiyatlarıyla hesaplandı.

## Sonuçlar: süre, token ve maliyet

![Sonuçlar: süre, token ve maliyet: Effort, Süre, Çıktı tokenı, Toplam token, Maliyet, Oyun kodu](/claude-opus-5-5-effort-sonuclar-sure-token-ve-maliyet-tr.jpg)

| Effort | Süre | Çıktı tokenı | Toplam token | Maliyet | Oyun kodu |
|---|---:|---:|---:|---:|---:|
| low | 32 sn | 3,368 | 129,315 | $0.48 | 138 satır |
| medium (varsayılan) | 52 sn | 6,299 | 133,428 | $0.56 | 358 satır |
| high | 1 dk 50 sn | 12,376 | 222,854 | $0.75 | 523 satır |
| xhigh | 4 dk 32 sn | 32,435 | 472,082 | $1.36 | 639 satır |
| max | 22 dk 22 sn | 160,033 | 2,504,957 | $5.25 | 1,121 satır |

- **Low ile medium neredeyse aynı.** Low %14 daha ucuz ve %38 daha kısa sürdü, ama fark 8 sent.
- **High, medium'dan yalnızca %34 pahalı.** Süre 52 saniyeden 1 dakika 50 saniyeye çıktı.
- **Maliyetin sıçradığı yer xhigh.** Medium'dan %143 pahalı oldu ve 4 dakika 32 saniye sürdü.
- **Max bambaşka bir lig.** Medium 52 saniye ve $0.56 tuttu; max 22 dakika 22 saniye ve $5.25. Çıktı tokenı 6,299'dan 160,033'e çıktı.

![Effort seviyesine göre süre ve maliyet: 32 sn ve $0.48 ile low'dan 22 dk 22 sn ve $5.25 ile max'e](/claude-opus-5-5-effort-tr-6.jpg)

![ccusage ölçüm kaydı: beş Opus 5.5 effort seviyesinin token ve maliyetleri](/claude-opus-5-5-effort-tr-7.jpg)

## Beş oyun yan yana

![Her Opus 5.5 effort seviyesinde yapılan beş tuğla kırma oyunu yan yana](/claude-opus-5-5-effort-tr-5.jpg)

Beş oyunun hepsi hatasız çalıştı ve isteği karşıladı: 2 bölüm, skor, 3 can, klavye ve fare kontrolü. Farklar, her seviyenin bunların üstüne neler eklediğinde.

| Effort | Ne ekledi |
|---|---|
| low | Tek renkli tuğlalar, en sade ekran, duraklatma yok |
| medium | Gökkuşağı tuğlalar, duraklatma, yeniden başlatma |
| high | + parçacık efektleri, kaydedilen en yüksek skor |
| xhigh | Parçacık efektleri, daha cilalı tasarım (en yüksek skor kaydı yok) |
| max | + ses efektleri, bölüm adları, uzaylı şeklinde 2. bölüm, ekran sarsıntısı, zafer havai fişekleri |

- **High ve üstünde model kendi işini denetlemeye çalıştı.** High ve xhigh kod sözdizimi denetimi, max ise otomatik oynanış testi denedi. Üçü de çalıştırma izni gerektirdiği için hiçbiri gerçekten çalışmadı; her biri bunun yerine kodu yeniden okuduğunu söylüyor. Low ve medium denetim yapmadan bitirdi.
- **İki vuruşta kırılan tuğlalar**, biz istemediğimiz hâlde her seviyede ortaya çıktı.

## Seviye seviye inceleme

Her oyunu oynadık ve modelin sonda bıraktığı özetle ve kodun kendisiyle karşılaştırdık.

### low: 32 saniye, $0.48

![effort low ile yapılan oyunun başlangıç ekranı ve oynanışı](/claude-opus-5-5-effort-tr-11.jpg)

- **Ne yaptı:** 1. bölüm dört sıra mavi tuğla; 2. bölümde iki vuruşta kırılan turuncu tuğlalar boşluklarla karışık ve top daha hızlı. Bölüm geçme, oyun bitti ve kazanma ekranları ile yeniden başlatma var.
- **İyi:** istenen her özellik mevcut ve topun rakete çarptığı nokta açısını değiştiriyor. 32 saniyede bitti.
- **Zayıf:** siyah arka plan ve tek renkli tuğlalarla en sadesi. Duraklatma yok ve 138 satırla en kısa kod.
- **Ne zaman kullanılır:** yalnızca bir şeyin çalıştığını görmek istediğinizde ve cilayı sonraya bırakacağınızda.

### medium: 52 saniye, $0.56 (varsayılan)

![effort medium ile yapılan oyunun başlangıç ekranı ve oynanışı](/claude-opus-5-5-effort-tr-12.jpg)

- **Ne yaptı:** 1. bölüm 5×10 gökkuşağı ızgarası; 2. bölümde boşluklar ve 2 ya da 3 vuruşta kırılan, kalan vuruş sayısını gösteren ve hasar aldıkça soluklaşan tuğlalar var.
- **İyi:** duraklatma (P veya Esc), yeniden başlatma (Enter) ve pencere odağı kaybedince otomatik duraklatma. Puanlama tuğla dayanıklılığına ve bölüme göre değişiyor.
- **Zayıf:** ses ve parçacık efekti yok.
- **Ne zaman kullanılır:** çoğu zaman. Low'dan 8 sent pahalı ve belirgin şekilde daha iyi.

### high: 1 dakika 50 saniye, $0.75

![effort high ile yapılan oyunun başlangıç ekranı ve oynanışı](/claude-opus-5-5-effort-tr-13.jpg)

- **Ne yaptı:** 2. bölüm, 2 ya da 3 vuruşta kırılan tuğlalardan oluşan bir elmas deseni; tuğlalar kırılınca parçacık saçıyor.
- **İyi:** bölüm geçme bonusu, kalan can bonusu, kaydedilen en yüksek skor ve dokunmatik kontrol. Ayrıca kendi kodunda sözdizimi denetimi denedi.
- **Zayıf:** medium'dan %112 daha uzun sürdü (52 saniyeden 1 dakika 50 saniyeye).
- **Ne zaman kullanılır:** başkalarına göstereceğiniz bir prototip ya da kalitenin önemli olduğu kodlama işleri için. Medium'dan yalnızca %34 pahalı.

### xhigh: 4 dakika 32 saniye, $1.36

![effort xhigh ile yapılan oyunun başlangıç ekranı ve oynanışı](/claude-opus-5-5-effort-tr-14.jpg)

- **Ne yaptı:** 2. bölüm, ilk vuruşta çatlayan çelik tuğlalarla çevrili bir elmas. Tuğlalar renge göre 10 ile 50 puan arası değerinde.
- **İyi:** en derli toplu görünen ekran; fare ve klavyeyi karışık kullanmak sorunsuz, raketi en son kullandığınız kontrol hareket ettiriyor.
- **Zayıf:** high'daki en yüksek skor kaydını ve dokunmatik kontrolü bıraktı. Medium'dan %143 pahalıya mal oldu ama high'a göre yeni özellik eklemedi.
- **Ne zaman kullanılır:** bunun gibi küçük işler için değil. Anthropic'e göre uzun süren işlere uygun.

### max: 22 dakika 22 saniye, $5.25

![effort max ile yapılan oyunun başlangıç ekranı ve oynanışı](/claude-opus-5-5-effort-tr-15.jpg)

- **Ne yaptı:** adlandırılmış bölümler ("Rainbow Wall", "Space Invader"), 14 gümüş tuğlası iki vuruşta kırılan uzaylı şeklinde bir 2. bölüm ve 2. bölümde daha dar bir raket.
- **İyi:** ses efektleri (M ile açılıp kapanıyor), kaydedilen en yüksek skor, dokunmatik kontrol, ekran sarsıntısı, zafer havai fişekleri ve otomatik duraklatma: tüm seviyeler içinde en fazlası. Bitmiş bir oyun gibi görünüyor.
- **Zayıf:** açık ara en yavaşı; bunun bir nedeni de izin gerektiren otomatik oynanış testini çalıştırmaya çalışması.
- **Ne zaman kullanılır:** kalitenin her şeyden önemli olduğu ve yeterli zamanınızla limitinizin bulunduğu durumlarda ya da başka hiçbir şey sorunu çözemediğinde.

## Gerçek kullanım: günlük işte medium, kodlamada high

Ben oyun geliştirmek için Opus 5.5'i Claude Max 20x planında kullanıyorum. Bu bir ölçüm değil, günlük kullanımda nasıl hissettirdiği.

- **Ayarım:** effort'u auto'da bırakıyorum. Genelde medium'da çalışıyor, kod yazarken high'a çıkıyor.
- **low:** hantal geldi, birkaç kez kullanıp bıraktım.
- **high:** sonuçlar açıkça daha iyi.
- **xhigh ve max:** her birini bir kez kadar denedim, kullanmam için nadiren bir neden oluyor.

Ölçümlerle karşılaştırınca low aslında en hızlısıydı ama en sade sonucu verdi; yani hantallık hissi hızdan değil çıktıdan kaynaklanıyordu. High'ın daha iyi sonuç verdiği ve xhigh ile max'e nadiren ihtiyaç duyulduğu hissi ise rakamlarla örtüştü.

## Anthropic ne öneriyor

- **Medium güçlü.** Anthropic'in testlerinde medium'daki Opus 5.5, kodlama ve bilgi işlerinde high'daki Opus 5'i yakaladı ya da geçti.
- **Low kodlamada medium'a yaklaşıyor,** üstelik çok daha düşük maliyetle, Anthropic'e göre. Bizim testimizde çıktıdaki fark belirgindi.
- **xhigh ve max'i, kalite artışını ölçtüğünüz işlere saklayın.**
- **Sohbetin ortasında effort'u değiştirmek istem önbelleğini bozabilir.** API'de önbelleği korumak için mesaj başına effort değişikliği kullanın.
- **Bağımsız testler de aynı yönde.** Artificial Analysis, max effort'taki Opus 5.5'in görev başına Opus 5'ten %63 daha fazla çıktı tokenı kullandığını buldu (basında çıkan haberlere göre).

## Hangi iş için hangi effort

![Hangi iş için hangi effort: İş, Önerilen effort, Neden](/claude-opus-5-5-effort-hangi-is-icin-hangi-effort-tr.jpg)

Ölçümleri, kendi deneyimimi ve Anthropic'in yönergelerini birleştiren önerilerimiz:

| İş | Önerilen effort | Neden |
|---|---|---|
| Basit düzenlemeler, yeniden adlandırma, dosya toparlama | low veya medium | Hızlı ve ucuz, ama low'un çıktısı sade |
| Günlük kodlama ve yeni özellikler | medium (varsayılan) | 52 saniyede $0.56'ya kullanılabilir sonuç |
| Oyun veya uygulama prototipleri, kalitenin önemli olduğu kodlama | high | %34 ek maliyetle açıkça daha iyi çıktı |
| 30 dakikayı aşan çalıştırmalar, büyük yeniden yapılandırmalar | xhigh | Anthropic'in yönergelerine göre |
| Başka hiçbir şeyin çözemediği zor sorunlar | max | Yalnızca gerektiğinde: süre ve maliyet sıçrıyor |

- **Medium'la başlayın.** Yalnızca sonucu yetersiz kalan işleri high'a taşıyın.
- **Abonelikteyseniz limitle düşünün.** API karşılığı maliyet ne kadar yüksekse Max ya da Pro limitiniz o kadar hızlı tükenir. Tek bir max çalıştırması, dokuzdan fazla medium çalıştırması kadar harcadı.
- **Not:** her seviye için tek çalıştırma, oldukça küçük bir görevde. Daha büyük projelerde farklar başka çıkabilir.

## Sonuç: varsayılan olarak medium, önemli olduğunda high

- **Varsayılan: medium.** 52 saniyede $0.56'ya kullanılabilir sonuç.
- **Kalite önemliyse: high.** Medium'dan yalnızca %34 fazlasına açıkça daha iyi çıktı. Beşi içinde fiyatına göre en iyisi.
- **xhigh: küçük işlerde atlayın.** Medium'dan %143 pahalı ama high'dan fazla özellik yok. Yalnızca uzun çalıştırmalarda değer.
- **max: yalnızca gerektiğinde.** En gösterişli sonuç, ama 22 dakika ve $5.25.
- **low: önerilmez.** Medium'a göre 8 sent tasarruf size yalnızca daha sade bir sonuç kazandırır.

## Sık sorulan sorular

**Opus 5.5'in varsayılan effort'u nedir?**
Medium. Opus 5'te varsayılan high idi. Effort belirtmeyen API istekleri Opus 5.5'te medium ile çalışır.

**Max her zaman daha mı iyi?**
Testimizde en çok özelliği ve cilayı ekledi, ama medium'un 52 saniye ve $0.56'sına karşılık 22 dakika ve $5.25 tuttu. Basit işler için fazla.

**Low çok tasarruf sağlar mı?**
Testimizde low, medium'dan yalnızca %14 ucuzdu. Daha sade sonucu da düşünülünce medium daha iyi seçim.

## Kendi işiniz için hesaplayın

[Kodlama ajanı maliyet hesaplayıcısına](/tr/agents) görev büyüklüğünü ve günlük görev sayısını girerek Opus 5.5'te bir ayın maliyetini görün. Tek bir istemin maliyetini [token sayacında](/tr/) kontrol edin. Opus 5 ile 5.5 arasındaki fiyat ve performans farkları için [Claude Opus 5 vs 5.5 (İngilizce)](/blog/claude-opus-5-vs-5-5) yazısına bakın.

*9 Ekim 2026'da ölçüldü. Maliyet, ccusage'ın API fiyatlarıyla yaptığı hesaplamadır; sonuçlar model ve Claude Code güncellemeleriyle değişebilir.*

## Kaynaklar

- [Anthropic: Effort](https://platform.claude.com/docs/en/build-with-claude/effort#recommended-effort-levels-for-claude-opus-5-5)
- [Anthropic: Claude Opus 5.5 için istem yazma](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)
- [Anthropic: Claude Opus 5'ten Opus 5.5'e geçiş](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide)
- [OfficeChai: Artificial Analysis Intelligence Index raporu](https://officechai.com/ai/claude-opus-5-5-creates-5-point-lead-over-gpt-6-astra-jumps-to-top-spot-on-artificial-analysis-intelligence-index/)
- [ccusage: Claude Code kullanım aracı (GitHub)](https://github.com/ryoppippi/ccusage)
<!-- autoimg -->
