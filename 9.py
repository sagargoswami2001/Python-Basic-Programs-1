'''
Write a Python Program Which Accepts a Sequence of Comma - Separated Numbers from User and Generate a list
and a tuple with those numbers.
'''
values = input("Input Some Comma Seprated Number: ")
list = values.split(",")
tuple = tuple(list)
print('List: ',list)
print('Tuple: ',tuple)