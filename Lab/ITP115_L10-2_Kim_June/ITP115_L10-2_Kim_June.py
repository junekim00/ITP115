# June Kim
# ITP115, Fall 2019
# Lab 10-2
# junek@usc.edu


# read the words from the txt file
def readfile(fileName):
    fileName = open(fileName, "r")
    dictionary = []
    for i in fileName:
        i = i.strip()
        dictionary.append(i)
    fileName.close()
    return dictionary


# searching if word already in dictionary
def findWord(wordsList, searchWord):
    if searchWord in wordsList:
        search = True
    else:
        search = False
    return search


# add new word in txt file
def writeFile(outputList, fileName):
    fileName = open(fileName, "w")
    for i in outputList:
        print(i, file=fileName)
    fileName.close()


# final program
def main():
    # naming variables
    fileName = input("Enter the name of the file you wish to read in: ")
    outputFile = input("Enter the name of the file you wish to write in: ")
    searchWord = input("Enter the word you wish to check: ")

    # creating initial list of words in txt
    wordsList = readfile(fileName)

    # search if new word is already in txt, add if not
    findWord(wordsList, searchWord)
    if findWord(wordsList, searchWord) == True:
        print(searchWord + " is already in the dictionary.")
    else:
        wordsList.append(searchWord)
        print(searchWord + " has been added to the dictionary.")

    # export new wordsList
    writeFile(wordsList, outputFile)
    print("The word list has been written to output.txt.")


main()
