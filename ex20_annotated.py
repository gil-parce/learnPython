from sys import argv # First import the argv command

script, input_file = argv # Then unpack it

# Define command print_all with argument of variable 'f' (file)
# Create function to read file
def print_all(f):
    print f.read()

# Define command rewind with argument f
# seek(0) moves to the start of the file (hence 'rewind')
def rewind(f):
    f.seek(0)

# Define command print_a_line with the 2 arguments
# line_count gives line number, readline() reads a line from the file
def print_a_line(line_count, f):
    print line_count, f.readline()
# Note: readline() function returns the \n at the end of the line from the file
# To avoid leaving empty lines, run:
# print line_count, f.readline(), (the difference is the comma)

# Creates variable current_file which opens the input_file given in argv
current_file = open(input_file)

# Print string
print "First let's print the whole file:\n"

# Print the entire input_file
print_all(current_file)

# Print string
print "Now let's rewind, kind of like a tape."

# Moves back to the start of the file with seek(0)
rewind(current_file)

# Print string
print "Let's print three lines:"

# print linecount (1) and reads and prints the first line
current_line = 1
print_a_line(current_line, current_file)

# print linecount (2) and second line
# rather than inputting "current_line = current_line + 1"
# can input "current_line += 1" to achieve the same thing
current_line += 1
print_a_line(current_line, current_file)

# print linecount (3) and third line
current_line += 1
print_a_line(current_line, current_file)
