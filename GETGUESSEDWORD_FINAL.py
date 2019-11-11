
"""
Created on Mon Nov 11 20:33:25 2019

@author: Angela Leenzae Edang
"""

''' Create a function getGuessedWord that takes in two parameters - a string,
 secretWord, and a list of letters, lettersGuessed. This function will return a string
 that is comprised of letters and underscores, based on what letters in 
 lettersGuessed are in secretWord. This shouldn't be too different from 
 isWordGuessed. '''
 
# getGuessedWord - function that will show guessed and unguessed letters of the secret word
# isWordGuessed - function that will check whether all the letters guessed are in the secret word
# isWordGuessed - will only accept lowercase letters in the string
# secretWord - a string, the word the player is trying to guess
# lettersGuessed - a list, the letters the player has guessed
# string - return, consists of letters and underscores that represents the components of the secretWord
# for, if-else statements - loops used to simulate the program
# str - string
# letter - guessed letter
# _ - symbol used for blank
 
def getGuessedWord(secretWord, lettersGuessed):
    str = " "
    for letter in secretWord:
        if letter in lettersGuessed:
           str = str + letter
        else:
            str = str + "_"
            
    return str