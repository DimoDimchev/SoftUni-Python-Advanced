text = input()
stack_brackets = []

for i in range(len(text)):
    if text[i] == "(":
        stack_brackets.append(i)
    elif text[i] == ")":
        start_index = stack_brackets.pop()
        print(text[start_index:i + 1])