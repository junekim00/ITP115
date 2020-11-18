# June Kim
# ITP 115, Fall 2019
# Assignment 2-1
# junek@usc.edu
# description:
# This program simulates a Harry Potter-verse vending machine order form.


def main():
    # initial menu options

    print("Please select an item from the vending machine:" +
          "\n\tA) Butterbeer: 58 knuts" +
          "\n\tB) Quill: 10 knuts" +
          "\n\tC) The Daily Prophet: 7 knuts" +
          "\n\tD) Book of Spells: 400 knuts")
    # while loop of item variable name
    item = input("> ").upper()
    while item != "A" and item != "B" and item != "C" and item != "D":
        print("Invalid option")
        item = input("> ").upper()
    if item == "A":
        itemname = "Butterbeer"
        price = int(58)
    elif item == "B":
        itemname = "Quill"
        price = int(10)
    elif item == "C":
        itemname = "The Daily Prophet"
        price = int(7)
    elif item == "D":
        itemname = "Quill"
        price = int(400)

    # calculate discount
    discount = input("Will you share this on Instagram for a discount? (Y/N)").upper()
    while discount != "Y" and discount != "N":
        print("Invalid Option")
        discount = input("Will you share this on Instagram for a discount? (Y/N)").upper()
    if discount == "Y":
        print("Thanks! You get 5 knuts off your purchase.")
        discountprice = int(5)
    elif discount == "N":
        print("Moving on without the discount:")
        discountprice = int(0)

    # calculate change after payment input
    print("Please input how many of each you will be paying with:\n")
    galleons = int(input("Galleons: "))
    sickles = int(input("Sickles: "))
    knuts = int(input("Knuts: "))
    totalpay = galleons*493+sickles*29+knuts
    change = totalpay-price+discountprice
    gchange = change//493
    schange = (change-gchange*493)//29
    kchange = (change-gchange*493) % 29

    # final statement
    print("You bought a " + itemname + " for " + str(price) + " knuts", end="")
    if discount == "Y":
        print(" (with a coupon of 5 knuts) and you paid with ", end="")
    else:
        print(" (with no coupon) and you paid with ", end="")
    print(str(galleons) + " galleons, "
          + str(sickles) + " sickles, and "
          + str(knuts) + " knuts.\n")
    print("Here is your change (" + str(change)
          + "):\nGalleons: " + str(gchange)
          + "\nSickles: " + str(schange)
          + "\nKnuts: " + str(kchange))


main()
