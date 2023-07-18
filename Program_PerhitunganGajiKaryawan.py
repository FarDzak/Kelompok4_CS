print("## Program Python Menghitung Gaji Karyawan ##")
print("=============================================")
print("")

nama = input("Nama Karyawan: ")
golongan = input("Golongan: ")
jam = int(input("Jumlah jam kerja: ")) 

print("")
print("Nama Karyawan:", nama)
print("Golongan:", golongan)
print("Jumlah jam kerja:", jam)


if golongan == "A":
    upah = 5000
elif golongan == "B":  
    upah = 7000
elif golongan == "C":  
    upah = 8000
elif golongan == "D":  
    upah = 10000
else:
    print("Golongan yang dimasukkan tidak valid.")
    exit()  

if jam > 48:
    uang_lembur = 4000
else:
    uang_lembur = 0

gaji = jam * upah
gaji_lembur = (jam - 48) * uang_lembur
gaji_total = gaji + gaji_lembur

print("{} Menerima upah Rp. {}".format(nama, gaji_total))  
