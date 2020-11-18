# June Kim
# ITP 115, Fall 2019
# Lab 3
# junek@usc.edu


def main():
    row = 1
    while row <= 10:
        if row == 1:
            print(" "*19 + "^")
        else:
            print(" "*(20-2*row) + " ^"*(2*row-1))
        row += 1


main()
