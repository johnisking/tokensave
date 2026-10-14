![Yapay zeka ile oyun yapmak kaç para? Maliyet ve süre (2026)](/yapay-zeka-ile-oyun-yapmak-maliyet-tr.jpg)

Yapay zeka ile oyun yapmak kaç para tutar? Bu soruyu en çok, hiç kod yazmadan kendi mobil oyununu çıkarmak isteyenlerden duyuyoruz. Ben de kodlama geçmişi olmadan başladım: oyunu yapay zekaya anlatarak yaptım ve Google Play'de yayımladım. Sonra herkesin kendi oyununu hesaplayabilmesi için ücretsiz bir [yapay zeka ile oyun maliyeti hesaplayıcısı](/tr/ai-game-cost-calculator) yaptım. Bu yazıdaki bütün rakamlar o hesaplayıcıdan ve kendi oyunumdan geliyor.

Fiyatlar 5 Ekim 2026 itibarıyla kontrol edildi. Araçların neredeyse hepsi dolarla fatura kesiyor; TL karşılıkları 1 USD ≈ 49,3 TL kuruyla, KDV hariç ve yuvarlanmış olarak verildi. Mağaza kayıt ücreti (Google Play 25 dolar) tablolara dahil değil, ayrıca anlatıyorum.

## Yapay zeka ile oyun yaparken neye para ödersiniz?

Tek başına yapılan bir 2D mobil oyunun maliyeti dört kalemden oluşur:

- **Görseller**: karakterler, animasyon kareleri, arka planlar, eşyalar ve arayüz. Midjourney, Gemini veya Leonardo gibi araçlarla üretilir.
- **Müzik ve ses efektleri**: Suno, ElevenLabs ya da Pixabay gibi ücretsiz kütüphaneler.
- **Kod**: Claude Code, Cursor veya Gemini CLI gibi bir yapay zeka kodlama ajanı. Siz ne istediğinizi anlatırsınız, ajan kodu yazar.
- **Mağaza ve sunucu**: Google Play, App Store veya Steam ücreti; çevrim içi oyunlarda sunucu.

Çoğu kişi en pahalı kalemin görseller olduğunu düşünür. Hesaplayıcının sonucu farklı: paranın büyük kısmı kodlama aboneliğine gidiyor. Aşağıda nedenini rakamlarla gösteriyorum.

## Boyuta göre maliyet ve süre ne kadar?

![Boyuta göre maliyet ve süre ne kadar?: Boyut, Süre, Görsel sayısı, Maliyet (USD), Maliyet (TL, yaklaşık)](/yapay-zeka-ile-oyun-yapmak-maliyet-boyuta-gore-maliyet-ve-sure-ne-kadar-tr.jpg)

Hesaplayıcının boyut referansları, tek bir kişinin yapay zeka kodlama ajanlarıyla yaptığı gerçek mobil oyunlar: küçük bir oyun yaklaşık 2 hafta, orta boy yaklaşık 4 hafta, büyük yaklaşık 6 hafta sürdü. Aşağıdaki tablo bir merge (birleştirme) oyunu için, **Standart** araç setiyle (Midjourney + Suno + ElevenLabs + Claude Max 5×), Android'de, kodlama deneyimi olmadan ve tam zamanlı çalışma varsayımıyla hesaplandı.

| Boyut | Süre | Görsel sayısı | Maliyet (USD) | Maliyet (TL, yaklaşık) |
|---|---|---|---|---|
| Küçük | 14–23 gün | 86 | 107–151 $ | 5.270–7.440 TL |
| Orta | 26–43 gün | 196 | 107–283 $ | 5.270–13.950 TL |
| Büyük | 39–63 gün | 358 | 214–434 $ | 10.550–21.390 TL |
| Çok büyük | 81–131 gün | 675 | 308–698 $ | 15.180–34.400 TL |

Orta boyda aralığın bu kadar geniş olmasının sebebi abonelik ayları. Oyunu 26 günde bitirirseniz bir aylık kodlama aboneliği ödersiniz, 43 gün sürerse iki ay ödersiniz. Yani yapay zeka ile oyun yaparken para token başına değil, **ay başına** gidiyor ve geciken her ay yeni bir fatura demek.

## Para nereye gidiyor?

![Para nereye gidiyor?: Kalem, Aylık ücret, Pay](/yapay-zeka-ile-oyun-yapmak-maliyet-para-nereye-gidiyor-tr.jpg)

Küçük bir merge oyununu Standart setle yaparken bir aylık kalemler şöyle:

| Kalem | Aylık ücret | Pay |
|---|---|---|
| Kod (Claude Max 5×, 1 ay) | 100 $ (≈ 4.930 TL) | yaklaşık %79 |
| Görseller (Midjourney Basic) | 10 $ (≈ 490 TL) | yaklaşık %8 |
| Müzik (Suno Pro) | 10 $ (≈ 490 TL) | yaklaşık %8 |
| Ses efektleri (ElevenLabs Starter) | 6 $ (≈ 300 TL) | yaklaşık %5 |

86 görsel, beklediğinizden ucuzdur. Kullandığınız her görsel için üç tane ürettiğinizi varsaysak bile Midjourney'nin en ucuz planı yetiyor. Kodlama ajanı ise bütün gün çalışıyor ve projenizi tekrar tekrar okuyor; bu yüzden kullanım sınırı geniş bir plan gerekiyor.

Aynı kodlamayı API ile yapsaydınız hesaplayıcının tahmini yaklaşık 248 milyon token, yani Claude Sonnet 5.5 ile yaklaşık 143 dolar (≈ 7.050 TL). Her gün kod yazan biri için abonelik daha ucuza geliyor. Token'ın ne olduğunu ve Türkçenin neden daha fazla token harcadığını [Türkçe token ölçümümüzde](/tr/blog/token-turkce-gpt) anlattık.

## Oyun türü maliyeti nasıl değiştirir?

![Oyun türü maliyeti nasıl değiştirir?: Tür (küçük oyun), Süre, Görsel sayısı, En ucuz set, Standart set](/yapay-zeka-ile-oyun-yapmak-maliyet-oyun-turu-tr.jpg)

Aynı "küçük" boyutta bile tür değişince görsel ve kod miktarı çok değişiyor:

| Tür (küçük oyun) | Süre | Görsel sayısı | En ucuz set | Standart set |
|---|---|---|---|---|
| Hiper-casual | 6–10 gün | 47 | 25–35 $ | 107–151 $ |
| Merge | 14–23 gün | 86 | 32–45 $ | 107–151 $ |
| RPG | 20–32 gün | 119 | 37–77 $ | 107–283 $ |

RPG'de daha fazla karakter ve animasyon karesi olduğu için merge oyununa göre yaklaşık %38 daha fazla görsel gerekiyor. Takvim de uzadığı için ikinci bir abonelik ayı eklenebiliyor. Hiper-casual oyunlar ise bir haftada bitebiliyor.

## Hangi araç seti: En ucuz, Standart mı En iyi mi?

![Yapay zeka ile oyun maliyeti hesaplayıcısında En ucuz, Standart ve En iyi araç setlerinin TL sonuçları](/yapay-zeka-oyun-maliyeti-arac-setleri-tr.jpg)

Hesaplayıcı üç hazır set arasında tek tıkla geçiş yapıyor:

- **En ucuz**: Gemini (Nano Banana 2) ile görseller + Pixabay'den ücretsiz müzik ve efektler + kod için Google AI Pro (Gemini CLI). Küçük merge oyunu için 32–45 dolar (≈ 1.580–2.220 TL).
- **Standart**: Midjourney + Suno + ElevenLabs + Claude Max 5×. 107–151 dolar (≈ 5.270–7.440 TL).
- **En iyi**: Midjourney + AIVA Pro + ElevenLabs + Claude Max 20×. 214–302 dolar (≈ 10.550–14.880 TL).

En ucuz set, Standart setin yaklaşık üçte biri tutuyor. Ama ücretsiz sesleri tek tek seçmek zaman alıyor ve kodlama ajanlarının kalitesi birbirinden farklı. Kendi projenizde kısa bir deneme yapmadan karar vermeyin. Abonelik fiyatlarının TL karşılaştırması için [yapay zeka abonelik fiyatları](/tr/blog/yapay-zeka-abonelik-fiyatlari) yazısına bakabilirsiniz.

## Türkiye'den ödeme yaparken nelere dikkat etmeli?

Bu araçların çoğu Türkiye'ye TL fiyat vermiyor, dolarla fatura kesiyor. Birkaç pratik not:

- **Claude** (Pro 20 dolar, Max 5× 100 dolar, Max 20× 200 dolar) dolarla faturalanıyor. Türkiye fatura adresiyle ödemede %20 KDV eklendiği bildiriliyor. Geçerli olan, ödeme ekranındaki son tutar.
- **Google AI Pro** Türkiye'de TL fiyatla satılıyor: ayda 869,99 TL. Dolar fiyatı (19,99 dolar) bugünkü kurla yaklaşık 985 TL ettiği için, En ucuz setin kod kalemi Türkiye'de biraz daha ucuza geliyor.
- **Midjourney, Suno, ElevenLabs** dolarla faturalanıyor. Bankanız doları kendi kuruyla TL'ye çevirir; kur farkı ve olası komisyon tutarı değiştirebilir.
- **Google Play geliştirici hesabı** bir kerelik 25 dolar (≈ 1.230 TL). Apple Developer Program yıllık 99 dolar (≈ 4.880 TL).

Hesaplayıcıda fiyatları TL ve KDV dahil görmek için Türkçe sayfadaki para birimi seçeneğini kullanabilirsiniz.

## Günde kaç saat çalıştığınız süreyi nasıl değiştirir?

Yukarıdaki süreler, kodlama deneyimi olmayan birinin günde yaklaşık 8 saat çalıştığını varsayıyor. Çoğu kişi oyununu işten sonra yapıyor; o zaman tablo değişiyor:

- **Günde 1–2 saat**: aynı küçük merge oyunu 56–90 gün sürüyor. Abonelik üç aya çıktığı için maliyet 201–547 dolar (≈ 9.910–26.960 TL) oluyor.
- **Geliştiriciyseniz**: süre yaklaşık %30 kısalıyor; küçük merge oyunu 10–16 gün.

Az saat çalışacaksanız, pahalı bir planı ay ay ödemek yerine daha ucuz bir kodlama planı seçmek mantıklı olabilir. Hesaplayıcıda "Günlük saat" ve "Kodlama deneyimi" seçeneklerini değiştirerek kendi durumunuzu görebilirsiniz.

## Kendi oyunumla test ettim: tahmin ve gerçek

Hesaplayıcının doğru olup olmadığını bilmiyordum, bu yüzden Google Play'de yayımladığım kendi oyunumun (basit bir yarış oyunu) özelliklerini girdim: küçük boyut, sade vektör çizim, 3 karakter, 3 müzik, 13 dil, reklam, uygulama içi satın alma ve kayıt; araçlar Claude Pro, Pixabay ve ücretsiz ses kütüphaneleri.

![Kendi yarış oyunumun özellikleriyle hesaplayıcının görsel, ses, kod ve token tahmini](/yapay-zeka-oyun-maliyeti-kendi-oyunum-tahmin-tr.jpg)

Görseldeki tutarlar TL ve %20 KDV dahil; aşağıdaki tabloda aynı sonucu dolar olarak, KDV hariç veriyorum.

| | Hesaplayıcı | Gerçek |
|---|---|---|
| Maliyet (mağaza ücreti hariç) | 26–72 $ | 20 $ (1 ay Claude Pro) |
| Mağaza ücreti | ayrı | 25 $ (Google Play) |
| Süre | 19–31 gün | yaklaşık 17 gün (3 gün yapım + 14 gün hata düzeltme) |
| Görseller | 10 $ (Midjourney) | 0 $ (karakterleri ve arka planları yapay zeka kodla çizdi) |
| Müzik ve efektler | 0 $ | 0 $ (Pixabay müziği, efektler kodla) |

Maliyeti neredeyse doğru tahmin etti. Toplamda 45 dolar ödedim: bir ay Claude Pro (20 dolar) ve Google Play ücreti (25 dolar). Fark görsellerdeydi, çünkü ben görsel üretmek yerine her şeyi yapay zekaya kodla çizdirdim.

Süre ise beklediğimden farklı dağıldı. Oyunun kendisi 3 günde bitti; kalan 14 gün neredeyse tamamen Google Play kapalı testinde hata düzeltmekle geçti. Yapay zekaya hatayı bulmasını söylediğimde çoğu zaman alakasız bir şeyi "düzeltti", bu yüzden hataların çoğunu kendim bulmak zorunda kaldım. Hesaplayıcı "bu planın kullanım sınırı yetmeyebilir" uyarısı da verdi; benim durumumda Claude Pro yayına çıkmaya yetti.

## İnsanların unuttuğu maliyetler neler?

- **Kapalı test**: Google Play'de yeni kişisel geliştirici hesapları, uygulamayı yayımlamadan önce en az 12 test kullanıcısıyla 14 gün kapalı test yapmak zorunda. Bu süreyi takvime ekleyin.
- **Mağaza ücretleri**: Google Play bir kerelik 25 dolar, Apple yıllık 99 dolar, Steam oyun başına 100 dolar. Web ücretsiz.
- **Sunucu**: çevrim içi oyunlar için Photon, Firebase veya küçük bir sunucu gerekir. Hesaplayıcı geliştirme süresince ayda 12 dolar hesaplıyor.
- **iOS sürümü**: derleme ve inceleme için yaklaşık 3 gün daha.
- **Diller**: eklediğiniz her dil için yaklaşık yarım gün.

Yayın sonrası bakım ve pazarlama dahil değil; çoğu zaman en büyük harcama da onlar oluyor.

## Roblox'ta oyun yapmak daha mı ucuz?

Roblox'ta mağaza ücreti yok ve sunucuları Roblox ücretsiz çalıştırıyor. Roblox Studio içindeki Roblox Assistant da ücretsiz bir kullanım hakkıyla geliyor. Bu yüzden En ucuz set Roblox'ta neredeyse sıfıra iniyor. Ama ücretsiz hak sınırlı; bütün bir oyun için büyük ihtimalle yetmiyor. Hesaplayıcıda platform olarak Roblox'u seçerseniz şu an yükselen Roblox oyun türlerini ve kazanç hesabını da görürsünüz.

## Sık sorulan sorular

**Kod bilmeden yapay zeka ile oyun yapılabilir mi?** Evet. Ben hiç kod bilmeden başladım. Ne istediğinizi kodlama ajanına anlatırsınız, o kodu yazar. Ama hataları test etmek ve ajanı doğru yöne çekmek size kalıyor; en çok zamanı da bu alıyor.

**Yapay zeka ile oyun yapmak için en ucuz yol nedir?** Görseller için Gemini gibi görsel başına ödemeli bir API, müzik ve efektler için Pixabay gibi ücretsiz kütüphaneler, kod için Google AI Pro gibi uygun bir plan. Küçük bir oyun böylece yaklaşık 32–45 dolar (≈ 1.580–2.220 TL) tutuyor; Google Play ücretini henüz ödemediyseniz 25 dolar daha ekleyin.

**Hesaplayıcı ücretsiz mi?** Evet, üyelik gerektirmiyor. Tür, boyut, motor ve platform seçince maliyet ve süre tahminiyle birlikte geliştirme, görsel, müzik ve ses efekti için hazır promptlar da veriyor. Yazdığınız hiçbir şey bir yere gönderilmiyor.

## Sonuç: küçük bir oyun için ne kadar ayırmalı?

Yapay zeka araçlarıyla tek başına küçük bir 2D mobil oyun yapmak tam zamanlı çalışırsanız yaklaşık 2–3 hafta sürüyor. Maliyet En ucuz setle yaklaşık 32–45 dolar (≈ 1.580–2.220 TL), Standart setle 107–151 dolar (≈ 5.270–7.440 TL); üstüne bir kerelik 25 dolarlık Google Play ücreti geliyor. Paranın büyük kısmı kodlama aboneliğine gidiyor, bu yüzden en büyük tasarruf, oyunu daha az ayda bitirmekten geliyor. Hata düzeltmeye de yapım kadar, hatta daha fazla zaman ayırın.

Kendi oyununuzun rakamlarını görmek için [yapay zeka ile oyun maliyeti hesaplayıcısını](/tr/ai-game-cost-calculator) açın; kodlama ajanının aylık maliyetini ayrıca [kodlama ajanı hesaplayıcısında](/tr/agents) karşılaştırabilirsiniz.

## Kaynaklar

- [Claude fiyatları (Pro ve Max planları)](https://claude.com/pricing)
- [Midjourney planlarının karşılaştırması](https://docs.midjourney.com/hc/en-us/articles/27870484040333-Comparing-Midjourney-Plans)
- [Suno fiyatları](https://suno.com/pricing)
- [ElevenLabs fiyatları](https://elevenlabs.io/pricing)
- [Google AI planları (Türkiye)](https://gemini.google/tr/subscriptions/)
- [Play Console Yardım: Play Console'u kullanmaya başlama (bir kerelik 25 dolarlık kayıt ücreti)](https://support.google.com/googleplay/android-developer/answer/6112435?hl=tr)
- [Play Console Yardım: yeni kişisel geliştirici hesapları için test şartları](https://support.google.com/googleplay/android-developer/answer/14151465?hl=tr)
- [Apple Developer Program (yıllık üyelik)](https://developer.apple.com/programs/)
- [Steamworks: Steam Direct ücreti](https://partner.steamgames.com/doc/gettingstarted/appfee)
- [Roblox Developer Exchange (DevEx)](https://create.roblox.com/docs/production/monetization/developer-exchange)
<!-- autoimg -->
