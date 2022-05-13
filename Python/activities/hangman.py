"""
Activity: Create a simple hangman game
First, randomly choose a word from a list of words to use for the hangman game
Each turn, request the user to input a guess, for a letter in the word
Check if the letter is in the word
    If it is, then update the hangman 'board' to show the position of the correctly guessed letter
    If it is not, then subtract one of the lives
End the game if lives==0 or if the entire word is correctly guessed
"""

import random
import re
#Initializing the word, word length, letters, lives, etc
words = ["computer","mug","phone","mouse","alcohol","bulb","calculator","ruler",]
word = random.choice(words)
letters = set(word)
lives = 7
n = 0
displaylst = []
while n < len(word):
    displaylst.append("_")
    n += 1
wrongguesses = []
end = False

#Main turn block
while lives > 0 and end==False:
    letterpos = []
    print("-"*40)
    print(" ".join(displaylst))
    print("{} lives remaining".format(lives))
    print("Wrong Guesses:"+",".join(wrongguesses))
    guess = input("Please enter a letter:")
    if guess not in letters:
        lives -= 1
        wrongguesses.append(guess)
    else:
        letterpos = [i.start() for i in re.finditer(guess,word)]
        for l in letterpos:
            displaylst[l] = guess
    if "_" not in displaylst:
        end = True

#post game messages
if lives == 0:
    print("You lose")
if end == True:
    print("You win!!")
print("The word was: {}".format(word))