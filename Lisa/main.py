print("PILIHAN MENU")
print("===================")
print("1. SEGITIGA ")
print("2. KOTAK ")
print("3. KOTAK BOLONG ")
print("===================")
pil = int(input("MASUKKAN PILIHAN MENU : "))
print("===================")
if pil == 1 :
  baris = int(input("masukkan banyaknya baris : "))
  x = baris
  z = 1
  while z <= baris :
    print("*" * z)
    z += 1
    x -= 1
elif pil == 2 :
  A = int(input("masukkan nilai : "))
  for i in range (A) :
    for j in range (A) :
      print ("*", end=" ")
    print("")
elif pil == 3 :
  print("Masukkan nilai : ", end="")
  a = int(input())
  for i in range (0, a, 1) :
    for j in range (0, a, 1) :
      if i == 0 or i == a-1 or j == 0 or j == a-1 :
        print("* ", end=" ")
      else : 
        print(" ", end="  ")
    print("")
else :
  print("SALAH INPUT")