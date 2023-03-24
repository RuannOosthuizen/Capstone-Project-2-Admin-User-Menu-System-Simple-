#=====importing libraries===========
# Here I am importing the current date at any time.
# Reference : https://www.programiz.com/python-programming/datetime/current-datetime#
# Reference: https://www.geeksforgeeks.org/get-current-date-using-python/
from datetime import date

#=====Login Section=====
# Here I am defining empty lists for where the usernames and passowrds will be stored in.
username_list = []
password_list = []

# This section I use the for loop to seperate the username and the password for each line in the text file. Then store that in the appropriate list.
with open("user.txt", "r") as login:
    for line in login:
        temp = line.strip()
        temp = temp.split(", ")

        username_list.append(temp[0])
        password_list.append(temp[1])

# Here I ask the user for their username and passowrd and store that in their appropriate variables.
user_login_name = input("To login please enter your username : ")
user_login_password = input("Please enter your password : ")

# Then I use the while loop to check if the user exist or has typed their credentails incorrectly and respond appropreately.
while user_login_name not in username_list or user_login_password not in password_list:
    print("The user name or passowrd you typed in is incorrect or does'nt exist, Please try again.")
    user_login_name = input("Please enter your username : ")
    user_login_password = input("Please enter your passowrd : ")

print(f"login successful! Welcom {user_login_name}!")

#=====Option Selection Menu Section=====

while True:
    # Then presenting the user the menu after a successful login and
    # making sure that the user input is coneverted to lower case.
    # This if statement determines if the user logged in is the admin or not, if so they have a different menu as well as more options they allow have access to.
    if user_login_name == "admin":
        menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    s - statistics
    e - Exit
: ''').lower()

        # If the user selected "r" they can then input the username and password of the new user as well as to confirm the new users password.
        if menu == 'r':
            # The use is prompted to input the new users details.
            new_username = input("Please enter the new username : ")
            new_password = input("Please enter the password for this user : ")
            confirm_pass = input("please confirm passowrd : ")
            # The program will also check to see if they have entered the password correctly or not.
            if new_password != confirm_pass:
                confirm_pass = print("Password does not match, Please try again : ")
            else:
                # If all the information is correct the new user is then written in the text file "user.txt" where all the users usernames and passwords are stored.
                with open("user.txt", "a") as adding_user:
                    adding_user.write(f"\n{new_username}, {new_password}")
                    adding_user.close()

        # If the user selected "s" they can then see how many users and tasks are stored in the text files.
        if menu == 's':
            with open("user.txt", "r") as users:
                # Here the number of lines are calculated by findind the len of reading all the lines.
                num_users = len(users.readlines())

            with open("tasks.txt", "r") as tasks:
                # Here the number of lines are calculated by findind the len of reading all the lines.
                num_tasks = len(tasks.readlines())

            # Then thoses calculated data of how many number of lines there are in each text file is printing in an easy to read format for the user.
            print("_" * 50)
            print(f'''
Total number of users registered:       {num_users}
Total number of tasks assigned:        {num_tasks}\n''')
            print("_" * 50)

            # Then the text files are closed.
            users.close()
            tasks.close()

    # If the user is not the admin they get the follow menu displyed with limited access compared to the admin access.
    else:
        menu = input('''Select one of the following Options below:
    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit
: ''').lower()

    # If the user selected "a" they can then input the detials of the new task they wish to add to the text file "tasks.txt" where all the tasks are stored.
    if menu == 'a':
        # The user is prompted to input the details of the new task.
        user_assigned = input("Please enter the usersname, this task is assigned to : ")
        task_title = input("Please enter the title of the task the user is assigned to : ")
        task_descipt = input("Please enter the description of the task : ")
        due_date = input("Please enter the due date of this task in the Date/Month abbreviation/Year format : ")
        # Here the current date is imported via the library using the date function.
        today = date.today()
        current_date = today.strftime("%d %b %Y")
        # Then the new task is written in the text file in the correct format as specified.
        with open("tasks.txt", "a") as adding_task:
            adding_task.write(f"\n{user_assigned}, {task_title}, {task_descipt}, {current_date}, {due_date}, No")
            adding_task.close()

    # If the user selected "va" they can then view all the tasks in the text file "tasks.txt".
    elif menu == 'va':
        # This section reads each line and stores each line in a list object to be easily used later.
        with open("tasks.txt", "r+") as output:
            line = output.read()
            num_lines = line.split("\n")
            # Here the for loop then loops for the appropriate amount of lines and seperate each section of the line to be printing separately.
            for line in num_lines:
                line = line.split(", ")
                # Then each task is then printed in a easy to read format for the user.
                print("_" * 50)
                print(f'''
Task:               {line[1]}
Assigned to:       {line[0]}
Date assigned:     {line[3]}
Due date:           {line[4]}
Task Complete?      {line[5]}
Task description:\n {line[2]}\n''')
            print("_" * 50)
            output.close()


    # If the user selected "vm" they can only then view the tasks they are assigned to.
    elif menu == 'vm':
        # This section reads each line and stores each line in a list object to be easily used later.
        with open("tasks.txt", "r") as output:
            line = output.read()
            num_lines = line.split("\n")
            # Here the for loop checks all the tasks and seperates each section of that line task to extract the users name assigned to the task.
            for line in num_lines:
                line = line.split(", ")
                # Then the if statement checks to see if the username of the user who is logged in, corresponds to the username assigned to the task.
                if line[0] == user_login_name:
                    # Then each task that corresponds to the user is then printed in a easy to read format.
                    print("_" * 50)
                    print(f'''
Task:               {line[1]}
Assigned to:       {line[0]}
Date assigned:     {line[3]}
Due date:           {line[4]}
Task Complete?      {line[5]}
Task description:\n {line[2]}''')
            print("_" * 50)
            output.close()

    # If the user is finsihed working with the program they can then simply exit by selecting "e".
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    # If the user types in the incorrect selection they will be informed and will be given the menu again.
    else:
        print("You have made a wrong choice, Please Try again")
