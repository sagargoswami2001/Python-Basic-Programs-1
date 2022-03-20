# Write a Python Program to display your details like name,age,address in three different lines.

def personal_details():
    name, age = "Sagar Goswami",21
    address = "Bangalore, Karnataka, India"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

personal_details()