# June Kim
# ITP 115, Fall 2019
# Lab 2
# junek@usc.edu


def main():
    cupsize = input("What size coffee do you want (S, M, L)? ").upper()
    temp = int(input("What temperature (degrees) do you want your drink to be? "))
    beans = input("What type of beans would you like? ")
    cream = input("Would you like to leave room for cream? (Y/N) ").upper()
    name = input("Can we have a name for that order? ")

    # size
    if cupsize == "S":
        print("\nI have a small", end="")
    elif cupsize == "M":
        print("\nI have a medium", end="")
    elif cupsize == "L":
        print("\nI have a large", end="")
    else:
        print("Sorry, that is not a valid order.")

    # temperature
    if temp < 70:
        print(", cold, " + beans, end="")
    else:
        print(", hot, " + beans, end="")

    # cream
    if cream == "Y":
        print(" with cream for", name + ".")
    else:
        print(" without cream for", name + ".")


main()
