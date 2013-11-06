#altering the function in the parent class.

class Parent(object):
	def altered(self):
		print "Parent got altered"

class Child (Parent): 

	def altered(self): 
		print "child before parent altered()"
		super (Child,self). altered() #runs the parent.altered() function
		print "Child, after parent altered"

dad= Parent()
son= Child()

dad.altered()
son.altered()
