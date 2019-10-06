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

import sys
import random

from GameBoard import GameBoard
from Human import Human
from Computer import Computer

class Othello:

    def __init__(self):
        self.gameBoard = GameBoard()
        self.player1 = None
        self.player2 = None
        self.turn = 0


    def createPlayer(self, symbol, playerNum):
        while True:
            p1 = input('Please choose player {} ({}): \n1. Human \n2. Computer Player \nYour choice is: '.format(playerNum, symbol))
            try:
                p1 = int(p1)
                if p1 == 1:
                    if playerNum == 1:
                        print('Player O is Human.')
                        return Human(symbol)
                    elif playerNum == 2:
                        print('Player X is Human.')
                        return Human(symbol)
                    else:
                        print('Invalid Input.')
                elif p1 == 2:
                    if playerNum == 1:
                        print('Player O is Computer.')
                        return Computer(symbol)
                    elif playerNum == 2:
                        print('Player X is Computer.')
                        return Computer(symbol)
                    else:
                        print('Invalid Input.')
                else:
                    print('Invalid Input.')
            except ValueError:
                print('Invalid Input.')

    def startGame(self):
	    #basic logic
        self.player1 = self.createPlayer('O', 1)
        self.player2 = self.createPlayer('X', 2)
        self.gameBoard.init_gameBoard()
        self.gameBoard.printGameBoard()

        while not self.gameBoard.check_ending():

            current_player = [self.player1, self.player2][self.turn]
            if self.gameBoard.check_legal_move(current_player.playerSymbol):
                pos = current_player.nextMove(self.gameBoard.board)
                self.gameBoard.execute_flip(pos, current_player.playerSymbol)
            self.turn = 1 - self.turn
            self.gameBoard.printGameBoard()
        s1, s2 = self.gameBoard.check_winner()
        if s1 > s2:
            winner = 'O'  # Black
        elif s1 < s2:
            winner = 'X'  # White
        elif s1 == s2:
            winner = ' '  # Tie

        print('Count O : {}'.format(s1))
        print('Count X : {}'.format(s2))
        if winner != ' ':
            print('Player {} won!\n'.format(winner))
        else:
            print('A tie')


if __name__ == "__main__":
    othello = Othello()
    othello.startGame()

