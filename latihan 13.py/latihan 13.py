# Latihan 1: Membuat dan Mengakses
jadwal_senin = ["Matematika", "Bahasa Indonesia", "Olahraga", "Sejarah"]

# Cetak seluruh list
print("Jadwal Senin:", jadwal_senin) 

# Cetak hanya mata pelajaran pertama
print("Pelajaran pertama:", jadwal_senin[0])

# Cetak mata pelajaran terakhir menggunakan indeks negatif
print("Pelajaran terakhir:", jadwal_senin[-1])

# ---------------------------------------------------------

# Latihan 2: Modifikasi List
# Mengubah "Olahraga" menjadi "Kimia"
jadwal_senin[2] = "Kimia"

# Cetak list yang sudah diperbarui
print("Jadwal Senin terbaru:", jadwal_senin)

# ---------------------------------------------------------

# Latihan 3: Traversing dan Modifikasi
nilai_mentah = [55, 63, 72, 81, 90]

# Loop melalui setiap indeks
for i in range(len(nilai_mentah)):
    nilai_mentah[i] += 5  # tambahkan 5 ke setiap elemen

# Cetak hasil nilai baru
print("Nilai setelah bonus:", nilai_mentah)

# ---------------------------------------------------------

# Latihan 4: Slicing dan Penggabungan
awal_minggu = ["Senin", "Selasa", "Rabu"]
akhir_minggu = ["Kamis", "Jumat", "Sabtu", "Minggu"]

# Gabungkan dua list
seminggu = awal_minggu + akhir_minggu

# Slicing untuk mendapatkan hari kerja (Senin - Jumat)
hari_kerja = seminggu[0:5]

# Cetak hasil
print("Hari kerja:", hari_kerja)
