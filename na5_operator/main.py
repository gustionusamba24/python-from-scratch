num = -90
print(num)

sum = 0
list_of_numbers = [10, 20, 30, 40, 50]
for num in list_of_numbers:
    sum += num
print(sum)

print(f"10 / 3 = {10 / 3}")
print(f"10 // 3 = {10 // 3}") # operasi pembagian dibulatkan ke bawah
print(f"9 // 2 = {9 // 2}")
print(f"9 / 2 = {9 / 2}")

print(f"7 % 4 = {7 % 4}")
print(f"4 % 7 = {4 % 7}")
print(f"5 % 7 = {5 % 7}")
print(f"6 % 7 = {6 % 7}")

print(f"6 % 10 = {6 % 10}")
print(f"5 % 10 = {5 % 10}")
print(f"4 % 10 = {4 % 10}")

""" 
is operator in python
"""
num_1 = 4003
num_2 = 4003
res = num_1 is num_2
print("num1 is num2:", res)
print("id(num_1): %s, id(num_2): %s" % (id(num_1), id(num_2)))

"""
Pengecekan nilai kosong (atau None) dianjurkan untuk selalu dilakukan menggunakan operator is dan menghindari penggunaan operator ==

Hal ini karena operator is membandingkan identitas data dan identitas data None selalu valid. Sedangkan operator == perbandingannya dilakukan dengan via special method __eq__() yang default method tersebut bisa di-override isinya.
"""

"""
Operator in digunakan untuk mengecek apakah suatu nilai merupakan bagian dari data kolektif atau tidak.

Operator ini bisa digunakan pada semua tipe data kolektif seperti dictionary, set, tuple, dan list. Selain itu, operator in bisa digunakan pada string untuk pengecekan substring
"""
sample_list = [2, 3, 4]
is_3_exist = 3 in sample_list
print(f"is 3 exist: {is_3_exist}")

sample_tuple = ("hello", "python")
is_hello_exist = "hello" in sample_tuple
print(f"is hello exist {is_hello_exist}")

sample_dict = {"nama": "agung", "age": 49}
is_key_nama_exist = "nama" in sample_dict
print(f"is_key_nama_exist {is_key_nama_exist}")

sample_set = {"benjang", "preiiiii"}
is_prei = "prei" in sample_set
print(f"is_prei {is_prei}")

text = "Hujan Kerang Ajaib"
is_Kerang_exist = "Kerang" in text
print(f"is_Kerang_exist {is_key_nama_exist}")