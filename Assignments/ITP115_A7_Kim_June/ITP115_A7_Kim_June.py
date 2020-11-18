# June Kim
# ITP115, Fall 2019
# Assignment 7
# junek@usc.edu
# This program allows for rock, paper, scissors games with a computer.
import random


# game rules
def displayMenu():
    print("Welcome! Let's play rock, paper, scissors.\n" +
          "The rules of the game are:\n\t" +
          "Rock smashes scissors\n\t" +
          "Scissors cut paper\n\t" +
          "Paper covers rock\n\t" +
          "If both the choices are the same, it's a tie.")


# computer choice
def getComputerChoice():
    computerChoice = random.randint(0, 2)
    return computerChoice


# player choice
def getPlayerChoice():
    playerChoice = int(input("Please choose (0) for rock, (1) for paper or (2) for scissors.\n"))
    while playerChoice != 0 and playerChoice != 1 and playerChoice != 2:
        print("Please only enter 0, 1, or 2.")
        playerChoice = input("Please choose (0) for rock, (1) for paper or (2) for scissors.\n")
    return playerChoice


# play round
def playRound(computerChoice, playerChoice):
    # labeling different choices
    if playerChoice == 0:
        player = "rock"
    if playerChoice == 1:
        player = "paper"
    if playerChoice == 2:
        player = "scissors"
    if computerChoice == 0:
        computer = "rock"
    if computerChoice == 1:
        computer = "paper"
    if computerChoice == 2:
        computer = "scissors"
    # print choices
    print("You chose " + player + ".\nComputer chose " + computer + ".")
    # outcomes
    if playerChoice == computerChoice:
        print("You chose the same. It's a tie!")
        return 0
    elif playerChoice == 0 and computerChoice == 1:
        print("Paper covers rock. You lose :(")
        return -1
    elif playerChoice == 1 and computerChoice == 2:
        print("Scissors cuts paper. You lose :(")
        return -1
    elif playerChoice == 2 and computerChoice == 0:
        print("Rock smashes scissors. You lose :(")
        return -1
    elif playerChoice == 0 and computerChoice == 2:
        print("Rock smashes scissors. You win!")
        return 1
    elif playerChoice == 1 and computerChoice == 0:
        print("Paper covers rock. You win!")
        return 1
    elif playerChoice == 2 and computerChoice == 1:
        print("Scissors cuts paper. You win!")
        return 1


# continue game
def continueGame():
    keepPlaying = input("Would you like to continue? (Y/N)").lower()
    while keepPlaying != "y" and keepPlaying != "n":
        print("Invalid choice.")
        keepPlaying = input("Would you like to continue? (Y/N").lower()
    if keepPlaying == "y":
        return True
    elif keepPlaying == "n":
        return False


# actual program
def main():
    # start score
    wins = 0
    loss = 0
    tie = 0
    play = True

    while play == True:
        displayMenu()
        computerChoice = getComputerChoice()
        playerChoice = getPlayerChoice()
        round = playRound(computerChoice, playerChoice)
        # keeping score
        if round == 0:
            tie += 1
        if round == 1:
            wins += 1
        if round == -1:
            loss += 1
        play = continueGame()
    else:
        # print final results
        print("You won " + str(wins) + " game(s).\n" +
              "You lost " + str(loss) + " game(s).\n" +
              "You tied " + str(tie) + " game(s).\n" +
              "Thanks for playing!")


main()
