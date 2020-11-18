# June Kim
# ITP115, Fall 2019
# Assignment 5-1
# junek@usc.edu
# This program creates a jumbled word game that counts attempts.


def main():
    # random words and their matching hints
    import random
    listwords = (("trojan", "USC students known as? (singular)"), ("viterbi", "USC School of Engineering"),
                 ("annenberg", "USC School of Communication"), ("spirit of troy", "USC marching band"),
                 ("traveler", "Our Mascot name"))
    word, hint = random.choice(listwords)
    wordlist = list(word)

    # jumbling the randomly chosen word
    for i in range(0, int(len(word))):
        jumbling = random.randrange(len(word))
        temp = wordlist[i]
        wordlist[i] = wordlist[jumbling]
        wordlist[jumbling] = temp
        print("".join(wordlist))
    print("The jumbled word is: " + "".join(wordlist) + "\nEnter your guess:")

    answer = False
    tries = 1
    while answer == False:
        guess = input(">").lower()
        if guess == word:
            print("Your guess is correct! You took " + str(tries) + " attempts.")
            answer = True
        if guess != word and tries < 6:
            print("Incorrect! Try again")
            tries = tries + 1
        if guess != word and tries > 5:
            print("Incorrect! Try again\n" + hint)
            tries = tries + 1
    if tries <= 5:
        print("You guessed without the hint! 100 points")
    if 5 < tries < 16:
        print("You guessed but you needed the hint. 50 points")
    if tries > 15:
        print("While you got the answer, you needed the hint and took over 15 tries. 5 points :(")


main()
