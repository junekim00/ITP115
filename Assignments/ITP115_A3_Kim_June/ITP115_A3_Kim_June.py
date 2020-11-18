# June Kim
# ITP 115, Fall 2019
# Assignment 3
# junek@usc.edu
# This program analyzes a set of numbers and outputs largest, smallest, and average numbers.


def main():
    # starting values
    numb = 0
    # set low to high number to guarantee low will be replaced
    low = 999999999999999999999999
    high = 0
    sums = 0
    average = 0
    counter = 0
    # allows first entry into program
    repeat = "Y"

    # outer loop is based on repeat answer
    while repeat != "Y" and repeat != "N":
        print("Invalid input")
    if repeat == "Y":
        # number input
        while numb >= 0:
            numb = int(input("Enter a number greater than or equal to zero or -1 to quit:\n"))
            if numb >= 0:
                # average
                counter = counter + 1
                sums = sums + numb
                average = sums / counter
            # maximum number
            if numb > high:
                high = numb
            # minimum number
            if numb < low and numb != -1:
                low = numb
        # quit after entering -1
            if numb == -1:
                print("Maximum is " + str(high)
                      + "\nMinimum is " + str(low)
                      + "\nAverage is " + str(average))
                repeat = input("Would you like to input another set of numbers? (Y/N): ").upper()
                # repeat and reset values
                if repeat == "Y":
                    numb = 0
                    low = 999999999999999999999999
                    high = 0
                    sums = 0
                    counter = 0
    # quit whole program
    if repeat == "N":
        print("\nGoodbye!")


main()
