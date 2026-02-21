"""
Increment: operator untuk menambah nilai dari suatu variabel
decrement: operator untuk mengurangi nilai suatu variabel
"""

#Increment:
nilai = 50
print("Nilai: ", nilai)
nilai += 20 #disini artinya kita menambahkan 20 kedalam variabel nilai tanpa harus menyatakan variabel kembali
print("Nilai setelah Increment: ", nilai)

#Decrement
nilai -= 10
print("Nilai setelah decrement: ", nilai)

#Jika tanpa Increment, untuk menambah atau mengurangi nilai, kalian harus menyatakan variabelnya lagi seperti ini:
angka = 50
angka = angka + 10
#dan jelas ini kurang efisien
