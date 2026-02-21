"""
Disini kita akan membahas tipe data dasar terlebih dahulu. Di python ada 3 tipe data dasar yaitu
numerik(angka), string(teks), dan boolean(True atau False/0 atau 1)

Tipe numerik terdiri dari:
int = angka bulat seperti 9, 11, 2008
float = angka desimal seperti 20.26, 1.0, 32.3343

untuk string berupa data teks seperti yang sudah dibahas seperti "Hidup JOKOWIIII"
"""

a = "Monokotil" #Ini string
n = 2024 #Ini int/integer
i = 11.100 #ini float
e = True #ini boolean
s = False #ini juga boolean
#Untuk boolean harus diawali dengan kapital, jika seperti dibawah ini
s = true #ini akan error karena true dianggap sebagai nama variabel
n = false #ini juga akan error karena false juga dianggap sebagai nama variabel

#Cara mengcek tipe dataL
tipe_data_a = type(a)
print(f"Tipe data a: {tipe_data_a}")
#Atau juga bisa langsung tanpa membuat variabel
print(type(n))
