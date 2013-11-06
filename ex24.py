print "lets practuce everything"
print "you\'d need to know \'bout escapes with\\ that do \n newlines and \t tabs" 

poem= """
\t the lovely world
with logic so firmly planted 
whcih iahf aiahr \n
ia ihf if cwsodjf s 
\t aiws ewfh 
"""

print "------"
print poem 
print "------"

five= 10-2+3-6
print "this should be %d:" %five

def secretformula (started):
	JB= started*500
	jars= JB/1000
	crates= jars/100
	return JB,jars, crates
	
startpoint = 1000
beans, jars, crates= secretformula (startpoint)

print "We start with %d" %startpoint 
print "and we have %d Jb, %d jars, %d crates" %(beans, jars, crates)

startpoint= startpoint/10
print "we can also do it this way"
print "we have %d JB, %d jars, %d crates" % secretformula (startpoint)
