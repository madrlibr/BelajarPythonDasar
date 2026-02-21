"""
Disini kita akan belajar fungsi atau function.
function adalah blok kode yang terstruktur dan dapat digunakan ulang

Jika dianalogikan, function ini mirip dengan rumus didalam mtk
"""

#Contoh function

def sapa(nama): #sapa adalah nama fungsi dan yang didalam kurung yaitu 'nama' disebut parameter
    print(f"Halo selamat datang, {nama}!")

#Cara penggunaan
sapa("Audit") #Memanggil fungsi dan mengisi parameter nama dengan "Audit"
sapa("Aodit")

#Contoh lain
def cariDeterminan(a, b, c, d):
    determinan = (a * d) - (b * c)
    return determinan

"""
return: berfungsi untuk mengembalikan sebuah nilai, dalam kasus ini kita mengembalikan nilai dari variabel determinan
jika tidak memakai return, kode tidak akan error namun fungsi tersebut hanya akan
menjalankan rumus namun tidak memberikan hasilnya
"""

#Kita juga bisa menampungnya kedalam variabel
determinanPertama = cariDeterminan(4, 14, 3, 5) #Untuk parameternya sesuai urutan yang berarti a = 4, b = 14, c = 3, d = 5
print(f"1) Determinan = {determinanPertama}")

#Jika kalian lupa urutan parametrnya, kalian juga bisa menggunakan cara ini
determinanKedua = cariDeterminan(b=3, a=23, c=2, d=22)
#Note: Pilih salah satu cara saja, jika kalian memakai = namun parametrnya sesuai urutan maka akan error contohnya:
#determinanKetiga = cariDeterminan(a=2, b=5, c=1, d=32) Ini akan error karena parameternya sudah sesuai urutan namun malah memakai =
print(f"2) Determinan = {determinanKedua}")

#Fungsi berguna agar kita tidak perlu menulis rumus atau kode secara berulang kali



