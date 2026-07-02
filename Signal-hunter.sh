#!/bin/bash

# Warna ANSI Premium untuk Termux
MERAH='\033[1;31m'
HIJAU='\033[1;32m'
KUNING='\033[1;33m'
BIRU='\033[1;34m'
CYAN='\033[1;36m'
PUTIH='\033[1;37m'
RESET='\033[0m'

cetak_banner() {
    clear
    echo -e "${CYAN}===============================================================${RESET}"
    echo -e "${CYAN}    📡  SIGNAL HUNTER: CELLULAR & WI-FI DETECTOR (.SH)  📡   ${RESET}"
    echo -e "${CYAN}===============================================================${RESET}"
    echo -e " ${PUTIH}Engine Linux   :${RESET} ${BIRU}Bash Script Core${RESET}"
    echo -e " ${PUTIH}Platform Target:${RESET} ${KUNING}Termux Android CLI${RESET}"
    echo -e " ${PUTIH}Status         :${RESET} ${HIJAU}Network Radar Online${RESET}"
    echo -e "${CYAN}===============================================================${RESET}\n"
}

bikin_bar_sinyal() {
    local persen=$1
    local jumlah_balok=$((persen / 5))
    local bar=""
    
    # Tentukan warna bar berdasarkan kekuatan
    if [ $persen -ge 75 ]; then
        local warna=$HIJAU
    elif [ $persen -ge 45 ]; then
        local warna=$KUNING
    else
        local warna=$MERAH
    fi

    # Susun balok sinyal
    for ((i=0; i<20; i++)); do
        if [ $i -lt $jumlah_balok ]; then
            bar="${bar}█"
        else
            bar="${bar}░"
        fi
    done
    echo -e "${warna}[${bar}] ${persen}%${RESET}"
}

jalankan_radar() {
    cetak_banner
    echo -e "${KUNING}[*] Menginisialisasi modul driver radio...${RESET}"
    sleep 0.8
    echo -e "${KUNING}[*] Membuka port antena virtual Termux...${RESET}"
    sleep 1
    
    echo -e "\n${PUTIH}🔎 Memulai Pemindaian Frekuensi Sekitar...${RESET}\n"
    sleep 0.5

    # Simulasi Data Provider Seluler & Wi-Fi (Bisa kamu modifikasi namanya)
    declare -a jaringan=("Telkomsel_4G" "XL_Axiata_5G" "Indosat_Ooredoo" "Smartfren_LTE" "Wi-Fi_Rumah_Tetangga" "Warkop_Free_WiFi")
    
    echo -e "${PUTIH}------------------------------------------------------------------------${RESET}"
    echo -e "${CYAN}SSID / PROVIDER NETWORK         | TYPE    | KEKUATAN SINYAL (BAR GRAPH)${RESET}"
    echo -e "${PUTIH}------------------------------------------------------------------------${RESET}"

    for net in "${jaringan[@]}"; do
        # Membuat angka acak antara 15 sampai 98 untuk simulasi sinyal
        local nilai_sinyal=$(( RANDOM % 84 + 15 ))
        
        # Deteksi tipe berdasarkan nama
        if [[ "$net" == *"Wi-Fi"* || "$net" == *"WiFi"* ]]; then
            local tipe="WLAN"
        else
            local tipe="CELL"
        fi

        printf "📶 %-28s | %-7s | " "$net" "$tipe"
        bikin_bar_sinyal $nilai_sinyal
        sleep 0.4 # Efek animasi radar scanning
    done
    
    echo -e "${PUTIH}------------------------------------------------------------------------${RESET}"
    echo -e "\n${HIJAU}[✅] Pemindaian Selesai! Gunakan 'Ctrl + C' untuk keluar atau jalankan ulang.${RESET}\n"
}

# Jalankan fungsi utama
jalankan_radar
