# tipe data kolektif yang disimpan secara urut dan bisa diubah nilainya (istilah lainnya adalah tipe data sequence)
# pada bahasa pemrograman lainnya, umumnya disebut array.

# contoh list
list_1 = [10, 70, 20]

# list dengan deklarasi element secara vertikal
list_2 = [
    "ab",
    "cd",
    "ef",
    "gh"
]

# list dengan element berisi bermacam-macam tipe data
list_3 = [3.14, "hello world", True, False]

# list kosong
list_4 = []

# perulangan pada list
for i in list_1:
    print("elem:", i)

# perulangan pada list dilakukan menggunakan index
for i in range(0, len(list_1)):
    print("index ke:", i, "elem:", list_1[i])

# enumerate() digunakan untuk membuat data sequence menjadi data enumerasi, yang jika dimasukkan ke perulangan di setiap iterasinya bisa kita akses index beserta elemennya
for i, v in enumerate(list_1): 
    print("index:", i, "elem:", v)

# nested list
matrix = [
    [0, 1, 0, 1, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 1, 1, 1, 0],
]

for row in matrix:
    for cel in row:
        print(cel, end=" ")
    print()

# Konversi range ke list
range_1 = range(0, 15)
list_1 = list(range_1)
print(f"konversi range ke list: {list_1}")

range_2 = range(0, 25, 3)
list_2 = list(range_2)
print(f"konversi range ke list: {list_2}")

range_3 = range(100, 0, -2)
list_3 = list(range_3)
print(f"konversi range ke list: {list_3}")

# Konversi string ke list
alphabets = list("abcdefghijklmnopqrstuvwxyz")
print(alphabets)

# Konversi tuple ke list
tuple_1 = (1, 2, 3, 4, 5)
numbers = list(tuple_1)
print(numbers)

# Slicing
# slicing adalah metode pengaksesan list menggunakan notasi slice. Notasi ini mirip seperti array, namun mengembalikan data bertipe tetap slice.
list_2 = ["ab", "cd", "ef", "gh"]
print("list_2:", list_2)

slice_1 = list_2[1:3]
print("slice_1:", slice_1)

"""
operasi append atau menambahkan element baru setelah index terakhir, bisa menggunakan 2 cara
"""
# via method append()
list_1 = [34, 67, 90]
print("before:", list_1)

list_1[1] = 99
list_1[2] = 150
print("after:", list_1)


# via slicing
list_1 = [34, 67, 90]
print("before:", list_1)

list_1[len(list_1):] = [12, 20]
print("after:", list_1)


"""
extend/concat/union adalah operasi penggabungan dua data list
"""
# via method extend()
list_1 = [10, 70, 20]
list_2 = [88, 77]
list_1.extend(list_2)
print(list_1)

# via slicing
list_1 = [10, 70, 20]
list_2 = [88, 77]
list_1[len(list_1):] = list_2
print(list_1)

# via operator +
list_1 = [10, 70, 20]
list_2 = [88, 77]
list_3 = list_1 + list_2
print(list_3)

list_3 = [10, 70, 20, 70]

# menyisipkan elemen pada index ke-i menggunakan insert()
list_3.insert(0, 15)
print(list_3)

list_3.insert(2, 25)
print(list_3)


"""
    menghapus element menggunakan method remove()
    Jika element yang ingin dihapus ditemukan ada lebih dari 1, maka yang
    dihapus hanya yang pertama (sesuai urutan index).
"""
list_3 = [10, 70, 20, 70]

list_3.remove(70)
print(list_3)

list_3.remove(70)
print(list_3)

"""
    Menghapus element pada index ke-i
    Method pop() berfungsi untuk menghapus element pada index tertentu. Jika tidak ada index yang ditentukan, maka data element terakhir yang dihapus
"""
list_3 = [10, 70, 20, 70]

x = list_3.pop()
print("after element is deleted using pop without argument:", list_3)

x = list_3.pop(0)
print("after element is deleted using pop with argument 0:", list_3)

"""
    Menghapus element pada range index
    Python memiliki keyword `del` yang berguna untuk menghapus suatu data.
    Dengan menggabungkan keyword ini dan slicing, kita bisa menghapus element dalam range tertentu dengan mudah.
"""
list_3 = [10, 40, 50, 90]

del list_3[1:3]
print("after the elements inside list_3 are deleted:", list_3)

"""
    Untuk mencari index menggunakan nilai element, gunakan method index() milik list. Contoh bisa dilihat berikut, data `cd` ada dalam list pada index 1
"""
list_2 = ["ab", "cd", "ef", "gh"]

idx_1st = list_2.index("cd")
print("idx_1st:", idx_1st)

"""
    Mengosongkan list
"""
# via method clear()
list_1 = [10, 70, 20]
list_1.clear()
print(list_1)


# Menimpanya dengan []
list_1 = [10, 70, 20]
list_1 = []
print(list_1)

# Menggunakan keyword del dan slicing
list_1 = [10, 70, 20]
del list_1[:]
print(list_1)

# Membalik urutan element list
# method reverse() digunakan untuk membalik posisi element pada list
list_1 = [10, 70, 20]
list_1.reverse()
print("after reversed", list_1)

"""
    copy list
    ada 2 cara untuk menduplikasi list, menggunakan method copy() dan teknik slicing
"""
# menggunakan method copy()
list_1 = [9, 17, 66]
list_2 = list_1.copy()
print(list_1)
print(list_2)

# menggunakan operasi assignment dan slicing
list_1 = [9, 17, 66]
list_2 = list_1[:]
print(list_1)
print(list_2)

# mengurutkan data list bisa dilakukan menggunakan default sorter milik Python 
list_1 = [89, 70, 43]
list_1.sort()
print(list_1)

#