from itertools import product

numbers = input().split(", ")
n = len(numbers)

cartesian_product = [list(x) for x in (product("+-", repeat=n))]

for signs in cartesian_product:
    elements = [''.join(x) for x in list(zip(signs, numbers))]
    expr = ''.join(elements)
    print(f"{expr}={eval(expr)}")