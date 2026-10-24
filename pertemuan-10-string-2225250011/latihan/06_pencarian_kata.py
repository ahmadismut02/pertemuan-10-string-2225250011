# Memeriksa keberadaan kata, menghitung frekuensi, dan menemukan indeks posisi awal

teks = "Python untuk data. Python untuk pendidikan."
teks_bersih = teks.lower()
kata = "python"

print("Apakah kata ada dalam teks? :", kata in teks_bersih)
print("Jumlah kemunculan kata      :", teks_bersih.count(kata))
print("Indeks awal kemunculan      :", teks_bersih.find(kata))
