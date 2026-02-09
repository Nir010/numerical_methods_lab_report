import numpy as np
from scipy.linalg import lu

# Coefficient matrix
A = np.array([
    [3, 2, 1],
    [2, 3, 2],
    [1, 2, 3]
], dtype=float)

# Right-hand side
B = np.array([10, 14, 14], dtype=float)

# LU factorization
P, L, U = lu(A)

print("L =\n", L)
print("\nU =\n", U)

# Solve Ly = B (forward substitution)
y = np.zeros_like(B)
for i in range(len(B)):
    y[i] = B[i] - np.dot(L[i,:i], y[:i])

# Solve Ux = y (back substitution)
x = np.zeros_like(B)
for i in range(len(B)-1, -1, -1):
    x[i] = (y[i] - np.dot(U[i,i+1:], x[i+1:])) / U[i,i]

print("\nSolution:")
print("x =", round(x[0], 4))
print("y =", round(x[1], 4))
print("z =", round(x[2], 4))
#PROBLEM: Solve the following linear equation by LU factorization [Dolittle’s] method. 3x + 2y + z = 10, 2x + 3y + 2z = 14, x + 2y + 3z = 14 