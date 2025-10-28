secret_number = 7

while True:
    try:
        tebakan = int(input("Masukkan tebakan (1-10): "))
    except ValueError:
        print("Input tidak valid! Harus angka antara 1-10.\n")
        continue  # kembali ke awal loop, minta input lagi

    if tebakan == secret_number:
        print("🎉 Selamat! Anda benar!")
        break
    else:
        print("Salah, coba lagi!\n")
