is_login= False

datbase= [

]

def login():
    global login
    user_name= input("username:")
    password= input("passsword:")

    for user in datbase:
        if user['name']== user_name and user['password']== password:
            user['login_in']= True
            is_login= True
            print("login successful !")
            return
        print("Invalid username or password.")

def register():
    email= input("Enter your Email:")
    user_name= input("Enter your Username:")
    password= input("Enetr your Password:")

    for user in datbase:
        if user['email']== email:
            print("Email Id Already Uses. Please change your Email Id.")
            return

    for user in datbase:
        if user['username']== user_name:
            print("Username Already Uses. Please change your Username.")
            return
        
    datbase.append({'email': email, 'username': user_name, 'password':password, 'login_in':False})
    print("Registration Successful !")

def list_user():
    print("list of registered users:")

    for user in datbase:
        print(f"username: {user['name']}")

while True:
    choice= input ("Are you new user please register? (yes/no):").lower()
    if choice== 'yes':
        register()
    elif choice== 'no':
        break
    else:
        print("Invalid choice. please enter 'yes' or 'no'.")
if not is_login:
    login()
list_user()