from math import *
from AllMethod import *

def EazyFun(x) :
	return (x-3)*(x+1)
def EazyFundif(x) :
	return (2*x-2)
def EazyFunG(x) :
	return 3/(x-2)
mmin = -10
mmax = 10
EazyFile = open("out/EazyFile.data","w")
for i in range(0,10):
	print("-----------------------------------------------------------",file=EazyFile)
	print("  Method                     X              F(x)      Times",file=EazyFile)
	DoMethod(EazyFun,EazyFundif,EazyFunG,mmin,mmax,EazyFile)
	print("-----------------------------------------------------------",file=EazyFile)

def Afun(x) :
	return (exp(x)-3*x*cos(2*x)-8.3)
def Afundif(x) :
	return (exp(x)-3*cos(2*x)-6*x*sin(2*x))
def AfunG(x) :
	return (8.3-exp(x))/(3*cos(2*x))
mmin = -10
mmax = 2
Afile = open("out/Afile.data","w")
for i in range(0,10):
	print("-----------------------------------------------------------",file=Afile)
	print("  Method                     X              F(x)      Times",file=Afile)
	DoMethod(Afun,Afundif,AfunG,mmin,mmax,Afile)
	print("-----------------------------------------------------------",file=Afile)

# def Bfun(x) :
# 	return (exp(x*sin(x))-x*cos(2*x)-2.8)
# def Bfundif(x) :
# 	return (exp(x*sin(x))*(sin(x)+x*cos(x))-cos(2*x)+2*x*sin(x))
# def BfunG(x) :
# 	return (log((cos(2*x)-2*x*sin(x))/(sin(x)+x*cos(x)))/sin(x))
# mmin = -10
# mmax = 10
# Bfile = open("out/Bfile.data","w")
# for i in range(0,10):
# 	print("-----------------------------------------------------------",file=Bfile)
# 	print("  Method                     X              F(x)      Times",file=Bfile)
# 	DoMethod(Bfun,Bfundif,BfunG,mmin,mmax,Bfile)
# 	print("-----------------------------------------------------------",file=Bfile)

# def Cfun(x) :
# 	return (x-3)*(x+1)
# def Cfundif(x) :
# 	return (2*x-2)
# def CfunG(x) :
# 	return 3/(x-2)
# mmin = -10
# mmax = 10
# Cfile = open("out/Cfile.data","w")
# for i in range(0,10):
# 	print("-----------------------------------------------------------",file=Cfile)
# 	print("  Method                     X              F(x)      Times",file=Cfile)
# 	DoMethod(Cfun,Cfundif,CfunG,mmin,mmax,Cfile)
# 	print("-----------------------------------------------------------",file=Cfile)

# def Dfun(x) :
# 	return (x**2-x-11)
# def Dfundif(x) :
# 	return (2*x-1)
# def DfunG(x) :
# 	return (5/(x+2))+3
# mmin = -10
# mmax = 10
# Dfile = open("out/Dfile.data","w")
# for i in range(0,10):
# 	print("-----------------------------------------------------------",file=Dfile)
# 	print("  Method                     X              F(x)      Times",file=Dfile)
# 	DoMethod(Dfun,Dfundif,DfunG,mmin,mmax,Dfile)
# 	print("-----------------------------------------------------------",file=Dfile)
