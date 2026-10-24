# Memecah kalimat menjadi list kata dan menggabungkannya kembali dengan pemisah khusus

kalimat = "data teks perlu dibersihkan"

# Memecah string menjadi list kata
kata = kalimat.split()
print("List Kata   :", kata)

# Menggabungkan kembali list kata dengan tanda hubung (-)
print("Hasil Join  :", "-".join(kata))
