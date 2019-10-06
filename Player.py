
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

