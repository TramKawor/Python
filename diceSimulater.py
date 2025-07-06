import random

choice = (input("Wanna roll a dice (Y/N)\n"))
if "Y" in choice:
    a = "b"
    while a == "b":
        roll = random.randint(1, 6)
        print(f"You rolled {roll}")
        a = str(input("Roll again? (Y/N)\n"))
    else:
        print("Goodbye!")
else:
    print("INVALID INPUT")