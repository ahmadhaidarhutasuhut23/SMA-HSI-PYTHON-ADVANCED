# SOAL NO 15

# Buat program login sederhana yang akan "mengunci" setelah 3 kali gagal
# 1. Buat variabel password_benar = "rahasia123" dan maks_percobaan = 3
# 2. Gunakan for loop dengan range(maks_percobaan)
# 3. Di dalam loop, minta pengguna memasukkan password
# 4. Jika password benar, cetak "Login berhasil!" dan gunakan break untuk keluar dari loop.
# 5. Jika salah, cetak pesan yang menunjukkan sisa percobaan.
# 6. Gunakan else setelah for loop. Blok ini akan berjalan jika loop selesai tanpa break (artinya semua
# percobaan gagal). Di dalamnya, cetak "Akun Anda terkunci!".

# Latihan 15: Simulasi Password Lockout

password_benar = "rahasia123"
maks_percobaan = 3

for percobaan in range(maks_percobaan):
    password = input("Masukkan password: ")
    if password == password_benar:
        print("Alhamdulillah Login berhasil!")
        break
    else:
        sisa = maks_percobaan - (percobaan + 1)
        print(f"Password salah! Sisa percobaan: {sisa}")
else:
    print("Akun Anda terkunci!")
