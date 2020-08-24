# this is just for revision and reference purpose

# class attribute- present in every instance of the class
# instance attribute - present in that particular instance only



class Student:
    name="Pranav"  # class attribute 
    def student_details(self):  
        print(self.name)

    def set_param(self):  # this self parameter is used to recieve the instance(eg s1 or s2) during a func call
        self.school="Institute of Technology"

s1=Student()  # instance of the class
s1.age=20  # instance attribute
print(s1.__dict__)  # helps to check/ print the instance attributes
s1.student_details()


s2=Student()
s2.batch=3 # instance attribute 
s2.student_details() # class function to print the class attribute
print(s2.name)  # can also print class or instance attribute directly using '.' operator


s3=Student()
s3.name="Rohan"
print(s3.batch) # this will give error since batch attr is instance attr of s2/ not a class attr

print(s3.name)  # it first searches the instance attributes for 'name' and then checks the class attribute 
# hence the instance attribute will be printed


#$ not so imp methods
print(hasattr(s3, "name"))  # checks if the instance has that attr
print(getattr(s1, "age"))  # gets the attr
delattr(s3, "name") #deletes the attr