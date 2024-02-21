
#single inheritance
# multi level inheritance
class GrandFather:
    house="good house"
    
    def __init__(self) -> None:
        print(self.house)

 
class Father(GrandFather):
    car="lambo"
    
    def __init__(self) -> None:
        print(self.car)
        print('new house')
        super().__init__()

class Mother:
    jewllery="god necklance"
    

    
class Son(Father,Mother):
    console="PS5"
    
    def __init__(self) -> None:
        print(self.console)
        super().__init__()


son=Son()
# print(son.jewllery)

