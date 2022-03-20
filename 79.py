# Write a Python Program to Convert the Distance (in feet) to inches,yards and miles.

d_ft = int(input("Input Distance in Feet: "))
d_inches = d_ft * 12
d_yards = d_ft / 3.0
d_miles = d_ft / 5280.0

print("The Distance in Inches is %i Inches." % d_inches)
print("The Distance in Yards is %.2f Yards." %d_yards)
print("The Distance in Miles is %.2f Miles." %d_miles)