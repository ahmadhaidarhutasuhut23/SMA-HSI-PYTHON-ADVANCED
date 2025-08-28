#  Mencari Bilangan Prima Pertama
#Buat program untuk menemukan dan mencetak 5 bilangan prima pertama setelah angka 1. Bilangan prima
# adalah bilangan yang hanya bisa dibagi oleh 1 dan dirinya sendiri.
# Gunakan while loop luar untuk memastikan kamu sudah menemukan 5 bilangan prima.
# Gunakan for loop di dalamnya untuk mengecek apakah sebuah angka bisa dibagi oleh angka lain
# selain 1 dan dirinya sendiri.
# Kamu akan butuh sebuah "flag" (variabel boolean) untuk menandai apakah sebuah angka prima atau tidak.

# Latihan 9: Mencari Bilangan Prima Pertama

count = 0       # jumlah bilangan prima yang sudah ditemukan
angka = 2       # mulai dari angka 2 (bilangan prima terkecil)

while count < 5:
    prima = True
    for i in range(2, angka):   # cek pembagi dari 2 sampai angka-1
        if angka % i == 0:
            prima = False
            break
    
    if prima:
        print(angka)
        count += 1   # tambah jumlah bilangan prima yang ditemukan
    angka += 1       # lanjut ke angka berikutnya

