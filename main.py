#!/usr/bin/env python

import random

def main():
    """Start a song guessing game."""
    print("Guess the song!")
    
    song = [
            "Dance To This",
            "There For You",
            "My My My",
            "Indigo",
            "Strawberries&Cigarettes",
            "Come Together",
            "With You"
            ]
    
    x = random.choice(song)
    
    guess = None

    while x != guess:

       guess = str(input("what song am I thinking of? "))

       if x == guess:
           print("You guessed {}.Congratulations you got it right!".format(guess))
           break
       else:
           print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))

main()
     