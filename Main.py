import os
import time

# Kode Warna Termux
MERAH = '\033[1;31m'
HIJAU = '\033[1;32m'
KUNING = '\033[1;33m'
BIRU = '\033[1;34m'
CYAN = '\033[1;36m'
RESET = '\033[0m'

def print_banner():
    print(f"{CYAN}==============================================={RESET}")
    print(f"{CYAN}   📡  DVB-T2 TV DIGITAL SIGNAL DETECTOR       {RESET}")
    print(f"{CYAN}==============================================={RESET}")
    print(f" Ekosistem: Termux CLI Tool")
    print(f" Status   : {HIJAU}Scanner Engine Ready{RESET}\n")

def cek_status_sinyal(persentase):
    if persentase >= 75:
        return f"{HIJAU}SANGAT KUAT (Sangat Layak Antena Dalam/Luar){RESET}"
    elif persentase >= 50:
        return f"{KUNING}CUKUP (Disarankan Antena Luar Pendek){RESET}"
    elif persentase >= 32:
        return f"{KUNING}LEMAH (Wajib Antena Luar Tinggi + Booster){RESET}"
    else:
        return f"{MERAH}NO SIGNAL / BLANK (ZONA BLANKSPOT){RESET}"

def scan_sinyal_wilayah(wilayah, jarak):
    print_banner()
    print(f"{BIRU}[*] Menghubungkan ke database pemancar TV Digital...{RESET}")
    time.sleep(1)
    
    print(f"{KUNING}[*] Memindai sinyal di wilayah: {wilayah.upper()}{RESET}")
    print(f"{KUNING}[*] Estimasi jarak ke Tower Pemancar: {jarak} KM{RESET}\n")
    
    # Simulasi perhitungan pelemahan sinyal berdasarkan jarak (Logarithmic Friis Path Loss approx)
    # Semakin jauh dari tower, persentase sinyal makin drop
    base_signal = 95
    loss = jarak * 1.8
    signal_strength = max(0, min(100, int(base_signal - loss)))

    # Database Mux TV Digital Umum di Indonesia
    mux_list = [
        {"name": "TVRI Nasional (TVRI, Klik TV, dll)", "ch": "22-48 UHF", "freq": "482-690 MHz"},
        {"name": "MNC Group (RCTI, GTV, MNC, iNews)", "ch": "28-44 UHF", "freq": "530-658 MHz"},
        {"name": "Media Group (Metro TV, Magna, BN TV)", "ch": "25-41 UHF", "freq": "506-634 MHz"},
        {"name": "VIVA Group (tvOne, ANTV)", "ch": "34-46 UHF", "freq": "578-674 MHz"},
        {"name": "Trans Media (Trans TV, Trans7, CNBC, CNN)", "ch": "32-42 UHF", "freq": "562-642 MHz"},
        {"name": "Emtek Group (SCTV, Indosiar, MOJI, Mentari)", "ch": "24-36 UHF", "freq": "498-594 MHz"}
    ]

    print(f"{CYAN}------------------------------------------------------------{RESET}")
    print(f"{'GROUP MUX TV DIGITAL':<35} | {'CH/FREQ':<13} | {'SIGNAL'}")
    print(f"{CYAN}------------------------------------------------------------{RESET}")
    
    for mux in mux_list:
        print(f"📡 {mux['name']:<32} | {mux['ch']} | {signal_strength}%")
        time.sleep(0.3) # Efek scanning progress
        
    print(f"{CYAN}------------------------------------------------------------{RESET}\n")
    
    print(f"📊 {CYAN}KESIMPULAN ANALISIS SINYAL:{RESET}")
    print(f"➡️ Kekuatan Sinyal Rata-rata : {signal_strength}%")
    print(f"➡️ Status Kelayakan Menerima : {cek_status_sinyal(signal_strength)}")
    
    if signal_strength < 50 and signal_strength >= 32:
        print(f"\n💡 {KUNING}Tips:{RESET} Arahkan antena luar Anda secara presisi tanpa terhalang gedung/pohon tinggi.")
    elif signal_strength < 32:
        print(f"\n💡 {MERAH}Peringatan:{RESET} Daerah Anda terlalu jauh dari pemancar. Pertimbangkan menggunakan Parabola/Streaming.")

if __name__ == "__main__":
    lokasi = input("📍 Masukkan Nama Kota/Kabupaten Anda: ").strip()
    while not lokasi:
        lokasi = input("📍 Nama wilayah tidak boleh kosong! Masukkan Kota/Kabupaten: ").strip()
        
    try:
        jarak_input = input("📏 Perkiraan jarak ke tower pemancar terdekat (KM) [Default: 15]: ").strip()
        if not jarak_input:
            jarak = 15
        else:
            jarak = float(jarak_input)
    except ValueError:
        print(f"{MERAH}Input jarak harus berupa angka! Menggunakan default 15 KM.{RESET}")
        jarak = 15
        
    os.system('clear')
    scan_sinyal_wilayah(lokasi, jarak)
  
