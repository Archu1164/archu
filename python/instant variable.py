#Instance Variables
#Belong to each object (instance) of a class.
#Defined inside the constructor (__init__) or other instance methods using self.
#Each object gets its own copy of instance variables.
#Example:
class Student:
    def __init__(self, name, age):
        self.name = name        # Instance variable
        self.age = age          # Instance variable

s1 = Student("Archana", 21)
s2 = Student("Meera", 22)

print(s1.name, s1.age)  # Archana 21
print(s2.name, s2.age)  # Meera 22
