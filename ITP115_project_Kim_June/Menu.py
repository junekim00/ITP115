# June Kim
# ITP115, Fall 2019
# Final Project Part 1 cont.
# junek@usc.edu
# This program will define the Menu class for the final program.


# retrieve information about items

from MenuItem import MenuItem

class Menu:
    # set class variable
    MENU_ITEM_TYPES = ["Drink", "Appetizer", "Entree", "Dessert"]
    # Extra Credit: utilizing one MenuItemDictionary instead of 4 lists
    # reading menu file and deciphering which are from which type and separate into dictionary
    def __init__(self, fileName):
        fileIn = open(fileName, "r")
        self.menuDictionary = {}
        menuInput = fileIn.readlines()
        for x in menuInput:
            # split columns from csv
            copy = x.split(",")
            # re-format into readable form
            copyItem = MenuItem(copy[0], copy[1], copy[2], copy[3])
            # error check to make sure type exists using keys function
            if copy[1] in self.menuDictionary.keys():
                # if type already in dictionary, add to list
                self.menuDictionary[copy[1]].append(copyItem)
            else:
                # if type not in dictionary, add type and item to list
                self.menuDictionary[copy[1]] = [copyItem]

    # get item from list given index and type
    def getMenuItem(self, menuType, ind):
        return self.menuDictionary[menuType][ind]

    # print all items of a type
    def printMenuItemsByType(self, menuType):
        a = " * " + menuType + " options *\n"
        counter = 1
        for x in self.menuDictionary.get(menuType):
            a += str(counter) + ") " + str(x)
            counter += 1
        print(a)

    # get number of items by type
    def getNumMenuItemsByType(self, menuType):
        return len(self.menuDictionary.get(menuType))