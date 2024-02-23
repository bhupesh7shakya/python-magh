class Person:
    def __init__(self, name,age,password) -> None:
        self.name= name
        self._age= age
        self.__password= password

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self,password):
        self.__password=password

    # def set_password(self,password):
    #     self.__password=password

    # def get_password(self):
    #     return self.__password
    
    # __password= property(get_password,set_password)

Person=Person('name',12,'password')

# print(Person.name)
# print(Person._age)
# print(Person.__password)

print(Person.name)
print(Person._age)
print(Person.password)