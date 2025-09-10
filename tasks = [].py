tasks = []

def view_tasks(tasks):
    if not tasks:
        print("The task list is empty")
    else:
        print(f'\n Your tasks: ')
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
  task_description = input("What task would you like to add?: ")
  tasks.append(task_description)
  with open("tasks.txt", "a") as file: 
   file.write(task_description + '\n')

def load_file():
  with open(tasks.txt, 'r') as file:
   content = file.read()
   return([task for task in content.split('\n') if task.strip()])

def delete_task(tasks):
  task_to_delete = (input("Which task would you like to delete?: "))
  if task_to_delete in tasks:
   tasks.remove(task_to_delete)
   print("Task deleted")
  else:
   print(f"Task not deleted, please check your spelling, here are the available tasks: \n {tasks} ")



while True: 
 print("Menu: \n add \n load \n view \n delete \n exit")
 user_choice = input("How can I help you?: ")
 print(f"You typed: '{user_choice}' and after lower: '{user_choice.lower()}'")
 if user_choice.lower() == 'add':
   add_task(tasks)
 elif user_choice.lower() == 'load':
   tasks = load_file()
 elif user_choice.lower() == 'view':
  view_tasks(tasks)
 elif user_choice.lower() == 'delete': 
   delete_task(tasks)
 elif user_choice.lower() == 'exit':
  break