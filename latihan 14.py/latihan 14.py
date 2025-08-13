# latihan no 1

# Membuat list kosong
belanjaan = []

# Menambahkan "Telur", "Susu", "Roti"
belanjaan.append("Telur")
belanjaan.append("Susu")
belanjaan.append("Roti")

# Menambahkan "Apel" di awal
belanjaan.insert(0, "Apel")

# Menghapus "Susu"
belanjaan.remove("Susu")

# Cetak list akhir
print("Daftar belanjaan:", belanjaan)

#----------------------------


# latihan no 2

# List nilai
nilai = [98, 76, 88, 100, 54]

# Mengurutkan menggunakan sorted()
nilai_terurut = sorted(nilai)

# Cetak list asli
print("List asli:", nilai)

# Cetak list baru
print("List terurut:", nilai_terurut)
 
#--------------------------------

# latihan no 3


# Meminta input dari pengguna
kalimat = input("Masukkan sebuah kalimat: ")

# Mengubah menjadi list kata
kata_kata = kalimat.split()

# Menghitung jumlah kata
print("Jumlah kata:", len(kata_kata))

# Mengurutkan kata-kata berdasarkan abjad
kata_kata.sort()

# Cetak list yang sudah terurut
print("Kata-kata terurut:", kata_kata)
 

#------------------------------------------

# latihan no 4

a = [1, 2, 3, 4, 5]
b = a
c = a.copy()

b[1] = 20
c[1] = 30

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

#-------------------------------------------