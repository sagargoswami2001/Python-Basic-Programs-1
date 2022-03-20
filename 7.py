# Write a Python Program to Display the Current Date and Time.
import datetime
now = datetime.datetime.now()
print("Current Date and Time: ")
print(now.strftime("%d-%m-%Y %H:%M:%S")) 