"""
Disini kita akan membahas for loop.
for loop adalah dimana kita bisa mengontrol seberapa banyak looping yang ingin kita lakukan
"""

#Contoh
for angka in range(1, 10): #Ini artinya "Untuk semua "angka" yang berada di rentang 0 - 9"
    print("angka", angka) #print angka sebanyak 9 10 kali(dari 1 sampai 9)
"""
jadi disini kita membuat variabel bernama "angka" untuk menampung nilai int dari 0 - 9
meskipunkipun kita menulis (0, 10) tapi ketika di print hanya sampai 9 saja karena cara kerja range:
range(angka_awal/dimulai=1, sampai_sebelum_angka=10 ) jadi itu artinya bukan (1 sampai 10) tapi (1 sampai sebelum 10) dan sebelum 10
adalah 9
"""

#tapi kita juga bisa menulis seperti ini
for nomor in range(50): #Ini akan dimulai dari 0 sampai 49
    print("nomor: ", nomor)

#Kita juga bisa pakai variabel
jumlah = 20
for number in range(jumlah):
    print("Jumlah lapangan pekerjaan = ", number, ".000.000")

#Cara lain memakai loop:
kumpulanNomor = [1, 2, 3, 4, 5] #Data bertipe list
for nomor in kumpulanNomor:
    perkalian = nomor * 10
    print("Hasil perkalian: ", perkalian)

#Ini berguna untuk menghitung banyak nilai sekaligus tanpa perlu menghitung satu per sati
