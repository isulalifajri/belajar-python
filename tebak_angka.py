import random

def app_tebak_angka():
    angka_acak = random.randint(1, 10)
    maksimal_tebakan = 3
    tebakan = 0

    while tebakan < maksimal_tebakan:
        try:
            angka_user = int(input("Masukkan angka (1-10): "))
        except ValueError:
            print("Input tidak valid! Harus angka.\n")
            continue

        tebakan += 1

        if angka_user < angka_acak:
            print("Angka terlalu kecil!\n")
        elif angka_user > angka_acak:
            print("Angka terlalu besar!\n")
        else:
            print("🎉 Selamat! Angka benar!\n")
            break
    else:
        print("Kamu telah melewati batas tebakan.")
        print("Angka acak yang benar adalah:", angka_acak, "\n")


def app_menu():
    while True:
        print("=== Program Tebak Angka Sederhana ===")
        print("1. Tebak Angka")
        print("2. Keluar")

        try:
            pilihan = int(input("Pilihan: "))
        except ValueError:
            print("Input tidak valid! Masukkan angka 1 atau 2.\n")
            continue

        if pilihan == 1:
            app_tebak_angka()
        elif pilihan == 2:
            print("Program selesai, sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.\n")


# Jalankan program
app_menu()
