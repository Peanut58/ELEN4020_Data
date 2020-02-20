import numpy as np 
import pymp

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

with pymp.Parallel(3) as p:
    rank3TensorMultOpenMP(A,B,C)
    p.print(p.num_threads, p.thread_num)