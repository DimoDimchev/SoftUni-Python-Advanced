def even_odd(*args):
    data = [arg for arg in args]
    command = data.pop()
    # data = [int(el) for el in data]
    if command == "odd":
        result = list(filter(lambda x: x % 2 != 0, data))
        return result
    else:
        result = list(filter(lambda x: x % 2 == 0, data))
        return result
