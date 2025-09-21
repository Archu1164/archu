#1.how can you access the static variables of outer class from inner class 

#Static variables of the outer class are accessed in the inner class using the outer class name.
#This approach ensures proper referencing and avoids ambiguity between inner and outer scopes.
class Outer:
# Static (class) variable
    outer_static_var = "I am static in Outer"
    class Inner:
        def show(self):
            # Access static variable of outer class using class name
            print(Outer.outer_static_var)
# Create inner class object
inner_obj = Outer.Inner()
inner_obj.show()
#2.how can you access the static variables of outer class from inner class 
#To access the instance variable of an outer class from an inner class,
# you must pass the outer class instance to the inner class and use it to reference the variable.
class Outer:
    def __init__(self, value):
        # Instance variable of outer class
        self.outer_instance_var = value
    class Inner:
        def __init__(self, outer_obj):
            # Store reference of outer class object
            self.outer_obj = outer_obj
        def show(self):
            # Access outer class instance variable
            print(self.outer_obj.outer_instance_var)
# Create outer object
outer_obj = Outer("Hello from Outer Instance")
# Pass outer object reference to inner class
inner_obj = Outer.Inner(outer_obj)
inner_obj.show()
