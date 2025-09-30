#!/usr/bin/env python3
'''
Created on Feb 26, 2017

@author: Wren Kohler
'''

import random

def fileToStringList(filename):
    """
    filename is a file,
    returns a list of strings, each string represents
    one line from filename
    """
    wordlist = []
    f = open(filename)
    for line in f:
        line = line.strip()
        wordlist.append(line)
    f.close()
    return wordlist

def getPossibleWords(wordlist,length):
    """
    returns a list of words from wordlist having a
    specified length
    """
    return [word for word in wordlist if len(word)==length]

def displayGuess(wordList):
    '''
    wordList is a list of characters with letters correctly
    guessed and '_' for letters not quessed yet
    returns the list as a String
    '''
    return ' '.join(wordList)

def guessStart(word):
    '''
    returns a list of single characters '_' the
    same size as word
    '''
    return ['_']*len(word)

def updateLetter(guessList,wordToGuess, letter):
    '''
    wordToGuess is the word the user is trying to guess.
    guessList is the word to guess as a list of characters, but
    only including the letters the user has guessed and showing
    the character '_' if a letter hasn't been guessed yet.
    letter is the current letter the user has guessed.

    Modify guessList to include letter in its proper locations if
    letter is in wordToGuess.

    For example, if the wordToGuess is "baloney" and so far only a and
    e have been guessed, then guessList is ['_','a','_','_','_','e','_']
    If letter is 'o', then guessList is modified to now be:
    ['_','a','_','o','_','e','_']

    '''
    indList = []
    ind = 0
    for char in wordToGuess:
        if char==letter:
            indList.append(ind)
        ind+=1
    if len(indList)>=1:
        print("You guessed a letter!")
        print()
        for item in indList:
            guessList[item]=letter
    else:
        print("That's a miss")
        print()

def playGame(words):
    '''
    Play the game. Let the user know if they won or not.
    '''
    #setup for game
    guessLength = int(input("How many letters should be in the word to guess? "))
    while guessLength<3:
        guessLength = int(input("Please enter a number of at least 3: "))
    wrongGuessNum = int(input("How many wrong letter guesses? "))
    while wrongGuessNum<1:
        wrongGuessNum = int(input("Please enter a number of at least 1: "))
    wordsOfLength = getPossibleWords(words,guessLength)
    wordToGuess = random.choice(wordsOfLength)
    guessList = guessStart(wordToGuess)
    letterList = []
    missCount = wrongGuessNum

    # start the guessing
    while True:
        if guessList.count('_') == 0:
            # all letters guessed
            break
        print() # output to print for each round
        print("Guessed so far: "+ displayGuess(guessList))
        print("Letters already guessed: "+ ''.join(letterList))
        print("Number of misses left: "+ str(wrongGuessNum))
        letter = input("Guess a letter or enter + to guess a word: ")
        while len(letter)>1:
            letter = input("Please only enter a single letter or a +: ")
        if letter=='+':
            wordGuess = input("Guess the word: ")
            if wordGuess == wordToGuess:
                guessList = wordToGuess
            else:
                break
        else:
            updateLetter(guessList, wordToGuess, letter)
            if letter not in guessList:
                wrongGuessNum -=1
                letterList.append(letter)
            else:
                if letter in letterList:
                    wrongGuessNum -=1
                    print("You have already guessed "+letter)
                letterList.append(letter)
        letterList.sort()
        if wrongGuessNum == 0:
            break
        letterList.sort()

    # game over
    if guessList.count('_') == 0:
        print("Congratulations, you win! You correctly guessed the word "+ wordToGuess)
        print("It took you "+str(missCount-wrongGuessNum)+" misses")
    else:
        if wrongGuessNum==0:
            print("Oh no! You ran out of guesses... The word was "+ wordToGuess)
        else:
            print("Oh no! That was the wrong word! The correct word was "+ wordToGuess)
    playAgain() #asks if user wants to play again

def playAgain():
    """
    Asks the user if they want to play again. If answer is 'y', starts a new game
    If answer is 'n', says Goodbye and ends
    """
    print()
    answer = input("Do you want to play again? Enter y/n: ")
    while (answer!="y") and (answer!="n"):
        answer = input("Please enter either y or n: ")
    if answer=='y':
        print()
        playGame(words)
    else:
        print("Goodbye")

if __name__ == '__main__':
    words = fileToStringList('lowerwords.txt')
    playGame(words)
