class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        # we will use a single list of length 9
        # that will represent the 3*3 board
        self.current_winner = None # to keep track of winner
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:  # need to unpack this.
        #this splits the board in rows
        # we make a list out of the elements, further divided into another list every third item.
        # this indexes into our len 9 list
            print('| ' + ' | '.join(row + ' |')
    
    @staticmethod # static methods are methods bound to the class, not the object