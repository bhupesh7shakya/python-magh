# class Person:
#     def __init__(self) -> None:
#         print('Mero name is Sandip Malla')
#         self.show()
#     def show(self):
#         print("Show method is running")
# Person()

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self) -> str:
        return self.name
    def __eq__(self,obj) -> bool:
        return self.age==obj.age
    def __ne__(self, obj) -> bool:
        return self.age!= obj.age
ram = Person('ram', 12)
shyam = Person('shyam',12)
print(ram!=shyam)