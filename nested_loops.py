def flatten(matrix):
    result = []
    for row in matrix:
        for value in row:
            result.append(value)
    return result

def row_sums(matrix):
    result = []
    for row in matrix:
        total = 0
        for value in row:
            total += value
        result.append(total)
    return result

def col_sums(matrix):
    result = []
    if len(matrix) > 0:
        for col in range(len(matrix[0])):
            total = 0
            for row in range(len(matrix)):
                total += matrix[row][col]
            result.append(total)
    return result
