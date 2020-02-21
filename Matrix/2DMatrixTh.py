import threading 
import numpy as np 

def rank2TensorMultOpenMP(A, B, C): 
    for i in range(0, len(A)):
        for j in range(0, len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    return C

N = [10,20,30]
for n in N:
    print("N is ",n)
    A = np.random.randint(0, 100, size=(n, n))
    B = np.random.randint(0, 100, size=(n, n))
    C = np.zeros((n, n), dtype=int)

    threads = []
    for threadNum in range(2):
        # print("thread number " , threadNum)
        x = threading.Thread(target=rank2TensorMultOpenMP, args=(A,B,C,))
        threads.append(x)
        # print(threading.enumerate())
        x.start()

    for threadNum, thread in enumerate(threads):
        thread.join()
    
        
