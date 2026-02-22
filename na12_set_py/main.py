"""
    Set adalah data yang digunakan untuk menampung nilai kolektif unik, jadi tidak ada duplikasi elemen. Elemen yang ada pada set disimpan tidak urut
"""

"""
    Pengenalan SetL langsung tulis nilai elemen dengan separator `,` dan diapit menggunakan tanda kurung kurawal `{}`
"""
data_1 = {1, "abc", False, ('gaming', 'coding')}
print("data:", data_1)

print("Panjang data_1:", len(data_1))

data_2 = set()
print("Set Kosong:", data_2)

"""
    Mengakses elemen set: Nilai set by default hanya bisa diakses menggunakan perulangan
"""
titan_shifter = {"Eren Yeager", "Reiner Braun", "Annie Leonhart"}

print("Titan Shifter: ")
for ts in titan_shifter:
    print(ts)

# Eliminasi elemen duplikat
data = {1, 2, 3, 2, 1, 4, 5, 2, 3, 5}
print(data)

data = [1, 2, 3, 2, 1, 4, 5, 2, 3, 5]
print("list data:", data)

data_unique_set = set(data)
print("data unique set:", data_unique_set)

data_unique = list(data_unique_set)
print("data unique in list:", data_unique)

"""
    Operasi pada Set
    Method `add` milik tipe data set digunakan untuk menambahkan element baru. Perlu diingat bahwa data ini didesain untuk mengabaikan urutan elemen, jadi urutan tersimpannya elemen bisa saja acak.
"""
titan = set()

titan.add("attack titan")
print(f"length: {len(titan)}, data: {titan}")

titan.add("armoured titan")
print(f"length: {len(titan)}, data: {titan}")

titan.add("female titan")
print(f"length: {len(titan)}, data: {titan}")

"""
    Menghapus element secara acak.
    Gunakan pop() untuk menghapus satu elemen secara acak atau random
"""
titan.pop()
print(f"length: {len(titan)}, data: {titan}")

titan.pop()
print(f"length: {len(titan)}, data: {titan}")

titan.pop()
print(f"length: {len(titan)}, data: {titan}")

"""
    Menghapus spesifik elemen
    Ada dua method tersedia untuk kebutuhan menghapus elemen tertentu dari sutatu set yaitu discard() dan remove(). Penggunaan keduanya adalah sama, harus disertai dengan 1 argument pemanggilan method yaitu elemen yang ingin dihapus.
    
    Perbedaan antara discard dan remove adalah ketika kita menggunakan discard lalu menuliskan suatu argumen yang tidak ada di set, maka tidak akan memunculkan error, sedangkan remove akan memunculkan error
"""
fellowship = {'aragorn', 'gimli', 'legolas', 'gandalf', 'boromir', 'frodo', 'sam', 'merry', 'pippin'}
print("fellowship:", fellowship)

fellowship.discard("boromir")
print("fellowship:", fellowship)

fellowship.remove("gimli")
print("fellowship:", fellowship)

"""
    Mengosongkan isi set
    method clear() digunakan untuk mengosongkan isi set
"""
fellowship = {'aragorn', 'gimli', 'legolas'}
fellowship.clear()

print(f"len: {len(fellowship)}, data: {fellowship}")

"""
    Copy set
    Method copy() digunakan untuk meng-copy set, menghasilkan data set baru.
"""