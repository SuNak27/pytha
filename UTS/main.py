total = int(input("Total = Rp"))
bayar = int(input("Total Bayar = Rp"))

if bayar < total :
  print("Uang anda kurang")
else :
  kembali = bayar - total
  print("Kembalian = ",kembali)
