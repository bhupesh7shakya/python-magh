database = []
isLogin=False
for i in range (5):
    p_email = (input("Enter your email: "))
    p_name = (input("Enter your name: "))
    p_password = (input("Enter your password: "))

    details ={
        'email': p_email,
        'name' : p_name,
        'password': p_password,
    }
    database.append(details)
print(database)
