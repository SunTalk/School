import random

def Secant(fun, mmin, mmax, epsilon):

	a = random.uniform(mmin, mmax)
	b = random.uniform(mmin, mmax)

	cnt = 0
	while( abs(a-b) >= epsilon ):
		cnt += 1
		x = (a*fun(b)-b*fun(a))/(fun(b)-fun(a))
		a = b
		b = x

	return b,cnt
