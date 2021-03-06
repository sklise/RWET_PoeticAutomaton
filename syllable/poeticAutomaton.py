#!/usr/bin/python
# http://mathworld.wolfram.com/ElementaryCellularAutomaton.html

# This probably won't be beautiful code.

import sys, re, hyphenate, random

try:
	if isinstance(sys.argv[1],str):
		seed = sys.argv[1]
		seed = seed.lower()
	else:
		seed = 'context'
except:
	seed = 'context'
try:
	totalsteps = int(sys.argv[2]) # `generations` is how many lines to repeat the cellular automaton
except:
	totalsteps = 4
try:
	pickrule = int(sys.argv[3])
except:
	pickrule = 30

cellrules = {\
	0	: [0,0,0,0,0,0,0,0],\
	1	: [0,0,0,0,0,0,0,1],\
	2 	: [0,0,0,0,0,0,1,0],\
	3	: [0,0,0,0,0,0,1,1],\
	4	: [0,0,0,0,0,1,0,0],\
	5	: [0,0,0,0,0,1,0,1],\
	6	: [0,0,0,0,0,1,1,0],\
	7	: [0,0,0,0,0,1,1,1],\
	8	: [0,0,0,0,1,0,0,0],\
	9	: [0,0,0,0,1,0,0,1],\
	10	: [0,0,0,0,1,0,1,0],\
	11	: [0,0,0,0,1,0,1,1],\
	12	: [0,0,0,0,1,1,0,0],\
	13	: [0,0,0,0,1,1,0,1],\
	14	: [0,0,0,0,1,1,1,0],\
	15	: [0,0,0,0,1,1,1,1],\
	16	: [0,0,0,1,0,0,0,0],\
	17	: [0,0,0,1,0,0,0,1],\
	18	: [0,0,0,1,0,0,1,0],\
	19	: [0,0,0,1,0,0,1,1],\
	20	: [0,0,0,1,0,1,0,0],\
	21	: [0,0,0,1,0,1,0,1],\
	22	: [0,0,0,1,0,1,1,0],\
	23	: [0,0,0,1,0,1,1,1],\
	24	: [0,0,0,1,1,0,0,0],\
	25	: [0,0,0,1,1,0,0,1],\
	26	: [0,0,0,1,1,0,1,0],\
	27	: [0,0,0,1,1,0,1,1],\
	28	: [0,0,0,1,1,1,0,0],\
	29	: [0,0,0,1,1,1,0,1],\
	30	: [0,0,0,1,1,1,1,0],\
	54	: [0,0,1,1,0,1,1,0],\
	60	: [0,0,1,1,1,1,0,0],\
	62	: [0,0,1,1,1,1,1,0],\
	102	: [0,1,1,0,0,1,1,0],\
	126	: [0,1,1,1,1,1,1,0],\
	188	: [1,0,1,1,1,1,0,0]\
}

def wordFromRule(word, rule):
	syls = []
	thematches = []
	leng = 0
	thesearch = ''
	syls = hyphenate.hyphenate_word(word) # split the word into syllables
	leng = len(syls)
	if leng <= 1: # if there aren't 3 syllables, make snippets.
		syls = ['','','']
		if len(word) >= 1:
			syls[0] = word[:1]
			syls[1] = word[1:2]
			syls[2] = word[-2:]
		else:
			syls[0] = word
			syls[1] = word
			syls[2] = word
	if rule in [0,1,4,5]: # Choose the appropriate search
		thesearch = re.compile(r'%s' % syls[1])
	elif rule in [2,3]:
		thesearch = re.compile(r'^%s' % syls[leng-1])
	else:
		thesearch = re.compile(r'%s$' % syls[leng-1])
	wordlist = open('sowpods.txt') # have to open this file each time, for whatever reason.
	for line in wordlist: # go through the dictionary
		try:
			#print "looks at a line"
			liner = line.strip() # strip whitespace, etc
			f = thesearch.search(liner)
			if f: # if the word matches
				thematches.append(liner) # add it to the list
		except:
			raise
			
	lm = len(thematches)
	if lm <= 1: # if there are no matches
		thematches = ['elephant'] # just use the original word.
	return random.choice(thematches)

def generate(x, y, rule):
	try: # Determine the parents.
		parent = grid[y-1]
		try:
			p1 = parent[x-1]
		except IndexError:
			p1 = ' '
		p2 = parent[x]
		try:
			p3 = parent[x+1]
		except IndexError:
			p3 = ' '
	except IndexError:
		print "index error"
	if p1 is not ' ' and p2 is not ' ' and p3 is not ' ' and rule[0]:
		return wordFromRule(p1,0)
	elif p1 is not ' ' and p2 is not ' ' and p3 is ' ' and rule[1]:
		return wordFromRule(p2,1)
	elif p1 is not ' ' and p2 is ' ' and p3 is not ' ' and rule[2]:
		return wordFromRule(p3,2)
	elif p1 is not ' ' and p2 is ' ' and p3 is ' ' and rule[3]:
		return wordFromRule(p1,3)
	elif p1 is ' ' and p2 is not ' ' and p3 is not ' ' and rule[4]:
		return wordFromRule(p2,4)
	elif p1 is ' ' and p2 is not ' ' and p3 is ' ' and rule[5]:
		return wordFromRule(p2,5)
	elif p1 is ' ' and p2 is ' ' and p3 is not ' ' and rule[6]:
		return wordFromRule(p3,6)
	else:
		return ' '

grid = [] # Make a grid to hold the poem.
gwidth = totalsteps*2-1 # Width of the grid based on specified steps
for i in xrange(totalsteps):
	gridline = []
	for j in xrange(gwidth):
		if i==0:
			if j==totalsteps-1:
				gridline.append(seed)
			else:
				gridline.append(' ')
		else:
			gridline.append(generate(j,i,cellrules[pickrule]))
	grid.append(gridline)

print seed + " in " + str(totalsteps)+r'/'+str(pickrule)
print ""

for r in grid: # PRINTING!
	for s in r:
		if s == ' ':
			print '            ',
		else:
			slen = len(s)
			if slen < 12: # if the word is short
				diff = 12 - slen # find the difference
				if diff % 2: # handle odd and even differently
					for i in xrange(diff/2):
						if diff > 2:
							s = ' '+s+' '
					s = ' '+s
				else:
					for i in xrange(diff/2):
						s = ' '+s+' '
				
			print s,
	print ""
print ""