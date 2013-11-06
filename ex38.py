tenthings= "Apples Oranges Crows Telephone Light Sugar" 

print "Not ten things.. Lets fix it"

stuff= tenthings.split (' ')
morestuff= ["Day", "Night", "evening", "song", "frisbee", "corn", "banana", "Boy"]

while len(stuff)!= 10: 
	nextone= morestuff.pop()
	print "adding:", nextone
	stuff.append(nextone)
	print "There are now %d items" %len(stuff)
	
print "there we go:" ,stuff

print stuff[1]
print stuff[-1]
print stuff.pop()
print ''.join(stuff) #joins all the elements in stuff
print '#'.join(stuff [3:5]) #joins elements <5

