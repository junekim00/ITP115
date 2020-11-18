# June Kim
# ITP115, Fall 2019
# Assignment 7
# junek@usc.edu
# This program allows for a game of tic-tac-toe.


import random
import TicTacToeHelper


# checking to see if spot is open or not
def isValidMove(boardList, spot):
    if boardList[spot] == "x" or boardList[spot] == "o":
        return False
    else:
        return True


# updating board to match move
def updateBoard(boardList, spot, playerLetter):
    boardList[spot] = playerLetter


# extra credit pretty board
def printPrettyBoard(boardList):
    for x in range(3):
        for y in range(3):
            number = 3 * x + y
            if y != 2:
                print(" " + str(boardList[number]) + " |", end="")
            else:
                print(" " + str(boardList[number]), end="")
        print("\n", end="")
        if x != 2:
            print("------------")

# gameplay
def playGame():
    counter = 0
    xTurn = True
    board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    check = TicTacToeHelper.checkForWinner(board, counter)
    computer = input("Would you like to play against a computer? (y/n)").lower()
    if computer != "y" and computer!= "n":
        print("Invalid option!")
        computer = input("Would you like to play against a computer? (y/n)").lower()
    # play against computer
    if computer == "y":
        while check == "n":
            # start game
            printPrettyBoard(board)
            # Player X turn
            if xTurn == True:
                move = int(input("Player x, pick a spot: "))
                counter += 1
                if isValidMove(board, move) == False:
                    print("Invalid move, please try again.")
                    move = int(input("Player x, pick a spot: "))
                updateBoard(board, move, "x")
                xTurn = False
                check = TicTacToeHelper.checkForWinner(board, counter)
            else:
                move = random.randint(0,8)
                counter += 1
                while isValidMove(board, move) == False:
                    move = random.randint(0,8)
                else:
                    updateBoard(board, move, "o")
                    print("Computer chose " + str(move) + ".")
                xTurn = True
                check = TicTacToeHelper.checkForWinner(board, counter)
        if check == "s":
            print("Game Over!\nStalemate reached!")
        if check == "x":
            print("Game Over!\nPlayer x is the winner!")
        elif check == "o":
            print("Game Over!\nPlayer o is the winner!")
    # extra credit choose which player starts
    if computer == "n":
        startPlayer = input("Who would you like to start? (x/o)").lower()
        while startPlayer != "x" and startPlayer != "o":
            print("Invalid option! ")
            startPlayer = input("Who would you like to start? (x/o)").lower()
        if startPlayer == "x":
            xTurn = True
        elif startPlayer == "o":
            xTurn = False
        # actual game
        while check == "n":
            # start game
            printPrettyBoard(board)
            # Player X turn
            if xTurn == True:
                move = int(input("Player x, pick a spot: "))
                counter += 1
                if isValidMove(board, move) == False:
                    print("Invalid move, please try again.")
                    move = int(input("Player x, pick a spot: "))
                updateBoard(board, move, "x")
                xTurn = False
                check = TicTacToeHelper.checkForWinner(board, counter)
            else:
                move = int(input("Player o, pick a spot: "))
                counter += 1
                if isValidMove(board, move) == False:
                    print("Invalid move, please try again.")
                    move = int(input("Player o, pick a spot: "))
                updateBoard(board, move, "o")
                xTurn = True
                check = TicTacToeHelper.checkForWinner(board, counter)
        if check == "s":
            print("Game Over!\nStalemate reached!")
        if check == "x":
            print("Game Over!\nPlayer x is the winner!")
        elif check == "o":
            print("Game Over!\nPlayer o is the winner!")


# keep going until player wishes to stop
def main():
    keepGoing = True
    while keepGoing == True:
        playGame()
        playAgain = input("Would you like to play again? (y/n)").lower()
        if playAgain == "n":
            keepGoing = False
    else:
        print("Thanks for playing!")


main()
