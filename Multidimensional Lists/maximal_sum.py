import sys

rows, cols = [int(el) for el in input().split()]

max_sum = -sys.maxsize
max_square = None

matrix = [[] * rows for x in range(0, rows)]
for i in range(rows):
    row = [int(el) for el in input().split()]
    for j in range(cols):
        matrix[i].append(row[j])

for i in range(len(matrix) - 2):
    row = matrix[i]
    for j in range(len(row) - 2):
        square = [
            [matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]],
            [matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]],
            [matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]]
        ]

        square_sum = 0

        for el in square:
            for k in el:
                square_sum += int(k)

        if square_sum > max_sum:
            max_square = square
            max_sum = square_sum

print(f"Sum = {max_sum}")
print("\n".join([' '.join(map(str, row)) for row in max_square]))
