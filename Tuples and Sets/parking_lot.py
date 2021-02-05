num = int(input())

garage = set()

for _ in range(num):
    direction, number = input().split(", ")
    if direction == "IN":
        garage.add(number)
    if direction == "OUT":
        garage.remove(number)

if garage:
    for car in garage:
        print(car)
else:
    print("Parking Lot is Empty")