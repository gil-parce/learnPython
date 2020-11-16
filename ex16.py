# Reading and Writing Files

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If we don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?") # gives the prompt '?'

print "Opening the file..."
target = open(filename, 'w') # the second argument ('w') represents the mode to be used - in this case, permission to write
# options for second argument are: 'r' for read only
# 'w' for writing only (erasing existing file with same name)
# 'a' for appending the file, adding additional data to the end
# 'r+' for reading and writing
# when second argument is ommitted, 'r' is the default

print "Truncating the file. Goodbye!"
target.truncate()
# Unnecessary - opening with 'w' autumatically truncates an existing file

print "Now I'm going to ask you for three lines."

# the following prompts 3 lines to be written which will form the txt file
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# the following writes the 3 lines into the file with linebreaks
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close() #this cloes the file
