'''
Remember the rules:

Snake   drinks  Water       and wins.
Water   drowns  the Gun     and wins.
Gun     shoots  the Snake   and wins.

Suppose: 

    Snake = 1, Water = 0, Gun = -1

'''
import random

'''
youChosed = input("Enter your choice: ")
youChosed = youChosed[0].lower() 
yourDict = {"s": 1, "w": 0, "g": -1}
you = yourDict[youChosed]

computer = random.choice([1, 0, -1])

if(you == computer):
    print("Match Draw. ")

else:
    if  (you == 1 and computer == 0):  # 1+0 = 1        # 1+(-0) = 1
        print("You Win!") # Win............................................

    elif(you == 1 and computer == -1): # 1+-1 = 0       # 1+(-(-1) = 2
        print("You Lose!")

    elif(you == 0 and computer == 1):  # 0+1 = 1        # 0+(-1) =-1
        print("You Lose!")

    elif(you == 0 and computer == -1): # 0-1 = -1       # 0+(-(-1) = 1
        print("You Win!") # Win............................................

    elif(you == -1 and computer == 0): # -1+0 = -1      # -1+(-0) = -1 
        print("You Lose!")

    elif(you == -1 and computer == 1): # -1+1 = 0       # -1+(-1) = -2
        print("You Win!") # Win............................................
        
    else:
        print("Something is wrong...")

# First approach will not work. (because 1,0,-1 all for win)
# Secound approach will work. (because of only 1,-2 you can win)
# So, now(The Most Small, Complex, Time-Efficient: approach): 
'''
print("\n")
n = int(input("..:: The Total Point: "))
print("\n")

draw = 0
win = 0
count = 0
while (count != n):

    yourInput = input(f"{count+1}. Enter your choice (S for Snake, W for Water, G for Gun): ")
    print("\n")
    yourInput = yourInput[0].lower() 

    if yourInput in ("s", "w", "g"):
        count += 1
        yourDict = {"s": 1, "w": 0, "g": -1}
        you = yourDict[yourInput]
        optionsStr = {1: "Snake", 0: "Water", -1: "Gun"}
        computer = random.choice([1, 0, -1])

        print(f"---> You Chose: {optionsStr[you]} AND The Computer Chose: {optionsStr[computer]}\n")


        if(you == computer):
            print("..:: Match Draw. ")
            draw += 1
        else:
            if(you - computer == 1 or you - computer == -2):
                print("..:: You Win!") # Win............................................
                win +=1
            else:
                print("..:: You Lose!")

        print("\n")
        lose = n-(win+draw) # for wrong input win and draw will not be increased. So, without WIN and DRAW everything(errors & loses) will count as LOSE....


    else:
        print("Invalid input. Please choose S, W, or G.")
        print("\n")

print(f"==> Total Win/(s): {win}, Lose/(s): {lose} and Draw/(s): {draw} in {n} Points...")
print("\n")
