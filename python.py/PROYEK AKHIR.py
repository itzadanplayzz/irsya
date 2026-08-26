data_siswa = []


def tentukan_predikat(nilai):
    if nilai >= 90:
        return "A - Sangat Baik"
    elif nilai >= 80:
        return "B - Baik"
    elif nilai >= 70:
        return "C - Cukup"
    elif nilai >= 60:
        return "D - Kurang"
    else:
        return "E - Sangat Kurang"


def tambah_data():
    print("\n=== TAMBAH DATA SISWA ===")
    nama = input("Nama siswa : ")
    nilai = float(input("Nilai       : "))

    siswa = {
        "nama": nama,
        "nilai": nilai,
    }
    data_siswa.append(siswa)
    print("Data siswa berhasil ditambahkan.")


def tampilkan_data():
    print("\n=== DATA SISWA ===")
    if not data_siswa:
        print("Belum ada data siswa.")
        return

    for nomor, siswa in enumerate(data_siswa, start=1):
        print(f"{nomor}. Nama: {siswa['nama']}")
        print(f"   Nilai: {siswa['nilai']:g}")
        print(f"   Predikat: {tentukan_predikat(siswa['nilai'])}")


def tampilkan_rata_rata():
    if not data_siswa:
        print("\nBelum ada data siswa.")
        return

    total_nilai = sum(siswa["nilai"] for siswa in data_siswa)
    rata_rata = total_nilai / len(data_siswa)
    print(f"\nRata-rata nilai: {rata_rata:g}")


def tampilkan_nilai_tertinggi():
    if not data_siswa:
        print("\nBelum ada data siswa.")
        return

    siswa_tertinggi = max(data_siswa, key=lambda siswa: siswa["nilai"])
    print(f"\nNilai tertinggi: {siswa_tertinggi['nilai']:g}")
    print(f"Nama siswa    : {siswa_tertinggi['nama']}")


def tampilkan_nilai_terendah():
    if not data_siswa:
        print("\nBelum ada data siswa.")
        return

    siswa_terendah = min(data_siswa, key=lambda siswa: siswa["nilai"])
    print(f"\nNilai terendah: {siswa_terendah['nilai']:g}")
    print(f"Nama siswa   : {siswa_terendah['nama']}")


def tampilkan_menu():
    print("\n=================================")
    print("       APLIKASI NILAI SISWA")
    print("=================================")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Rata-rata Nilai")
    print("4. Nilai Tertinggi")
    print("5. Nilai Terendah")
    print("6. Keluar")
    print("=================================")


def program_utama():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            tampilkan_data()
        elif pilihan == "3":
            tampilkan_rata_rata()
        elif pilihan == "4":
            tampilkan_nilai_tertinggi()
        elif pilihan == "5":
            tampilkan_nilai_terendah()
        elif pilihan == "6":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak tersedia.")


program_utama()
