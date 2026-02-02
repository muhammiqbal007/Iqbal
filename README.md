# 📊 Proyek Capstone Modul 2
## Analisis Kinerja Penjualan SaaS, Segmentasi Pelanggan (LRFM), dan Proyeksi Laba

---

## 📌 Gambaran Umum Proyek
Proyek ini bertujuan untuk menganalisis kinerja penjualan dan profitabilitas perusahaan SaaS
menggunakan data transaksi historis. Analisis ini berfokus pada identifikasi wawasan bisnis,
segmentasi pelanggan menggunakan metode LRFM, dan proyeksi strategi peningkatan laba
untuk wilayah yang berkinerja buruk.

Proyek ini dikembangkan sebagai bagian dari **Proyek Capstone 2** dan menerapkan
**pendekatan berbasis data** untuk mendukung pengambilan keputusan bisnis strategis.

## 🎯 Tujuan Bisnis
Tujuan utama proyek ini adalah:
- Menganalisis distribusi penjualan dan laba di berbagai wilayah dan industri
- Mengidentifikasi industri dan wilayah dengan penjualan tinggi tetapi profitabilitas rendah
- Melakukan segmentasi pelanggan berdasarkan nilai perilaku menggunakan analisis LRFM
- Memproyeksikan potensi peningkatan laba di wilayah berkinerja rendah
- Memberikan rekomendasi bisnis yang dapat ditindaklanjuti berdasarkan wawasan data

---

## 🗂 Dataset
- **Nama Dataset:** Dataset Penjualan SaaS
- **Periode Waktu:** 1 Tahun
- **Granularitas:** Data tingkat transaksi

### Fitur Utama:
- `Tanggal Pesanan`
- `Wilayah`
- `Industri`
- `Pelanggan`
- `Penjualan`
- `Laba`
- `Diskon`

Fitur tambahan dibuat selama persiapan data, seperti:
- `margin_laba`
- `bulan_pesanan`
- `tahun_pesanan`

---

## 🛠 Alat & Teknologi
- **Python** (Analisis & Pemodelan Data)

- pandas
- matplotlib
- seaborn
- **Jupyter Notebook**
- **Tableau** (Visualisasi Data)
- **Microsoft PowerPoint** (Presentasi)

---

## 🔍 Alur Kerja Analisis
1. Pemuatan data dan pemahaman data
2. Pembersihan dan pra-pemrosesan data
3. Rekayasa fitur
4. Analisis Data Eksplorasi (EDA)
5. Analisis Indikator Kinerja Utama (KPI)
6. Segmentasi pelanggan menggunakan LRFM
7. Proyeksi keuntungan untuk wilayah yang berkinerja buruk
8. Rekomendasi bisnis dan waktu implementasi

---

## 👥 Segmentasi Pelanggan (LRFM)
Pelanggan disegmentasikan menggunakan kerangka kerja LRFM:
- **Panjang**: Masa hidup pelanggan
- **Kekinian**: Waktu sejak pembelian terakhir
- **Frekuensi**: Jumlah transaksi
- **Moneter**: Total nilai penjualan

Segmen pelanggan meliputi:

- Pelanggan Unggulan
- Pelanggan Setia
- Pelanggan Potensial
- Pelanggan Berisiko

Segmentasi ini membantu memprioritaskan strategi retensi dan pertumbuhan.

## 📈 Proyeksi Keuntungan
Proyeksi keuntungan dilakukan dengan mensimulasikan peningkatan margin
di wilayah dengan kinerja keuntungan saat ini terendah.

Selain itu, tiga industri teratas dengan potensi margin keuntungan tertinggi diidentifikasi untuk mendukung strategi pertumbuhan yang ditargetkan.

---

## ⏰ Waktu Implementasi yang Direkomendasikan
Berdasarkan tren penjualan bulanan historis, strategi bisnis direkomendasikan
untuk diimplementasikan selama **Februari–Maret (musim pra-puncak)** untuk memaksimalkan
dampaknya selama periode penjualan yang lebih tinggi di Q2–Q3.

---

## 📊 Visualisasi
- Python digunakan sebagai alat utama untuk analisis dan pemodelan data
- Tableau digunakan untuk memvisualisasikan wawasan utama bagi pemangku kepentingan non-teknis
- Dasbor Tableau dibangun menggunakan data yang telah dibersihkan dan dipersiapkan yang diekspor dari Python

---

## 📁 Struktur Proyek
