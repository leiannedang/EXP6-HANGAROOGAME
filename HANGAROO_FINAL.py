
"""
Created on Mon Nov 11 22:11:31 2019

@author: Angela Leenzae Edang
"""

''' Create a function called Hangaroo, which takes one parameter - the secretWord
 the user is to guess. This starts up an interactive game of Hangaroo between the 
 user and the computer. Be sure you take advantage of the three helper functions,
 isWordGuessed, getGuessedWord, and getAvailableLetters, that you've defined in
 the previous part. '''

# Hangaroo - function that creates an actual interactive game between the user and the computer
# isWordGuessed - function that will check whether all the letters guessed are in the secret word 
# getGuessedWord - function that will show guessed and unguessed letters of the secret word
# getAvailableLetters - function that will show a list of the letters guessed
# secretWord - the word to be guessed by the player
# LettersGuessed - a list, the letters the player has guessed
# Guesses - the number of guesses left the player has 
# for, while, if, elif and else statements - loops used to simulate the program

def Hangaroo(secretWord):
    
    lettersGuessed = []
    Guesses = 5
    
    print("You are now playing Hangman!")
    print("I am thinking of a word that is ", len(secretWord), "letters long.")
    
    
    while Guesses > 0:
        print("You only have ", Guesses, " guesses remaining.")
        print("Available Letters: ", getAvailableLetters(lettersGuessed))
        
        guessInput = input("Guess a letter: ")
        
        if (guessInput not in secretWord):
            print("Woops! That letter is not in my word. ", getGuessedWord(secretWord, lettersGuessed))
            Guesses = Guesses - 1
        elif (guessInput in lettersGuessed):
            print("You already guessed that letter. Try again!", getGuessedWord(secretWord, lettersGuessed))
        else:
            print("Wow! That letter is in my word. ", getGuessedWord(secretWord, lettersGuessed))
        lettersGuessed.append(guessInput)
        
        if (isWordGuessed(secretWord, lettersGuessed) == True):
            print("Congratulations! You won the game!")
            print("The word was ", secretWord)
            return
    
    if (Guesses == 0):
        print("Sorry, you ran out of guesses! The word was ", secretWord)
        print("Game Over!")
        return
    
