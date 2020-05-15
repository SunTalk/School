import random
import math
from DATA import *
from Lagrange import *
from Newton import *
from GregoryForward import *
from GregoryBackward import *
from OriFunction import *

def fun(x) :
	return ((math.sin(2*x)+math.cos(2*x))-x*math.sin(x))

DataX = []
DataY = []
DataNum = 3

for i in range(DataNum):
    DataX_ = list()
    DataY_ = list()
    for j in range(20):
        x = random.uniform(2.5,7.5) 
        DataX_.append(x)
    DataX_.sort()
    for j in DataX_ :
        DataY_.append(fun(j))
    DataX.append(DataX_)
    DataY.append(DataY_)

DataX.append([(2.5+i*0.25) for i in range(21)])
DataY.append([fun(i) for i in DataX[-1]])

DrawOriFun(fun,2,8,"(2~8)")
DrawOriFun(fun,1,8,"(1~8)")
DrawOriFun(fun,2,9,"(2~9)")
DrawOriFun(fun,0,10,"(0~10)")

print("Lagrange...")
for i in range(DataNum):
    Lagrangefun(DataX[i],DataY[i], 2, 8, "Function(2~8)"+str(i+1))
for i in range(DataNum):
    Lagrangefun(DataX[i],DataY[i], 1, 8, "Function(1~8)"+str(i+1))
for i in range(DataNum):
    Lagrangefun(DataX[i],DataY[i], 2, 9, "Function(2~9)"+str(i+1))
for i in range(DataNum):
    Lagrangefun(DataX[i],DataY[i], 0, 10, "Function(0~10)"+str(i+1))
Lagrangefun(DataSetX,DataSetY, 2.4, 8.1, "DataSetOne")
Lagrangefun(DataSetX_,DataSetY_, 2.4, 8.1, "DataSetTwo")

print("Newton...")
for i in range(DataNum):
    Newtonfun(DataX[i],DataY[i], 2, 8, "Function(2~8)"+str(i+1))
for i in range(DataNum):
    Newtonfun(DataX[i],DataY[i], 1, 8, "Function(1~8)"+str(i+1))
for i in range(DataNum):
    Newtonfun(DataX[i],DataY[i], 2, 9, "Function(2~9)"+str(i+1))
for i in range(DataNum):
    Newtonfun(DataX[i],DataY[i], 0, 10, "Function(0~10)"+str(i+1))
Newtonfun(DataSetX,DataSetY, 2.4, 8.1, "DataSetOne")
Newtonfun(DataSetX_,DataSetY_, 2.4, 8.1, "DataSetTwo")

print("GregoryForward...")
GregoryForwardfun(DataX[-1],DataY[-1], 2, 8, "Function(2~8)")
GregoryForwardfun(DataX[-1],DataY[-1], 1, 8, "Function(1~8)")
GregoryForwardfun(DataX[-1],DataY[-1], 2, 9, "Function(2~9)")
GregoryForwardfun(DataX[-1],DataY[-1], 0, 10, "Function(0~10)")

GregoryForwardfun(DataSetX_,DataSetY_, 2.4, 8.1, "DataSetTwo")

print("GregoryBackward...")
GregoryBackwardfun(DataX[-1],DataY[-1], 2, 8, "Function(2~8)")
GregoryBackwardfun(DataX[-1],DataY[-1], 1, 8, "Function(1~8)")
GregoryBackwardfun(DataX[-1],DataY[-1], 2, 9, "Function(2~9)")
GregoryBackwardfun(DataX[-1],DataY[-1], 0, 10, "Function(0~10)")

GregoryBackwardfun(DataSetX_,DataSetY_, 2.4, 8.1, "DataSetTwo")

