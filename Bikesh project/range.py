# def my_range(start, stop, step):
#     print(start)
#     start+=step
#     if start>stop:
#         return 0
#     else:
#         my_range(start, stop, step)
# my_range(1, 10, 2)




def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    if b!=0:
     print(a/b)
    else:
        return "Cannot divided by zero"
    
a= int(input("First Number:"))
b= int(input("Second Number:"))
c= input("Operation(+,-,*,/):")
if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b)
else:
    print ("Invalid Number")

print(f"print: {print}")
