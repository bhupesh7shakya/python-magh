from module import *
 
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

print(f"Print: {result}")
