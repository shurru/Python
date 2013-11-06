def add (a,b):
	print "Adding %d to %d" %(a,b)
	return a+b

def sub (a,b):
	print "Subtracting %d from %d" % (b,a)
	return a-b

def mult (a,b):
	print "Multiplying %d and %d" %(a,b)
	return a*b

def div (a,b):
	print "Dividing %d and %d" %(a, b)
	return a/b

print "give me two variables" 
var1= float(raw_input ("variable1:"))
var2= float(raw_input ("variable2:"))

age= add (var1, var2)
height=sub (var1, var2)
weight=mult (var1, var2)
cure= div (var1, var2)

print " you are %d years old, %d feet tall, %d kgs heavy and can be cured by %d medicines" %(age, height, weight, cure)

print "here's a puzzle" 

what= add(age, sub(height, mult(weight, div(cure,2))))

print "that becomes" ,what, "can you do it by hand?"