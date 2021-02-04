from collections import deque

quantity_food = int(input())

queue = deque(input().split())
max_order = max([int(el) for el in queue])

finished = True

while queue:
    if quantity_food >= int(queue[0]):
        quantity_food -= int(queue.popleft())
    else:
        finished = False
        break

print(max_order)
if not finished:
    print(f"Orders left: {' '.join([el for el in queue])}")
else:
    print("Orders complete")