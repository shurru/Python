def func1(x, y, z): 
	print "My name is %r " %x
	print "My age is %r " %y
	print "I live in %r" %z 


name= raw_input ('What is your name? \t') 
age= raw_input("what's your age?\t") 
live= raw_input("which country do you live in? \t")

func1 (name,age,live)