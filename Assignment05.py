# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   phiphat pinyosophon, 07/31/2024, update script to read/write to json, replace list with dictionary
#   create try/except to catch errors and exception
#   <Your Name Here>,<Date>, <Activity>
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
# json_data: str = ''
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.
# parts: list = []

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file

try:
    file = open(FILE_NAME, "r")  # open json file in read mode
    students = json.load(file)  # load data from json file assign it to students list

except FileNotFoundError:  # creating exception where if there's no file, create one
    print("file not found, creating new file...")
    open(FILE_NAME, "w")
except Exception as e:
    print("file not found!", type(e), e, sep='\n')
finally:
    if file and not file.closed:  # Make sure the file is open before trying to close it.
        file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name[0].isalpha():  # chec if first name start with alphabet or not
                raise ValueError("First Name should start with a letter")

            student_last_name = input("Enter the student's last name: ")
            if not student_last_name[0].isalpha():  # check if last name start with alphabet or not
                raise ValueError("First Name should start with a letter")

            course_name = input("Enter the student's Course name: ")
            if not course_name[0].isalpha():  # check if course name start w alphabet or not
                raise ValueError("Course Name should start with a letter")
            student_data = {"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name}
            students.append(student_data)
            print(f'You have registered {student_data["FirstName"]}'
                  f' {student_data["LastName"]} for {student_data["CourseName"]}.')
        except ValueError as e:
            print(e)

        continue

    # Present the current data

    elif menu_choice == "2":
        print("-" * 50)
        for student in students:
            print(f'Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)
        continue

    # Save the data to a file

    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            #            json.dump(students, file, indent=1) #this indent=1 will hlep format json file when writing it out
            json.dump(students, file)  # writing students list to json
            for row in students:
                print(f'Student {row["FirstName"]} {row["LastName"]} is enrolled in {row["CourseName"]}')
            print(f"these data have been recorded in {FILE_NAME}")
        except Exception as e:
            print("error saving data to file")
            print(e)
        finally:
            if file and not file.closed:
                file.close()


    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
