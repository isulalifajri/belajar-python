print("KALKULATOR SEDERHANA")

while True:
    try:
        angka1 = int(input("Angka Pertama: "))
        angka2 = int(input("Angka Kedua: "))
        hasil = angka1 / angka2
        print("Hasil:", hasil)
        break  #keluar dari loop kalau berhasil
    except ValueError:
        print("Input pengguna bukan angka\n")
        continue
    except ZeroDivisionError:
        print("Tidak bisa dibagi dengan 0\n")
        continue
    except Exception as e:
        print("Terjadi kesalahan:", e)
        continue

print("PROGRAM SELESAI")
