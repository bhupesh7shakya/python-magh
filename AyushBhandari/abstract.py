from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def behavior(self):
        pass

class Aayush(Person):
    def behavior(self):
        return "OOO"

class Aayusha(Person):
    def behavior(self):
        return "PPP"

aayush = Aayush()
aayusha = Aayusha()

print(aayush.behavior())
print(aayusha.behavior())

