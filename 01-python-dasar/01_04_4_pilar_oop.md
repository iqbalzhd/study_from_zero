# 4 Pilar Utama OOP (Object-Oriented Programming) di Python

Catatan ringkas ini merangkum 4 pilar utama OOP beserta contoh penerapannya pada studi kasus **Sistem Dompet Digital** (`01-04-oop-dasar.py`) dan kaitannya dengan **Django**.

---

## 1. Encapsulation (Enkapsulasi)
**Konsep:** Membungkus data (*atribut*) dan perilaku (*method*) ke dalam satu `class`, sekaligus melindungi data agar tidak dimodifikasi sembarangan dari luar tanpa melewati aturan validasi.

* **Contoh pada `Dompet`:**
  Atribut `self.saldo` tidak diubah langsung dari luar class (misalnya `andi.saldo = -500000`), melainkan wajib melalui method `topup()`, `withdraw()`, dan `transfer()` yang sudah dilengkapi validasi `value > 0` dan pengecekan kecukupan saldo.
* **Konvensi Python:**
  Untuk menandai bahwa sebuah atribut bersifat *internal/private* dan tidak boleh disentuh langsung dari luar, programmer Python memberi awalan garis bawah, misalnya `self._saldo` (protected) atau `self.__saldo` (private name mangling).

---

## 2. Inheritance (Pewarisan)
**Konsep:** Membuat *child class* baru yang otomatis mewarisi atribut dan method dari *parent class*, sehingga kita tidak perlu menyalin ulang kode yang sama.

* **Contoh pada `Dompet`:**
  ```python
  class DompetPremium(Dompet):
      def transfer(self, penerima, value):
          status = super().transfer(penerima, value)
          if value >= 100000 and status is True:
              self.saldo += 5000
              self.history("Cashback", 5000)
          return status
  ```
  `DompetPremium` langsung memiliki fitur `topup`, `withdraw`, `history`, dan `cek_saldo` milik `Dompet` tanpa menulis ulang satu baris pun.
* **Kaitan dengan Django:**
  Saat membuat tabel database di Django Models, kita selalu menulis `class Tugas(models.Model):`—class `Tugas` mewarisi seluruh kemampuan penyimpanan database milik `models.Model`.

---

## 3. Polymorphism (Polimorfisme)
**Konsep:** *"Satu nama, banyak bentuk perilaku."* Dua class yang berbeda (atau induk dan anak) memiliki method dengan nama yang **sama**, tetapi menghasilkan perilaku yang **berbeda** sesuai jenis objeknya.

* **Contoh pada `Dompet`:**
  Baik objek `biasa = Dompet("Andi", 100000)` maupun `premium = DompetPremium("Budi", 200000)` sama-sama memiliki method `.transfer(penerima, value)`.
  * Saat `biasa.transfer(...)` dipanggil → hanya memindahkan saldo.
  * Saat `premium.transfer(...)` dipanggil dengan nominal `>= 100000` → memindahkan saldo **sekaligus** memberikan cashback `5000`.

---

## 4. Abstraction (Abstraksi)
**Konsep:** Menyembunyikan detail kerumitan proses di balik antarmuka (*interface*) yang sederhana, sehingga pengguna cukup tahu cara memakainya tanpa perlu memahami proses internal di belakang layar.

* **Contoh pada `Dompet`:**
  Pemanggil cukup menulis satu baris sederhana:
  ```python
  premium.transfer(biasa, 150000)
  ```
  Di balik satu baris tersebut, sistem secara otomatis mengecek identitas objek (`penerima != self`), memvalidasi saldo dan nominal positif, memperbarui saldo dua objek berbeda, mencatat riwayat di pengirim dan penerima, lalu menghitung cashback—tanpa membebani pemanggil dengan detail teknisnya.
* **Tingkat lanjut di Python:**
  Abstraksi formal juga bisa dibuat menggunakan modul `abc` (*Abstract Base Class*) untuk memaksa setiap *child class* mengimplementasikan method tertentu.
