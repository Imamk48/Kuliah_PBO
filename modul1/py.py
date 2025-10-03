class Mahasiswa:
    
    #class attribute / class variable
    jumlah_mahasiswa = 0
    
# konstruktor
    def __init__(self, name, nim, prodi):
        # instance / object variable / attribute
        self.name = name
        self.nim = nim
        self.prodi = prodi
        Mahasiswa.jumlah_mahasiswa += 1 #jumlah_mahasiswa = jumlah_mahasiswa = 1
        print(f"membuat objek mahasiswa dengan dengan nama " + self.name)
        
# membuat objek
mhs1 = Mahasiswa("Imam", "24241020", "Pti")
print("Total Mahasiswa = " + str(mhs1.jumlah_mahasiswa))

mhs2 = Mahasiswa("nilam", "24241021", "Pti")
print("Total Mahasiswa = " + str(mhs1.jumlah_mahasiswa))
