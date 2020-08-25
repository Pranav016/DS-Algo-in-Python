# In python, protected variables are same as public var. They are just there to ensure that we are using them less outside the class

class vehicle:
    def __init__(self,color):
        self._color=color  # we use a single underscore '_' to declare protected variables

    def setColor(self,color):
        self._color=color

    def getColor(self):
        return self._color

class car(vehicle):
    def __init__(self,color,gears):
        #super().__init__(color)
        #self.setColor(color)
        self._color=color
        self.gears=gears
    
    def print_details(self):
        print(self.gears)
        #print(self.getColor())
        print(self._color)

s=car("red",6)
s.print_details()