import numpy as np
import pymp
import time

def rank2TensorMultOpenMP(A, B, C): 
    for i in range(0, len(A)):
        for j in range(0, len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    return C

N = [10, 20, 30]
np.random.seed()
noThreads = 3
for n in N:
    print("N is ",n)
    A = np.random.randint(0, 100, size=(n, n))
    B = np.random.randint(0, 100, size=(n, n))
    C = np.zeros((n, n), dtype=int)
    #print(A)
    #print(B)

    t1 = time.perf_counter()
    with pymp.Parallel(noThreads) as p:
        rank2TensorMultOpenMP(A,B,C)
        #p.print(p.num_threads, p.thread_num)
    t2 = time.perf_counter()
    print(f"Time taken for a %s x %s with Python MP was {t2 - t1:0.4f} sec for %s threads"%(n,n,noThreads))

    #arrC = np.dot(A, B)
    #print("actual answer")
    #print(arrC)
    #print("my answer")
    #print(C)