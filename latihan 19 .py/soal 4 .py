import re

kalimat = "Kucing, anjing, dan burung adalah hewan peliharaan."
hasil = re.findall(r'\w+g\b', kalimat)
print(hasil)
