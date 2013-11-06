#override explicitly 
#the child has its own function which can be chosen
#mixin with the implicit inheritance

class Parent(object):
	
	def override(self):
		print"Parent override"

	def follow(self):
		print "You must follow me!"


class Child(Parent):
	def override(self): #child gets to use its own function
		print "Child override" 
	#we can still call functions available in the parent class

dad= Parent()
son= Child()

dad.override()
son.override()
son.follow() #since this is an implicit inheritance it just inherits

		
