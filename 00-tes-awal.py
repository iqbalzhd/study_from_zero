"""
TES DIAGNOSTIK AWAL (Tanpa Bantuan AI)

Soal 1:
Buat fungsi hitung_bayar(total_belanja). Jika >= 100000, diskon 10% dan return harga akhir.
Jika kurang, return harga asli.

Soal 2:
Diberikan nilai = [65, 80, 45, 90, 72]. Hitung ada berapa banyak angka >= 70, lalu cetak hasilnya.

Soal 3:
Diberikan profil = {"nama": "Zed", "semester": 7}.
Apa yang terjadi jika memanggil profil["jurusan"], dan bagaimana cara aman mengambilnya
dengan nilai default "Belum diisi" agar tidak crash?
(Catatan: akses langsung [] akan memunculkan KeyError)
"""

# Jawaban Soal 1
def hitung_bayar(total_belanja):
    if total_belanja >= 100000:
        total_belanja = total_belanja - (total_belanja * 10 / 100)
        return total_belanja
    else:
        return total_belanja


# Jawaban Soal 2
nilai = [65, 80, 45, 90, 72]
nilai.sort(reverse=True)
nilaiFilter = []
for i in nilai:
    if i >= 70:
        nilaiFilter.append(i)
    else:
        break

print(nilaiFilter)
print(len(nilaiFilter))


# Jawaban Soal 3
profil = {
    "nama": "Zed",
    "semester": 7,
}
jurusan = profil.get("jurusan", "Belum diisi")
print("profil:", jurusan)