for i in range(5):
    print("index:", i)

r = range(5)
print("r:", list(r))

r_with_3_step = range(1, 12, 3)
print("r with 3 step:", list(r_with_3_step))

for i in range(5, -5, -1):
    print("index:", i)

# Iterasi data list
messages = ["morning", "afternoon", "evening"]
for m in messages:
    print(m)

# Iterasi data tuple
numbers = ("twenty four", 24)
for n in numbers:
    print(n)

# Iterasi data string
for char in "hello python":
    print(char)

# Iterasi data dictionary
bio = {
    "name": "balmond alfriansyah",
    "role": "software engineer"
}

for key in bio:
    print("key:", key, "value:", bio[key])

# Iterasi data set
numbers = {"twenty four", 24}
for n in numbers:
    print(n)

# perulangan bercabang
max = int(input("masukkan jumlah bintang: "))

for i in range(max):
    for j in range(0, max - i):
        print("*", end=" ")
    print()

print()

for i in range(max):
    for j in range(i + 1):
        print(f"{j + 1}", end=" ")
    print()

print()

initial_number = 2
for i in range(max):
    for s in range(max - i - 1):
        print("", end=" ")
    for j in range(i + 1):
        print(initial_number, end=" ")
        initial_number += 2
    print()