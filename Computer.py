
from Player import Player
import random
class Computer(Player):
    def checkup(self, x, symbol,board):
        selfboard= board
        if x[0] == 0:
            return False
        if selfboard[x[0] - 1][x[1]] == ' ':
            return False
        if symbol == 'O':
            for i in range(0, x[0]):
                if selfboard[i][x[1]] == 'X':
                    if i == 1:
                        return False
                    if selfboard[i-1][x[1]] == ' ':
                        return [i-1, x[1]]
        elif symbol == 'X':
            for i in range(0, x[0]):
                if selfboard[i][x[1]] == 'O':
                    if i == 1:
                        return False
                    if selfboard[i-1][x[1]] == ' ':
                        return [i-1, x[1]]
        return False

    def checkdown(self, x, symbol, board):
        selfboard = board
        if x[0] == 7:
            return False
        if selfboard[x[0] + 1][x[1]] == ' ':
            return False
        if symbol == 'O':
            for i in range(x[0], 8):
                if selfboard[i][x[1]] == 'X':
                    if i == 7:
                        return False
                    if selfboard[i+1][x[1]] == ' ':
                        return [i+1, x[1]]
        elif symbol == 'X':
            for i in range(x[0], 8):
                if selfboard[i][x[1]] == 'O':
                    if i == 7:
                        return False
                    if selfboard[i + 1][x[1]] == ' ':
                        return [i + 1, x[1]]
        return False

    def checkleft(self, x, symbol, board):
        selfboard = board
        if x[1] == 0:
            return False
        if selfboard[x[0]][x[1]-1] == ' ':
            return False
        if symbol == 'O':
            for i in range(0, x[1]):
                if selfboard[x[0]][i] == 'X':
                    if i == 1:
                        return False
                    if selfboard[x[0]][i-1] == ' ':
                        return [x[0], i-1]
        elif symbol == 'X':
            for i in range(0, x[1]):
                if selfboard[x[0]][i] == 'O':
                    if i == 1:
                        return False
                    if selfboard[x[0]][i-1] == ' ':
                        return [x[0], i-1]
        return False

    def checkright(self, x, symbol, board):
        selfboard= board
        if x[1] == 7:
            return False
        if selfboard[x[0]][x[1]+1] == ' ':
            return False
        if symbol == 'O':
            for i in range(x[1], 8):
                if selfboard[x[0]][i] == 'X':
                    if i == 7:
                        return False
                    if selfboard[x[0]][i+1] == ' ':
                        return [x[0], i+1]
        elif symbol == 'X':
            for i in range(x[1], 8):
                if selfboard[x[0]][i] == 'O':
                    if i == 7:
                        return False
                    if selfboard[x[0]][i + 1] == ' ':
                         return [x[0], i + 1]
        return False

    def checkupperleft(self, x, symbol, board):
        selfboard = board
        j = x[0]
        k = x[1]
        if x[0] == 0 or x[1] == 0:
            return False
        if selfboard[x[0] - 1][x[1] - 1] == ' ':
            return False
        if symbol == 'O':
            if selfboard[x[0]-1][x[1]-1] == 'X':
                while True:
                    if j == 0 or k == 0:
                        return False
                    if selfboard[j-1][k-1] == 'X':
                        j = j - 1
                        k = k - 1
                    elif selfboard[j-1][k-1] == ' ':
                        return [j-1, k-1]
                    elif selfboard[j-1][k-1] == 'O':
                        return False
        elif symbol == 'X':
            if selfboard[x[0]-1][x[1]-1] == 'O':
                while True:
                    if j == 0 or k == 0:
                        return False
                    if selfboard[j-1][k-1] == 'O':
                        j = j - 1
                        k = k - 1
                    elif selfboard[j-1][k-1] == ' ':
                        return [j-1, k-1]
                    elif selfboard[j - 1][k - 1] == 'X':
                        return False
        return False

    def checkupperright(self, x, symbol, board):
        selfboard = board
        j = x[0]
        k = x[1]
        if x[0] == 0 or x[1] == 7:
            return False
        if selfboard[x[0] - 1][x[1] + 1] == ' ':
            return False
        if symbol == 'O':
            if selfboard[x[0]-1][x[1]+1] == 'X':
                while True:
                    if j == 0 or k == 7:
                        return False
                    if selfboard[j-1][k+1] == 'X':
                        j = j - 1
                        k = k + 1
                    elif selfboard[j-1][k+1] == ' ':
                        return [j-1, k+1]
                    elif selfboard[j-1][k+1] == 'O':
                        return False
        elif symbol == 'X':
            if selfboard[x[0]-1][x[1]+1] == 'O':
                while True:
                    if j == 0 or k == 7:
                        return False
                    if selfboard[j-1][k+1] == 'O':
                        j = j - 1
                        k = k + 1
                    elif selfboard[j-1][k+1] == ' ':
                        return [j-1, k+1]
                    elif selfboard[j-1][k+1] == 'X':
                        return False
        return False

    def checkdownright(self, x, symbol,board):
        selfboard = board
        j = x[0]
        k = x[1]
        if x[0] == 7 or x[1] == 7:
            return False
        if selfboard[x[0] + 1][x[1] + 1] == ' ':
            return False
        if symbol == 'O':
            if selfboard[x[0]+1][x[1]+1] == 'X':
                while True:
                    if j == 7 or k == 7:
                        return False
                    if selfboard[j+1][k+1] == 'X':
                        j = j + 1
                        k = k + 1
                    elif selfboard[j+1][k+1] == ' ':
                        return [j+1, k+1]
                    elif selfboard[j + 1][k + 1] == 'O':
                        return False
        elif symbol == 'X':
            if selfboard[x[0]+1][x[1]+1] == 'O':
                while True:
                    if j == 7 or k == 7:
                        return False
                    if selfboard[j+1][k+1] == 'O':
                        j = j + 1
                        k = k + 1
                    elif selfboard[j+1][k+1] == ' ':
                        return [j+1, k+1]
                    elif selfboard[j+1][k+1] == 'X':
                        return False
        return False

    def checkdownleft(self, x, symbol, board):
        selfboard = board
        j = x[0]
        k = x[1]
        if x[0] == 7 or x[1] == 0:
            return False
        if selfboard[x[0] + 1][x[1] - 1] == ' ':
            return False
        if symbol == 'O':
            if selfboard[x[0]+1][x[1]-1] == 'X':
                while True:
                    if j == 7 or k == 0:
                        return False
                    if selfboard[j+1][k-1] == 'X':
                        j = j + 1
                        k = k - 1
                    elif selfboard[j+1][k-1] == ' ':
                        return [j+1, k-1]
                    elif selfboard[j+1][k-1] == 'O':
                        return False
        elif symbol == 'X':
            if selfboard[x[0]+1][x[1]-1] == 'O':
                while True:
                    if j == 7 or k == 0:
                        return False
                    if selfboard[j+1][k-1] == 'O':
                        j = j + 1
                        k = k - 1
                    elif selfboard[j+1][k-1] == ' ':
                        return [j+1, k-1]
                    elif selfboard[j+1][k-1] == 'X':
                        return False
        return False

    def check_legal_move(self, symbol, board):
        selfboard = board
        cirlist = []
        croslist = []
        validlist = []
        crosvalidlist = []
        checkuplist = []
        checkdownlist = []
        checkleftlist = []
        checkrightlist = []
        checkupperleftlist = []
        checkupperrightlist = []
        checkdownleftlist = []
        checkdownrightlist = []
        if symbol == 'O':
            for i in range(0, 8):
                for j in range(0, 8):
                    if selfboard[i][j] == 'O':
                        cirlist.append([i, j])
            for i in cirlist:
                checkuplist.append(self.checkup(i, symbol,selfboard))
                checkdownlist.append(self.checkdown(i, symbol,selfboard))
                checkleftlist.append(self.checkleft(i, symbol,selfboard))
                checkrightlist.append(self.checkright(i, symbol,selfboard))
                checkupperleftlist.append(self.checkupperleft(i, symbol,selfboard))
                checkupperrightlist.append(self.checkupperright(i, symbol,selfboard))
                checkdownleftlist.append(self.checkdownleft(i, symbol,selfboard))
                checkdownrightlist.append(self.checkdownright(i, symbol,selfboard))
                if False in checkuplist:
                    checkuplist.remove(False)
                if False in checkdownlist:
                    checkdownlist.remove(False)
                if False in checkleftlist:
                    checkleftlist.remove(False)
                if False in checkrightlist:
                    checkrightlist.remove(False)
                if False in checkupperleftlist:
                    checkupperleftlist.remove(False)
                if False in checkupperrightlist:
                    checkupperrightlist.remove(False)
                if False in checkdownrightlist:
                    checkdownrightlist.remove(False)
                if False in checkdownleftlist:
                    checkdownleftlist.remove(False)
            if len(checkuplist) == 0 and len(checkdownlist) == 0 and len(checkleftlist) == 0 and len(
                    checkrightlist) == 0 and len(checkupperleftlist) == 0 and len(checkupperrightlist) == 0 and len(
                    checkdownrightlist) == 0 and len(checkdownleftlist) == 0:
                print('There is no valid move for Player O.')
                return False
            else:
                if len(checkuplist) > 0:
                    for i in checkuplist:
                        validlist.append(i)
                if len(checkdownlist) > 0:
                    for i in checkdownlist:
                        validlist.append(i)
                if len(checkleftlist) > 0:
                    for i in checkleftlist:
                        validlist.append(i)
                if len(checkrightlist) > 0:
                    for i in checkrightlist:
                        validlist.append(i)
                if len(checkupperleftlist) > 0:
                    for i in checkupperleftlist:
                        validlist.append(i)
                if len(checkupperrightlist) > 0:
                    for i in checkupperrightlist:
                        validlist.append(i)
                if len(checkdownleftlist) > 0:
                    for i in checkdownleftlist:
                        validlist.append(i)
                if len(checkdownrightlist) > 0:
                    for i in checkdownrightlist:
                        validlist.append(i)
                return validlist

        if symbol == 'X':
            for i in range(0, 8):
                for j in range(0, 8):
                    if selfboard[i][j] == 'X':
                        croslist.append([i, j])

            for i in croslist:
                checkuplist.append(self.checkup(i, symbol,selfboard))
                checkdownlist.append(self.checkdown(i, symbol,selfboard))
                checkleftlist.append(self.checkleft(i, symbol,selfboard))
                checkrightlist.append(self.checkright(i, symbol,selfboard))
                checkupperleftlist.append(self.checkupperleft(i, symbol,selfboard))
                checkupperrightlist.append(self.checkupperright(i, symbol,selfboard))
                checkdownleftlist.append(self.checkdownleft(i, symbol,selfboard))
                checkdownrightlist.append(self.checkdownright(i, symbol,selfboard))
                if False in checkuplist:
                    checkuplist.remove(False)
                if False in checkdownlist:
                    checkdownlist.remove(False)
                if False in checkleftlist:
                    checkleftlist.remove(False)
                if False in checkrightlist:
                    checkrightlist.remove(False)
                if False in checkupperleftlist:
                    checkupperleftlist.remove(False)
                if False in checkupperrightlist:
                    checkupperrightlist.remove(False)
                if False in checkdownrightlist:
                    checkdownrightlist.remove(False)
                if False in checkdownleftlist:
                    checkdownleftlist.remove(False)
            if len(checkuplist) == 0 and len(checkdownlist) == 0 and len(checkleftlist) == 0 and len(
                    checkrightlist) == 0 and len(checkupperleftlist) == 0 and len(checkupperrightlist) == 0 and len(
                    checkdownrightlist) == 0 and len(checkdownleftlist) == 0:
                print('There is no valid move for Player X.')
                return False
            else:
                if len(checkuplist) > 0:
                    for i in checkuplist:
                        crosvalidlist.append(i)
                if len(checkdownlist) > 0:
                    for i in checkdownlist:
                        crosvalidlist.append(i)
                if len(checkleftlist) > 0:
                    for i in checkleftlist:
                        crosvalidlist.append(i)
                if len(checkrightlist) > 0:
                    for i in checkrightlist:
                        crosvalidlist.append(i)
                if len(checkupperleftlist) > 0:
                    for i in checkupperleftlist:
                        crosvalidlist.append(i)
                if len(checkupperrightlist) > 0:
                    for i in checkupperrightlist:
                        crosvalidlist.append(i)
                if len(checkdownleftlist) > 0:
                    for i in checkdownleftlist:
                        crosvalidlist.append(i)
                if len(checkdownrightlist) > 0:
                    for i in checkdownrightlist:
                        crosvalidlist.append(i)
                return crosvalidlist
            return True

    def nextMove(self, board):
        validPos = self.check_legal_move(self.playerSymbol, board)
        while True:
            print("Player {}'s turn.".format(self.playerSymbol))
            rowcols = random.choice(validPos)
            break
        row = rowcols[0] + 1
        col = rowcols[1] + 1
        return [row,col]
