todo_list = []
def main():
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        
        if choice == '1':
            task = input("Enter the task: ")
            todo_list.append(task)
            print("Task added successfully!")

        
        elif choice == '2':
            if not todo_list:
                print("Your list is empty.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(todo_list, 1):
                    print(f"{i}. {task}")

    
        elif choice == '3':
            if not todo_list:
                print("Nothing to update.")
            else:
                try:
                    idx = int(input("Enter task number to update: ")) - 1
                    if 0 <= idx < len(todo_list):
                        new_task = input("Enter new task: ")
                        todo_list[idx] = new_task
                        print("Task updated!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        
        elif choice == '4':
            if not todo_list:
                print("Nothing to delete.")
            else:
                try:
                    idx = int(input("Enter task number to delete: ")) - 1
                    if 0 <= idx < len(todo_list):
                        removed = todo_list.pop(idx)
                        print(f"Removed: {removed}")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
