# Latihan 1 – class Kucing

class Kucing:
    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna

    def bersuara(self):
        print("RAWRRRRRRRRRR!")

    def perkenalkan_diri(self):
        print(f"Halo, saya kucing bernama {self.nama} dan warna saya {self.warna}.")

# Membuat 2 object
joko = Kucing("joko", "Oranye")
oreo = Kucing("oreo", "hitam putih")

# Memanggil method pada masing-masing object
joko.perkenalkan_diri()
joko.bersuara()

oreo.perkenalkan_diri()
oreo.bersuara()
