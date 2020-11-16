tabby_cat = "\tI'm tabbed in." # \t tabs in the line (indent)
persian_cat = "i'm split\non a line." # \n is linebreak
backslash_cat = "I'm \\ a \\ cat." # \\ [romts backslash "\"

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
''' #Triple-quote allows multiple lines of string

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print '''
I'm so excited to be feline this good.
You see, normally, %s.
But not today.
Today, %s - nothing more, nothing less.
I will claw my way out of this mess.
''' % (tabby_cat, backslash_cat)
# Note that the escape sequence does not work with %r
# Because %r prints out the raw representation of what is typed, including the original escape sequence as typed.
# Got to use %s instead
