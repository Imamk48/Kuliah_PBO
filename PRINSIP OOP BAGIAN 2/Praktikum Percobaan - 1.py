# parent class (orang taua)
class Kendaraan:
    # konstruktor
    def __init__(self, nama):
        # atribut objek
        self.nama = nama
        print(f"Sebuah Kendaraan '{self.nama}' dibuat.")
   
       # method objek
    def maju(self):
        print(f"Kendaraan {self.nama} bergerak maju.")

# class mobil adalah chill dari class kendaraan (anak)
class Mobil(Kendaraan):
    # method untuk class anak
    def putar_AC(self):
        print(f"{self.nama}: AC dinyalakan, sejuk!")

# diluar class
print("--- Membuat Object Mobil ---")
avanza = Mobil("Avanza Putih") 
avanza.maju() 
avanza.putar_AC()

# --- Membuat Objek dari Class Kendaraan ---
print("\n--- Membuat Objek Kendaraan ---")
motor = Kendaraan("Motor Honda")
motor.maju()