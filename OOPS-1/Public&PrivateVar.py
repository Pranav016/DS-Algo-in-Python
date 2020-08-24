# we use double underscore "__" before a variable name to make it a private variable
# By default all variables are pubic
# we can only access private variables from within the class and not from outside the class
class Student:

    __institute="abc" # private class variable

    def __init__(self,name):
        self.__name=name # private instance variable

    def printStudent(self):
        print("Institute= ",self.__institute)
    
s=Student("Pranav")
s.printStudent()

# we cannot access/ change a private var from outside the class
print(s.institute) # will give error
print(s.name) # will give error
s.printStudent()
