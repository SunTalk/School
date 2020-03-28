from math import *
from AllMethod import *

def Afun(x) :
	if( abs(x) > 100 ):
		return inf
	return (exp(x)-3*x*cos(2*x)-8.3)
def Afundif(x) :
	if( abs(x) > 100 ):
		return inf
	return (exp(x)-3*cos(2*x)-6*x*sin(2*x))
def AfunG(x) :
	if( abs(x) > 100 ):
		return inf
	return (8.3-exp(x))/(3*cos(2*x))
mmin = -10
mmax = 2
Afile = open("out/Afile.data","w")
for i in range(0,10):
	print("-----------------------------------------------------------",file=Afile)
	print("  Method                     X              F(x)      Times",file=Afile)
	DoMethod(Afun,Afundif,AfunG,mmin,mmax,Afile)
	print("-----------------------------------------------------------",file=Afile)

def Bfun(x) :
	if( abs(x) > 100 ):
		return inf
	return (exp(x*sin(x))-x*cos(2*x)-2.8)
def Bfundif(x) :
	if( abs(x) > 100 ):
		return inf
	return (exp(x*sin(x))*(sin(x)+x*cos(x))-cos(2*x)+2*x*sin(x))
def BfunG(x) :
	if( abs(x) > 100 ):
		return inf
	return ((exp(x*sin(x))-2.8)/cos(2*x))
mmin = -10
mmax = 10
Bfile = open("out/Bfile.data","w")
for i in range(0,10):
	print("-----------------------------------------------------------",file=Bfile)
	print("  Method                     X              F(x)      Times",file=Bfile)
	DoMethod(Bfun,Bfundif,BfunG,mmin,mmax,Bfile)
	print("-----------------------------------------------------------",file=Bfile)

def Cfun(x) :
	return ((sin(2*x)+cos(2*x))-x*sin(x))
def Cfundif(x) :
	return (2*cos(2*x)-2*sin(2*x)-sin(x)-x*cos(x))
def CfunG(x) :
	return ((sin(2*x)+cos(2*x))/sin(x))
mmin = -10
mmax = 10
Cfile = open("out/Cfile.data","w")
for i in range(0,10):
	print("-----------------------------------------------------------",file=Cfile)
	print("  Method                     X              F(x)      Times",file=Cfile)
	DoMethod(Cfun,Cfundif,CfunG,mmin,mmax,Cfile)
	print("-----------------------------------------------------------",file=Cfile)

def Dfun(x) :
	return (sin((x**2)*cos(x))-x*cos(x))
def Dfundif(x) :
	return 2*x*cos((x**2)*cos(x))*cos(x)-(x**2)*cos((x**2)*cos(x))*sin(x)-cos(x)+x*sin(x)
def DfunG(x) :
	return ((sin((x**2)*cos(x)))/cos(x))

mmin = -10
mmax = 10
Dfile = open("out/Dfile.data","w")
for i in range(0,10):
	print("-----------------------------------------------------------",file=Dfile)
	print("  Method                     X              F(x)      Times",file=Dfile)
	DoMethod(Dfun,Dfundif,DfunG,mmin,mmax,Dfile)
	print("-----------------------------------------------------------",file=Dfile)
