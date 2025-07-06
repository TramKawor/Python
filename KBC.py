questions= [
    ["1. Who is known as the father of Asia", "Gautam Buddha", "Jesus Christ", "Lord Shivaji", "Prophet Mohamad",None, 1],
    ["2. Who is known as the father of World", "Gautam Buddha", "Jesus Christ", "Lord Shivaji", "Prophet Mohamad",None, 2],
    ["3. Who is known as the father of Computer", "Gautam Buddha", "Jesus Christ", "Charles Babbage", "Prophet Mohamad",None, 3],
    ["4. Who is known as the father of Nepal", "Gautam Buddha", "Jesus Christ", "Lord Shivaji", "Prithivi Narayan Shah",None, 4],
]
levels = [1000,2000,3000,4000,5000,10000,20000,50000,100000,300000,500000,600000,700000,1000000,10000000]

for i in range(0, len(questions)):
    question = questions[i]
    # for i in range(0, len(questions)):
    #     print(f"{question[0+i]}")
    print(f"Question for Rs.{levels[i]} :\n")
    
    print(f"1. {question[1]}          2. {question[2]}")
    print(f"3. {question[3]}          4. {question[4]}")
    reply = int(input("\nChoose your answer between 1 to 4 or 0 to quit:\n"))
    if reply == 0:
        money == levels[-1]
        break
    if reply == question[-1]:
        print(f"Correct Answer, you have won Rs.{levels[i]}.\n")
        if(i == 4):
            money = 5000
        elif(i == 8):
            money = 100000
        elif(i == 12):
            money = 1000000
    else:
        print("Sorry, wrong answer.\n")
        break

print(f"Congratulations, You have won {money}")

 

