import numpy as np
import threading

def rank2TensorMultOpenMP(A, B, C): 
    for i in range(0, len(A)):
        for j in range(0, len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    return C

def threadFunc():
    for i in range(8):
        rank2TensorMultOpenMP(A,B,C)


N = [10, 20, 30]
np.random.seed()
for n in N:
    print("N is ",n)
    A = np.random.randint(0, 100, size=(n, n))
    B = np.random.randint(0, 100, size=(n, n))
    C = np.zeros((n, n), dtype=int)
   
    th = threading.Thread(target=threadFunc)
    
        
