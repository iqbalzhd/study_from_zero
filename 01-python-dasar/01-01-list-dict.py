"""
MINGGU 1 - SESI 1: List of Dictionaries (Tanpa Bantuan AI)

Soal:
Diberikan data keranjang belanja berisi nama, harga, dan qty.
Buatlah fungsi hitung_total(daftar_belanja) yang:
1. Menghitung dan mengembalikan (return) total harga keseluruhan (harga * qty).
2. Mencetak nama barang yang subtotalnya lebih dari 50000.
"""

keranjang = [
    {"nama": "Kopi Susu", "harga": 25000, "qty": 2},
    {"nama": "Roti Bakar", "harga": 18000, "qty": 1},
    {"nama": "Matcha Latte", "harga": 30000, "qty": 3},
]


def hitung_total(daftar_belanja):
    total = 0
    for item in daftar_belanja:
        totalItem = item["qty"] * item["harga"]
        if totalItem > 50000:
            print(f"Jumlah Pembelian {item['nama']} lebih dari 50,000")
        total += totalItem
    return total


print("Total Pembelian anda adalah :", hitung_total(keranjang))