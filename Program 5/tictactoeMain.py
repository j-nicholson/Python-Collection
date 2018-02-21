import tictactoe
import json
import os.path

"""Main tic tac toe program run"""

if __name__ == '__main__':
    tictactoeMatch = tictactoe.TicTacToe()

    print('* * * Welcome to Tic Tac Toe * * *\n')

    while True:
        gameBoard = [' '] * 10
        playerLetter, computerLetter = 'O', 'X'
        turn = tictactoeMatch.chooseFirstPlayer()
        print('The ' + turn + ' will go first.')
        gamePlaying = True

        # Reads computerlosses.txt file at start of game to add losing boards if the file exists
        if os.path.isfile('computerlosses.txt'):
            with open('computerlosses.txt', 'r') as f:
                file_losses = json.load(f)
                for i, item in enumerate(file_losses):
                    # Appends bad moves from computerlosses.txt file to bad moves list if not currently in list
                    if item not in tictactoeMatch.getCaptureComputerLoss():
                        tictactoeMatch.captureComputerLoss(file_losses[i])
                tictactoeMatch.setComputerWinStatus(False)
            f.closed

        while gamePlaying:

            if turn == 'player':
                tictactoeMatch.drawboard(gameBoard)
                playerMove = tictactoeMatch.getPlayerMove(gameBoard)
                tictactoeMatch.move(gameBoard, playerLetter, playerMove)

                if tictactoeMatch.winner(gameBoard, playerLetter):
                    tictactoeMatch.drawboard(gameBoard)
                    tictactoeMatch.captureComputerLoss(tictactoeMatch.copyBoard(gameBoard))

                    # write player winning board to computerlosses.txt file
                    losses = tictactoeMatch.getCaptureComputerLoss()
                    with open('computerlosses.txt', 'w') as f:
                        # dump losses list as json data into computerlosses.txt file
                        json.dump(losses, f)
                    f.closed

                    tictactoeMatch.setComputerWinStatus(False)
                    print('You have won!')
                    gamePlaying = False
                else:
                    if tictactoeMatch.isBoardFull(gameBoard):
                        tictactoeMatch.drawboard(gameBoard)
                        print('This game ends in a tie!')
                        break
                    else:
                        turn = 'computer'

            else:
                tictactoeMatch.drawboard(gameBoard)
                if not (tictactoeMatch.getComputerWinStatus()):
                    computerMove = tictactoeMatch.getComputerMoveBasedOnLosingBoard(gameBoard, computerLetter)
                    tictactoeMatch.move(gameBoard, computerLetter, computerMove)
                else:
                    print('Yo Dawg this aint workin')
                    computerMove = tictactoeMatch.getComputerMove(gameBoard)
                    tictactoeMatch.move(gameBoard, computerLetter, computerMove)

                if tictactoeMatch.winner(gameBoard, computerLetter):
                    tictactoeMatch.drawboard(gameBoard)
                    print('The computer has won. You lose.')
                    gamePlaying = False
                else:
                    if tictactoeMatch.isBoardFull(gameBoard):
                        tictactoeMatch.drawboard(gameBoard)
                        print('This game ends in a tie!')
                        break
                    else:
                        turn = 'player'

        if not tictactoeMatch.rematch():
            break
