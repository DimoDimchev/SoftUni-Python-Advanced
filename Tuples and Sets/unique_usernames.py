num = int(input())

username_list = []

for _ in range(num):
    username_list.append(input())

for el in set(username_list):
    print(el)