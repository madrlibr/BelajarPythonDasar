"""
Disini kita membahas mengenai cara untuk mengontrol looping
ada dua komponen utama yaitu break dan continue

break: berfungsi untuk menghentikan looping, caranya adalah menyatakan/membuat kondisi yang
       jika dipenuhi akan menghentikan looping, umumnya menggunakan logika if

continue : continue berfungsi untuk melewati suatu iterasi(tergantung kondisinya) dan lanjut ke iterasi selanjutnya 
"""

#Contoh break:
for n in range(1, 21): #Untuk setiap n yang ada di rentang 1-20
    print("N = ", n) #Print variabel n
    if n == 10: #Jika n sama dengan 10 maka
        print("Looping berhenti!")
        break #Hentikan looping


#Contoh continue
for i in range(1, 101):
    if i % 2 != 0: #Jika i % 2 tidak sama dengan 0 maka:
        continue #lewati iterasi
    else: #jika sebaliknya
        print(i) #print variabel i


