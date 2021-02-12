def find_negative(data):
    negative_sum = 0
    for el in data:
        if el < 0:
            negative_sum += el
    print(negative_sum)
    return abs(negative_sum)


def find_positive(data):
    positive_sum = 0
    for el in data:
        if el >= 0:
            positive_sum += el
    print(positive_sum)
    return abs(positive_sum)


def evaluate(data):
    negative = find_negative(data)
    positive = find_positive(data)
    if negative > positive:
        return "The negatives are stronger than the positives"
    else:
        return "The positives are stronger than the negatives"


data_list = [int(el) for el in input().split()]
print(evaluate(data_list))