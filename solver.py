#!/usr/bin/env python3

# Original code by fisheravonlea@gmail.com 
#
# The text file contains a non-exhaustive set of words, which means that some
# words that are valid for a Spelling Bee puzzle may not appear in the solver's
# output. Additionally, not all of the output words will be valid entries for
# the puzzle. The puzzles are curated to exclude highly obscure words, which are
# not systematically excluded by the solver.


import sys

def solve_spelling_bee(letters_list, center_letter):
    
    '''Takes in a list of strings for letters_list and a single character string for center_letter.
       Returns a list of words from word list which contain the center letter, have a length of at 
       least 4, and do not contain any unacceptable letters.'''
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
                'u', 'v', 'w', 'x', 'y', 'z']
    
    unacceptable_letters = [l for l in alphabet if l not in letters_list]
    acceptable_words = []

    word_file = open("/usr/share/dict/words", "r") #replace with your own file path

    wordlist = []

    for word in word_file:
        wordlist.append(str(word).lower()[:-1])

    blocklist_file = open("blocklist.txt", "r") #replace with your own file path
    blocklist = []

    for blockword in blocklist_file:
        blocklist.append(str(blockword).lower()[:-1])

    for word in wordlist:
        if center_letter in word:
            if word not in acceptable_words and word not in blocklist:
                if len(word) > 3:
                    if any(l in unacceptable_letters for l in word) == False:
                        acceptable_words.append(word)
                        
    return acceptable_words


# make sure there are two arguemnts
if len(sys.argv) != 3:
    print("Usage: python3 solver.py <letters> <center letter>")
    sys.exit(1)

# convert the letters to a list
letters_list = list(sys.argv[1])
center_letter = sys.argv[2]

if len(sys.argv[2]) != 1:
    print("Please enter 1 letter for center letter.")
    sys.exit(1)

if len(letters_list) != 7:
    print("Please enter 7 letters for letters-list.")
    sys.exit(1)

solution = solve_spelling_bee(letters_list, center_letter)

for word in solution:
    print("%-10s %d" % ( word.title(), len(word)))

