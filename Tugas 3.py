# perulangan while
# kondisi :
# aksi

angka = int(input("Masukkan angka: "))

while angka < 0:
    print("Harus positif!")
    angka = int(input("Masukkan angka: "))

print("Angka yang dimasukkan:", angka)