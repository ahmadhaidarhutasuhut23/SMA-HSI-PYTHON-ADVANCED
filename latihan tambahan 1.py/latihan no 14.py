# SOAL NO 14

# Gunakan for loop dengan range() untuk menghitung mundur dari 20 ke 1. Tapi, jika angka tersebut
# adalah kelipatan 4, jangan cetak angka tersebut (gunakan continue).
# Contoh Output (sebagian):
# 20 (dilewati)
# 19
# 18
# 17
# 16 (dilewati)
# 15
# ...

# Latihan 14: Hitung Mundur dengan continue

for i in range(100, 0, -1):   # mundur dari 20 ke 1
    if i % 25 == 0:
        continue             # lewati jika kelipatan 4
    print(i)
