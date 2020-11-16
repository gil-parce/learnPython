# Reading Files

from sys import argv # Imports the module argv

script, filename = argv # Uses argv to get a filename

txt = open(filename) # Opens the file

print "Here's your file %r:" % filename # Prints a little introductory line
print txt.read() # Call a "read" function on txt
# Can run commands on the file retrieved from "open"
# Run commands with dot ("."), the name of the command ("read"), and parameters, like with "open" and "raw_input"
# The following essentially repeats the process.

print "Type the filename again:" # Prints an instruction line
file_again = raw_input("> ") # Prompts with ">" and saves the filename as variable "file_again"

txt_again = open(file_again) # Opens the file and sets the open command as a value for "txt_again"

print txt_again.read() # Calls a "read" function on txt_again
