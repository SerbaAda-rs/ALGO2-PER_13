import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print("====== Program Mini Project ======")
print("====== Rahmadi_552012105009 ======")

# Fungsi membaca file
def baca_file(nama_file):
    data = {}

    try:
        with open(nama_file, "r") as file:
            for baris in file:
                nim, nilai = baris.strip().split(",")
                data[nim] = float(nilai)

    except FileNotFoundError:
        print("File belum tersedia, membuat data baru.")

    return data


# Fungsi simpan data ke file
def simpan_file(nama_file, data):
    with open(nama_file, "w") as file:
        for nim, nilai in data.items():
            file.write(f"{nim},{nilai}\n")


# Fungsi sorting data (Insertion Sort)
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


# Fungsi searching
def cari_data(data):
    nim = input("Masukkan NIM yang dicari: ")

    if nim in data:
        print("Nilai:", data[nim])
    else:
        print("Data tidak ditemukan.")



# Fungsi hapus data
def hapus_data(data):
    nim = input("Masukkan NIM yang akan dihapus: ")

    if nim in data:
        del data[nim]
        print("Data berhasil dihapus.")
    else:
        print("Data tidak ditemukan.")


# Kompleksitas rata-rata O(1) untuk pencarian dictionary


# Fungsi menu
def tampilkan_menu():
    print("\n==== MINI PROJECT NILAI MAHASISWA ====")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Simpan & Keluar")
    


# Fungsi tambah data
def tambah_data(data):
    nim = input("Masukkan NIM: ")

    try:
        nilai = float(input("Masukkan nilai: "))
        data[nim] = nilai

    except ValueError:
        print("Nilai harus berupa angka.")


# Fungsi tampilkan data
def tampilkan_data(data):
    if not data:
        print("Belum ada data.")
    else:
        print("\nDaftar Nilai Mahasiswa")
        for nim, nilai in data.items():
            print(f"NIM: {nim} | Nilai: {nilai}")


# Program utama
def main():
    nama_file = "data.txt"
    data = baca_file(nama_file)

    while True:
        tampilkan_menu()
        pilih = input("Pilih Menu: ")

        if pilih == "1":
            tambah_data(data)

        elif pilih == "2":
            tampilkan_data(data)

        elif pilih == "3":
           hapus_data(data)

        elif pilih == "4":
            simpan_file(nama_file, data)
            print(f"Data Berhasil disimpan ke {nama_file}, Program Selesai")
            break

        else:
            print("Pilihan tidak valid.")


main()

# =====================================================
# RINGKASAN ANALISIS KOMPLEKSITAS SISTEM
# Fitur                Kompleksitas
# Tambah Data          O(1)
# Tampilkan Data       O(n)
# Hapus Data           O(1)
# Simpan File          O(n)
#
# Kompleksitas Dominan : O(n)
# Karena proses menampilkan data dan
# menyimpan file harus membaca seluruh data.
# =====================================================
