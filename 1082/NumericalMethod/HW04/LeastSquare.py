import matplotlib.pyplot as plt
import numpy as np

def LeastSquare(dataX, dataY) :
	
	OUT = open("./out/output.out","w")

	Error = list()
	flag = True

	for K in range(2,len(dataX)+6) :

		print("P{}(X)".format(K), file=OUT)

		A = np.zeros(K*K).reshape(K,K)
		B = np.zeros(K)

		for i in range(K) :
			for j in range(K) :
				for X in dataX :
					A[i,j] += X**(i+j)
		for i in range(K) :
			for j in range(len(dataX)) :
				B[i] += dataY[j]*(dataX[j]**i)

		X = np.linalg.solve(A,B)

		error = 0
		N = len(dataY)

		NewAns = list()
		for i in range(N) :
			ans = 0
			for j in range(K) :
				ans += X[j]*(dataX[i]**j)
			NewAns.append(ans)
		
		print("[ ",end="",file=OUT)
		for x in X :
			print("{0:3.6f}".format(x),end=", ",file=OUT)
		print("]",file=OUT)


		for i in range(N) :
			error += (NewAns[i]-dataY[i])**2

		print("Error : {0:3.6f}".format(error),file=OUT)

		if len(Error) > 0 :
			if Error[-1]/error < 2.0 :
				print("{} is the Best Choise".format(K-1),file=OUT)
				flag = False
		print("-----",file=OUT)

		Error.append(error)

		# draw pic
		plt.cla()
		plt.clf()
		plt.title("LeastSquare"+str(K))

		ORI, = plt.plot(dataX,dataY,'b:')
		RES, = plt.plot(dataX,NewAns,'r:')
		plt.legend([RES,ORI],["Result","Origin"])

		y_ticks = np.arange(0.5,2.6,0.1)
		x_ticks = np.arange(0,10,1)
		plt.xticks(x_ticks)
		plt.yticks(y_ticks)
		plt.xlim((-1,10))
		plt.ylim((0.4,2.6))
		plt.savefig("./out/P"+str(K)+".png")
		# end draw pic

	MMIN = 10000.0
	IDX = -1
	for E in range(len(Error)) :
		if Error[E] < MMIN :
			MMIN = Error[E]
			IDX = E
	print("MIN Error is {:d} , Error = {:3.6f}".format(IDX+2,Error[IDX]),file=OUT)
