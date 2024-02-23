# # # a = 10
# # # print(a, 'is a character')
# # # a = 'Hello World'
# # # print(a[::-1])
# # # a = 'samdjcbkjd'
# # # print(type(a))
# # # myString = "Hello World Programmers"
# # # a = [1, 2, 'sandip']
# # # a[0] = 3
# # # print(a)

# # # a = (1, 2, 'sandip')

# # # print(a[0])
# # # a = {1,2,3,4,55,33,66}
# # # print(a)
# # # a = 'Sandip'
# # # print(f"My name is {a}")
# # # Dictionary

# # }
# # # first_name = person['name']
# # # age = person['age']
# # # city = person['city']
# # # members = person['family_members']
# # # print(members[0:])
# # # print(f'My name is {first_name} . I am {age} years old and i live in {city}. Below are my family members\n {members[0:4]}')
# # print(f'My name is {person['name']} . I am {person['age']} years old and i live in {person['city']}. Below are my family members:\n {person['family_members']}')


# # Type casting (type conversion)
# x = 2.11
# print(int(x))

# a = [1,2,3,4,5]
# b = tuple(a)
# print(b)

# a = (1,2,3,4,5)
# b = list(a)
# b[0] = 10

# print(b)
# a = (1,2,3,4,5)
# b = set(a)
# print(b)

# a = 10
# b = 3
# print(a//b)
# print(a**2)

# a =  "Shivesh"
# b = input()
# if a==b:
#     print(a + "Madarchod ho ")
# else:
#     print(b + "Jhan thulo madarchod ho")

#  keyword : (and , or ,  not )

# name = "Sandip"
# print(name[::-1])

# a = float(input('Enter the float number: '))
# b = int(input('Enter the integer number : '))
# print(a, '\n' ,b)
# person = {
#     'name':'Sandip Malla',
#     'age': 20,
#     'city': 'Kathmandu',
#     'family_members' : ['Father', 'Mother']
# }
# print(person['family_members'][1][2])
# for i in range(10):
#     if i%2!=0:
#         print(i)

# name = 'Sandip'
# age = [1,2,3,4,]
# number = int(input("Enter the number: "))
# # result = 0
# # counter = 1
# for i in range(1,number+1):     
#     print(i)
# def person(name, age):
#     print(f"Hello {name}. Your Age is {age}")
# person(name="Sandip", age=25)
                        # *Args for accepting infinite number of arguments
# def person(*names):
#     for name in names:
#         print(f'Hello {name}')
# person('Sandip', 'Shivesh')
                        # **KeyWord Arguments(kwargs) for accepting infinite number of arguments
# def person(**details):
#     print(details['name'], details['age'])
# person(name='Sandip', age=25)
# def factorial(n=5):
#     print(n)
#     factorial(n+1)
# # factorial()
# f_name=input("Enter your Name: ")
# age=int(input('Enter your Age: '))
# address=input('Enter your Address: ')
# def person(**details):
#     print(f'My name is {details['name']}. I am {details['age']} years old. I live in {details['address']}.')
# person(name=f_name, age=age, address=address)
# s = (input('Enter the number: '))
# if s=='':
#     print("Please enter a number")
# else:
#     print(s)
# a = "san|dip"
# print(a.split('|'))
# name = [1,2,3,4,5,1,1]
# for i in  range(10):
#     names = input("Enter your friend's names: ")
#     name.append(names)
# # print('Your friends names are:', name)
                            # List methods
# name.extend([12,22,3,3,3])
# print(name)
# print(sorted(set(name)))
# print(name.insert(2,5))
# name.remove(5)
# print(name)
# print(name.count(1))
# name.reverse()
# print(name)
# def hello():
#     print(a)
#     # a=11
# hello()
# print(a)
a = 10
def changer():
    global a
    a=15
changer()
print(a)
