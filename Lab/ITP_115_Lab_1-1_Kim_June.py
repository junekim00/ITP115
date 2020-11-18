# June Kim
# ITP 115, Fall 2019
# Lab 1
# junek@usc.edu


def main():
    # box
    print(" ___ \n|   |\n|   |\n|___|")

    # quote
    print("\nYou don't frighten us, English pig-dogs! "
          "\nGo and boil your bottoms, sons of a silly person!"
          "\n\t\t-\"Monty Python and the Holy Grail\"", end="\n\n")

    # date
    month = input("What month is it?")
    day = input("What day of the week is it?")
    date = int(input("What day of the month is it? (number only)"))
    print("Today is", day, month, str(date) + ". Tomorrow will be", month, str(date+1) + ".")


main()
