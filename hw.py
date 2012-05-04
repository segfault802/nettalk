#!/usr/bin/python2 
from ann import *

topology = [3,20,1]
delta = []
values = []
weights = []
gradient = []
#timesteps = 10000
#patterns = 100
offset = 0
eta = 2.0
a = .9
p = 0
numCorrect = 0

allocate_lists(topology,values,weights,delta,gradient)

#r.seed(5890)
initialize_weights(weights,topology)
#data = gen_xor(patterns)




print "Testing"
patterns = 100
timesteps = 100
offset = 0
data = load_data("testing.dat")
desired = [data[0]]
for i in range(timesteps):	
	values[0][0] = data[p][0]
	values[0][1] = data[p][1]
	values[0][2] = data[p][2]
	desired[0] = data[p][3]
	update(weights,values)
	err = error(values[2],desired)
	#print err
	if(err <= .1):
		numCorrect += 1
	p += 1
	if(p >= patterns):
		print i, " timesteps"
		print "Correctly classified ",numCorrect, " of ",patterns," patterns"
		if(numCorrect == patterns):
			break
		numCorrect = 0
		p = offset


timesteps = 500000
patterns = 1000
offset = 0


data  = load_data("training.dat")
#print data

for i in range(timesteps):	
	values[0][0] = data[p][0]
	values[0][1] = data[p][1]
	values[0][2] = data[p][2]
	desired[0] = data[p][3]
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
		#print i, " timesteps"
		#print "Correctly classified ",numCorrect, " of ",patterns," patterns"
		if(numCorrect == patterns):
			break
		numCorrect = 0
		p = offset


print "Testing"
patterns = 100
timesteps = 100
offset = 0
data = load_data("testing.dat")
for i in range(timesteps):	
	values[0][0] = data[p][0]
	values[0][1] = data[p][1]
	values[0][2] = data[p][2]
	desired[0] = data[p][3]
	update(weights,values)
	err = error(values[2],desired)
	#print err
	if(err <= .1):
		numCorrect += 1
	p += 1
	if(p >= patterns):
		print i, " timesteps"
		print "Correctly classified ",numCorrect, " of ",patterns," patterns"
		if(numCorrect == patterns):
			break
		numCorrect = 0
		p = offset
