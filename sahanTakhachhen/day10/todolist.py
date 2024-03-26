todos = []

def add_todo():
    title = input("Enter the title of the to-do item: ")
    description = input("Enter the description of the to-do item: ")
    todos.append({"title": title, "description": description})

def display_todos():
    for i, todo in enumerate(todos, start=1):
        print(f"{i}. {todo['title']} : {todo['description']}")

while True:
    print("\n1. Add a to-do item")
    print("2. Display all to-do items")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_todo()
    elif choice == '2':
        display_todos()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")
