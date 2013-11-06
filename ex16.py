from sys import argv

script, filename= argv

print "we're going to erase %r" %filename
print "if you don't want it, hit Ctrl-C"
print "If do you do want that, hit Return"

raw_input("?")

print "opening the file.."
#opens the file after erasing it.. 
# w is the short for write, we would use r for read. 
# we want to write into the target, so we use 'w'
target= open(filename, 'w')

print "truncating the file. ciao"
target.truncate 

print "Now input three lines"

#give variables the raw inputs so that they can write
line1=raw_input("line1:")
line2=raw_input ("line2:")
line3= raw_input ("line3:")


print "I'm going to write this to the file" 

target.write(line1)
target.write ("\n")
target.write(line2)
target.write ("\n")
target.write(line3)
target.write ("\n")

print "Now we close"
target.close()
