#------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# LTurner ,8.2.21,Added code to start assignment 05 (read file, change to lines, and print rows)
#LTurner, 8.3.21, Working on Options 1,2 and 3 in the menu
#LTurner, 8.4.21, Worked on Options 4,5 in the menu
#LTurner, 8.5.21, cleaning up the code and adding extra notes
#LTurner, 8.6.21, created a new remove row script after watching zoom
#LTurner, 8.7.21, continuing to check code and clean before GIT HUB entry
#                 added a try and except for reading file to dictionary
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
filename1 = "ToDoList.txt" #string for file name
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
strItem = ""
strPriority = ""
count = ""
exitStr = ""


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
try:
    objFile = open(filename1, 'r')
    for row in objFile:
        lstRow = row.split(',')
        dicRow = {'Task':lstRow[0], 'Priority':lstRow[1].strip()}
        #print(dicRow['Task']+','+dicRow['Priority'])
        lstTable.append(dicRow)
    objFile.close()
except:
    print('Unable to find or read the requested file. List will start empty.')
    print('If you want to create a list text file, please save using menu option 4.')

#Loop to go through the menu options and allow the user to keep entering inputs.

while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
# Asking user for input to pick a menu option
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    # Loop to go through all the rows and print in simple form (task, priority)
    if (strChoice.strip() == '1'):
        print('Here is a current listing of To Dos:')
        for row in lstTable:
            print(row['Task'],',',row['Priority'])
        continue

    # Step 4 Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strItem = str(input('Please enter a task: '))
        strPriority = str(input('Please enter a priority for the task: '))
        dicRow = {'Task':strItem,'Priority':strPriority}
        lstTable.append(dicRow)
        print(strItem, ",", strPriority,' was added to the To Do List.')
        continue

    # Step 5 - Remove a new item from the list/Table
    # Uses a loop to check all the row for the task or priority input
    # Use a counter to check to see if a task was completed or not
    # With the counter variable, determine what happened in the first if loop
    # print final statement to the user that nothing was deleted if the counter still equals 1
    elif (strChoice.strip() == '3'):
        removeItem = (input('Please enter the task or priority you wish to delete: '))
        count = 1
        for row in lstTable:
            if row['Task'].lower() == removeItem.lower():
                lstTable.remove(row)
                print('Task has been deleted.')
                count = count+1
            elif row['Priority'].lower() == removeItem.lower():
                lstTable.remove(row)
                print('Priority has been deleted.')
                count = count+1
            else:
                continue

        #second if statement to check to see if the script found a row to remove
        #if no row removed, it lets to user know it wasn't found
        if count == 1:
            print('Your task or priority entered was not found in the list. ')
            print('No task or priority was deleted.')
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(filename1, 'w')
        for row in lstTable:
            objFile.write(row['Task']+','+row['Priority']+'\n')
        objFile.close()
        print('The To Do List has been saved to file.')

   # Step 7 - Exit the script if the user selects yes, "y"
    elif (strChoice.strip() == '5'):
        exitStr = str(input('Do you want to exit? (y or n): '))
        if exitStr.lower() == "y":
            print('Thank you for using the program.')
            break  # and Exit the program
        else:
            print('The menu will restart.')
            continue
    #Step 8 - Final else statement to allow the user to enter a menu option if 1-5 was not entered
    else:
        print('Please enter a menu option. (1-5)')
        print('To exit use menu option 5.')
        continue

