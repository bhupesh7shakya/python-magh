from calculator import *
while True:
    a = int(input("Enter first numbers: "))
    b = int(input("Enter second numbers: "))
    c = input("Enter any one operator '+', '-' , '*' , '/', '**', '%', '//': ")
    if c=='+':
        sum(a,b)
    elif c=='-':
        subtract(a,b)
    elif c=='*':
        product(a,b)
    elif c=='/':
        if b==0:
            print('Divider cannot be 0')
        else:
            divide(a,b)
    elif c=='**':
        expo(a,b)
    elif c=='%':
        mod(a,b)
    elif c=='//':
        quotient(a,b)
    else:
        print('Wrong operator chosen, please choose the correct operator')