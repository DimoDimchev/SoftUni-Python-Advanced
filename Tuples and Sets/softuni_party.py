num = int(input())

guest_dict = {}

for i in range(num):
    guest_dict[input()] = 0

while True:
    command = input()
    if command == "END":
        break
    else:
        if command in guest_dict:
            guest_dict.pop(command)

print(len(guest_dict))

if guest_dict:
    for key in sorted(guest_dict.keys()):
        print(key)