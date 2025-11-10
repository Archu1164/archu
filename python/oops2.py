# Various Places to declare Static Variables
class Student:
    school = "ZP School"  # Inside class
    def __init__(self):
        Student.school = "ABC School"  # Inside constructor
    def set_school(self):
        Student.school = "New School"  # Inside method
# Where we can modify the Value of Static Variable     
class Student:
    school="ZP School"
    def change_school(self,new_name):
     Student.school=new_name 
s1=Student()
s2=Student()
print(Student.school)
s1.change_school("MET")
print(Student.school)
#how to delete static variables of class
class Student:
    school="ZP school"
del Student.school
#passing members from one class to another class
class A:
    def __init__(self,value):
        self.value=value
class B:
    def __init__(self,obj):
        self.obj=obj
a=A(5)
b=B(a)
print(b.obj.value)
#inner class
class outer:
    class inner:
        def show(self):
            print("inner class method")
o=outer()
i=outer.inner()
i.show()
#garbage collection
import gc
print(gc.isenabled())
#destructors
class obj:
    def __del__(self):
       print("destructor called")
o=obj()
del o


