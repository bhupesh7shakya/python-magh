#                         # imheritance and Method overriding

# class Baje:
#     bunglow = "52 acre ko jagga ko bunglow xa."
#     def __init__(self):
#         print("Ma baje ho.")
# class Bau(Baje):
#     car = "Tesla xa hai kta ho"
#     def __init__(self):
#         print("Ma tero bau ho.")
# class Xora(Bau):
#     sampati = "Ma sanga sab xa hi hahahaha"
#     # def __init__(self):
#     #     print("Ma ma  ho.")
# # Object create garda init auto run vayo ani sabai init overriding gardai ayo.
# xora = Xora()  
# print(xora.car)


            # access modifier _ 'Protected' [within a file]   __ 'Private' [within a class]
class Person:
    def  __init__(self, name, age, password):
        self.name = name
        self._age = age
        self.__password = password
    @property
    def password(self):
        return  self.__password
    @password.setter
    def password(self, password):
            self.__password = password

person = Person('Sandip', 25, 'sandip123')
print(person.password)
person.password="arko password"
print(person.password)