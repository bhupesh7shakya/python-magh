# def sum(a,b):
#     print(a+b)
    
# sum(1,2) 

sum= lambda a,b:a+b

# print(sum(1,2))

def func(n):
    return lambda x:x*n

# lambda x:x*2
doubler=func(2)
print(doubler(10))