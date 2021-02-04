from collections import deque

queue = deque(input().split())
eliminate_num = int(input())

while not len(queue) == 1:
    for i in range(1, eliminate_num + 1):
        person = queue.popleft()
        if i == eliminate_num:
            print(f"Removed {person}")
        else:
            queue.append(person)

print(f"Last is {queue.popleft()}")