print "you enter a dark room with two dorrs. Do you go through Door 1 or Door 2"
door= raw_input ("1 or 2?\n")

if door== "1": 
	print "You see a huge bear eating a cake, what do you do?" 
	print "1. Take the cake"
	print "2. Scream at the bear"
	bear= raw_input ("1 or 2 \n")
	
	if bear== "1":
		print "The bear ate your face off. Yay"
	
	if bear== "2":
		print "The bear ate your legs off. Poor you."

elif door=="2":
	print "You stare at the endless abyss of the retina of the devil"
	print "1. Blueberries."
	print "2. Yellow jacket"
	print "3. Revolvers singing songs"
	mad= raw_input ("1,2 or 3 \n")
	
	if mad== "1" or mad== "2":
		print "You're not insane at all"
	else: print "You've lost it"
	
else: 
	print "your eyes melt into a puddle and you die"
	