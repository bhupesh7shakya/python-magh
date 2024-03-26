# Homework(CRUD):-
# 1.make todo list
# 2.must take user input(title & desc). [title & desc must be store in a dictionary]
# 3.store it in global database.
# 4.tya store vako sapai data herna milna paryo.
# 5.insert new data
# 6.delete data


# eval and str converts string back to list
# todo_task = [] is a global variable accessible to all{list,tuple j rakheni    hunxa}
# enumerate changes list to tuple

todo_task = []

# it will add task to our todo list in the form of dictionary
def add_task():
    title = input('Enter task title: ')
    desc = input('Enter task description: ')
    stat = bool(input('Write status!: '))
    task = {
        'title': title, 
        'description': desc,
        'status': stat,
        }

    todo_task.append(task)
    print('\n------Task Added Successfully------\n')
    
# for viewing todo_task    
def view():
    if not todo_task:
        print("No any tasks to show.\n")
    else:
        print('\n-----Tasks:-----')
        for index, task in enumerate(todo_task):
            print(f"{index}. Title: {task['title']}, Description: {task['description']}, Status: {task['status']}\n")
 
# for deleting todo_task                    
def delete():  
    # global todo_task  
    if not todo_task:
        print('No tasks to delete.\n')
    else:
        view()
        index = int(input('\nEnter index task you want to delete: '))
        if 0 <= index <= len(todo_task):
            remove = todo_task.pop(index)
            print(f'Task deleted successfully.\n')
        else:
            print("Task index not found.\n")

# load_task() will load the saved task
def load():
    global todo_task
    try:
        # with open(filename, 'r') as file:
        # file_content = file.read()
        file = open('todo_task.txt', 'r')
        todo_task = eval(file.read())
        
    except FileNotFoundError:
        todo_task = []

# it will save all tasks we add
def save():
    file = open('todo_task.txt', "w")
    file.write(str(todo_task))

def main():    
    global todo_task
    load()
    while True:     
        print('\nThis is TODO-LIST')
        
        print('1. Add Task: ')
        print('2. View Task: ')
        print('3. Delete Task: ')
        print('4. Save & Exit: ')
        
        user = input('\nEnter your choice: ')
        
        if user == '1':
            add_task()
        elif user == '2':
            view()
        elif user == '3':
            delete()
        elif user == '4':
            save()
            break
        else:
            print("Invalid choice!!! Select correct choice and run again.\n")
            break

main()