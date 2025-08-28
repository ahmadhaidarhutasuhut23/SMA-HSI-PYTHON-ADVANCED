#  SOALLL NO 7

#Buat program untuk menghitung jumlah kuadrat dari N bilangan bulat pertama.
# -. Minta pengguna memasukkan sebuah angka N.
# 3/. Gunakan while loop untuk menghitung 1² + 2² + 3² + ... + N².
# 0. Cetak hasil akhirnya.
# Contoh Input: N = 3
# Output yang diharapkan: Jumlah kuadrat dari 3 bilangan pertama adalah: 14 (karena 11 +
# 22 + 3*3 = 1 + 4 + 9 = 14).

# Latihan 7: Pola Akumulator dengan while

N = int(input("Masukkan sebuah angka N: "))

total = 0   # variabel akumulator, menyimpan hasil penjumlahan
i = 1       # variabel penghitung awal

while i <= N: 
    total += i ** 2   # tambahkan kuadrat dari i ke total
    i += 1           # naikkan i untuk lanjut ke angka berikutnya

print(f"Jumlah kuadrat dari {N} bilangan pertama adalah: {total}")
