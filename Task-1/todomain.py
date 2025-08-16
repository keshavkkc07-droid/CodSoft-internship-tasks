
todo_list=[]

def add_task():
    task=input("Enter your task : ")
    todo_list.append(f"{task} : [❌ Not Done] ")
    print("✅ Task added!")

def mark_done():
    i=0
    for list in todo_list:
        print(f"{i+1}.{list}")
        i+=1
    
    md=int(input("Enter task number to mark as done (one choice at a time): "))

    if ": [❌ Not Done]" in todo_list[md-1] :
        todo_list[md-1]=todo_list[md-1].replace(": [❌ Not Done]"," : [✅ done]")

    elif ': [✅ done]' in todo_list[md-1] :
        print("Task already compleated 😉")



def delete_task():

    i=0
    for list in todo_list:
        print(f"{i+1}.{list}")
        i+=1
    
    md=int(input("Enter task number to Delete (one choice at a time): "))
    todo_list.pop(md-1)


    print()

def show_task():
    i=0
    for list in todo_list:
        print(f"{i+1}.{list}")
        i+=1





while True:
    print(
        '''📋 To-Do List Menu:
1. Show Tasks
2. Add Task
3. Mark Task as Done
4. Delete Task
5. Exit'''
    )
    opt=input(" Enter your choice (1-5):")
    if opt=='1':
        show_task()

    elif opt=='2':
        add_task()
    
    elif opt=='3':
        mark_done()
        
    elif opt=='4':
        delete_task()
    elif opt=='5':
        break
    else:
        print("Invalid choice")

    


