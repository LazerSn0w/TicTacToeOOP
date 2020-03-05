import random
class gameBoard(object):
    def __init__(self):
        """
        Initialize board
        """
        self.board = [' '] * 9
    def drawBoard(self):
        """
        Function that draws board
        """
        print('   |   |')
        print(' ' + self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2])
        print('   |   |')
    def choosePlayer(self):
        """
        :return: List of random permutation of X and O
        """
        if random.randint(0, 1) == 1:
            print('Player 1 is X and Player 2 is O')
            return ['X', 'O']
        print('Player 1 is O and Player 2 is X')
        return ['O', 'X']
    def chooseStarter(self):
        """
        :return: Randomly returns either Player 1 or Player 2
        """
        if random.randint(0, 1) == 1:
            return "Player 1"
        return "Player 2"
    def getPlayerMove(self):
        """
        :return: Player's move
        """
        playerMove = int(input('What is your move (0-8)?'))
        while playerMove > 8 or playerMove < 0:
            print('Your number is not valid please enter a number from 0-8')
            playerMove = int(input())
        if 8 >= playerMove >= 0:
            return playerMove
    def playerMove(self, playerValue, move):
        """
        :param playerValue: Player's value (X or O)
        :param move: Player's move
        Adds players's value to designated spot on board
        """
        madeMove = False
        while not madeMove:
            if self.board[move] == ' ':
                self.board[move] = playerValue
                madeMove = True
            else:
                print("This cell is already occupied, your turn will be skipped.")
                break
    def isWinner(self, playerValue):
        """
        Checks for all 3 in a row combinations
        :return: Returns true if playerValue makes 3 in a row
        """
        return ((self.board[6] == playerValue and self.board[7] == playerValue and self.board[8] == playerValue) or
                (self.board[3] == playerValue and self.board[4] == playerValue and self.board[5] == playerValue) or
                (self.board[0] == playerValue and self.board[1] == playerValue and self.board[2] == playerValue) or
                (self.board[6] == playerValue and self.board[3] == playerValue and self.board[0] == playerValue) or
                (self.board[7] == playerValue and self.board[4] == playerValue and self.board[1] == playerValue) or
                (self.board[8] == playerValue and self.board[5] == playerValue and self.board[2] == playerValue) or
                (self.board[6] == playerValue and self.board[4] == playerValue and self.board[2] == playerValue) or
                (self.board[8] == playerValue and self.board[4] == playerValue and self.board[0] == playerValue))
    def boardFull(self):
        """
        Checks if all cells are used up
        :return: Returns True if it is
        """
        cellsUsed = 0
        for cell in self.board:
            if not cell == ' ':
                cellsUsed += 1
            if cellsUsed == 9:
                return True
        return False
    def boardReset(self):
        """
        Resets board to original state
        """
        self.board = [" "] * 9
    def playAgain(self):
        """
        Asks user whether they want to play again
        :return: Returns True if yes
        """
        x = input('Do you wan to play again? Type "Y" ')
        x = input('Do you want to play again? Type "Y" ')
        if x == "Y":
            return True
        return False
    def rules(self):
        """
        Asks player whether they want to see the rules
        If yes display rules
        """
        x = input('Would you like to see the rules. Type "Y" ')
        if x == 'Y':
            print('Rules of the game:')
            print("""    1. The game is played on a 3x3 grid.
    2. There are two players, X and O who are randomly chosen.
    3. Players take turn putting their marks on an empty cell.
    4. The first player to get 3 of their marks in a row wins!
    5. If all 9 cells are used up and no one has won, the game ends in a tie""")
            print('Good luck! and have fun')
            print('   |   |')
            print(' ' + '6' + ' | ' + '7' + ' | ' + '8')
            print('   |   |')
            print('-----------')
            print('   |   |')
            print(' ' + '3' + ' | ' + '4' + ' | ' + '5')
            print('   |   |')
            print('-----------')
            print('   |   |')
            print(' ' + '0' + ' | ' + '1' + ' | ' + '2')
            print('   |   |')
print('Welcome to Tic Tac Toe')
board = gameBoard()
while True:
    board.boardReset()
    board.rules()
    player1, player2 = board.choosePlayer()
    turn = board.chooseStarter()
    game = True
    while game:
        if turn == 'Player 1':
            print()
            print('Player 1 turn')
            board.drawBoard()
            move = board.getPlayerMove()
            board.playerMove(player1, move)
            if board.isWinner(player1):
                board.drawBoard()
                print('Hooray! Player 1 has won')
                game = False
            else:
                if board.boardFull():
                    board.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 2'
        if turn == 'Player 2':
            print()
            print('Player 2 turn')
            board.drawBoard()
            move = board.getPlayerMove()
            board.playerMove(player2, move)
            if board.isWinner(player2):
                board.drawBoard()
                print('Hooray! Player 2 has won!')
                gameIsPlaying = False
            else:
                if board.boardFull():
                    board.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'
    if not board.playAgain():
        break
