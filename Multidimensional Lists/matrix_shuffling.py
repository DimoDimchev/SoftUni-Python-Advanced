rows, cols = [int(el) for el in input().split()]

matrix = [[] * rows for x in range(0, rows)]

for i in range(rows):
    row = input().split()
    for j in range(cols):
        matrix[i].append(row[j])

while True:
    command = input()
    if command == "END":
        break
    else:
        command_list = command.split()
        if command_list[0] == "swap" and len(command_list) == 5:
            if int(command_list[1]) <= len(matrix) and int(command_list[2]) <= len(matrix) and int(command_list[3]) <= len(matrix) and int(command_list[4]) <= len(matrix):
                element1_row = int(command_list[1])
                element1_col = int(command_list[2])
                element2_row = int(command_list[3])
                element2_col = int(command_list[4])

                matrix[element1_row][element1_col], matrix[element2_row][element2_col] = matrix[element2_row][element2_col], matrix[element1_row][element1_col]
                print("\n".join([' '.join(map(str, row)) for row in matrix]))
            else:
                print("Invalid input!")
        else:
            print("Invalid input!")