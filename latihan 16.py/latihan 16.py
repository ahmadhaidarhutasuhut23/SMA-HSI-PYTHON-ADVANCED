# latihan no 1
#======================================

# Dictionary harga buah
harga_buah = {"apel": 5000, "jeruk": 8500, "mangga": 7800, "pisang": 3000}

total = 0

# Iterasi dengan .items()
for buah, harga in harga_buah.items():
    print(f"Harga 1 kg {buah} adalah Rp {harga}")
    total += harga

print("Total harga semua buah adalah Rp", total)


# latihan no 2
#======================================
# Dictionary kosong
kontak = {}

# Tambahkan tiga kontak
kontak["Ibu"] = "081234567890"
kontak["Ayah"] = "081298765432"
kontak["Teman"] = "082112233445"

# Ubah nomor telepon Ibu
kontak["Ibu"] = "089912345678"

# Hapus "Teman"
kontak.pop("Teman")

# Cetak dictionary akhir
print("Kontak akhir:", kontak)

# latihan no 3
#======================================
# Nested dictionary
produk = {
    "PROD001": {"nama": "Laptop", "harga": 7500000, "stok": 5},
    "PROD002": {"nama": "samsung", "harga": 3500000, "stok": 10}
}

# Cetak nama dan harga dari PROD002
print("Nama Produk:", produk["PROD002"]["nama"])
print("Harga Produk:", produk["PROD002"]["harga"])

# latihan no 4
#======================================

# Buka file
filename = "mbox-short.txt"
hari_count = {}

with open(filename) as f: 
    for line in f:
        if line.startswith("From "):
            kata = line.split()
            hari = kata[2]   # kata ketiga adalah hari
            hari_count[hari] = hari_count.get(hari, 0) + 1

print(hari_count)
