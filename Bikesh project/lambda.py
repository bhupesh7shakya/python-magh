# def sum(a,b):
#     print(a+b)

# sum = lambda a, b:a+b
# print(sum(6,2))



def func(n):
    return lambda x:x*n

# lambda x:x*4
# doubler = func(4)
# print(doubler(10))

tripler = func(3)
print(tripler(10))
