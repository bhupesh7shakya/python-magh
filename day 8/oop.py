# # class House:
# #     window=10
# #     color="red"
# #     door=1
    
# #     def set_window(self,window):
# #         self.window = window
        
# #     def get_window(self):
# #         return self.window
    
# # ram_ko_ghar=House()

# # # ram_ko_ghar.set_window(11)
# # # print(ram_ko_ghar.get_window())
# # hari_ko_ghar=House()


# class Burger:
    
#     def bun(self):
#         print('bun')
#         return self
#     def cheese(self):
#         print('cheese')
#         return self
#     def patty(self):
#         print('patty')
#         return self
    
# burger=Burger()

# burger.bun().cheese().patty().bun()


database=[
    {
        'name':'ram',
        'password':'<PASSWORD>'
    },
    {
        'name':'hari',
        'password':'<PASSWORD>'
    }
]
print(database)

for i in range(2):
    name=input('name')
    password=input('password')


    user={
        'name':name,
        'password':password
    }

    database.append(user)
    
print(database)