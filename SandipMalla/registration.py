isLogin=False
database = [{'email': 'scrsandeep@gmail.com', 'name':'Sandip','password': 'sandip123'},
            {'email': 'naruto@gmail.com', 'name':'Naruto', 'password': 'naruto123'},
            {'email': 'sasuke@gmail.com', 'name':'Sasuke', 'password': 'sasuke123'},
            {'email': 'luffy@gmail.com',  'name':'Monkey D. Luffy','password': 'luffy123'},
            {'email': 'ace@gmail.com', 'name':'Portugas D. Ace', 'password': 'ace123'}
            ]
def  login():
    global isLogin
    global p_name
    p_email = input("Enter your email: ")
    p_name = input('Enter your name: ')
    p_password = input("Enter your password: ")
    for  data in database:
        if(data['email'] == p_email and  data['name']==p_name and data['password']==p_password):
            isLogin = True
            # print(f"Logged In Successfully.\n Welcome back {p_name}")
login()
if isLogin==True:   
    print(f"Logged In Successfully.\n Welcome back {p_name}")
    print(f"Here's your database \n {database}")
else:
    print(f"\nIncorrect Email/Password or Name.\n Please check it and try again!!!")
 