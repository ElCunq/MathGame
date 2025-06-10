import random

point = 0
i = 0

def maths(c,answer):
    global point
    if c == answer:
        print ("Correct! Here is +1 point for you.")
        point += 1
    else:
        print ("Wrong! I'll take one of your points.")
        point -= 1

def easy():
    global point , i
    print ("You have chosen the LOSERS path you idiot. We are starting with 5 questions.")
    for i in range (5):
        num1 = random.randint(1,50)
        num2 = random.randint(1,50)
        if num1 >= num2:
            answer = num1 - num2
            print ("Quesiton ", i, "\n", num1, "-", num2)
        else:
            answer = num1 + num2
            print ("Quesiton ", i, "\n", num1, "+", num2)
        u_answer = int(input("Your Answer: "))
        maths(u_answer,answer)
    i += 1
    print ("Your last point is: ", point)


def normal():
    global point , i
    print ("You have chosen middle classers path adventurer. You are going to answer 10 questions.")
    for i in range (10):
        num1 = random.randint(1,100)
        num2 = random.randint(1,100)
        if num1 >= num2:
            answer = num1 - num2
            print ("Quesiton ", i, "\n", num1, "-", num2)
        else:
            answer = num1 + num2
            print ("Quesiton ", i, "\n", num1, "+", num2)
        u_answer = int(input("Your Answer: "))
        maths(u_answer,answer)
    i += 1
    print ("Your last point is: ", point)

def hard():
    global point , i
    print ("Aaah! I see. You choose the real mans path. I'm proud of you. Now answer this 10 quesitons.")
    for i in range (10):
        num1 = random.randint(50,500)
        num2 = random.randint(50,500)
        operator = random.choice(['+', '-', '*'])
        print (num1, operator, num2)
        expression = f"{num1} {operator} {num2}"
        answer = eval (expression)
        u_answer = int(input("Your Answer: "))
        maths(u_answer,answer)
    i += 1
    print ("Your last point is: ", point)



selection = str(input("Please select your destination (Easy: e, Normal: n, Hard: h): "))

if selection == 'e':
    easy()
elif selection == 'n':
    normal()
elif selection == 'h':
    hard()
else:
    print("You have chosen the wrong path! Try from one of the options.")

