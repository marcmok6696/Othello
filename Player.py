# CSCI3180 Principles of Programming Languages
#
# --- Declaration ---
#
# I declare that the assignment here submitted is original except for source
# material explicitly acknowledged. I also acknowledge that I am aware of
# University policy and regulations on honesty in academic work, and of the
# disciplinary guidelines and procedures applicable to breaches of such policy
# and regulations, as contained in the website
# http://www.cuhk.edu.hk/policy/academichonesty/
#
# Assignment 2
# Name : MOK KA SHUN
# Student ID : 1155081387
# Email Addr : marcmokkashun@gmail.com

class Player:

    def __init__(self, symbol):
        self.playerSymbol = symbol

    def printa(self):
        print('this is player')

    def nextMove(self, board):
        while True:
            print("Player {}'s turn.".format(self.playerSymbol))
            rowcols = input('Type the row and col to put the disc: ').split()
            try:
                rowcols = list(map(int, rowcols))
                maprowcols = [rowcols[0] - 1, rowcols[1] - 1]
                if len(rowcols) != 2:
                    raise ValueError
                for i in rowcols:
                    if i > 8:
                        raise ValueError
                if board[rowcols[0] - 1][rowcols[1] - 1] != ' ':
                    raise ValueError
                if maprowcols not in validPos:
                    raise ValueError
                else:
                    return rowcols
                break
            except ValueError:
                print('Invalid Input.')

