class vehicle:
    def __init__(self,color):
        self.__color=color

    def setColor(self,color):
        self.__color=color

    def getColor(self):
        return self.__color

class car(vehicle):
    def __init__(self,color,gears):
        #super().__init__(color)
        self.setColor(color)
        self.gears=gears
    
    def print_details(self):
        print(self.gears)
        print(self.getColor()) # cannot access color directly because it is a private member of the parent class so i access it using a method

s=car("red",6)
s.print_details()