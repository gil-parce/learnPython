# Functions and Variables extra task

def coffee_types(cof_origin):
    print "We have %d origins of coffee" % cof_origin
    print "Each one has a different profile"
    print "So, choose your origin.\n"

coffee_types(6)
prompt = '> '

print "So, which origin would you like?"
origin_choice = raw_input(prompt)

print "The %r has two processes, natural or washed." % origin_choice
print "Which would you prefer?"
cof_process = raw_input(prompt)

print "And do you need that ground?"
grinding = raw_input(prompt)

print "Okay, here's your %r, %r coffee." % (
origin_choice, cof_process)
