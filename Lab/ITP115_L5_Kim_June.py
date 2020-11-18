# June Kim
# ITP 115, Fall 2019
# Lab 5
# junek@usc.edu


def main():

    # default words
    articles = ["a", "the"]
    nouns = ["person", "place", "thing"]
    verbs = ["danced", "ate", "frolicked"]
    # default enter program
    keepgoing = True

    # menu options printed
    print("\nWelcome to the Sentence Generator\nMenu"
          + "\n1) View Words\n2) Add Words\n3) Remove Words\n4) Generate Sentence\n5) Exit")

    while keepgoing == True:
        # choose from menu
        choice = input(">")
        # input not 1-5
        while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
            print("Invalid input")
            choice = input("Welcome to the Sentence Generator\nMenu"
                           + "\n1) View Words\n2) Add Words\n3) Remove Words\n4) Generate Sentence\n5) Exit")
        # print words
        if choice == "1":
            print("Articles: " + str(articles)
                  + "\nNouns: " + str(nouns)
                  + "\nVerb: " + str(verbs))

        # add words
        if choice == "2":
            typeword = input("To add a noun, press 1. To add a verb, press 2. ")
            while typeword != "1" and typeword != "2":
                print("Invalid input")
                typeword = input("To add a noun, press 1. To add a verb, press 2. ")
            if typeword == "1":
                nouns.append(input("Enter a noun: "))

            if typeword == "2":
                verbs.append(input("Enter a verb: "))

        # remove words
        if choice == "3":
            removetype = input("To remove a noun, press 1. To remove a verb, press 2. ")
            while removetype != "1" and removetype != "2":
                print("Invalid input")
                removetype = input("To remove a noun, press 1. To remove a verb, press 2. ")
            if removetype == "1":
                nouns.remove(input("Enter a noun to remove: "))

            if removetype == "2":
                verbs.remove(input("Enter a verb to remove:"))

        # generate a sentence
        if choice == "4":
            import random
            print(random.choice(articles), random.choice(nouns), random.choice(verbs),
                  random.choice(articles), random.choice(nouns))

        # exit program
        if choice == "5":
            keepgoing = False
    if keepgoing == False:
        print("Have a nice day!")


main()
