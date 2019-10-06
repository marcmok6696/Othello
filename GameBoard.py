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

class GameBoard:
    def __init__(self):
        self.board = None
        self.validPos = None
    def init_gameBoard(self):
        self.board = [[' ' for i in range(8)] for i in range(8)]
        self.board[4][4] = 'X'
        self.board[3][3] = 'X'
        self.board[3][4] = 'O'
        self.board[4][3] = 'O'

    def check_ending(self):
        #check whether the game is over or not
        if self.check_legal_move('O') is False and self.check_legal_move('X') is False:
            return True
        else:
            return False
        #return True or False

    def checkup(self, x, symbol):
        if x[0] == 0:
            return False
        if self.board[x[0] - 1][x[1]] == ' ':
            return False
        if symbol == 'O':
            for i in range(0, x[0]):
                if self.board[i][x[1]] == 'X':
                    if i == 1:
                        return False
                    if self.board[i-1][x[1]] == ' ':
                        return [i-1, x[1]]
        elif symbol == 'X':
            for i in range(0, x[0]):
                if self.board[i][x[1]] == 'O':
                    if i == 1:
                        return False
                    if self.board[i-1][x[1]] == ' ':
                        return [i-1, x[1]]
        return False

    def checkdown(self, x, symbol):
        if x[0] == 7:
            return False
        if self.board[x[0] + 1][x[1]] == ' ':
            return False
        if symbol == 'O':
            for i in range(x[0], 8):
                if self.board[i][x[1]] == 'X':
                    if i == 7:
                        return False
                    if self.board[i+1][x[1]] == ' ':
                        return [i+1, x[1]]
        elif symbol == 'X':
            for i in range(x[0], 8):
                if self.board[i][x[1]] == 'O':
                    if i == 7:
                        return False
                    if self.board[i + 1][x[1]] == ' ':
                        return [i + 1, x[1]]
        return False

    def checkleft(self, x, symbol):
        if x[1] == 0:
            return False
        if self.board[x[0]][x[1]-1] == ' ':
            return False
        if symbol == 'O':
            for i in range(0, x[1]):
                if self.board[x[0]][i] == 'X':
                    if i == 1:
                        return False
                    if self.board[x[0]][i-1] == ' ':
                        return [x[0], i-1]
        elif symbol == 'X':
            for i in range(0, x[1]):
                if self.board[x[0]][i] == 'O':
                    if i == 1:
                        return False
                    if self.board[x[0]][i-1] == ' ':
                        return [x[0], i-1]
        return False

    def checkright(self, x, symbol):
        if x[1] == 7:
            return False
        if self.board[x[0]][x[1]+1] == ' ':
            return False
        if symbol == 'O':
            for i in range(x[1], 8):
                if self.board[x[0]][i] == 'X':
                    if i == 7:
                        return False
                    if self.board[x[0]][i+1] == ' ':
                        return [x[0], i+1]
        elif symbol == 'X':
            for i in range(x[1], 8):
                if self.board[x[0]][i] == 'O':
                    if i == 7:
                        return False
                    if self.board[x[0]][i + 1] == ' ':
                         return [x[0], i + 1]
        return False

    def checkupperleft(self, x, symbol):
        j = x[0]
        k = x[1]
        if x[0] == 0 or x[1] == 0:
            return False
        if self.board[x[0] - 1][x[1] - 1] == ' ':
            return False
        if symbol == 'O':
            if self.board[x[0]-1][x[1]-1] == 'X':
                while True:
                    if j == 0 or k == 0:
                        return False
                    if self.board[j-1][k-1] == 'X':
                        j = j - 1
                        k = k - 1
                    elif self.board[j-1][k-1] == ' ':
                        return [j-1, k-1]
                    elif self.board[j-1][k-1] == 'O':
                        return False
        elif symbol == 'X':
            if self.board[x[0]-1][x[1]-1] == 'O':
                while True:
                    if j == 0 or k == 0:
                        return False
                    if self.board[j-1][k-1] == 'O':
                        j = j - 1
                        k = k - 1
                    elif self.board[j-1][k-1] == ' ':
                        return [j-1, k-1]
                    elif self.board[j - 1][k - 1] == 'X':
                        return False
        return False

    def checkupperright(self, x, symbol):
        j = x[0]
        k = x[1]
        if x[0] == 0 or x[1] == 7:
            return False
        if self.board[x[0] - 1][x[1] + 1] == ' ':
            return False
        if symbol == 'O':
            if self.board[x[0]-1][x[1]+1] == 'X':
                while True:
                    if j == 0 or k == 7:
                        return False
                    if self.board[j-1][k+1] == 'X':
                        j = j - 1
                        k = k + 1
                    elif self.board[j-1][k+1] == ' ':
                        return [j-1, k+1]
                    elif self.board[j-1][k+1] == 'O':
                        return False
        elif symbol == 'X':
            if self.board[x[0]-1][x[1]+1] == 'O':
                while True:
                    if j == 0 or k == 7:
                        return False
                    if self.board[j-1][k+1] == 'O':
                        j = j - 1
                        k = k + 1
                    elif self.board[j-1][k+1] == ' ':
                        return [j-1, k+1]
                    elif self.board[j-1][k+1] == 'X':
                        return False
        return False

    def checkdownright(self, x, symbol):
        j = x[0]
        k = x[1]
        if x[0] == 7 or x[1] == 7:
            return False
        if self.board[x[0] + 1][x[1] + 1] == ' ':
            return False
        if symbol == 'O':
            if self.board[x[0]+1][x[1]+1] == 'X':
                while True:
                    if j == 7 or k == 7:
                        return False
                    if self.board[j+1][k+1] == 'X':
                        j = j + 1
                        k = k + 1
                    elif self.board[j+1][k+1] == ' ':
                        return [j+1, k+1]
                    elif self.board[j + 1][k + 1] == 'O':
                        return False
        elif symbol == 'X':
            if self.board[x[0]+1][x[1]+1] == 'O':
                while True:
                    if j == 7 or k == 7:
                        return False
                    if self.board[j+1][k+1] == 'O':
                        j = j + 1
                        k = k + 1
                    elif self.board[j+1][k+1] == ' ':
                        return [j+1, k+1]
                    elif self.board[j+1][k+1] == 'X':
                        return False
        return False

    def checkdownleft(self, x, symbol):
        j = x[0]
        k = x[1]
        if x[0] == 7 or x[1] == 0:
            return False
        if self.board[x[0] + 1][x[1] - 1] == ' ':
            return False
        if symbol == 'O':
            if self.board[x[0]+1][x[1]-1] == 'X':
                while True:
                    if j == 7 or k == 0:
                        return False
                    if self.board[j+1][k-1] == 'X':
                        j = j + 1
                        k = k - 1
                    elif self.board[j+1][k-1] == ' ':
                        return [j+1, k-1]
                    elif self.board[j+1][k-1] == 'O':
                        return False
        elif symbol == 'X':
            if self.board[x[0]+1][x[1]-1] == 'O':
                while True:
                    if j == 7 or k == 0:
                        return False
                    if self.board[j+1][k-1] == 'O':
                        j = j + 1
                        k = k - 1
                    elif self.board[j+1][k-1] == ' ':
                        return [j+1, k-1]
                    elif self.board[j+1][k-1] == 'X':
                        return False
        return False

    def check_legal_move(self, symbol):
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
            for i in range(0,8):
                for j in range(0,8):
                    if self.board[i][j] == 'O':
                        cirlist.append([i, j])
            for i in cirlist:
                checkuplist.append(self.checkup(i, symbol))
                checkdownlist.append(self.checkdown(i, symbol))
                checkleftlist.append(self.checkleft(i, symbol))
                checkrightlist.append(self.checkright(i, symbol))
                checkupperleftlist.append(self.checkupperleft(i, symbol))
                checkupperrightlist.append(self.checkupperright(i, symbol))
                checkdownleftlist.append(self.checkdownleft(i, symbol))
                checkdownrightlist.append(self.checkdownright(i, symbol))
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
            if len(checkuplist) == 0 and len(checkdownlist) == 0 and len(checkleftlist) == 0 and len(checkrightlist) == 0 and len(checkupperleftlist) == 0 and len(checkupperrightlist) == 0 and len(checkdownrightlist) == 0 and len(checkdownleftlist) == 0:
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
                self.validPos = validlist
                return True

        if symbol == 'X':
            for i in range(0, 8):
                for j in range(0, 8):
                    if self.board[i][j] == 'X':
                        croslist.append([i, j])

            for i in croslist:
                checkuplist.append(self.checkup(i, symbol))
                checkdownlist.append(self.checkdown(i, symbol))
                checkleftlist.append(self.checkleft(i, symbol))
                checkrightlist.append(self.checkright(i, symbol))
                checkupperleftlist.append(self.checkupperleft(i, symbol))
                checkupperrightlist.append(self.checkupperright(i, symbol))
                checkdownleftlist.append(self.checkdownleft(i, symbol))
                checkdownrightlist.append(self.checkdownright(i, symbol))
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
            if len(checkuplist) == 0 and len(checkdownlist) == 0 and len(checkleftlist) == 0 and len(checkrightlist) == 0 and len(checkupperleftlist) == 0 and len(checkupperrightlist) == 0 and len(checkdownrightlist) == 0 and len(checkdownleftlist) == 0:
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
                self.validPos = crosvalidlist
                return True
            return True
	    #check if their is a legal move given symbol
        #return True or False


    def check_winner(self):
        #return a list[s1,s2], represent the total number for O and X
        cir = 0
        cross = 0
        for i in range(0, 8):
            for j in range(0, 8):
                if self.board[i][j] == 'O':
                    cir = cir+1
                if self.board[i][j] == 'X':
                    cross = cross+1
        return [cir, cross]


    def execute_flip(self, pos, symbol):
        self.board[pos[0]-1][pos[1]-1] = symbol
        x = pos[0]
        y = pos[1]
        a = pos[0]
        c = pos[0]
        e = pos[0]
        b = pos[1]
        d = pos[1]
        f = pos[1]
        for i in range(pos[0], 8):
            if symbol =='O':
                if self.board[i][pos[1] - 1] == 'O':
                    if self.board[i][pos[1] - 1] == ' ':
                        break
                    j = i
                    for j in range(pos[0], j):
                        if self.board[j][pos[1]-1] == 'X':
                            self.board[j][pos[1]-1] = 'O'
                    break
            elif symbol =="X":
                if self.board[i][pos[1] - 1] == 'X':
                    if self.board[i][pos[1] - 1] == ' ':
                        break
                    j = i
                    for j in range(pos[0], j):
                        if self.board[j][pos[1] - 1] == 'O':
                            self.board[j][pos[1] - 1] = 'X'
                    break

        for i in range(0, pos[0]):
            if symbol == 'O':
                if self.board[i][pos[1] - 1] == 'O':
                    j = i
                    if self.board[i][pos[1] - 1] == ' ':
                        break
                    for j in range(j, pos[0]):
                        if self.board[j][pos[1] - 1] == 'X':
                            self.board[j][pos[1] - 1] = 'O'
                    break

            elif symbol == "X":
                if self.board[i][pos[1] - 1] == 'X':
                    if self.board[i][pos[1] - 1] == ' ':
                        break
                    j = i
                    for j in range(j, pos[0]):
                        if self.board[j][pos[1] - 1] == 'O':
                            self.board[j][pos[1] - 1] = 'X'
                    break
        #left right
        for i in range(pos[1], 8):
            if symbol =='O':
                if self.board[pos[0]-1][i] == 'O':
                    if self.board[pos[0] - 1][i] == ' ':
                        break
                    j = i
                    for j in range(pos[1], j):
                        if self.board[pos[0]-1][j] == 'X':
                            self.board[pos[0]-1][j] = 'O'
                    break
            elif symbol =="X":
                if self.board[pos[0]-1][i] == 'X':
                    if self.board[pos[0] - 1][i] == ' ':
                        break
                    j = i
                    for j in range(pos[1], j):
                        if self.board[pos[0] - 1][j] == 'O':
                            self.board[pos[0] - 1][j] = 'X'
                    break

        for i in range(0, pos[1]):
            if symbol == 'O':
                if self.board[pos[0]-1][i] == 'O':
                    if self.board[pos[0] - 1][i] == ' ':
                        break
                    j = i
                    for j in range(j, pos[1]):
                        if self.board[pos[0]-1][j] == 'X':
                            self.board[pos[0]-1][j] = 'O'
                    break

            elif symbol == "X":
                if self.board[pos[0]-1][i] == 'X':
                    j = i
                    if self.board[pos[0] - 1][i] == ' ':
                        break
                    for j in range(j, pos[1]):
                        if self.board[pos[0]-1][j] == 'O':
                            self.board[pos[0]-1][j] = 'X'
                    break
       #downleft right
        while True:
            j = pos[0]
            k = pos[1]
            if symbol == "O":
                if x == 8 or y == 8:
                    break
                if self.board[x][y] == '':
                    break
                if self.board[x][y] == 'O':
                    while j != x or k != y:
                        if self.board[j][k] == ' ':
                            break
                        elif self.board[j][k] == 'X':
                            self.board[j][k] = 'O'
                        j = j+1
                        k = k+1

            if symbol == "X":
                if x == 8 or y == 8:
                    break
                if self.board[x][y] == '':
                    break
                if self.board[x][y] == 'X':
                    while j != x or k != y:
                        if self.board[j][k] == ' ':
                            break
                        elif self.board[j][k] == 'O':
                            self.board[j][k] = 'X'
                        j = j + 1
                        k = k + 1
            x = x+1
            y = y+1
        #down left
        while True:
            j = pos[0]
            k = pos[1]
            if symbol == "O":
                if a == 8 or b == 0:
                    break
                if self.board[a][b - 2] == ' ':
                    break
                if self.board[a][b - 2] == 'O':
                    while j != a or k != b:
                        if self.board[j][k - 2] == ' ':
                            break
                        elif self.board[j][k-2] == 'X':
                            self.board[j][k-2] = 'O'
                        j = j + 1
                        k = k - 1

            if symbol == "X":
                if a == 8 or b == 0:
                    break
                if self.board[a][b - 2] == ' ':
                    break
                if self.board[a][b - 2] == 'X':
                    while j != a or k != b:
                        if self.board[j][k - 2] == ' ':
                            break
                        elif self.board[j][k - 2] == 'O':
                            self.board[j][k - 2] = 'X'
                        j = j + 1
                        k = k - 1
            a = a + 1
            b = b - 1
        #upperright

        while True:
            j = pos[0]
            k = pos[1]
            if symbol == "O":
                if c == 0 or d == 8:
                    break
                if self.board[c-2][d] == ' ':
                    break
                if self.board[c-2][d] == 'O':
                    while j != c or k != d:
                        if self.board[j - 2][k] == ' ':
                            break
                        elif self.board[j - 2][k] == 'X':
                            self.board[j - 2][k] = 'O'
                        j = j - 1
                        k = k + 1

            if symbol == "X":
                if c == 0 or d == 8:
                    break
                if self.board[c - 2][d] == ' ':
                    break
                if self.board[c - 2][d] == 'X':
                    while j != c or k != d:
                        if self.board[j - 2][k] == ' ':
                            break
                        elif self.board[j - 2][k] == 'O':
                            self.board[j - 2][k] = 'X'
                        j = j - 1
                        k = k + 1

            c = c - 1
            d = d + 1
        #upper left
        while True:
            j = pos[0]
            k = pos[1]
            if symbol == "O":
                if e == 0 or f == 0:
                    break
                if self.board[e - 2][f - 2] == ' ':
                    break
                if self.board[e - 2][f - 2] == 'O':
                    while j != e or k != f:
                        if self.board[j - 2][k - 2] == ' ':
                            break
                        elif self.board[j - 2][k - 2] == 'X':
                            self.board[j - 2][k - 2] = 'O'
                        j = j - 1
                        k = k - 1

            if symbol == "X":
                if e == 0 or f == 8:
                    break
                if self.board[c - 2][d - 2] == ' ':
                    break
                if self.board[c - 2][d - 2] == 'X':
                    while j != e or k != f:
                        if self.board[j - 2][k - 2] == ' ':
                            break
                        elif self.board[j - 2][k - 2] == 'O':
                            self.board[j - 2][k - 2] = 'X'
                        j = j - 1
                        k = k - 1

            e = e - 1
            f = f - 1

    def printGameBoard(self):
        print("  | ",end="")
        for k in range(0,8):


            print(str(k+1) + " | ", end="")
        print("\n-----------------------------------")
        for i in range (0,8):
            print(str(i+1) + " | ", end="")
            for j in range (0,8):
                print(self.board[i][j]+" | ",end="")
            print("\n-----------------------------------")
