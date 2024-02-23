# def hello(f_name,m_name,l_name):
#     print(f'hello {f_name},{m_name},{l_name}')

# hello('Bikesh','kumar','yadav')


# def hello(f_name,m_name,l_name):
#     print(f'$$hello,{f_name},{m_name},{l_name}$$')
#     return 1
# a= hello(m_name='Kumar', f_name='Bikesh',l_name='Yadav')
# print(a)





# def person(*names):
#     # names = ('Bikesh')  [ single name print in row]
#     for name in names:
#         print(f"hello,{name}")

# person ('Bikesh','Shivesh','sandip')



# def person(**attrs):
#     print(attrs['name'],attrs['age'])

# person(name="Bikesh", age= 22)




# def number(n=1):
#     print(n)
#     if n==20:
#         return
#     number(n+1)


# number()




# tasks
# implement function the calculator 

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

c = input("Enter operation (+, -, *, /): ")

if c == "+":
    result = add(a, b)
elif c == "-":
    result = sub(a, b)
elif c == "*":
    result = mult(a, b)
elif c == "/":
    result = div(a, b)
else:
    result = "Invalid operation"

print(f"Result: {result}")




# #  range

# def my_list(start, end, step):
#     return list(range(start, end, step))
# result_list = my_list(1, 10, 2)
# print(result_list)
