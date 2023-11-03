todo_list = []

try:
    with open("todo_list.txt", "r") as file:
        todo_list = file.read().splitlines()
except FileNotFoundError:
    pass  # Continue with an empty to-do list if the todo_list.txt doesn't exist

while True:
    print("To-Do List Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        task = input("Enter a new task: ")
        todo_list.append(task)
        print(f"Task '{task}' added to the to-do list.")
    elif choice == '2':
        print("To-Do List:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")
    elif choice == '3':
        if not todo_list:
            print("The to-do list is empty.")
        else:
            try:
                task_number = int(input("Enter the number of the task to remove: "))
                if 1 <= task_number <= len(todo_list):
                    removed_task = todo_list.pop(task_number - 1)
                    print(f"Task '{removed_task}' removed from the to-do list.")
                else:
                    print("Invalid task number. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    elif choice == '4':
        #Save the to-do list to the file before quitting
        with open("todo_list.txt", "w") as file:
            for task in todo_list:
                file.write(task + "\n")
        break
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
