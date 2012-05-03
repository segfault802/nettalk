#!/usr/bin/python2 
import random as r
import re

def load_data(filename):
	data = []
	f = open(filename,"r")
	row = []
	for line in f:
		if(len(line) < 5):
			row.append(float(line))
			if(row[3] == 2):
				row[3] = .5
			data.append(row)
			row = []
		else:
			items = line.split(",")
			row.append(float(items[0]))
			row.append(float(items[1]))
			row.append(float(items[2]))
	return data
def gen_xor(size):
	data = []
	for i in range(size):
		new = []
		num = r.random()
		if(num < .25):
			new.append(0)
			new.append(0)
			new.append(0)
		elif(num >= .25 and num < .5):
			new.append(0)
			new.append(1)
			new.append(1)
		elif(num >= .5 and num < .75):
			new.append(1)
			new.append(0)
			new.append(1)
		else:
			new.append(1)
			new.append(1)
			new.append(0)
		data.append(new)
	return data
