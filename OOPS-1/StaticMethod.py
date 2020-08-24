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

s1=Student() #instance
s1.welcome()  #remove one func to avoid ambiguity