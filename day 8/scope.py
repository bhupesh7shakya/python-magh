a=10


# def hello():
#     print(a)
#     a=11
    
# print(a) 
# hello()


# def outer():
#     def inner():
#         print('inner sees a as ',a)    
#     print("outer sees a  as",a )
#     inner()

# print("gloabll  a as",a)
# outer()
    
    
def changer():
    global a
    a=11

changer()
print(a)