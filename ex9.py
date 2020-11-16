# Printing Printing Printing

# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug" # Linebreak. Important to use \n rather than /n as linebreak

print "Here are the days: ", days
print "Here are the months: ", months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""" # triple-quotes allow multi-line string without breaking the command. See below

# The backslash \ acts as an escape sequence
    # It allows us to encode difficult-to-type characters into a string, in this case the "n" for new line
    # It could also be used when we want to return a string including double-quotes
        # eg "I am 6'2\" tall." - backslash prevents Python from ending the string print command after "2"
        # OR with single-quotes, 'I am 6\'2" tall.'
# Triple quote """ is another way. It allows as many lines of text as desired between the 2 sets of triple-quotes
