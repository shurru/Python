from sys import argv

script, filename= argv
#opens up the files you want to read
#creates a file object
txt= open(filename)

print "Voila, here's your file %r" %filename
#reads the file and prints out its contents
print txt.read()
#make sure to close if you read any file so that it doesn't consume resources
txt.close()

print "Type the filename again"
file_again= raw_input ('>')

txt_again= open(file_again)

print txt_again.read()
txt.close()
