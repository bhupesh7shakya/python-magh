# class House:
#     window=10
#     color='red'
#     door = 1
#     def set_window(self, window):
#         self.window = window
#     def get_window(self):
#         return self.window
# ram_house  = House()
# ram_house.set_window(15)
# print(ram_house.get_window())

class Sandwich:
    def bread(self):
        print('bread')
        return self
    def meat(self):
        print('meat')
        return self
    def cheese(self):
        print('cheese')
        return self
sandwich = Sandwich()
# Method chaining
sandwich.bread().meat().cheese().bread() 
print('Your Sandwich is a ready')
