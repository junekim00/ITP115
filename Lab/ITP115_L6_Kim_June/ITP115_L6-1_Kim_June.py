# June Kim
# ITP 115, Fall 2019
# Lab 6-1
# junek@usc.edu


def main():

    # input of words
    print("Enter a word: ")
    firstword = input(">").lower()
    print("Enter a second word: ")
    secondword = input(">").lower()

    # remove spaces
    fword = firstword.replace(" ", "")
    sword = secondword.replace(" ", "")

    # turn into list
    fwlist = list(fword)
    swlist = list(sword)

    # joined alphabetically sorted
    orderfirst = "".join(sorted(fwlist))
    ordersecond = "".join(sorted(swlist))

    # anagram
    if orderfirst == ordersecond:
        print("The two words entered are anagrams.")
    else:
        print("The two words entered are not anagrams.")

    # palindromes
    """replace the letter in first half of word with corresponding letter from
    end of the word until it reaches the middle"""
    for i in range(0, int(len(fword))):
        fwlist[i] = fwlist[int(len(fword)-i-1)]
        i = i+1
    if "".join(fwlist) == fword:
        print("The first word is a palindrome.")
    else:
        print("The first word is not a palindrome.")

    for j in range(0, int(len(sword))):
        swlist[j] = swlist[int(len(sword) - j - 1)]
        j = j + 1
    if "".join(swlist) == sword:
        print("The first word is a palindrome.")
    else:
        print("The first word is not a palindrome.")


main()
