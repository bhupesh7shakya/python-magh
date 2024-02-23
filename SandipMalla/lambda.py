# def sum(a,b):
#     print(a+b)
# print(sum(2,2))
# sum = lambda a,b:a+b
# print(sum(3,5))

def func(n):
    return lambda x:x*n

tripler = func(3)
print(tripler(5))  #8
