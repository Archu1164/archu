#what is class and object
class Car:   # Class
    def __init__(self, brand, color):
        self.brand = brand      # Instance variable
        self.color = color
    def drive(self):
        print(f"{self.color} {self.brand} is driving")
# Create objects (instances)
car1 = Car("Toyota", "Red")
car2 = Car("BMW", "Black")
# Use objects
car1.drive()
car2.drive()

#2what is reference variable
class student:
    name="name"
    age=20
archana=student()
rachana=archana
print(rachana.age)
print(archana.age)
#instance variable
class Student:
    def __init__(self, name, age):
        self.name = name      # Instance variable
        self.age = age        # Instance variable
s1 = Student("Archana", 20)
s2 = Student("Rachana", 22)
print(s1.name, s1.age)  # Archana 20
print(s2.name, s2.age)  # Rachana 22

#local variable
class Student:
    def show(self):
        message = "Hello from method"   # Local variable
        print(message)
s = Student()
s.show()      

#static variable
class Student:
    college = "ABC University"   # static variable
    def __init__(self, name):
        self.name = name   # instance variable
s1 = Student("Archana")
s2 = Student("Rachana")
print(s1.college)      # ABC University
print(s2.college)      # ABC University
print(Student.college) # ABC University

## Where we can declare Instance Variables
#inside constructor
#inside instance method 
#outside the class using object reference variable
class Student:
    def __init__(self, name):
        self.name = name
    # instance method example of declaring instance variable
    def set_age(self, age):
        self.age = age
obj = Student("Archana")
obj.set_age(21)
#declaring instance variable outside the class using object reference variable
obj.age=20  
print(obj.name)  # Output:Archana
print(obj.age)   # Output: 20   
obj2 = Student("sindhu")
obj2.set_age(22)
print(obj2.name)  # Output: sindhu
print(obj2.age)   # Output: 22
obj3 = Student("Saadh")
obj3.set_age(20)
print(obj3.name)  # Output: Saadh
print(obj3.age)   # Output: 20
print(obj.__dict__)  
print(obj2.__dict__)
print(obj3.__dict__) 
del obj.age  
del obj2.age  
del obj3.age  
print(obj.__dict__)  
print(obj2.__dict__)  
print(obj3.__dict__) 