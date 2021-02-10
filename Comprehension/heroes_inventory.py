heroes_list = input().split(", ")

heroes_dict = {name: {} for name in heroes_list}

while True:
    command = input()
    if command == "End":
        break
    else:
        name, weapon, quantity = command.split("-")
        if weapon not in heroes_dict[name]:
            heroes_dict[name][weapon] = int(quantity)

[print(f"{name} -> Items: {len(heroes_dict[name])}, Cost: {sum(heroes_dict[name].values())}") for name in heroes_dict]
