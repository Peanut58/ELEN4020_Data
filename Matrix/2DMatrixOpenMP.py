import numpy as np
import pymp

def rank2TensorMultOpenMP(A, B, C): 
    for i in range(0, len(A)):
        for j in range(0, len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    return C

N = [10, 20, 30]
np.random.seed()
for n in N:
    print("N is ",n)
    A = np.random.randint(0, 100, size=(n, n))
    B = np.random.randint(0, 100, size=(n, n))
    C = np.zeros((n, n), dtype=int)
    #print(A)
    #print(B)

    with pymp.Parallel(3) as p:
        rank2TensorMultOpenMP(A,B,C)
        p.print(p.num_threads, p.thread_num)

    #arrC = np.dot(A, B)
    #print("actual answer")
    #print(arrC)
    #print("my answer")
    #print(C)