"""
disini folder ini kita akan membahas looping
Jadi apa itu looping?

Looping adalah proses dimana kita mengulang sebuah blok kode secara terus menerus, dan akan berhenti
dengan kondisi yang ditentukan, mirip dengan konsep kondisi seperti if-else

konsep if-else:
jika suatu kondisi terjadi/dipenuhi, maka jalankan blok kode dibawah

konsep looping(while loop):
selama suatu kondisi/situasi terpenuhi atau terjadi, maka jalankan blok kode dibawah ini secara terus menerus selama kondisinya terpenuhi/True


Dibawah ini kita akan membahas while loop
"""

#while loop
bangun_tidur = False

while bangun_tidur == False: #bangun_tidur == False adalah kondisinya
    print("Bangun lee")


"""
Ini bisa dibaca "selama bangun_tidur sama dengan False, maka jalankan: print("Bangun lee")
jadi disini baris yang ada didalam while akan dijalankan secara terus menerus selama kondisinya terpenuhi.

jika kode di atas dijalankan, maka program akan mencetak "Bangun lee" selamanya karena variabel bangun_tidur tidak bisa dirubah selama
program berjalan, untuk menghentikan program, kalian bisa pencet ctrl+c untuk menghentikan program secara paksa
"""
