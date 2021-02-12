def find_min(data):
    min_num = min(data)
    return min_num


def find_max(data):
    max_num = max(data)
    return max_num


def find_sum(data):
    sum_num = sum(data)
    return sum_num


data_list = [int(el) for el in input().split()]
print(f"The minimum number is {find_min(data_list)}")
print(f"The maximum number is {find_max(data_list)}")
print(f"The sum number is {find_sum(data_list)}")