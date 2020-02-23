#Sequential 2D matrix mulltiplication 

import numpy as np
import sys
import time

#2D matrix multiplication. C = A*B
def rank2Tensor(A, B, C): 
    if len(A[0]) != len(B):
        sys.exit('The number of columns in Matrix A is not equal to the number of rows in Matrix B')

    for i in range(0, len(A)):
        for j in range(0, len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    return C

#Array bounds
N = [10, 20, 30]
#set seed to ensure that new random numbers is always generated
np.random.seed()
noThreads = 0
for n in N:
    #generate A and B matrices with random numbers between 0 and n. Dimension is n*n. Generate an empty C matrix of dimention n*n
    print("N is ",n)
    A = np.random.randint(0,n, size=(n, n))
    B = np.random.randint(0, n, size=(n, n))
    C = np.zeros((n, n), dtype=int)

    #start timer for timing matrix multiplication
    t1 = time.perf_counter()
    rank2Tensor(A,B,C)
    #end timer for timing matrix multiplication
    t2 = time.perf_counter()
    #calculate time of program execution
    print(f"Time taken for a %s x %s with Python MP was {t2 - t1:0.4f} sec for %s threads"%(n,n,noThreads))