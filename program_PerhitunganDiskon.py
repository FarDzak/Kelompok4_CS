print("## Program Python Diskon Potongan Harga ##")
print("==========================================")
print("")

totalBelanja = float(input("Total belanja anda: Rp."))

if totalBelanja < 100000:
    print("Maaf, anda tidak mendapatkan diskon")
    print("Total bayar: Rp.",totalBelanja)

elif 100000 < totalBelanja < 500000:
    print("Selamat, anda mendapat diskon 10%")
    diskon = totalBelanja * 10/100
    totalBayar = totalBelanja - diskon
    print("Total bayar: Rp.", totalBayar)

elif 500000 < totalBelanja < 1000000:
    print("Selamat, anda mendapat diskon 20%")
    diskon = totalBelanja * 20/100
    totalBayar = totalBelanja - diskon
    print("Total bayar: Rp.", totalBayar)

elif totalBelanja > 1000000:
    print("Selamat, anda mendapat diskon 30%")
    diskon = totalBelanja * 30/100
    totalBayar = totalBelanja - diskon
    print("Total bayar: Rp.", totalBayar)
