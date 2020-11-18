# June Kim
# ITP115, Fall 2019
# Assignment 4-2
# junek@usc.edu
# This program simulates 5 different win conditions for 5 different D20 dice games.


def main():

    # initial score
    score = 0

    # choose case 10 times
    for match in range(10):
        # random case choice
        import random
        case = random.randrange(1, 6)
        # case 1
        if case == 1:
            dice = random.randrange(1, 21)
            print("You're playing for case 1. You win if you roll:\n1 2 3 4 5\n\nYou rolled: " + str(dice))
            if dice in range(1, 6):
                print("You win!\n")
                score += 50
            else:
                print("You didn't win.\n")

        # case 2
        if case == 2:
            dice = random.randrange(1, 21)
            print("You're playing for case 2. You win if you roll:\n1 3 5 ... 17 19\n\nYou rolled: " + str(dice))
            if dice in range(1, 20, 2):
                print("You win!\n")
                score += 50
            else:
                print("You didn't win.\n")

        # case 3
        if case == 3:
            dice = random.randrange(1, 21)
            print("You're playing for case 3. You win if you roll:\n5 6 7 8 9 10\n\nYou rolled: " + str(dice))
            if dice in range(5, 11):
                print("You win!\n")
                score += 50
            else:
                print("You didn't win.\n")

        # case 4
        if case == 4:
            dice = random.randrange(1, 21)
            print("You're playing for case 4. You win if you roll:\n10 12 14 16 18 20\n\nYou rolled: " + str(dice))
            if dice in range(10, 21, 2):
                print("You win!\n")
                score += 50
            else:
                print("You didn't win.\n")

        # case 5
        if case == 5:
            dice = random.randrange(1, 21)
            print("You're playing for case 5. You win if you roll:\n3 6 9 ... 15 18\n\nYou rolled: " + str(dice))
            if dice in range(3, 21, 3):
                print("You win!\n")
                score += 50
            else:
                print("You didn't win.\n")

    print("After 10 rounds, your final score is " + str(score) + ".")


main()
