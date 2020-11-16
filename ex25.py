# Even More Practice

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ') # We are splitting on blank spaces between words
    return words

def sort_words(words): # We are feeding the results of break_words into sort_words
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0) # pop(0) finds first word
    print word # Here, we do print, rather than return

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1) # pop(-1) goes to the end rather than beginning
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence) # relies on earlier defined function break_words
    return sort_words(words) # returns a sorted list
# Does same as break_words and sort_words but in 1 function rather than 2

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words) # uses 3 previously defined functions

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# This is not a script per se, but a module
# As argv is a module
# We can call the module in Python to use on other objects
# Module name 'ex25' - so we begin in Python with
# "import ex25" or "from ex25 import *"
# the second option avoids having to type "ex25." later
# run help() for descriptions of the functions
# or run help(break_words) for description of break_words, etc
