# 📡 Signal Hunter v1.0.0 (.sh Version) 📱

[![Shell](https://img.shields.io/badge/shell-bash-green.svg)](https://www.gnu.org/software/bash/)
[![Platform](https://img.shields.io/badge/platform-Termux-orange.svg)](https://termux.dev/)

**Signal Hunter** adalah sebuah script utilitas berbasis **Bash Shell (`.sh`)** yang dirancang untuk mensimulasikan pemindaian, pelacakan, dan visualisasi grafik kekuatan sinyal jaringan seluler serta Wi-Fi di lingkungan sekitar secara real-time lewat terminal **Termux Android**.

Karena ditulis murni menggunakan sintaks Bash, tool ini mengeksekusi logika pencarian frekuensi radio secara instan tanpa membutuhkan ketergantungan (dependencies) eksternal seperti Python, Node.js, atau compiler lainnya.

---

## ✨ Fitur Unggulan Tool
* 🚀 **Zero Dependencies**: Berjalan murni menggunakan interpreter Bash bawaan Android/Termux.
* 📊 **Dynamic Bar Graph Visualizer**: Menampilkan kekuatan daya tangkap sinyal (dBm equivalent) dalam bentuk grafik balok (`████░░░░`) berwarna otomatis.
* 🌈 **Smart ANSI Color Code**: Warna bar grafis berubah secara dinamis (Hijau = Sinyal Sempurna, Kuning = Sinyal Cukup, Merah = Sinyal Kritis/Lost).
* 🔋 **Ultra Lightweight**: Ukuran file script sangat kecil (< 3KB) sehingga hemat penggunaan RAM dan memori penyimpanan internal HP Anda.

---

## 🛠️ Langkah-Langkah Instalasi di Termux

Silakan ikuti instruksi command di bawah ini secara berurutan pada aplikasi Termux Anda:

### 1️⃣ Update Environment System
Langkah awal untuk memastikan repositori Termux Anda berada di server yang tepat dan up-to-date:
```bash
pkg update && pkg upgrade -y
