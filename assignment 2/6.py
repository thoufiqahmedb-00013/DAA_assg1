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
def knapsack(weights, values, capacity):
    n = len(weights)
    best_value = 0
    best_combination = []
    for r in range(1, n + 1):
        combs = combination(list(range(n)), r)
        for c in combs:
            total_weight = 0
            total_value = 0
            for i in c:
                total_weight += weights[i]
                total_value += values[i]

            if total_weight <= capacity and total_value > best_value:
                best_value = total_value
                best_combination = c

    return best_combination, best_value
if __name__ == "__main__":
    weights = [2, 3, 4, 5, 9, 7]
    values = [3, 4, 8, 8, 10, 6]
    capacity = 15

    best_items, max_value = knapsack(weights, values, capacity)

    print("Weights:", weights)
    print("Values :", values)
    print("Capacity:", capacity)
    print("\n")

    print("Best combination of item:", best_items)
    print("Total Value:", max_value)
    total_weight = 0
    for i in best_items:
        total_weight += weights[i]
    print("Total Weight:", total_weight)
