![Bahasa Indonesia pakai 15% token lebih banyak dari bahasa Inggris di GPT](/token-bahasa-indonesia-gpt-id.jpg)

Saya menerjemahkan prompt layanan pelanggan yang sama ke 41 bahasa dan menghitung token dengan o200k_base, tokenizer OpenAI saat ini (GPT-4o dan setelahnya). Bahasa Inggris butuh 34 token, bahasa Indonesia **39 token — 15% lebih banyak dari bahasa Inggris**, peringkat 3 dari 41 (1 = paling murah).

Versi bahasa Indonesia:

> Ringkas email pelanggan di bawah ini dalam tiga poin dan sarankan balasan yang sopan. Pelanggan mengatakan pesanan tiba dua hari terlambat dan satu barang hilang dari kotak.

## Hasil

| Bahasa | Token | Dibanding bahasa Inggris | Hemat jika dikirim dalam bahasa Inggris |
|---|---:|---:|---:|
| English | 34 | ±0% | – |
| 简体中文 | 35 | +3% | 3% |
| **Bahasa Indonesia** | **39** | **+15%** | **13%** |
| Español | 40 | +18% | 15% |
| Deutsch | 43 | +26% | 21% |
| 한국어 | 49 | +44% | 31% |
| हिन्दी | 51 | +50% | 33% |
| 日本語 | 61 | +79% | 44% |
| Čeština | 68 | +100% | 50% |
| Ελληνικά | 70 | +106% | 51% |
| ਪੰਜਾਬੀ | 83 | +144% | 59% |

![Grafik: token tambahan tiap bahasa dibanding bahasa Inggris di GPT](/blog-language-tax-chart-v5.png)

## Mengapa

![Mengapa: terlambat → terl | amb | at · 3; Pelanggan → Pel | anggan · 2; sarankan → sar | ankan · 2](/token-bahasa-indonesia-gpt-mengapa-id.jpg)

Tokenizer terutama belajar dari teks bahasa Inggris: kata seperti " polite" atau " customer" hanya satu token, sedangkan kata berimbuhan dalam bahasa Indonesia dipecah:

- terlambat → `terl | amb | at` · 3
- Pelanggan → `Pel | anggan` · 2
- sarankan → `sar | ankan` · 2

## Beralih ke bahasa Inggris dengan satu tombol

Penghematan terbesar adalah mengirim prompt dalam bahasa Inggris: sekitar 13% lebih sedikit token dibanding bahasa Indonesia. Model saat ini sangat memahami instruksi berbahasa Inggris dan akan menjawab dalam bahasa Indonesia jika Anda memintanya. Di penghitung token TokenSave, tempel prompt Anda lalu tekan **💸 Hemat token**: tombol ini merapikan spasi, menerjemahkan ke bahasa Inggris, membuang kata yang tidak perlu, dan menambahkan "Reply in Indonesian." agar jawabannya tetap dalam bahasa Anda. Fitur ini memakai penerjemah bawaan Chrome 138+ / Edge 148+ versi desktop; terjemahan berjalan di perangkat Anda sendiri dan teks Anda tidak pernah diunggah. Tekan **↩ Asli** untuk mengembalikan teks asli.

## Dalam uang

Dengan model seharga $2 per 1 juta token input, mengirim prompt ini 1 juta kali menghabiskan $68 dalam bahasa Inggris dan $78 dalam bahasa Indonesia. Jika jawabannya juga berbahasa Indonesia, pengali yang sama berlaku untuk token output yang biasanya 300–400% lebih mahal.

## Cara berhemat

![Cara berhemat: Tulis system prompt dan instruksi tetap dalam bahasa Inggris; biarkan hanya input pengguna dalam bahasa Indone](/token-bahasa-indonesia-gpt-cara-berhemat-id.jpg)

- Tulis system prompt dan instruksi tetap dalam bahasa Inggris; biarkan hanya input pengguna dalam bahasa Indonesia.
- Minta langkah perantara (klasifikasi, ekstraksi, pemanggilan tool) dalam bahasa Inggris atau JSON, dan hanya jawaban akhir dalam bahasa Indonesia.
- Gunakan prompt caching untuk bagian prompt yang tetap.

## Batasan

- Hanya satu prompt yang diukur; pada teks lain rasionya bisa berbeda ±0,1–0,2.
- Claude dan Gemini memakai tokenizer lain; angka ini hanya berlaku untuk model OpenAI.
- Terjemahan didasarkan pada terjemahan mesin yang sudah diperiksa.

Coba dengan teks Anda sendiri di [penghitung token](/id/); perbandingan semua bahasa ada di [tabel bahasa](/languages).

Hasil lengkap 41 bahasa (dalam bahasa Inggris): [perbandingan 41 bahasa](/blog/token-cost-by-language)

## Sumber

- [tiktoken: tokenizer OpenAI (o200k_base) di GitHub](https://github.com/openai/tiktoken)
- [Harga OpenAI API](https://developers.openai.com/api/docs/pricing)

<!-- autoimg -->
