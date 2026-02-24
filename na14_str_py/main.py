"""
    String atau str adalah kumpulan data char atau karakter yang tersimpan secara urut. String di python mengadopsi standar Unicode degan default encoding adalah UTF-8
"""
text = "hello python"
print(text)

text = 'hello python'
print(text)

name = "Eren Yeager"
titan_shifter = "Attack Titan"

print(f"My name is {name}, I am {titan_shifter}".format(name=name, titan_shifter=titan_shifter))

# menggabungkan 2 string menggunakan method join()
text = " ".join(["Annie Leonhart"])
print(text)

# split string
text = "today, I learn python. I use python for several project that will be I am focusing on"
res = text.split(" ")
print(res)

nama_saya = "Gustio Nusamba"
for ch in nama_saya:
    print(ch)

print(nama_saya[2:7])

# mengecek karakter alfabet dan angka
# jika ada spasi maka dianggap false juga
print(nama_saya.isalpha())

print("jujur987".isdigit())
print("777777".isdigit())

print('4²'.isnumeric())
print('2⅓'.isnumeric())

"""
    isalpha() -> digunakan untuk mengecek apakah string berisi karakter alfabet atau tidak. Nilai kembaliannya True jika semua karakter dalam string adalah alfabet.
    
    isdigit() -> digunakan untuk mengecek apakah string berisi karakter digit atau tidak. Nilai kembaliannya True jika semua karakter dalam string adalah angka numerik (termasuk pangkat).
    
    isdecimal() -> digunakan untuk mengecek apakah string berisi karakter desimal atau tidak. Nilai kembaliannya True jika semua karakter dalam string adalah angka numerik desimal.
    
    isnumeric() -> digunakan untuk mengecek apakah string berisi karakter desimal atau tidak. Nilai kembaliannya True jika semua karakter dalam string adalah angka numerik (termasuk pecahan, pangkat, dan angka numerik lainnya).
    
    isalnum() -> digunakan untuk mengecek apakah string berisi setidaknya karakter alfabet atau digit, atau tidak keduanya. Nilai kembaliannya True jika semua karakter dalam string adalah alfabet atau angka numerik.
    
    isspace() -> digunakan untuk mengecek apakah string berisi karakter whitespace.
    
    islower() -> digunakan untuk mengecek apakah semua karakter string adalah ditulis dalam huruf kecil (lower case), jika kondisi tersebut terpenuhi maka nilai kembaliannya adalah True.
    
    istitle() -> igunakan untuk mengecek apakah kata dalam string adalah ditulis dengan awalan huruf besar (title case), jika kondisi tersebut terpenuhi maka nilai kembaliannya adalah True.
    
    issuper() -> digunakan untuk mengecek apakah semua karakter string adalah ditulis dalam huruf besar (upper case), jika kondisi tersebut terpenuhi maka nilai kembaliannya adalah True.
"""

"""
    Mengubah karakter case
    
    capitalize() -> berfungsi untuk mengubah penulisan karakter pertama string menjadi huruf besar (capitalize).
    title() -> berfungsi untuk mengubah penulisan kata dalam string diawali dengan huruf besar (title case).
    upper() -> berfungsi untuk mengubah penulisan semua karakter string menjadi huruf besar (upper case).
    lower() -> berfungsi untuk mengubah penulisan semua karakter string menjadi huruf kecil (lower case).
    swapcase() -> berfungsi untuk membalik penulisan case karakter string. Untuk karakter yang awalnya huruf kecil menjadi huruf besar, dan sebaliknya.
"""

"""
    Pengecekan substring
    
    startswith() -> digunakan untuk mengecek apakah suatu string diawali dengan huruf/kata tertentu
        print("hello world".startswith("hell"))
        # output ➜ True
        
        print("hello world".startswith("ello"))
        # output ➜ False
    
    endswith() -> digunakan untuk mengecek apakah suatu string diakhiri dengan huruf/kata tertentu.
        print("hello world".endswith("orld"))
        # output ➜ True
        
        print("hello world".endswith("worl"))
        # output ➜ False
    
    count() -> digunakan untuk mengecek suatu string merupakan bagian dari string lain.
        print("hello world".count("ello"))
        # output ➜ 1
        print("hello world".count("l"))
        # output ➜ 3
"""

"""
    Pencarian index substring
    
    method-method berikut sebenernya kegunaanya mirip seperti method untuk pengecekan substring, perbedaanya adalah nilai balik pemanggilan method berupa index substring.
"""
text = "hello world hello world"
print(text.count("ello"))

text = "hello world hello world"
print(text.index("worl"))
# output ➜ 6

text = "hello world hello world"
print(text.rindex("worl"))

text = "hello world hello world"
print(text.find("woxl"))

text = "hello world hello world"
print(text.rfind("worl"))

"""
    Replace substring
    
    replace() -> digunakan untuk me-replace suatu substring dengan string lain. Contoh penggunaan:
"""
str_old = "hello world"
str_new = str_old.replace("world", "dunia")
print(f"new string: {str_new}")

"""
    trimming / stripping

    Metode trimming/stripping digunakan untuk menghapus whitespace yang diantaranya adalah baris baru dan juga spasi.
"""

text = """
hello python
"""
print(f"--{text}--")

# menggunakan teknik trimmnigg
print(f"--{text.strip()}--")

"""
    join string

    Method join() berguna untuk menggabungkan list berisi element string. String yang digunakan untuk memanggil method ini menjadi separator operasi join.
"""
data = ["hello", "world", "abcdef"]
res = "-".join(data)
print(res)
