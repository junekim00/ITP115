# June Kim
# ITP115, Fall 2019
# Final Project Part 2
# junek@usc.edu
# This program will define the Diner class for the final program.


class Diner:
    # set variables for diner status
    STATUSES = ["seated", "ordering", "eating", "paying", "leaving"]
    def __init__(self, name):
        self.name = name
        self.order = []
        self.status = 0

    # Diner getters including actual status and integer index of status
    def getName(self):
        return self.name
    def getOrder(self):
        return self.order
    def getStatus(self):
        return self.STATUSES[self.status]
    def getStatusInt(self):
        return self.status

    # Diner setters
    def setName(self, newName):
        self.name = newName
    def setOrder(self, newOrder):
        self.order = [newOrder]
    def setStatus(self, newStatus):
        self.status = int(newStatus)

    # update status by one step
    def updateStatus(self):
        self.status += 1

    # add a new order to pre-existing
    def addToOrder(self, newItem):
        self.order.append(newItem)

    def printOrder(self):
        print(self.getName() + " ordered:")
        for x in self.getOrder():
            print(x)

    def calculateMealCost(self):
        cost = 0
        for x in self.getOrder():
            cost += float(x.getPrice())
        return cost

    # return readable message about diner and status
    def __str__(self):
        a = "Diner " + self.getName() + " is currently " + self.getStatus()
        return a