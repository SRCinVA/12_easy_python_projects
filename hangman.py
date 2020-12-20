import random
from words import words #she has a large file that she created to find a random word
import string

# here's the catch: 
# some of the words have hyphens, so we'll need to
# pick out a valid one first.

def get_valid_word(words):
    word = random.choice(words)  # random.choice is a powerful tool ...
    while '-' or ' ' in word:
        word = random.choice(words)
    # while loop will continue as long as there are 
    # dashes and spaces. When it hits one without 
    # dashes or spaces, it will exit the loop.
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)    # saves all the words in the letters as a set, to keep track of them.
    alphabet = set(string.ascii_uppercase) # this imports a pre-existing list of upper case Latin letters.
    used_letters = set() # what the user has guessed.

    # getting user input
    user_letter = input("Guess a letter: ").upper()
    if user_letter in alphabet - used_letters:   # Amazing. Didn't know you could subtract sets in Python.
        used_letters.add(user_letter)
        if user_letter in word_letters: # if that letter has already been used, you wouldn't get here.
            word_letters.remove(user_letter)


user_input = input("Type something: ")
print(user_input)
