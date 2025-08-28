# SOALL NO 11

# Gunakan nested loops untuk menghasilkan pola angka berikut:
#1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# Petunjuk: Loop luar mengontrol angka baris (1 sampai 5). 
# Loop dalam mengontrol berapa kali angka tersebut dicetak di baris itu.

# Latihan 11: Nested Loops untuk Pola Angka

for i in range(1, 10):      # baris dari 1 sampai 5
    for j in range(i):     # banyak angka di tiap baris sesuai i
        print(i, end=" ")
    print()                # ganti baris setelah satu baris selesai atau <--- pindah baris
