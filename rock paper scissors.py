import random

def play():
    player = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissor")
    opponent = random.choice(['r','p','s'])
    # r > s, s > p, p > r

    if player == opponent:
        return 'It\'s a tie'

    if is_win(player, opponent): # a shorthand way of saying "if is_win is True"
        return 'You won!'

    return 'You lost!'     # notice that you don't even need "else" here; the only 
                            # the only way you reach this line is for the 
                            # previous 'if' statements to fail.

def is_win(player, opponent):  # this is a helper function
    # return true if player wins
    if (player == 'r' and opponent == 's') \
        or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())  # you have to print out the play function; it's the essence of the game.

# somehting was wrong with her code: she did not define 'player'
# to fix it, I made "user" (which was in fact defined) the "player", and 'computer' into 'opponent'.
# 