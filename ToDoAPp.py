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
print("3:update a task")
print("4:delete the task")
User_choice = int(input("enter your choice"))

os.system("cls" if os.name == "nt" else "clear")


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


New_account()
