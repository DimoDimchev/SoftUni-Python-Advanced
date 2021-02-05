num = int(input())

result_set = []

for _ in range(num):
    temp_list = input().split()
    for el in temp_list:
        if el not in result_set:
            result_set.append(el)

for el in result_set:
    print(el)