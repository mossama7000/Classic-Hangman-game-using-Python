# Hangman game

import string
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):

    return random.choice(wordlist)


wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):


    for i in secretWord:
        if i in lettersGuessed:
            continue
        else:
            return False

    return True

def getGuessedWord(secretWord, lettersGuessed):

    emptyWord = ['_' for i in range(len(secretWord))]

    for j in range(len(secretWord)):
        for k in lettersGuessed:
            if secretWord[j] == k:
                emptyWord[j] = secretWord[j]

    emptyWord1 = ''

    for m in emptyWord:
        emptyWord1 = emptyWord1 + m

    return emptyWord1


def getAvailableLetters(lettersGuessed):


    alphabet = string.ascii_lowercase

    availableLetters = ''

    for n in alphabet:
        if n not in lettersGuessed:
            availableLetters += n

    return availableLetters

def hangman(secretWord):

    numOfLetters = len(secretWord)

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(numOfLetters) +" letters long.")
    print("-----------------------------------------")

    lettersGuessed = []

    l = 0

    while l < 8:



        print("You have " + str(8-l) + " guesses left.")

        availableLetters = getAvailableLetters(lettersGuessed)

        print("Available Letters: " + availableLetters)

        guess = input("Please guess a letter: ")
        guessInLowerCase = guess.lower()


        if guessInLowerCase not in lettersGuessed:


            lettersGuessed.append(guessInLowerCase)

            GuessedWord = getGuessedWord(secretWord, lettersGuessed)

            if guessInLowerCase not in secretWord:
                l = l + 1
                print("Oops! That letter is not in my word: " + GuessedWord)

            else:
                print("Good guess: " + GuessedWord)


        else:
            print("Oops! You've already guessed that letter: " + GuessedWord)


        print("-----------------------------------------")

        checkGuess = isWordGuessed(secretWord, lettersGuessed)

        if checkGuess:
            print("Congratulations, you won!")
            return None
        else:
            if l == 8:
                print("Sorry, you ran out of guesses. The word was " + secretWord)
                return None


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
