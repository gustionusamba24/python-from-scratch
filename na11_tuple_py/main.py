# Tuple adalah tipe data sequence yang ideal digunakan untuk menampung nilai kolektif yang isinya tidak akan berubah (immutable), berbeda dengan list yang lebih cocok untuk data yang bisa berubah nilai elemennya (mutable)

# Semua fungsi di tuple hampir sama dengan yang ada di list

# Nested Tuple
tuple_nested = ((0, 2), (0, 3), (0, 4), (0, 5))

for row in tuple_nested:
    for cell in row:
        print(cell, end=" ")
    print()

"""
    Tipe data list dan tuple umum dikombinasikan. Keduanya sangat mirip tapi memiliki perbedaan yang jelas, yaitu nilai tuple tidak bisa dimodifikasi sedangkan list bisa.
"""

data = [
    ("ultra instinc shaggy", 1, True, ["detective", "saiyan"]),
    ("nightwing", 3, True, ["teen titans", "bat family"]),
]

# append tuple ke list
data.append(("noob saibot", 10, False, ["brotherhood of shadow"]))

# append tuple ke list
data.append(("tifa lockhart", 2, True, ["avalanche"]))

# print data
print("name \t|\t rank \t|\t win \t|\t affiliation")
print("-------------------------------------------------")
for row in data:
    for cell in row:
        print(cell, end=" | ")
    print()

# Tuple packing dan unpacking
"""
    packing adalah istilah untuk menggabungkan beberapa data menjadi satu data kolektif. Contoh pengaplikasiannya bisa dilihat pada program berikut
"""
first_name = "eren yeager"
rank = 5
win = False

# metode packing (bisa menggunakan `()` atau tanpa `()`)
row_data = (first_name, rank, win)

print(row_data)

# Tuple unpacking
# unpacking adalah istilah untuk menyebar isi suatu data kolektif ke beberapa variabel. Unpacking merupakan kebalikan dari packing
row_data = ("reiner braun", 4, False)
name, rank, win = row_data

print(name, rank, win)

# Tuple bisa saja tidak berisi apapun, contohnya data `()`, yang cukup umum digunakan untuk merepresentasikan data kolektif yang isinya bisa saja kosong.
empty_tuple = ()
print(empty_tuple)

"""
    Berikut adalah contoh penerapannya, dimisalkan ada data kolektif yang didapat dari database berbentuk array object. Data tersebut perlu disimpan oleh variabel list yang element-nya adalah tuple dengan spesifikasi.
"""
