n = int(input("Enter the size of the matrix: "))
print("\n")
matrix = []

for i in range(n):
    row = []
    for j in range(n):
        val = int(input(f"Enter element at position ({i}, {j}): "))
        row.append(val)
    matrix.append(row)

# Step 2: Get i and j from user
i = int(input(f"Enter row index i (0 to {n-1}): "))
j = int(input(f"Enter column index j (0 to {n-1}): "))

# Step 3: Fetch and display the value
if 0 <= i < n and 0 <= j < n:
    print(f"Value at position ({i}, {j}) is: {matrix[i][j]}")
else:
    print("Invalid indices. Please enter values between 0 and n-1.")