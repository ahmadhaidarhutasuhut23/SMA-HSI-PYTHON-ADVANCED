# SOALL NO 8

# Buat program yang meminta pengguna memasukkan sebuah kalimat. Program akan mencetak ulang kalimat
# tersebut huruf per huruf, tetapi semua huruf vokal (a, i, u, e, o, baik besar maupun kecil) akan
# dilewati (tidak dicetak).
# Gunakan for loop untuk mengiterasi setiap huruf dalam kalimat.
# Gunakan if dan continue untuk melewati huruf vokal.

# Contoh Input: "saya anak pintar"
# Contoh Output: Sy ank pnt

# Latihan 8: Iterasi String dengan continue

kalimat = input("Masukkan sebuah kalimat: ")

for huruf in kalimat:
    if huruf.lower() in "aiueo":   # cek huruf vokal
        continue                  # lewati huruf vokal
    print(huruf, end="")          # cetak huruf selain vokal
