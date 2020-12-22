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

    lives = 6

    # getting user input
    while len(word_letters > 0) and lives > 0:
        # to help out your users, print out the letters they've already used
        print("You have ", lives, " left and you've already used these letters: ', '".join(used_letters)) # .join iterates over an iterable and turns them into a string.

        # tell them what the current word is, with dashes indicating unguessed letters.
        word_list = [letter if letter in used_letters else '-' for letter in word]  
        print('Current word: ', ' '.join(word_list)) # not sure what's going on with this one.

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:   # Amazing. Didn't know you could subtract sets in Python.
            used_letters.add(user_letter)   # if you guess a letter, and it's still an option in the remaining alphabet, it gets added to used_letters.
            if user_letter in word_letters: # if that letter is already depleted, you wouldn't even get to the inner if statement. NOW it tests against word_letters.
                word_letters.remove(user_letter) # if that letter is present in word_letters, it's removed (and you get it right).

            else:
                lives = lives - 1
                print('Sorry, that letter\'s not in the word.')

        elif user_letter in used_letter:
            print("you've already used this one, dog. Try again.")

        else:
            print("This is an invalid character.")

    if lives == 0:
        print("Game over, bruh.")
    else:
        ("You guessed the word", word, "!!")

    # gets here when len(word_letters) == 0

user_input = input("Type something: ")
print(user_input)
