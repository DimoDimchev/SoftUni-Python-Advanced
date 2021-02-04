from collections import deque

queue = deque([])

starting_capacity = int(input())

while True:
    command = input()
    if command == "Start":
        break
    else:
        queue.append(command)

while True:
    command = input()
    if command == "End":
        break
    else:
        if "refill" in command:
            command = command.split()
            quantity = int(command[1])
            starting_capacity += quantity
        else:
            quantity = int(command)
            if quantity <= starting_capacity:
                print(f"{queue.popleft()} got water")
                starting_capacity -= quantity
            else:
                print(f"{queue.popleft()} must wait")

print(f"{starting_capacity} liters left")