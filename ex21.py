# Functions Can Return Something

def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b
# 'return' creates a value that can then be
# assigned to a variable that calls the function
# Note: function works well without print line
# print line would not usually be included

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"
# This is the first thing that prints because
# the print commands above are in the function defs
# The functions have not actually been called yet


age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
# By calling the functions to assign values to variables:
# 1) the function runs, which is why their text appears in console
# (If the print lines were not included in the functions the text wouldn't appear)
# 2) the resulting value is assigned to the variables

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."


what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# Python observes the order of operations
# Start with inner parentheses (divide)
# Then moves out to multiply, then out to subtract, then out to add
# We see the process printed out in the terminal
# because the functions include print lines

# To write it out numerically:
# # what = (30 + 5) + ((78 - 4) - ((90 * 2) * ((100 / 2) / 2)))

print "That becomes: ", what, "Can you do it by hand?"
