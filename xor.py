#!/usr/bin/python2 
from ann import *

topology = [2,2,1]
delta = []
values = []
weights = []
gradient = []
timesteps = 100000
patterns = 100
offset = 0
eta = 1.0
a = .9
p = 0
numCorrect = 0

allocate_lists(topology,values,weights,delta,gradient)

r.seed(5890)
initialize_weights(weights,topology)
data = gen_xor(patterns)


#data  = load_data("training.dat")
#print data
desired = [data[0]]

for i in range(timesteps):	
	values[0][0] = data[p][0]
	values[0][1] = data[p][1]
	desired[0] = data[p][2]
	#print "timestep: ",i, "pattern: ",p," input: ",values[0][0], " ",values[0][1]
	#print "feedforward"
	update(weights,values)
	#print "MSE"
	err = error(values[2],desired)
	#print "A: ",values[0][0],"B: ",values[0][1],"Output: ", sigmoid(values[2][0]), "Error: ",err
	#print err,desired[0],sigmoid(values[2][0])
	#print "backpropagate"
	if(err > .1):
		backpropagate(values,desired,weights,gradient)
		compute_delta(delta,gradient,values,a,topology)
		update_weight(delta,weights,eta,topology)
	else:
		numCorrect += 1
	p += 1
	if(p >= patterns):
		print i, " timesteps"
		print "Correctly classified ",numCorrect, " of ",patterns," patterns"
		if(numCorrect == patterns):
			break
		numCorrect = 0
		p = offset
