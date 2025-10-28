username = input("username: ")
password = input("password: ")

if username == "admin":

    if password == "12345":
        print("login berhasil")
        print("Selamat datang admin")
    else:
        print("Password salah")

else:
    print("Username tidak ditemukan")

hari = input("Masukkan nama hari: ").lower()

match hari:
    case "senin" | "selasa" | "rabu" | "kamis" | "jumat":
        print("Hari kerja")
    case "sabtu" | "minggu":
        print("Hari libur")
    case _:
        print("Nama hari tidak valid")