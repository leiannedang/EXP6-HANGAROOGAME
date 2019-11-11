
"""
Created on Mon Nov 11 21:04:58 2019

@author: Angela Leenzae Edang
"""

''' Create a function getAvailableLetters that takes in one parameters - a list of letters,
 lettersGuessed. This function will return a string that is comprised of lowercase
 English letters - all lowercase English letters that are not in lettersGuessed. '''
 
# getAvailableLetters - function that will show a list of the letters guessed
# lettersGuessed - a list, the letters the player has guessed
# string - an imported library, a return, consists of all lowercase letters not yet guessed
# for, if statements - loops used to simulate the program
# str - string
# alphabet - all lowercase letters
# letter - guessed letter
# word - return, consists of the list of all unused letters from the alphabet
 
def getAvailableLetters(lettersGuessed):
    
    import string
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    word = " "
    
    for letter in alphabet:
        if not letter in lettersGuessed:
            word = word + letter
    return word