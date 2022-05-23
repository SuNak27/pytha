# +++++++3----------------10++++++++++++

inputUser = int(input("Masukkan angka <3 >10 = "))

kurangTiga = (inputUser < 3)

lebihsepuluh = (inputUser > 10)

hasil = (kurangTiga or lebihsepuluh)

print(hasil)


# ------3++++++++++++10------
# Kasus Irisan

msk = int(input("masukkan angka >3 <10 = "))

lebihtiga = (msk >= 3)

kurangsepuluh = (msk <= 10)

hsl = (lebihtiga and kurangsepuluh)
print(hsl)