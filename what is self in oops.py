#>self :
#self refers to the current object of the class.
#It is used to access attributes and methods of the object.
#It is always the first parameter in instance methods.
#You don’t pass it when calling a method; Python handles it automatically.
#It’s a convention, not a keyword — but it’s best to use self.
#It helps to store data unique to each object.

class Person:
    def __init__(self, name):
        self.name = name  # store name in the object
    def greet(self):
        print("Hello, my name is", self.name)
# Create an object
person1 = Person("Archana")
# Call the method
person1.greet()

