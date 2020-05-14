import random
import math
from DATA import *
from Lagrange import *
from Newton import *
from GregoryForward import *
from GregoryBackward import *

def fun(x) :
	return ((math.sin(2*x)+math.cos(2*x))-x*math.sin(x))

DataX = [[(2.5+i*0.25) for i in range(21)]]
DataY = [[fun(i) for i in DataX[0]]]
DataNum = 10

for i in range(DataNum):
    DataX_ = list()
    DataY_ = list()
    DataX_.append(2.5)
    DataX_.append(7.5)
    for j in range(20):
        x = random.uniform(2.5,7.5) 
        DataX_.append(x)
    DataX_.sort()
    for j in DataX_ :
        DataY_.append(fun(j))
    DataX.append(DataX_)
    DataY.append(DataY_)

print("Lagrange...")
for i in range(DataNum):    
    Lagrangefun(DataX[i],DataY[i], "Function"+str(i+1))
Lagrangefun(DataSetX,DataSetY, "DataSetOne")
Lagrangefun(DataSetX_,DataSetY_, "DataSetTwo")

print("Newton...")
for i in range(DataNum):
    Newtonfun(DataX[i],DataY[i], "Function"+str(i+1))
Newtonfun(DataSetX,DataSetY, "DataSetOne")
Newtonfun(DataSetX_,DataSetY_, "DataSetTwo")

print("GregoryForward")
GregoryForwardfun(DataX[0],DataY[0],"Function")
GregoryForwardfun(DataSetX_,DataSetY_, "DataSetTwo")

print("GregoryBackward")
GregoryBackwardfun(DataX[0],DataY[0],"Function")
GregoryBackwardfun(DataSetX_,DataSetY_, "DataSetTwo")








