a = 9
b = 5
# OR (|)
c = a | b
print("=====OR=====")
print("nilai : ", a, ' , binary : ', format(a, '08b'))
print("nilai : ", b, ' , binary : ', format(b, '08b'))
print("========== |")
print("nilai : ", c, ' , binary : ', format(c, '08b'))

# AND (&)
c = a & b
print("=====AND=====")
print("nilai : ", a, ' , binary : ', format(a, '08b'))
print("nilai : ", b, ' , binary : ', format(b, '08b'))
print("========== &")
print("nilai : ", c, ' , binary : ', format(c, '08b'))

# XOR (^)
c = a ^ b
print("=====XOR=====")
print("nilai : ", a, ' , binary : ', format(a, '08b'))
print("nilai : ", b, ' , binary : ', format(b, '08b'))
print("========== ^")
print("nilai : ", c, ' , binary : ', format(c, '08b'))

# NOT (~)
c = ~a
print("=====NOT=====")
print("nilai : ", a, ' , binary : ', format(a, '08b'))
print("========== ~")
print("nilai : ", c, ' , binary : ', format(c, '08b'))
print("============= (^)")
d = 0b0000001001
e = 0b1111111111
print('nilai : ', e^d,' , binary : ', format(e^d, '08b'))

# Shifting

# shiht right (>>)
c = a >> 1
print("=====SHIFHT RIGHT=====")
print("nilai : ", a, ' , binary : ', format(a, '08b'))
print("========== >>")
print("nilai : ", c, ' , binary : ', format(c, '08b'))

# shiht left (>>)
c = a << 2
print("=====SHIFHT LEFT=====")
print("nilai : ", a, ' , binary : ', format(a, '08b'))
print("========== >>")
print("nilai : ", c, ' , binary : ', format(c, '08b'))