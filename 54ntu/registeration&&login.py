is_loggedIn = False
database = []


def mainFunction():
    choice = input("1. Register 2. Login\n")
    if choice == "1":
        register()
    elif choice == "2":
        login()
    else:
        print("Invalid choice")
        mainFunction()


def register():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Check if the email already exists in the database
    for userdata in database:
        if userdata['email'].lower() == email.lower():
            print("Email already exists")
            mainFunction()

    newdata = {"name":name,"email":email,"password":password}
    database.append(newdata)
    print("data inserted successfully")
    mainFunction()  

    
def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    for userdata in database:
        if((userdata['email'].lower() == email.lower()) and (userdata['password'] == password) ):
            is_loggedIn = True
            print("You are logged in")
            print(f"loggedin status is {is_loggedIn}")
            print(f"database values are {database}")
        else:
            print("creadentials are not matching")
            print("*"*10)
            print("enter your email and password again ")
            login()

mainFunction() # main function is called