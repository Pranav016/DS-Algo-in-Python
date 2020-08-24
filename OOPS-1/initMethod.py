class Student:
    def __init__(self, name, age, roll):  # this method is just like a cunstructor in cpp, it gets called automatically when we create an object of the class

        self.name=name  # instance variables are made here
        self.age=age
        self.roll=roll


s1=Student("Pranav",20,8122)
print(s1.__dict__)

s2=Student("Rohan",20,8123)
print(s2.__dict__)