"""
    Python mengenal 3 jenis tipe data numerik yaitu int, float, dan complex
"""
import math

"""
    Bilangan bulat direpresentasikan oleh tipe data int. Cara deklarasi nilai bertipe data ini adalah menggunakan literal integer dimana angka ditulis langsung.
"""
angka1 = 50
angka2 = 71
total = angka1 + angka2
print(f"total penjumlahan: {total}")

angka3 = 19_515_819
print(f"angka 3: {angka3}")

"""
    Hexadecimal, octal, binary
    
    Bilangan bulat bisa dituliskan menggunakan basis lain, misal hexadecimal, octal, dan binary.
    
    - Prefix literal untuk hexadecimal 0x
    - Prefix literal untuk octal 0o
    - Prefix literal untuk binary 0b
"""
angka = 140
angka_hexadecimal = 0x8c
angka_octal = 0o214
angka_binary = 0b10001100

print(f"angka: {angka}")
print(f"angka heksadecimal: {angka_hexadecimal}")
print(f"angka octal: {angka_octal}")
print(f"angka binary: {angka_binary}")

# Memunculkan angka sesuai dengan basisnya
print("\nMemunculkan angka sesuai basisnya")
print(f"angka: {angka:d}")
print(f"angka heksadecimal: {angka_hexadecimal:x}")
print(f"angka octal: {angka_octal:o}")
print(f"angka binary: {angka_binary:b}")

if angka == angka_hexadecimal:
    print("angka decimal sama dengan angka hexadecimal")

"""
    Fungsi int()
    Fungsi int() digunakan untuk mengkonversi data string berisi angka numerik berbasis apapun (selama basisnya 0 hingga 36) ke tipe data integer.
"""
int1 = int("0b10001100", base=2)
print(f"int1: {int1}")

int2 = int("0x8c", base=16)
print(f"int2: {int2}")

"""
    Pembulatan nilai di belakang koma dilakukan menggunakan fungsi round(). Panggil fungsi tersebut, sisipkan data float yang ingin dibulatkan sebagai argumen pertama fungsi dan jumlah digit belakang koma sebagai argumen ke dua
"""
pi = 3.141592653589

n1 = round(pi, 3)
print(f"n1: {n1}")

n2 = round(pi, 5)
print(f"n2: {n2}")

n3 = math.floor(pi)
print(f"n3: {n3}")

n4 = math.ceil(pi)
print(f"n4: {n4}")

# untuk menjumlahkan float, gunakan suffix :f
total = 2.53 + 5.1
print(f"total: {total:f}")

# menampilkan jumlah digit belakang koma
print(f"total: {total:.2f}")

"""
    Notasi float exponential
    menggunakan {f}e{n} atau {f}e+{n}, atau literal ini sama dengan f * (10 ^ n)
"""
float1 = 36e0
print(f"float1: {float1}")

float2 = 36e3
print(f"float2: {float2}")

float3 = 36e+4
print(f"float3: {float3}")

"""
    Bilangan complex adalah bilangan yang isinya merupakan kombinasi bilangan real dan bilangan imajiner, contohnya seperti 120+3j.
    
    Informasi bilangan real pada complex number bisa dimunculkan menggunakan property real sedangkan informasi bilangan imajinernya menggunakan property imag. Contoh:
"""
angka_complex = 120+3j
print(f"angka complex: {angka_complex}")

r = angka_complex.real
print(f"angka real: {r}")

i = angka_complex.imag
print(f"angka imajiner: {i}")

"""
    Fungsi complex() adalah digunakan sebagai alternatif cara membuat bilangan kompleks.
    Sebagai contoh, bilangan 120+3j jika dituliskan menggunakan complex() maka penulisannya seperti berikut:
"""
angka_complex = complex(960, 5)
print(f"angka complex: {angka_complex}")