# June Kim
# ITP115, Fall 2019
# Final Project Part 1
# junek@usc.edu
# This program will define the MenuItem class for the final program.


class MenuItem:
    # set proper classes for different aspects of class
    def __init__(self, name, itemType, price, description):
        self.name = name
        self.itemType = itemType
        self.price = float(price)
        self.description = description

    # MenuItem getters
    def getName(self):
        return self.name
    def getType(self):
        return self.itemType
    def getPrice(self):
        return self.price
    def getDescription(self):
        return self.description

    # MenuItem setters
    def setName(self, newName):
        self.name = newName
    def setType(self, newType):
        self.itemType = newType
    def setPrice(self, newPrice):
        self.price = newPrice
    def setDescription(self, newDescription):
        self.description = newDescription

    # set a str to return all 4 aspects of menu item in a readable format
    def __str__(self):
        a = self.getName() + " (" + self.getType() + "): $" + str(self.getPrice()) + "\n\t" + self.getDescription()
        return a
