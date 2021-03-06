import math
import random

class Player: # this is a "base" player for use later on.
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter
    
    #we want all players to get their next move given a game (??)
    def get_move(self, game):
        pass  #just a placeholder in code.

class RandomComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__    # super gives access to methods and properties in the parent or sibling class
                            # b/c you are inheriting here, you dont use 'self' (I guess?)
    def get_move(self,game):
        square = random.choice(game.available_moves)# the player can randomly start anywhere
                                                    # then we pass in game.available_moves (in other file)
        return square   # this just gives us a random valid spot


class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self, game):
        # before the player has input a letter to play
        valid_square = False # we want the human to be able to give input through the terminal
        val = None
        while not valid_square: # meaning, when the square is in fact valid ...
            square = input(self.letter + '\'s turn. Input move (0-8)')
            # now we have to make sure that the input is valid
            try:
                val = int(square)   # to make sure they actually put in an integer
                                    # if it can't be cast to an int, it will throw an error.
                if val not in game.available_moves():
                    raise ValueError     
                # if we pass both of those conditions, then we can go to the condition below:
                valid_square = True    
            # next, if we don't get to "True," then we "catch" that ValueError outside of the "try" block:
            except ValueError:
                print("Invalid square; try again!")   
        #after all of this, and we get a valid square, we return it and it becomes the human player's next move.
        return val
