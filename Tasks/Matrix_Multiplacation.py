matrix1 = [[0] * 3 for _ in range(3)]
matrix2 = [[0] * 3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        print(f"Enter element at ({i}, {j}): ", end="")
        matrix1[i][j] = int(input())

for i in range(3):
    for j in range(3):
        print(f"Enter element at ({i}, {j}): ", end="")
        matrix2[i][j] = int(input())

result = [[0] * 3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        for k in range(3):
            result[i][j] += matrix1[i][k] * matrix2[k][j]

print("Resultant Matrix:")
for row in result:
    print(row)

