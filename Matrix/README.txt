Data Intensive Computing in Computer Science
Laboratory 1
Alice Drozdov (1370992), Marguerite Strydom(1090709), Sansha Gupta (1619757)

Build Tool: virtualenv

The source code has been seperated according to the dimensions and type of parallelisation. 
The source code files are as follows:
2DMatrixOri.py - 1D Matrix multiplication with one thread i.e. sequential programming
2DMatrixOpenMP.py - 2D Matrix multiplication using OpenMP - Number of threads must be specified
2DMatrixPThread.py - 2D Matrix multiplication using PThreads - Number of threads must be specified 
3DMatrix.py - 3D Matrix multiplication with one thread i.e. sequential programming. 
3DMatrixOpenMP.py - 3D Matrix multiplication using OpenMP - Number of threads must be specified
3DMatrixPThread.py - 3D Matrix multiplication using PThreads - Number of threads must be specified 

The program can be run and compiled using the runTest.sh bash file.
It specifies the number of threads from 1 to 4 and provides the execution time for the 2D and 3D multiplicaiton, 
using the specified number of threads for paralellisation. It also uses matrices with an increasing number of 
elements to represent how scaling and the number of threads impacts paralellisation. The script shows the execution
time taken for matrix multiplication using PythonMP and Threading. 

These can be built and compiled using 

The program can be run using the runTest.sh bash file. 
This file outputs the times for all the threads and dimensions. 

To run any of the files above: 
-For file with no parallelisation use command: 
    $python3 <filename>
-For file with parallelisation, use command:
    %python3 <filename> <no. of threads>
