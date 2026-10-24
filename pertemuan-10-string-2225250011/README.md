# Pertemuan 10: String dan Pengolahan Teks dalam Python

**Nama Mahasiswa:** Ahmad Ismut Thoriequddin  
**NIM:** 222525011  
**Kelas:** 3A
**Mata Kuliah:** Algoritma dan Pemrograman

---

## 📌 Tujuan

1. Memahami konsep string sebagai urutan karakter yang bersifat *immutable* di Python.
2. Menguasai teknik manipulasi string: indeks, slicing, method pembersihan, *split*, *join*, dan pencarian.
3. Menerapkan fungsi pengolahan teks pada data nama mahasiswa dan kode kelas yang tidak konsisten.
4. Mendokumentasikan dan mengelola versi kode menggunakan Git dan GitHub.

---

## 📁 Struktur Program

- **`latihan/`**: Terdiri dari 6 program latihan dasar pengolahan string (`01_dasar_string.py` s.d. `06_pencarian_kata.py`).
- **`tugas/`**: File `normalisasi_data_mahasiswa.py` untuk memproses dan menormalisasi input data teks secara otomatis.

---

## 🚀 Cara Menjalankan Program

Pastikan Python 3 sudah terpasang.

### Menjalankan Latihan

```bash
python latihan/01_dasar_string.py
python latihan/02_indeks_slicing.py
python latihan/03_method_string.py
python latihan/04_bersihkan_teks.py
python latihan/05_split_join.py
python latihan/06_pencarian_kata.py
```

### Menjalankan Tugas

```bash
python3 tugas/normalisasi_data_mahasiswa.py
python tugas/normalisasi_data_mahasiswa.py
```

Di Windows, gunakan `py` jika perintah `python` tidak tersedia. Contoh:

```bash
py latihan/01_dasar_string.py
```

---

## 📊 Contoh Hasil Pengujian

| Input Nama | Input Kode Kelas | Hasil Nama Bersih | Hasil Kode Kelas | Jumlah Kata | Inisial | Status |
|---|---|---|---|---:|---|---|
| `aan hendrayana` | `pmat a 2026` | Aan Hendrayana | PMAT-A-2026 | 2 | AH | PASS |
| `fATHIYYAH MUTHMAINNAH` | `kelas b` | Fathiyyah Muthmainnah | KELAS-B | 2 | FM | PASS |
| `BUDI` | `pmtk 01` | Budi | PMTK-01 | 1 | B | PASS |
| `siti nur aisyah` | `kelas c` | Siti Nur Aisyah | KELAS-C | 3 | SNA | PASS |

---

## Refleksi Pembelajaran

- **Hal yang Dipahami:** Saya memahami bahwa string bersifat *immutable*, sehingga setiap operasi pembersihan (seperti `strip()` atau `replace()`) menghasilkan string baru tanpa mengubah nilai variabel aslinya secara langsung.
- **Masalah & Solusi:** Awalnya, spasi ganda di tengah nama tidak bisa dihilangkan hanya dengan `.strip()`. Solusinya adalah menggunakan penggabungan `.split()` dan `" ".join()` untuk menyatukan kembali kata-kata secara konsisten.
