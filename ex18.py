# Names, Variables, Code, Functions

# this one is like your scripts with argv
def print_two(*args): # The * tells Python to take all arguments to the function and then put them in args as a list
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

#this one takes no arguments
def print_none():
    print "I got nothin'."

# The following provide variables for the functions
print_two("Gil", "Selby")
print_two_again("Gil", "Selby")
print_one("First!")
print_none()

# First, tell Python we want to make a function with 'def' (define)
# Next, name the function (e.g. print_two)
# Next, we place the argument/s (if any) inside parentheses
# No need to unpack arguments as in "print_two" above
    # Can just use the names we want directly inside the parentheses
# End with : and start indenting
# In this exercise, functions have been printed like scripts to show what they do
