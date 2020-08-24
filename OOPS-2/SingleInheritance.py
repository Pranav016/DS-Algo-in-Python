class animal:
    def __init__(self,color):
        self.color=color

class Dog(animal): # single inheritance
    def __init__(self,color,breed):
        super().__init__(color) # calling the init func of parent/ super class
        self.breed=breed

    def print_details(self):
        print(self.color)
        print(self.breed)

d=Dog("red","Bulldog")
d.print_details()