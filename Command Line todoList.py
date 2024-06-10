tasks = []


def list_tasks():
    if not tasks:
        print("No tasks currently their!")
    else:
        for index, task in enumerate(tasks, start=1):
            print(index, task)
            
def add_task():
    task_to_be_added = input("Enter task: ")
    tasks.append(task_to_be_added);
    print(f"Task '{task_to_be_added}' successfully added!")
    

def delete_task():
    list_tasks()
    try:
        task_to_be_deleted = int(input("Enter task no.: "))
        task_to_be_deleted -= 1
        if task_to_be_deleted >= 0 and task_to_be_deleted < len(tasks):
            
            tasks.pop(task_to_be_deleted)
            print(f"Task '{task_to_be_deleted}' was successfully deleted.")
    except:
        print("Invalid input!")
        
choice = 0
while True:
    print("\n")
    print("Enter choice: ")
    print("1.Add a task")
    print("2.delete a task")
    print("3.list all task")
    print("4.quit")
    
    try:
        choice = int(input("Enter your choice: "))
    except:
        print("Invalid input!")
    
    match choice:
        case 1:
            add_task()
        case 2:
            delete_task()
        case 3:
            list_tasks()
        case 4:
            print("Exit!")
            break
        case _:
            print("Invalid input try again!")
        