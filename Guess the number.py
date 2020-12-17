import random

def guess(x):
    random_number = random.randint(1, x)
    # once the computer has selected a number, now we need to guess
    guess = 0   # we don't want our guess to initialize the variable
                # to something that could be the random number.
                # otherwise, the game would be over before it began
    while guess != random_number:          # remember: while loops are good for undefined situations
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print("Too low!! Try again ...")
        elif guess > random_number:
            print("Whoa, Tex!! A little too high there ...")

    print(f"Badda-bing! With {random_number}, you nailed it.")


def computer_guess(x):
    low = 1   # to initialize low
    high = x  # to initialize high
    feedback = ''
    while feedback != 'c':
        if low != high:     # if low == high, random throws an error
            guess = random.randint(low,high)  # so the machine goes ahead to offer a number within these ever-narrowing range
        else:
            guess = low # but could also be high. This is just a place to park the guess.
                        # what we're trying to do is get the user to say "c."
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?').lower()
        if feedback == 'h':
            high = guess - 1 # this resets the upper bound of the randint range
        elif feedback == 'l':
            low = guess + 1 # this resets the lower bound of the randint range
    print(f'Excellent! The computer guessed your number, {guess}, correctly!')

computer_guess(1000)
