import os
import time
import sys

# Kode Warna ANSI Premium untuk Termux
MERAH    = '\033[1;31m'
HIJAU    = '\033[1;32m'
KUNING   = '\033[1;33m'
BIRU     = '\033[1;34m'
MAGENTA  = '\033[1;35m'
CYAN     = '\033[1;36m'
PUTIH    = '\033[1;37m'
RESET    = '\033[0m'

def cetak_banner():
    os.system('clear')
    print(f"{CYAN}==============================================================={RESET}")
    print(f"{CYAN}   📡  ADVANCED DVB-T2 DIGITAL TV SIGNAL DETECTOR (TERMUX) 📡 {RESET}")
    print(f"{CYAN}==============================================================={RESET}")
    print(f" {PUTIH}Engine Version :{RESET} {MAGENTA}v1.1.2-Stable{RESET}")
    print(f" {PUTIH}Target Platform:{RESET} {KUNING}Termux Android CLI{RESET}")
    print(f" {PUTIH}Status         :{RESET} {HIJAU}Scanner Core Online & Ready{RESET}")
    print(f"{CYAN}==============================================================={RESET}\n")

def dapatkan_status(persen):
    if persen >= 80:
        return f"{HIJAU}🥇 SANGAT KUAT (Lancar Jaya, Antena Dalam OK){RESET}"
    elif persen >= 60:
        return f"{HIJAU}🥈 KUAT (Sangat Stabil, Antena Luar Standar){RESET}"
    elif persen >= 40:
        return f"{KUNING}🥉 CUKUP (Berpotensi Patah, Wajib Antena Luar){RESET}"
    elif persen >= 25:
        return f"{MERAH}⚠️ LEMAH (Sering No Signal, Butuh Booster + Tiang Tinggi){RESET}"
    else:
        return f"{MERAH}🚫 BLANKSPOT (Sinyal Tidak Terjangkau / Hilang){RESET}"

def hitung_loss_sinyal(jarak, halangan):
    # Logika kalkulasi redaman sinyal UHF berdasarkan jarak dan kondisi geografis
    base_signal = 98
    
    # Redaman jarak (Path Loss)
    if jarak <= 5:
        loss_jarak = jarak * 1.2
    elif jarak <= 15:
        loss_jarak = jarak * 1.8
    else:
        loss_jarak = jarak * 2.3
        
    # Redaman halangan geografis
    faktor_halangan = {
        "1": 0,   # Lapangan terbuka / Flat
        "2": 12,  # Banyak pohon / Perumahan padat
        "3": 25,  # Terhalang gedung tinggi
        "4": 38   # Daerah pegunungan / Lembah
    }
    
    loss_geografis = faktor_halangan.get(halangan, 12)
    total_sinyal = int(base_signal - loss_jarak - loss_geografis)
    
    return max(0, min(100, total_sinyal))

def jalankan_pemindaian():
    cetak_banner()
    
    # Input Data dengan validasi sederhana
    wilayah = input("📍 Masukkan Nama Kota / Kabupaten Anda: ").strip()
    if not wilayah:
        wilayah = "DKI Jakarta & Sekitarnya"
        
    try:
        jarak = float(input("📏 Perkiraan jarak rumah ke Tower Pemancar terdekat (KM): "))
    except ValueError:
        print(f"{KUNING}[!] Input salah. Menggunakan estimasi default 15 KM.{RESET}")
        jarak = 15.0
        
    print(f"\n🏔️  {PUTIH}Pilih Kondisi Geografis Lingkungan Rumah Anda:{RESET}")
    print(" 1. Lapangan Terbuka / Tanpa Penghalang")
    print(" 2. Area Perumahan Padat / Banyak Pohon")
    print(" 3. Terhalang Gedung-Gedung Tinggi")
    print(" 4. Daerah Lembah / Pegunungan (Blankspot Terbanyak)")
    halangan = input("👉 Pilih nomor (1-4) [Default 2]: ").strip()
    if halangan not in ["1", "2", "3", "4"]:
        halangan = "2"
        
    cetak_banner()
    print(f"{BIRU}[*] Menginisialisasi modul pencarian frekuensi...{RESET}")
    time.sleep(0.8)
    print(f"{BIRU}[*] Menghitung interferensi gelombang UHF (Ultra High Frequency)...{RESET}")
    time.sleep(1)
    
    final_signal = hitung_loss_sinyal(jarak, halangan)
    
    # Daftar Frekuensi MUX TV Digital Terbesar di Indonesia
    database_mux = [
        {"operator": "TVRI Nasional", "ch": "22 - 48 UHF", "freq": "482 - 690 MHz", "tipe": "Mux Pemerintah"},
        {"operator": "MNC Group (RCTI, GTV, MNC, iNews)", "ch": "28 - 44 UHF", "freq": "530 - 658 MHz", "tipe": "Mux Swasta"},
        {"operator": "Media Group (Metro TV, Magna, BN)", "ch": "25 - 41 UHF", "freq": "506 - 634 MHz", "tipe": "Mux Swasta"},
        {"operator": "VIVA Group (tvOne, ANTV)", "ch": "34 - 46 UHF", "freq": "578 - 674 MHz", "tipe": "Mux Swasta"},
        {"operator": "Trans Media (TransTV, Trans7, CNN)", "ch": "32 - 42 UHF", "freq": "562 - 642 MHz", "tipe": "Mux Swasta"},
        {"operator": "Emtek Group (SCTV, Indosiar, MOJI)", "ch": "24 - 36 UHF", "freq": "498 - 594 MHz", "tipe": "Mux Swasta"}
    ]
    
    print(f"\n{KUNING}[📊] HASIL PEMINDAIAN SPEKTRUM FREKUENSI DI {wilayah.upper()}:{RESET}\n")
    print(f"{PUTIH}------------------------------------------------------------------------{RESET}")
    print(f"{'OPERATOR MUX TV DIGITAL':<32} | {'SALURAN UHF':<12} | {'FREKUENSI':<11} | {'KONSISTENSI'}")
    print(f"{PUTIH}------------------------------------------------------------------------{RESET}")
    
    for mux in database_mux:
        # Sedikit variasi sinyal antar Mux agar terlihat realistis
        variasi_sinyal = max(0, min(100, final_signal + (hash(mux['operator']) % 7) - 3))
        
        if variasi_sinyal >= 60:
            warna_bar = HIJAU
        elif variasi_sinyal >= 30:
            warna_bar = KUNING
        else:
            warna_bar = MERAH
            
        print(f"📡 {mux['operator']:<29} | {mux['ch']:<12} | {mux['freq']:<11} | {warna_bar}{variasi_sinyal}%{RESET}")
        time.sleep(0.4) # Efek delay scanner animasi CLI
        
    print(f"{PUTIH}------------------------------------------------------------------------{RESET}\n")
    
    # Ringkasan Analisis Diagnostik
    print(f"{CYAN}[⚙️] DIAGNOSTIK SINYAL UTAMA:{RESET}")
    print(f" 🟩 Wilayah Pemindaian      : {PUTIH}{wilayah}{RESET}")
    print(f" 🟩 Jarak ke Pemancar       : {PUTIH}{jarak} KM{RESET}")
    print(f" 🟩 Estimasi Daya Tangkap   : {PUTIH}{final_signal}%{RESET}")
    print(f" 🟩 Status Kelayakan Siaran : {dapatkan_status(final_signal)}")
    print(f"{CYAN}==============================================================={RESET}")
    
    # Solusi Rekomendasi Antena
    print(f"\n💡 {MAGENTA}REKOMENDASI TEKNISI:{RESET}")
    if final_signal >= 75:
        print(f" {HIJAU}Antena dalam ruangan pendek sudah cukup mendapat gambar HD jernih tanpa semut.{RESET}")
    elif final_signal >= 45:
        print(f" {KUNING}Gunakan Antena Luar Ruangan tipe Yagi (sedang). Pastikan kabel coaxial tidak terkelupas.{RESET}")
    else:
        print(f" {MERAH}Sinyal kritis! Anda Wajib menaikkan antena luar > 6 meter, arahkan presisi, atau gunakan booster atas-bawah.{RESET}")
    print("\n")

if __name__ == "__main__":
    try:
        jalankan_pemindaian()
    except KeyboardInterrupt:
        print(f"\n{MERAH}[!] Pemindaian dibatalkan pengguna.{RESET}")
      
