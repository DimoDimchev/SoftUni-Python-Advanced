def create_triangle(num, list):
    for i in range(1, num + 1):
        list.append(i)
        print(*list)

    for i in range(num, 1, -1):
        list.remove(i)
        print(*list)
