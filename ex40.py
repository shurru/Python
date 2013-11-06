class Song(object): 
	#normally done by other languages, need to explicitly state in Python
	#self automatically gets called.. needed for functioning 
	def __init__(self, lyrics): 
		self.lyrics= lyrics
		
	def singmeasong(self): 
		for line in self.lyrics: 
			print line

#setting the titles as instances of the class
happy_bday= Song(["Happy Birthday to you", 
				  "You live in a zoo", 
				  "you look like a monkey and act like one too"])

bullsonaparade= Song(["They rally around the family", 
					  "With pockets full of shells"])
					  
happy_bday.singmeasong()

bullsonaparade.singmeasong()