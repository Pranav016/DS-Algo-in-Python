class student:
    institution="abc"
    course="IT"

    def __init__(self, name, age):  # instance function/ constructor
        self.name=name
        self.age=age
    
    @classmethod  # class decorators   
    # class method is used when i am interacting with the class variables and got nothing to do with the instance variables
    # the changes done using this method will be common for all class instances

    def change(cls, course)  # by default they recieve class as argument and by convention its named cls
        cls.course="CSE"

    @staticmethod 
    #static method is used when you dont want to add or manipulate any instance variables, just perform some tasks that is why it is called utility method
    def sum(a,b):
        return a+b

