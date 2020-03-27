import random

def FixPoint(fun, mmin, mmax, epsilon):

	x = random.randint(mmin, mmax)
	old = x+2*epsilon

	cnt = 0
	while( abs(x-old) >= epsilon ):
		cnt += 1
		
		old = x
		x = fun(x)

	return x,cnt