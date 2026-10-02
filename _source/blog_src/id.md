Saya menerjemahkan prompt layanan pelanggan yang sama ke 41 bahasa dan menghitung token dengan o200k_base, tokenizer OpenAI saat ini (GPT-4o dan setelahnya). Bahasa Inggris butuh 34 token, bahasa Indonesia **39 token — 1,15× bahasa Inggris**, peringkat 3 dari 41 (1 = paling murah).

Versi bahasa Indonesia:

> Ringkas email pelanggan di bawah ini dalam tiga poin dan sarankan balasan yang sopan. Pelanggan mengatakan pesanan tiba dua hari terlambat dan satu barang hilang dari kotak.

## Hasil

| Bahasa | Token | Dibanding bahasa Inggris | Hemat jika dikirim dalam bahasa Inggris |
|---|---:|---:|---:|
| English | 34 | 1,00× | – |
| 简体中文 | 35 | 1,03× | 3% |
| **Bahasa Indonesia** | **39** | **1,15×** | **13%** |
| Español | 40 | 1,18× | 15% |
| Deutsch | 43 | 1,26× | 21% |
| 한국어 | 49 | 1,44× | 31% |
| हिन्दी | 51 | 1,50× | 33% |
| 日本語 | 61 | 1,79× | 44% |
| Čeština | 68 | 2,00× | 50% |
| Ελληνικά | 70 | 2,06× | 51% |
| ਪੰਜਾਬੀ | 83 | 2,44× | 59% |

![Hasil](/blog-language-tax-chart-v4.png)

## Mengapa

Tokenizer terutama belajar dari teks bahasa Inggris: kata seperti " polite" atau " customer" hanya satu token, sedangkan kata berimbuhan dalam bahasa Indonesia dipecah:

- terlambat → `terl | amb | at` · 3
- Pelanggan → `Pel | anggan` · 2
- sarankan → `sar | ankan` · 2

## Beralih ke bahasa Inggris dengan satu tombol

Penghematan terbesar adalah mengirim prompt dalam bahasa Inggris: sekitar 13% lebih sedikit token dibanding bahasa Indonesia. Model saat ini sangat memahami instruksi berbahasa Inggris dan akan menjawab dalam bahasa Indonesia jika Anda memintanya. Di penghitung token TokenSave, tempel prompt Anda lalu tekan **💸 Hemat token**: tombol ini merapikan spasi, menerjemahkan ke bahasa Inggris, membuang kata yang tidak perlu, dan menambahkan "Reply in Indonesian." agar jawabannya tetap dalam bahasa Anda. Fitur ini memakai penerjemah bawaan Chrome 138+ / Edge 148+ versi desktop; terjemahan berjalan di perangkat Anda sendiri dan teks Anda tidak pernah diunggah. Tekan **↩ Asli** untuk mengembalikan teks asli.

## Dalam uang

Dengan model seharga $2 per 1 juta token input, mengirim prompt ini 1 juta kali menghabiskan $68 dalam bahasa Inggris dan $78 dalam bahasa Indonesia. Jika jawabannya juga berbahasa Indonesia, pengali yang sama berlaku untuk token output yang biasanya 4–5× lebih mahal.

## Cara berhemat

- Tulis system prompt dan instruksi tetap dalam bahasa Inggris; biarkan hanya input pengguna dalam bahasa Indonesia.
- Minta langkah perantara (klasifikasi, ekstraksi, pemanggilan tool) dalam bahasa Inggris atau JSON, dan hanya jawaban akhir dalam bahasa Indonesia.
- Gunakan prompt caching untuk bagian prompt yang tetap.

## Batasan

- Hanya satu prompt yang diukur; pada teks lain rasionya bisa berbeda ±0,1–0,2.
- Claude dan Gemini memakai tokenizer lain; angka ini hanya berlaku untuk model OpenAI.
- Terjemahan didasarkan pada terjemahan mesin yang sudah diperiksa.

Hasil lengkap 41 bahasa (dalam bahasa Inggris): [perbandingan 41 bahasa](/blog/token-cost-by-language)
