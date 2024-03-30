def main():
    todo_list = []

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Clear Completed Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(todo_list)
        elif choice == '2':
            view_tasks(todo_list)
        elif choice == '3':
            mark_completed(todo_list)
        elif choice == '4':
            clear_completed(todo_list)
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

def add_task(todo_list):
    task = input("Enter the task: ")
    todo_list.append({"task": task, "completed": False})
    print("Task added successfully.")

def view_tasks(todo_list):
    print("\n===== To-Do List =====")
    for index, task in enumerate(todo_list, start=1):
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"{index}. {task['task']} - {status}")

def mark_completed(todo_list):
    view_tasks(todo_list)
    task_index = int(input("Enter the index of the task to mark as completed: ")) - 1
    if 0 <= task_index < len(todo_list):
        todo_list[task_index]["completed"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task index.")

def clear_completed(todo_list):
    for task in todo_list[:]:
        if task["completed"]:
            todo_list.remove(task)
    print("Completed tasks cleared.")

if __name__ == "__main__":
    main()
