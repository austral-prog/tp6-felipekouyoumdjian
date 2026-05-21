def put(value, lst):
    index = -1
    i = 0
    while i < len(lst) and index == -1:
        if lst[i] == "":
            lst[i] = value
            index = i
        i += 1
    return index

def remove(value, lst):
    count = 0
    for i in range(len(lst)):
        if lst[i] == value:
            lst[i] = ""
            count += 1
    return count
