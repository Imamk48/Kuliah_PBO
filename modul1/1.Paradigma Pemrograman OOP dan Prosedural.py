# pratikum 1
class Dosen:
    def __init__(self, nama, nip, mata_kuliah):
        self.nama = nama
        self.nip = nip
        self.mata_kuliah = mata_kuliah

    def mengajar(self):
        print(f"{self.nama} sedang mengajar {self.mata_kuliah}")

class Siswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def belajar(self):
        print(f"{self.nama} sedang belajar di jurusan {self.jurusan}")

# Membuat object
dosen1 = Dosen("Pak Budi", "12345", "Pemrograman")
siswa1 = Siswa("Imam", "24241020", "PTI")

# Memanggil method
dosen1.mengajar()
siswa1.belajar()