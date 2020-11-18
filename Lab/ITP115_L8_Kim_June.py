# June Kim
# ITP115, Fall 2019
# Lab 9-1
# junek@usc.edu
import random
global face
global totalCounter
global tossNumbers
tossNumbers = []


# coin toss function
def coin():
    toss = random.randint(0, 1)
    if toss == 0:
        face = "heads"
    if toss == 1:
        face = "tails"


coin()


# 3 heads in a row function
def experiment():
    headsCounter = 0
    totalCounter = 0

    while headsCounter < 3:
        coin()
        if face == "heads":
            headsCounter += 1
            totalCounter += 1
        if face == "tails":
            headsCounter = 0
            totalCounter += 1

experiment()


def main():

    for i in range(0, 10):
        experiment()
        tossNumbers.append(totalCounter)
        average = sum(tossNumbers)/len(tossNumbers)
    print("The average number of tosses for 3 heads in a row is: " + str(average))


main()
