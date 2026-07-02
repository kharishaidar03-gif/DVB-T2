# 📡 DVB-T2 TV Digital Signal Detector for Termux 📺

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/platform-Termux%20%7C%20Linux-orange.svg)](https://termux.dev/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

**DVBT2-Signal-Detector** adalah sebuah alat bantu berbasis *Command Line Interface* (CLI) yang berjalan di dalam aplikasi **Termux Android**. Tool ini dirancang khusus untuk memetakan, memprediksi, dan mendeteksi kekuatan sinyal siaran TV Digital (**DVB-T2**) di berbagai daerah di Indonesia setelah era penutupan total TV Analog (*Analog Switch-Off*).

Sistem menganalisis sinyal secara dinamis dengan menghitung faktor **Path Loss (Redaman Jarak)** serta **Faktor Penghalang Geografis** (gedung perkotaan, pepohonan, lembah, atau pegunungan) untuk menyimpulkan apakah rumah Anda berada di zona *Safe-Spot* atau *Blank-Spot*.

---

## 🚀 Fitur Utama Tool
* 📊 **Multi-MUX Database**: Sinkronisasi simulasi pemindaian untuk 6 operator multipleksing terbesar di Indonesia (TVRI, MNC, Media Group, VIVA, Trans Media, dan Emtek).
* 🧮 **Friis Path Loss Approximation**: Algoritma perhitungan redaman sinyal UHF asli berdasarkan jarak real menara transmisi ke lokasi pengguna.
* ⛰️ **Terrain Obstacle Correction**: Menghitung gangguan topografi lingkungan sekitar (gedung/pepohonan/pegunungan) demi akurasi status kelayakan siaran.
* 🎨 **Termux ANSI Color Graphic**: Tampilan antarmuka yang memanjakan mata, memudahkan identifikasi status sinyal lewat indikator warna (Hijau, Kuning, Merah).
* 💡 **Smart Technician Recommendation**: Memberikan solusi realistik mengenai jenis antena yang harus Anda beli berdasarkan kekuatan sinyal di lapangan.

---

## 🛠️ Panduan Instalasi Super Lengkap (Langkah demi Langkah)

Pastikan aplikasi Termux Anda diunduh dari **F-Droid** atau **GitHub Termux resmi**, bukan dari Play Store (karena versi Play Store sudah usang/deprecated).

### Langkah 1: Perbarui Sistem Environment Termux
Langkah awal ini wajib agar repositori Termux mendownload paket paling stabil:
```bash
pkg update && pkg upgrade -y
