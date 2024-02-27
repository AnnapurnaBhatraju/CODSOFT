import os

def display_menu():
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Quit")

def view_todo_list():
    with open("todo.txt", "r") as file:
        tasks = file.readlines()
        if tasks:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task.strip()}")
        else:
            print("Your to-do list is empty.")

def add_task():
    task = input("Enter the task: ")
    with open("todo.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully.")

def update_task():
    view_todo_list()
    try:
        task_number = int(input("Enter the task number to update: "))
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
        if 1 <= task_number <= len(tasks):
            new_task = input("Enter the new task: ")
            tasks[task_number - 1] = new_task + "\n"
            with open("todo.txt", "w") as file:
                file.writelines(tasks)
            print("Task updated successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            view_todo_list()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    if not os.path.exists("todo.txt"):
        with open("todo.txt", "w"):
            pass
    main()
