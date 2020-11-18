# June Kim
# ITP115, Fall 2019
# Final Project Part 3
# junek@usc.edu
# This program will define the Waiter class for the final program.


# imports
from Menu import Menu
from Diner import Diner

class Waiter:
    # each waiter must have list of diners and menu
    def __init__(self, menu):
        self.diners = []
        self.menu = menu

    def addDiner(self, newDiner):
        self.diners.append(newDiner)

    def getNumDiners(self):
        return len(self.diners)

    # loop through statuses of diners to group and print all diners of a waiter by status
    def printDinerStatuses(self):
        for x in range(0,5):
            hold = []
            # adds diner into container list based on status, in order of statuses
            for diner in self.diners:
                if diner.getStatus() == Diner.STATUSES[x]:
                    hold.append(diner)
            print("Diners who are " + Diner.STATUSES[x] + ":")
            for x in hold:
                print(x)

    # check for diners who are ordering and retrieve one menu item of each type
    def takeOrders(self):
        for diner in self.diners:
            if diner.getStatus() == Diner.STATUSES[1]:
                for x in range(0, len(Menu.MENU_ITEM_TYPES)):
                    currentType = self.menu.MENU_ITEM_TYPES[x]
                    self.menu.printMenuItemsByType(currentType)
                    # create loop that assumes invalid response until valid response breaks loop (error check)
                    valid = False
                    while valid == False:
                        try:
                            order = int(input(diner.getName() + ", please select a " +
                                               currentType + " menu item number. "))
                            if order >= 1 and order <= self.menu.getNumMenuItemsByType(currentType):
                                diner.addToOrder(self.menu.getMenuItem(currentType, order-1))
                                valid = True
                            else:
                                print("Invalid option, please choose again.")
                        except ValueError:
                            print(">")
                diner.printOrder()

    # check for paying diners and calculate and print final cost
    def ringUpDiners(self):
        for x in self.diners:
            if x.getStatus() == "paying":
                cost = x.calculateMealCost()
                print(x.getName() + ", your meal cost $" + str(cost))

    # check for leaving diners and thank and remove them
    def removeDoneDiners(self):
        for x in self.diners:
            if x.getStatus() == "leaving":
                print(x.getName() + ", thank you for dining with us! Come again soon!")
        for y in range(self.getNumDiners()-1, -1, -1):
            # reverse loop to check for leaving diners and remove from list
            if self.diners[y].getStatus() == Diner.STATUSES[4]:
                del self.diners[y]

    # advances status of each diner and update statuses
    def advanceDiners(self):
        self.printDinerStatuses()
        self.takeOrders()
        self.ringUpDiners()
        self.removeDoneDiners()
        for diner in self.diners:
            diner.updateStatus()
