rows, cols = [int(el) for el in input().split()]

matrix = [[] * rows for x in range(0, rows)]

for row in range(rows):
    for col in range(cols):
        matrix[row].append(f"{chr(97+row)}{chr(97+col+row)}{chr(97+row)}")

for row in matrix:
    print(' '.join(row))
