# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Phiphat, 08/07/2024, modify the script with classes and functions
# ------------------------------------------------------------------------------------------ #
import json
from json import JSONDecodeError
from typing import TextIO

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
FILE_NAME: str = "Enrollments.json"
#variable
students: list = []

class FileProcessor:
    @staticmethod
    def read_data_from_file(filename: str, student_data: list) -> list:
        '''
        get data from json file and store it in a list called student data
        :param filename: refer to json file
        :param student_data: a list created to store data from json file
        :return: will return a list
        '''
        try:
            file = open(filename, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_message("Text file must exist before running this script!\n", e)
            file = open(filename, "w")
            json.dump(student_data, file)
        except JSONDecodeError as e:
            IO.output_error_message("--Technical Information--", e)
            file = open(filename, "w")
            json.dump(student_data, file)
        except Exception as e:
            IO.output_error_message("Unhandle Exception", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(filename: str, student_data: list):
        '''
        will write data to json file
        :param filename: json file
        :param student_data: data received from other function to write to json file
        :return: None
        '''

        try:
            file = open(filename, "w")
            json.dump(student_data, file)

            file.close()
            IO.output_message("The following data was saved to file!")
            for student in student_data:
                IO.output_message(f'Student {student["FirstName"]} '
                                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except Exception as e:
            if file.closed == False:
                file.close()
            IO.output_error_message("Error: There was a problem with writing to the file.", e)


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
class IO:
    @staticmethod
    def output_message(message: str):
        '''
        print message
        :param message: string message to print
        :return: None
        '''
        print(message)

    @staticmethod
    def output_error_message(message: str, error: Exception = None):
        '''
        print error message when there's exception
        :param message: string messsage to print
        :param error: Exception
        :return: None
        '''
        if Exception is not None:
            print("--technical information--")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def input_menu_choice(menu:str)->str:
        '''
        get user input when display menu
        :param menu: MENU variable to display
        :return: string 1,2,3,4 as choices user can make
        '''
        return input(menu)

    @staticmethod
    def add_data_to_table(student_data: list)->list:
        '''
        get user input and add them to student data list
        :param student_data: a list created to store and adding data from user input
        :return: return a list of student data
        '''
        student_first_name: str = ''
        student_last_name : str = ''
        course_name: str = ''
        student_row: dict = {}
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The First name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_row = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(student_row)
            IO.output_message(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_message("-- Technical Error Message -- ", e)  # Prints the custom message

        except Exception as e:
            IO.output_error_message("Error: There was a problem with your entered data.", e)

        return student_data

    @staticmethod
    def output_student_courses(student_data: list)->None:
        '''
        display student name, last name, and courses
        :param student_data: list of student data returned from other function
        :return: None
        '''
        IO.output_message("-" * 50)

        for student in student_data:
            IO.output_message(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        IO.output_message("-" * 50)

#get data returned from read_data_from_file so it can be used in other function, as Python is executed from top-down
#this has to be done here so other function can have access to it
students = FileProcessor.read_data_from_file(filename = FILE_NAME, student_data = students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_message('\n')
    IO.output_message("what do you want to do?")
    menu_choice = IO.input_menu_choice(menu = MENU)
    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        IO.add_data_to_table(student_data = students)
    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(student_data = students)

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(filename = FILE_NAME, student_data = students)
    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        IO.output_message("Please only choose option 1, 2, 3, or 4")

IO.output_message("Program Ended")
