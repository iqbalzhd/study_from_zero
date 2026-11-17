"""
MINGGU 1 - SESI 3: Mini-Proyek CLI CRUD (Tanpa Bantuan AI)

Soal:
Buatlah program To-Do List CLI dengan ketentuan berikut:
1. Siapkan satu list kosong daftar_tugas = [].
2. Tampilkan menu berulang kali dengan 4 pilihan:
   - 1. Tambah tugas: Minta user mengetik nama tugas, lalu simpan ke daftar_tugas.
   - 2. Lihat semua tugas: Tampilkan seluruh tugas dengan nomor urut mulai dari 1.
        Jika masih kosong, tampilkan pesan bahwa belum ada tugas.
   - 3. Hapus tugas: Minta user memasukkan nomor urut tugas yang ingin dihapus,
        lalu hapus dari daftar_tugas (perhatikan nomor urut 1 vs index 0).
   - 4. Keluar: Hentikan program.
3. Jika user memilih angka selain 1-4, tampilkan pesan "Pilihan tidak valid."
"""

daftar_tugas = []
def pembukaan():
    print("To-Do List CLI")

def awal():
    print("---------------------------------------------------\n Silahkan pilih menu:\n1. Tambah tugas\n2. Lihat semua tugas\n3. Hapus tugas\n4. Tutup aplikasi")
    choice = input("Tulis menu : ")
    if choice == "1":
        tambah_tugas()
    elif choice == "2":
        lihat_tugas()
    elif choice == "3":
        hapus_tugas()
    elif choice == "4":
        return 'exit'
    else:
        print("Input anda salah, silahkan masukkan lagi")
    
def ambil_data():
    urut = 1
    for i in daftar_tugas:
        print(urut, i)
        urut +=1

def tambah_tugas():
    tugas = input("Masukkan tugas baru: ")
    daftar_tugas.append(tugas)
    print(f"Tugas '{tugas}' berhasil ditambahkan.")

def lihat_tugas():
    if not daftar_tugas:
        print("Tidak ada tugas yang tersimpan.")
    else:
        ambil_data()
        
def hapus_tugas():
    if not daftar_tugas:
        print("Tidak ada tugas yang tersimpan.")
    else:
        ambil_data()
        while True:
            pilih_hapus = input("Tulis nomor tugas yang ingin di hapus : ")
            if int(pilih_hapus) > len(daftar_tugas) or int(pilih_hapus) <= 0 :
                print("Input tidak valid")
            else:
                daftar_tugas.pop(int(pilih_hapus) - 1)
                print("Berikut tampilan tugas terbaru")
                ambil_data()
                break
            


pembukaan()
while True:
    choice = awal()
    if choice == 'exit':
        break
