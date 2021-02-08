rows, columns = [int(el) for el in input().split(", ")]

matrix = [0 for x in range(rows)]

for row in range(rows):
    lines = [int(x) for x in input().split(", ")]
    matrix[row] = lines

sum_elements = 0

for element in matrix:
    for number in element:
        sum_elements += number

print(sum_elements)
print(matrix)