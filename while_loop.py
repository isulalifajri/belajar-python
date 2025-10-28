# Mencetak angka 1 sampai 5
angka = 1
while angka <= 5:
    print(angka)
    angka += 1

#input sampai benar
password = ""
while password != "12345":
    password = input("Masukkan Password: ")
    if password != "12345":
        print("Password salah, coba lagi!")

print("Password benar!")