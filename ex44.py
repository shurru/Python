#implicit inheritance 
#without any defintion in the child class, it inherits the function in parent

class Parent (object): 

	def implicit(self):
		print "Parent implicit()"

class Child(Parent): #inherits the behavior from parent
	pass #pass is how you tell python you want an empty block

dad= Parent()
son= Child()

dad.implicit()
son.implicit() #calls the function in the parent class, so it inherits the feature