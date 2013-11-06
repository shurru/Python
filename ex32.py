thecount= [1,2,3,4,5] #created an array/list
fruits= ['apples', 'oranges', 'pears', 'apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

#for loops are different in this case 
for number in thecount:
	print "This is the count %d" %number 

for fruit in fruits:
	print "A fruit of type: %s" %fruit #use the variable and not the list

#use %r for mixed lists
for i in change: #automatically does the increment
	print "here's your change %r" %i

elements=[]
for i in range(0,6): #0 to less than 6
	print"Adding %d to the list." %i 
	#appending the list- adds to the end of the list
	elements.append(i)
	
for i in elements:
	print "Element was: %d" %i

