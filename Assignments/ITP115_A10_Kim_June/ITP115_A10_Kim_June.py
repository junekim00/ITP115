# June Kim
# ITP115, Fall 2019
# Assignment 10
# junek@usc.edu
# This program will read csv file and and adjust attributes based on user input.


class Animal:

    # setting animal attributes
    def __init__(self, hunger, happiness, health, energy, age, name, species):
        self.hunger = int(hunger)
        self.happiness = int(happiness)
        self.health = int(health)
        self.energy = int(energy)
        self.age = int(age)
        self.name = name
        self.species = species

    # play increases happiness by 10 and hunger by 5 with max 100
    def play(self):
        if self.happiness < 100:
            self.happiness += 10
        if self.happiness > 100:
            self.happiness = 100
        if self.hunger < 100:
            self.hunger += 5
        if self.hunger > 100:
            self.hunger = 100

    # feed decreases hunger by 10 with min 0
    def feed(self):
        if self.hunger > 0:
            self.hunger -= 10
        if self.hunger < 0:
            self.hunger = 0

    # give medicine decreases happiness by 20 with min 0 and increases health by 20 with max 100
    def giveMedicine(self):
        if self.happiness > 0:
            self.happiness -= 20
        if self.happiness < 0:
            self.happiness = 0
        if self.health < 100:
            self.health += 20
        if self.health > 100:
            self.health = 100

    # sleep increases energy by 20 with max 100 and age by 1
    def sleep(self):
        if self.energy < 100:
            self.energy += 20
        if self.energy > 100:
            self.energy = 100
        self.age += 1

    # returns current animal attributes
    def __str__(self):
        return ("Name: " + str(self.name) + " the " + str(self.species) +
                "\nHealth: " + str(self.health) + "\nHappiness: " +
                str(self.happiness) + "\nHunger: " + str(self.hunger) +
                "\nEnergy: " + str(self.energy) + "\nAge: " + str(self.age) +
                "\n********************************")


def parseLine(line):
    # read one line of csv and return all elements as list
    word = ''
    lineList = []
    new = False
    for letter in line:
        if letter != ",":
            if letter == "\n":
                lineList.append(word)
                new = True
            else:
                word = word + letter
        elif letter == ",":
            lineList.append(word)
            word = ""
    if not new:
        lineList.append(word)
    return lineList


def loadAnimals(inName):
    # read file to find objects for each animal and return in a list
    try:
        with open(inName, "r") as inFile:
            label = False
            labelList = []
            data = []
            objects = []

            # Parse File
            for line in inFile:
                if label:
                    labelList = parseLine(line)
                    label = False
                else:
                    data.append(parseLine(line))

            inFile.close()

            for element in data:
                objects.append(Animal(element[0], element[1], element[2],
                                      element[3], element[4], element[5],
                                      element[6]))
            return objects

    except OSError:
        return False


def displayMenu():
    # print user choice menu
    menu = ["Play", "Feed", "Give Medicine", "Sleep", "Print an Animal's stats", "View All Animals", "Exit"]
    print('')
    # print number before choice
    for i, menuElement in enumerate(menu):
        print(str(i + 1) + ') ' + str(menuElement))
    print('')


def countObject(animalList):
    # determines start and end index
    count = 0
    for animal in animalList:
        count += 1
    if count == 0:
        return 0, 0
    else:
        return 1, count


def selectAnimal(animalList):
    # return index of animal based on user input
    # show animal list and number choices
    start, end = countObject(animalList)
    for i, animal in enumerate(animalList):
        print(str(i + 1) + ") " + str(animal.name) + " the " + str(animal.species))
    print("\nPlease select an animal from the list (enter the " + str(start) + "-" + str(end) + "): ")
    userAnimal = input()

    while userNumInputChecker(userAnimal, start, end):
        print("Invalid input, please try again!")
        print("\nPlease select an animal from the list (enter the " + str(start) + "-" + str(end) + "): ")
        userAnimal = input()

    return int(userAnimal) - 1


def userNumInputChecker(userInput, start=1, end=7):
    # checks if input is number and in range 1-7
    try:
        userInput = int(userInput)
    except ValueError:
        return True
    return False if userInput >= start and userInput <= end else True


def outputNameFormatChecker(output):
    # is .csv the extension of output name
    fileNameExtension = output[-4:]
    if fileNameExtension == ".csv":
        return False
    else:
        return True


def saveFile(output, animalList):
    # Output to csv
    try:
        with open(output, "w+") as outFile:
            for i, animal in enumerate(animalList):
                if i != (len(animalList) - 1):
                    outFile.write(str(animal.hunger))
                    outFile.write(",")
                    outFile.write(str(animal.happiness))
                    outFile.write(",")
                    outFile.write(str(animal.health))
                    outFile.write(",")
                    outFile.write(str(animal.energy))
                    outFile.write(",")
                    outFile.write(str(animal.age))
                    outFile.write(",")
                    outFile.write(str(animal.name))
                    outFile.write(",")
                    outFile.write(str(animal.species))
                    outFile.write("\n")
                else:
                    outFile.write(str(animal.hunger))
                    outFile.write(",")
                    outFile.write(str(animal.happiness))
                    outFile.write(",")
                    outFile.write(str(animal.health))
                    outFile.write(",")
                    outFile.write(str(animal.energy))
                    outFile.write(",")
                    outFile.write(str(animal.age))
                    outFile.write(",")
                    outFile.write(str(animal.name))
                    outFile.write(",")
                    outFile.write(str(animal.species))
            outFile.close()
            return False

    except OSError:
        return True


def main():
    # set default input name
    inFileName = "animals.csv"
    # load animal list file
    animalList = loadAnimals(inFileName)

    # if failed to open input
    while not animalList:
        print("Failed to open: \"" + str(inFileName) + "\"")
        print("Make sure Input File is in the same folder with the python source code!\n")
        print("Enter Input File Name (type 'q' to exit the program): ")
        inFileName = input().strip().lower()
        if inFileName == "q":
            print("Goodbye!")
            quit()
        animalList = loadAnimals(inFileName)

    print("Welcome to the Animal Daycare! Here is what we can do:")
    # set default user input that is not quit
    userInput = "a"

    # while loop until user exit
    while userInput != 7:
        displayMenu()
        print("Please make a selection: ")
        userInput = input()
        # check for NaN and valid input
        while userNumInputChecker(userInput):
            print("*Invalid selection, please try again.")
            displayMenu()
            print("Please make a selection: ")
            userInput = input()

        userInput = int(userInput)

        # different outcomes from user choice
        if userInput == 1:
            animalIndex = selectAnimal(animalList)
            animalList[animalIndex].play()
            print("You played with " + str(animalList[animalIndex].name) + " the " + str(
                animalList[animalIndex].species) + '!')
        elif userInput == 2:
            animalIndex = selectAnimal(animalList)
            animalList[animalIndex].feed()
            print("You fed " + str(animalList[animalIndex].name) + " the " + str(animalList[animalIndex].species) +
                  "!")
        elif userInput == 3:
            animalIndex = selectAnimal(animalList)
            animalList[animalIndex].giveMedicine()
            print("You gave " + str(animalList[animalIndex].name) + ' the ' + str(animalList[animalIndex].species) +
                  " some medicine!")
        elif userInput == 4:
            animalIndex = selectAnimal(animalList)
            animalList[animalIndex].sleep()
            print(str(animalList[animalIndex].name) + " the " + str(animalList[animalIndex].species) + " took a nap!")
        elif userInput == 5:
            print(animalList[selectAnimal(animalList)])
        elif userInput == 6:
            for animal in animalList:
                print(animal)

    # Extra credit: output to csv
    outputExtra = input("\nWould you like to save the current state of Animals to a .csv file? (Y/N) \n").lower()
    while outputExtra != "y" and outputExtra != "n":
        print("*Invalid choice")
        outputExtra = input("\nWould you like to save the current state of Animals to a .csv file? (Y/N) \n").lower()

    if outputExtra == "y":
        print("\nType 'q' to cancel and exit the program")
        outputName = input("Enter name of the file to save results to (.csv): \n")
        # account for capitalization
        if outputName == "q" or outputName == "Q":
            print("Goodbye!")
            quit()
        while outputNameFormatChecker(outputName):
            print("\nInvalid filename format!" +
                  "\nType 'q' to cancel and exit the program")
            outputName = input("Enter name of the file to save results to (.csv): \n")
            if outputName == "q" or outputName == "Q":
                print("Goodbye!")
                quit()

    # if fail to output
    while saveFile(outputName, animalList):
        print("\nFailed to write \"" + str(outputName) + "\"")
        print("Make sure this program has the appropriate OS permission to write file! \n")
        print("Type 'q' to cancel and exit the program")
        outputName = input("Enter name of the file to save results to (.csv): \n")
        if outputName == "q" or outputName == "Q":
            break
        while outputNameFormatChecker(outputName):
            print("\nInvalid filename format!")
            print("Type 'q' to cancel and exit the program")
            outputName = input("Enter name of the file to save results to (.csv): \n")
            if outputName == "q" or outputName == "Q":
                break

    print("Goodbye!")


main()
