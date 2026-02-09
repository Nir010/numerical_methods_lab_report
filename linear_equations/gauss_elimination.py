import numpy as np

# Augmented matrix
A = np.array([
    [3.0, 1.0, 1.0, 1.0],
    [2.0, 4.0, 1.0, 2.0],
    [1.0, 1.0, 5.0, 3.0]
])

n = len(A)

# Forward Elimination
for i in range(n):
    for j in range(i+1, n):
        ratio = A[j][i] / A[i][i]
        for k in range(n+1):
            A[j][k] = A[j][k] - ratio * A[i][k]

# Back Substitution
x = np.zeros(n)
x[n-1] = A[n-1][n] / A[n-1][n-1]

for i in range(n-2, -1, -1):
    x[i] = A[i][n]
    for j in range(i+1, n):
        x[i] = x[i] - A[i][j] * x[j]
    x[i] = x[i] / A[i][i]

# Print solution
print("Solution:")
print("x =", round(x[0], 4))
print("y =", round(x[1], 4))
print("z =", round(x[2], 4))


#PROBLEM: Solve the system of equations using Gauss elimination method
# 3x + y + z = 1,    2x + 4y + z = 2,   x + y + 5z = 3