def app_penjumlahan():
    print("=== Program Penjumlahan ===")
    try:
        angka1 = int(input("Angka 1: "))
        angka2 = int(input("Angka 2: "))
        hasil = angka1 + angka2
        print("Hasil penjumlahan:", hasil)
    except ValueError:
        print("Input tidak valid! Harus berupa angka.")
    input("\nTekan Enter untuk lanjut...")


def app_pengurangan():
    print("=== Program Pengurangan ===")
    try:
        angka1 = int(input("Angka 1: "))
        angka2 = int(input("Angka 2: "))
        hasil = angka1 - angka2
        print("Hasil pengurangan:", hasil)
    except ValueError:
        print("Input tidak valid! Harus berupa angka.")
    input("\nTekan Enter untuk lanjut...")


def app_perkalian():
    print("=== Program Perkalian ===")
    try:
        angka1 = int(input("Angka 1: "))
        angka2 = int(input("Angka 2: "))
        hasil = angka1 * angka2
        print("Hasil perkalian:", hasil)
    except ValueError:
        print("Input tidak valid! Harus berupa angka.")
    input("\nTekan Enter untuk lanjut...")


def app_pembagian():
    print("=== Program Pembagian ===")
    try:
        angka1 = int(input("Angka 1: "))
        angka2 = int(input("Angka 2: "))
        hasil = angka1 / angka2
        print("Hasil pembagian:", hasil)
    except ValueError:
        print("Input tidak valid! Harus berupa angka.")
    except ZeroDivisionError:
        print("Tidak bisa membagi dengan 0.")
    input("\nTekan Enter untuk lanjut...")


def app_menu():
    while True:
        print("\n=== Program Kalkulator Sederhana ===")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Keluar")

        try:
            pilihan = int(input("Pilih menu (1-5): "))
        except ValueError:
            print("Input tidak valid! Masukkan angka 1–5.")
            continue

        if pilihan == 1:
            app_penjumlahan()
        elif pilihan == 2:
            app_pengurangan()
        elif pilihan == 3:
            app_perkalian()
        elif pilihan == 4:
            app_pembagian()
        elif pilihan == 5:
            print("Sampai jumpa lagi!")
            break
        else:
            print("Pilihan tidak tersedia. Coba lagi.")
            continue


# Jalankan program
app_menu()
