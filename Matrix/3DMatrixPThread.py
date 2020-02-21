import numpy as np 
import time
import threading
import sys

def rank3TensorMultPThread(A,B,C):
    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(A[0][0])):
                for l in range(len(B)):
                    C[i][j][k] += A[i][j][l]*B[l][j][k]
    return C
    
N = [10,20,30]
np.random.seed()
noThreads = int(sys.argv[1])

for n in N:
    A = np.random.randint(0, 10, size=(n,n,n))
    B = np.random.randint(0, 10, size=(n,n,n))
    C = np.zeros((n,n,n), dtype=int)
    #print("A")
    #print(A)
    #print("B")
    #print(B)
    
    threads = []
    t1 = time.perf_counter()
    for threadNum in range(noThreads):
        x = threading.Thread(target=rank3TensorMultPThread, args=(A,B,C,))
        threads.append(x)
        x.start()

    for threadNum, thread in enumerate(threads):
        thread.join()
    t2 = time.perf_counter()
    print(f"Time taken for a %s x %s x %s with Python MP was {t2 - t1:0.4f} sec for %s threads"%(n,n,n,noThreads))
    #print("my answer")
    #print(C)

