
"""
Created on Mon Nov 11 20:21:51 2019

@author: Angela Leenzae Edang
"""

''' Create a function that is named as: isWordGuessed that takes in two parameters -
 a string, secretWord, and a list of letters, lettersGuessed. This function will return a 
 boolean - True if secretWord if all the letters of secretWord as in lettersGuessed
 and False if not. '''

# isWordGuessed - function that will check whether all the letters guessed are in the secret word
# isWordGuessed - will only accept lowercase letters in the string
# secretWord - a string, the word the player is trying to guess
# lettersGuessed - a list, the letters the player has guessed
# bool - return, either True or False depending on the lettersGuessed
# for, if-else statements - loops used to simulate the program

def isWordGuessed(secretWord, lettersGuessed):
    word = 0 
    for letter in secretWord:
        if letter in lettersGuessed:
            word = word + 1 
        else:
            return False
    return True