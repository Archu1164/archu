#static method
class mathutils:
    @staticmethod
    def add(a,b):
        return a+b
    @staticmethod
    def mul(a,b):
        return a*b
print(mathutils.add(2,3))
print(mathutils.mul(2,3))
#example2-static method
class bike:
    def __init__(self,color):
        self.color=color
    @staticmethod
    def show():
        return "this is a bike"
my_bike=bike("black")
print(my_bike.color)
print(bike.show())
print(my_bike.show())
# Instance Variable vs Static Variable
class Student:
    school = "KITSW"
    def __init__(self, name):
        self.name = name

s1 = Student("Archana")
s2 = Student("Bunny")                 
print(s1.name)        # Instance variable
s1.name = "sahaswi"  # Modifying instance variable for s1
print(s2.name)        # Instance variable  
print(Student.school) # Static variable
print(s1.school)     # Accessing static variable via instance   

s1.school = "ZP High School"  # This creates an instance variable for s1     
