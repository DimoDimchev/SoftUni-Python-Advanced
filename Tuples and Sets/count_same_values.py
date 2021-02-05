input_tuple = tuple([float(el) for el in input().split()])

items_dict = {}

for el in input_tuple:
    if el not in items_dict:
        items_dict[el] = input_tuple.count(el)

for (key, value) in items_dict.items():
    print(f"{key} - {value} times")