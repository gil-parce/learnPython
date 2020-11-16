# More Variables and Printing

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
height_metric = height * 2.54
weight_metric = weight / 2.2
description = 'big fat American 35 year old'

print "Let's take about %s." % name
print "He's %d inches tall." % height
print "Outside of the US, that translates to %f cm." % height_metric
print "He's %d pounds heavy... And that's %f kg to the rest of the world" % (weight, weight_metric)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)




# %s prints a string
# %d prins an integer
# %f prints a floating point number (decimal)
# %.<number of digits>f prints a floating point number with a fixed number of digits
