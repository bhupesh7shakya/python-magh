isLogin = False
database = [
            {'name':'Sandip Malla','email': 'scrsandeep@gmail.com','password': 'sandip123', 'age':24, 'address':'Kathmandu'},
            {'name':'Naruto Uzumaki','email': 'naruto@gmail.com', 'password': 'naruto123', 'age':24, 'address':'Kathmandu'},
            {'name':'Sasuke Uchiha','email': 'sasuke@gmail.com', 'password': 'sasuke123','age':24, 'address':'Kathmandu'},
            {'name':'Monkey DLuffy','email': 'luffy@gmail.com','password': 'luffy123','age':24, 'address':'Kathmandu'},
            {'name':'Portugas DAce','email': 'ace@gmail.com', 'password': 'ace123','age':24, 'address':'Kathmandu'}
            ]

def signup():
    f_name = input("Enter your first name: ")
    l_name = input("Enter your last name: ")
    email = input("Enter your email address: ")
    password = input("Create a password: ")
    age = input("Enter your age: ")
    address = input("Enter your address: ")
    details = {
        'name':f_name +" "+l_name,
        'email':email,
        'password':password,
        'age':age,
        'address':address
    }
    database.append(details)
    print("\nYour account has been created. Now you can log in.")
def login():
    email = input("Enter your email address: ")
    password = input("Enter your password: ")
    for data in database:
        if data['email']==email and data['password']==password:
            global isLogin
            isLogin = True
def listOfUsers():
    print(f" Below is the list of users.\n {database}")
    
while True:
    answer =input("Are you a new user? \n type 'yes' if yes and 'no' if not: ").lower()
    if answer=='yes':
        print("Please signup first. ")
        signup()
        login()
    elif answer =='no' or answer=="":
        print("Enter your credentials:\n")
        login()
    if isLogin == True:
        print(f"Logged in Succesfully. Welcome back!")
        listOfUsers()
    else:
        print("Please enter right credentils.")
        
