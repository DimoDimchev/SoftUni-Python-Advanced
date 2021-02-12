def age_assignment(*args, **kwargs):
    names = args
    ages = kwargs
    result_dict = {}

    for letter in ages.keys():
        for name in names:
            if letter == name[0]:
                result_dict[name] = ages[letter]
    return result_dict


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))