# Hangman.py
# @Author - Shashwat Aggarwal
# 
# Hangman game
#


import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    result = False
    for char in secretWord:
        if char in lettersGuessed :
            result = True
        else :
            result = False
            break
    return result

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    result = ''
    for char in secretWord:
        if char in lettersGuessed :
            result = result + char
        else :
            result = result + '_ '
    return result


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    result = ''
    for char in string.ascii_lowercase:
        if char not in lettersGuessed:
            result = result + char
    return result    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...

    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is '+ str(len(secretWord)) +' letters long.'

    lettersGuessed = []
    mistakesMade = 0
    guess = 8

    while(mistakesMade != 8):

        print '-------------'
        print 'You have '+ str(guess) +' guesses left.'
        print 'Available letters: ' + getAvailableLetters(lettersGuessed)
        print 'Please guess a letter:',

        char_temp =  raw_input()
        char =  char_temp.lower()

        if char not in lettersGuessed :
            lettersGuessed.append(char)

            if char in secretWord :
                print 'Good guess: ' + getGuessedWord(secretWord, lettersGuessed)
            else :        
                print 'Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed)
                guess = guess - 1
                mistakesMade += 1 

        else :
            print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)

        
        if isWordGuessed(secretWord, lettersGuessed):
            print '-------------'
            print 'Congratulations, you won!'
            break 

    if mistakesMade == 8 :
        print '-------------'
        print 'Sorry, you ran out of guesses. The word was ' + str(secretWord)+ '.'
        

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
