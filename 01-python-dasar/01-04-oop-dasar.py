"""
MINGGU 2 - SESI 4: OOP Dasar Python - Sistem Dompet Digital (Tanpa Bantuan AI)

Soal:
Buatlah sistem dompet digital berbasis OOP dengan ketentuan arsitektur berikut:

1. class Dompet:
   - __init__(self, pemilik, saldo_awal=0):
     Menyimpan nama pemilik, saldo (jika saldo_awal negatif, atur menjadi 0),
     dan list kosong riwayat untuk mencatat log transaksi.
   - top_up(self, jumlah):
     Menambah saldo hanya jika jumlah > 0, lalu mencatat ke riwayat.
     Jika tidak valid, tampilkan pesan error dan jangan ubah saldo.
   - tarik(self, jumlah):
     Mengurangi saldo hanya jika jumlah > 0 dan saldo mencukupi, lalu mencatat ke riwayat.
   - transfer(self, penerima, jumlah):
     Parameter penerima adalah objek Dompet lain. Pastikan:
     * Tidak bisa transfer ke diri sendiri.
     * jumlah > 0 dan saldo pengirim mencukupi.
     * Jika valid: saldo pengirim berkurang, saldo penerima bertambah,
       dan keduanya mencatat transaksi tersebut ke riwayat masing-masing.

2. class DompetPremium(Dompet) [Inheritance]:
   - Mewarisi Dompet menggunakan super().__init__(...).
   - Menambahkan aturan khusus pada transfer: setiap kali DompetPremium berhasil
     mentransfer minimal 100000, pemiliknya otomatis mendapat cashback 5000
     yang langsung masuk ke saldo dan tercatat di riwayat.
     (Jika transfer gagal, cashback tidak boleh cair).

3. Skenario Pengujian:
   - Buat minimal 2 akun (1 DompetPremium dan 1 Dompet biasa).
   - Uji skenario berhasil (top-up, transfer >= 100000) dan skenario gagal
     (transfer ke diri sendiri, tarik melebihi saldo, atau nominal <= 0).
   - Cetak saldo akhir dan seluruh isi riwayat kedua akun.
"""

# Tulis kode Anda di bawah ini:

from pyclbr import Class


class Dompet:
    def __init__(self, nama, saldo_awal=0):
        self.nama = nama
        self.saldo = saldo_awal if saldo_awal >= 0 else 0
        self.transaksi = []

    def cek_saldo(self):
        print("Jumlah Saldo anda : ", self.saldo)

    def history(self, status, value):
        self.transaksi.append({"status": status, "value" : value, "saldo_akhir" : self.saldo})
      
    def show_history(self):
        for i in self.transaksi:
            print(i["status"], "|",i["value"], "|", i["saldo_akhir"])
            
          
    def topup(self,value):
        if value > 0:
            self.saldo += value
            self.history("topup", value)
        else:
            print("Nominal top up tidak valid")

    def withdraw(self,value):
        if value > 0 and self.saldo >= value:
            self.saldo -= value
            self.history("withdraw", -value)
        else:
            print("Nominal tarik tidak valid atau saldo tidak mencukupi")

    def transfer(self, penerima, value):
        if penerima != self and value <= self.saldo and value > 0:
            self.saldo -= value
            penerima.saldo +=value
            self.history(f"Transfer to {penerima.nama}", -value)
            penerima.history(f"Receive transfer from {self.nama}", value)
            return True
        else:
            if penerima == self:
                print("Tidak bisa transfer ke diri sendiri")
            elif value > self.saldo:
                print("Saldo anda tidak cukup untuk melakukan transfer")
            else:
                print("Data yang anda input tidak valid")
            return False


class DompetPremium(Dompet):
    def __init__(self, nama, saldo_awal=0):
        super().__init__(nama, saldo_awal)
        # Kalau tidak ada perubahan tidak pakai def init tidak apa apa
      
    def transfer(self, penerima, value):
        status = super().transfer(penerima, value)
        if value >= 100000 and status is True:
            self.saldo += 5000
            super().history("Cashback", 5000)


biasa = Dompet("andi", 100000)
premium = DompetPremium("Budi", 200000)

     
biasa.topup(75000)
biasa.transfer(biasa, 50000)
biasa.transfer(premium, 500000)
biasa.transfer(premium, 50000)
biasa.transfer(premium, 0000)
premium.transfer(biasa, 150000)
biasa.withdraw(0)
biasa.withdraw(5000)
biasa.withdraw(500000)
biasa.show_history()
premium.show_history()
biasa.cek_saldo()
premium.cek_saldo()





