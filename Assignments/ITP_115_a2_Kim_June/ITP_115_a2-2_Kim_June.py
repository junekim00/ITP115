# June Kim
# ITP 115, Fall 2019
# Assignment 2-2
# junek@usc.edu
# description:
# This program simulates a Choose Your Own Adventure set in college.


# first choice
def main():
    print("It is your first year of college. What do you do?" +
          "\na: Make a timetable for you classes, focus on studies, and prepare for internship opportunities." +
          "\nb: Focus on joining clubs and making new friends." +
          "\nc: College is freedom. Go out and party!")
    choice1 = input("> ").lower()

# while loop for choice 1
    while choice1 != "a" and choice1 != "b" and choice1 != "c":
        print("Invalid choice. Try again.")
        choice1 = input("> ").lower()

# second choice if chose A
    if choice1 == "a":
        print("You get good grades, but you struggle with your social life. " +
              "It's your next year, what do you do now?" +
              "\na: Continue to throw yourself in your studies. Don't let social life distract you." +
              "\nb: Become a little more lax with academics but join more organizations." +
              "\nc: Focus all your efforts on improving your social life.")
        choicea = input("> ").lower()

# end results if chose A

        while choicea != "a" and choicea != "b" and choicea != "c":
            print("Invalid choice. Try again.")
            choicea = input("> ").lower()

        if choicea == "a":
            print("Your grades are fantastic, and you have plenty of acquaintances from classes who ask you for help." +
                  "\nHowever, you don't have friends you consider close and your mental health is deteriorating. " +
                  "Focus on balance for next year!")

        elif choicea == "b":
            print("While your grades aren't as flawless as last year, you are still doing very well. " +
                  "\nYou have close friends and not so close friends, but either way you are having fun. " +
                  "\nKeep up the good balance between social and academics next year too!")

        elif choicea == "c":
            print("Your grades are suffering massively, and while you are having fun, you're still a little " +
                  "disoriented from the rapid change.\nYou go to far at parties, and you have had to get help from " +
                  "strangers getting home. \nYou're parents are worried. Try to bring it back a little and find a " +
                  "good balance.")

# second choice if chose A

    elif choice1 == "b":
        print("You joined too many clubs at first, but now are managing just the right amount. " +
              "\nYour grades were satisfactory but not the best they could've been, and you haven't been to any " +
              "\"parties\" that everyone keeps talking about.\nNext year is here. What will you do?" +
              "\na: Continue focusing mostly on club work and orient clubs towards your major." +
              "\nb: Give up one or two clubs to focus more on academics." +
              "\nc: Move towards clubs that are known to party and go into the party life.")
        choiceb = input("> ").lower()

# end results if chose B

        while choiceb != "a" and choiceb != "b" and choiceb != "c":
            print("Invalid choice. Try again.")
            choiceb = input("> ").lower()

        if choiceb == "a":
            print("You're doing well at college, but starting to lose sight of what you're here for. " +
                  "\nMaybe be you afford to focus a little more on academics or social life, but don't " +
                  "feel obligated to change. \nYou're doing fine. Continue to next year.")

        elif choiceb == "b":
            print("Your grades are rising, and you are tying more of what you learn to the clubs you are in. " +
                  "\nYou're very motivated, and you have a lot of friends. Keep it up! Go to next year.")

        elif choiceb == "c":
            print("You're grades are dropping, but you are having a great time at parties. " +
                  "\nYou have so many friends, but you have been under the influence more. Your parents are worried " +
                  "and you are a little worried too. \nBalance a little better next year!")

# second choice if chose C

    elif choice1 == "c":
        print("You're grades have suffered greatly, but you're having a great time! " +
              "\nYou're parents are concerned about your academics, and you realize that you are participating in " +
              "\nillegal substances to the point where you can see yourself becoming addicted. " +
              "What do you do in your next year?" +
              "\na: College is all about having fun. Keep partying!" +
              "\nb: Cut down a little on the parties and focus on raising your grades, " +
              "but still go out every other week" +
              "\nc: Remove all social activities to focus on grades.")
        choicec = input("> ").lower()

# end results if chose C

        while choicec != "a" and choicec != "b" and choicec != "c":
            print("Invalid choice. Try again.")
            choicec = input("> ").lower()

        if choicec == "a":
            print("Your grades are dangerously low. You need to smoke or drink regularly or else you feel " +
                  "feel anxious.\nYour parents have gone from worried to furious and pressing, and your academic " +
                  "advisor has warned you about your grades.\nYou need to make some choices if you want to " +
                  "stay in college.\nOf course, it isn't the end of the road if you leave but keep in mind for " +
                  "next year that you are at risk.")

        elif choicec == "b":
            print("Your grades are rising, and you are less reliant on substances. Your parents are relieved, " +
                  "and you feel a lot better.\nYou have lost some party friends, but gained other friends who don't " +
                  "party as much.\nYou are more motivated and like your major more. Keep it up! Go to next year.")

        elif choicec == "c":
            print("Your grades have risen massively. Your remaining friends are shocked, and most of your " +
                  "party friends have stopped hanging out with you.\nWhile you're struggling mentally and " +
                  "emotionally from the social strain, you are relieved that you are finding your path again " +
                  "and your parents are ecstatic.\nMaybe join a few clubs to balance your life for next year.")


main()
