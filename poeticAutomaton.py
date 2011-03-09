#!/usr/bin/python
# http://mathworld.wolfram.com/ElementaryCellularAutomaton.html

# This probably won't be beautiful code.

import sys, re, hyphenate

rule30 = [0,0,0,1,1,1,1,0]

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
		return rule[0]
	if p1 is not ' ' and p2 is not ' ' and p3 is ' ':
		return rule[1]
	if p1 is not ' ' and p2 is ' ' and p3 is not ' ':
		return rule[2]
	if p1 is not ' ' and p2 is ' ' and p3 is ' ':
		return rule[3]
	if p1 is ' ' and p2 is not ' ' and p3 is not ' ':
		return rule[4]
	if p1 is ' ' and p2 is not ' ' and p3 is ' ':
		return rule[5]
	if p1 is ' ' and p2 is ' ' and p3 is not ' ':
		return rule[6]
	if p1 is ' ' and p2 is ' ' and p3 is ' ':
		return rule[7]

# `seed` is the word to start the poem with.
seed = sys.argv[1]
# `generations` is how many lines to repeat the cellular automaton
totalsteps = int(sys.argv[2])

# Make a grid to hold the poem.
# Words will first be put in here.
grid = []
# Width of the grid based on specified steps
gwidth = totalsteps*2-1
for i in xrange(totalsteps):
	line = []
	for j in xrange(gwidth):
		if i==0:
			if j==totalsteps-1:
				line.append(seed)
			else:
				line.append(' ')
		else:
			if generate(j,i,rule30):
				line.append('X')
			else:
				line.append(' ')
	grid.append(line)


# PRINTING!
for r in grid:
	print r
	