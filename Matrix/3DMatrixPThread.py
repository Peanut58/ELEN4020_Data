#Parallisation of 3D matrix multiplication using using threading

import numpy as np 
import time
import threading
import sys

#3D matrix multiplication. C = A*B
def rank3TensorMultPThread(A,B,C):
    if len(B) != len(A[0][0]):
        sys.exit('Matrix A and Matrix B cannot be multiplied due to incompatible dimensions')

    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(A[0][0])):
                for l in range(len(B)):
                    C[i][j][k] += A[i][j][l]*B[l][j][k]
    return C

#Array bounds
N = [10,20,30]
#set seed to ensure that new random numbers is always generated
np.random.seed()
noThreads = int(sys.argv[1])

for n in N:
    #generate A and B matrices with random numbers between 0 and n. Dimension is n*n*n. Generate an empty C matrix of dimention n*n*n
    A = np.random.randint(0, n, size=(n,n,n))
    B = np.random.randint(0, n, size=(n,n,n))
    C = np.zeros((n,n,n), dtype=int)
    
    #set up the array for thread management
    threads = []
    #start timer for timing matrix multiplication
    t1 = time.perf_counter()
    #start generating threads
    for threadNum in range(noThreads):
        #apply parallelisation to matrix multiplication
        x = threading.Thread(target=rank3TensorMultPThread, args=(A,B,C,))
        #add threads to array
        threads.append(x)
        #start parallelisation
        x.start()

    #join threads for management
    for threadNum, thread in enumerate(threads):
        thread.join()
    #end timer for timing matrix multiplication
    t2 = time.perf_counter()
    #calculate time of program execution
    print(f"Time taken for a %s x %s x %s with Python MP was {t2 - t1:0.4f} sec for %s threads"%(n,n,n,noThreads))

