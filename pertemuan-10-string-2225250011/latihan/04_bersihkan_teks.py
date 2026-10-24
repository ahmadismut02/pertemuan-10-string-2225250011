# Menghapus spasi berlebih di tengah kalimat dan mengubah kapitalisasi kalimat

teks = "   belajar   python   untuk   pendidikan   "

# 1. Hapus spasi di awal dan akhir
teks = teks.strip()

# 2. Kurangi spasi berlebih di tengah menggunakan loop
while "  " in teks:
    teks = teks.replace("  ", " ")

print("Teks Bersih:", teks.capitalize())
