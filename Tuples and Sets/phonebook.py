contact_dict = {}

finished = False

while True:
    command = input()
    if command.isdigit():
        finished = True
        break
    else:
        name, number = command.split("-")
        contact_dict[name] = number

if finished:
    for _ in range(int(command)):
        contact = input()
        if contact not in contact_dict:
            print(f"Contact {contact} does not exist.")
        else:
            print(f"{contact} -> {contact_dict[contact]}")