def nama_function():
    print("Hello dari function")

nama_function()

def sapa_nama(nama):
    print("Halo", nama)
    print("senang bertemu denganmu")

# Memanggil function dg argument
sapa_nama("Alice")
sapa_nama("Bob")

def hitung_luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    print("Luas persegi panjang:", luas)

hitung_luas_persegi_panjang(10, 5)
hitung_luas_persegi_panjang(5, 3)

def hitung_luas_lingkaran(radius):
    pi = 3.14159
    luas = pi * radius * radius
    return luas

luas1 = hitung_luas_lingkaran(5)
luas2 = hitung_luas_lingkaran(10)

print("Luas lingkaran radius 5: ", luas1 )
print("Luas lingkaran radius 10: ", luas2 )
print("Total luas: ", luas1 + luas2)

def sapa(nama, sapaan="Halo"):
    print(sapaan, nama)

sapa("Alice")
sapa("Bob", "Hei")

def perkenalan(nama, umur, kota):
    print("Nama: ", nama)
    print("Umur: ", umur, "tahun")
    print("Asal: ", kota)
    print("----")

#urutan harus sesuai
perkenalan("Alice", 25, "Bandung")

#keyword arguments (urutan bebas)
perkenalan(kota="Bandung", nama="Bob", umur=30)
perkenalan(umur=26, kota="Bogor", nama="Alice")

def buat_profil(nama, umur, kota="Jakarta", pekerjaan="Belum bekerja"):
    print(f"=== PROFIL {nama.upper()} ===")
    print(f"Umur: {umur} tahun")
    print(f"Kota: {kota}")
    print(f"Pekerjaan: {pekerjaan}")
    print

# Positional + keywoard arguments
buat_profil("Alice", 25)
buat_profil("Bob", 30, kota="Bandung")
buat_profil("langit", 26, pekerjaan="Developer")

def local_varibel():
    x = 10
    print("Nilai x adalah", x)
local_varibel()

variabel_global = "Alice"

def tampilkan_nama():
    print("Nama:", variabel_global)

def ubah_nama():
    global variabel_global
    variabel_global = "Cahaya"

tampilkan_nama()
ubah_nama()
tampilkan_nama()

def cetak_list(*list): #tanda bintang artinya bisa memasukkan lebih dari 1 data
    for item in list:
        print(item) 

cetak_list(1, 2, 3, 4, 5)

def cetak_dict(**dict):
    for key, value in dict.items():
        print(f"{key}: {value}")

cetak_dict(nama="Alice", umur=25, kota="Jakarta")

