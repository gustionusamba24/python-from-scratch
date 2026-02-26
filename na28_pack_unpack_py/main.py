"""
    Upacking adalah teknik pendistribusian elemen type data kolektif ke banyak variabel
"""
names = (
    'Mikasa Ackerman',
    'Armin Arlert',
    'Eren Yeager',
    'Zeke Yeager',
    'Reiner Braun',
    'Annie Leonhart'
)

soldier1, soldier2, soldier3, warrior1, warrior2, warrior3 = names
print(soldier1)  # output ➜ Mikasa Ackerman
print(soldier2)  # output ➜ Armin Arlert
print(soldier3)  # output ➜ Eren Yeager
print(warrior1)  # output ➜ Zeke Yeager
print(warrior2)  # output ➜ Reiner Braun
print(warrior3)  # output ➜ Annie Leonhart

print("\nUnpack hanya N elements pertama:\n")

"""
    Contoh penerapannya bisa dilihat di kode berikut. Tuple yang sama, 3 element pertamanya saja yang ditampung ke variabel baru. Untuk element sisanya, tetap harus ditampung juga tapi cukup di 1 variabel saja, tersimpan dalam tiple data list.
"""
names = (
    'Mikasa Ackerman',
    'Armin Arlert',
    'Eren Yeager',
    'Zeke Yeager',
    'Reiner Braun',
    'Annie Leonhart'
)

soldier1, soldier2, deceiver1, *warriors = names

print(soldier1)  # output ➜ Mikasa Ackerman
print(soldier2)  # output ➜ Armin Arlert
print(deceiver1)  # output ➜ Eren Yeager
print(warriors)  # output ➜ ['Zeke Yeager', 'Reiner Braun', 'Annie Leonhart']

"""
    Bisa dilihat dari output, bahwa 3 element pertama berhasil ditampung di 3 variabel baru. Sisanya tetap disimpan ke variabel lain yang pada contoh di atas adalah variabel warriors.

    Penulisan variabel penampung sisa element diawali dengan karakter * dan pasti tipe datanya adalah list.
"""

"""
    Katakanlah data element yang dibutuhkan hanya 3 pertama, sisanya bisa dibuang, maka bisa gunakan variabel _ sebagai tempat pembuangan element yang tidak terpakai.
"""
soldier1, soldier2, deceiver1, *_ = names

print(soldier1)  # output ➜ Mikasa Ackerman
print(soldier2)  # output ➜ Armin Arlert
print(deceiver1)  # output ➜ Eren Yeager

print("\nUnpack hanya N elements terakhir:\n")
names = [
    'Mikasa Ackerman',
    'Armin Arlert',
    'Eren Yeager',
    'Zeke Yeager',
    'Reiner Braun',
    'Annie Leonhart'
]

*soldiers, deceiver1, deceiver2, warrior1, warrior2 = names

print(soldiers)  # output ➜ ['Mikasa Ackerman', 'Armin Arlert']
print(deceiver1)  # output ➜ Eren Yeager
print(deceiver2)  # output ➜ Zeke Yeager
print(warrior1)  # output ➜ Reiner Braun
print(warrior2)  # output ➜ Annie Leonhart

"""
    Packing element tuple, list, set
    Packing element adalah operasi pemuatan banyak data ke sebuah data kolektif. Cara penerapannya sangat mudah, cukup tulis saja variabel yang ingin di-pack sebagai element data kolektif. Untuk tipenya bisa berupa tuple, list, maupun set.
"""
soldier1 = 'Mikasa Ackerman'
soldier2 = 'Armin Arlert'
soldier3 = 'Eren Yeager'
warrior1 = 'Zeke Yeager'
warrior2 = 'Reiner Braun'
warrior3 = 'Annie Leonhart'

tuple1 = (soldier1, soldier2, soldier3, warrior1, warrior2, warrior3)
print(tuple1)
# output ↓
#
# ('Mikasa Ackerman',
#  'Armin Arlert',
#  'Eren Yeager',
#  'Zeke Yeager',
#  'Reiner Braun',
#  'Annie Leonhart')

list1 = [soldier1, soldier2, soldier3, warrior1, warrior2, warrior3]
print(list1)
# output ↓
#
# ['Mikasa Ackerman',
#  'Armin Arlert',
#  'Eren Yeager',
#  'Zeke Yeager',
#  'Reiner Braun',
#  'Annie Leonhart']

set1 = {soldier1, soldier2, soldier3, warrior1, warrior2, warrior3}
print(set1)
# output ↓
#
# {'Mikasa Ackerman',
#  'Eren Yeager',
#  'Reiner Braun',
#  'Armin Arlert',
#  'Annie Leonhart',
#  'Zeke Yeager'}

print("\nPrepend element:\n")

"""
    Operasi prepend bisa dilakukan dengan mudah menggunakan syntax (newElement, *oldData). Contohnya pada kode berikut, tuple names ditambahi element baru dengan posisi di awal.
"""
names = [
    'Mikasa Ackerman',
    'Armin Arlert',
    'Eren Yeager',
    'Zeke Yeager',
    'Reiner Braun',
    'Annie Leonhart'
]

names = ('Jean Kirstein', *names)
print(names)
# output ↓
#
# ('Jean Kirstein',
#  'Mikasa Ackerman',
#  'Armin Arlert',
#  'Eren Yeager',
#  'Zeke Yeager',
#  'Reiner Braun',
#  'Annie Leonhart')

names = ('Jean Kirstein', *names)
print(f"type: {type(names).__name__}")
# output ➜ type: tuple

names2 = ['Jean Kirstein', *names]
print(f"type: {type(names2).__name__}")
# output ➜ type: list

names3 = {'Jean Kirstein', *names}
print(f"type: {type(names3).__name__}")
# output ➜ type: set

print("\nUnpack hanya N elements pertama:\n")
"""
    Di atas telah dicontohkan kalau tanda * bisa digunakan untuk menampung sisa pendistribusian keys dictionary (ingat, hanya keys-nya saja!), maka berarti tidak bisa digunakan untuk operasi append dan prepend dictionary.

    Cara append/prepend dictionary adalah dengan memanfaatkan tanda **. Contoh penerapannya bisa dilihat pada kode berikut:
"""
data = {
    'name': 'Mikasa Ackerman',
}
print(data)
# output ➜ { 'name': 'Mikasa Ackerman' }

data = {
    **data,
    'occupation': 'Paradise Survey Corps',
}
print(data)
# output ➜ { 'name': 'Mikasa Ackerman', 'occupation': 'Paradise Survey Corps' }

data = {
    'id': 'U0001',
    **data,
    'gender': 'female',
}

print(data)
# output ↓
#
# {
#   'id': 'U0001',
#   'name': 'Mikasa Ackerman',
#   'occupation': 'Paradise Survey Corps',
#   'gender': 'female'
# }

def show_biography(id, name, occupation, gender):
    print(f"id: {id}")
    print(f"name: {name}")
    print(f"occupation: {occupation}")
    print(f"gender: {gender}")

data1 = {
    'id': 'U0001',
    'gender': 'female',
    'name': 'Mikasa Ackerman',
    'occupation': 'Paradise Survey Corps',
}

show_biography(**data1)
# output ↓
#
# id: U0001
# name: Mikasa Ackerman
# occupation: Paradise Survey Corps
# gender: female

data2 = {
    'gender': 'female',
    'name': 'Mikasa Ackerman',
    'occupation': 'Paradise Survey Corps',
}
show_biography('U0002', **data2)
# output ↓
#
# id: U0002
# name: Mikasa Ackerman
# occupation: Paradise Survey Corps
# gender: female