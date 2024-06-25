# 2-d array simulation, although is's a list
print("\n 2-d array\n")

A = [[1, 2, 3]] * 4  # 4x3
B = [[1, 2, 3, 4]] * 3  # 3x4
C = [[0, 0, 0, 0]] * 4  # 4x4

# (IxK) @ (KxJ) -> (IxJ)
I = len(A)
K = len(A[0])
J = len(B[0])

for i in range(I):
    for j in range(J):
        for k in range(K):
            C[i][j] += A[i][k] * B[k][j]
            print(f"C[{i}][{j}] += A[{i}][{k}] * B[{k}][{j}]")

print("\nAfter reordering\n")
# reorder
for i in range(I):
    for k in range(K):
        for j in range(J):
            C[i][j] += A[i][k] * B[k][j]
            print(f"C[{i}][{j}] += A[{i}][{k}] * B[{k}][{j}]")

# 1-d array simulation

print("\n 1-d array\n")

A = [1, 2, 3] * 4  # 4x3 IxK
B = [1, 2, 3, 4] * 3  # 3x4 KxJ
C = [0, 0, 0, 0] * 4  # 4x4 IxJ

I = 4
K = 3
J = 4

for i in range(I):
    for j in range(J):
        for k in range(K):
            print(f"C[{j + i * J}] += A[{k + i * K}] * B[{j + k * J}]")
            C[j + i * J] += A[k + i * K] * B[j + k * J]

print("\nAfter reordering\n")
# reorder

for i in range(I):
    for k in range(K):
        for j in range(J):
            print(f"C[{j + i * J}] += A[{k + i * K}] * B[{j + k * J}]")
            C[j + i * J] += A[k + i * K] * B[j + k * J]
