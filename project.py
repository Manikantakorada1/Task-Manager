def main():
    tasks = []
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Remove Task")
        print("4. List Tasks")
        print("5. Exit")
        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            task = input("Enter task description: ")
            add_task(tasks, task)
        elif choice == 2:
            if tasks:
                print("Current tasks:")
                list_tasks(tasks)
                task_index = int(input("Enter task sl.no to complete: "))
                task_index -= 1
                complete_task(tasks, task_index)
            else:
                print("No tasks to complete.")
        elif choice == 3:
            if tasks:
                print("Current tasks: ")
                list_tasks(tasks)
                task_index = int(input("Enter task sl.no to remove: "))
                task_index -= 1
                remove_task(tasks, task_index)
            else:
                print("No tasks to remove.")
        elif choice == 4:
            if tasks:
                print("Current tasks: ")
                list_tasks(tasks)
            else:
                print("No tasks.")
        elif choice == 5:
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

def add_task(task_list, task):
    task_list.append({"task": task, "completed": False})
    print(f"Task '{task}' added.")

def complete_task(task_list, task_index):
    if task_index >= 0 and task_index < len(task_list):
        task_list[task_index]["completed"] = True
        print(f"Task '{task_list[task_index]['task']}' marked as completed.")
    else:
        print("Invalid task sl.no.")

def remove_task(task_list, task_index):
    if task_index >= 0 and task_index < len(task_list):
        del task_list[task_index]
        print("Task removed.")
    else:
        print("Invalid task sl.no")

def list_tasks(task_list):
    for index, task in enumerate(task_list):
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"{index+1}. {task['task']} - {status}")


if __name__ == "__main__":
    main()
