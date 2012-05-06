#!/usr/bin/python2 
import math
import copy
import random as r
from misc import *
#from bigfloat import *

#functions for the neural network including update, backprogation
#sigmoid, etc.

def sigmoid(value):
	#print "sigmoid: ", value
	return 1 / (1 + math.exp(- value))

def dsigmoid(value):
	return math.exp(- value) / ((math.exp(- value) + 1) * (math.exp(- value) + 1)) 

#update the network, w contains the weights
#v is a ragged array of values for each layer (including input)
def update(w,v):
	#prev = copy.deepcopy(v)
	n = len(v)
	for i in range(1,n): #each layer
		for j in range(len(v[i])): #node in each layer
			sum = 0
			for k in range(len(w[i][j])):
				for l in range(len(w[i][j][k])):
					#print "Update I: ", i,"J: ", j, "K: ", k,"L: ",l
					sum += sigmoid(v[k][l])*w[i][j][k][l]
			#print v
			v[i][j] = sum
			

#finds the mean squared error of the output for a given pattern
def error(output,desired):
	error = 0
	n = len(output)
	for i in range(n):
		error += ((desired[i] - sigmoid(output[i])) * (desired[i] - sigmoid(output[i])))
	return error

#parameters are lists
def backpropagate(v,desired,w,gradient):
	for i in range(len(v[2])):
		gradient[2][i] = (desired[i] - sigmoid(v[2][i]))*dsigmoid(v[2][i])
	for i in range(len(v[1])):
		sum  = 0
		for j in range(len(v[2])):
			sum += gradient[2][j]*w[2][j][1][i]*dsigmoid(v[1][i])
		gradient[1][i] = sum
		

def compute_delta(delta,gradient,output,a,topology):
	numLayers = len(topology)
	for i in range(1,numLayers):
		for j in range(topology[i]):
			for k in range(i):
				for l in range(topology[k]):
					#print "I: ", i,"J: ", j, "K: ", k,"L: ",l
					delta[i][j][k][l] = delta[i][j][k][l]*a + ((1 - a) * gradient[i][j] * sigmoid(output[k][l]))

def update_weight(delta,weights,eta,topology):
	numLayers = len(topology)
	for i in range(1,numLayers):
		for j in range(topology[i]):
			for k in range(i):
				for l in range(topology[k]):
					#delta[i][j][k][l] = delta[i][j][k][l]*a + ((1 - a) * gradient[i][j] * output[i][k])
					weights[i][j][k][l] += delta[i][j][k][l]*eta

#allocate all the lists to be used in here,
#topology is a vector 
def allocate_lists(topology,v,weights,delta,gradient):
	numLayers = len(topology)
	for i in range(numLayers):
		nodesInLayer = topology[i]
		new = []
		v.append(copy.deepcopy(new))
		gradient.append(copy.deepcopy(new))
		for j in range(nodesInLayer):
			v[i].append(0)
			gradient[i].append(0)
	delta.append(copy.deepcopy(new))
	weights.append(copy.deepcopy(new))
	for i in range(1,numLayers):
		#print "i: ",i
		delta.append(copy.deepcopy(new))
		weights.append(copy.deepcopy(new))
		for j in range(topology[i]):
			#print "J: ", j
			delta[i].append(copy.deepcopy(new))
			weights[i].append(copy.deepcopy(new))
			for k in range(i):
				#print "I: ", i,"J: ", j, "K: ", k
				delta[i][j].append(copy.deepcopy(new))
				weights[i][j].append(copy.deepcopy(new))
				for l in range(topology[k]):
					#print "I: ", i,"J: ", j, "K: ", k,"L: ",l
					delta[i][j][k].append(0)
					weights[i][j][k].append(0)	
				

def initialize_weights(weights,topology):
	numLayers = len(topology)
	for i in range(1,numLayers):
		for j in range(topology[i]):
			for k in range(i):
				for l in range(topology[k]):
					num = r.random() * .3
					sign = r.random()
					if(sign < .5):
						num *= -1
					weights[i][j][k][l] = num
					#weights[i][j][k][l] = BigFloat(num,context=precision(100))
	

