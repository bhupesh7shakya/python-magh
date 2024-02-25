f_name=input("Enter your Name: ")
age=int(input('Enter your Age: '))
address=input('Enter your Address: ')
def person(**details):
    print(f'My name is {details['name']}. I am {details['age']} years old. I live in {details['address']}.')
person(name=f_name, age=age, address=address)
def sum(*nums):
    total=0
    for i in range(len(nums)):
       for num in nums[i]:
            total+=num
    return total


print(sum([1,2,3],[4,5,6]))  

