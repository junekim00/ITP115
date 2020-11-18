# June Kim
# ITP115, Fall 2019
# Assignment 4-1
# junek@usc.edu
# This program counts the number of each character and outputs that number of asterisks.


def main():
    # input sentence
    initialsentence = input("Character Counter\nInput a sentence: ").lower()

    # remove spaces
    sentence = initialsentence.replace(" ", "")

    # alphabet string
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # counters
    countalpha = 0

    # going through regular alphabet
    for i in alphabet:
        countchar = 0
        if i != " ":
            for j in sentence:
                if i == j:
                    countchar = countchar + 1
        countalpha = countchar + countalpha
        output = i + ": "
        if countchar == 0:
            output = output + "NONE"
        else:
            for j in range(countchar):
                output = output + "*"
        print(output)

    # going through special characters by using counter and comparing with length of sentence
    special = "Special Character" + ": "
    if len(sentence) != countalpha:
        for i in range(len(sentence) - countalpha):
            special = special + "*"
    else:
        special = special + "NONE"
    print(special)


main()
