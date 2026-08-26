def menu_biodata():
    print("\n=== MENU BIODATA ===")
    nama = input("Nama    : ")
    kelas = input("Kelas   : ")
    sekolah = input("Sekolah : ")

    print("\nBiodata siswa")
    print("Nama    :", nama)
    print("Kelas   :", kelas)
    print("Sekolah :", sekolah)


def menu_kalkulator():
    print("\n=== MENU KALKULATOR ===")
    angka_pertama = float(input("Angka pertama: "))
    operator = input("Operator (+, -, *, /): ")
    angka_kedua = float(input("Angka kedua  : "))

    if operator == "+":
        hasil = angka_pertama + angka_kedua
    elif operator == "-":
        hasil = angka_pertama - angka_kedua
    elif operator == "*":
        hasil = angka_pertama * angka_kedua
    elif operator == "/":
        if angka_kedua == 0:
            print("Tidak dapat membagi dengan nol.")
            return
        hasil = angka_pertama / angka_kedua
    else:
        print("Operator tidak tersedia.")
        return

    print("Hasil:", hasil)


def menu_nilai_siswa():
    print("\n=== MENU NILAI SISWA ===")
    nilai = [80, 75, 90, 85, 70]
    jumlah_nilai = sum(nilai)
    rata_rata = jumlah_nilai / len(nilai)

    print("Seluruh nilai   :", nilai)
    print("Nilai tertinggi :", max(nilai))
    print("Nilai terendah  :", min(nilai))
    print("Jumlah nilai    :", jumlah_nilai)
    print("Rata-rata       :", rata_rata)


def tampilkan_menu():
    print("\n========================")
    print("       MENU UTAMA")
    print("========================")
    print("1. Biodata")
    print("2. Kalkulator")
    print("3. Nilai Siswa")
    print("4. Keluar")
    print("========================")


def program_utama():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            menu_biodata()
        elif pilihan == "2":
            menu_kalkulator()
        elif pilihan == "3":
            menu_nilai_siswa()
        elif pilihan == "4":
            print("Program selesai")
            break
        else:
            print("Pilihan tidak tersedia")


program_utama()
