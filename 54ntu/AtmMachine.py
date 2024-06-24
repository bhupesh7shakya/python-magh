#todos 
# set default values for pin
# define gloabl variable for total_balance, attempts=3
#take the pin 
#coampare it
#count the attempts
#if attempt is more than three then block that account

#if pin is ok then display the menus i.e. withdraw, deposit, inquiry and exit
#if selected withdraw then ask the user to enter the amount
# check whther the amount is sufficient or not
# if not sufficient then display the msg and go to main menu
#if sufficient amount then decrease the amount from total_balance
#print the remaining amount and go to main menu
# if deposit is selected then 
# ask the user to enter the amount
#then add the amount to the total_balance
# print the total balance amount and go to the main menu
#if inquiry then display the balance amount
# if exit then just exit the main menu



total_balance = 0
pin = 1234
attempts = 3

def ATM():
    global attempts    # here we declared attempts as global because if we want to modify the value of gloabl variables in python then we need to redeclare that variable as global inside the function
    if(attempts <=3 and attempts >0):  
        userPin = int(input("enter your pin : "))
        if(userPin ==pin):
            print("1. Withdraw      2.Deposit \n  3.Inquiry       4.Exit")

            userchoice = int(input("select your choice 1,2,3,4 : "))
            if(userchoice == 1):
                withdraw()
            elif(userchoice == 2):
                deposit()
            elif(userchoice == 3):
                inquiry()
            elif(userchoice == 4):
                exit()
        else:
            print("pin doesnot match")
            attempts = attempts - 1
            ATM()

    else:
        print("*"*10)
        print("your account is blocked")
        exit()


def withdraw():
    global total_balance
    amount = int(input("enter the amount in multiple of 1000 : "))
    if amount>total_balance:
        print("insufficient balance")
        ATM()
    else:
        total_balance = total_balance-amount
        print("please collect your card and cash   .....")
        print(f"your account is debited with Rs {amount} ")
        print(f"And remaining balance is : {total_balance}")
        print("Thank you for using NIC ASIA Bank")


def deposit():
    global total_balance
    amount = int(input("enter the amount you want to deposit : "))
    if(amount >0):
        total_balance += amount
        print(f"your account is creadited with Rs {amount} and the new balance is : {total_balance}")
        ATM()

    
    else:
        print(" \nAmount must be greater than 0 \n ")
        deposit()
    

def inquiry():
    print(f"your total balance is  {total_balance}")

ATM()
