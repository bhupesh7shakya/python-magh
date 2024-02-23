a = int(input("First number: "))
b = int(input("Second number: "))
c = input("Operation (+, -, *, /): ")

if c == '+':
    result = a + b
elif c == '-':
    result = a - b
elif c == '*':
    result = a * b
elif c == '/':
    if b != 0:
        result = a / b
    else:
        result = "Bsdk 0 kine rakhe ko jaba timi lai thaa xa ki zero le kehi huna wala xhai na"
else:
    result = "Invalid operation"

print(result)