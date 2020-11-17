# Branches and Functions

from sys import exit

# define the function, gold_room
def gold_room():
    print "This room is full of gold. How much do you take?"

    choice = raw_input("> ")
    if "0" in choice or "1" in choice: # Valid responses must contain '1' or '0'
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")

# define function bear_room
def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False # means that the first raw_input response will affect whether the bear moves or not
#
    while True:
        choice = raw_input("> ")
    # creates infinite loop so any non-recognised input will be met with "I got no idea what that means"
    # and promp further input until recognisable input given

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."

# define function cthulu_room
def cthulu_room():
    print "Here you see the great evil Cthulu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    choice = raw_input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulu_room()
    # Allows input to be anything - as long as it contains either "flee" or "head"
    # Note: because 'flee' comes first in else-if, python will accept 'flee' if both words are in input

# defines function dead(why)
# whenever dead is called, it will print whatever is placed in () followed by ", good job!"
# and will then call exit function to quit the game
def dead(why):
    print why, "Good job!"
    exit(0)

# defines start function with initial choices
def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulu_room()
    else:
        dead("You stumble around the room until you starve.")

# Tells python to begin with start() function
start()