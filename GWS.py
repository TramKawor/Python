print("*************Welcome to the GWS Game*************")
game = ["snake", "gun", "water"]
print("Choices = snake or gun or Water")
yourChoice = str(input("Type what you want to choose: "))
if yourChoice in game:
    import random
    compChoice = random.choice(game)
    print("Your Choie is:", yourChoice)
    print("Computer Choice is:",compChoice)
    print("*******FINAL RESULT*********")

    if yourChoice == "snake" and compChoice == "gun":
        print("You lose the match.")
    elif yourChoice == "snake" and compChoice == "water":
        print("You win the match.")
    elif yourChoice == "snake" and compChoice == "snake":
        print("Match is tie.")
    elif yourChoice == "gun" and compChoice == "snake":
        print("You win the match.")
    elif yourChoice == "gun" and compChoice == "water":
        print("You lose the match.")
    elif yourChoice == "gun" and compChoice == "gun":
        print("Match is tie.")
    elif yourChoice == "water" and compChoice == "snake":
        print("You lose the match.")
    elif yourChoice == "water" and compChoice == "gun":
        print("You win the match.")
    elif yourChoice == "water" and compChoice == "water":
        print("Match is tie.")
    else:
        print("Invalid Input")

else:
    print("Type the write choice:")



