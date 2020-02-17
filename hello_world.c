# include <stdlib.h>
# include <stdio.h>
# include "omp.h"

int main ()
{
# pragma omp parallel
	{
	printf (" hello   world  \n");
 	}
}
/*
To compile
14 % gcc -fopenmp -lgomp hello_world .c -o hello_world
To run use :
export OMP_NUM_THREADS =8 # <number of threads to use >
% ./ hello_world
*/
