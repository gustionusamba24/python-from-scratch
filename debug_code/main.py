def sum_numbers(*numbers): 
    total = 0
    for n in numbers:
        total += n
        print(f"current total: {total}")
    return total

print(sum_numbers(1, 2, 3, 4, 5))