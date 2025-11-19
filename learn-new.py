print("Manipulasi String")

n = 100

for i in range(1, n + 1):
    if i % 3 == 0 :  # jika bisa di bagi 3
        print(f"{i} Tik")    # ubah angkanya jadi tik
    elif i % 2 == 0 :
        print(f"{i} Tok")
    else:
        print(f"{i} Tiktok")