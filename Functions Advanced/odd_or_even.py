def odd_command(data):
    odd_elements = sum(list(filter(lambda x: x % 2 != 0, data)))
    return odd_elements * len(data)


def even_command(data):
    even_elements = sum(list(filter(lambda x: x % 2 == 0, data)))
    return even_elements * len(data)


command = input()
data_list = [int(el) for el in input().split()]

if command == "Odd":
    print(odd_command(data_list))
else:
    print(even_command(data_list))
