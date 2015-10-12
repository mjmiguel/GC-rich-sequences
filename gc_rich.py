# add key(seq names), values (seqs) to dict
def make_dict(fa):
	myDict = {}
	key = ''
	for line in fa:
		line = line.strip() 
    		if '>' in line:
        		key = line.strip(">")
        		myDict[key] = ''
        	else:
        		myDict[key] += line
	return myDict
	fa.close()

# calculate gc content in given seq
def calc_gc(seq):
	gc = 0.0
	for char in seq:
		if char.lower() == 'g' or char.lower() == 'c':
			gc += 1
	return round((gc / len(seq)) * 100, 2)

import sys

fa = open(sys.argv[1], 'r')
myDict = make_dict(fa)

# from dict, print seq name with gc content
for key, val in myDict.iteritems():
	print key, calc_gc(val)
