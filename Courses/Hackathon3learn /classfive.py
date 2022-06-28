import requests  # another default python library that has functions that handle http/url things

url = "https://api.airtable.com/v0/appeekE2Z1dwHurFW/Tasks/"  # like a username
headers = {"Authorization": "Bearer keyWSDE6so5IkTl4B"}  # like a password

def add_task(): # using functions to make code easier to read and more organized
  print("What is the name of the task you want to add?")
  name = input()
  body = { # this is a dictionary, which is just a special way of holding information, it includes key-value pairs
    "records": [
      {
        "fields": {
          "Name": name
        }
      }
    ]
  }
  # the airtable api documentation says to use post
  requests.post(url, headers=headers, json=body)
  print("Task added!")

def remove_task():
  tasks = requests.get(url, headers=headers).json()['records']
  if(len(tasks) == 0): # make sure there are existing tasks
    print("There are no tasks to remove")
    return # this makes the program leave this function, and it then goes back to the while loop
  print("What is the name of the task you want to be removed?")
  name = input()
  id = "" # we need to find the id of the task that we are trying to delete
  for task in tasks:
    if task['fields']['Name'] == name:
      id = task["id"]
      break # this keyword makes the program exit out of the for loop
  if id == "":
    print("Task not found")
  body = {
    "records[]": id
  }
  requests.delete(url, headers=headers, params=body)
  print("Task deleted!")
      

def list_tasks():
  tasks = requests.get(url, headers=headers).json()['records']
  # print(tasks) # you can use print statements to figure out what something looks like, in this case, what is contained in the json that is returned by airtable
  if(len(tasks) == 0):
    print("There are no tasks")
    return
    # you can use while or for loops
  # i = 0
  # while i < len(tasks):
  #   name = tasks[i]['fields']['Name']
  #   print("- " + name)
    # print(tasks[i])
    # i = i + 1
  for task in tasks:
    name = task['fields']['Name']
    print("- " + name)

while True: # this will continue forever unless a keywork like break is used
  print("Enter 1 to add a task to your To-Do list")
  print("Enter 2 to remove a task from your To-Do list")
  print("Enter 3 to list of the tasks in your To-Do list")
  print("Enter 4 to end this loop")
  
  option = int(input())

  if option < 1 or option > 4:
    print("Please enter either 1, 2, 3, or 4")
    continue # this makes the program ignore the next lines that are part of the while loop and it continues back at the beginning of the loop

  if option == 1:
    add_task()

  if option == 2:
    remove_task()

  if option == 3:
    list_tasks()

  if option == 4:
    break # this makes the while loop end
