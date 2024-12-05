to_do_list = []
def start():
        choice = int(input("Enter your choice as follow\n1.Add task\n2.Delete Task\n3.View Taks"))
        if choice == 1:
            addTask()
        elif choice == 2:
            RemoveTask()
        elif choice == 3:
            DisplayTask()
        else:
            print("\nInvalid Input\n")
            exit(1)
            
def addTask():
    
        task = input("\nEnter the task to store in To Do List\n")
        to_do_list.append(task)
        
        next_task = input("\nDo you want to add new task in the list? (Y/N): ")
        if next_task.lower() == 'y':
            addTask()
        else:
            start()
        
def RemoveTask():
       if not to_do_list:
           print("\nThe To do list is empty\n Back to Menu")
           start()

       else:
           index = int(input("\nenter the index to be deleted\n"))
           if index not in range(1,len(to_do_list)+1):
               
               print("\nindex out of range\n")
               start()
           else:
               to_do_list.pop(index-1)
               print("\nThe new to do list is as follow\n")
               for task in to_do_list:
                   print(task)

    
def DisplayTask():
    if not to_do_list:
        print("\nThe To do list is empty\n back to menu")
        start()
    else:
        print("\nThe to do list added are as follow\n")
    for i in to_do_list:
        print(i)

start()

print(f"\nThe length of the list is\t {len(to_do_list)}")






