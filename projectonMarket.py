listOfFruits = {"1":"orange", "2":"banana", "3":"kiwi", "4":"mango", "5":"pineapple"}
listOfVegetables = {"1":"carrot", "2":"broccoli", "3":"cauliflower", "4":"potato", "5":"tomato"}
listOfNonVeg= {"1":"Fish", "2":"Mutton", "3":"Chicken", "4":"Beef", "5":"Buff"}

print("!!! Welcome to the Market !!!")

print("1. Fruits")
print("2. Vegetables")
print("Please choose from the above options:\n")
option=int(input())
if option == 1:
    print(listOfFruits)
    print("\n")
    print("Choose the fruit number that you wanna buy:\t")
    fName = str(input())
    if "1" in fName:
        print("The price of 1 Kg Orange is 100\n")
        print("How much kilo orange you wanna buy:\t")
        kilo = int(input())
        print("The total price is", kilo * 100)
    elif "2" in fName:
        print("The price of 1 Kg Banana is 80\n")
        print("How much kilo banana you wanna buy:\t")
        kilo = int(input())
        print("The total price is", kilo * 80)
    elif "3" in fName:
        print("The price of 1 Kg Kiwi is 120\n")
        print("How much kilo kiwi you wanna buy:\t")
        kilo = int(input())
        print("The total price is", kilo * 120)
    elif "4" in fName:
        print("The price of 1 Kg Mango is 150\n")
        print("How much kilo mango you wanna buy:\t")
        kilo = int(input())
        print("The total price is", kilo * 150)
    elif "5" in fName:
        print("The price of 1 Kg Pineapple is 200\n")
        print("How much kilo pineapple you wanna buy:\t")
        kilo = int(input())
        print("The total price is", kilo * 200)
    else:
        print("Invalid Input")

elif option == 2:
    print(listOfVegetables)
    print("Choose the vegetable that you wanna buy:\t")
    vName = str(input())
    print("\n")
    if "carrot" in vName:
        print("The price of 1 Kg Carrot is Rs.60\n")
        print("How much kilo carrot you wanna buy:\t")
        kilo = int(input())
        print("The total price is", kilo * 60)
    elif "broccoli" in vName:
        print("The price of 1 Kg Brocoli is Rs.50\n")
        print("How much kilo brocoli you wanna buy:\t")
        kilo = int(input())
        print("The total price is", kilo * 50)
    elif "cauliflower" in vName:
        print("The price of 1 Kg Cauliflower is Rs.40\n")
        print("How much kilo cauliflower you wanna buy:\t")
        kilo = int(input())
        print("The total price is", kilo * 40)
    elif "potato" in vName:
        print("The price of 1 Kg Potato is Rs.150\n")
        print("How much kilo potato you wanna buy:\t")
        kilo = int(input())
        print("The total price is", kilo * 150)
    elif "tomato" in vName:
        print("The price of 1 Kg Tomato is Rs.100\n")
        print("How much kilo tomato you wanna buy:\t")
        kilo = int(input())
        print("The total price is", kilo * 100)

elif option == 3:
    print(listOfNonVeg)
    print("Choose the Non veg Item: \n")
    nonVeg = str(input())
    print("\n")
    if "1" in listOfNonVeg:
        print("The price of 1 Kg Fish is Rs.400\n")
        print("How much kilo Fish you wanna but:\t")
        kilo=int(input())
        print("The total price is", kilo * 400)
    elif "2" in listOfNonVeg:
        print("The price of 1 Kg Mutton is Rs.450\n")
        print("How much kilo Mutton you wanna buy:\n")
        kilo=int(input())
        print("\n")
        print("The total price of is", kilo * 450)
        

else:
    print("Invalid Input")


