"""
    Chapter ini membahas bagaimana penerapan args dan kwargs fungsi di python.
"""

"""
    Pengenalan Args
    Args (atau yang umumnya ditulis sebagai *args) merupakan notasi penulisan parameter spesial dengan kapabilitas bisa menampung banyak positional argument untuk ditampung dalam 1 parameter saja.
"""


def sum_then_print(*numbers):
    total = 0
    for n in numbers:
        total = total + n
    print(total)


sum_then_print(1, 2, 3, 4, 5)

"""
    Args untuk argument dengan tipe data bervariasi
    metode *args mampu menampung segala jenis argument tanpa menghiraukan tipe datanya. Contohnya bisa dilihat pada program berikut ini:
"""


def print_data(*params):
    print(f"type: {type(params)}, data: {params}")
    for i in range(len(params)):
        print(f"param {i}: {params[i]}")


print_data("eren yeager", ["attack titan", "founding titan", True], "mikasa ackerman", "eldian", 3,
           ("maria", "rose", "sina"), {"reiner", "armored titan"})

"""
    Kombinasi positional argument, args, dan keyword argument
"""


def sum_total_with_description(message: str, *args, suffix_msg: str):
    total = 0
    for i in args:
        total = total + i
    print(f"{message}: {total}. {suffix_msg}")


sum_total_with_description("total perhitungan nilai", 1, 2, 3, 4, 5, suffix_msg="perhitungan selesai")

"""
    Pengenalan Kwargs
    kwargs atau keyword arguments, merupakan notasi penulisan parameter spesial dengan kapabilitas bisa menampung banyak keyword argument pemanggilan fungsi dalam 1 parameter saja.
"""


def print_data(**data):
    print(f"type: {type(data)}")
    print(f"data: {data}")

    for key in data:
        print(f"param: {key}, value: {data[key]}")

print_data(name="eren yeager", is_dead=True, is_founding_titan=True, total_inherited_titan=3, titans=("attack", "war hammer", "founding"))

"""
    Kombinasi positional argument, args, dan kwargs
    Kombinasi antara positional argument, *args, dan **kwargs bisa dilakukan dengan ketentuan semua positional argument ditulis terlebih dahulu, kemudian diikuti *args lalu **kwargs.
"""
def print_all(message, *params, **others):
    print(f"message: {message}")
    print(f"params: {params}")
    print(f"others: {others}")

print_all("attack titan", 24, True, ("yes, it is", "no, we're not"), name="eren yeager", is_dead=True, has_girlfriend=True)