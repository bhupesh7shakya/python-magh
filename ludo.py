from random import randint as r
while True:
    a = input("Press 'Enter' to roll the dice: ")
    if a=="":
        print("Rolling the dice......")
        print(f"The number is {r(1,6)}")
        print("Please roll the diiice again!!!")
        