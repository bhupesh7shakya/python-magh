import os
def load_todos():
    if os.path.exists('todos.txt'):
        with open('todos.txt', 'r') as f:
            lines = f.readlines()
            return [eval(line.strip()) for line in lines]
    else:
        return []

def save_todos(todos):
    with open('todos.txt', 'w') as f:
        for todo in todos:
            f.write(str(todo) + '\n')

def add_todo(todos):
    title = input("Enter the title of the to-do item: ")
    description = input("Enter the description of the to-do item: ")
    status = input("Enter the status of the to-do item: ")
    todos.append({"title": title, "description": description, "status": status})

def update_todo(todos):
    display_todos(todos)
    index = int(input("Enter the number of the to-do item you want to update: ")) - 1
    if index < 0 or index >= len(todos):
        print("Invalid number. Please try again.")
        return
    title = input("Enter the new title of the to-do item: ")
    description = input("Enter the new description of the to-do item: ")
    status = input("Enter the new status of the to-do item: ")
    todos[index] = {"title": title, "description": description, "status": status}

def delete_todo(todos):
    display_todos(todos)
    index = int(input("Enter the number of the to-do item you want to delete: ")) - 1
    if index < 0 or index >= len(todos):
        print("Invalid number. Please try again.")
        return
    del todos[index]

def display_todos(todos):
    for i, todo in enumerate(todos, start=1):
        print(f"{i}. {todo['title']} : {todo['description']} : git{todo['status']}")

def main():
    todos = load_todos()
    while True:
        print("\n1. Add a to-do item")
        print("2. Update a to-do item")
        print("3. Delete a to-do item")
        print("4. Display all to-do items")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_todo(todos)
            save_todos(todos)
        elif choice == '2':
            update_todo(todos)
            save_todos(todos)
        elif choice == '3':
            delete_todo(todos)
            save_todos(todos)
        elif choice == '4':
            display_todos(todos)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
