import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PerceptronLearning import *

def FinalChart() :
	fig = plt.figure()
	ax = Axes3D(fig)
	for i in Test :
		now = Weight.dot(i) + Biases
		for j in now :
			j[0] = hardlim(j[0])
		if Decide(now) == "W" :
			ax.scatter(i[0], i[1], i[2],c='r')
		if Decide(now) == "B" :
			ax.scatter(i[0], i[1], i[2],c='g')
		if Decide(now) == "P" :
			ax.scatter(i[0], i[1], i[2],c='b')
		if Decide(now) == "O" :
			ax.scatter(i[0], i[1], i[2],c='black')
	
	for i in range(len(Weight)) :
		X,Y = np.meshgrid(range(-8,8), range(-8,8))
		Z = (- Weight[i][0] * X - Weight[i][1] * Y - Biases[i]) * 1. / Weight[i][2]
		ax.plot_surface(X,Y,Z)

	ax.plot_surface(X,Y,Z)
	ax.set_xlabel('Shape')
	ax.set_ylabel('Texture')
	ax.set_zlabel('Weight')
	plt.show()

if __name__ == "__main__":
	init()
	Traning()
	StartTest()
	FinalChart()