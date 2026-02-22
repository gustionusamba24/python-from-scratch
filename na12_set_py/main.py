"""
    Set adalah data yang digunakan untuk menampung nilai kolektif unik, jadi tidak ada duplikasi elemen. Elemen yang ada pada set disimpan tidak urut
"""
from traceback import print_tb

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

"""
    Pengecekan difference antar set
    Method difference() digunakan untuk mencari perbedaan elemen antara data (dimana method dipanggil) vs data pada argumen pemanggilan method tersebut.
"""
# mencari elemen di real madrid yang tidak ada di man_utd
real_madrid = {"cristiano ronaldo", "karim benzema", "varane", "casemiro", "luca modric", "carvajal"}
man_utd = {"casemiro", "cristiano ronaldo", "varane", "marcus rashford", "bruno fernandes"}

diff = real_madrid.difference(man_utd)
print("diff:", diff)

"""
    ada juga method difference_update() yang kegunaannya adalah mengubah nilai data (dimana method dipanggil) dengan nilai baru yang didapat dari perbedaan elemen antara data tersebut vs data pada argumen pemanggilan method
"""
real_madrid.difference_update(man_utd)
print("real madrid:", real_madrid)

"""
    Pengecekan intersection antar set
    Method intersection() digunakan untuk mencari elemen yang ada di data (dimana method dipanggil) vs data pada argumen pemanggilan method tersebut.
"""
fellowship = {'aragorn', 'gimli', 'legolas', 'gandalf', 'boromir', 'frodo', 'sam', 'merry', 'pippin'}
hobbits = {'frodo', 'sam', 'merry', 'pippin', 'bilbo', 'agus'}
inter = fellowship.intersection(hobbits)
print(fellowship)

"""
    Pengecekan keanggotaan subset
    Di awal chapter ini kita telah sedikit menyinggung pengecekan membership menggunakan kombinasi keyword if dan in. Selain method tersebut, ada alternatif cara lain yang bisa digunakan untuk mengecek apakah suatu data (yang pada konteks ini adalah set). Caranya menggunakan method issubset()
"""
fellowship = {'aragorn', 'gimli', 'legolas', 'gandalf', 'boromir', 'frodo', 'sam', 'merry', 'pippin'}
hobbits_1 = {'frodo', 'sam', 'merry', 'pippin', 'bilbo'}
res_1 = hobbits_1.issubset(fellowship)
print("res_1:", res_1)

hobbits_2 = {'frodo', 'sam', 'merry', 'pippin'}
res_2 = hobbits_2.issubset(fellowship)
print("res_2:", res_2)

"""
    Pengecekan keanggotaan superset
    Selain issubset(), ada juga issuperset() yang fungsinya kurang lebih sama namun kondisinya pengecekannya dibalik.
"""
fellowship = {'aragorn', 'gimli', 'legolas', 'gandalf', 'boromir', 'frodo', 'sam', 'merry', 'pippin'}
hobbits_1 = {'frodo', 'sam', 'merry', 'pippin', 'bilbo'}

res_1 = fellowship.issuperset(hobbits_1)
print("res_1:", res_1)

""" 
    Pengecekan keanggotaan disjoint
    method ini mengembalikan nilai True jika set pada pemanggilan fungsi berisi elemen yang semuanya bukan anggota data dimana method dipanggil.
"""
fellowship = {'aragorn', 'gimli', 'legolas', 'gandalf', 'boromir', 'frodo', 'sam', 'merry', 'pippin'}

res_1 = fellowship.isdisjoint({"aragorn", "gimli"})
print("res_1:", res_1)

res_2 = fellowship.isdisjoint({'pippin', 'bilbo'})
print("res_2:", res_2)

res_3 = fellowship.isdisjoint({'bilbo'})
print("res_3:", res_3)

"""
    Operator bitwise pada set
    Operasi or pada set menggunakan operator |
    Berisi kombinasi antar 2 elemen
"""
a = set("abracadabra")
b = set("alacazam")

res = a | b
print(res)

# operasi and pada set menggunakan &
# berisi elemen set yang merupakan anggota set a dan set b. Operasi ini biasa disebut dengna operasi and
a = set("abracadabra")
b = set("alacazam")

res = a & b
print(res)

# operasi exclusive or pada set menggunakan operator ^
# berisi elemen set yang ada di set a atau b tetapi tidak ada di keduanya
a = set('abracadabra')
b = set('alacazam')

res = a ^ b
print(res)

# Operator `-` pada set
# Digunakan untuk pencarian perbedaan elemen. Contoh penerapan
a = set('abracadabra')
b = set('alacazam')

res_1 = a - b
res_2 = b - a
print(res_1)
print(res_2)