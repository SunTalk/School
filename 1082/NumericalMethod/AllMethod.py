from BisectionMethod import *
from FalsePositionMethod import *
from ModifyFalsePositionMethod import *
from SecantMethod import *
from NewtonMethod import *
from FixedPointMethod import *

outfile = open("out/output.out","w")
def DoMethod( fun, fundif, funG, mmin, mmax, out = outfile):

	ans,cnt = Bisection(fun,mmin,mmax,1e-8)
	print( "Bisection:           {:+15.10f} {:+15.10f} {:>5d}" .format(ans ,fun(ans),cnt) ,file = out)
	# print("Bisection")
	ans,cnt = FalsePosition(fun,mmin,mmax,1e-8)
	print( "FalsePosition:       {:+15.10f} {:+15.10f} {:>5d}" .format(ans ,fun(ans),cnt) ,file = out)
	# print("FalsePosition")
	ans,cnt = ModifyFalsePosition(fun,mmin,mmax,1e-8)
	print( "ModifyFalsePosition: {:+15.10f} {:+15.10f} {:>5d}" .format(ans ,fun(ans),cnt) ,file = out)
	# print("ModifyFalsePosition")
	ans,cnt = Secant(fun,mmin,mmax,1e-8)
	print( "Secant:              {:+15.10f} {:+15.10f} {:>5d}" .format(ans ,fun(ans),cnt) ,file = out)
	# print("Secant")
	ans,cnt = Newton(fun,fundif,mmin,mmax,1e-8)
	print( "Newton:              {:+15.10f} {:+15.10f} {:>5d}" .format(ans ,fun(ans),cnt) ,file = out)
	# print("Newton")
	ans,cnt = FixPoint(funG,mmin,mmax,1e-8)
	print( "FixPoint:            {:+15.10f} {:+15.10f} {:>5d}" .format(ans ,fun(ans),cnt) ,file = out)
	# print("FixPoint")