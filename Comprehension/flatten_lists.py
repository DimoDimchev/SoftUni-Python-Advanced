sublist = ' '.join([sublist[::-1] for sublist in input().split('|')])
print(' '.join(reversed([el for el in sublist.split() if el != " "])))