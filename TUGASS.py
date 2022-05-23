from ast import If
# Zakat
a = int(input("Total Kekayaan : "))
b = a * 0.025
print("Zakat : ",b)


# Kasir
daftarmenu = ["a. Kacang : 500", "b. Fanta : 4000", "c. Sprite : 4000", "d. Kopikap : 1000", "e. Bakso : 10.000"]
daftarMenu = []
pilihMenu = []
jumlahMenu = []
pilihLagi = True

print("\n===== Daftar Menu ======")
for menu in daftarmenu:
  print(menu)

def pilih_menu() :
  if input_menu == "a":
    daftarMenu.append("Kacang")
  elif input_menu == "b":
    daftarMenu.append("Fanta")
  elif input_menu == "c":
    daftarMenu.append("Sprite")
  elif input_menu == "d":
    daftarMenu.append("Kopikap")
  elif input_menu == "e":
    daftarMenu.append("Bakso")


def jumlah_menu():
  jumlahMenu.append(jumlah)
  if input_menu == "a":
    pilihMenu.append(500 * jumlah)
  elif input_menu == "b":
    pilihMenu.append(4000 * jumlah)
  elif input_menu == "c":
    pilihMenu.append(4000 * jumlah)
  elif input_menu == "d":
    pilihMenu.append(1000 * jumlah)
  elif input_menu == "e":
    pilihMenu.append(10000 * jumlah)
  else:
    print("Silahkan masukkan a,b,c,d atau e")
  
while pilihLagi:
  input_menu = input("\nPilih menu : ")
  pilih_menu()

  jumlah = int(input("Jumlah: "))
  jumlah_menu()

  lagi = input("Lagi? Y/N : ")

  if lagi == "n":
    pilihLagi = False


print("\n==== Keranjang ====")
for i in range(len(pilihMenu)):
  print(daftarMenu[i], ":", jumlahMenu[i])


total = 0
for j in range(len(pilihMenu)) :
  total += pilihMenu[j]

print("Jumlah : Rp",total)

b = int(input("Jumlah Bayar : Rp "))
while b < total :
  print("uang anda kurang")
  b = int(input("Jumlah Bayar : Rp "))

c = b - total
if b > total :
  print("Kembalian : Rp",c)
  print("Terima Kasih")
elif b == total :
  print("Uang anda Pas. Terima Kasih")
