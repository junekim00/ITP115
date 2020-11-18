# June Kim
# ITP115, Fall 2019
# Assignment 5-2
# junek@usc.edu
# This program encrypts and decrypts a phrase with a Caesar cipher.


def main():
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # input
    phrase = input("Enter phrase you want encrypted: ")
    lcphrase = phrase.lower()
    shiftnumb = int(input("Enter a number to shift by (0-25): "))

    # create cipher alphabet
    cypher = alphabet[shiftnumb:] + alphabet[0:shiftnumb]

    # encrypt phrase
    newphrase = []
    for i in range(0, len(phrase)):
        if lcphrase[i].isalpha() == True:
            number = alphabet.index(lcphrase[i])
            newletter = cypher[number]
            newphrase.append(newletter)
        if lcphrase[i].isalpha() == False:
            newphrase.append(lcphrase[i])
    print("\nEncrypting...\nThe encrypted word is: " + "".join(newphrase))

    # decrypt phrase
    decphrase = []
    for i in range(0, len(phrase)):
        if newphrase[i].isalpha() == True:
            dnumber = cypher.index(newphrase[i])
            dletter = alphabet[dnumber]
            decphrase.append(dletter)
        if newphrase[i].isalpha() == False:
            decphrase.append(newphrase[i])
    print("\nDecrypting...\nThe decrypted word is: " + "".join(decphrase))


main()
