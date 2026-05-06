def sum_numbers(*numbers): 
    total = 0
    for n in numbers:
        total += n
        print(f"current total: {total}")
    return total

print(sum_numbers(1, 2, 3, 4, 5))

def matrix_multiply_scalar(matrix, scalar=1):
    res = []
    for row in matrix:
        res.append([cell * scalar for cell in row])
    return res

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print(f"matrix * scalar {1}:")
res1 = matrix_multiply_scalar(matrix)
for el in res1:
    print(el)

    
print(f"matrix * scalar {5}:")
res2 = matrix_multiply_scalar(matrix, scalar=5)
for el in res2: 
    print(el)
