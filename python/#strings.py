#strings
print("hello world")
#
Name="archu"
Age=15
print("Name:",Name,"Age:",Age)

#special character in strings

print("Frst line\nSecond line")
print("Name:\tArchana")
print("She said\"Hello!\"")
print("c:\\program files\\python")

#
print("Hello", end="")
print("world")

print("Apple","banana","cherry",sep=",")

#string formatting
name="Archana"
age=22
print(f"{name} is {age} years old")
print("{} is {} years old".format(name,age))
price=49.35
quantity=2
print(f"Total:${price* quantity:.2f}")