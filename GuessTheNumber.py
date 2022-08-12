#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 14:39:37 2022

@author: Justin Salcedo
This script executes a guessing game where the user has to find
a random whole number between or including two integers.
The program will validate legal inputs and then compare them
against a random-generated number while counting user attempts.
Some clues will display until the user hits the 'winning' message.
"""

import random

# Helpers

# Try to parse an input string to an integer until valid
def inputValidInteger(inputMsg) -> int:
    userInput = input(inputMsg)
    isValidNumber = False
    while (not isValidNumber):
        try:
            userInput = int(userInput)
        except ValueError:
            print("Your input is not a number")
            userInput = input(inputMsg)
        else:
            isValidNumber = True
    return userInput



# Constants # Change these values as you like
RANDOM_MIN = 0
RANDOM_MAX = 10
INPUT_MSG = "Type a whole number including or between {} and {}: ".format(RANDOM_MIN, RANDOM_MAX)

# Main code flow
def main():
    try:
        randomNumber = random.randint(RANDOM_MIN, RANDOM_MAX)
    except ValueError:
        print("Invalid range for random number. This may be due to RANDOM_MIN being bigger than RANDOM_MAX")
    else:
        print("Hi! Welcome to the 'Guess The Number' game")
        userInput = inputValidInteger(INPUT_MSG)

        nAttempts = 1
        while (userInput != randomNumber):
            nAttempts += 1
            if (userInput > RANDOM_MAX or userInput < RANDOM_MIN):
                print("Remember, the number is between {} and {} or even any of those.".format(RANDOM_MIN, RANDOM_MAX))
            if (userInput > randomNumber):
                userInput = inputValidInteger("Try a smaller number: ")
            if (userInput < randomNumber):
                userInput = inputValidInteger("Try a bigger number: ")
            
        if (nAttempts == 1):
            print("Congratulations! You guessed the number {} on the first try.".format(randomNumber))
        else:
            print("Correct! You guess the number {} in {} attempts.".format(randomNumber, nAttempts))

if __name__ == "__main__":
    main()