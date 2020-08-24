# Polymorphism means one method can take many forms
# here print function is printing the vehicle attr and also the car attr

class vehicle:
    def __init__(self,color):
        self.__color=color

    def setColor(self,color):
        self.__color=color

    def print(self):
        print(self.__color)

class car(vehicle):
    def __init__(self,color,gears):
        #super().__init__(color)
        self.setColor(color)
        self.gears=gears
    
    def print(self):
        #print(self.print())   # this will search the print function first within the class car and then in its parent class
        # in this case it will go in infinite recursion so to avoid this we can use-
        super().print()
        print(self.gears)

s=car("red",6)
s.print() # searches for print in class car and if not found then only in its parent class vehicle