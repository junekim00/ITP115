# June Kim
# ITP 115, Fall 2019
# Lab 4
# junek@usc.edu


def main():

    print("\nElcómewó óten heten Igpén Lvísheá ránslátórtë!" +
          "\n(Welcome to the Pig Elvish translator!)")

    keepgoing = True

    while keepgoing == True:
        word = input("\nPlease enter a word you would like to translate: ").lower()

        # rearrange word
        for letter in word:
            newword = word.replace("k", "c").replace("e", "ë")
            pigword = newword[1:] + newword[0]
        import random
        vowel = random.choice("aeiou")

        # pig word 3 letters or less
        if len(pigword) < 4:
            print("\n" + word + " in Pig Elvish is: " + pigword + "ën")

        # pig word 4 letters of more
        if len(pigword) > 3:
            print("\n" + word + " in Pig Elvish is: " + pigword + vowel)

        # repeat process
        repeat = input("\nWould you like to continue? (y/n): ").upper()
        while repeat != "Y" and repeat != "N":
            print("Invalid choice")
            repeat = input("\nWould you like to continue? (y/n): ").upper()
            print("User said: " + repeat)
        if repeat == "N":
            print("\nOodbyega! Aveha aen icenë ayden! (Goodbye! Have a nice day!)")
            keepgoing = False


main()
