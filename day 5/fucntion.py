# def hello(f_name,m_name,l_name):
#     print(f'$$hello,{f_name} {m_name} {l_name}$$')
#     return 1
# a=hello(m_name='bahadur',f_name='ram',l_name='somting')
# print(a)                                                                                                                        


# def person(*names):
#     for name in names:
#         print(f"hello,{name}")
    
# person('ram','shyam','fjlsdkfj',1,2,3,4,5)


# def person(**attrs):
#     print(attrs['name'],attrs['age'])
    
# person(name="ram",age=12)


def number(n=1):
    print(n)
    if n==10:
        return
    number(n+1)


number()


# taks
# implement fucntionin the caclulator


print(list(range(1,10,2)))