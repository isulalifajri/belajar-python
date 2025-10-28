nama = "langit"
umur = 26

pesan = "nama saya " + nama + ", umur " + str(umur)

print(pesan)
print(len(nama))
print(len(pesan))

nama = "hujan"
print(nama[0]) #dimulai dari char awal
print(nama[1])
print(nama[2])

print(nama[-1]) #dimulai dari char akhir
print(nama[-2])
print(nama[-3])

print(nama[0:3]) #index(0, 1, 2)
print(nama[:3]) #dari awal -> index 0 sampai index 2
print(nama[2:]) #dari index 2 sampai akhir
print(nama[:]) #seluruh string

nama = "langit biru"
print(nama.upper())
print(nama.lower())
print(nama.title())
print(nama.capitalize())

nama = " embun "
print(nama)
print(nama.strip())

kalimat = "embun di sore hari"
print("kalimat: ",kalimat.replace("sore", "pagi"))
print("jumlah huruf a pada kalimat diatas:",kalimat.count("a")) #menghitung jumlah huruf a

kalimat = "senja di langit biru"
position = kalimat.find("langit")
print("index ke", position)

kalimat = "Baris pertama\nBaris kedua"
print(kalimat)

kalimat = "Nama:\tSuci\nUmur:27"
print(kalimat)

location = "D:\\Python\\study"
print(location)

#menggunakan f-string
kalimat = f"Halo, {nama}, salam kenal"

price = 2000
jumlah = 3

result = f"harga {jumlah} buah ini {price}"
print(result)