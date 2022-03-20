# Practice...
# x = 5
# x = complex(x)

# txt = "Sagar"
# print(txt[0])

# txt = "Hello"
# x = txt[2:5]
# print(x)

# txt = " Hello World "
# x = txt.strip()

# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age))

# print(bool("abc"))

# if 5 == 10 or 4 == 4:
#   print("At least one of the statements is true")

# fruits = ["apple", "banana", "cherry"]
# fruits[0] = "kiwi"
# print(fruits)

# fruits = ["apple", "banana", "cherry"]
# fruits.append("orange")

# fruits = ["apple", "banana", "cherry"]
# fruits.insert(1,"lemon")
# print(fruits)

# fruits = ["apple", "banana", "cherry"]
# print(fruits[-1])

# fruits = {"apple", "banana", "cherry"}
# more_fruits = ["orange", "mango", "grapes"]
# fruits.update(more_fruits)

# Use the get method to print the value of the "model" key of the car dictionary.
# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(car.get("model"))

# Change the "year" value from 1964 to 2020.
# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car["year"] = 2020

# Add the key/value pair "color" : "red" to the car dictionary.
# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car["color"] = "red"
# print(car)

# Use the correct short hand syntax to write the following conditional expression in one line:
# print("Yes") if 5 > 2 else print("No")

'''
If you do not know the number of arguments that will be passed into your function, there is a prefix 
you can add in the function definition, which prefix?
'''
# def my_function(*kids):
#   print("The youngest child is " + kids[2])

'''
If you do not know the number of keyword arguments that will be passed into your function, 
there is a prefix you can add in the function definition, which prefix?
'''
# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# Assign Multiple Values //Variable
# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)

# Output Variables
# x = "Python is "
# y = "awesome"
# z =  x + y
# print(z)

# Create a variable inside a function, with the same name as the global variable
# x = "awesome"

# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)

# myfunc()

# print("Python is " + x)

# If you use the global keyword, the variable belongs to the global scope:
# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)

# Setting the Data Type
x = 1j
print(type(x))

# x = range(6)
# print(type(x))

# x = frozenset({"apple", "banana", "cherry"})
# print(type(x))

# x = b"Hello"
# print(type(x))

# x = bytearray(5)
# print(type(x))

# x = memoryview(bytes(5))
# print(type(x))

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price))