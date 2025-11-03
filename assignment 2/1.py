import random
def permutation(data):
    if len(data) == 0 or len(data) == 1:
        return [data]
    result = []
    l = random.sample(data, len(data))
    for i in l:
        temp = permutation(l[:l.index(i)] + l[l.index(i)+1:])
        for p in temp:
            result.append([i] + p)
    return result

data = [1, 2, 3]
print(permutation(data))
