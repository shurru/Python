print "How old are you?", 

#raw_input() is the scanf or cin line, gets input

age= raw_input()
print "How tall are you?",

#use raw_input() instead of input() because of security preferences

height= raw_input()
print "How much do you weigh", 
weight= raw_input()

print "So you are %r years old, %r cm high and %r kg heavy" %(age,height,weight)
