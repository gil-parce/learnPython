# Printing, Printing

formatter = "%r %r %r %r" # "formatter" is a variable assigned 4 string items

print formatter % (1, 2, 3, 4) # The variable is printed with these 4 integers
print formatter % ("one", "two", "three", "four") # The variable is printed with 4 words
print formatter % (True, False, False, True) # The variable is printed with a boolean sequence
print formatter % (formatter, formatter, formatter, formatter) # "formatter" variable is filled with the word "formatter"
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sting.",
    "So I said goodnight."
) # The variable is filled with 4 longer strings, separated by comma
