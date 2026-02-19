should_continue = True

while should_continue:
    n = int(input("enter an even number greater than 0: "))

    if n <= 0 or n % 2 == 1:
        print(n, "is not an even number greater than 0")
        should_continue = False
    else:
        print("number:", n)

n = int(input("enter max data: "))
i = 1

while i <= n:
    print("number", i)
    i += 1

# keyword break
while True:
    n = int(input("enter a number divisible by 3: "))
    if n % 3 != 0:
        break
    print("%d is divisible by 3" % (n))
    