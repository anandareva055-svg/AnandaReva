print("================")
print("Andi")
print("================")

nama = input("Masukkan nama siswa: ")

if nama == "Andi":
  target = 70
elif nama == "Budi":
  target = 75   
elif nama == "Citra":
  target = 80
else:
  target = 0


percobaan = 1

while percobaan <= 3:
    nilai = int(input("Masukkan nilai ujian: "))

    if nilai >= target:
        print("Selamat,", nama, "berhasil lulus!")
        break
    else:
        print("Nilai belum mencapai target.")
        percobaan += 1

if percobaan > 3:
    print(nama, "dinyatakan tidak lulus setelah 3 kali percobaan.")

print("================")
print("BUDI")
print("================")

nama = input("Masukkan nama siswa: ")

if nama == "Andi":
  target = 70
elif nama == "Budi":
  target = 75   
elif nama == "Citra":
  target = 80
else:
  target = 0


percobaan = 1

while percobaan <= 3:
    nilai = int(input("Masukkan nilai ujian: "))

    if nilai >= target:
        print("Selamat,", nama, "berhasil lulus!")
        break
    else:
        print("Nilai belum mencapai target.")
        percobaan += 1

if percobaan > 3:
    print(nama, "dinyatakan tidak lulus setelah 3 kali percobaan.")

print("==========")
print("CITRA")
print("==========")

nama = input("Masukkan nama siswa: ")

if nama == "Andi":
  target = 70
elif nama == "Budi":
  target = 75   
elif nama == "Citra":
  target = 80
else:
  target = 0


percobaan = 1

while percobaan <= 3:
    nilai = int(input("Masukkan nilai ujian: "))

    if nilai >= target:
        print("Selamat,", nama, "berhasil lulus!")
        break
    else:
        print("Nilai belum mencapai target.")
        percobaan += 1

if percobaan > 3:
    print(nama, "dinyatakan tidak lulus setelah 3 kali percobaan.")

