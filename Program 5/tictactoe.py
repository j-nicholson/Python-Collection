import random

"""Class that contains methods needed to set up a Tic Tac Toe match."""
class TicTacToe:

    """Tic Tac Toe constructor"""
    def __init__(self):
        self.winningPlayerBoard = []
        self.computerWon = True

    """Draws tic tac toe board"""
    def drawboard(self, board):
        print('\n   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |\n')

    """Chooses first player"""
    def chooseFirstPlayer(self):
        return 'computer'

    """Asks for a rematch upon end of game"""
    def rematch(self):
        print('Would you like to play again? (y/n): ')
        return input().lower().startswith('y')

    """Places a player move at specified board location"""
    def move(self, board, letter, move):
        board[move] = letter

    """Checks winning combinations to see if a player has won the game"""
    def winner(self, board, letter):
        return ((board[7] == letter and board[8] == letter and board[9] == letter) or # across the top
        (board[4] == letter and board[5] == letter and board[6] == letter) or # across the middletter
        (board[1] == letter and board[2] == letter and board[3] == letter) or # across the top
        (board[7] == letter and board[4] == letter and board[1] == letter) or # down the left side
        (board[8] == letter and board[5] == letter and board[2] == letter) or # down the middle
        (board[9] == letter and board[6] == letter and board[3] == letter) or # down the right side
        (board[7] == letter and board[5] == letter and board[3] == letter) or # diagonal
        (board[9] == letter and board[5] == letter and board[1] == letter)) # diagonal

    """Returns a copy of the current tic tac toe board"""
    def copyBoard(self, board):
        boardCopy = []

        for i in board:
            boardCopy.append(i)

        return boardCopy

    """Checks to see if a specified space is free to make a legal move"""
    def spaceFree(self, board, move):
        return board[move] == ' '

    """Takes input for a player move, then returns the played move if it is legal"""
    def getPlayerMove(self, board):
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.spaceFree(board, int(move)):
            print('Enter a move (1-9): ')
            move = input()

        return int(move)

    """AI to make the computer choose a move if a space is free based on the provided possible move set"""
    def computerMove(self, board, movesList):
        possibleMoves = []
        for i in movesList:
            if self.spaceFree(board, i):
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

    """AI to make the computer choose a move based on lists of previous losses"""
    def getComputerMoveBasedOnLosingBoard(self, board, computerLetter):
        playerLetter = ''
        if computerLetter == 'X':
            playerLetter = 'O'
        else:
            playerLetter = 'X'

        for i in range(1, 10):
            copy = self.copyBoard(board)
            if self.spaceFree(copy, i):
                self.move(copy, computerLetter, i)
                if self.winner(copy, computerLetter):
                    return i

        for i in range(0, len(self.winningPlayerBoard)):
            for j in range(1, len(self.winningPlayerBoard[i])):
                if self.winningPlayerBoard[i][j] != computerLetter:
                    copy = self.copyBoard(board)
                    if self.spaceFree(copy, j):
                        self.move(copy, playerLetter, j)
                        if self.winner(copy, playerLetter):
                            return j

        return self.computerMove(board, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    """AI to make the computer choose a random move if available"""
    def getComputerMove(self, board):
        return self.computerMove(board, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    """Checks to see if the game board's spaces are full"""
    def isBoardFull(self, board):
        for i in range(1, 10):
            if self.spaceFree(board, i):
                return False

        return True

    """Captures a list containing the losing moves of the computer AI"""
    def captureComputerLoss(self, winningPlayerBoard):
        self.winningPlayerBoard.append(winningPlayerBoard)

    """Returns a list containing the losing moves of the computer AI"""
    def getCaptureComputerLoss(self):
        return self.winningPlayerBoard

    """Sets the specified win status of the computer"""
    def setComputerWinStatus(self, status):
        self.computerWon = status

    """Returns the current win status of the computer"""
    def getComputerWinStatus(self):
        return self.computerWon
