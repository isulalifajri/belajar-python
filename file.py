print("SIMPAN DATA NILAI")

file = open("nilai_siswa.txt", "w")

while True:
    nama = input("Nama siswa (enter utk selesai): ")
    if nama == "":
        break

    nilai = input("Nilai: ")

    # Tulis ke file
    file.write(nama + "," + nilai + "\n")
    print("Data", nama, "berhasil disimpan")

file.close()
print("Semua data berhasil disimpan ke nilai_siswa.txt")