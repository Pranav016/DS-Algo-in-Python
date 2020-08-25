class father:

    def __init__(self,name):
        self.name=name
    
    @staticmethod
    def print():
        print("Father class called")

class mother:

    def __init__(self,name):
        self.name=name
    
    @staticmethod
    def print():
        print("Father class called")

class child(father,mother): # multiple inheritance

    def __init__(self,name):
        super().__init__(name)

    def printChild(self):
        print(self.name)
        self.print() # here we can see that the father class is called based on the order of inheritance

c=child("Rohan")
c.printChild()
