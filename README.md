# 📈 AI YouTube Title & SEO Optimizer

Aplikasi berbasis web menggunakan **Streamlit** dan **Google Gemini AI** untuk menganalisis dan mengoreksi judul YouTube yang memiliki performa CTR (Click-Through Rate) rendah. 

Alat ini dirancang khusus sebagai pendamping alur kerja paska-produksi (*post-production*). Setelah *video editing* selesai—termasuk pemasangan *opening sequence* 30-60 detik dan bumper logo—alat ini memastikan pengemasan teks (Judul dan SEO) dikalibrasi secara presisi dengan DNA masing-masing *channel*.

## ✨ Fitur Utama
- **Multi-Channel DNA:** Dilengkapi dengan System Prompt khusus untuk 3 *channel* berbeda (Suara Filsuf, Tutur Kyai, Nalar Senyap).
- **Auto-Correction & Character Limit:** Menganalisis judul lama dan meracik ulang menjadi judul baru dengan perhitungan batas karakter keras (maksimal 70 karakter).
- **Tabbed UI/UX:** Memisahkan *output* AI ke dalam tiga *tab* (Hook & Judul, Thumbnail, SEO & Metadata) agar mudah dibaca dan langsung di-copy-paste ke YouTube Studio.
- **Transkrip Anti-Halusinasi:** Mendukung input transkrip penuh agar AI tidak mengarang konteks di luar video aktual.
- **Secure by Design:** API Key tidak di-*hardcode* di dalam skrip, melainkan dimasukkan melalui *sidebar* UI saat aplikasi berjalan.

## 🚀 Cara Instalasi dan Menjalankan

1. Clone repositori ini:
   ```bash
   git clone [https://github.com/hasansahru/youtube-optimizer.git](https://github.com/hasansahru/youtube-optimizer.git)
   cd youtube-optimizer
