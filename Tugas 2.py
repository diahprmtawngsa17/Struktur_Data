#Masukan nama anda: {nama pendek anda}
#Jika benar akan lanjut ke program selanjutnya
#Jika salah, akan muncul pesan "silahkan coba lagi"

#Buat program yang menampilkan tabel perkalian dari angka yang dimasukkan user (1 sampai 10).

#Contoh:
# Input nama
nama = input("Masukkan nama anda: ")
if nama == "diah":
    print(f"Selamat datang {nama}")
else:
    print("Program selesai")

# Program tabel perkalian 1 sampai 10
angka = int(input("Masukkan angka: "))

for i in range(1, 11):
    hasil = angka * i
    print(f"{angka} x {i} = {hasil}")