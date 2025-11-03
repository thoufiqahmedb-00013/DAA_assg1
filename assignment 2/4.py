distance = [
    [0, 3, 8, 15, 6],
    [3, 0, 5, 10, 7],
    [8, 5, 0, 12, 4],
    [15, 10, 12, 0, 9],
    [6, 7, 4, 9, 0]
]

def permutation(data):
    if len(data) == 0 or len(data) == 1:
        return [data]
    result = []
    for i in range(len(data)):
        current = data[i]
        remaining = data[:i] + data[i+1:]
        for p in permutation(remaining):
            result.append([current] + p)
    return result

def salesman(distance):
    n = len(distance)
    cities = list(range(1, n))

    permutations = permutation(cities)

    min_cost = 111111
    min_path = []

    for perm in permutations:
        path = [0] + perm + [0]
        cost = 0
        for i in range(n):
            cost += distance[path[i]][path[i + 1]]
        if cost < min_cost:
            min_cost = cost
            min_path = path

    return min_path, min_cost

path, cost = salesman(distance)
print("Shortest Path:", path)
print("Minimum Cost:", cost)