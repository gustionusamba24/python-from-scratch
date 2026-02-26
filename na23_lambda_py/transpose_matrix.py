def transpose_matrix(m):
    tm = []
    for i in range(len(m[0])):
        tr = []
        for row in m:
            tr.append(row[i])
        tm.append(tr)

    return tm

matrix = [[1, 2], [3, 4], [5, 6]]
res = transpose_matrix(matrix)
print(res)