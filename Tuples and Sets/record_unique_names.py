num = int(input())

names_list = []

for _ in range(num):
    names_list.append(input())

unique_names = set(names_list)
for name in unique_names:
    print(name)