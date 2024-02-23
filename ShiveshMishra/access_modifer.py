class person: 
    def __init__(self,name,age,password):
       self.name='shivesh'
       self._age=age
       self.__password='hello123'
    def set_password(self,password):
        self.__password=password
    def get_password(self):
        return self.__password  

    
    password=property(get_password,set_password)    
person=person('name',24,'password')
# print(person.password)
person.name='ravi'
# person.set_password('ovaiii')
person.password="oher0"
print(person.name)
print(person._age) 
print(person.get_password())       
           
      