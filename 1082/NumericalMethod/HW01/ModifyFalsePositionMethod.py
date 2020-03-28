import random

def ModifyFalsePosition(fun, mmin, mmax, epsilon):

	a = 1
	while( fun(a) < 0 ):
		a = random.randint(mmin, mmax)
	b = 1
	while( fun(b) > 0 ):
		b = random.randint(mmin, mmax)

	old = a
	new = b
	Fa = fun(a)
	Fb = fun(b)

	cnt = 0
	while( abs(new-old) >= epsilon ) :
		cnt += 1

		old = new
		new = (a*Fb-b*Fa)/(Fb-Fa)
		Fc = fun(new)

		if( Fc == 0 ) :
			return new,cnt

		if( Fa*Fc < 0 ):
			b = new
			Fa = Fa/2
			Fb = fun(b)
		else :
			a = new
			Fa = fun(a)
			Fb = Fb/2

	return new,cnt



