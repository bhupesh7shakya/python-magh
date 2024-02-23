class GrandFather:
   house = "good house"
   def __init__(self):
       self.house
       print('hello budy i am grandFather')
class father(GrandFather):
    car='lambo'
    # def __init__(self):
    #       self.car
    #       print('hello i am father')
class mother:
    jewllery="god necklance"
    # def __init__(self):
    #     self.jewllery
    #     print('i am mother')
class son(father,mother):
    console="ps5"
    def __init__(self):
        print(self.console)
        print('new ghar')
        super().__init__()
    #     print('i am son')
Son=son()
print(son.car) 
