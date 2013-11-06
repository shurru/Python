x= "There are %d type of people" %10
binary= "binary"
dont= "do not"
#when you want to declare two variables, you will have to put the % in front of the brackets

y= "Those who know %s and those who %s" %(binary, dont)

print x
print y 

#adding a %r helps get quotes around the string.. it is the raw data
print " I said %r" %x
print " I also said : '%s'" %y #to add the single quotes, we either use %r or '%s'

hilarious= False
jokeeval= "isn't that joke funny? %r"

print jokeeval%hilarious

w= "This is the left side of.."
e= "..a string with a right side"

print w+e
