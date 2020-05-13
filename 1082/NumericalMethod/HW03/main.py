from math import *
from Lagrange import *

DataX = list()
DataY = list()

def fun(x) :
	return ((sin(2*x)+cos(2*x))-x*sin(x))

x = 2.5
for i in range(21):
    DataX.append(x)
    DataY.append(fun(x))
    x += 0.25

OUT = open("out/Lagrange.data","w")

Lagrange(DataX,DataY,fun)


