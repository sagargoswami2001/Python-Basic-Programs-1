'''Write a Python Program to Convert Pressure in Kilopascals to Pounds per Square Inch, a Millimeter of Mercury (mmHg) and
Atmosphere Pressure.'''

kpa = float(input("Input Pressure in Kilopascals: "))
psi = kpa / 6.89475729
mmhg = kpa * 760 / 101.325
atm = kpa / 101.325
print("The Pressure in Pounds per Square Inch: %.2f Psi" % (psi))
print("The Pressure in Millimeter of Mercury: %.2f mmHg" % (mmhg))
print("Atmosphere Pressure: %.2f ATM" % (atm))