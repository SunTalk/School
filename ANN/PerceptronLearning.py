import numpy as np
import math
import random
import time

##############################
########## TwoNeuron #########
##############################

# Weight = np.array([
# 	[0.0, 0.0, 0.0],
# 	[0.0, 0.0, 0.0]
# ])
# Biases = np.array([
# 	[0.0],[0.0]
# ])

# W = np.array([[0.0],[0.0]])
# B = np.array([[0.0],[1.0]])
# P = np.array([[1.0],[0.0]])
# O = np.array([[1.0],[1.0]])

# OutputFile = open("TwoNeuron.out", "a")
# def init() :
# 	for i in range(2) :
# 		for j in range(3):
# 			Weight[i][j] = random.uniform(-10.0, 10.0)
# 	for i in range(2) :
# 		Biases[i] = random.uniform(-10.0, 10.0)
# 	# give Weight and Biases random initial values

##############################
######### FourNeuron #########
##############################

Weight = np.array([
	[0.0, 0.0, 0.0],
	[0.0, 0.0, 0.0],
	[0.0, 0.0, 0.0],
	[0.0, 0.0, 0.0]
])
Biases = np.array([
	[0.0],[0.0],[0.0],[0.0]
])

W = np.array([[1.0],[0.0],[0.0],[0.0]])
B = np.array([[0.0],[1.0],[0.0],[0.0]])
P = np.array([[0.0],[0.0],[1.0],[0.0]])
O = np.array([[0.0],[0.0],[0.0],[1.0]])

OutputFile = open("FourNeuron.out", "a")
def init() :
	for i in range(4) :
		for j in range(3):
			Weight[i][j] = random.uniform(-10.0, 10.0)
	for i in range(4) :
		Biases[i] = random.uniform(-10.0, 10.0)
	# give Weight and Biases random initial values

############################################################
###### annotation one of upon can change Neuron number #####
############################################################

TraningFile = open("training_data.txt","r")
TestFile = open("testing_data.txt","r")

Data = list()
Test = list()
Result = list()

ErrNum = 0
TotalError = 0
Epoch = 0
EpochLimit = 10000
LRate = 1

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
				Weight = Weight + LRate*e.dot(i[0].T)
				Biases = Biases + LRate*e
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

	
	for i in TestFile.readlines() :
		S,T,W = i.split()
		Obj = np.array([[float(S)],[float(T)],[float(W)]])
		Test.append(Obj)
	# read Test Data

	ErrNum = 0
	kase = 1
	Result.clear()
	for i in Test :
		now = Weight.dot(i) + Biases
		for j in now :
			j[0] = hardlim(j[0])
		res = Decide(now)
		if res == "Error" :
			ErrNum += 1
		Result.append([kase,res])
		kase += 1
	# run Test data
	TotalError += ErrNum

def TestPrint() :

	for i in Result:
		print("{}[{}]".format(i[0], i[1]), end = " " , file = OutputFile)
		if i[0]%10 == 0 :
			print("", file=OutputFile)
	print("\nError Number : {}".format(ErrNum), file=OutputFile)
	# print results for Test data

def WBprint() :
	print("Weight:",file = OutputFile)
	print(Weight,file = OutputFile)
	print("Biases:",file = OutputFile)
	print(Biases,file = OutputFile)
	# ouput the data of Weight and Biases

def CheckFile() :
	if len(Biases) == 2 :
		OutputFile = open("TwoNeuron.out", "w")
	if len(Biases) == 4 :
		OutputFile = open("FourNeuron.out", "w")
	# let draw.py can't clear the file

if __name__ == "__main__":
	CheckFile()
	TotalTime = 0.0
	SetRange = 1000
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
		print("Learning Rate:",end = " " ,file = OutputFile)
		print(LRate,file = OutputFile)
		
		print("\nEnd Epoch: {}".format(Epoch), file=OutputFile)
		print("Speed: {}\n".format(tEnd - tStart), file=OutputFile)
		
		StartTest()
		TestPrint()
		print("End Test: {}".format(i), file = OutputFile)
		print("--------------------------------------------------", file = OutputFile)
		
		# if i%10 == 0 :
		# 	LRate -= 0.01

	print("Total Error: {}".format(TotalError), file = OutputFile)
	print("Avg Error: {}".format(TotalError/SetRange), file = OutputFile)
	print("Total Time: {} sec".format(TotalTime), file = OutputFile)
	print("Avg Time: {} sec".format(TotalTime/SetRange), file = OutputFile)
