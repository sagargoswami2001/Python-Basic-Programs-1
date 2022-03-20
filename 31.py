#Write a Python Program to print the calendar of a given month and year.
import calendar
y = int(input("Input the Year: "))
m = int(input("Input the Month: "))
print(calendar.month(y, m))
