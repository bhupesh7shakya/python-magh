# name='shivesh\n'
# print(name*10)


# a=10                                    
# b=20                   

# result=a/b                                                                   
# print("divide=",result)
                              
# a=10
# b=15
# result=a**b
# print(result)

# a=10
# b=15
# result=a//b
# print(result)

# a=10
# a+=7
# print(a)

# a=10
# a//=15
# print(a)

# a=5
# b=4
# print(a==b)

# a=5
# b=4
# print(a!=b)

# a=5
# b=4
# print(a>=b)

# Condition

# a='sandip'
# b='prakash'
# c='bikesh'
# if (a and b)!=c:
#     print(True)
# else:
#     print(False)

#For reverse string
# a='arjun'[::-1]
# print(a)

# a=input('enter first number')
# b=input('enter second number')
# sum=int(a)+int(b)
# print("the sum is:",sum)

# age=18
# if age> 18:
#     print("adult")
# elif age<18:
#     print("noob")
# else:
#     print("mc")   



# n=0  
# while n<=10:
    
#     print(f'{n} hello')
#     if n==5:
#         break
#     n+=1
# print('loop ends')

# numbers=range(10)
# print(numbers)

# n=0
# while n<=10:
#     if n%2==0:

#         print(n)
#     n+=1
# print('loop ends')       
    
# for i in range(5,10):
#    if i%2!=0:
#        print(i)
 
# for i in range(20):
#     if i%2==0:
#         print(i)


# number = int(input("Enter a number: "))
# factorial =1
# current_number = 1
# while current_number <= number:
#     factorial *= current_number
#     current_number += 1
# print("The factorial of", number, "is:", factorial)

# n=0
# while n<=20:
#     if n%2!=0:
#         print(n)
#     n+=1
# print("loop ends")

# number=int(input("enter a number:"))
# factorial=1
# current_number=1
# while current_number<=number:
#     factorial*=current_number
#     current_number+=1
# print("the factorial of",number,"is:",factorial)


# a=int(input("enter a number:"))
# d=0
# while a!=0:
#     c=a%10
#     d=d*10+c
#     a=int(a/10)
    


# print(d)

# FUNCTION

# def hello(f_name,m_name,l_name):
#     print(f'hello,{f_name}{m_name}{l_name}')
#     return 1
# a=hello('shivesh','kumar','mishra')
# print(a)

# def person(*names):
#     for name in names:
#         print(f"hello,{name}")
# person('ram','shayam','rita',123,)

# def person(**attrs):
#     print(attrs['name'],attrs['age'],attrs['clz'])
# person(name="shivesh",age=24,clz="hicole")

# def number(n=1):
#     print(n)
#     if n==20:
#         return
#     number(n+1)    
# number()

# def star(func):
#     print("SAnd")
#     def wrapper(name):
#         print('*'*10)
#         func(name)
#         print('*'*10)
#     return wrapper
# def hello(name):
#     print('hello',name)
# # def bye():
# #     print('hello')
# star(hello)('Sivesh')
   
# lambda  

# sum=lambda a,b:a+b
# print(sum(10,12))

# def func(n):
#     return lambda x:x*n
# tripler=func(3)
# print(tripler(5))

# datatype methods

# String function
# a="abcd"
# print(len(a))
# print(a.upper())
# print(a.strip())
# print(a.split())

# list function
# fruits=[
#     "apple"
# ]
# fruits.append('mango')
# print(fruits)

# class wrok(to print 10 elements)
# name=[]
# for i in range(10):
#     names=input("enter players name:")
#     name.append(names)
# print(name)


# a=[1,2,3]
# b=[6,7]
# a.extend(b)
# print(a)

# a=[1,2,3,4]
# b=[5,6,7]
# c=[10,12,14]
# c.remove(12)
# print(c)


# fruits = ['apple', 'banana', 'orange', 'grape', 'kiwi']
# print( fruits)
# fruits.pop(1)
# print( fruits)


# my_list = []
# my_list.insert(0, 'apple')   
# my_list.insert(1, 'banana') 
# my_list.insert(2, 'orange')  
# my_list.insert(3, 'grape')   
# print("Modified List:", my_list)



# fruits = ['apple', 'banana', 'orange', 'grape', 'kiwi']
# index_of_orange = fruits.index('orange')
# print("Index of 'orange':", index_of_orange)

# # day 8 (scope.py)
# a=10
# def hello():
#     print(a)
#     a=10
# print(a)
# hello()     

# a=10
# def changer():
#     global a
#     a=11
# changer()
# print(a)

# database=[
#     {
#         'name':'vindi',
#         'password':'<ovaiii>'
#     },
#     {
#         'name':'praku',
#         'password':'<hehehe>'
#     }
# ]
# print(database)
# for i in range(2):
#     name=input('name:')
#     password=input('password:')


#     user={  
#     'name':name,
#     'password':password   
#     }
    
#     database.append(user)
# print(database)

# isLogin='false'
# database=[
#     {
#         'name':'vindi',
#         'password':'ovaiii'    
#     },
#     {
#         'name':'praku',
#         'password':'hehehe',
#     }
# ]

# def login():
#     username = input('Username: ')
#     password = input('Password: ')

#     for user in database:
#         if user['name'] == username and user['password'] == password:
#             user['logged_in'] = True
#             print('Login successful!')
#             return
#     print('Invalid username or password.')

# print("Before login:", database)
# login()
# # print("After login:", database)

isLogin = False
database = []

def login():
    global isLogin
    username = input('Username: ')
    password = input('Password: ')

    for user in database:
        if user['name'] == username and user['password'] == password:
            user['logged_in'] = True
            isLogin = True
            print('Login successful')
            return
    print('Invalid username or password.')

def register():
    global database
    username = input('Enter username: ')
    password = input('Enter password: ')

    for user in database:
        if user['name'] == username:
            print("Username already exists. arko choose gar vai.")
            return
    
    database.append({'name': username, 'password': password, 'logged_in': False})
    print("Registration successful")

def list_users():
    global database
    print("List of registered users:")
    for user in database:
        print(f"Username: {user['name']}")

while True:
    choice = input("Do you want to register a new user? (yes/no): ").lower()
    if choice == 'yes':
        register()
    elif choice == 'no':
        break
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
if not isLogin:
    login()
list_users()  





     
 

    
              


          
          
          


    
