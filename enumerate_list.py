def enumerate_list(lst):
    result = []
    index = 0
    for value in lst:
        if value != "":
            result.append(str(index) + ". " + value)
            index += 1
    return result

def enumerate_backwards(lst):
    result = []
    index = 0
    for value in lst:
        if value != "":
            result.append(str(index) + ". " + value[::-1])
            index += 1
    return result
