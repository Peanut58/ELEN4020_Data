Data Intensive Computing in Computer Science
Laboratory 1
Alice Drozdov (1370992), Marguerite Strydom(1090709), Sansha Gupta (1619757)

Build Tool: virtualenv

The source code has been seperated according to the dimensions and type of parallelisation. 
The source code files are as follows:
2DMatrixOri.py - 1D Matrix multiplication with one thread
2DMatrixOpenMP.py - 2D Matrix multiplication using OpenMP - Number of threads must be specified
2DMatrixPThread.py - 2D Matrix multiplication using PThreads - Number of threads must be specified 
3DMatrix.py - 3D Matrix multiplication with one thread
3DMatrixOpenMP.py - 3D Matrix multiplication using OpenMP - Number of threads must be specified
3DMatrixPThread.py - 3D Matrix multiplication using PThreads - Number of threads must be specified 


These can be built and compiled using 

The program can be run using the runTest.sh bash file. 
This file outputs the times for all the threads and dimensions. 

To run any of the files above: 
-For file with no parallelisation use command: 
    $python3 <filename>
-For file with parallelisation, use command:
    %python3 <filename> <no. of threads>
