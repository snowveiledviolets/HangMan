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
    movielist = []
    f = open(filename)
    for line in f:
        line = line.strip()
        movielist.append(line)
    f.close()
    print("Number of movie titles read in: "+str(len(movielist)))
    return movielist

def getPossibleMovies(movielist,length):
    """
    returns a list of movies from movielist having a
    specified length
    """
    lengthlist = []
    for movie in movielist:
        if len(movie.split())==length:
            lengthlist.append(movie)
    return lengthlist

def displayGuess(movieList):
    '''
    movieList is a list of characters with letters correctly
    guessed and '_' for letters not quessed yet
    returns the list as a String
    '''
    return ' '.join(movieList)

def guessStart(word):
    '''
    returns a list of single characters '_' the
    same size as movie
    '''
    displayWord = []
    for char in word:
        if (char.lower() in 'abcdefghijklmnopqrstuvwxyz') or (char in '1234567890'):
            displayWord.append('_')
        else:
            displayWord.append(char)
    return displayWord

def updateLetter(guessList,movieToGuess, letter):
    '''
    movieToGuess is the movie the user is trying to guess.
    guessList is the movie to guess as a list of characters, but
    only including the letters the user has guessed and showing
    the character '_' if a letter hasn't been guessed yet.
    letter is the current letter the user has guessed.
    '''
    indList = []
    ind = 0
    for char in movieToGuess.lower():
        if char==letter:
            indList.append(ind)
            ind+=1
        else:
            ind+=1
    if len(indList)>=1:
        for item in indList:
            guessList[item]=letter
        return guessList
    else:
        return guessList

def playGame(words):
    '''
    Play the game. Let the user know if they won or not.
    '''
    #setup for game
    guessLength = int(input("How many words should be in the movie to guess? "))
    while guessLength<1:
        guessLength = int(input("Please enter a number of at least 1: "))
    wrongGuessNum = int(input("How many wrong letter/number guesses? "))
    while wrongGuessNum<1:
        wrongGuessNum = int(input("Please enter a number of at least 1: "))
    moviesOfLength = getPossibleMovies(words,guessLength)
    movieToGuess = random.choice(moviesOfLength)
    guessList = guessStart(movieToGuess)
    letterList = []
    wordsLeft = guessLength
    # start the guessing
    while True:
        if guessList.count('_') == 0:
            # all letters guessed
            break
        print() # output to print for each round
        print("Guessed so far: "+ displayGuess(guessList))
        print("Letters/numbers already guessed: " +''.join(letterList))
        print("Number of misses left: "+ str(wrongGuessNum))
        print("Number of words left to complete: "+ str(wordsLeft))
        letter = input("Guess a letter/number or enter + to guess a movie: ")
        while (len(letter)>1):
            letter = input("Please only enter a single letter/number or a +: ")
        if letter=='+':
            movieGuess = input("Guess the movie (make sure to include symbols if there are any): ")
            if movieGuess.lower() == movieToGuess.lower():
                guessList = movieToGuess
            else:
                break
        else:
            updateLetter(guessList, movieToGuess, letter.lower())
            if letter.lower() not in guessList:
                wrongGuessNum -=1
                letterList.append(letter.lower())
            else:
                if letter.lower() in letterList:
                    wrongGuessNum -=1
                    print("You have already guessed "+letter)
                letterList.append(letter.lower())
        letterList.sort()
        if wrongGuessNum == 0:
            break
        letterList.sort()
        toGO =0
        for word in (''.join(guessList)).split():
            if '_' not in word:
                toGO +=1
        wordsLeft = guessLength - toGO

    # game over
    if guessList.count('_') == 0:
        print("Congratulations, you win! You correctly guessed the movie: "+ movieToGuess)
    else:
        if wrongGuessNum==0:
            print("Oh no! You ran out of guesses... The movie was: "+ movieToGuess)
        else:
            print("Oh no! That was the wrong movie! The correct movie was: "+ movieToGuess)
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
    words = fileToStringList('movies.txt')
    playGame(words)
