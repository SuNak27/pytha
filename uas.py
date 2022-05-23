# Nomor 1 dan 2
jurusan = ["Teknologi Informasi", "Informatika", "Sistem Informasi", "Rekayasa Perangkat Lunak", "Teknik Elektro"]
for i in jurusan:
  print(i)
  
# Nomor 3 dan 4
jurusan = {
  "TI": "Teknologi Informasi",
  "IF": "Informatika",
  "SI": "Sistem Informasi",
  "RPL": "Rekaya Perangkat Lunak",
  "TE": "Teknik Elektro"
}
for j in jurusan:
  print(j, '->', jurusan[j])
  
# Nomor 5
def rataRata(bil1, bil2, bil3) :
  hsl = (bil1 + bil2 + bil3) / 3
  return hsl
hasil = rataRata(1,2,3)
print(hasil)

# Nomor 6
angka = int(input("Masukkan bilangan : "))
for i in range(2, angka, 2) :
  print(i)

# Nomor 7
jumlah = 0
stop = False
while stop == False:
  angka   = input("input angka : ")
  if angka == '0' :
    stop = True
  else :
    angka = int(angka)
    jumlah  += angka
hasil = jumlah
print("Jumlah : ", hasil)