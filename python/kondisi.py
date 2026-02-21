"""
Disini kita akan membahas "kondisi" atau percabangan yaitu ada if, else, elif.
Sebelum itu apakah kalian tau konsep sebab-akibat? konsep sebab-akibat(kausalitas) adalah konsep yang menjelaskan
hubugan dua peristiwa yaitu sebab dan akibat, dimana sebab menghasilkan sebuah akibat, 
contohnya:
"Aku lapar maka aku makan" disini "lapar" adalah sebab dan "makan" adalah akibat
nah di "kondisi" konsepnya sama seperti di konsep "sebab-akibat".
"""

#Contoh:
umur = 11 #kita punya variabel bernama umur = 11

if umur < 18: #kita pakai operator perbandingan yaitu >
    print("Umur kurang dari 18, tidak bisa masuk!")

"""
Jika kita pakai bahasa manusia untuk membaca baris kode diatas, maka bisa dibaca
"variabel umur adalah 11, jika kurang dari 10 maka cetak("Umur kurang dari 18, tidak bisa masuk!")

nah baris "if umur < 18" bisa dianggap sebagai sebab/penyebab dan baris didalamnnya yaitu print("Umur kurang dari 18, tidak bisa masuk")
adalah akibatnya

lalu bagaimana jika umur lebih dari 10? nah disana kita memakai else, dimana jika blok if atau kondisi if tidak
dipenuhi atau False, maka program akan menjalan blok else.
lalu kondisi else itu apa? kondisi else akan otomatis menjadi kebalikan dari if, jika if < 18 maka else secara otomatis akan menjadi
else > 18 tanpa harus kita menulis bagian > 18
"""

#Contoh:
Nilai = int(input("Masukan Nilai anda: "))
kkm = 74

if Nilai > kkm:
    #blok if
    print("Nilai kamu diatas KKM")
else:
    #blok else
    print("Nilai kamu dibawah KKM")

"""
ELSE IF

Nah kalau "else if" itu satu tingkat dibawah if, jika if bernilai True, else if tidak akan dijalankan tapi
kalau if bernilai False, maka yang dijalankan adalah "else if" bukan else, baru kalau if dan else if false maka else yang akan dijalankan
"""

#Contoh
Nilai = 85

if Nilai >= 90:
    print("Nilai A")
elif Nilai >= 80: 
    print("Nilai B") # Ini akan dijalankan karena 85 >= 80
elif Nilai >= 70:
    print("Nilai C")
else:
    print("Nilai kurang dari 70")
