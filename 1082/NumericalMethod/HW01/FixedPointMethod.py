import random
import math

def FixPoint(fun, mmin, mmax, epsilon):

	x = random.randint(mmin, mmax)
	old = x+2*epsilon

	cnt = 0
	while( abs(x-old) >= epsilon ):
		cnt += 1
		
		old = x
		x = fun(x)

		if( x == math.inf or cnt == 10000):
			return x,cnt


	return x,cnt