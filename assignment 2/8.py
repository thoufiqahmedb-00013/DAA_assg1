def MatrixInput(rows, cols, name):
    matrix = []
    print(f"Enter elements of matrix {name} row-wise:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Element of matrix {name} [{i+1},{j+1}]: "))
            row.append(element)
        matrix.append(row)
    return matrix

def MulpyMatrix(A,B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            sum = 0
            for k in range(len(B)):
                sum += A[i][k] * B[k][j]
            row.append(sum)
        result.append(row)
    return result
r1 = int(input(f"Enter number of rows for matrix A: "))
c1 = int(input(f"Enter number of columns for matrix A: "))
r2 = int(input(f"Enter number of rows for matrix B: "))
c2 = int(input(f"Enter number of columns for matrix B: "))

if c1 != r2:
    print("Matrix multiplication not possible with given dimensions.")
else:
    A = MatrixInput(r1, c1, 'A')
    B = MatrixInput(r2, c2, 'B')
    result = MulpyMatrix(A, B)

    for row in result:
        print(row)
