#!/usr/bin/python2 

from mapping import *
from  misc import *
from ann import *

#main nettalk implementation


delta = []
values = []
weights = []
gradient = []
eta = 1.0
a = .9
passes = 100 #number of passes through the set
words = 1 #number of words to use
offset = 0 #offset from the beginning of the list
groupSize = 29 #size of the input group for each character
margin = 3 #number of characters on either side of the current character
frame = 2*margin+1 #total size of the character window
input = frame * groupSize #total number of input units
topology = [input,20,26]
charIndex = [] #this holds the start indices for each input group
for i in range(0,input,groupSize):
	charIndex.append(i)

allocate_lists(topology,values,weights,delta,gradient)

r.seed(5890)
initialize_weights(weights,topology)


#print charIndex
data = load_nettalk_data('out.dat')
#print data

for i in range(passes):
	numCorrect = 0
	total = 0	
	for word in range(words):
		print 'word: ', data[word][0]
		strlen = len(data[word][0])		 
		for pos in range(strlen):
			print 'position: ',pos			
			start = pos - margin
			end = pos + margin + 1
			#window = []
			index = 0
			for j in range(start,end):
				if(j < 0 or j >= strlen):
					newChar = '-'
				else:
					newChar = data[word][0][j]
				converted = map_char(newChar)
				cIndex = 0
				#charIndex[index+1]
				for k in range(charIndex[index],charIndex[index]+groupSize):			
					#print k					
					#print cIndex					
					values[0][k] = converted[cIndex]
					cIndex += 1
				index += 1								
				#window.append(newChar)
			#print values[0]
			
			#set the desired output, get the phoneme and stress vectors and join them
			pVector = map_phoneme(data[word][1][pos])
			sVector = map_stress(data[word][2][pos])
			desired = pVector + sVector
			#print desired
			
			#update and do backpropagation
			update(weights,values)
			err = error(values[2],desired)
			print err			
			if(err > .1):
				backpropagate(values,desired,weights,gradient)
				compute_delta(delta,gradient,values,a,topology)
				update_weight(delta,weights,eta,topology)
			else:
				numCorrect += 1
			total += 1
	print "Correctly classified ",numCorrect, " of ",total," phonemes"
	numCorrect = 0
			

