# Perulangan 1 FOR
print("=== Perulangan For ===")
jumlah = 0
total = 0
for i in range(0, 3) :
  angka   = float(input("input angka : "))
  total   += angka
  jumlah  += 1
rata2 = total / jumlah
print("Rata rata = ", rata2)
print("\n=== Perulangan While ===")

# Prulangan 1 While
jumlah = 0
total = 0
stop = False
while stop == False:
  angka   = input("input angka : ")
  if angka == '' :
    stop = True
  else :
    angka = float(angka)
    total   += angka
    jumlah  += 1
rata2 = total / jumlah
print("Rata rata = ", rata2)

# Perulangan 2
print("\n === Perulangan 2 (Square) ===")
angka = int(input("Masukkan angka : "))
for i in range (1, angka + 1):
  for j in range (1, angka) :
    print("* ", end='')
  print("*")

print("\n === Perulangan 2 (Triangle) ===")
angka = int(input("Masukkan angka : "))
for i in range (1, angka + 1):
  for j in range (i) :
    print("* ", end='')
  print("")

print("\n === Perulangan 2 (Inverted Triangle) ===")
angka = int(input("Masukkan angka : "))
for i in range (angka, 0, -1):
  for j in range (i) :
    print("* ", end='')
  print("")