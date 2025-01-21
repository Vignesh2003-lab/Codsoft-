tasks =[]
def add_task():
    task=input("Enter a new task:")
    tasks.append(task)
    print("Task added succefully:")


def view_task():
    if len(tasks)==0:
        print("no tasks")
    else:
        print("list of tasks:")
        for i,task in enumerate(tasks,start=1):
            print(f'{i}.{task}')


def delete_task():
    if len(tasks)==0:
        print("no task to delete.")
    else:
        print("Tasks:")
        for i,task in enumerate(tasks,start=1):
            print(f'{i}.{task}')
        choice=int(input("Enter the task number to delete:"))
    if 0<choice <= len(tasks):
        del tasks[choice-1]
        print("Task deleted successfully.")
    else:
        print("Invaild task number.")


def main():
    while True:
        print('\n****** TO-DO-LIST Application ********')
        print("1.Add task")
        print("2. View task")
        print("3.Delete task")
        print("4.Quit")

        choice= int(input("enter the choice:"))
        if choice ==1:
            add_task()
        elif choice ==2:
            view_task()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            print("Thank you for using the To-Do-List Application.")
            break
        else:
            print("Invalid choice.please try again")
if __name__=="__main__":
    main()
