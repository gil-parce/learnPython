#Printing

print "Mary had a little lamb." # Simple string print
print "Its fleece was white as %s." % 'snow' # 'snow' is not a variable - just a string. A variable would not be wrapped in single-quotes
print "And everywhere that Mary went." # simple string print
print "." * 10 # what'd that do? Print "." 10 times

# The following creates 12 variables
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch the comma at the end. Try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6, # The comma acts as a "space" - otherwise it defaults to linebreak
print end7 + end8 + end9 + end10 + end11 + end12 # Could run as one single-line print but such a long one (l>80 characters) is bad Python style

#The final two prints give the string "Cheese Burger"
