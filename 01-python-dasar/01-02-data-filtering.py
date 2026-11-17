# Buatlah fungsi bernama ambil_kandidat_beasiswa(data_mahasiswa) yang:
    # 1. Menyaring mahasiswa dengan syarat status aktif bernilai True DAN ipk >= 3.5.
    # 2. Mengembalikan (return) list baru yang hanya berisi nama-namanya saja.
    # 3. Panggil fungsinya dengan data mahasiswa di atas dan cetak hasilnya (output yang diharapkan: ["Dina"]).

mahasiswa = [
    {"nama": "Andi", "ipk": 3.4, "aktif": True},
    {"nama": "Budi", "ipk": 2.7, "aktif": True},
    {"nama": "Citra", "ipk": 3.8, "aktif": False},
    {"nama": "Dina", "ipk": 3.6, "aktif": True},
]
def ambil_kandidat_beasiswa(data_mahasiswa):
  student_pass =[]
  for student in data_mahasiswa:
    ipk = student.get("ipk")
    status = student.get("aktif")
    nama = student.get("nama")
    if ipk >= 3.5:
      if status is True:
        student_pass.append(nama)
  return student_pass

print(ambil_kandidat_beasiswa(mahasiswa))
