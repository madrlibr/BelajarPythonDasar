"""
Operator logika yaitu ada and, or, dan not
operator ini berfungsi untuk membandingkan kedua buah pernyataan atau perbandingan
"""


#Contoh operator logika AND
x = 9 == 9 and 13 == 13
print("x: ", x)
"""
Disini ada dua perbandingan yaitu (10 == 10)kiri) dan (13 == 13)kanan)
"and" disini bisa berarti: "kalau kedua perbandingan yaitu perbandingan kiri dan kanan hasilnya True, maka hasilkan nilai True"
kalau salah satu perbandingan kiri ataupun kanan bernilai False, maka operator and akan menghasilkan nilai False, ini 
seperti bertanya "Apakah kedua perbandingan memiliki nilai True" kalau salah satunya saja False
maka hasilkan nilai False
"""

#Contoh operator logika OR
y = 9 != 1 or 11 == 21
print("y: ", y)
""" 
Ini mirip dengan and, hanya saja operator "or" tidak meminta kedua perbandingan untuk agar dia menghasilkan nilai True, tapi
kalau salah satunya saja True, maka operator or akan mau menghasilkan nilai True. Disini variabel y akan bernilai True
karena meskipun 11 == 21 itu bernilai salah/False tapi 9 != 1 itu bernilai benar/True
"""

#Contoh operator logika NOT
z = not 9 == 9
print("z: ", z)
"""
Operator not adalah operator yang akan memutar balikan nilai booleannya, jika perbandingannya bernilai True, maka
dengan operator not, dia akan dirubah sebaliknya menjadi False
kita tau bahwa 9 == 9 bernilai True, dengan not, kita membalik nilainya menjadi False
dan sebaliknya, jika nilanya False maka akan dengan menggunakan not, nilainya menjadi True
"""

#Contoh penggunaanL

usernameLama = "Wirman"
usernameBaru = "Wirman"

passowrdLama = "Halo1212"
passowrdBaru = "Halo1212"

if usernameLama == usernameBaru or passowrdLama == passowrdBaru:
    print("Password atau Username baru tidak boleh sama dengan yang lama!")

statusLogin = False

if not statusLogin:
    print("Anda belum login!")


