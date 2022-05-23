a = input("Nama : ")
b = int(input("NIM : "))
potongan = 10000 
j = 1
bayar = 0

for i in range(0, 3) :
  print("Masukan Harga", j)
  bayar += float(input()) 
  j += 1

total = bayar

if bayar > 50000 :
  bayar -= potongan
else : 
  potongan = 0

print("\nTotal : ", total)
print("Potongan : ", potongan)
print("Bayar : ", bayar)






