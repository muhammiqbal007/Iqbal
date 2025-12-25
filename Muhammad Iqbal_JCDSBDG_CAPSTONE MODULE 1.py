# MUHAMMAD IQBAL JCDS BDG
# CAPSTONE PROJECT MODULE 1
# APLIKASI DISTRIBUSI BANTUAN BANJIR
# =====================================================

from tabulate import tabulate
import sys

# DATA AWAL
# =====================================================
data_bantuan = [
    {"no_kk": "3201010001", "nama_kk": "Andi Saputra", "alamat": "Desa Cinunuk", "jenis_bantuan": "Sembako", "jumlah": 5, "status_distribusi": "Belum"},
    {"no_kk": "3201010002", "nama_kk": "Siti Aminah", "alamat": "Desa Cinunuk", "jenis_bantuan": "Air Bersih", "jumlah": 1, "status_distribusi": "Sudah"},
    {"no_kk": "3201010003", "nama_kk": "Budi Santoso", "alamat": "Desa Cinunuk", "jenis_bantuan": "Selimut", "jumlah": 3, "status_distribusi": "Sudah"},
    {"no_kk": "3201010004", "nama_kk": "Rina Marlina", "alamat": "Desa Cinunuk", "jenis_bantuan": "Sembako", "jumlah": 4, "status_distribusi": "Belum"},
    {"no_kk": "3201010005", "nama_kk": "Ahmad Fauzi", "alamat": "Desa Cinunuk", "jenis_bantuan": "Obat-obatan", "jumlah": 2, "status_distribusi": "Sudah"},
    {"no_kk": "3201010006", "nama_kk": "Dewi Lestari", "alamat": "Desa Cinunuk", "jenis_bantuan": "Pakaian Layak", "jumlah": 6, "status_distribusi": "Belum"},
    {"no_kk": "3201010007", "nama_kk": "Joko Prasetyo", "alamat": "Desa Cinunuk", "jenis_bantuan": "Sembako", "jumlah": 5, "status_distribusi": "Sudah"},
    {"no_kk": "3201010008", "nama_kk": "Nur Aisyah", "alamat": "Desa Cinunuk", "jenis_bantuan": "Air Bersih", "jumlah": 1, "status_distribusi": "Belum"},
    {"no_kk": "3201010009", "nama_kk": "Eko Wijaya", "alamat": "Desa Cinunuk", "jenis_bantuan": "Selimut", "jumlah": 4, "status_distribusi": "Sudah"},
    {"no_kk": "3201010010", "nama_kk": "Lina Kusuma", "alamat": "Desa Cinunuk", "jenis_bantuan": "Sembako", "jumlah": 3, "status_distribusi": "Belum"},
    {"no_kk": "3201010011", "nama_kk": "Suci Yulianti", "alamat": "Desa Cinunuk", "jenis_bantuan": "Sembako", "jumlah": 7, "status_distribusi": "Belum"},
    {"no_kk": "3201010012", "nama_kk": "Astri Widia", "alamat": "Desa Cinunuk", "jenis_bantuan": "Air Bersih", "jumlah": 1, "status_distribusi": "Sudah"},
    {"no_kk": "3201010013", "nama_kk": "Agus Suherman", "alamat": "Desa Cinunuk", "jenis_bantuan": "Selimut", "jumlah": 3, "status_distribusi": "Sudah"},
    {"no_kk": "3201010014", "nama_kk": "Rani Humairah", "alamat": "Desa Cinunuk", "jenis_bantuan": "Sembako", "jumlah": 4, "status_distribusi": "Belum"},
    {"no_kk": "3201010015", "nama_kk": "Kokom Komala", "alamat": "Desa Cinunuk", "jenis_bantuan": "Obat-obatan", "jumlah": 2, "status_distribusi": "Sudah"},
    {"no_kk": "3201010016", "nama_kk": "Asep Sodikin", "alamat": "Desa Cinunuk", "jenis_bantuan": "Pakaian Layak", "jumlah": 6, "status_distribusi": "Sudah"},
    {"no_kk": "3201010017", "nama_kk": "Jajang Kusmana", "alamat": "Desa Cinunuk", "jenis_bantuan": "Sembako", "jumlah": 9, "status_distribusi": "Sudah"},
    {"no_kk": "3201010018", "nama_kk": "Asep Kusnandar", "alamat": "Desa Cinunuk", "jenis_bantuan": "Air Bersih", "jumlah": 1, "status_distribusi": "Sudah"},
    {"no_kk": "3201010019", "nama_kk": "Enjang Sujayanto", "alamat": "Desa Cinunuk", "jenis_bantuan": "Selimut", "jumlah": 2, "status_distribusi": "Sudah"},
    {"no_kk": "3201010020", "nama_kk": "Maman Suryaman", "alamat": "Desa Cinunuk", "jenis_bantuan": "Sembako", "jumlah": 7, "status_distribusi": "Belum"},
]

# VALIDASI
# =====================================================
def validasi_no_kk_format(no_kk):
    return no_kk.isdigit() and len(no_kk) == 10


def validasi_jumlah(jumlah):
    return jumlah.isdigit() and int(jumlah) > 0


# TAMPILAN TABEL
# =====================================================
def tampilkan_tabel(data):
    if not data:
        print("⚠ Data kosong")
        return

    tabel = [[
        d["no_kk"],
        d["nama_kk"],
        d["alamat"],
        d["jenis_bantuan"],
        d["jumlah"],
        d["status_distribusi"]
    ] for d in data]

    header = [
        "NO KK",
        "Nama Kepala Keluarga",
        "Alamat",
        "Jenis Bantuan",
        "Jumlah",
        "Status Distribusi"
    ]

    print(tabulate(tabel, headers=header, tablefmt="fancy_grid"))


# CREATE
# =====================================================
def tambah_bantuan():
    print("\n=== TAMBAH DATA BANTUAN ===")

    no_kk = input("NO KK (10 digit angka): ")

    if not validasi_no_kk_format(no_kk):
        print("❌ NO KK harus berupa ANGKA dan TEPAT 10 digit")
        return

    data_ada = [d for d in data_bantuan if d["no_kk"] == no_kk]

    if data_ada:
        print("\n⚠ NO KK sudah terdaftar. Data berikut sudah ada:")
        tampilkan_tabel(data_ada)

        print("1. Kembali ke Menu")
        print("2. Keluar Program")
        pilihan = input("Pilih (1/2): ")

        if pilihan == "2":
            print("Program selesai 👋")
            sys.exit()
        else:
            return

    nama_kk = input("Nama Kepala Keluarga: ")
    alamat = input("Alamat: ")
    jenis_bantuan = input("Jenis Bantuan: ")

    while True:
        jumlah = input("Jumlah Bantuan: ")
        if validasi_jumlah(jumlah):
            jumlah = int(jumlah)
            break
        print("❌ Jumlah harus berupa angka dan > 0")

    status = input("Status Distribusi (Belum/Sudah): ")

    print("\n--- KONFIRMASI DATA ---")
    tampilkan_tabel([{
        "no_kk": no_kk,
        "nama_kk": nama_kk,
        "alamat": alamat,
        "jenis_bantuan": jenis_bantuan,
        "jumlah": jumlah,
        "status_distribusi": status
    }])

    print("1. Simpan Data")
    print("2. Kembali ke Menu (Batal)")
    pilih = input("Pilih (1/2): ")

    if pilih == "1":
        data_bantuan.append({
            "no_kk": no_kk,
            "nama_kk": nama_kk,
            "alamat": alamat,
            "jenis_bantuan": jenis_bantuan,
            "jumlah": jumlah,
            "status_distribusi": status
        })
        print("✅ Data berhasil disimpan")
    else:
        print("❌ Input dibatalkan")


# READ
# =====================================================
def tampilkan_semua():
    tampilkan_tabel(data_bantuan)


def cari_bantuan():
    no_kk = input("Masukkan NO KK: ")
    hasil = [d for d in data_bantuan if d["no_kk"] == no_kk]
    tampilkan_tabel(hasil)


def filter_status():
    status = input("Status (Belum/Sudah): ").lower()
    hasil = [d for d in data_bantuan if d["status_distribusi"].lower() == status]
    tampilkan_tabel(hasil)


# UPDATE
# =====================================================
def update_bantuan():
    no_kk = input("Masukkan NO KK yang ingin diupdate: ")

    for d in data_bantuan:
        if d["no_kk"] == no_kk:
            d["nama_kk"] = input("Nama Kepala Keluarga baru: ")
            d["alamat"] = input("Alamat baru: ")
            d["jenis_bantuan"] = input("Jenis Bantuan baru: ")

            while True:
                jumlah = input("Jumlah baru: ")
                if validasi_jumlah(jumlah):
                    d["jumlah"] = int(jumlah)
                    break
                print("❌ Jumlah harus angka > 0")

            d["status_distribusi"] = input("Status baru (Belum/Sudah): ")
            print("✅ Data berhasil diupdate")
            return

    print("❌ NO KK tidak ditemukan")


# DELETE
# =====================================================
def hapus_bantuan():
    no_kk = input("Masukkan NO KK yang ingin dihapus: ")

    for d in data_bantuan:
        if d["no_kk"] == no_kk:
            tampilkan_tabel([d])
            if input("Yakin hapus data ini? (Y/N): ").lower() == "y":
                data_bantuan.remove(d)
                print("✅ Data berhasil dihapus")
            else:
                print("❌ Penghapusan dibatalkan")
            return

    print("❌ NO KK tidak ditemukan")


# REKAP
# =====================================================
def rekap_bantuan():
    print("\n=== REKAP DISTRIBUSI BANTUAN ===")
    print(f"Total Data   : {len(data_bantuan)}")
    print(f"Total Jumlah : {sum(d['jumlah'] for d in data_bantuan)}")
    print(f"Sudah        : {sum(1 for d in data_bantuan if d['status_distribusi'].lower() == 'sudah')}")
    print(f"Belum        : {sum(1 for d in data_bantuan if d['status_distribusi'].lower() == 'belum')}")


# MENU UTAMA
# =====================================================
def menu():
    while True:
        print("""
============================
MENU DISTRIBUSI BANTUAN
============================
1. Tambah Data Bantuan
2. Tampilkan Semua Data
3. Cari Data (NO KK)
4. Filter Status
5. Update Data
6. Hapus Data
7. Rekap Bantuan
8. Keluar
""")

        pilih = input("Pilih menu (1-8): ")

        if pilih == "1":
            tambah_bantuan()
        elif pilih == "2":
            tampilkan_semua()
        elif pilih == "3":
            cari_bantuan()
        elif pilih == "4":
            filter_status()
        elif pilih == "5":
            update_bantuan()
        elif pilih == "6":
            hapus_bantuan()
        elif pilih == "7":
            rekap_bantuan()
        elif pilih == "8":
            print("Program selesai 👋")
            break
        else:
            print("❌ Pilihan tidak valid")


# PROGRAM START
# =====================================================
menu()
