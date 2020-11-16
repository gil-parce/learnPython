# Functions and Variables

# Defines function "cheese_and_crackers" with 2 arguments:
    # "cheese_count" and "box_of_crackers"
def cheese_and_crackers(cheese_count, box_of_crackers):
    print "You have %d cheeses!" % cheese_count # Prints value of cheese_count in a string
    print "You have %d boxes of crackers!" % box_of_crackers # Prints value of box_of_crackers in string
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# All of the following show different ways of filling the above function

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)
# Above calls the function "cheese_and_crackers" with argument values 20 and 30

# The following will create variables amount_of_cheese (10) and amount_of_crackers (50)
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
# Note: The above variables are separate from the function
# They are passed to the function and temporary versions are made just for the function's run

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# This line calls the function cheese_and_crackers with arguments set to the variables created above

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)
# Calls function cheese_and_crackers with variables "10+20" and "5+6"

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
# Creates variables combining string and maths for arguments in cheese_and_crackers function
# And calls cheese_and_crackers function
