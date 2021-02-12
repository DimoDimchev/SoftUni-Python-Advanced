from itertools import combinations

people = input().split(", ")
chairs = int(input())

for combination in combinations(people, chairs):
    print(', '.join(combination))
