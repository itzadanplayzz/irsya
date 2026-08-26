nama = input("Masukkan nama siswa: ")
nilai = int(input("Masukkan nilai: "))

if nilai >= 90:
    predikat = "A"
    keterangan = "Sangat Baik"
elif nilai >= 80:
    predikat = "B"
    keterangan = "Baik"
elif nilai >= 70:
    predikat = "C"
    keterangan = "Cukup"
elif nilai >= 60:
    predikat = "D"
    keterangan = "Kurang"
else:
    predikat = "E"
    keterangan = "Sangat Kurang"

print("\nNama     :", nama)
print("Nilai    :", nilai)
print("Predikat :", predikat)
print("Keterangan:", keterangan)