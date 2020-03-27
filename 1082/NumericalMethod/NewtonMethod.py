import random

def Newton(fun, fundif, mmin, mmax, epsilon):

	x = random.uniform(mmin, mmax)
	delta = -fun(x)/fundif(x)

	cnt = 0
	while( abs(delta) >= epsilon ):
		cnt += 1
		
		x += delta
		delta = -fun(x)/fundif(x)

		if cnt == 10000:
			return x,cnt

	return x,cnt
