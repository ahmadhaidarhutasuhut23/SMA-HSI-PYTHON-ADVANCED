# latihan no 4 :Dictionary dengan Tuple Key

# Dictionary papan catur
papan_catur = {}

# Isi posisi dengan tuple (baris, kolom) sebagai key
papan_catur[(1, 'a')] = "Benteng Putih"
papan_catur[(1, 'b')] = "Kuda Putih"
papan_catur[(8, 'h')] = "Benteng Hitam"

# Akses isi papan
print("Isi papan pada (1, 'a'):", papan_catur[(1, 'a')])
