from math import log

number = int(input())
base = input()

if base == "natural":
    print('{0:.2f}'.format(log(number)))
else:
    print('{0:.2f}'.format(log(number, int(base))))