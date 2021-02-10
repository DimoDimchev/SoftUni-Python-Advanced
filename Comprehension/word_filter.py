start_list = input().split()

result_list = [el for el in start_list if len(el) % 2 == 0]

for el in result_list:
    print(el)