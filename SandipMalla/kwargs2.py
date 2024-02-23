f_name=input("Enter your Name: ")
age=int(input('Enter your Age: '))
address=input('Enter your Address: ')
def person(**details):
    print(f'My name is {details['name']}. I am {details['age']} years old. I live in {details['address']}.')
person(name=f_name, age=age, address=address)
