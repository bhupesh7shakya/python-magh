from abc import ABC, abstractclassmethod

class Computer(ABC):
    def run(self,app):
        self.process(app)

    @abstractclassmethod
    def process(self,app):
        pass

# class Laptop(Computer):
#     def process(self,app):
#         print("Laptop is running on " + app)

# class Mobile(Computer):
#     def process(self,app):
#         print("Laptop is running on " + app)

# asus=Laptop()
# asus.run('Cricket')

# samsung=Mobile()
# samsung.run('Facebook')


class Animal(Computer):
    def process(self,app):
        print("cow give "+ app)

cow=Animal()
cow.run('milk')