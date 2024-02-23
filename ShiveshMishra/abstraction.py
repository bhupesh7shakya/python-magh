from abc import ABC,abstractmethod
class Computer(ABC):
    def run(self,app):
        self.process(app)
    @abstractmethod
    def process(self,app):
        pass        
class Laptop(Computer):
    def process(Self,app):
        print("laptop is running on" +app)
class Mobile(Computer): 
    def process(Self,app):
        print("Mobile is runnin on" +app)
acer=Laptop()
acer.run('pubg') 
samsung=Mobile()
samsung.run('chrome')
