siswa = {
    "nama": "biru",
    "umur": 19,
    "kelas": "17A",
}

print(siswa)
print(siswa["nama"])

siswa["kelas"] = "19A"

del siswa["umur"]
print(siswa)

for key in siswa:
    print(key, siswa[key])

for key, value in siswa.items():
    print(key, value)