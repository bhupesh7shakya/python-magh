from random import randint as r
while True:
    a = int(input("Enter your ticket number between 1 and 5: "))
    b = r(1,3)
    if a==b:
        print("Congratulation!!! you've won $200,000 Lottery")
    else:
        print(f"Sorry, better luck next time. The number was {b}")