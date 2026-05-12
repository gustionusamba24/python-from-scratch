"""
    Dictionary atau dict adalah tipe data kolektif berbentuk key-value. Contoh penulisannya:
"""
import pprint
import json
from traceback import print_tb

profile = {
    "id": 2,
    "name": "john wick",
    "hobbies": ["playing with pencil"],
    "is_female": False
}

print("data:", profile)
print("total keys:", len(profile))

# Untuk memunculkan nilai item tertentu berdasarkan key-nya, bisa dilakukan menggunakan notasi dict["key"]
print("name:", profile["name"])
print("hobbies:", profile["hobbies"])

"""
    Urutan item dictionary
    Mulai dari python 3.7, item dictionary tersimpan secara urut. Artinya urutan item dictionary akan selalu sesuai dengan bagaimana inisialisasi awalnya.
"""

"""
    Pretty print dictionary
    Agar data dictionary yang di-print di console muncul dengan tampilan yang mudah dibaca, dia diantaranya:
    Menggunakan pprint.pprint()
"""
pprint.pprint(profile)

# Menggunakan json.dumps()
print(json.dumps(profile, indent=4))

# Membuat dictionary menggunakan dict() dengan isi list tuple
profile = dict([
    ("set", "id"),
    ("name", "reiner braun"),
    ("hobbies", ["battling with other titans"]),
    ("is_female", False)
])

print("dict with list tuple:", profile)

for key in profile:
    print("key:", key, "\t value:", profile[key])

# Nested dictionary
profile = {
    "id": 2,
    "name": "eren yeager",
    "uniqueness": ("rumbling", "angry", "saving eldian from the suffer"),
    "is_female": False,
    "affiliations": [
        {
            "name": "mikasa ackerman",
            "affiliation": "crush"
        },
        {
            "name": "armin arlert",
            "affiliation": "best friend"
        }
    ]
}

print("name:", profile["name"])
print("hobbies:", profile["uniqueness"])

print("affiliation: ")

for item in profile["affiliations"]:
    print("   -> %s (%s)" % (item["name"], item["affiliation"]))

"""
    Operasi data dictionary
"""
# Pengaksesan item bisa menggunakan dict["key"] atau get()
# Menambah item dict menggunakan update() diikuti bentuk dictionary
# Menghapus item dict menggunakan pop() dengan argumen nama key-nya yang ada

"""
    Pengaksesan dictionary keys
    digunakan untuk mengakses semua keys dictionary, hasilnya adalah tipe data view objects dict_keys.
"""
print(list(profile.keys()))

# akses value
print(list(profile.values()))

# digunakan untuk mengakses semua item dictionary
print(list(profile.items()))