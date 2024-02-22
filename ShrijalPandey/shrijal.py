"""
my_string="hello world apple"
print (type(my_string))             string
print (my_string[1:-1])

fruits=[
'apple', 'orange',1,1,1
]                                    list
fruits[0]='banana'
print(fruits[0])
"""
'''
fruits=(
   'apple', 'banana',2,2,1 )   
 # fruits[1]='orange' tuple doesnot support changing of variable            tuple
print(fruits[1])
'''
'''
my_set={
12,33,14,78,'helllo'  
}                               set
print(my_set[4])            value is random , particular print garna mildaina
'''
'''
person= {
'name' : 'ram',
'age' :20,
'city' : 'kathmandu',
'family_members' :[                 dictionary
'father',
'mother',
'sister',
'brother',
]
}
print(person['name'],person['age'],person['family_members'])
 output 
ram 20 ['father', 'mother', 'sister', 'brother']
'''
'''
name='ram'
print ('hello',name,'k gardai xau')
'''
'''
person= {
'name' : 'Ram',
'age' :20,
'city' : 'Kathmandu',
'family_members' :[
'father','mother','sister','brother',
]
}
print('My name is', person['name'])
print('I am', person['age'], 'years old')
print('I live in', person['city'])
print('My family members are',person['family_members'])
'''
'''
name='shrijal'
address='kathmandu'
print(f'my name is {name} and i live in {address}')
'''
'''
x=float('3.14')
print(x)
print(type(x))
'''
'''
x=bool(1)
print(x)
x=int(bool(x))
print(x)
'''
'''
x=list((1,2,3)) 
print(x)
'''
'''
a=1000
b=3
sum=a+b
diff=a-b
pro=a*b
div=a/b
mod=a%b
exp=a**b
floordiv=a//b

print(sum)
print(diff)
print(pro)
print(div)
print(mod)
print(exp)
print(floordiv)
'''
'''
a=99
a%=a
print(a)
'''
'''
a=20
b=10
if(a==b):
 print(a, 'is equal to', b)
elif(a<b):
 print(a, 'is less than', b)
else:
 print(b, 'is less than', a)
 '''
''' 
a=10
b=2
print (a<=1 and b>1)
print(a<b or b>a)
print(not(a>b or b>a))
'''

'''name=input('enter your name')
print(name)'''

##homework
#user input
#a float
#b float
#user input operators 
#make a calculator

#hello world ko ulto

#mother ko t nikalne
#brother ko ulto

"""
#calculator
first=input("enter a number")
operator=input("enter operator[+,-,*,/,%]")
second=input("enter a number")
first=float(first)
second=float(second)
if operator=="+":
    print('The sum is',first + second) 
elif operator=="-":
    print('The difference is',first - second)
elif operator=="*":
    print('The product is',first * second)
elif operator=="/":
    print('The division is',first / second)
elif operator=="%":
    print('The remainder is',first % second)
else: 
    print("Math Error")
    """
"""
#hello world ko ulto
a='hello world'
print(a[::-1])
"""
'''
person= {
'name' : 'ram',
'age' :20,
'city' : 'kathmandu',
'family_members' :  {           
'father','mother','sister','brother'
}
}
print(person['family_members':[2]])
'''
'''
n=1
while n<=10:
    print(f'{n}hello')
    if n==5:
        break
    n+=1
print('loop ends')
'''
'''
a=range(0,100,5)
print(tuple(a))
'''
'''
#print even number
n=2
while n<=100:
    print(n)
    if n==10:
         break
    n=n+2
    '''
#print(88 in (2,7,8,9,0))
    
'''for i in range(1,20,1):
    print(i)
'''
'''
fruits=['apple', 'banana', 'orange']
fruits[1]='watermelon'
for a in fruits:
    print(a)
        '''
'''
fruits=['apple', 'banana', 'orange']
fruits[1]='watermelon'
for i,a in enumerate(fruits):
    print(i,a)
   '''
 #for loop use garera odd
#for i in range(1,100,2):
    #print(i)
'''
def shrijal():
    print('hello world')
       
shrijal()
'''
'''
def hello(name):
    print(f'Hello {name}')
    
hello('ram')
hello('shyam')
'''

'''
def hello(hi,f_name,l_name,):
    print(f'{hi} {f_name} {l_name}','?')  
    return 'shrijal' 
a=(hello('how are you', 'shrijal','pandey'))
print(a)
'''
'''
def person(*names):
        for name in names:
            print(f'hello {name}')
        
person('shrijal','ram','shyam')
'''
'''
def person(**attrs):
    print (attrs['name'],attrs['age'])   
    
person(name='ram',age=111)
'''
'''
def number(n=1):
    print(n)
    if n==10:
        return 
    number(n+1)
    
number()
'''

#hw. calculator ma function include garnu
#. print(list(range(2,10,2)) 
'''
def main():
    first = float(input("Enter the first number: "))
    operator = input("Enter operator [+,-,*,/,%]: ")
    second = float(input("Enter the second number: "))
    
    if operator == "+":
        result = first + second
    elif operator == "-":
        result = first - second
    elif operator == "*":
        result = first * second
    elif operator == "/":
        if second != 0:
            result = first / second
        else:
            result = "Division by zero is not allowed"
    elif operator == "%":
        result = first % second
    else:
        result = "Math Error"

    print("Result:", result)

main()
'''
'''
numbers = list(range(2, 10, 2))   
for number in numbers:
    print(number)
'''
'''

def star(func):
    def wrapper():
        print('*'*10)
        func()
        print('*'*10)
    return wrapper
@star
def hello():
    print('hello')

@star    
def bye():
    print('hello')
    
hello()
bye()
'''
'''
a='shrijal'
a=len(a)
print (a)
'''
'''
a='       heLLo SHrIjAL '
print(a)
print(len(a))    #length of string
print(a.lower()) #lowercase
print(a.upper()) #uppercase
print(a.strip()) #removes spaces
print(a.split()) #makes list
'''
'''
fruits=['apple']
for i in range(10):
    a=input('enter name of the fruit')
    fruits.append(a)
    
print(fruits)
'''
#hw
'''
top lvl database variable
name, email, password


'''
'''
a=[7,8,9]
b=['apple','banana']
a.extend(b)
a.insert(1,3)
a.remove(9)
a.pop(0)
print(a)
'''
'''
first=input("Enter a number:")
operator=input("Enter operator[+,-,*,/,//,%,**]:")
second=input("Enter a number:")
first=float(first)
second=float(second)
if operator=="+":
    print('The sum is',first + second) 
elif operator=="-":
    print('The difference is',first - second)
elif operator=="*":
    print('The product is',first * second)
elif operator=="/":
    print('The division is',first / second)
elif operator=="//":
    print('The truncated division is',first // second)
elif operator=="%":
    print('The modulus is',first % second)
elif operator=="**":
    print('The exponentiation is',first ** second)
else: 
    print("Math Error")
'''

#recursion
'''
def range(n=1):
    print(n)
    if n==16:
        return
    range(n+4)
    
range()
'''


#15 FEB
'''
a=10
def hello():
    a=11
    print(a)
   # a=11 error falxa

hello()
print(a)
'''

'''
a=10
def outer():
    a=12
    def inner():
        
        print('inner sees a as', a)
    print('outer sees a as', a)
    inner()
outer()
print('global a as', a)   
'''
#a ko value change garxa
'''
a=10
def hi():
   global a
   a=11
    
hi()
print(a)
'''
#OOP
'''
class house:
    window=10
    color='black'
    door=1
class hous:
     window=11
     color='blue'
     door=3
ram_ghar=house()
print(ram_ghar.color)
hari_ghar=hous()
print(hari_ghar.color)
'''

'''
class house:
    window=10
    color='black'
    door=1
    
    def set_window(self,window):
        self.window=window
        

    def get_window(self):
        return self.window
        
ram_ghar=house()
#ram_ghar.set_window(11)
#print(ram_ghar.window)
'''

'''
class burger:
    def cheese(self):
        print('cheese')
        return self
    
    def patty(self):
        print('patty')
        return self

Burger=burger()

Burger.cheese().patty().cheese()
'''

'''
is_Login = False
Database = {
    "name": "Shrijal",
    "cast": "Pandey",
    "age": 18,
    "id": 25,
    "password": "shrijal123@",
    "email": "shrijal@gmail.com"

    
}
def Register():
    database = {
        "name": input("Enter name: "),
        "cast": input("Enter caste: "),
        "age": input("Enter age: "),
        "id": input("Enter id: "),
        "password": input("Enter password: "),
        "email": input("Enter email: ")
    }
    return database

registered_user = Register()


if Database == registered_user:
    def update_global():
     global is_Login 
    is_Login=True
    print(is_Login)
    update_global()
    print("Values match")
    print(show)
    
else:
    print(is_Login)
    print("Wrong person")
'''
'''
#single inhertance
class grandfather():
    house='good house'
    
class father(grandfather):
    car='nano'
 
    def __init__(self):
        print('i am father')
        print(self.car)
        super().__init__()
        
class mother:
    jwellery='gold'
    money='$'
  
class son(father,mother):
    console='ps3'
    
    def __init__(self):
        print(self.console)
        super().__init__()
    
    
son=son()
#print(son.house)
#print(isinstance(son,father))

'''
'''
class Person:

    def __init__(self,name,age,password) -> None:
        self.name=name
        self._age=age
        self.__password=password
        
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self,password):
        self.__password=password
    
person=Person('name',12,'password')
person.password='new'
print(person.password)
        
'''
'''
#abstraction: inbuilt module

from abc import ABC,abstractclassmethod

class computer(ABC):
    
    def run(self,app):
        self.process(app)
        
    @abstractclassmethod
    def process(self,app):
        pass
    
class laptop(computer):
    
    def process(self,app):
        print('pubg is running on '+app)
        
class mobile(computer):

    def process(self,app):
        print('chrome is running on '+app)
        

acer=laptop()
acer.run('laptop')

samsung=mobile()
samsung.run('mobile')
'''
'''
is_Login = False

Database = {
    "name": "Shrijal",
    "cast": "Pandey",
    "age": 18,
    "id": 25,
    "password": "shrijal123@",
    "email": "shrijal@gmail.com"
}

def Register():
    database = {
        "name": input("Enter name: "),
        "cast": input("Enter caste: "),
        "age": input("Enter age: "),
        "id": input("Enter id: "),
        "password": input("Enter password: "),
        "email": input("Enter email: ")
    }
    return database

registered_user = Register()

if Database['email'] == registered_user['email'] and Database['password'] == registered_user['password']:
    is_Login = True
    print("Login successful")
    print("Welcome, " + Database['name'])
else:
    print("Login failed due to invalid credintals") 
    print("Try again")
'''
'''
while True:
    try:    
        a=int(input("first number"))
        b=int(input("second number"))
    
        if a==10:
            raise Exception("10 not allowed")    
        print(a/b)
    except ZeroDivisionError:
        print("A number cannot be divided by zero") 
        
    except Exception as e:
        print("something wnet wrong",e)    
 '''   
'''
while True:
    try:
        arr=[0,1,2,3,4] 
        a=int(input('enter any number'))
        if a>len(arr):
            raise Exception('Number should not be greater than 4')
     
        print(arr[a])

    except Exception as e:
        print('Something went wrong',e)
'''



