numbers= []
 
def loopy(i): 

  while i<=6: 
    print "at the top of i is %d" %i 
    numbers.append(i) 
    
    i = i+1
    print "Numbers now", numbers
    print "at the bottom of i is %d" %i 
  return numbers
 
nu= int(raw_input(">insert your number"))
if nu<=6:
	numb= loopy(nu)
	print "The numbers", numb
else: 
	print"Number inserted is too large"
 
