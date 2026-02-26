"""
    Pada chapter ini kita akan belajar tentang beberapa hal yang berhubungan dengan object/data dan reference, diantaranya:
    - Apa itu identifier data (object ID)
    - Bagaimana python mengelola data
    - Apa yang terjadi sewaktu data di-assign ke variabel lain
    - Dan juga peran ID dalam data reference dan operasi slicing
"""
import sys

"""
    Object ID
    Di python, semua object atau data memiliki identifier, yaitu angka unik yang merepresentasikan data tersebut. Sebagai contoh, pada kode berikut nilai numerik 24 tersimpan pada variable number, ID nya adalah 140728206353928.
"""
number_1 = 24
number_2 = 24

print("data:", number_1)
print("data:", number_2)

identifier_1 = id(number_1)
identifier_2 = id(number_2)
print("identifier:", identifier_1)
print("identifier:", identifier_2)

"""
    Reference / alamat memori data
    Reference pada konteks programming artinya adalah referensi suatu data ke alamat memori
    Contoh: variabel message1 berisi string `hello world`. String tersebut kemudian di-assign ke message2. Selain itu ada juga variabel message3 berisi string yang sama persis tapi dari deklarasi literal berbeda.
"""

message1 = "hello world"
message2 = message1
message3 = "hello world"

print(f"var: message1, id: {message1}, data: {id(message1)}")
print(f"var: message2, id: {message2}, data: {id(message2)}")
print(f"var: message3, id: {message3}, data: {id(message3)}")

print(f"message1 ({id(message1)}) is message2 ({id(message2)}) ➡️ {message1 is message2}")
# output ➜ message1 (2131034204400) is message2 (2131034204400) ➡️ True

print(f"message1 ({id(message1)}) is message3 ({id(message3)}) ➡️ {message1 is message3}")
# output ➜ message1 (2131034204400) is message3 (2131034205616) ➡️ False

print(f"message2 ({id(message2)}) is message3 ({id(message3)}) ➡️ {message2 is message3}")
# output ➜ message2 (2131034204400) is message3 (2131034205616) ➡️ False

message1 = "hello world"
message2 = message1
message3 = "hello world"

print(f"message1 ({id(message1)}) is message2 ({id(message2)}) ➜ {message1 is message2}")
print(f"message1 ({id(message1)}) is message3 ({id(message3)}) ➜ {message1 is message3}")
print(f"message2 ({id(message2)}) is message3 ({id(message3)}) ➜ {message2 is message3}")

message2 = "hello world"

print(f"message1 ({id(message1)}) is message2 ({id(message2)}) ➜ {message1 is message2}")
print(f"message1 ({id(message1)}) is message3 ({id(message3)}) ➜ {message1 is message3}")
print(f"message2 ({id(message2)}) is message3 ({id(message3)}) ➜ {message2 is message3}")

message3 = message2

print(f"message1 ({id(message1)}) is message2 ({id(message2)}) ➜ {message1 is message2}")
print(f"message1 ({id(message1)}) is message3 ({id(message3)}) ➜ {message1 is message3}")
print(f"message2 ({id(message2)}) is message3 ({id(message3)}) ➜ {message2 is message3}")

"""
    Reference data sequence
"""
numbers1 = [1, 2, 3, 4, 5]
print("numbers1", id(numbers1), numbers1)

numbers2 = numbers1
print("numbers1", id(numbers1), numbers1)

print("numbers2", id(numbers2), numbers2)

# Apa yang terjadi jika ada penambahan elemen baru di salah satu variabel
numbers1 = [1, 2, 3, 4, 5]
print("numbers1", numbers1, id(numbers1), sys.getsizeof(numbers1))

numbers2 = numbers1
numbers2.append(9)

# sys.getsizeof() digunakan untuk melihat ukuran data dalam byte
print("numbers1", numbers1, id(numbers1), sys.getsizeof(numbers1))
print("numbers2", numbers2, id(numbers2), sys.getsizeof(numbers2))

angka1 = [5, 5, 5, 5]
print(f"angka1: {angka1}")

# ketika angka2 di-assign ke angka1, maka nilai angka1 akan ikut berubah dikarenakan reference-nya sama
angka2 = angka1
angka2.append(6)

print(f"angka1: {angka1}")
print(f"angka2: {angka2}")

"""
    Reference pada data hasil slicing
    - Ketika suatu data sequence di-assign dari satu variabel ke variabel lain, maka keduanya memiliki reference yang sama.
    - Namun, jika assignment tersebut merupakan hasil operasi slice, maka data hasil slicing merupakan data baru yang tersimpan di alamt memory baru. jadi ID-nya sudah pasti berbeda.
"""
numbers1 = [3, 5, 7, 9]
numbers2 = numbers1
numbers3 = numbers1[:]

print(f"numbers1: {numbers1}, id: {id(numbers1)}")
print(f"numbers2: {numbers2}, id: {id(numbers2)}")
print(f"numbers3: {numbers3}, id: {id(numbers3)}")

numbers2.append(11)
print("after appending:")

print(f"numbers1: {numbers1}, id: {id(numbers1)}")
print(f"numbers2: {numbers2}, id: {id(numbers2)}")
print(f"numbers3: {numbers3}, id: {id(numbers3)}")