import numpy as np
import sys
import math
import random
import time

OutputFile = open("TwoNeuron.out", "a")
TraningFile = open("training_data2.txt","r")
TestFile = open("testing_data2.txt","r")

Data = list()
Test = list()
Result = list()

Weight = np.array([])
Biases = np.array([])
W = np.array([])
B = np.array([])
P = np.array([])
O = np.array([])

ErrNum = 0
TotalError = 0
Epoch = 0
EpochLimit = 10000
LRate = 1

def init() :
	for i in range(len(Weight)) :
		for j in range(len(Weight[i])):
			Weight[i][j] = random.uniform(-10.0, 10.0)
	for i in range(len(Biases)) :
		Biases[i] = random.uniform(-10.0, 10.0)
	# give Weight and Biases random initial values

def read_file():
	
	for i in TraningFile.readlines() :
		S,T,W,K = i.split()
		Obj = np.array([[float(S)],[float(T)],[float(W)]])
		if sys.argv[1] == '2N2C' or sys.argv[1] == '4N2C':
			Obj = np.array([[float(S)],[float(T)]])
		Ans = Turn_to_Martix(K)
		Data.append([Obj,Ans])
	# read Training Data
	for i in TestFile.readlines() :
		S,T,W = i.split()
		Obj = np.array([[float(S)],[float(T)],[float(W)]])
		if sys.argv[1] == '2N2C' or sys.argv[1] == '4N2C':
			Obj = np.array([[float(S)],[float(T)]])
		Test.append(Obj)
	# read Test Data

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
	# read which one want to run
	# then change data and file
	global OutputFile
	global TraningFile
	global TestFile
	
	global Weight
	global Biases
	global W
	global B
	global P
	global O

	if len(sys.argv) == 1 :
		return 0
	if sys.argv[1] == '2N' :
		OutputFile = open("TwoNeuron.out", "w")
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
	if sys.argv[1] == '4N' :
		OutputFile = open("FourNeuron.out", "w")
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
	if len(sys.argv) == 3 and sys.argv[2] == '0' :
		TraningFile = open("training_data1.txt","r")
		TestFile = open("testing_data1.txt","r")
		if sys.argv[1] == '2N2C' :
			OutputFile = open("TwoNeuron_Data1.out", "w")
			Weight = np.array([
				[1.0, 0.0],
				[0.0, 1.0]
			])
			Biases = np.array([
				[1.0],[1.0]
			])
			W = np.array([[0.0],[0.0]])
			B = np.array([[0.0],[1.0]])
			P = np.array([[1.0],[0.0]])
			O = np.array([[1.0],[1.0]])
		if sys.argv[1] == '4N2C' :
			OutputFile = open("FourNeuron_Data1.out", "w")
			Weight = np.array([
				[0.0, 0.0],
				[0.0, 0.0],
				[0.0, 0.0],
				[0.0, 0.0]
			])
			Biases = np.array([
				[0.0],[0.0],[0.0],[0.0]
			])
			W = np.array([[1.0],[0.0],[0.0],[0.0]])
			B = np.array([[0.0],[1.0],[0.0],[0.0]])
			P = np.array([[0.0],[0.0],[1.0],[0.0]])
			O = np.array([[0.0],[0.0],[0.0],[1.0]])
	elif sys.argv[1] == '2N2C' :
		OutputFile = open("TwoNeuron_twoComponents.out", "w")
		Weight = np.array([
			[0.0, 0.0],
			[0.0, 0.0]
		])
		Biases = np.array([
			[0.0],[0.0]
		])
		W = np.array([[0.0],[0.0]])
		B = np.array([[0.0],[1.0]])
		P = np.array([[1.0],[0.0]])
		O = np.array([[1.0],[1.0]])
	elif sys.argv[1] == '4N2C' :
		OutputFile = open("FourNeuron_twoComponents.out", "w")
		Weight = np.array([
			[0.0, 0.0],
			[0.0, 0.0],
			[0.0, 0.0],
			[0.0, 0.0]
		])
		Biases = np.array([
			[0.0],[0.0],[0.0],[0.0]
		])

		W = np.array([[1.0],[0.0],[0.0],[0.0]])
		B = np.array([[0.0],[1.0],[0.0],[0.0]])
		P = np.array([[0.0],[0.0],[1.0],[0.0]])
		O = np.array([[0.0],[0.0],[0.0],[1.0]])
	
	return 1

def main(SetRange) :
	global LRate
	TotalTime = 0.0
	read_file()
	for i in range(1,SetRange+1):

		print(i) # monitor progress
		print("Test {}:".format(i), file = OutputFile)

		if len(sys.argv) < 3 :
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
		
		if i%10 == 0 :
			LRate -= 0.01

	print("Total Error: {}".format(TotalError), file = OutputFile)
	print("Avg Error: {}".format(TotalError/SetRange), file = OutputFile)
	print("Total Time: {} sec".format(TotalTime), file = OutputFile)
	print("Avg Time: {} sec".format(TotalTime/SetRange), file = OutputFile)

if __name__ == "__main__":
	if CheckFile() :
		if len(sys.argv) == 3 and sys.argv[2] != '0' :
			main(int(sys.argv[2]))
		else:
			main(1)
	else :
		print("You need enter which one you want to run")