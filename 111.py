# Create a List and Tuple with Comma Separated Numbers in Python.

values = input("Input Some Numbers: ")
list = values.split(",")
tuple = tuple(list)

print('List :' , list)
print('Tuple :' ,tuple)