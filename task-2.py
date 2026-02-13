todo_tasks = []

while True:
    print("\n===== TODO MENU =====")
    print("1. Add Task")
    print("2. View Specific Task")
    print("3. View All Tasks")
    print("4. Delete Task")
    print("5. Exit")

    try:
        ch = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Add Task
    if ch == 1:
        task = input("Enter task to add: ").strip()
        if task:
            todo_tasks.append(task)
            print("Task added successfully!")
        else:
            print("Task cannot be empty.")

    # View Specific Task
    elif ch == 2:
        task = input("Enter task to search: ").strip()
        if task in todo_tasks:
            print("Task found:", task)
        else:
            print("Task not found.")

    # View All Tasks
    elif ch == 3:
        if not todo_tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(todo_tasks, start=1):
                print(f"{i}. {t}")

    # Delete Task
    elif ch == 4:
        if not todo_tasks:
            print("No tasks to delete.")
        else:
            for i, t in enumerate(todo_tasks, start=1):
                print(f"{i}. {t}")

            try:
                index = int(input("Enter task number to delete: ")) - 1
                if 0 <= index < len(todo_tasks):
                    removed = todo_tasks.pop(index)
                    print("Removed:", removed)
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Enter a valid number.")

    # Exit
    elif ch == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice.")






