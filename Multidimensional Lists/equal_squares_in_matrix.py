rows, cols = [int(el) for el in input().split()]
squares = []
equal_squares = 0

matrix = [[] * rows for x in range(0, rows)]
for i in range(rows):
    row = input().split()
    for j in range(cols):
        matrix[i].append(row[j])

for i in range(len(matrix) - 1):
    row = matrix[i]
    for j in range(len(row) - 1):
        square = [
            [matrix[i][j], matrix[i][j + 1]],
            [matrix[i + 1][j], matrix[i + 1][j + 1]]
        ]
        if square[0].count(square[0][0]) == 2 and square[1].count(square[0][0]) == 2:
            equal_squares += 1
        squares.append(square)

print(equal_squares)