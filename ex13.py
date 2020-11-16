#Parameters, Unpacking, Variables

#The following is an "import" - it is how to add modules to the script from the Python feature set
from sys import argv  #argv is the argument variable - it holds the arguments passed through the script when it's run

#The following unpacks argv so that whatever is held in argv is unpacked and assigned to these variables
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
# the commas are essential - without them, an error is returned

# Rather than running only "python ex13.py"
# Must run with 4 values as follows:
# python ex13.py {value 1}, {value 2}, {value 3}
    # the values can be anything
