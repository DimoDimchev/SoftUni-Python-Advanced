num = int(input())

longest_intersection = {}
len_longest = 0

for _ in range(num):
    temp_list1, temp_list2 = input().split("-")
    temp_list1 = temp_list1.split(",")
    temp_list2 = temp_list2.split(",")

    list1 = []
    list2 = []

    for i in range(int(temp_list1[0]), int(temp_list1[1]) + 1):
        list1.append(i)

    for i in range(int(temp_list2[0]), int(temp_list2[1]) + 1):
        list2.append(i)

    set1 = set(list1)
    set2 = set(list2)

    intersection = list(set1 & set2)
    if len(intersection) > len_longest:
        len_longest = len(intersection)
        longest_intersection["intersection"] = intersection

for value in longest_intersection.values():
    print(f"Longest intersection is {value} with length {len_longest}")