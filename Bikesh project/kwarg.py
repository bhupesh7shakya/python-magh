f_name= input("Your Name:")
age= int(input("Your Age:"))
address= input("Your Address:")
def person(**details):
    print(f'my name is {details['Name']}. I am {details['age']} yeras old. I live in {details['address']}.')
person(Name= f_name, age= age, address=address)