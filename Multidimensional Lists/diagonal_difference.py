def find_diagonal1(matrix, diagonal, i):
    for element in matrix:
        diagonal += element[i]
        i += 1
    return diagonal


def find_diagonal2(matrix, diagonal, i):
    for element in matrix:
        diagonal += element[len(element) - 1 - i]
        i += 1
    return diagonal


diagonal = 0
i = 0

num = int(input())
input_matrix = [[] * num for x in range(0, num)]

for row in range(num):
    lines = [int(x) for x in input().split()]
    input_matrix[row] = lines

print(abs(find_diagonal1(input_matrix, diagonal, i) - find_diagonal2(input_matrix, diagonal, i)))
