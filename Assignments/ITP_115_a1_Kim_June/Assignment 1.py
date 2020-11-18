# June Kim
# ITP 115, Fall 2019
# Assignment 1
# junek@usc.edu


def main():
    # madlib input start
    major = input("Enter a noun: ")
    adverb1 = input("Enter an adverb: ")
    subj = input("Enter a class subject abbreviation (i.e. ITP): ")
    classnumb = int(input("Enter a 3 digit integer number: "))
    country = input("Enter a country: ")
    timeperiod = int(input("Enter a multiple of 100: "))
    lastname = input("Enter a last name: ")
    price = float(input("Enter a number with exactly 2 decimal points: "))
    rating = int(input("Enter an integer: "))
    totalrating = int(input("Enter another integer larger than previous: "))
    # madlib story start
    print("\n\nToday, I started my major in \""
          + major
          + "\"ology at USC.\nAs I \""
          + adverb1
          + "\" jogged to my first class (\""
          + subj + "\"\""
          + str(classnumb)
          + "\": \""
          + major
          + "\" in \""
          + country
          + "\" of the \""
          + str(timeperiod)
          + "\"s), \nI couldn't help but remember the ridiculous price of the require textbook for our class."
          + "\nProfessor \""
          + lastname
          + "\" insisted that we buy it, despite it costing $\""
          + str(price)
          + "\". \nI would rate this whole experience a \""
          + str(rating)
          + "\" out of \""
          + str(totalrating)
          + "\".")


main()
