import random as r


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


