a=float(input('enter the first number:'))
b=float(input('enter the second number:'))
operator=input("select the operator(+,-,/,*):")
if  operator=='/':
    if b==0:
        print("Ye vai 0 na haan")
    else:
        print("answer is:",a/b)        
elif  operator=='+':     
    print("answer is :",a+b)
elif   operator=='-':
    print("answer is:",a-b)    
elif   operator=='*':
    print("answer is:",a*b)
else:print("invalid number")

def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:  
            return num1 / num2
        else:
            return "Error: zero le divide jadain vai"
    else:
        return "Error: Invalid operator!"
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
result = calculator(num1, num2, operator)
print("Result:", result)

# Assignment to print 2 to 10 number using recursion function(2,4,6,8,10)

# def print_even(n):
#     if n <= 10:
#         if n % 2==0:
#             print(n)
#         print_even(n + 1)

# print_even(1)


# Assignment 3
# def person(name, age, location):
#     print("Hello","i am ",age,"and", name , "I am live in", location)
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# location = input("Enter your location:")
# person(name, age, location)

# # Assignment 4
# # def sum_numbers(*args):
# #     return sum(args)
# # result = sum_numbers(1, 2, 3, 4)
# # print("Sum:", result)

#class work (day 7) #Method
# name=[]
# for i in range(10):
#     names=input("enter players name:")
#     name.append(names)
# print(name)










        

  