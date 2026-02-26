"""
    Closure adalah istilah umum dalam programming untuk deklarasi fungsi yang berada di dalam fungsi lain (nested function).
"""


def outer_func(numbers=[]):
    print(f"numbers: {numbers}")

    def inner_func():
        print(f"max: {max(numbers)}")
        print(f"min: {min(numbers)}")

    print("call inner_func() within outer_func()")
    inner_func()

    return inner_func


print("call outer_func()")
f = outer_func([1, 2, 3, 4])

print("call inner_func() outside of outer_func()")
f()

"""
    Fungsi sebagai argument parameter
"""


def aggregate(message, numbers, f):
    res = f(numbers)
    print(f"{message}: {res}")


def sum(numbers):
    total = 0
    for i in numbers:
        total += i

    return total


def avg(numbers):
    total = 0
    for i in numbers:
        total += i

    return total / len(numbers)


aggregate("total", [24, 67, 22, 98, 3, 50], sum)
aggregate("average", [24, 67, 22, 98, 3, 50], avg)
aggregate("max number", [24, 67, 22, 98, 3, 50], max)
aggregate("min number", [24, 67, 22, 98, 3, 50], min)
