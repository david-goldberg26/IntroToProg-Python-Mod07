''''
        Title: Assignment08
        Description: Script that uses classes, constructors, properties, and inheritance
        ChangeLog: (Who, When, What)
        RRoot,1.5.2030,Created Script
        David Goldberg, 5/20/2024, Attempt at Assignment 07

'''

import json
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
# Define the Data Constants
# FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

# Define the Variables 
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.
class Person:
    '''
    Class representing 'Person' Data
    
    Properties:
    student_first_name: person's first name
    student_last_name: person's last name
    '''

    def __init__(self, student_first_name: str = '', student_last_name: str = ''):     # allows us to set initial values to the class's attributes    
        self.student_first_name = student_first_name        #attribute set to student_first_name
        self.student_last_name = student_last_name      #attribute set to student_last_name

    @property
    def student_first_name(self):       # getter for student_first_name
        return self.__student_first_name.title()        # making fist_name a 'sectret' variable
    
    @student_first_name.setter      # when someone tries to set a value to first_name, it will call this method
    def student_first_name(self, value: str = ''):
        if value.isalpha() or value == '':      #checking if the input is letters only
            self.__student_first_name = value
        else:
            raise ValueError("the first name should not contain numbers")       # will raise value error if not all letters
        
    @property
    def student_last_name(self):        #getter for student_last_name
        return self.__student_last_name.title()     # sectret variable, first letter will be caps
    
    @student_last_name.setter       # when someone tries to set a value to last_name, it will call this method       
    def student_last_name(self, value:str):
        if value.isalpha() or value == '':      #checking if the input is letters only        
            self.__student_last_name = value
        else:
            raise ValueError("the first name should not contain numbers")       # will raise value error if not all letters
    
    def __str__(self):      # method that acts like a string function, will print first name and last name
        return f"{self.student_first_name},{self.student_last_name}"
        
class Student(Person):      # inherits person class to student class
    '''
    Class the represents student data
    
    Properties:
    student_first_name: person's first name
    student_last_name: person's last name
    course_name: student's course name
    '''
    def __init__(self, student_first_name:str = '', student_last_name: str='', course_name: str= ''):       #initializes the students first name, last name, and course name
        super().__init__(student_first_name=student_first_name, student_last_name=student_last_name)     # properties you will inherit from person class

        self.course_name = course_name      # add course_name attribute on top of what was inherited from person

    @property
    def course_name(self):      # getter for course_name
        return self.__course_name
    
    @course_name.setter     # setter for course_name
    def course_name(self, value: str):
        if value:       # check if the input contains something, if empty it will output a message to the user
            self.__course_name = value
        else:
            print("please input your course name")


    def __str__(self):      # User str method to output the instance of first name, last name, and course name
        return f'{self.student_first_name},{self.student_last_name},{self.course_name}'

class FileProcessor:
    '''
    Contains two functions that read in and write to a JSON File
    '''
    @staticmethod
    def read_data_from_file(file_name:str, student_data: list):   
        '''
        Function that reads in data from a JSON file and then into a dictionary
        :param file_name: A string indicating the file name
        :param student_data: dictionary from students inputs
        :return: list of student data

        ''' 
        file: TextIO = None 
        try:
            list_of_dictionary_data: list = []  # classes change the functionality of json, need to create a dictionary
            file = open(file_name, "r")     # open the file in read mode
            list_of_dictionary_data = json.load(file)
            for student in list_of_dictionary_data:
                new_student = Student(student_first_name=student["FirstName"], student_last_name=student["LastName"], course_name=student["CourseName"])        # create a constructor that calls the student class and associates keys with its attributes
                student_data.append(new_student)        # append read dictionary to the multi-dim list
            file.close()
            print("data retreived")
        except Exception as e:
            IO.output_error_message(message='text file not found\n', error = e)     # calling IO class for structured error
        finally:
            if file == False:
                file.close()
        return student_data
    
    @staticmethod
    def write_data_to_file(file_name:str, student_data:list):
        '''
        Function that reads the students dictionarties into the JSON File
        :param file_name: A string indicating the file name
        :param student_data: dictionary from students inputs

        '''
        try:
            list_of_dictionary_data = []
            for student in students:
                student_json: dict \
                = {"FirstName": student.student_first_name, "LastName":student.student_last_name, "CourseName":student.course_name}     # create a dictionary prior to writing it to the json file
                list_of_dictionary_data.append(student_json)
            file = open(file_name, "w")     # open a file to write to
            json.dump(list_of_dictionary_data, file)       # write the dictionary/dictionaries to the json file
            file.close()
            print("The following data was saved to file!\n")
            IO.output_student_courses(student_data=student_data)        # calling IO class to output inputs 
        except Exception as e:      # Structured error handling if any exceptions occur
            if file.closed == False:
                file.close()
            IO.output_error_message(message='There was a problem with writing the file', error=e)       # calling IO class for structured error
        finally:
            if file.closed == False:
                file.close()


    
class IO:
    '''
    Contains functions that deal with inputs and outputs
    Printing the Menu
    Selecting a Menu Choice
    Error handling
    inputting student data
    outputting student data
    '''
    @staticmethod
    def output_error_message(message:str, error: Exception = None):
        '''
        Function displays prints error statements
        :param message: string of data containing a message
        :param error: message that pertains to the Exception

        :return: None

        '''

        print(message)
        if error is not None:       #Print error messages from the exceptions 
            print('--- technical info--\n')
            print(error, error.__doc__, type(error), sep = '\n') 

    
    @staticmethod
    def output_menu(menu:str):
        '''
        Function Displays menu choices to students
        :param menu: student menu choice
        :return: None
        '''
        print('\n')
        print(menu)     # will print the menu
        print('\n')

    @staticmethod
    def input_menu_choice():
        '''
        Function allows students to input student choice
        :return: students string choice
        '''
        string_choice = input("Enter a choice from the menu: ")     #allows student to input the menu choice
        while string_choice not in ['1', '2', '3', '4']:        # checks if input is 1-4
            IO.output_error_message("Please enter an option between 1 and 4")       # calling IO class for structured error
            string_choice = input('Enter a valid menu choice: ')        # will ask the user again
        return string_choice

    @staticmethod
    def input_student_data(student_data:list):
        '''
        Function allows for students to input their names and courses
         :param student_data: list of dictionaries that are filled by students inputs
        :return: dictionary (list)
          '''
        try:
            new_student = Student()     # calling the student class to input the student's information
            new_student.student_first_name = input("Enter the student's first name: ")      # student will input first name
            new_student.student_last_name = input("Enter the student's last name: ")      # student will input first name
            new_student.course_name = input("Please enter the name of the course: ")
            student_data.append(new_student)
            print(f"You have registered {new_student.student_first_name} {new_student.student_last_name} for {new_student.course_name}.")
        except ValueError as e:
            IO.output_error_message(message= "inputted name is not the correct data type", error=e)     # calling IO class for structured error
        except Exception as e:
            IO.output_error_message(message= "Error: Problem with entering your data", error=e)     # calling IO class for structured error
        return student_data
    
    @staticmethod
    def output_student_courses(student_data:list = []):
        '''
        Function is to output the students compelete dictionary
        :param student_data: list of students inputs
        '''
        print("-" * 50)
        for student in student_data:
            print(f'student {student.student_first_name} ' 
                  f'{student.student_last_name} is enrolled in {student.course_name}')      # output students inputs when called
        print("-" * 50)


# Main Body

students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)       #calls the class and function necessary to read data 

while True:

    IO.output_menu(menu=MENU)       # calls IO class and a method to output the menu
    menu_choice = IO.input_menu_choice()        # calls IO class and a method to get students choice

    if menu_choice == "1":
        students = IO.input_student_data(students)      # if choice is 1 it will call the input method 
        continue

    elif menu_choice == "2":
        IO.output_student_courses(students)     # if choice is 2 it will call the output student method
        continue

    elif menu_choice == '3':
        FileProcessor.write_data_to_file(FILE_NAME, students)       #if choice is 3 it will call method to write to file
        continue

    elif menu_choice == '4':        # break out of the program and exit
        break

print('End of program')
        