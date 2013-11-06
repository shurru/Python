from sys import argv

#unpacking argv into two variables
script, user_name= argv
prompt ='what do you think?' 

print "Hi %s, i'm the %s script" %(user_name, script)
print "I'd like to ask you a few questions"
print "Do you like me %s?" %user_name
likes= raw_input (prompt)

print "Where do you live %s?" %user_name
lives= raw_input(prompt)

print "What computer do you have?" 
comp= raw_input(prompt)

print """
Alright so you said %r about liking me 
You live in %r, not sure where that is 
You have a %r computer..
""" %(likes, lives, comp, comp)

