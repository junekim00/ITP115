# June Kim
# ITP115, Fall 2019
# Assignment 9
# junek@usc.edu
# This program will read csv file and save to new output file.



def main():
    # choosing input and output files
    print("Welcome to EPA Mileage Calculator")
    year = int(input("What year would you like to view data for? (2008 or 2009): "))
    while year != 2008 and year != 2009:
        year = int(input("*Invalid input, please try again!\n" +
                         "What year would you like to view data for? (2008 or 2009): "))
    output = input("Enter the filename to save results to: ")
    inputFile = "epaVehicleData" + str(year) + ".csv"

    # setting blank variable names
    counter = 0
    min = 1000000
    max = 0
    minModels = []
    maxModels = []

    # reading input file
    readFile = open(inputFile, "r")

    # read file and remove vans and pickups
    for line in readFile:
        # counter is to skip title row
        if counter != 0 and "van" not in line[0] and "pickups" not in line[0]:
            line = line.split(",")
            # checking if greater than or equal to max MPG
            if int(line[8]) > max:
                max = int(line[8])
                # removing prior max models from list
                maxModels = []
                maxModels.append(line[2])
            elif int(line[8]) == max:
                maxModels.append(line[2])
            # doing the same for min
            if int(line[8]) < min:
                min = int(line[8])
                minModels = []
                minModels.append(line[2])
            elif int(line[8]) == min:
                minModels.append(line[2])
        counter += 1

    # writing in output file
    outputFile = open(output, "w+")
    outputFile.write("EPA City MPG Calculator (" + str(year) + ")\n" +
                     "---------------------------------\n" +
                     "Maximum mileage (city): " + str(max) + "\n")
    for car in maxModels:
        outputFile.write("\t" + car + "\n")
    outputFile.write("Minimum mileage (city): " + str(min) + "\n")
    for car in minModels:
        outputFile.write("\t" + car + "\n")
    print("Operation success! Mileage data has been saved to " + output + ".\n" +
          "Thanks, and have a great day!")
    outputFile.close()


main()
