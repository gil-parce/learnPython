# Asking Questions

# raw_input() fimctopm presents a prompt to the user, gets input and returns the data in a string
# In the following case, it pauses after each question to allow the user to respond to the question
# raw_input() will always return data as a string, while input() converts the input as if it were code and returns it as it deems appropriate
print "How old are you?",
age = raw_input("Age? ") #In this particular eg, ("Age? ") gives a prompt. The word "Age" is not included in the script printed below
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r years old, %s tall and %r heavy." % (
    age, height, weight) # The variables are returned within single-quotes
# weight must be printed with %s rather than %r
    # %r prints '5/'7"' while %s prints '5'7"'

print "What's your name?",
name = raw_input()
print "What do you do?",
job = raw_input()
print "How do you like it?",
opinion = raw_input()

print "So, %r, if you like being a %r so much, why the fuck are you learning python?" % (
name, job
)
