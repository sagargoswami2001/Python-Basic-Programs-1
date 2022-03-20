# Write a Python Program to Convert all Units of Time into Seconds.

Days = int(input("Input Days: ")) * 3600 * 24
Hours = int(input("Input Hours: ")) * 3600
Minutes = int(input("Input Minutes: ")) * 60
Seconds = int(input("Input Seconds: "))

Time = Days + Hours + Minutes + Seconds

print("The Amounts of Seconds", Time)