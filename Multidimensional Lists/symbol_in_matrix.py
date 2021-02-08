num = int(input())

matrix = [[] * num for x in range(0, num)]
found_element = False
location = None

for i in range(num):
    row = input()
    for j in range(num):
        matrix[i].append(row[j])

element = input()

for row in range(num):
    if found_element:
        break
    for col in range(num):
        if matrix[row][col] == element:
            location = [row, col]
            found_element = True

if found_element:
    print(f"({location[0]}, {location[1]})")
else:
    print(f"{element} does not occur in the matrix")