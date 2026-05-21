def countdown(n):
    result = []
    while n >= 0:
        result.append(n)
        n -= 1
    return result

def double_until(limit):
    result = []
    value = 1
    while value <= limit:
        result.append(value)
        value *= 2
    return result
