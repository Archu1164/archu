#list
fruits=["apple","banana","cherry","date"]

first=fruits[0]
second=fruits[1]
third=fruits[2]
last=fruits[-1]
second_last=fruits[-2]
third_last=fruits[-3]
#
if "apple" in fruits:
    print("Apple is present")
print("first:",first)
print("second:",second)
print("third:",third)
print("last:",last)
print("second_last:",second_last)
print("third_last:",third_last)
#
print(len(fruits))
print(first)
print(second)
print(third)
print(last)
print(second_last)
print(third_last)
#
print(fruits[0])
print(fruits[-3])

fruits.remove("banana")
print(fruits)
print(len(fruits))

#
fruits.append("orange")
print(fruits)

fruits.insert(2,"mango")
print(fruits)

more_fruits=["grapes","pear"]
fruits.extend(more_fruits)
print(fruits)

#
last=fruits.pop()
print(last)

if "banana" in fruits:
 fruits.remove("banana")
print("after apppend:",fruits)

fruits.clear()
print(fruits)

#numbers
numbers=[3,1,4,1,5,6,9,2]
print("list:",numbers)
#access elements
print("first element:", numbers[0])
print("last element:", numbers[-1])
#length
print("length:",len(numbers))

#


