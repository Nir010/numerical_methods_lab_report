import numpy as np

# Original matrix
A = np.array([
    [1, 2, 6],
    [2, 5, 15],
    [6, 15, 46]
], dtype=float)

n = A.shape[0]

# Create augmented matrix [A | I]
aug = np.hstack((A, np.identity(n)))

# Gauss-Jordan elimination
for i in range(n):
    # Make the pivot = 1
    aug[i] = aug[i] / aug[i, i]

    # Make all other entries in column i = 0
    for j in range(n):
        if j != i:
            aug[j] = aug[j] - aug[j, i] * aug[i]

# Extract inverse matrix
A_inv = aug[:, n:]

# Round for readability
A_inv = np.round(A_inv, 3)

print("Inverse of A using Gauss-Jordan:")
print(A_inv)
#Using Gauss Jordan method, find the inverse of the matrix:
# {1  2  6 }
# {2  5  15}
# {6  15 46}