import os

filename = "list.txt"

while True:
    print("\nThis is Your To Do List")
    print("1. See list")
    print("2. Change list")
    print("3. Clear list")
    print("4. Exit")

    try:
        a = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number.")
        continue

    if a == 1:
        # See list
        if os.path.exists(filename):
            with open(filename, "r") as f:
                content = f.read()
                if content.strip():
                    print("\nYour tasks:")
                    print(content.strip())
                else:
                    print("No tasks yet.")
        else:
            print("No tasks yet.")

    elif a == 2:
        # Change list
        print("What do you want to change?")
        print("1. Remove a task")
        print("2. Add new to-do")

        try:
            x = int(input("Enter choice: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if x == 1:
            # Remove a task
            if not os.path.exists(filename):
                print("No tasks to remove.")
            else:
                with open(filename, "r") as f:
                    lines = f.readlines()

                if not lines:
                    print("No tasks to remove.")
                else:
                    print("\nTasks:")
                    for i, line in enumerate(lines, 1):
                        print(f"{i}. {line.strip()}")

                    try:
                        choice = int(input("Enter task number to remove: ")) - 1
                        if 0 <= choice < len(lines):
                            lines.pop(choice)
                            with open(filename, "w") as f:
                                f.writelines(lines)
                            print("Task removed.")
                        else:
                            print("Invalid number.")
                    except ValueError:
                        print("Please enter a number.")

        elif x == 2:
            # Add new to-do
            task = input("Enter what you want to do: ").strip()
            if task:
                with open(filename, "a") as f:
                    f.write(task + "\n")
                print("Task added.")
            else:
                print("Task cannot be empty.")

        else:
            print("Invalid choice.")

    elif a == 3:
        # Delete list
        x = input("Do you want to delete the whole list? [y/n]: ").strip().lower()
        if x == "y":
            with open(filename, "w") as f:
                pass  # clears the file
            print("List cleared.")
        elif x == "n":
            print("Cancelled.")
        else:
            print("Invalid choice.")

    elif a == 4:
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
