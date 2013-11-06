# def funcname (variables): is how you define functions. 
# can get them from libraries as well. 
#make sure you indent to get it to be a part of the 
def print_two (*args):
	arg1, arg2= args
	print "arg1: %r, arg2: %r" %(arg1,arg2)

def print_twoa (arg1, arg2):
	print "arg1: %r, arg2: %r" %(arg1,arg2)
	
def print_one (arg1):
	print "arg1: %r" %arg1

def print_none ():
	print "Got nothing bro"
	
print_two ("shurru" , "rules")
print_twoa ("is", "awesome")
print_one ("rocking")
print_none ()

