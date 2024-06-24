# def todos(todo):
#     todosItem = []
#     # print(type(todosItem))
#     def addTodos(todo):
#         pass


# todos(input("enter your todo item"))


# todolist = []
# def todos(num):
#     if num == 1:
#             AddTodo()

#     elif num == 2:
#             RemoveTodo()


# def AddTodo():
#      todo = input("enter your todos : ")
#     #  print(todo)
#      todolist.append(todo)
#      userAns = input("would you like to add more:    yes or no : ")
#      if (userAns.lower() == "yes"):
#            AddTodo()
#      else:
#       print(f"your todos list are : ", todolist)


# def RemoveTodo():
#       mytodos = ['going to meeting','going to college','bring cake']
#       print(mytodos)
#       indexOfTodo = int(input("enter the index of the todo item to be removed : "))
#       if(indexOfTodo.isnumeric):
#             mytodos.pop(indexOfTodo)
#             print(f"mytodos after removing todo at index {indexOfTodo} : {mytodos}")

#       else:
#             print('you have entered non integer values: ')

# todos(int(input("what you want to do Add or remove 1 for add and 2 for remove : ")))


# second method

todolist = []
def todos(num):
    if num == 1:
        AddTodo()

    elif num == 2:
        RemoveTodo()

def AddTodo():
    todo = input("enter your todos : ")
    #  print(todo)

    todolist.append(todo)
    
    userAns = input("would you like to add more:    yes or no : ")
    if (userAns.lower() == "yes"):
         AddTodo()
    else:
      print(f"your todos list are : ", todolist)
      removeQuery = input("want to remove your todos  yes or no  : ")
      if(removeQuery.lower() == "yes"):
          RemoveTodo()
      else:
          print("thank you ")

def RemoveTodo():
    print("*"*10)
    print(todolist)
    indexOfTodo = int(input("enter the index of the todo item to be removed : "))
    todolist.pop(indexOfTodo)
    print(f"mytodos after removing todo at index {indexOfTodo} : {todolist}")



# function calling with the user input queries
todos(int(input("what you want to do Add or remove 1 for add and 2 for remove : ")))
