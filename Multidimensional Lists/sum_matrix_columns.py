rows, columns = [int(el) for el in input().split(", ")]

matrix = [0 for x in range(rows)]

for row in range(rows):
    lines = [int(x) for x in input().split()]
    matrix[row] = lines

for i in range(columns):
    sum_el = 0
    for j in range(rows):
        sum_el += matrix[j][i]
    print(sum_el)
