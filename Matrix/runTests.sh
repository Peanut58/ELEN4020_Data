#!/bin/bash

#run a programs automatically
for noThreads in 1 2 3 4
do
    echo $noThreads
    python3 2DMatrixOpenMP.py $noThreads
    python3 2DMatrixPThread.py $noThreads
    python3 3DMatrixOpenMP.py $noThreads
    python3 3DMatrixPThread.py $noThreads
done