# SOAL no 12
#Ini adalah soal wawancara coding klasik. Tulis program yang menggunakan for loop untuk mencetak angkadari 1 hingga 100, dengan aturan:
# Jika angka tersebut kelipatan 3, cetak "Fizz".
# Jika angka tersebut kelipatan 5, cetak "Buzz".
# Jika angka tersebut kelipatan 3 dan 5, cetak "FizzBuzz".
# Jika tidak memenuhi ketiganya, cetak angka itu sendiri.

# Latihan 12: Permainan "FizzBuzz"

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
