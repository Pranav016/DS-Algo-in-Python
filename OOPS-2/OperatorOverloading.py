# going to perform addition of two complex numbers
import math
class operator:

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __add__(self,other): #this is the function that we have to overload if we want to overload the '+' operator
        return self.a + other.a ,self.b + other.b

    def __str__(self): # this function is invoked when we call a print statement
        return self.a,self.b

    def __lt__(self,other): # operator overloading for '<' operator for a complex no
        return math.sqrt(self.a**2+self.b**2) < math.sqrt(other.a**2+other.b**2)

o1=operator(1,2)
o2=operator(3,4)
o3=o1+o2
print(o3)
print(o2<o3)