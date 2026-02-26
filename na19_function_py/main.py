import math


def say_hello():
    print("hello")

say_hello()
say_hello()
say_hello()

def print_something():
    print("hello")

    today = "thursday"
    print(f"happy {today}")

    for i in range(5):
        print(f"i: {i}")

print_something()

def calculate_circle_area(message: str, r: int):
    area = 3.14 * (r ** 2)
    print(message, area)

calculate_circle_area("area of circle", 14)

# Fungsi di python sama halnya dengan fungsi di bahasa pemrograman lain

"""
    Keyword pass secara fungsional umumnya tidak terlalu berguna, kecuali untuk beberapa situasi. Misalnya untuk dipergunakan sebagai isi pada fungsi yang masih belum selesai dikerjakan. Daripada fungsi isinya kosong dan akan menghasilkan error kalau di-run, lebih baik diisi pass. 
    
    Sebagai contoh, penulis berencana membuat fungsi bernama transpose_matrix(), namun fungsi tersebut tidak akan di-coding sekarang karena suatu alasan. Jadi yang penulis lakukan adalah mendeklarasikan fungsi tersebut, kemudian diisi hanya statement pass.
"""

# this method needs to complete sometime later
def transpose_matrix(matrix):
    pass