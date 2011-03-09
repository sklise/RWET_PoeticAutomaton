Poetic Automaton
=====

#### Steven Klise <http://stevenklise.com>
#### Reading & Writing Electronic Text, ITP 2011

----

### Purpose: These poems take one word and evolve it according to the rules of a [cellular automata](http://mathworld.wolfram.com/ElementaryCellularAutomaton.html). The [rules list](http://atlas.wolfram.com/01/01/views/3/TableView.html) in terms of neighbors.

### Method:

1. Get input of a single word and a positive integer.
2. Choose a cellular automata rule (Rule)  from a subset of 255 rules from Mathworld. <http://mathworld.wolfram.com/ElementaryCellularAutomaton.html>
	- Only use rules which result in triangular shapes (000 => 0).
3. Split the input word into its syllables. Group the syllables in to as many pieces as designated by the Rule. If the word is one syllable, split the characters.
4. Use regular expressions to find words that start, end or have as middles the parts of the first word.
5. Put the resulting words on a second line.
6. Repeat 3-5 as many times as indicated from input integer.


Help from [Hyphenate.py](http://nedbatchelder.com/code/modules/hyphenate.html) and SOWPODS.