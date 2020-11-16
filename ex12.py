# Prompting People

# The following is another way to achieve the same result as in ex11.
# This will print question prompts
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So you're %r years old, %s tall and %r heavy." % (
    age, height, weight)
