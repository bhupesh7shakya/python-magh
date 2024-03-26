
todo_task = []

def add_task():
    title = input('enter title of the task: ')
    description = input('enter description about your title: ')
    status = input('enter true or false: ')
    task = {
        'title': title,
        'description': description,
        'status': status,
    }
    todo_task.append(task)
    print('task added successfully.')
    
def view_task():
    if not todo_task:
        print('no any task to show.')
    else:
        for index, task in enumerate(todo_task):
            print(f"{index}. Title: {task['title']}, Description: {task['description']}, Status: {task['status']}")

def delete_task():
    if not todo_task:
        print('No task to delete.')
    else:
        index = int(input('Enter index to delete task.'))
        if 0<=index<=len(todo_task):
            remove = todo_task.pop(index)
            print('It is deleted successfully.')
        else:
            print('Task not found.')

def main():
    global todo_task
    while True:
        print('1. Add task')
        print('2. view task')
        print('3. delete task')
        print('4. exit')
        user_choice = input('Enter your choice:')
        
        if user_choice == '1':
            add_task()
        elif user_choice == '2':
            view_task()
        elif user_choice == '3':
            delete_task()
        elif user_choice == '4':
            break
        else:
            print('select correct choice.')
                      
main()
    