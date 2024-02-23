from module import *
while True:
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




