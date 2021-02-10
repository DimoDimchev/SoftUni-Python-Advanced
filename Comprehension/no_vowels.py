vowels_list = ['a', 'o', 'u', 'e', 'i']

result_list = [char for char in list(input()) if char not in vowels_list]
print(''.join(result_list))