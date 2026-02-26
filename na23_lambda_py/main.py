"""
    Pengenalan Lambda
    Lambda adalah fungsi yang tidak memiliki nama. Lambda umumnya disimpan ke suatu variabel atau dieksekusi langsung. Lambda bisa memiliki parameter dan mengembalikan nilai balik, seperti fungsi pada umumnya.

    Perbedaan signifikan antara lambda dengan fungsi/closure adalah pada lambda isinya hanya boleh 1 baris statement. Jika ada lebih dari 1 baris silahkan gunakan fungsi saja.
"""


def say_hello1():
    print("hello world")


say_hello1()

say_hello2 = lambda: print("hello python")
say_hello2()

# Lambda return value
get_hello_msg = lambda: "hello python"
res = get_hello_msg()
print("lambda return value:", res)

# Lambda argument/parameter
get_full_name = lambda first, last: f"{first} {last}"
full_name = get_full_name("reiner", "braun")
print(full_name)


def transpose_matrix(m):
    tm = []
    for i in range(len(m[0])):
        tr = []
        for row in m:
            tr.append(row[i])
        tm.append(tr)

    return tm

matrix = [[1, 2], [3, 4], [5, 6]]
res = transpose_matrix(matrix)
print(res)
