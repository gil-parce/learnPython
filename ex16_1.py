#Study Drill

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If we don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write these into the file"

target.write(line1 + '\n' + line2 + '\n' + line3 + '\n')
# note that line1, line2, line3 cannot be string laterals ie outside of quotes
# but '\n' only makes sense inside a string lateral hences quotes
# and '+' is necessary as we are adding to combine the strings

print "And finally, we close it."
target.close()
