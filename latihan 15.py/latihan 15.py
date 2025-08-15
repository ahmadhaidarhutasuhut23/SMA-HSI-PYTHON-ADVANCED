# Latihan 1: Membuat dan Mengakses
biodata = {
    "nama": "Ahmad Haidar",
    "umur": 18,
    "hobi": ["olahraga", "berenang"],
    "sudah_menikah": False
}

# Cetak seluruh dictionary
print(biodata)

# Cetak hanya value dari key "nama"
print(biodata["nama"])

# Cetak hobi pertama dari list hobi
print(biodata["hobi"][0])


#---------------------------------------------------------------

# latihan no 2 Modifikasi Dictionary

# Tambahkan key baru
biodata["kota"] = "cirebon"

# Ubah umur menjadi tahun depan
biodata["umur"] = biodata["umur"] + 1

# Cetak dictionary terbaru
print(biodata)



#---------------------------------------------------------------

# Latihan 3 Penggunaan .get()

# Mencoba akses key "pekerjaan" dengan bracket notation (ERROR)
# print(biodata["pekerjaan"])  # -> Akan error KeyError, jadi kita komentari

# Menggunakan .get() tanpa default
print(biodata.get("pekerjaan"))  # None

# Menggunakan .get() dengan default
print(biodata.get("pekerjaan", "Pelajar"))



#---------------------------------------------------------------

# Latihan 4 Histogram Kata


# Meminta kalimat dari pengguna
kalimat = input("Masukkan sebuah kalimat: ")

# Ubah ke lowercase agar tidak membedakan huruf besar/kecil
kalimat = kalimat.lower()

# Pecah kalimat menjadi list kata
kata_kata = kalimat.split()

# Buat dictionary kosong untuk histogram
histogram = {}

# Loop setiap kata untuk menghitung frekuensinya
for kata in kata_kata:
    if kata in histogram:
        histogram[kata] += 1
    else:
        histogram[kata] = 1

# Cetak histogram
print(histogram)

