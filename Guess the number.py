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

guess(10)
