# a = int(input("Enter first numbers: "))
# b = int(input("Enter second numbers: "))
# c = (input("Enter any one operator '+', '-' , '*' , '/', '**', '%', '//': "))
# from add import *
def sum(a,b):
     return print(f"The sum of {a} and {b} is {a + b}")
def subtract(a,b):
    return print(f"The difference between {a} and {b} is {a - b}")
def product(a,b):
    return print(f"The product of {a} and {b} is {a * b}")
def divide(a,b):
    return print(f"{a} divided by {b} is {a / b}")
def expo(a,b):
    return print(f"{a} raised to the power of {b} is {a ** b}")
def mod(a,b):
    return print(f"The remainder when {a} is divided by {b} is {a % b}")
def quotient(a,b):
    return print(f"The quotient when {a} is divided by {b} is {a // b}")
    
# if c=='+':
#     sum(a,b)
# elif c=='-':
#     subtract(a,b)
# elif c=='*':
#     product(a,b)
# elif c=='/':
#     if b==0:
#         print('Divider cannot be 0')
#     else:
#      divide(a,b)
# elif c=='**':
#     expo(a,b)
# elif c=='%':
#     mod(a,b)
# elif c=='//':
#     quotient(a,b)
# else:
#     print('Wrong operator chosen, please choose the correct operator')