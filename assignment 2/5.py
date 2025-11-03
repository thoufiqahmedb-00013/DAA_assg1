def knapsack_brute_force(weights, values, capacity):
    n = len(weights)
    max_value = 0
    best_combo = []

    for i in range(2**n):
        combo = []
        total_weight = 0
        total_value = 0

        for j in range(n):
            if (i >> j) & 1:
                total_weight += weights[j]
                total_value += values[j]
                combo.append(j)

        if total_weight <= capacity and total_value > max_value:
            max_value = total_value
            best_combo = combo

    return best_combo, max_value

weights = [2, 3, 4, 5, 9, 7]
values =  [3, 4, 8, 8, 10, 6]
capacity = 15

items, value = knapsack_brute_force(weights, values, capacity)
print("Best Item Indices:", items)
print("Maximum Value:", value)

