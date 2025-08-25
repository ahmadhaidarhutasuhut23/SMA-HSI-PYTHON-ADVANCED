import re

teks = "python adalah bahasa yang menyenangkan, python mudah dipelajari."

hasil_search = re.search('python', teks)
if hasil_search:
    print("re.search() →", hasil_search.group())

hasil_findall = re.findall('python', teks)
print("re.findall() →", hasil_findall)
