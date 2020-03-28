import random

def FalsePosition(fun, mmin, mmax, epsilon):

	a = 1
	while( fun(a) < 0 ):
		a = random.randint(mmin, mmax)
	b = 1
	while( fun(b) > 0 ):
		b = random.randint(mmin, mmax)

	old = a
	new = b

	cnt = 0
	while( abs(new-old) >= epsilon ) :
		cnt+=1
		
		old = new
		new = (a*fun(b)-b*fun(a))/(fun(b)-fun(a))

		if( fun(new) == 0 ) :
			return new,cnt

		if( fun(a)*fun(new) < 0 ):
			b = new
		else :
			a = new

	return new,cnt



