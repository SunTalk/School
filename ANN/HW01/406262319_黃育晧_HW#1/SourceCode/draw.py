import numpy as np
import matplotlib.pyplot as plt
TraningFile = open("training_data2.txt","r")

def Draw() :

	for i in TraningFile.readlines() :
		S,T,W,K = i.split()
		if K == "W" :
			plt.scatter(float(S),float(T),c='r')
		if K == "B" :
			plt.scatter(float(S),float(T),c='g')
		if K == "P" :
			plt.scatter(float(S),float(T),c='b')
		if K == "O" :
			plt.scatter(float(S),float(T),c='black')

	plt.savefig("2C.png")

if __name__ == "__main__":
	Draw()