text = input()

elements_dict = {}

for l in text:
    if l not in elements_dict.keys():
        elements_dict[l] = text.count(l)

for (key, value) in sorted(elements_dict.items()):
    print(f"{key} : {value} time/s")