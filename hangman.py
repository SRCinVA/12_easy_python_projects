import random
from words import words #she has a large file that she created to find a random word

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
    word_letters = set(word)    # saves all the words in the letters as a set