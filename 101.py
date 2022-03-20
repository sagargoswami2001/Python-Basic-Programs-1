# Faulty Calculator
operator = input("Enter Operator: ")
val1 = int(input("Enter First Operand: "))
val2 = int(input("Enter Second Operand: "))
if operator =="+":
    if val1 == 56 and val2 == 9:
        print("77")
    else:
        print("Sum is: ", val1 + val2)
if operator =="-":
    print("Substract is: ", val1 - val2)
if operator =="*":
    if val1 == 45 and val2 == 3:
        print("555")
    else:
        print("Multiply is: ", val1*val2)
if operator =="/":
    if val1 == 56 and val2 == 6:
        print("4")
    else:
        print("Divide is: ",float(val1/val2))
    
    
#int = 3
#print(int)
#print(type(int))
#
#int = float(1.0)
#print(type(int))
#print(int)

# D = {'sagar': '12.12.2000',
#      'mohit': '14.52.3000',
#      'prakash': '45.15.6000',
# }

# print("Enter Your Key: ")
# type = input()
# print(D[type])

# name = input("Enter the Name: ")
# print(D[name])

# Dict = {}
# key = input("type key for dict: ")
# value = int(input("Type the value: "))
# Dict [key] = value
# print (Dict)

# a  = input("Enter a Single Word(S,M,V,S,P,K): ")
# d = {"S" : "Hello" , 'M' : 'Sagar' , "V" : "Chutiya " , 'S' : "Kese" , 'P' : 'Ho' , 'K' : 'Sab Badiya'}
# if a in d['S']:
#     print(d["S"])

# dict1 = {"sagar" : "Sagar is a Python Programmer", "mohit" : "mohit is a good boy"}
# while(1):
#     d=input("Enter Your Key: ")
#     for key,value in dict1.items():
#         if key==d:
#             print(dict1[d])
#             break

# d1 = {"Sagar" : "My Name is Sagar" , "Mohit" : "My Second Name is Mohit"}
# a = input("Enter Your Key: ")
# b=a.capitalize()
# print(b," = ",d1[b])