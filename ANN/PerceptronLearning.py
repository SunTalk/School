import numpy as np
import math
import random
import time

##############################
########## TwoNeuron #########
##############################

Weight = np.array([
	[0.0, 0.0, 0.0],
	[0.0, 0.0, 0.0]
])
Biases = np.array([
	[0.0],[0.0]
])

W = np.array([[0.0],[0.0]])
B = np.array([[0.0],[1.0]])
P = np.array([[1.0],[0.0]])
O = np.array([[1.0],[1.0]])

OutputFile = open("TwoNeuron.out", "w")
def init() :
	for i in range(2) :
		for j in range(3):
			Weight[i][j] = random.uniform(-10.0, 10.0)
	for i in range(2) :
		Biases[i] = random.uniform(-10.0, 10.0)
	# give Weight and Biases random initial values

##############################
######### FourNeuron #########
##############################

# Weight = np.array([
# 	[0.0, 0.0, 0.0],
# 	[0.0, 0.0, 0.0],
# 	[0.0, 0.0, 0.0],
# 	[0.0, 0.0, 0.0]
# ])
# Biases = np.array([
# 	[0.0],[0.0],[0.0],[0.0]
# ])

# W = np.array([[1.0],[0.0],[0.0],[0.0]])
# B = np.array([[0.0],[1.0],[0.0],[0.0]])
# P = np.array([[0.0],[0.0],[1.0],[0.0]])
# O = np.array([[0.0],[0.0],[0.0],[1.0]])

# OutputFile = open("FourNeuron.out", "w")
# def init() :
# 	for i in range(4) :
# 		for j in range(3):
# 			Weight[i][j] = random.uniform(-10.0, 10.0)
# 	for i in range(4) :
# 		Biases[i] = random.uniform(-10.0, 10.0)
	# give Weight and Biases random initial values

############################################################
###### annotation one of upon can change Neuron number #####
############################################################

TraningFile = open("training_data.txt","r")
TestFile = open("testing_data.txt","r")

Data = list()
Test = list()
TotalError = 0
EpochLimit = 10000

def Turn_to_Martix(k) :
	if k == "W" :
		return W
	if k == "B" :
		return B
	if k == "P" :
		return P
	if k == "O" :
		return O

def hardlim(x):
	if x >= 0.0 :
		return 1.0
	return 0.0
	# hardlim fun

def NeedUpdate(e):
	for i in e :
		if i != 0.0 :
			return True
	return False
	# check if it need to update the Weight and Biases

Epoch = 0
def Traning() :
	global Weight
	global Biases
	global Epoch

	for i in TraningFile.readlines() :
		S,T,W,K = i.split()
		Obj = np.array([[float(S)],[float(T)],[float(W)]])
		Ans = Turn_to_Martix(K)
		Data.append([Obj,Ans])
	# read Training Data

	Epoch = 1;
	Completed = False
	while True :
		if Epoch > EpochLimit or Completed:
			break
		Epoch += 1
		Completed = True
		for i in Data :
			now = Weight.dot(i[0]) + Biases
			for j in now :
				j[0] = hardlim(j[0])
			e = i[1]-now
			if NeedUpdate(e) :
				Completed = False
				Weight = Weight + e.dot(i[0].T)
				Biases = Biases + e
	# Traning


def Decide(K) :
	if np.array_equal(K,W):
		return "W"
	if np.array_equal(K,B):
		return "B"
	if np.array_equal(K,P):
		return "P"
	if np.array_equal(K,O):
		return "O"
	return "Error"
	# Decide which one it is
	# if none of them return Error

def StartTest() :
	global TotalError

	kase = 1;
	for i in TestFile.readlines() :
		S,T,W = i.split()
		Obj = np.array([[float(S)],[float(T)],[float(W)]])
		Test.append(Obj)
	# read Test Data

	ErrNum = 0
	for i in Test :
		now = Weight.dot(i) + Biases
		for j in now :
			j[0] = hardlim(j[0])
		result = Decide(now)
		if result == "Error" :
			ErrNum += 1
		print("{}[{}]".format(kase, result), end = " " , file = OutputFile)
		if kase%10 == 0 :
			print("", file=OutputFile)
		kase += 1
	# run Test data and print it
	print("\nError Number : {}".format(ErrNum), file=OutputFile)
	TotalError += ErrNum

def WBprint() :
	print("Weight:",file = OutputFile)
	print(Weight,file = OutputFile)
	print("Biases:",file = OutputFile)
	print(Biases,file = OutputFile)
	# ouput the data of Weight and Biases


if __name__ == "__main__":
	TotalTime = 0.0
	SetRange = 100
	for i in range(1,SetRange+1):

		print(i) # monitor progress
		print("Test {}:".format(i), file = OutputFile)

		init()
		print("\nInitial:", file = OutputFile)
		WBprint()

		tStart = time.time()
		Traning()
		tEnd = time.time()
		TotalTime += (tEnd - tStart)
		print("\nAfter Traning:", file = OutputFile)
		WBprint()

		print("\nEnd Epoch: {}".format(Epoch), file=OutputFile)
		print("Speed: {}".format(tEnd - tStart), file=OutputFile)
		StartTest()
		print("End Test: {}".format(i), file = OutputFile)
		print("--------------------------------------------------", file = OutputFile)
	
	print("Total Error: {}".format(TotalError), file = OutputFile)
	print("Avg Error: {}".format(TotalError/SetRange), file = OutputFile)
	print("Total Time: {} sec".format(TotalTime), file = OutputFile)
	print("Avg Time: {} sec".format(TotalTime/SetRange), file = OutputFile)
