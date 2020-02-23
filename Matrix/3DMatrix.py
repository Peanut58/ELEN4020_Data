import numpy as np 
import time
import sys

def rank3Tensor(A,B,C):
    if len(B) != len(A[0][0]):
        sys.exit('Matrix A and Matrix B cannot be multiplied due to incompatible dimensions')

    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(A[0][0])):
                for l in range(len(B)):
                    C[i][j][k] += A[i][j][l]*B[l][j][k]
    return C

N = [10,20,30]
np.random.seed()
noThreads = 0
for n in N:
    A = np.random.randint(0, n, size=(n,n,n))
    B = np.random.randint(0, n, size=(n,n,n))
    C = np.zeros((n,n,n), dtype=int)

    t1 = time.perf_counter()
    rank3Tensor(A,B,C)
    t2 = time.perf_counter()
    print(f"Time taken for a %s x %s with Python MP was {t2 - t1:0.4f} sec for %s threads"%(n,n,noThreads))