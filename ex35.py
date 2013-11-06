from sys import exit

def goldroom():
	print "this room is full of gold. How much do you take?"
	
	next= raw_input(">")
	
	#in is a membership operator: if there is a 1 or 0 in the number that's taken in, it proceeds
	if ("1" or "0" or "2" or "3") in next	:  #need to find an easier way around this.. range? 
		how_much= int(next)
	else: 
		dead("Man go learn to type a number")
	
	if how_much <50: 
		print "nice, you're not greedy. You win"
		#aborts the system
		exit(0)
	
	else: 
		dead ("you greedy bastard!")

def bearroom(): 
	print "there is a bear here" 
	print "the bear has honey" 
	print "the fat bear is in front of another door" 
	print "how are you going to move the bear" 
	bearmoved= False
	
	#stuck in an infinite loop
	while True: 
		next= raw_input(">")
		
		if next== "take honey" : 
			dead("the bear will slap your face off")
		
		elif next== "taunt bear" and not bearmoved:
			print "THe bear has moved from the door, go through"
			bear_moved= True
			goldroom()
			
		elif next== "taunt bear" and bearmoved:
			print "run for your life. it's going to eat you"
			goldroom()
			
		elif next== "open door" and bearmoved: 
			goldroom()

def cthuluroom (): 
	print "here's the evil cthulu" 
	print " he who stares at it goes insane" 
	print" Do you flee or eat your head?"
	
	next= raw_input(">")
	
	if "flee" in next: 
		start()
	elif "head" in next: 
		dead("well that was tasty")
	else: 
		cthuluroom()
		
def dead(why): 
	print why, "good job"
	exit(0)
	
def start(): 
	print "You are in a dark room" 
	print "there are doors to your right and your left"
	print "which one do you take?" 
	
	next= raw_input (">")
	if next== "left":
		bearroom()
	
	elif next== "right":
		cthuluroom()
	else: 
		dead ("You stumble around the room until you starve")

start()