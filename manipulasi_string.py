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
