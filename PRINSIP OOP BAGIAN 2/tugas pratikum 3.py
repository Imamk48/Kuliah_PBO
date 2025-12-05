class Pegawai:
    def __init__(self, nama, nip, gaji_pokok):
        self.nama = nama
        self.nip = nip
        self.__gaji_pokok = gaji_pokok  # Atribut private

    def get_gaji_pokok(self):
        return self.__gaji_pokok

    def hitung_bonus(self):
        # Method ini akan di-override oleh subclass
        return 0

    def get_gaji_total(self):
        return self.__gaji_pokok + self.hitung_bonus()

    def tampilkan_info(self):
        print(f"Nama: {self.nama}, NIP: {self.nip}")
        print(f"Gaji Pokok: Rp {self.get_gaji_pokok():,.0f}")

class Manager(Pegawai):
    def __init__(self, nama, nip, gaji_pokok, tunjangan_jabatan):
        super().__init__(nama, nip, gaji_pokok)
        self.tunjangan_jabatan = tunjangan_jabatan

    def hitung_bonus(self):
        return 0.15 * self.get_gaji_pokok()

    def get_gaji_total(self):
        return super().get_gaji_total() + self.tunjangan_jabatan

    def tampilkan_info(self):
        print("--- Info Manager ---")
        super().tampilkan_info()
        print(f"Tunjangan: Rp {self.tunjangan_jabatan:,.0f}")
        print(f"Gaji Total Manager: Rp {self.get_gaji_total():,.0f}")


class StaffTeknis(Pegawai):
    def __init__(self, nama, nip, gaji_pokok, jumlah_proyek):
        super().__init__(nama, nip, gaji_pokok)
        self.jumlah_proyek = jumlah_proyek

    def hitung_bonus(self):
        return 500000 * self.jumlah_proyek

    def tampilkan_info(self):
        print("--- Info Staff Teknis ---")
        super().tampilkan_info()
        print(f"Jumlah Proyek: {self.jumlah_proyek}")
        print(f"Gaji Total Staff: Rp {self.get_gaji_total():,.0f}")


# Membuat instance dari kelas Manager dan StaffTeknis
manager = Manager("Budi Hartono", "M-001", 10000000, 5000000)
staff = StaffTeknis("Susi Susanti", "S-001", 6000000, 3)

# Menampilkan informasi pegawai
manager.tampilkan_info() 
print("\n==============================\n")
staff.tampilkan_info()
print("\n==============================\n")

# Tes Enkapsulasi
print("--- Tes Keamanan (Encapsulasi) ---")
try:
    print(staff.__gaji_pokok)  # Mencoba mengakses atribut private langsung dari luar kelas
except AttributeError as e:
    print(f"ERROR: {e}")
    print("-> TIDAK BISA diakses langsung dari luar!")

print(f"Gaji Total Susi (tetap): Rp {staff.get_gaji_total():,.0f}")  # Memastikan gaji total tetap dapat diakses melalui getter

# Membuat objek dari kelas Pegawai
print("\n==============================\n")
pegawai1 = Pegawai("Andi Saputra", "P-001", 4500000)

# Menampilkan informasi pegawai
pegawai1.tampilkan_info()

print(f"Gaji Total Pegawai: Rp {pegawai1.get_gaji_total():,.0f}")
