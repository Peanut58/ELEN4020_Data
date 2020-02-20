import numpy as np 

def rank3TensorMultOpenMP(A,B,C):
    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(A[0][0])):
                for l in range(len(B)):
                    C[i][j][k] += A[i][j][l]*B[l][j][k]
    return C
N = [10,20,30]
np.random.seed()

for n in N:
    A = np.random.randint(0, 10, size=(n,n,n))
    B = np.random.randint(0, 10, size=(n,n,n))
    C = np.zeros((n,n,n), dtype=int)
    # print("A")
    # print(A)
    # print("B")
    # print(B)
    
    # print("\n")

    rank3TensorMultOpenMP(A,B,C)
    # print("my answer")
    # print(C)

