from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file) # Open from_file and put its information in a variable called in_file
indata = in_file.read() # Having opened the file, this command reads it and puts the text into "indata" variable
# To do it in 1 line: indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file) # Uses exist function imported above to see if to_file exists
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w') # Opens to_file with writing permission and stores it in variable out_file
out_file.write(indata) # Reads the indata (read from in_file) and places it in out_file

print "Alright, all done."

out_file.close()
in_file.close() # This would be unnecessary if indata is created in 1 line earlier
                # Since in_file would not have been left open
