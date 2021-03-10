words = open('words.txt', 'r')
text = open('text.txt', 'r')
word_list = []
word_dict = {}

for word in words:
    word_list.append(word)

text = ''.join([el for el in text])

word_list = word_list[0].split()

for word in word_list:
    word_dict[word] = text.count(word)

for key, value in word_dict.items():
    print(f"{key} - {value}")