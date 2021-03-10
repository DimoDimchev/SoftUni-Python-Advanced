try:
    f = open('file.txt', 'r')
    print("File found")
except FileNotFoundError:
    print("File not found")