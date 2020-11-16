# Loops and Lists

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# This first kind of for-loop goes through a list
# After 'for' comes variable name - in this case 'number', though 'i' is common
for number in the_count:
    print "This is count %d" % number

# the same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# we can go through mixed lists too
# notice we have to use %r since it has both string and numbers
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
# range starts at 0 by default or with first given number
# and stops BEFORE the specified number (6)
# so could be written as range(6)
# can specify if range foes up or down, if it skips numbers
for i in range(0, 6):
    print "Adding %d to the list." % i
    #append is a function that lists understand
    elements.append(i)
    # element is the name given to the list
    # we run the dot function, append, on the object, element

# now we can print them out too
for i in elements:
    print "Element was: %d" % i

# Another, quicker way to do it:
elements2 = range(6)
for i in elements2:
    print "elements2 was: %d" % i
