len1, len2 = [int(el) for el in input().split()]

set1 = []
set2 = []
result_set = []

for _ in range(len1):
    set1.append(input())

for _ in range(len2):
    set2.append(input())

result_set = set(set1) & set(set2)

if result_set:
    for el in result_set:
        print(el)