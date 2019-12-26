import math
import random

class Neuron(object):

	def __init__(self,weightNum):
		self.inputs = []
		self.weights = []
		self.bias = random.uniform(0.0, 1.0)
		self.output = 0
		self.delta = 0
		for i in range(weightNum):
			self.weights.append(random.uniform(0.0, 1.0))

	def sigmoid(x) :
		return 1/(1+math.exp(-x))

	def calOutput(self,inputs):
		self.output = 0
		self.inputs = inputs
		for i in range(len(self.weights)):
			self.output += self.weights[i] * inputs[i]
		self.output = sigmoid(self.output+self.bias)
		return self.output

	def update(self,learningRate):
		self.delta = self.output*(1-self.output)
		for i in range(len(self.weights)):
			self.weights[i] =  self.weights[i] - learningRate*self.inputs[i]*self.delta
		self.bias = self.bias - learningRate*self.delta

class NeuronLayer(object):

	def __init__(self,inputNum,neuronNum,bias = 1):
		self.neurons = []
		for i in range(neuronNum):
			n = Neuron(inputNum)
			n.bias = bias
			self.neurons.append(n)

	def feedForward(self,inputs):
		outputs = []
		for n in self.neurons:
			outputs.append(n.calOutput(inputs))
		return outputs

	def getDelta(self):
		return [n.delta for n in self.neurons]

	def update(self,learningRate):
		for n in self.neurons:
			n.update(learningRate)


