"""  
Operator perbandingan adalah operator untuk membandingan sebuah nilai dan akan menghasilkan nilai boolean yaitu
True ataupun False
"""

a = 10 == 10 #Ini seperti bertanya "Apakah 10 sama dengan 10" kalau hasilnya True berarti benar bahwa 10 sama dengan 10
b = 10 == 9 #Ini bertanya "Apakah 10 sama dengan 9" dan hasilnya akan False atau tidak benar karena 10 tidak sama dengan 9

c = 10 != 1 #Nah kalau ini seperti bertanya "Apakah 10 tidak sama dengan 1" dan jawabannya True atau benar karena 10 memang tidak sama dengan 9
d = 10 != 10 #kalau ini bertanya "Apakah 10 tidak sama dengan 10" dan jawabannya False atau salah karena 10 itu sama dengan 19
#kalian coba print sendiri dan lihat hasilnya

e = 10 > 4 #ini bertanya "Apakah 10 lebih besar dari 4"
f = 10 < 4 #ini bertanya "Apakah 10 kurang dari 4"

h = 9 >= 9 #ini bertanya "Apakah 9 lebih besar atau sama dengan 9" dan hasilnya akan True meskipun 9 tidak lebih besar dari 9 tapi 9 sama dengan 9
i = 9 <= 9 #Ini bertanya "Apakah 9 kurang dari atau sama dengan 9" jika 9 tidak lebih dari 9 tapi sama dengan 9 maka nilainya True

#Operator ini bisa digunakan untuk variabel dan tidak hanya variabel angka tapi juga string

#Contoj:
angka1 = 10
angka2 = 12

perbandingan = angka1 == angka2
print(f"{angka1} dan {angka2} sama? {perbandingan}")

#Atau
teks1 = "sawit"
teks2 = "monokotil"

perbandinganTeks = teks1 != teks2
print(f"Apakah {teks1} dan {teks2} tidak sama? {perbandinganTeks}")


#Operator perbandingan banyak digunakan untuk looping untuk menyatakan sebuah kondisi yang nanti kita akan dibahas di file lain
