# class House:
#     def __init__(self):
#         print('Hello World')
#         self.show()


#     def show(self):
#         print("show")

# House().show()



class Person():
    def __init__(self,name,age):
        self.age= age
        self.name= name


    def __str__(self) -> str:
        return self.name
    
    def __eq__(self,obj):
        return self.name==obj.name
    
    def __ne__(self,obj):
        return self.age!= obj.age
    
ram=Person('ram',22)
shyam=Person('shyam',23)
bharat=Person('bharat',22)
print(ram==shyam, ram!=bharat)