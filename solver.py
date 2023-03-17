#!/usr/bin/env python3
import sys

def solve_spelling_bee(letters_list, center_letter):
    
    '''Takes in a list of strings for letters_list and a single character string for center_letter.
       Returns a list of words from wordlist which contain the center letter, have a length of at 
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

    for word in wordlist:
        if center_letter in word:
            if word not in acceptable_words:
                if len(word) > 3:
                    if any(l in unacceptable_letters for l in word) == False:
                        acceptable_words.append(word)
                        
    return acceptable_words


# make sure there are two arguemnts
if len(sys.argv) != 3:
    print("Usage: python3 solver.py <letters> <center letter>")
    sys.exit(1)


# test
# convert the letters to a list
letters_list = list(sys.argv[1])
center_letter = sys.argv[2]

solution = solve_spelling_bee(letters_list, center_letter)

for word in solution:
    print("%-10s %d" % ( word, len(word)))

