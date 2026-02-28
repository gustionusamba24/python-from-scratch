"""
    Patern matching merupakan teknik pencocokan pola menggunakan kombinasi keyword match dan case. Penggunaan dasarnya mirip seperti seleksi kondisi menggunakan keyword if.
"""
command = input("Enter command: ")

match command.split(" "):
    case ["greet"]:
        name = input("Your name: ")
        print("hello", name)

    case ["greet", "balmond"]:
        print("hello balmond, how's it going?")

    case["greet", name]:
        print(f"hello {name}, how's it going?")

    case ["sum_numbers"]:
        numbers = input("The number separated by comma: ")
        total = 0
        for num in numbers.split(', '):
            total = total + int(num)
        print("total:", total)

    case ["sum_numbers", *args]:
        total = 0
        for num in args:
            total = total + int(num)
        print(f"total number using args: {total}")

    case ["lucky_number"]:
        import random
        n = random.randint(0, 100)
        print("your lucky number:", n)

    case _:
        print("unrecognized command")
