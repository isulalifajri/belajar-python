angka = int(input("Masukkan angka : "))

if angka > 0:
    print("Angka positif")

if angka < 0:
    print("Angka negatif")

if angka == 0:
    print("Angka NOL")

nilai = int(input("Masukkan nilai: "))

if nilai >= 60:
    print("Anda lulus")
else:
    print("Anda tidak lulus")

# Menggunakan elif

value = int(input("Masukkan value: "))
if value >= 90:
    print("Grade A")
elif value >=80:
    print("Grade B")
elif value >=70:
    print("Grade C")
elif value >=60:
    print("Grade D")
else:
    print("Grade E")

umur = int(input("Masukkan umur: "))
punya_sim = input("Punya SIM? (ya/tidak) \n")

if umur >= 17 and punya_sim == "ya":
    print("Boleh mengendarai motor")
else:
    print("Tidak boleh mengendarai motor")