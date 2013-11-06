# do not need to declare variable type

my_name= "peekawho"
my_age= 12
myheight= 128
myweight=12
myeyes= "black"
myteeth= 'white' 
myhair= 'brown'

# don't forget the % signs for the variables

print "Lets talk about %s" %my_name
print "It is %d cm tall" %myheight
print "It is %d years old" %my_age
print "It has a mass of %d" %myweight
print "It's got %s eyes and %s teeh and OMG, %s hair" % (myeyes, myteeth, myhair)

# %r is the universal shizz, %d is decimal and %s be the strings

print "If I add %r, %d, and %d we get %d" % (my_age, myheight,myweight, my_age+ myheight +myweight)

# apparently you can not concatenate a string and an int, indepedent of stuff
#a= "hello" b= 3 c= a+b

#perform calculations
cm= 1000

print "The height is %d" %cm
print "In metres, this would be %d" %(cm/1000)
