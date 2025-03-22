# latihan 1
# nama = input("masukan nama anda: ")
# print("Hello",nama)

# def hitung_umur(thn_lahir, thn_sekarang):
#     umur = thn_sekarang - thn_lahir
#     return umur 
# thn_lahir = int(input("masukan tahun lahir anda: "))
# thn_sekarang = int(input("masukan tahun sekarang: "))

# umur = hitung_umur(thn_lahir, thn_sekarang)
# print("umur anda saat ini adalah", umur, "tahun")

# Contoh Variabel dan Tipe Data
x = 5
y = 10.5
nama = "Firman"
print("Contoh Variabel:")
print("x:", x, "y:", y, "nama:", nama)

# Contoh Fungsi
def tambah(a, b):
    return a + b

print("\nContoh Fungsi:")
print("Hasil tambah 5 dan 3 =", tambah(5, 3))

# Contoh Pengkondisian
print("\nContoh Pengkondisian:")
if x > 0:
    print("x adalah bilangan positif")
else:
    print("x adalah bilangan negatif")

# Contoh Loop
print("\nContoh Loop:")
for i in range(5):
    print("Iterasi ke-", i)

# Contoh List dan Dictionary
daftar_buah = ["apel", "jeruk", "pisang"]
print("\nContoh List:")
print("Daftar buah:", daftar_buah)

data_siswa = {"nama": "Firman", "umur": 20}
print("\nContoh Dictionary:")
print("Data siswa:", data_siswa)

# contoh oop sederhana
class mobil:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna
        
    def info(self):
        print("\nmerek mobil:", self.merk)
        print("warna mobil:", self.warna)
        
mobil1 = mobil("Toyota", "Hitam")
mobil1.info()

# kode acept
# try:
#     hasil = 10 / 0
# except ZeroDivisionError:
#     print("tidak dapat membagi dengan noll")
# finally:
#     print("program selesai",hasil)
    
# lirik laguu
import time
import sys

def type_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
lyrics = [
  "\nDan Kau hadir merubah segalanya",
  "\nmenjadi lebih indah",
  "\nKau bawa cintaku setinggi angkasa",
  "\nMembuatku Merasa Sempurna",
]
for line in lyrics:
    type_effect(line, 0.1)
    time.sleep(0.5)
    
class Motor:
    def __init__(ini, merek, warna):
        ini.merek = merek
        ini.warna = warna
        
    def infomaseh(ini):
            print("\nmerek motor:", ini.merek)
            print("warna motor:", ini.warna)
            
motor1 = Motor("kawasaki", "hijau")
motor1.infomaseh()