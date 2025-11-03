def combination(data, r):
    if r == 0:
        return [[]]
    if len(data) < r:
        return []
    result = []
    for i in range(len(data)):
        for j in combination(data[i+1:], r-1):
            result.append([data[i]] + j)

    return result

print(combination([1, 2, 3], 2))