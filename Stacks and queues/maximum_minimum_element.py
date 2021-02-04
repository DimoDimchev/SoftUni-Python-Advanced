stack = []

nums = int(input())

for _ in range(nums):
    command_list = input().split()

    if command_list[0] == '1':
        stack.append(int(command_list[1]))
    if stack and command_list[0] == '2':
        stack.pop()
    if stack and command_list[0] == '3':
        print(max(stack))
    if stack and command_list[0] == '4':
        print(min(stack))

stack = reversed([str(el) for el in stack])
print(', '.join(stack))