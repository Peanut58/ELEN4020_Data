import numpy as np

# A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# B = np.array([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
# C = np.zeros((3, 3), dtype=int)
N = [10, 20, 30]
for n in N:
    print("N is ",n)
    A = np.random.randint(0, 100, size=(n, n))
    B = np.random.randint(0, 100, size=(n, n))
    C = np.zeros((n, n), dtype=int)
    print(A)
    print(B)

    for i in range(0, len(A)):
        for j in range(0, len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]

    arrC = np.dot(A, B)
    print("actual answer")
    print(arrC)
    print("my answer")
    print(C)