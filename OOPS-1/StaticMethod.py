class Student:
    name="Pranav"
    age=18

    def student_details(self):
        print(self.name, self.age)

    # this will give error because the function by default expects am argument(instance)
    def welcome():  
        print("Hello! Welcome to school")

    
    # to fix this we can use a static method decorator over a func in which the instance argument is not required
    @staticmethod
    def welcome():  
        print("Hello! Welcome to school")


    # we can use a class method to change the class attributes that is common for all the instances
    @classmethod
    def change_age(cls,age): # default argument is the class name - cls by convention
        cls.age=age

s1=Student() #instance
s1.welcome()  #remove one func to avoid ambiguity

Student.change_age(19) # changes age in the class variable hence changed for all the instance variables 
print(s1.age)