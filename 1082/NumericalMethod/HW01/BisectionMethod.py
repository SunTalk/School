import random

def Bisection(fun, mmin, mmax, epsilon):
	
	a = 1
	while( fun(a) < 0 ):
		a = random.randint(mmin, mmax)
	b = 1
	while( fun(b) > 0 ):
		b = random.randint(mmin, mmax)

	cnt = 0
	while( abs(a-b) >= epsilon ):
		cnt += 1
		
		c = (a+b)/2
		if( fun(c) == 0 ):
			return c,cnt
		if( fun(a)*fun(c) < 0 ):
			b = c
		else :
			a = c

	return (a+b)/2,cnt

