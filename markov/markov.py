class MarkovGenerator(object):

	def __init__(self, n, max):
		self.n = n # order (length) of ngrams
		self.max = max # maximum number of elements to generate
		self.beginnings = [list(),list(),list()] # beginning ngram of every line
		self.ngrams = [dict(),dict(),dict()]

	def tokenize(self, text):
		text = text.lower()
		return text.split(" ")

	def feed(self, text):
		tokens = self.tokenize(text)
		
		for j in range(0,3): # save 1,2,3-grams.
			
			n = j+1
			
			# discard this line if it's too short
			if len(tokens) < n:
				return

			# store the first ngram of this line
			beginning = tuple(tokens[:n])
			self.beginnings[j].append(beginning)

			for i in range(len(tokens) - n):

				gram = tuple(tokens[i:i+n])
				next = tokens[i+n] # get the element after the gram

				# if we've already seen this ngram, append; otherwise, set the
				# value for this key as a new list
				if gram in self.ngrams[j]:
					self.ngrams[j][gram].append(next)
				else:
					self.ngrams[j][gram] = [next]

	# called from generate() to join together generated elements
	def concatenate(self, source):
		return " ".join(source)

	# generate a text from the information in self.ngrams
	def generate(self,alist,n):
		from random import choice
		
		current = tuple(alist)
		output = alist
		
		for i in range(self.max):
			if current in self.ngrams[n-1]:
				possible_next = self.ngrams[n-1][current]
				next = choice(possible_next)
				output.append(next)
				# get the last N entries of the output; we'll use this to look up
				# an ngram in the next iteration of the loop
				current = tuple(output[-n:])
			else:
				break

		output_str = self.concatenate(output)
		return output_str
	

if __name__ == '__main__':

	import sys

	generator = MarkovGenerator(n=3,max=1)
	for line in sys.stdin:
		line = line.strip()
		generator.feed(line)

	for i in range(14) :
		print generator.generate(3)
		# print generator.beginnings[i]
		# print ""

	# for i in generator.ngrams[1]:
		# print i
		
# "\[[A-z]*|\W*\]"
