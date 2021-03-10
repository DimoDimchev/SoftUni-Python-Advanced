try:
    file = open('my_first_file.txt', 'x')
    file.write("I just created my first file!")
    file.close()
except FileExistsError:
    print("File already exists")
finally:
    print("Program finished")