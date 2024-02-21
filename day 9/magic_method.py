class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        # self.show()
    
    def __str__(self) -> str:
        return self.name
    
    def __eq__(self,obj):
        return self.name==obj.name
        
   
        
ram=Person('ram',12)
shyam=Person('shyam',12)
print(ram == shyam)