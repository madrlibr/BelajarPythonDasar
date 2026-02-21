"""
Disini kita akan membahas data struktur yang umum digunakan:
1. list
2. Tuple
3. Dictionary

List:
list adalah tipe data berurutan yang isinya dapat dirubah atau mutable
bentuknya: [10, 32, 23, 11, 64, 46]

Tuple:
Simpelnya, Tuple adalah list namun datanya bersifat tetap tidak bisa dirubah atau immutable
bentuknya: (21, 32, 11, 43, 5, 32)

Dictionary:
Dictionary adalah data dengan pasangan key:value contohnya
{
    "nama": "Joe cow i"
    "umur": 89
}
"""


#============LIST===============#
minuman = ["Cola coca", "Pepsay", "Es cekek"]
print(minuman)
print(len(minuman)) #Mengambil banyak/panjang data

#menambah data baru
minuman.append("Sirup marjuwan")
print(minuman)

#menghapus data berdasarkan nilai/isinya
minuman.remove("Cola coca")
print(minuman)

#menghapus data terakhir
minuman.pop()
print(minuman)

#Indexing
print("Minuman indeks ke 0: ", minuman[0])

#Mengubah data dengan indeks
minuman[0] = "Jus albino" #Mengubah data ke 0 menjadi "Jus albino"
print(minuman)
#==========================


#===========TUPLE===========#
koleksiPassword = (21232232, 32434234, 2414112, 14124)
koleksiKode = (323232, "AEZAKMI32", True, True, 323, False) #tuple juga bisa bertipe gabungan
print(koleksiPassword)
print(koleksiKode)

print(len(koleksiPassword))

#Tuple juga bisa indexing
print(f"Indeks ke-1 dari koleksiPassword: {koleksiPassword[0]}")


#===========DICTIONARY============#

akun_1 = {
    "username": "Walter_putih",
    "umur": 50,
    "menikah": True,
    "sandi": "breaking good"
    #key: value
}

#Dictionary tidak mendukung indexing tapi sebagai gantinya Dictionary memakai key, dalam contoh diatas Username, umur, dan menikah adakah key-nya
print(akun_1)
print(40 * "=")
print(f"Username akun ke-1 adalah: {akun_1["username"]}")

#Mengubah value/nilai umur
akun_1["umur"] = 51
print(akun_1)

print(40 * "=")
print(f"Kunci akun_1: {akun_1.keys()}")
print(f"Nilai akun_1: {akun_1.values()}")
print(f"Pasangan kunci dan nilai akun_1: {akun_1.items()}")
print(40 * "=")
#selain tipe data dasar, kita juga bisa menjadikan list dan Dictionary lain sebagai value dari sebuah Dictionary
 
akun_2 = {
    "username": "Lilhab",
    "umur": 100,
    "menikah": True,
    "sandi": "admin123"
}

database = {
    "akun_1": akun_1,
    "akun_2": akun_2
}
print(f"akun ke-2 di database: {database["akun_2"]}")




MMMM
