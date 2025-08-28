# SOAL NO 13
# Buat program yang meminta input sebuah kata dari pengguna. Program kemudian harus membangun
# sebuah string baru berbentuk "piramida" dari kata tersebut.
# Gunakan for loop dengan range(len(kata)).
# Gunakan slicing kata[:i+1] untuk mendapatkan potongan kata di setiap iterasi

# Latihan 13: Piramida dari kata

kata = input("enter any word you like :  ")

for i in range(len(kata)):
    print(kata[:i+1])   # potong kata dari index 0 sampai i
