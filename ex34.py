animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
print animals # Print the list of animals
for i in animals:
    print i
# This tells python to print each animal in turn

# To access a particular item in a list
# put list name then the index number in square brackets

for i in range(len(animals)):
# len measures the length, so using range(len(xyz))
# it automatically runs the range as the length of the list
# allowing me to change the number of items and still run
# the entire length of the list
    print "Index %d in the list is %s." % (i, animals[i])

#to print just 1 particular item in the list:
print animals[3]