start = int(input())
end = int(input())

result = list({el for el in range(start, end + 1) for i in range(2, 11) if el % i == 0})
print(result)
