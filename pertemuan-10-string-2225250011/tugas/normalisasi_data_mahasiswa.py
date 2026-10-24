# Tugas 4: Normalisasi Data Mahasiswa
# File: tugas/normalisasi_data_mahasiswa.py


def normalisasi_nama(nama):
    """Membersihkan spasi ganda/ujung dan mengubah format ke Title Case."""
    kata = nama.strip().split()
    return " ".join(kata).title()


def buat_inisial(nama):
    """Mengambil huruf pertama dari setiap kata nama yang sudah dinormalisasi."""
    nama_bersih = normalisasi_nama(nama)
    kata = nama_bersih.split()
    return "".join(k[0] for k in kata).upper()


def normalisasi_kode(kode):
    """Menghapus spasi, mengubah ke huruf besar, dan mengganti spasi dengan tanda hubung (-)."""
    kata = kode.strip().upper().split()
    return "-".join(kata)


def main():
    print("==========================================")
    print(" PROGRAM NORMALISASI DATA TEKS MAHASISWA ")
    print("==========================================")

    # Input dari pengguna
    nama_input = input("Masukkan Nama Lengkap : ")
    kode_input = input("Masukkan Kode Kelas   : ")

    # Proses pengolahan data
    nama_bersih = normalisasi_nama(nama_input)
    kode_bersih = normalisasi_kode(kode_input)
    inisial = buat_inisial(nama_input)
    jumlah_kata = len(nama_bersih.split())

    # Output ringkasan
    print("\n------------------------------------------")
    print(" HASIL NORMALISASI DATA")
    print("------------------------------------------")
    print(f"Nama bersih : {nama_bersih}")
    print(f"Kode kelas  : {kode_bersih}")
    print(f"Jumlah kata : {jumlah_kata}")
    print(f"Inisial     : {inisial}")
    print("------------------------------------------")


if __name__ == "__main__":
    main()
