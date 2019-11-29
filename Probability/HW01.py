import matplotlib.pyplot as plt
import random

num = list()
x = list()
y = list()
MAXN = 100000
AVG = 10

for i in range(130,160+1) :
	x.append(i)
	y.append(0)

for i in range(MAXN) :
	num.append(random.randint(130,160))
	y[(num[i]-130)] += 1

plt.title('All')
plt.xlabel('Height')
plt.ylabel('number')
plt.bar(x,y)
plt.savefig('All.png')
plt.close()

for k in range(1,12):
	for i in range(len(y)) :
		y[i] = 0

	for i in range(MAXN//AVG):
		now = 0
		for j in range(AVG):
			now += num[i*AVG+j]
		now = now//AVG
		y[(now-130)]+= 1

	plt.title('AVG'+str(AVG))
	plt.xlabel('Height')
	plt.ylabel('number')
	plt.ylim(0,1500)
	plt.bar(x,y)
	plt.savefig('AVG'+str(AVG)+'.png')
	plt.close()

	AVG += 5

