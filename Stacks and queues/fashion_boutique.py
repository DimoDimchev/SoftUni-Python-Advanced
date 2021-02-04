stack = [int(el) for el in input().split()]
rack_capacity = int(input())

racks = 1
sum_clothes = 0

while stack:
    last = stack.pop()
    if sum_clothes + last <= rack_capacity:
        sum_clothes += last
    else:
        racks += 1
        sum_clothes = last

print(racks)