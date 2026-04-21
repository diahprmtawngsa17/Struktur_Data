# Input nama
nama = input("Masukkan nama anda: ")

# Cek nama (misalnya nama yang benar adalah "diah")
if nama == "diah":
    print(f"Selamat datang {nama}")
else:
    print("Program selesai")

# Input umur
umur = int(input("Masukkan umur anda: "))

# Percabangan umur
if umur <= 0:
    print("Anda belum lahir")
elif umur < 18:
    print("Anda belum cukup umur")
elif umur >= 18 and umur <= 60:
    print("Anda cukup umur")
elif umur > 60:
    print("Banyakin ibadah, bentar lagi mati")

print("Program selesai")