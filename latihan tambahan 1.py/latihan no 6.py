# SOAL NO 6

#Buat program yang meminta pengguna memasukkan umur mereka. Program harus terus meminta input
# selama pengguna memasukkan nilai yang tidak valid (bukan angka atau angka di luar rentang wajar, misal <
# 0 atau > 100). Gunakan while True loop, try-except untuk menangani ValueError, dan if untuk
# mengecek rentang. Jika input sudah valid, cetak umur tersebut dan hentikan loop dengan break.

# Latihan 6: Validasi Input dengan while

while True:
    try:
        umur = int(input("Masukkan umur Anda: "))
        
        if umur < 0 or umur > 100:
            print("Umur tidak wajar. Harap masukkan umur antara 0 dan 100.")
        else:
            print(f"Terima kasih. Umur Anda adalah {umur}.")
            break  # keluar dari loop karena input valid
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
