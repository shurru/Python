def breakwords (stuff):
	"""This helps us split stuff up"""
	words= stuff.split()
	return words 

def sortwords (words):
	"""sorts words"""
	return sorted(words)
	
def printfirstword (words): 
	"""prints first word after popping it""" #documentation comments. you get these when you run help
	word= words.pop(0)
	return word

def printlastword (words):
	"""prints the last word"""
	word= words.pop (-1) #-1 is the last word in the array? 
	return word
	
def sortsentence (sentence):
	"""takes the sentence and sorts it"""
	words= breakwords(sentence)
	return sortwords(words)

def printfirstandlast (sentence): 
	words= breakwords(sentence)
	printfirstword (words)
	printlastword (words)

def printfirstandlastsorted(sentence): 
	words= sortsentence(sentence)
	printfirstword (words)
	printlastword (words)

