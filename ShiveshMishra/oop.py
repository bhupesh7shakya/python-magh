# class house:
#     window=10
#     color="red"
#     door=2
#     def set_window(self,window):
#         self.window=window
#     def get_window(self):
#         return self.window
# ram_vai_ko_ghar=house()
# ram_vai_ko_ghar.set_window(11)
# print(ram_vai_ko_ghar.get_window())
# print(ram_vai_ko_ghar.door)
# # hari_jimu_ko_ghar=house()
# # print(hari_jimu_ko_ghar.color)


class pizza:
    def peetho(self):
        print('peetho')
        return self
    def stone(self):
        print('stone')
        return self
    def chicken(self):
        print('chicken')
        return self
pizza=pizza()
pizza.peetho().stone().chicken() 