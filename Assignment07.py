# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Phiphat Pinyosophon, 08/12/2024, update script to use Person and Student class, create validation for each attribute
#   Update the rest of the code to referencing object instances created from Student class whenever an object is created
#   <Your Name Here>,<Date>,<Activity>
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
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str = ''  # Hold the choice made by the user.


# TODO Create a Person Class
class Person:
    '''
    class created for Student to inherit first_name and last_name attributes
    '''
    # TODO Add first_name and last_name properties to the constructor (Done)
    def __init__(self, first_name: str = '', last_name: str = ""):
        '''
        creating property with constructor for person class with
        first_name and last_name as parameters to initialize
        :param first_name: string parameter we assign for first_name
        :param last_name: string parameter we assign for last_name
        '''
        self.first_name = first_name #(putting a single underscore here to make it "protected attribute"
        self.last_name = last_name #tell it that you're not supposed to access this outside a person class)

    # TODO Create a getter and setter for the first_name property (Done)
    @property  # this part is getter
    def first_name(self)->str:  # retrieve first_name
        '''
        getter, returns first_name as title
        :return: the first name formatted with first letter capitalized
        '''
        return self._first_name.title()  # return first_name, capitalize it and store it in memory

    @first_name.setter  # this part is setter
    def first_name(self, value: str)->None:
        '''
        setter, set first name and doing validaitons
        :param value: value to be set for first_name
        :return: None
        '''
        if value.isalpha() or value == '':  # check if the input is alphabetic, it's ok if not putting anything here as well
            self._first_name = value  # assign value to this private instance if it meets condition
        else:
            raise ValueError("First name must be alphabetic")  # raise this error if it'snot

    # TODO Create a getter and setter for the last_name property (Done)
    @property  # getter part
    def last_name(self)->str:  # retrieve last_name
        '''
        getter, returns last_name as title
        :return: the last name formatted with first letter capitalized
        '''
        return self._last_name.title()  # return last_name, make it capitalized and store it in memory

    @last_name.setter
    def last_name(self, value: str)->None:  # setter for last_name
        '''
         setter, set last name and doing validaitons
        :param value: value to be set for last_name
        :return: None
        '''
        if value.isalpha() or value == '':  # validation part, check if input is alphabetic, not putting anything is ok too
            self._last_name = value  # if meet condition, assign value to last_name private instance
        else:
            raise ValueError("Last name must be alphabetic")  # raise value error if not

    # TODO Override the __str__() method to return Person data (Done)
    def __str__(self):  # override string method and return Person data
        '''
        string function for person
        :return: string as csv value
        '''
        return f'{self.first_name},{self.last_name}'  # return first name and last name with a comma in between


# TODO Create a Student class the inherits from the Person class (Done)
class Student(Person):
    '''
    class created to inherit first_name and last_name attributes from Person Superclass, this one has course_name
    '''

    # TODO call to the Person constructor and pass it the first_name and last_name data (Done)
    def __init__(self, first_name: str = '', last_name: str = '', course_name: str = ''):
        '''
        inherit first_name and last_name from Person class, construct course_name property
        :param first_name: string parameter inheriting for first_name parameter from Person class
        :param last_name: string parameter inheriting for last_name parameter from Person class
        :param course_name: string parameter assigned for course_name
        '''
        super().__init__(first_name=first_name, last_name=last_name)
        # TODO add a assignment to the course_name property using the course_name parameter (Done)
        self.course_name = course_name

    # TODO add the getter for course_name (Done)
    @property  # getter
    def course_name(self)->str:  # retrieving course_name
        '''
        getter, returns course_name as title
        :return: course name formatted with first letter capitalized
        '''
        return self.__course_name.title()  # return course_name, capitalize it and store in memory

    # TODO add the setter for course_name (Done)
    @course_name.setter  # setter
    def course_name(self, value: str):  # course_name validation
        '''
         setter, set course name and doing validaitons
        :param value: value to be set for course_name
        :return: None
        '''
        # use for loop to check for each character in value string,
        # if any of them is a special character, raise ValueError
        if all(char.isalnum() or char.isspace() for char in value) or value == '':
            # if each letter is alphanumeric, or white space, or nothing is put there, return true
            self.__course_name = value  # and value will be assigned to course_name
        else:
            raise ValueError("course name must be letters")

    # TODO Override the __str__() method to return the Student data (Done)
    def __str__(self):
        '''
        string function for Student
        :return:
        '''
        result = super().__str__()  # inheriting this string method from Person Superclass
        return f'{result},{self.course_name}'  # combine inherited string from Superclass to course_name


# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads data from a json file and map its dictionary to parameters created with
        constructor from student_obj, which is an object instance from Student class.

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        phiphat p, 08/11/2024 mapping parameters from Student to json dictionary

        :param file_name: string data with name of file to read from
        :param student_data: list of dictionary rows to be filled with file data

        :return: list
        """

        try:
            file = open(file_name, "r")
            list_of_dict_data = json.load(file)  # store list of dictionary from json to here
            for student in list_of_dict_data:
                student_obj: Student = Student(first_name=student["FirstName"],
                                               last_name=student["LastName"],
                                               course_name=student["CourseName"])
                student_data.append(student_obj)
            file.close()
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)

        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        phiphat 08/12/2024 mapping parameters from Student to json dictionary

        :param file_name: string data with name of file to write to
        :param student_data: list of dictionary rows to be writen to the file

        :return: None
        """

        try:
            list_of_dict_data: list = []
            for student in student_data:
                student_json: dict = {"FirstName": student.first_name,
                                      "LastName": student.last_name,
                                      "CourseName": student.course_name}
                list_of_dict_data.append(student_json)
            file = open(file_name, "w")
            json.dump(list_of_dict_data, file)
            file.close()
            IO.output_student_and_course_names(student_data=student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message, error=e)
        finally:
            if file.closed == False:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    RRoot,1.2.2030,Added menu output and input functions
    RRoot,1.3.2030,Added a function to display the data
    RRoot,1.4.2030,Added a function to display custom error messages
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function


        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list):
        """ This function displays the student and course names to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        phiphat, 08/12/2024, update it to use reference from object instance from Student class

        :param student_data: list of dictionary rows to be displayed

        :return: None
        """

        print("-" * 50)
        for student in student_data:
            print(f'Student {student.first_name} '
                  f'{student.last_name} is enrolled in {student.course_name}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the student's first name and last name, with a course name from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        phiphat, 08/12/2024, mapping each input from user to related parameter from Student class

        :param student_data: list of dictionary rows to be filled with input data

        :return: list
        """

        try:
            student = Student()
            student.first_name = input("Enter the student's first name: ")
            student.last_name = input("Enter the student's last name: ")
            student.course_name = input("Please enter the name of the course: ")
            student_data.append(student)
            print()
            print(f"You have registered {student.first_name} {student.last_name} for {student.course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="One of the values was the correct type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data


# Start of main body

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while True:

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_names(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
