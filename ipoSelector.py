from random import randint as r 
from random import choice
database = ['1122334455',
            '1112223330',
            '1234567890',
            '2121212121',
            '1234445566',
            '1111111111',
            '2223233333',
            '1222222222',
            '2345678907',
            '1233455666'          
            ]
num1=r(0,len(database)-1)
num2=r(0,len(database)-1)
print(f"Congrats!! demat number {database[num1]} has been alotted the IPO.")
print(f"Congrats!! demat number {database[num2]} has been alotted the IPO.")

# print(f"Congrats!! demat number {choice(database)} has been alotted the IPO.")
# print(f"Congrats!! demat number {choice(database)} has been alotted the IPO.")

