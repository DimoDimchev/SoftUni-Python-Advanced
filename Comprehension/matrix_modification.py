num = int(input())
matrix = [[int(i) for i in input().split(" ")] for _ in range(num)]

while True:
    command = input()
    if command == "END":
        break
    else:
        command_list = command.split()

        action = command_list[0]
        x_coordinate = int(command_list[1])
        y_coordinate = int(command_list[2])
        value_to_change = int(command_list[3])

        if 0 <= x_coordinate < num and 0 <= y_coordinate < num:
            if action == "Add":
                matrix[x_coordinate][y_coordinate] += value_to_change
            else:
                matrix[x_coordinate][y_coordinate] -= value_to_change
        else:
            print("Invalid coordinates")

[print(*row) for row in matrix]