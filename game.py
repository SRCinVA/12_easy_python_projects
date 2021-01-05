class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        # we will use a single list of length 9
        # that will represent the 3*3 board
        self.current_winner = None # to keep track of winner
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:  
        # Line 9 creates a slice (from "start" to "end," exclusive of "end")
        # Range() in Python is exclusive of user's input, so this encompasses 0,1,2
        # the range bracket creates three "self-contained" slices of indices, like this:
            # [0,1,2],[3,4,5],[6,7,8]
        # we make a list out of the elements, further divided into another list every third item.
        # it indexes into our len 9 list
        
            print('| ' + ' | '.join(row) + ' |')
            # print the first pipe; join() method intersperses the pipe between the iterables; print the last pipe.
    
    @staticmethod # static methods are methods bound to the class, not the object
    def print_board_nums(): # this doesn't relate to any specific board, so we don't have to pass in self (makes sense).
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        # inner list gives the indices present in a single row.
        # outer list gives all of the rows.
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        # the long way to do it:
        # moves = []  # initialize moves to an empty list.
        # for (i,spot) in enumerate(self.board): # basically, it attaches an object to its index place.
        #     # ['x','x','o'] --> [(0,'x'),(1,'x'),(2,'o')]
        #     if spot == ' ':  # meaning that it's empty and available for use.
        #         moves.append(i)  # we append that index to know that it's been taken. 
        #         return moves
    
        # using list comprehension:
        return [i for i, spot in emumerate(self.board) if spot == ' ']
        # basically, this says: "when enumerating through (i, spot),
        # if the spot is empty, put it into this list." (where is 'moves' here?)

    def empty_squares(self):
        # return ' ' in self.board # this will just return a boolean if the selection is an empty space
        return self.board.count(' ') # she opted to just count the spaces in the board; seems easier


    # we might want to know the number of empty squares
    def num_empty_squares(self):
        return len(self.available_moves())
        # the above will retutn the available_moves list, and we can count the number of empty spots

    # to actually make a move
    def make_move(self, square, letter):
        # if we're going to make a move, then we need to be sure it's valid
        # If valid, it returns True; if not, then False
        if self.board[square] == ' ': # if that square on the board is empty ...
            self.board[square] = letter # ... then put the letter in that space.
            return True
        else:
            return False



# notice that this function exists outside of the TicTacToe class

def play(game, x_player, o_player, print_game=True):
    if print_game: #meaning, if we want to see it
        game.print_board_nums # this way we can see which number corresonds to which spot.

    letter = "X" # a starting letter
    # iterate while the game has empty squares
    # (we don't have to worry about a winner because we'll
    # just return whatever breaks the loop).

    # she calls this "the play loop" (which makes sense):
    while game.empty_squares(): # for checking if the game has empty squares
        # while there are emptyspaces, let's get the next move from the appropriate player
        if letter == "0":
            square = o_player.get_move(game)
        else:
            square = x_player.getmove(game)

    # define a function to actually make a move
        if game.make_move(square, letter): # meaning, "is valid":
            if print_game:
                print(letter + f' makes a move to square {square}')

