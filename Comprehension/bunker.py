item_categories = input().split(", ")

categories_dict = {category: [] for category in item_categories}
quantity = 0
quality = 0

for _ in range(int(input())):
    command_list = input().split(" - ")
    category = command_list[0]
    food = command_list[1]

    quantity += int(command_list[2].split(";")[0].split(":")[1])
    quality += int(command_list[2].split(";")[1].split(":")[1])

    categories_dict[category].append(food)

print(f"Count of items: {quantity}")
print(f"Average quality: {'{0:.2f}'.format(quality / len(categories_dict))}")
[print(f"{category} -> {', '.join(categories_dict[category])}") for category in categories_dict]
