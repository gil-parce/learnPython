# While Loops

i = 0
numbers = []
# Creates an empty list called 'numbers'

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)
    # Appends the value of i with each loop

    i += 1
    print "Numbers now: ", numbers # this prints the list defined up as 'numbers'
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num
# for-loop simply prints each number

# 1. Convert this while-loop to a function you can call,
# and replace 6 in the test (i < 6) with a variable.

print "\nConverting while-loop to function drill_1:"
def drill_1(n): # Here, n is the variable within the function, i is the increment/index
    i = 0
    numbers1 = [ ]
    while i < n:
        print "Item: %d" % i
        numbers1.append(i)
        i += 1
    print numbers1

# 2. Use this function to rewrite the script to try different numbers.

print "\nUsing drill_1 with n = 11"
drill_1(11)

print "\nUsing drill_1 with n = 5"
drill_1(5)

# 3. Add another variable to the function arguments that you can pass in
# that lets you change the + 1 on line 10 so you can
# change how much it increments by.

print "\nCreating function drill_3 to allow variable step size"
def drill_3(n, s): # n is the number, s is the step size
    i = 0
    numbers3 = [ ]
    while i < n:
        print "Item: %d" % i
        numbers3.append(i)
        i += s
    print numbers3

# 4. Use this function to see what effect it has.

print "\nUsing drill_3 with n = 25, s = 5"
drill_3(25, 5)

print "\nUsing drill_3 with n = 11, s = 2"
drill_3(11, 2)

# 5. Write it to use for-loops and range.

print "\ndrill_5 uses a for-loop and range instead."
def drill_5(n, s): # first define the function drill_5 as drill_3 above
    numbers5 = range(0, n, s)
    # need to include starting point 0 in this case
    # otherwise, python assumes n is starting point and s ending point
    for i in numbers5: # Now comes the for-loop
        print "Item: %d" % i
    print numbers

drill_5(28, 7)
