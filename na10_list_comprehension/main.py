"""
    List comprehension adalah metode ringkas dalam pembuatan list (selain menggunakan literal) [] atau menggunakan list(). Cara ini lebih banyak diterapkan untuk operasi list yang menghasilkan struktur baru.
"""

# Contoh 1
seq = []
for i in range(5):
    seq.append(i * 2)

print("Contoh 1:", seq)

# contoh di atas bisa dituliskan menggunakan list comprehension, menjadi seperti berikut:
seq = [i * 2 for i in range(5)]
print("Contoh 1, menggunakan list comprehension:", seq)

seq = [i * 3 for i in range(100)]
print("Contoh 1, menggunakan list comprehension:", seq)

# Contoh 2
seq = []
for i in range(10):
    if i % 2 == 1:
        seq.append(i)

print("Contoh 2:", seq)

# menggunakan list comprehension
seq = [i for i in range(10) if i % 2 == 1]
print("Contoh 2, menggunakan list comprehension:", seq)

seq = [i for i in range(100) if i % 3 == 0]
print("Contoh 2, menggunakan list comprehension:", seq)

# Contoh 3
seq = []
for i in range(1, 10):
    seq.append(i * (2 if i % 2 == 0 else 3))

print("Contoh 3, di dalam append bisa menggunakan ternary:", seq)

# cara di atas bisa menggunakan list comprehension
seq = [(i * (2 if i % 2 == 0 else 3)) for i in range(1, 10)]
print("Contoh 3, menggunakan list comprehension:", seq)

# Contoh 4:
list_x = ['a', 'b', 'c']
list_y = ['1', '2', '3']

seq = []
for x in list_x:
    for y in list_y:
        seq.append(x + y)

print("Contoh 4:", seq)

# bisa dituliskan seperti ini:
seq = [x + y for x in list_x for y in list_y]
print("Contoh 4, menggunakan list comprehension:", seq)

# Contoh 5
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

for row in matrix:
    print(row)

transposed = []
for i in range(4):
    tr = []
    for row in matrix:
        tr.append(row[i])
    print(tr)

print("Contoh 5:", transposed)