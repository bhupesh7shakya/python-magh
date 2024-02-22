a=10



# def hello():
#     print(a)
#     a=11

# hello()
# print(a)




# def outer():
#     a=12
#     def inner():
#         a=13
#         print("inner sees a as", a)
#     print("outer sees a as", a)
#     inner()

# print("global a as", a)
# outer()




def changer():
    global a
    a=11

changer()
print(a)