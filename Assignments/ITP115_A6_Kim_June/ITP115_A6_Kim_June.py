# June Kim
# ITP115, Fall 2019
# Assignment 6
# junek@usc.edu
# This program allows for airplane seat reservation, displays seat arrangement, and prints boarding passes.


def main():
    # setting initial empty seats
    seating = ["", "", "", "", "", "", "", "", "", ""]
    totalSeats = 10
    filled = 0
    firstClassSeats = 4
    filledFirstClass = 0
    economySeats = 6
    filledEconomy = 0
    menuChoice = 0
    keepGoing = True

    while keepGoing == True:
        # menu
        print("1:   Assign Seat.\n2:   Print Seat Map.\n3:   Print Boarding pass.\n-1:  Quit.")
        menuChoice = input(">")
        if menuChoice != "1" and menuChoice != "2" and menuChoice != "3" and menuChoice != "-1":
            print("Invalid choice.")
            menuChoice = input(">")

        # assign seat
        if menuChoice == "1":
            if filled != totalSeats:
                print("Input full name:")
                name = input(">").title()

                # extra credit economy vs first class
                print("Type 1 for First Class or Type 2 for Economy.")
                seatType = input(">")
                keepSeatGoing = True
                if seatType != "1" and seatType != "2":
                    print("Invalid choice.")

                while keepSeatGoing == True:

                    # first class
                    if seatType == "1":
                        if firstClassSeats == filledFirstClass:
                            print("First class is full. Would you like to book economy? (Y/N)")
                            bookOther = input(">").lower()
                            if bookOther != "y" and bookOther != "n":
                                "Invalid choice."
                                keepSeatGoing = False
                            if bookOther == "y":
                                seatType = "2"
                            if bookOther == "n":
                                print("Next flight leaves in 3 hours.")
                                keepSeatGoing = False
                        if firstClassSeats != filledFirstClass:
                            print("Please choose a seat (1-4):")
                            seatChoice = int(input(">"))
                            seatChoiceIndex = seatChoice - 1
                            if seating[seatChoiceIndex] != "":
                                print("This seat is already taken. Please choose again.")
                                keepSeatGoing = False
                            else:
                                del seating[seatChoiceIndex]
                                seating.insert(seatChoiceIndex, name)
                                filled = filled + 1
                                filledFirstClass = filledFirstClass + 1
                                keepSeatGoing = False

                    # economy
                    if seatType == "2":
                        if economySeats == filledEconomy:
                            print("Economy is full. Would you like to book first class? (Y/N)")
                            bookOther = input(">").lower()
                            if bookOther != "y" and bookOther != "n":
                                "Invalid choice."
                                keepSeatGoing = False
                            if bookOther == "y":
                                seatType = "1"
                            if bookOther == "n":
                                print("Next flight leaves in 3 hours.")
                                keepSeatGoing = False
                        if economySeats != filledEconomy:
                            print("Please choose a seat (5-10):")
                            seatChoice = int(input(">"))
                            seatChoiceIndex = seatChoice - 1
                            if seating[seatChoiceIndex] != "":
                                print("This seat is already taken. Please choose again.")
                                keepSeatGoing = False
                            else:
                                del seating[seatChoiceIndex]
                                seating.insert(seatChoiceIndex, name)
                                filled = filled + 1
                                filledEconomy = filledEconomy + 1
                                keepSeatGoing = False

            if filled == totalSeats:
                print("Next flight leaves in 3 hours.")

        # print seat map
        if menuChoice == "2":
            for i in range(len(seating)):
                # first class
                if i < 4:
                    if seating[i] != "":
                        print("First Class Seat #" + str(i+1) + ": " + seating[i])
                    if seating[i] == "":
                        print("First Class Seat #" + str(i+1) + ": Empty")
                # economy
                if i >= 4:
                    if seating[i] != "":
                        print("Economy Seat #" + str(i+1) + ": " + seating[i])
                    if seating[i] == "":
                        print("Economy Seat #" + str(i+1) + ": Empty")

        # print boarding pass
        if menuChoice == "3":
            print("Type 1 to search boarding pass by seat number.\n" +
                  "Type 2 to search boarding pass by name.")
            search = input(">")
            if search != "1" and search != "2":
                print("Invalid choice")
            # search by seat number
            if search == "1":
                print("What is your seat number?")
                numbSearch = input(">")
                if numbSearch.isdigit() == False or int(numbSearch) > 10:
                    print("Invalid choice.")
                else:
                    seatChoiceIndex = int(numbSearch) - 1
                    print("======= BOARDING PASS =======\n" +
                          "Seat #: " + numbSearch +
                          "\nPassenger Name: " + seating[seatChoiceIndex] +
                          "\n=============================")
            # search by name
            if search == "2":
                print("What is your name?")
                searchName = input(">").title()
                fakeSeatNumb = 11
                for j in range(len(seating)):
                    if seating[j] == searchName:
                        fakeSeatNumb = j + 1
                if fakeSeatNumb > 10:
                    print("Name not found.")
                else:
                    print("======= BOARDING PASS =======\n" +
                          "Seat #: " + str(fakeSeatNumb) +
                          "\nPassenger Name: " + searchName +
                          "\n=============================")
        # quit
        if menuChoice == "-1":
            keepGoing = False
    else:
        print("Have a nice day!")


main()
