from sys import argv
script, inputfile= argv

#makes it read the file and print it
def print_all (f):
	print f.read()
#seeks the line numbers, sets the file's current position
def rewind(f):
	f.seek(0) #moving to the start of the line
	
def printaline (linecount, f):
	print linecount, f.readline()

currentfile= open(inputfile)

print "lets print the whole file: \n" 

print_all (currentfile)

print "now lets rewind"
rewind(currentfile)

print "Lets print three lines shall we: \n"

currentline=1
printaline (currentline,currentfile)

currentline+=1
printaline(currentline, currentfile)

currentline+=1
printaline(currentline, currentfile)