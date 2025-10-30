import random

def ambil_soal():
    soal_asli = []
    with open("bank_soal.txt", "r", encoding="utf-8") as file:
        for line in file:
            soal_asli.append(line.strip())
    return soal_asli

def buat_soal():
    soal_asli = ambil_soal()
    random.shuffle(soal_asli)

    soal_ujian = []
    for i in range(min(10, len(soal_asli))):
        soal = soal_asli[i]
        data = soal.split("|")
        pertanyaan = data[0]
        semua_jawaban = data[1]

        jawaban = semua_jawaban.split(",")
        jawaban_benar = jawaban[0]

        random.shuffle(jawaban)

        soal_ujian.append({
            "pertanyaan": pertanyaan,
            "jawaban": jawaban,
            "jawaban_benar": jawaban_benar,
        })
    return soal_ujian

def app_ujian():
    soal_ujian = buat_soal()
    opsi = ["A", "B", "C", "D"]
    jawaban_benar = 0
    jawaban_salah = 0

    for i, soal in enumerate(soal_ujian, start=1):
        print(f"\nPertanyaan {i}: {soal['pertanyaan']}")
        print("Jawaban:")
        for j in range(len(soal["jawaban"])):
            print(f"{opsi[j]}. {soal['jawaban'][j]}")

        jawaban_user = input("Pilih jawaban (A/B/C/D): ").upper()
        if jawaban_user not in opsi:
            print("Input tidak valid, dihitung salah.")
            jawaban_salah += 1
            continue

        jawaban_user_index = opsi.index(jawaban_user)
        jawaban_asli_user = soal["jawaban"][jawaban_user_index]

        if jawaban_asli_user == soal["jawaban_benar"]:
            print("Jawaban benar!")
            jawaban_benar += 1
        else:
            print(f"Jawaban salah. Jawaban benar: {soal['jawaban_benar']}")
            jawaban_salah += 1

    print("\n===== HASIL UJIAN =====")
    total = jawaban_benar + jawaban_salah
    print(f"Jawaban benar : {jawaban_benar}")
    print(f"Jawaban salah : {jawaban_salah}")
    print(f"Nilai akhir   : {jawaban_benar / total * 100:.2f}%")

app_ujian()
