#add features (real name: modules) sys is a module to your script from Python feature set
#another way to input data
from sys import argv #argv is argument variable
from sys import stdin

line= stdin.readline()
print "you typed:", line

#unpacks the argument into four different variables
 #holds the arguments to pass to Python
 
script, first, second = argv


print "The script is called:", script
print "Your first variable: ", first
print " your second variable:" , second
#print "Your third variable:", third

#why can't I print the users' choices from this method?

first= raw_input("what do you want the first variable to be?")
second= raw_input ("second?")
#third= raw_input ("third?")

print "Your new first variable is %r" %first
print "Your new second variable is %r" %second
