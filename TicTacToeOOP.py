import random

class gameBoard(object):
    def __init__(self):
        self.board=[" "]*9
    def drawboard(self):
        print('   |   |')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('   |   |')
    def chosePlayer(self):
        if random.randint(0,1) == 1:
            print('Player 1 is X and Player 2 is O')
            return ['X', 'O']
        print('Player 1 is O and Player 2 is X')
        return ['O', 'X']
    def getPlayerMove(self):
        playerMove = int(input('what is your move player1 (1-9)?'))
        while playerMove > 9 or playerMove < 1:
            print('your number is not valid please enter a number from 1-9')
            playerMove = int(input())
        if playerMove <= 9 and playerMove >= 1:
            return playerMove
    def playerMove(self, player, move):
        madeMove = False
        while madeMove == False:
            if self.board[move] == '':
                self.board[move] = player
            print("This cell is already occupied, please select a different cell")
    def boardFull(self):
        for i in self.board:
            if not i == ' ':
                continue
            return True
        return False
