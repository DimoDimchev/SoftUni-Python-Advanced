from collections import deque

queue = deque([])

while True:
    name = input()
    if name == "Paid":
        for p in queue:
            print(p)
        queue.clear()
    elif name == "End":
        break
    else:
        queue.append(name)

print(f"{len(queue)} people remaining.")