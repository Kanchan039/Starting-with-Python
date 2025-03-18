#Simple To-Do List App

todo_list=[]

def show_menu():
    print("\n------TO-DO LIST------\n")
    print("1. Add task")
    print("2. Mark task as done")
    print("3. View task")
    print("4. Delete Task")
    print("5. Exit")

def view_task():
    if not todo_list:
        print("\nNo tasks in the list.")
    else:
        print("\nYour Tasks.")
        for index, task in enumerate(todo_list,start=1):
            status ="Done" if task['completed'] else "Not Done"
            print(f"{index}.{task['task']}[{status}]")

def add_task():
    task_name=input("Enter the Task:")
    todo_list.append({'task':task_name,'completed':False})
    print("Task added successfully!")

def complete_task():
    view_task()
    try:
        task_num=int(input("Enter task number to mark as completed:"))
        if 1<=task_num<=len(todo_list):
            todo_list[task_num-1]['completed']=True
            print("Task marked as completed!")
        else:
            print("Invalid Task Number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        
def delete_task():
    view_task()
    try:
        task_num = int(input("Enter the task number to delete:"))
        if 1 <= task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)
            print(f"Task '{removed_task['task']}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
        
while True:
    show_menu()
    choice=input("Choose an option (1-5):")

    if choice=='1':
        add_task()
    elif choice=='2':
        complete_task()
    elif choice=='3':
        view_task()
    elif choice=='4':
        delete_task()
    elif choice=='5':
        print("Thank you for using To Do List App.")
        break
    else:
        print("Invalid Choice. please select a valid option.")