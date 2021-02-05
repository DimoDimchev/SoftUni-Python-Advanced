num = int(input())

odd_set = []
even_set = []

for i in range(1, num + 1):
    name = input()
    word_score = 0

    for letter in name:
        word_score += ord(letter)

    word_score = int(word_score / i)

    if word_score % 2 == 0:
        even_set.append(word_score)
    else:
        odd_set.append(word_score)

odd_set = set(odd_set)
even_set = set(even_set)

sum_odd = sum(odd_set)
sum_even = sum(even_set)

if sum_odd == sum_even:
    result = odd_set | even_set
elif sum_odd >= sum_even:
    result = odd_set - even_set
elif sum_odd <= sum_even:
    result = odd_set ^ even_set

result = [str(el) for el in result]
print(', '.join(result))