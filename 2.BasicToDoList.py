# Python program for BasicToDoList Application.
def add_tasks(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print(f'Task added successfully!')


def display_tasks(tasks):
    if tasks:
        print("\n--- ToDo List ---")
        for i, task in enumerate(tasks,start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{i}. {task['task']} - {status}")
    else:
        print("No tasks available.")
   

def mark_task_completed(tasks):
    display_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("Enter the task number to mark as completed: "))
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]["completed"] = True
                print(f'Task mark as completed!')
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    tasks = []
    while True:
        print("\n--- Basic To-Do List ---")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_tasks(tasks)
        elif choice == "2":
            mark_task_completed(tasks)
        elif choice == "3":
            display_tasks(tasks)
        elif choice == "4":
            print("Exiting the ToDo List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__=="__main__":
    main()

