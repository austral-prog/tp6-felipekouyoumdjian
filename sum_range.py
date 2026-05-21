def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def sum_evens(n):
    total = 0
    for i in range(2, n + 1, 2):
        total += i
    return total

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
