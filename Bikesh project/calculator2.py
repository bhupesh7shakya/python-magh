a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

c = input("Enter operation (+, -, *, /): ")
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Jaba timi lai thaa xa ki zero le divide hudai na. invalid vanxa vane kina divide gara ko ma sita jiske ko. bsdk gaad faad dinxu."
    
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
