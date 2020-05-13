import numpy as np
import random
import time

num = [2,3,5,10,50,100,300,500,800,1000,2000,4000]

OUT = open("data.out","w")
TIME = open("time.out","w")

for N in num:

	

	# print("* {}".format(N),file = OUT)

	A = np.zeros(N*N).reshape(N,N)
	B = np.zeros(N)

	tRs = time.time()
	for i in range(N):
		for j in range(N):
			A[i,j] = random.randint(-10,10)
		B[i] = random.randint(-10,10)
	tRe = time.time()

	if N <= 100 :
		for i in range(N):
			print("$",end="",file=OUT)
			for j in range(N):
				if A[i][j] >= 0 and j != 0 :
					print("+",end="",file=OUT) 
				print("{}X_{{{}}}".format(A[i,j],j),end="",file=OUT)
			print(" = {}$".format(B[i]),file=OUT)

	tStart = time.time()
	X = np.linalg.solve(A,B)
	tEnd = time.time()

	if N <= 100 :
		for i in range(N):
			print("$X_{{{}}} = {:.6f}$".format(i,X[i]),file=OUT)
		print("---------------",file = OUT)

	print("{:>4d}".format(N),end=" : ",file=TIME)
	print("{:.6f},{:.6f}".format((tEnd - tStart),(tRe-tRs)),file=TIME)
	print(N)
