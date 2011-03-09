#!/usr/bin/python
# http://mathworld.wolfram.com/ElementaryCellularAutomaton.html

# This probably won't be beautiful code.

import sys, re, hyphenate

rule30	= [0,0,0,1,1,1,1,0]
rule54	= [0,0,1,1,0,1,1,0]
rule60	= [0,0,1,1,1,1,0,0]
rule126 = [0,1,1,1,1,1,1,0]

wordlist = open('sowpods.txt')

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
		
	if p1 is not ' ' and p2 is not ' ' and p3 is not ' ':
		if rule[0]:
			syls = hyphenate.hyphenate_word(p1)
			print syls[0]
			return searchPos(syls[0],2)
		else:
			return ' '
	if p1 is not ' ' and p2 is not ' ' and p3 is ' ':
		if rule[1]:
			syls = hyphenate.hyphenate_word(p1)
			return searchPos(syls[0],1)
		else:
			return ' '
	if p1 is not ' ' and p2 is ' ' and p3 is not ' ':
		if rule[2]:
			return 'c'
		else:
			return ' '
	if p1 is not ' ' and p2 is ' ' and p3 is ' ':
		if rule[3]:
			syls = hyphenate.hyphenate_word(p1)
			return searchPos(syls[0],1)
		else:
			return ' '
	if p1 is ' ' and p2 is not ' ' and p3 is not ' ':
		if rule[4]:
			syls = hyphenate.hyphenate_word(p2)
			try:
				return searchPos(syls[1],2)
			except IndexError:
				return searchPos(syls[0],2)
		else:
			return ' '
	if p1 is ' ' and p2 is not ' ' and p3 is ' ':
		if rule[5]:
			syls = hyphenate.hyphenate_word(p2)
			try:
				return searchPos(syls[0],3)
			except IndexError:
				return searchPos(syls[0],3)
		else:
			return ' '
	if p1 is ' ' and p2 is ' ' and p3 is not ' ':
		if rule[6]:
			syls = hyphenate.hyphenate_word(p3)
			n = len(syls)
			return searchPos(syls[n-1],3)
		else:
			return ' '
	if p1 is ' ' and p2 is ' ' and p3 is ' ':
		if rule[7]:
			return 'h'
		else:
			return ' '

def searchPos(st,pos):
	answer = st
	for line in wordlist:
		line = line.strip()
		if pos is 1:
			if re.search('^%s.*' % st, line):
				answer = line
		elif pos is 2:
			if re.search('.*%s,*' % st, line):
				answer = line
		else:
			if re.search('%s$' % st, line):
				answer = line
	return answer

seed = sys.argv[1] # `seed` is the word to start the poem with.
totalsteps = int(sys.argv[2]) # `generations` is how many lines to repeat the cellular automaton

grid = [] # Make a grid to hold the poem.
gwidth = totalsteps*2-1 # Width of the grid based on specified steps
for i in xrange(totalsteps):
	line = []
	for j in xrange(gwidth):
		if i==0:
			if j==totalsteps-1:
				line.append(seed)
			else:
				line.append(' ')
		else:
			line.append(generate(j,i,rule30))
	grid.append(line)

for r in grid: # PRINTING!
	print r