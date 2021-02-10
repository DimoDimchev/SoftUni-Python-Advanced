num = int(input())

matrix = [[] * num for x in range(0, num)]

for i in range(num):
    row = input().split(', ')
    for j in range(len(row)):
        matrix[i].append(row[j])

new_matrix = [[int(el) for el in sublist if int(el) % 2 == 0] for sublist in matrix]

print(new_matrix)