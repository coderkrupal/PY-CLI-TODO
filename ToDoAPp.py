import pyfiglet
import csv
import os


def print_banner():
    banner_text = "Modern To Do App"
    ascii_banner = pyfiglet.figlet_format(banner_text)
    print(ascii_banner)


if __name__ == "__main__":
    print_banner()


print("1:create a new account")
print("2:create a new task")
print("3:delete the task")
User_choice = int(input("enter your choice"))

os.system("cls" if os.name == "nt" else "clear")


def Create_NewTasl():
    print("--------------Enter your Task-----------------------")
    task = str(input())
    Newtask = [[task]]
    with open("alltask.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(Newtask)
        os.system("cls" if os.name == "nt" else "clear")
    print("---------------------Task successfully add -----------------")

    os.system("cls" if os.name == "nt" else "clear")

def display_alltask():
    try:
       with open("alltask.csv", mode="r") as file:
           reader = csv.reader(file)
           tasks = list(reader)
           if not tasks:
               print("No tasks found!")
               return[]
           print("your tasks:")
           for i,task in enumerate(tasks,start=1):
               print(f"{i}.{task[0]}")
               
        
           return tasks
    except FileNotFoundError:
        print("No tasks file found!")
        return []


# Function to delete a task
def delete_task(task_number):
    tasks = display_alltask()
    if not tasks:
        return
    
    if 1 <= task_number <= len(tasks):
        del tasks[task_number - 1]  # Remove the selected task
        with open("alltask.csv", mode="w", newline="") as file:  # Overwrite file
            writer = csv.writer(file)
            writer.writerows(tasks)  # Write back remaining tasks
        print("Task deleted successfully!")
    else:
        print("Invalid task number!")

if User_choice == 3:

    def Delete_task():
       
        print("plase use (GO..) for show all the task")
        Back_func =  str(input(""))
        if(Back_func == "GO.."):
            display_alltask() 
        print("enter a task you want to delete")
        user_delete = int(input(""))
      
        delete_task(user_delete)
Delete_task()


def New_account():
    print("enter username")
    userName = str(input(""))
    print("enter email")
    email = str(input(""))
    print("enter age")
    age = int(input(""))
    print("enter password")
    password = str(input(""))

    data = [
        [userName, email, age, password],
    ]
    with open("data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)
    os.system("cls" if os.name == "nt" else "clear")
    print("---------------------accout is successfully creates-----------------")

    def Validate_user():
        print("Enter username for log in:")
        entered_username = input().strip()  # Username input first
        print("Enter password:")
        entered_password = input().strip()  # Password input second

        with open("data.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            users = list(reader)
            for row in users:
                if len(row) < 4:
                    continue
            stored_username, _, _, stored_password = (
                row  # Extract username and password
            )
            if (
                entered_username == stored_username
                and entered_password == stored_password
            ):
                print("✅ Login successful! Welcome,", entered_username)

            else:
                print("❌ Invalid username or password. Please try again.")
                Validate_user()

    Validate_user()
    Create_NewTasl()


if User_choice == 1:
    New_account()
