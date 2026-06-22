import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_screen()

print("====== PROGRAM_MINI_PROJECT_02 ======")
print("======  Rahmadi_552012105009   ======")
# FUNGSI MEMBACA FILE
# Kompleksitas: O(n)
def baca_file(nama_file):
    data = {}

    try:
        with open(nama_file, "r") as file:
            for baris in file:
                nim, nilai = baris.strip().split(",")
                data[nim] = float(nilai)

    except FileNotFoundError:
        print("File belum tersedia.")
        print("Membuat file baru...")

        with open(nama_file, "w") as file:
            pass

    except ValueError:
        print("Format data dalam file tidak valid.")

    return data

# FUNGSI MENYIMPAN FILE
# Kompleksitas: O(n)
def simpan_file(nama_file, data):
    try:
        with open(nama_file, "w") as file:
            for nim, nilai in data.items():
                file.write(f"{nim},{nilai}\n")

        print("Data berhasil disimpan.")

    except Exception as e:
        print("TERJADI KESALAHAN:", e)

# FUNGSI TAMBAH DATA
# Kompleksitas: O(1)
def tambah_data(data):
    nim = input("Masukkan NIM : ")
    #Harus angka 
    if not nim.isdigit():
        print("NIM harus berupa angka!")
        return
    #Harus 12 angka
    if len(nim) != 12:
        print("NIM Harus terdiri dari 12 ANGKA!")
        return
   
    #Tidak boleh duplikat
    if nim in data:
        print("NIM SUDAH TERDAFTAR!")
        return

    try:
        nilai = float(input("Masukkan Nilai : "))

        #Menempatkan data baru ke atas
        data_baru = {nim: nilai}
        data_baru.update(data)
        
        data.clear()
        data.update(data_baru)

        print("Data berhasil ditambahkan.")

    except ValueError:
        print("NILAI HARUS ANGKA.")

# FUNGSI TAMPILKAN DATA
# Kompleksitas: O(n)
def tampilkan_data(data):

    if not data:
        print("Belum ada data.")
        return

    print("\n===== DAFTAR NILAI MAHASISWA =====")

    for nim, nilai in data.items():
        print(f"NIM : {nim} | Nilai : {nilai}")

# FUNGSI SORTING (INSERTION SORT)
# Kompleksitas: O(n²)
def sorting_nilai(data):

    items = list(data.items())

    for i in range(1, len(items)):
        key = items[i]
        j = i - 1

        while j >= 0 and items[j][1] > key[1]:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = key

    return items

# FUNGSI SEARCHING
# Kompleksitas rata-rata: O(1)
def cari_data(data):

    nim = input("Masukkan NIM yang dicari : ")

    if not nim.isdigit():
        print("NIM HARUS ANGKA!")
        return

    if nim in data:
        print(f"Nilai mahasiswa {nim} adalah {data[nim]}")

    else:
        print("DATA TIDAK DITEMUKAN!.")

# FUNGSI HAPUS DATA
# Kompleksitas rata-rata: O(1)
def hapus_data(data):

    if not data:
        print("Belum ada data.")
        return

    print("\n===== DAFTAR DATA =====")

    for nim, nilai in data.items():
        print(f"NIM : {nim} | Nilai : {nilai}")

    nim = input("\nMasukkan NIM yang akan dihapus : ")

    if not nim.isdigit():
        print("NIM harus berupa angka!")
        return

    if nim in data:

        nilai = data[nim]

        print("\n===== DATA YANG AKAN DIHAPUS =====")
        print(f"NIM   : {nim}")
        print(f"Nilai : {nilai}")

        konfirmasi = input(
            "\nYakin ingin menghapus data ini? (Y/T) : "
        ).upper()

        if konfirmasi == "Y":

            del data[nim]

            print("Data berhasil dihapus.")

        else:
            print("Penghapusan dibatalkan.")

    else:
        print("Data tidak ditemukan.")

# FUNGSI STATISTIK DATA
# Kompleksitas: O(n)
def statistik_data(data):

    if not data:
        print("Belum ada data.")
        return

    total_data = len(data)
    rata_rata = sum(data.values()) / total_data
    nilai_tertinggi = max(data.values())
    nilai_terendah = min(data.values())

    print("\n===== STATISTIK DATA =====")
    print("Total Mahasiswa :", total_data)
    print("Rata-rata Nilai :", round(rata_rata, 2))
    print("Nilai Tertinggi :", nilai_tertinggi)
    print("Nilai Terendah  :", nilai_terendah)

# FUNGSI MENU
def tampilkan_menu():

    print("\n===== MINI PROJECT NILAI MAHASISWA =====")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Sorting Nilai")
    print("4. Cari Data")
    print("5. Hapus Data")
    print("6. Statistik Data")
    print("7. Simpan Data")
    print("8. Keluar")

# PROGRAM UTAMA
def main():

    nama_file = "HASIL_PROJECT02.txt"
    data = baca_file(nama_file)

    while True:

        tampilkan_menu()
        pilih = input("Pilih Menu : ")
        
        if pilih not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            print("INPUT HARUS ANGKA DARI 1-8!")
            continue

        if pilih == "1":
            tambah_data(data)
            
        elif pilih == "2":
            tampilkan_data(data)

        elif pilih == "3":
            hasil = sorting_nilai(data)
            print("\n===== DATA TERURUT BERDASARKAN NILAI =====")
            for nim, nilai in hasil:
                print(f"{nim} : {nilai}")

        elif pilih == "4":
            cari_data(data)

        elif pilih == "5":
            hapus_data(data)

        elif pilih == "6":
            statistik_data(data)

        elif pilih == "7":
            simpan_file(nama_file, data)

        elif pilih == "8":
            print("Program selesai, Terima Kasih.")
            break
        else:
            print("Pilihan tidak valid.")
            
main()

# =====================================================
# ANALISIS KOMPLEKSITAS SISTEM
# Tambah Data      : O(1)
# Cari Data        : O(1) rata-rata
# Hapus Data       : O(1) rata-rata
# Tampilkan Data   : O(n)
# Statistik Data   : O(n)
# Simpan File      : O(n)
# Baca File        : O(n)
# Sorting Nilai    : O(n²)
#
# Kompleksitas dominan sistem adalah O(n²)
# karena proses pengurutan menggunakan
# algoritma Insertion Sort.
#
# =====================================================

# Revisi Program:
# 1. Menambahkan validasi menu agar hanya menerima input 1 sampai 8.
# 2. Menambahkan validasi NIM harus berupa angka dan tidak boleh duplikat.
# 3. Mengubah penambahan data sehingga data terbaru tampil di urutan paling atas.
# 4. Menampilkan daftar data sebelum proses penghapusan data dilakukan.
# 5. Menambahkan fitur clear screen dan validasi input untuk meningkatkan kenyamanan pengguna.
