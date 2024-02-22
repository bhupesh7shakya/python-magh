# single inheritance
# multi level inheritance

class GrandFather:
    house= "good house"
    def __init__(self) -> None:
        self.house
        print('i am a Programmer')

class Father(GrandFather):
    car= "lambo"
    def __init__(self) -> None:
        self.car
        print('code error')
        super().__init__()

class Mother:
    jkewllery= "gold necklance"

class Son(Father, Mother):
    console="PS5"

    def __init__(self) -> None:
        print(self.console)
        super().__init__()


son=Son()
# print(son.house)


# print (isinstance(son,object))