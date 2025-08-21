# Latihan 2 – class RekeningBank

def rupiah(angka: int) -> str:
    # Hanya biar rapi saat ditampilkan (Rp 450.000)
    return f"Rp {angka:,.0f}".replace(",", ".")

class RekeningBank:
    def __init__(self, nomor_rekening, nama_pemilik):
        self.nomor_rekening = nomor_rekening
        self.nama_pemilik = nama_pemilik
        self.saldo = 0  # saldo awal

    def lihat_saldo(self):
        print(f"Saldo saat ini: {rupiah(self.saldo)}")

    def setor(self, jumlah):
        if jumlah <= 0:
            print("Jumlah setor harus lebih dari 0.")
            return
        self.saldo += jumlah
        print(f"Setor {rupiah(jumlah)} berhasil. Saldo baru: {rupiah(self.saldo)}")

    def tarik(self, jumlah):
        if jumlah <= 0:
            print("Jumlah tarik harus lebih dari 0.")
            return
        if jumlah > self.saldo:
            print("Saldo tidak mencukupi")
            return
        self.saldo -= jumlah
        print(f"Tarik {rupiah(jumlah)} berhasil. Saldo baru: {rupiah(self.saldo)}")

# Sesi uji: rekening_budi
rekening_budi = RekeningBank("1234567890", "Budi")

rekening_budi.lihat_saldo()   # 0
rekening_budi.setor(1000_000)  # jadi 1000.000
rekening_budi.setor(5000_000)  # jadi 5000.000
rekening_budi.tarik(7000_000)  # gagal (melebihi saldo)
rekening_budi.tarik(300_000)  # berhasil, sisa 5700.000
rekening_budi.lihat_saldo()   # cek akhir
