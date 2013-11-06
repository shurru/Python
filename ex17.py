from sys import argv
#returns true if file exists, and false if it doesn't
#import allows you to get in different files 
from os.path import exists

script, fromfile, tofile= argv

print "Copying from %s to %s" %(fromfile, tofile)

infile= open(fromfile)
indata= infile.read()

print "The input file is %d bytes long" %  len(indata)

print "Does the output file exist? %r" % exists(tofile)
#print "If you want to continue, hit Return or hit Ctrl-C to exit"
#raw_input()

outfile= open (tofile, 'w')
outfile.write(indata)

print "all done"

infile.close()
outfile.close()