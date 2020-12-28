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
        pass

class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)
    
    def get_move(self, game):
        pass

# we'll create another file for the game itself
