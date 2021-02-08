num = int(input())

matrix = [0 for x in range(num)]
diagonal = 0
i = 0

for row in range(num):
    lines = [int(x) for x in input().split()]
    matrix[row] = lines


for row in matrix:
    diagonal += row[i]
    i += 1

print(diagonal)