"""
MINGGU 2 - SESI 5: Error Handling & Custom Exception (Tanpa Bantuan AI)

Soal:
Buatlah simulasi backend checkout e-commerce yang memisahkan lapisan logika bisnis
(raise, tanpa print error) dengan lapisan pemanggil (try/except yang tahan banting):

1. Custom Exceptions:
   Buat 2 class error baru yang mewarisi Exception:
   - StokTidakCukupError
   - KuponTidakValidError

2. Fungsi Logika proses_checkout(nama_produk, qty, kode_kupon=None):
   Di dalam fungsi ini, JANGAN gunakan print(). Validasi dengan melempar (raise) error:
   - Jika nama_produk tidak ada di katalog -> raise KeyError(...)
   - Jika qty <= 0 -> raise ValueError(...)
   - Jika qty > stok -> raise StokTidakCukupError(...)
   - Jika kode_kupon diisi (bukan kosong/None) dan tidak ada di kupon_diskon -> raise KuponTidakValidError(...)
   - Jika semua valid: kurangi stok di katalog, hitung total akhir (dikurangi diskon jika ada kupon),
     lalu return total akhir tersebut.
     (Perhatikan urutan validasi: stok tidak boleh berkurang jika kupon tidak valid!)

3. Lapisan Pemanggil Interaktif (while True + try/except):
   - Minta input nama_produk (ketik "exit" untuk keluar), qty, dan kode_kupon
     (boleh tekan Enter jika tidak memakai kupon).
   - Bungkus konversi int(qty) dan pemanggilan proses_checkout(...) dengan try/except
     untuk menangkap masing-masing error secara spesifik:
     ValueError, KeyError, StokTidakCukupError, KuponTidakValidError.
   - Pastikan program tidak pernah crash meskipun user mengetik huruf di qty,
     memasukkan produk yang tidak ada, atau menginput kupon palsu.
"""

katalog = {
    "kopi": {"harga": 25000, "stok": 5},
    "roti": {"harga": 15000, "stok": 2},
}
kupon_diskon = {"HEMAT10": 0.10, "PROMO20": 0.20}

class StokTidakCukupError(Exception):
    pass
  
class KuponTidakValidError(Exception):
    pass
  
def proses_checkout(nama_produk, qty, kode_kupon=None):
    
    if nama_produk not in katalog:
        raise KeyError ("Nama Produk tidak ada")
    stok = katalog[nama_produk]["stok"]
    harga = katalog[nama_produk]["harga"]
    if qty <= 0:
        raise ValueError("Jumlah quantity tidak valid")
    elif qty > stok:
        raise StokTidakCukupError(f"Sisa stok tidak mencukupi, saat ini sihsa stok ada sebanyak {stok} buah")
    elif kode_kupon != "" and kode_kupon not in kupon_diskon:
        raise KuponTidakValidError(f"kode kupon {kode_kupon} tidak valid")

    total = qty * harga
    katalog[nama_produk]["stok"] -= qty
    if kode_kupon != "" and kode_kupon in kupon_diskon:
        total -= (total*kupon_diskon[kode_kupon])
    return total

while True:
    try:
        nama_produk = input("Masukkan nama produk yang sesuai : ")
        if nama_produk == "exit":
            break
        qty = int(input("Masukkan Jumlah barang yang ingin dibeli :"))
        kode_kupon = input("Masukkan Kode Kupon (opsional)")
    
        proses_checkout(nama_produk, qty, kode_kupon)
    except KeyError:
        print("Error : Tolong masukkan nama produk yang sesuai")
    except ValueError:
        print("Error : Tolong masukkan jumlah quantity yang valid")
    except StokTidakCukupError:
        print("Error : Jumlah stok tidak sebanyak itu")
    except KuponTidakValidError:
        print("Error : Kode kupon tidak valid")
    else:
        print("Pembelian berhasil")
