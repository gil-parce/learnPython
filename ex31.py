# Making Decisions

print """
You enter a dark room with two doors.
Do you go through door #1 or door #2?
Or do you ignore the doors... Fuck the system!
Or... what is a door? These mushrooms look interesting though.
"""

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"

elif door == "ignore":
    print """
You think you're a rebel, asshole?
Fuck off and tell me who would win in a fight...
\t 1. Johnny Rotten
or
\t 2. Freddy Mercury
    """

    fight = raw_input("> ")

    if fight == "1":
        print "Johnny went Anti-Christ on you. Don't expect to resurrect any time soon."
    elif fight == "2":
        print "This ain't the real life. This ain't fantasy. You sure you didn't try the 'shrooms?'"
    else:
        print "Choosing your own answer. You may be the chosen one rebel child."

elif door == "mushrooms":
    print "It's not a portabello, but maybe try it anyway?"
    print "1. Grab a handful, shuvel in and swallow before doubt has a chance to kick in."
    print "2. I'm not so sure about this... Just try one to begin with."
    print "3. Drugs are lame. My body is a temple. I shall not be sullied."

    mushrooms = raw_input("> ")

    if mushrooms == "1" or mushrooms == "2":
        print "You're tripping your tits off. Shower and off to bed. Why is my bed here? And who is asking me these questions?"

        who = raw_input("> ")

        if who == "god":
            print "Lame myth. Fuck off."
        elif who == "me":
            print "Not entirely wrong. Good job!"
        else:
            print "Wise ass. Fuck you."

    else:
        print "You're lame. But no worries, we both know you took a couple of 'shrooms on the way in and you're tripping baaaaaallllllls... Dost thou deny it?"

        deny = raw_input("> ")

        if deny == "yes":
            print "You lie, you die. Freddy Krueger style. Sweet fucking dreams."
        else:
            print "Honesty is the best policy. A fitting end to our story. Sweet dreams"

else:
    print "You stumble around and fall on a knife and die. Good job!"
