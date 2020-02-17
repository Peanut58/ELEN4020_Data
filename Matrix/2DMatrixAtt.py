import array as arr
import numpy as np

#matrix multiplication C = AB
np.random.seed()
arr_A = np.zeros((1,3),dtype = np.ndarray)
arr_B = np.zeros((1,3),dtype = np.ndarray)
count = 2
loc = 0
#initialise array A and array B with 3 matrices with size 10, 20 and 30
while count <=6:
	arr_a = np.random.randint(0,100, size=(count,count))
	arr_b = np.random.randint(0,100, size=(count,count))
	print(arr_a)
	print(arr_b)
	arr_A[0,loc] = [arr_a]
	arr_B[0,loc] = [arr_b]
	loc += 1
	count += 2

#test to see if output is correct
#print("Array A at first location")
#print (arr_A[0,0])
#print("Array A first index of array at first location") 
#print(arr_A[0][0][0][0])
#print("Array A at second location")
#print (arr_A[0,1])
#print("Array A at third location")
#print (arr_A[0,2])

#2D matrix multiplication. Answers will be stored in matrix C
arr_C = np.zeros((1,3), dtype = np.ndarray)
r = 0

for r in range(2):
	for i in range((len(arr_B[0,0])):
		for j in range(len(arr_A[0,0])):
			for k in range(len(arr_A[0,0])):
				arr_C[0,r,i,j] += arr_A[0][r][i][k]*arr_B[0][r][k][j]
				k += 1
			j += 1
		i += 1
	#arr_C[0,r] = arr_c
	r += 1

print("Array C in first location")
print(arr_C[0,0])


