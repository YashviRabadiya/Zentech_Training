matrix = []

# Take input for 3x3 matrix
for i in range(3):
    row = []
    for j in range(3):
        num = int(input(f"Enter element at ({i}, {j}): "))
        row.append(num)
    matrix.append(row)

# Calculate determinant
det = (
    matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
    - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
    + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
)

print("Matrix:")
for row in matrix:
    print(row)

print("Determinant:", det)