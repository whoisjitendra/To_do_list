# Take a list variable
tasks = []

# Define an empty list to store tasks
tasks = []

while True:
    print("Please choose the option to to continue the operation->")
    print("1-> Add a task \n2-> View tasks \n3-> Remove a task \n4-> Exit")
    
    
   

    choice = input("Enter your choice given given above option-> ")
# To add the task
    if choice == '1':
        task = input("Enter a task: ")
        tasks.append(task)
        print(f"Task '{task}' added to the to-do list.")
# To view the task        
    elif choice == '2':
        if tasks:
            print("To-Do List:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks in the to-do list.")
# To remove the task    
    elif choice == '3':
        if tasks:
            view_tasks = "\n".join([f"{i}. {task}" for i, task in enumerate(tasks, 1)])
            print("To-Do List:")
            print(view_tasks)
            try:
                task_number = int(input("Enter the number of the task to remove: ")) - 1
                if 0 <= task_number < len(tasks):
                    removed_task = tasks.pop(task_number)
                    print(f"Task '{removed_task}' removed from the to-do list.")
                else:
                    print("Invalid task number. Please enter a valid task number.")
            except ValueError:
                print("Invalid input. Please enter a valid task number.")
        else:
            print("No tasks in the to-do list.")
# To exit the loop            
    elif choice == '4':
        break
    else:
        print("Please choose the correct option to continue the operation:")

print("Thank-you")




