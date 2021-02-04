stack = list(input())

result = ""
while stack:
    item = stack.pop()
    result += item

print(result)