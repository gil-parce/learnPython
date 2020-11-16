# Strings and Text

x = "There are %d types of people." % 10 # Create a longer string variable for "x" with its own numerical variable "10" within it
binary = "binary" # Set a variable named binary as "binary"
do_not = "don't" # Set a binary named do_not as "don't"
y = "Those who know %s and those who %s." % (binary, do_not) # Create longer string variable "y" with short string variables included

# The following commands print "x" and "y" as created above
print x
print y

# The following return variables "x" and "y" again within typed strings
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
