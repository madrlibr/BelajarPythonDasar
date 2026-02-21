"""
Jadi di file ini kita akan belajar mengenai variabel
Nah jadi apa itu variabel?
variabel adalah tempat dimana kita menaruh sebuah nilai, 'tempat' disini bukan berarti
tempat beneran ya.

kalau kalian ingat pelajaran matematika yaitu dimana phi=3,14.. atau e=2.71.., nah phi atau e
itulah yang dinamakan variabel dan berisi sebuah nilai, dalam kasus ini phi atau e adalah variabel yang berisi
sebuah angka yaitu 3,14 dan 2.71, nah di pemrograman kita bisa membuat variabel kita sendiri sama seperti di matematika,
namun hanya saja di pemrograman, tipe nilainya itu bukan hanya angka, tapi bisa sangat luas, bisa berupa text, input, list, variabel lain, dll
"""

x = 10 # Nah ini adalah variabel, dimana x adalah 10
#dan disini cara kerjanya juga mirip dengan variabel di matematika dimana variabel bisa dipakai berulang ulang

print(x)
"""
disini ada print juga, print artinya mencetak sesuatu ke terminal, dan disini kita mau mencetak x
Jika kalian sudah bisa tahu hasilnya bagaimana sebelum kodenya di run/dijalankan itu artinya kalian sudah paham, tapi kalau tidak pun
tidak papa.
"""

# Untuk cara menjalankan kode, kalian ketik py "nama_file".py di terminal kalian, dan karena ini file ini namanya variabel.py
# maka kalian ketik py variabel.py di terminal, jika tidak bisa, coba ganti py menjadi python dan pastikan direktori kalian benar

"""
Nah ketika di run akan menghasilkan angka 10, kenapa begitu? karena di atas kalian sudah menyatakan bahwa x adalah 10.
"terus kalau gitu huruf x nya jadi diambil dong dan gak ada huruf x?" nah tidak begitu juga, kalian tetap bisa mem-print 
huruf x sebagai teks atau dalam pemrograman biasanya disebut string.
untuk memprint teks, kalian harus mengapitnya dengan tanda kutip
contohnya: print("Halo Dunia"). Kalau tanpa tanda kutip, komputer akan menganggap itu adalah nama variabel.
"""
#Contohnya seperti ini
print("x")
#jadi untuk memprint teks atau biasa disebut string, kalian harus menggunakan tanda " atau juga bisa '

y = "Halo Indonesia" #Ini adalahh variabel bertipe string

#tadi dikatakan bahwa variabel isinya luas tidak hanya angka, nah ini salah satunya yaitu string
#dan cara  kerjanya masih sama dengan yang tadi, kalian tinggal memanggil nama variabelnya, lalu nilainya nanti akan ditampilkan/dicetak
print(y) #mencetak variavel y
#output: Halo Indonesia

"""
Kenapa pakai variabel? variabel cocok untuk tugas repetitif jadi kalian tidak perlu menulis ulang
sebuah nilai, jadi kalian tinggal memanggil variabelnya saja, contoh dibawah ini
"""

halo = "halo selamat datang di"
print(halo, "Indonesia")
print(halo, "ngawi island")

#kalian juga bisa membuat beberapa variabel sekaligus dalam satu baris seperti dibawah ini
nama, umur, kelamin = "Mas amba", 100, "Monyet Ijo banyumas"
print(nama) #Output: Mas amba
print(umur) #Output: 100
print(kelamin) #Output: Monyet Ijo banyuma
